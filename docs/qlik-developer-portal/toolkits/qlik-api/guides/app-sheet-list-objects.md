---
source: https://qlik.dev/toolkits/qlik-api/guides/app-sheet-list-objects/
last_updated: 2026-01-19T14:21:00Z
---

# Obtain a list of sheets and objects on that sheet from an analytics app

This guide shows you how to explore the internal structure of sheet objects in a Qlik Sense app
programmatically using the Qlik API TypeScript library (`@qlik/api`).

Building on the [app sheet list example](https://qlik.dev/toolkits/qlik-api/examples/app-sheet-list/), you'll learn how to:

- Understand the relationships between sheets and their child objects
- Retrieve the list of objects belonging to a sheet
- Resolve objects down to their root visualizations through recursive traversal
- Handle container objects that nest other visualizations
- Identify and resolve master item references
- Prevent infinite loops when traversing circular references
- Track master item usage across sheets
- Generate visualization type distribution reports
- Create comprehensive app inventories for analysis

Use this guide to build tools that introspect and automate app management.

The complete working code for this example is available in the [qlik-cloud-examples repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/examples/app-sheet-list-objects).

## Prerequisites

- Node.js 22+ and npm
- Access to a Qlik Cloud tenant
- OAuth client credentials (Client ID and Secret with `user_default` scopes)
- A Qlik Sense app with sheets and visualizations (or use the [Qlik Cloud App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)
  as this contains both master items and container objects)

## Understanding generic objects and their relationships

In Qlik Sense, [generic objects](https://qlik.dev/embed/foundational-knowledge/app-anatomy/generic-object-model/) are flexible JSON
structures representing app components (sheets, visualizations, bookmarks, master items, etc.).
Generic objects are identified by their `qType` property and can contain or reference other generic objects.

There's no explicit parent-child structure in Qlik apps. Instead, objects form
relationships
through specific properties:

- **`cells`** - Sheet properties contain a `cells` array listing the direct children on the sheet
- **`qChildList`** - Object layouts may include this to reference nested objects (for containers)
- **`qExtendsId`** - Objects based on master items use this to reference the master object definition

When working with visualizations, you'll encounter these common object types:

- **Sheets** - Generic objects with `qType: "sheet"` that contain child visualizations in their `cells` property
- **Visualizations** - Chart objects (bar chart, KPI, table, etc.) identified by their `visualization` property
- **Container objects** - Visualizations that hold other visualizations (they have `cells` in properties and/or children
  in layout)
- **Master items** - Reusable object definitions referenced via `qExtendsId`
- **Extension objects** - Custom visualizations with their own `visualization` identifier

The key challenge is resolving objects that reference or contain other objects. This guide shows you how to traverse
these relationships to find all visualizations and understand their definitions.

## Set up environment configuration

Create a `.env` file in your project root:

```bash
QLIK_HOST=your-tenant.region.qlikcloud.com
QLIK_CLIENT_ID=your-client-id
QLIK_CLIENT_SECRET=your-client-secret
QLIK_APP_ID=your-app-id
SAVE_LAYOUTS=false
```

Set `SAVE_LAYOUTS=true` if you want to save the layout JSON for each object to disk for inspection.

## Initialize the Qlik API Client with OAuth2

```ts
import 'dotenv/config';
import { auth, qix } from "@qlik/api";
import fs from 'fs';
import path from 'path';

const hostConfig = {
  authType: "oauth2",
  host: process.env.QLIK_HOST,
  clientId: process.env.QLIK_CLIENT_ID,
  clientSecret: process.env.QLIK_CLIENT_SECRET,
};

auth.setDefaultHostConfig(hostConfig);
```

This example uses OAuth2 M2M (machine-to-machine) authentication, which is ideal for server-side scripts and automation
tools.

**Why OAuth instead of API Key?**

This example requires a WebSocket connection to the Qlik Engine API. While API keys work, they require configuring a
web integration for WebSocket connections.
OAuth provides direct WebSocket access without additional configuration.

## Open the app session

```ts
const appId = process.env.QLIK_APP_ID;
const session = qix.openAppSession({ appId, withoutData: true });
const app = await session.getDoc();
```

The `withoutData: true` option opens the app without loading data into memory, which improves performance when you only
need to inspect the app structure.

## Understand how sheet children are stored

Unlike what you might expect from the sheet list, the actual child objects on a sheet are stored in the sheet's
**properties**, not its layout:

```ts
// Get the sheet list (contains basic metadata)
const sheetList = await app.getSheetList();

for (const sheet of sheetList) {
  console.log(`Sheet: ${sheet.qMeta.title}`);
  
  // Get the actual sheet object
  const sheetObject = await app.getObject(sheet.qInfo.qId);
  
  // Get properties - this is where children are stored
  const sheetProperties = await sheetObject.getProperties();
  
  // The children are in the cells property
  const children = sheetProperties.cells || [];
  
  console.log(`└─ Sheet has ${children.length} object(s)`);
  
  for (const child of children) {
    console.log(`   Object ID: ${child.name}`);
  }
}
```

- `getSheetList()` returns lightweight metadata including `qChildList`, but this doesn't contain all the information
- To get the actual child object IDs, you must call `getObject()` and `getProperties()` on the sheet
- Sheet children are in the `cells[]` array in properties, where each cell has a `name` property containing the object
  ID
- Properties contain the **configuration** (what's defined), while layout contains the **runtime state** (what's
  evaluated).
  For more information, see [Properties vs layout: understanding the difference](#properties-vs-layout-understanding-the-difference).

## Recursively traverse child objects

Some objects contain other objects (containers). You need to recursively traverse these relationships:

```ts
// Track visited objects to prevent infinite loops
const visitedObjects = new Set();

async function getChildObjects(objectId, indent = '  ') {
  // Prevent circular references
  if (visitedObjects.has(objectId)) {
    return 0;
  }
  
  visitedObjects.add(objectId);
  
  try {
    const childObject = await app.getObject(objectId);
    const childProperties = await childObject.getProperties();
    const layout = await childObject.getLayout();
    
    // Extract title and type
    const title = layout.title || layout.qMeta?.title || 'Untitled';
    const type = layout.visualization;
    
    console.log(`${indent}Object ID: ${objectId}`);
    console.log(`${indent}  Name: ${title}`);
    console.log(`${indent}  Type: ${type}`);
    
    let childCount = 0;
    const childIds = new Set();
    
    // Check properties for container cells
    if (childProperties.cells && childProperties.cells.length > 0) {
      for (const cell of childProperties.cells) {
        if (cell.name) {
          childIds.add(cell.name);
        }
      }
    }
    
    // Check layout for child list
    if (layout.qChildList && layout.qChildList.qItems) {
      for (const layoutChild of layout.qChildList.qItems) {
        if (layoutChild.qInfo && layoutChild.qInfo.qId) {
          childIds.add(layoutChild.qInfo.qId);
        }
      }
    }
    
    // Process all children recursively
    if (childIds.size > 0) {
      console.log(`${indent}  └─ Has ${childIds.size} child object(s):`);
      for (const childId of childIds) {
        childCount += await getChildObjects(childId, indent + '     ');
      }
    }
    
    return 1 + childCount;
  } catch (error) {
    // Object might not be accessible
    return 0;
  }
}
```

**Why fetch both properties and layout?**

You need to call both `getProperties()` and `getLayout()` for each object to build a detailed object inventory:

- **Properties** gives child object IDs (in `cells[]`) and configuration details like `qExtendsId`
- **Layout** gives display information (title, visualization type) and sometimes additional child information in
  `qChildList`

Different object types store child references in different places, so checking both ensures you find all nested objects.

**Why track visited objects?**

Apps can have circular references or shared objects. The `visitedObjects` Set prevents infinite loops by skipping
objects you've already processed.

**Two places to find children:**

1. **`properties.cells[]`** - Contains children for container visualizations (the configuration)
2. **`layout.qChildList.qItems[]`** - Contains children for some object types (the evaluated state)

Check both locations to ensure you find all nested objects.

## Identify master item references

Objects can reference master items through the `qExtendsId` property:

```ts
async function getChildObjects(objectId, indent = '  ') {
  // ... previous code ...
  
  const childObject = await app.getObject(objectId);
  const childProperties = await childObject.getProperties();
  const layout = await childObject.getLayout();
  
  // Check if this is a master item instance
  const isMasterItem = childProperties.qExtendsId && 
                       !objectId.includes('qlik-compound-context');
  const masterItemId = childProperties.qExtendsId || null;
  
  const title = layout.title || layout.qMeta?.title || 'Untitled';
  const type = layout.visualization;
  
  console.log(`${indent}Object ID: ${objectId}`);
  console.log(`${indent}  Name: ${title}`);
  console.log(`${indent}  Type: ${type}`);
  
  if (isMasterItem && masterItemId) {
    console.log(`${indent}  Master Item ID: ${masterItemId}`);
  }
  
  // ... rest of function ...
}
```

**Important notes:**

- `qExtendsId` is found in **properties**, not layout - this is why you need to call `getProperties()` to look for
  master item relationships
- You filter out `qlik-compound-context` objects because these are internal system objects that technically have
  `qExtendsId` but aren't user-facing master items
- The `title` and `visualization` type come from the **layout** because those are runtime-evaluated values

## Optional: Save layouts and properties to disk

For debugging and analysis, you can save each object's layout and properties as JSON files to disk, by
setting `SAVE_LAYOUTS=true` in your `.env` file.

This creates a `layouts/<app-id>/` directory with JSON files for sheets, objects, and a comprehensive inventory:

- Each sheet's layout: `sheet-layout_<sheet-id>.json`
- Each sheet's properties: `sheet-properties_<sheet-id>.json`
- Each object's layout: `viz_<object-id>.json`
- Complete app analysis: `object-library.json`

The layout and properties files contain full metadata, configuration, and child object information.

**The Object Library File**

The `object-library.json` file contains a comprehensive analysis of your app:

- **Sheets**: List of all sheets with IDs, titles, and object counts
- **Objects**: Complete inventory of all objects with ID, title, type, master item status, depth, and associated sheet
- **Master Item Usage**: Detailed tracking showing each master item ID, total usage count, and every sheet/object where
  it's used
- **Visualization Types**: Distribution of visualization types across the app (sorted by frequency)
- **Summary Statistics**: Total sheets, objects, unique visualization types, and master items used

**Use Cases for Saving Layouts:**

- **Debugging object structures** - Inspect the complete JSON structure of complex objects
- **Understanding object relationships** - See how objects reference each other
- **Analyzing app composition** - Query the object library to build reports on what types of objects are used
- **Tracking master item usage** - Identify where master items are used across sheets
- **Comparing sheets vs objects** - See the difference between sheet properties and object layouts
- **Exporting configurations** - Document or migrate object and sheet definitions
- **Auditing visualizations** - Understand the distribution of visualization types in your app

## Get the complete example

The complete working example that combines all these concepts is available in the [qlik-cloud-examples repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/examples/app-sheet-list-objects):

1. Clone or download the repository
2. Navigate to the `app-sheet-list-objects` directory
3. Copy `.env.example` to `.env` and add your credentials
4. Run `npm install` to install dependencies
5. Run `npm start` to execute the script

The repository includes:

- Complete source code with all the patterns discussed
- Package.json with dependencies configured
- README with detailed setup instructions
- Example .env file for configuration

Use this as a template for building your own app analysis tools.

## Understanding the output

When you run the script from the repository, you'll see output like this:

**Example Output:**

```bash
Sheet: Dashboard
└─ Sheet has 3 object(s):
  - Object ID: abc123
    Name: Sales Overview
    Type: barchart
    Master Item ID: master-123
  - Object ID: def456
    Name: KPI Panel
    Type: sn-layout-container
    └─ Has 2 child object(s):
       - Object ID: ghi789
         Name: Total Sales
         Type: kpi
       - Object ID: jkl012
         Name: Total Orders
         Type: kpi

==================================================
Summary:
  Total Sheets: 1
  Total Objects: 5
==================================================

==================================================
Master Item Usage:
==================================================

Master Item ID: master-123
  Used 1 time(s):
  └─ Sheet: "Dashboard" (sheet1)
     1 instance(s)
       - abc123: "Sales Overview"

==================================================
Visualization Type Distribution:
==================================================
  kpi: 2
  barchart: 1
  sn-layout-container: 1
==================================================
```

The output includes four main sections:

### Sheet and object details

For each object, the script displays:

- **Object ID**: The unique identifier for the generic object
- **Object Name**: The title from the layout (user-visible name)
- **Object Type**: The visualization type from `layout.visualization`
- **Master Item ID** (if applicable): The ID of the master item this object is based on
- **Child objects**: Any nested objects within containers, with recursive traversal

### Summary statistics

Shows the total count of sheets and objects (including nested objects) found in the app.

### Master item usage report

For apps that use master items, this section shows:

- Each master item ID
- How many times it's used across the app
- Which sheets contain the master item
- The specific object instances (ID and title) on each sheet

This helps identify:

- Which master items the app uses most
- Where specific master items are referenced
- Opportunities to consolidate duplicate visualizations into master items

### Visualization type distribution

Shows all visualization types found in the app, sorted by frequency. This helps you:

- Understand the composition of your app
- Identify which chart types are most common
- Audit custom extensions vs. native visualizations

## Properties vs layout: Understanding the difference

Generic objects have two critical components you interact with through separate API calls. Understanding the difference
is essential for working with Qlik apps.

**Properties** (`getProperties()`) - Design-time configuration:

- `cells[]` - Child object IDs (what objects are on the sheet)
- `qExtendsId` - Master item reference
- `qMetaDef` - Basic metadata (sheets only)
- Dimension and measure definitions
- Configuration settings

**Layout** (`getLayout()`) - Runtime evaluated state:

- `qMeta` - Rich metadata (owner, privileges, timestamps)
- `qChildList` - Evaluated child objects with their layouts
- `visualization` - Visualization type
- Computed titles and labels
- Current data and calculated values
- User permissions

**When to use each:**

- Use **properties** when you need to modify/clone objects, access child IDs, or view master item relationships
- Use **layout** when you need display information, runtime data, or user permissions

In this example, you need both because children can appear in `properties.cells[]` OR `layout.qChildList`, depending on
the object type.

## Key patterns

- **Find children**: In `sheetProperties.cells[]` (must call `getProperties()` on the sheet),
  `containerProperties.cells[]`, and `layout.qChildList.qItems[]`
- **Prevent loops**: Track visited objects within a set to avoid infinite depth recursion
- **Master items**: Filter out `qlik-compound-context` when checking `qExtendsId`
- **Handle missing titles**: Use `layout.title || layout.qMeta?.title || 'Untitled'`.
  This checks `layout.title` first, then falls back to `layout.qMeta.title` (for master items), and finally defaults to
  `'Untitled'`.

## Advanced: Using the object inventory

The example code already includes a starter inventory tracker built-in. When you enable `SAVE_LAYOUTS=true`, it
generates per-object files, and an `object-library.json` file with detailed analysis.

**Querying the Object Library**

You can use tools like `jq` to query the inventory file:

```bash
# Find all objects of a specific type
jq '.objects[] | select(.type == "barchart")' layouts/<app-id>/object-library.json

# Count objects by type
jq '.visualizationTypes | sort_by(-.count)' layouts/<app-id>/object-library.json

# Find which sheets use a specific master item
jq '.masterItemUsage[] | select(.masterItemId == "abc123") | .usages' layouts/<app-id>/object-library.json

# Get objects at a specific nesting depth
jq '.objects[] | select(.depth == 2)' layouts/<app-id>/object-library.json

# List all sheets with more than 10 objects
jq '.sheets[] | select(.objectCount > 10)' layouts/<app-id>/object-library.json
```

**Extending the Inventory**

The inventory is built using JavaScript Maps during traversal:

```ts
const inventory = {
  sheets: [],
  objects: [],
  masterItemUsage: new Map(),
  visualizationTypes: new Map(),
};
```

During object traversal, the script:

- Tracks each visualization type and its count
- Records master item usage with sheet and object details
- Captures object depth for understanding nesting complexity
- Associates each object with its parent sheet

You can extend this pattern to track additional metrics like:

- Custom properties or themes
- Data model fields used in dimensions/measures
- Objects with specific configurations
- Performance characteristics

## Summary

You now understand how to:

- Work with the [generic object model](https://qlik.dev/embed/foundational-knowledge/app-anatomy/generic-object-model/) in Qlik Sense
- Open an app session with `withoutData: true` for structure-only inspection
- Navigate from sheets to their child objects using `getProperties()` and the `cells[]` array
- Retrieve full object details with `getObject()`, `getProperties()`, and `getLayout()`
- Recursively traverse container relationships through both `properties.cells[]` and `layout.qChildList`
- Resolve master item references using the `qExtendsId` property (while filtering compound context objects)
- Prevent infinite loops by tracking visited objects
- Handle fallback values for missing object titles
- Track and analyze master item usage across sheets
- Generate visualization type distribution reports
- Create comprehensive object inventories with the `object-library.json` file
- Query inventory data for app composition analysis

## Next steps

- Use these patterns to build automation tools, migration scripts, app analyzers, or documentation generators.
- Clone the complete working example from the [qlik-cloud-examples repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/examples/app-sheet-list-objects)
  and use it as a template for your own tools.
