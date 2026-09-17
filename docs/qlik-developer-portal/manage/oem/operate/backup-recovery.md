---
source: https://qlik.dev/manage/oem/operate/backup-recovery/
last_updated: 2026-05-27T18:16:42+01:00
---

# Backup and recovery

For backup and recovery in OEM deployments, focus on protecting two key areas: your deployment configuration and your
customers' user-created content.

## Store deployment configuration as code

All templates, connections, and deployment configuration discussed in the [Product Development](https://qlik.dev/manage/oem/product-development/)
section should be stored outside of Qlik Cloud as configuration files. This defines the desired state of your deployment
and serves as your primary backup mechanism.

**Configuration storage options:**

- JSON files in version control (recommended)
- Relational database
- Flat files or configuration management system

Your deployment configuration should include:

- Application templates and their versions
- Data connection configurations
- User role and permission templates
- Automation workflows
- Tenant configuration settings

## Built-in disaster recovery

Qlik Cloud includes built-in disaster recovery with automatic failover to other regions if a cloud provider experiences
a regional outage. You do not need to implement your own DR procedures for the Qlik Cloud infrastructure. Read more on
the [Qlik Trust Center](https://www.qlik.com/us/trust).

## Backing up user-created content

For customers who create their own content within your applications (sheets, visualizations, bookmarks, stories), you
need to back up both the application files and the object metadata. This ensures you can rebuild customer content with
proper ownership if you need to recreate a tenant.

**What to back up:**

- **Application files:** Export .qvf files using `@qlik/api` or REST APIs
- **Object metadata:** Which users own which sheets, bookmarks, and stories, along with their approval and publish state
- **Telemetry data:** Optional, via Qlik Cloud Monitoring apps or REST APIs

**When to back up user content:**

- You allow customers to create their own sheets and visualizations
- Customers have self-service analytics capabilities
- Customers are administering their own tenant
- You need to preserve telemetry data for compliance or analytics

If you provision all content through templates and customers only consume pre-built content, backing up user-created
objects may not be necessary.

## Exporting object metadata

To restore user-created content with correct ownership, you must export object metadata as well as
the application files. This metadata includes which users own which sheets, bookmarks, stories, and other objects,
along with their approval and publish state.

The following Node.js script exports object metadata for all apps in managed spaces using `@qlik/api`
with OAuth machine-to-machine authentication. The OAuth client requires the `admin_classic` and `admin.apps` scopes:

```javascript
// export-apps-with-metadata.js
// Exports apps and their object metadata using @qlik/api
// Requires OAuth client with 'admin_classic' and 'admin.apps' scopes

import { auth, apps, spaces } from "@qlik/api";
import { qix } from "@qlik/api";
import fs from "fs";
import path from "path";

// Configuration
const hostConfig = {
  host: process.env.QLIK_HOST, // "<tenant.region.qlikcloud.com>"
  authType: "oauth2",
  clientId: process.env.QLIK_CLIENT_ID,
  clientSecret: process.env.QLIK_CLIENT_SECRET,
  scope: "admin_classic admin.apps"
};

auth.setDefaultHostConfig(hostConfig);

// Create export directory
const exportDir = "app-exports";
if (!fs.existsSync(exportDir)) {
  fs.mkdirSync(exportDir);
}

(async () => {
  try {
    // Get all managed spaces
    const spacesList = await spaces.getSpaces({ type: "managed" });
    
    for (const space of spacesList.data) {
      console.log(`\nProcessing space: ${space.name}`);
      
      // Get all apps in this space
      const appsList = await apps.getApps({ spaceId: space.id });
      
      for (const app of appsList.data) {
        const appId = app.attributes.id;
        const appName = app.attributes.name;
        
        console.log(`  Processing app: ${appName} (${appId})`);
        
        try {
          // Export the app file
          const exportData = await apps.exportApp(appId, { NoData: true });
          const appFilePath = path.join(exportDir, `${appId}.qvf`);
          fs.writeFileSync(appFilePath, Buffer.from(exportData));
          
          // Get object metadata using Engine API
          const session = qix.openAppSession({
            appId: appId,
            withoutData: true
          });
          
          const doc = await session.getDoc();
          
          // Get all app objects
          const objectsList = await doc.getAllInfos();
          
          // Build metadata for each object
          const metadata = [];
          
          for (const obj of objectsList.qInfos) {
            // Get object layout to access qMeta with owner information
            const genericObj = await doc.getObject(obj.qId);
            const layout = await genericObj.getLayout();
            
            metadata.push({
              appId: appId,
              appName: appName,
              objectId: obj.qId,
              objectType: obj.qType,
              objectTitle: layout.qMeta?.title || "",
              ownerId: layout.qMeta?.ownerId || "",
              ownerSubject: layout.qMeta?.owner || "",
              approved: layout.qMeta?.approved || false,
              published: layout.qMeta?.published || false,
              publishTime: layout.qMeta?.publishTime || null
            });
          }
          
          // Close the session
          await session.close();
          
          // Export metadata as JSON
          const metadataPath = path.join(exportDir, `${appId}-metadata.json`);
          fs.writeFileSync(
            metadataPath,
            JSON.stringify(metadata, null, 2)
          );
          
          console.log(`    Exported ${metadata.length} objects with metadata`);
          
        } catch (error) {
          console.error(`    Error exporting app ${appName}: ${error.message}`);
        }
      }
    }
    
    console.log(`\nExport complete. Files saved to ${exportDir} directory.`);
    
  } catch (error) {
    console.error("Export failed:", error);
  }
})();
```

This script:

- Exports `.qvf` files for each application (without data)
- Creates `-metadata.json` files with object metadata from each object's layout including:
  - Object ID, type, and title
  - Owner ID and **owner subject**
  - Approved and published state
  - Publish time

**Why capture user subjects?** When a tenant is rebuilt, user IDs will change but user subjects (the unique identifier
from your identity provider) remain constant. The `qMeta.owner` field contains the user subject, which allows you to
look up users by their subject when restoring ownership in the new tenant.

## Restoring apps and metadata

To restore backed up applications with preserved user ownership, follow these steps in reverse:

1. **Import the application:** Use the Apps API to import the `.qvf` file into a shared space
2. **Restore object ownership:** Use the metadata files to change the owner of each object to the correct user by
   looking up users by their subject
3. **Move to managed space:** Move the app to a managed space for consumption

On your next deployment, you'll publish over this restored app with your latest template version, replacing the base
sheets while preserving user-created content.

For detailed examples of the import and ownership restoration process, see:

- [Import the app to Qlik Cloud](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate/#2-import-the-app-to-qlik-cloud)
- [Change owner of objects in Qlik Cloud](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate/#4-change-owner-of-objects-in-qlik-cloud)
- [Move the app to a managed space](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate/#5-move-the-app-to-a-managed-space)

## Next steps

You've reached the end of the playbook.

**Return to the playbook:** → [Get started with the OEM & ISV playbook](https://qlik.dev/manage/oem/introducing-playbook/)
