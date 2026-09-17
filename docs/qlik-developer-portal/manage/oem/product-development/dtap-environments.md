---
source: https://qlik.dev/manage/oem/product-development/dtap-environments/
last_updated: 2026-05-27T18:16:42+01:00
---

# DTAP environments

Based on experience with successful OEM customers, a well-structured DTAP (Development, Test, Acceptance,
Production) environment strategy significantly contributes to deployment success. This guide covers the recommended
environment setup using Qlik Cloud spaces and version control.

## Recommended environment architecture

### Single tenant with space-based development, test, and acceptance environments

**Recommended approach for OEM deployments:**

For development, test, and acceptance environments, it is recommended to use
a **single Qlik Cloud tenant on a separate
subscription** from your production subscription. Within this tenant, use **spaces** to separate
Development, Test, and Acceptance stages.

**Why this approach:**

- **Simplified management** - Centralized administration and user management, typically your development team will
  need access to all development environments to collaborate on apps
- **Easy promotion** - Apps move between spaces within the same tenant
- **Clear separation** - Spaces provide logical boundaries between stages
- **Production isolation** - Production runs on separate subscription with separate tenants per customer, this protects
  your production entitlements from being used by development or test environments

**Architecture:**

```text
Non-Production Subscription:
└── Development Tenant
    ├── Shared Spaces (per project)
    │   ├── Project A Development
    │   ├── Project B Development
    │   └── Project C Development
    ├── Managed Spaces
    │   ├── Commit Space (commits published apps to version control, then deletes)
    │   ├── Test Space (automated promotion from version control)
    │   └── Acceptance Space (automated promotion once merged to main)
    ├── Version Control Integration (GitHub, GitLab, Azure DevOps)
    └── Qlik Automate (for deployment automation, or use your own CI/CD tooling)

Production Subscription:
├── Customer A Tenant
├── Customer B Tenant
└── Customer C Tenant
```

### Environment stages explained

#### Development (Shared Spaces)

**Purpose:** Active development and collaboration

- One shared space per project/product
- Developers build apps collaboratively
- Rapid iteration with test data
- App templates stored here

#### Test (Managed Space)

**Purpose:** Automated testing and validation

- Managed space allows testing of core (approved) content, while permitting testers to maintain and verify their own
  sheets, bookmarks, visualizations, or other objects and configuration
- Apps automatically promoted from test via version control
- Integration testing with realistic data
- App evaluation for performance testing - automatically run on each change to the app
- Reviewer approval required before promotion to acceptance, this is a human verification gate controlled by merge to
  main branch

#### Acceptance (Managed Space)

**Purpose:** Final validation before production

- Managed space for production-readiness review, this is a human verification gate before a release
- Manual review and sign-off required
- App evaluation to ensure performance - automatically run on each change to the app
- Final approval gate before customer deployment

#### Production (Separate Subscription)

**Purpose:** Live customer environments

- Separate tenant per customer
- Apps deployed via Qlik Automate or your own CI/CD tooling
- Production data and monitoring
- Full isolation between customers
- Limited or no interactive access for your development team

## Recommended DTAP workflow

### Overview: Version control-driven promotion

The recommended workflow uses **app names as unique keys** across spaces and version control, enabling automated
promotion with human verification gates.

**Key principles:**

- All steps automated except approval, merge, and deployment (human verification required)
- Apps identified by name across all spaces
- Version control (GitHub/GitLab/Azure DevOps) tracks all changes
- Diffs in version control reveal changes not visible in the UI
- App evaluation ensures performance at each stage

[![Video thumbnail](https://play.vidyard.com/ff7H6XJUaTy7PtGJQcka9L.jpg)](https://play.vidyard.com/ff7H6XJUaTy7PtGJQcka9L)

### Step-by-step workflow

#### Step 1: Development in shared spaces

**Developers work in shared spaces per project:**

```text
// Development space structure
Development Tenant
├── Shared Space: "Customer Analytics Project"
│   ├── Product A Historical Dashboard
│   ├── Product A Monthly Performance Dashboard
│   └── Product A Live Wallboard
└── Managed Space: "Commit" (commits to version control, then deletes app)
```

**Development process:**

1. Developers collaborate on apps in the shared development space
2. Apps use test data and variable-based configuration
3. When a new version is ready, **developer publishes the app to the "Commit" managed space**
4. Publishing to the Commit space automatically triggers the version control workflow
5. Once committed to version control, the app is automatically deleted from the Commit space
6. App name is used as the unique identifier throughout the process

**Purpose of the Commit space:**

- **Space description**: "A space that commits the published version of your app immediately to version control. The
  app will be deleted from the Commit space once it has been committed."
- Acts as a trigger point for automation
- Transient storage only - apps are not retained here
- Keeps the space clean and purpose-focused

#### Step 2: Automated version control commit

**Automatically push apps to version control:**

You can use a Qlik Automate workflow to automatically push apps to GitHub, GitLab, or Azure DevOps when ready for
promotion. You can also use your own CI/CD tooling to automate the process by registering a webhook with Qlik Cloud on
the app publish event.

```text
// Qlik Automate: Push to version control
Trigger: App published to "Commit" managed space
Actions:
  1. Export app from Commit space
  2. Extract app metadata and structure
  3. Create/update branch in version control (e.g., GitHub)
  4. Commit changes with app name as key
  5. Create pull request for review
  6. Delete app from Commit space (keep space clean)
  7. Automatically deploy to Test space
```

**Benefits of version control:**

- **Diff tracking** - See exactly what changed in the app structure, load scripts, and objects
- **Small changes visible** - Version control diffs catch changes not obvious in the Qlik UI
- **Audit trail** - Complete history of who changed what and when
- **Rollback capability** - Easy revert to previous versions
- **Code review** - Team can review changes before promotion

#### Example: GitHub Actions unbuild workflow

One effective pattern for version control integration is to let GitHub (or your CI/CD platform) handle
the unbuild step. When a developer exports a `.qvf` and commits it, a workflow runs that imports it into
a temporary tenant, unbuilds it into its component files (load scripts, app properties, objects, images),
and commits those components back to the branch. This gives reviewers a meaningful diff in the pull
request rather than a binary file comparison.

**Benefits of this approach:**

- **Reviewable diffs** - load scripts, variables, and object definitions appear as text diffs in the PR
- **Customer-controlled compute** - runs on the customer's own GitHub Actions runners (or self-hosted runners)
- **Composable** - uses qlik-cli below, but you can substitute the [`@qlik/api` TypeScript library](https://qlik.dev/toolkits/qlik-api/)
  or raw REST calls to the [Apps API](https://qlik.dev/apis/rest/apps/) to suit your toolchain
- **Structure flexibility** - you control the directory layout and what gets extracted

**Required GitHub configuration:**

| Secret / Variable | Type     | Description                                                   |
| ----------------- | -------- | ------------------------------------------------------------- |
| `CLIENT_SECRET`   | Secret   | OAuth client secret for the non-production tenant             |
| `TENANT_HOSTNAME` | Variable | Tenant hostname (for example, `your-tenant.eu.qlikcloud.com`) |
| `CLIENT_ID`       | Variable | OAuth client ID                                               |

The OAuth client needs `apps:create`, `apps:export`, `apps:delete`, and media read scopes on the non-production tenant.

Save as `.github/workflows/unbuild-app.yml`:

<details>
  <summary>Click to expand: unbuild-app.yml</summary>

`embed:./snippets/oem-playbook/unbuild-app.yml`

</details>

The workflow calls a helper script, `extract-components.sh`, which splits the consolidated `dimensions.json`, `measures.json`,
and `variables.json` files output by `app unbuild` into one file per object. This makes individual dimension and measure
changes visible as targeted diffs rather than a single large file modification. It also removes `connections.yml`,
which contains environment-specific connection references that should not be version-controlled.

Save as `.github/workflows/scripts/extract-components.sh`:

<details>
  <summary>Click to expand: extract-components.sh</summary>

`embed:./snippets/oem-playbook/extract-components.sh`

</details>

**How it works:**

1. On every PR that touches a `.qvf` file, the workflow identifies which app files changed
2. Each `.qvf` is imported into the non-production tenant using the [Apps API](https://qlik.dev/apis/rest/apps/)
3. qlik-cli's `app unbuild` command extracts the app into individual JSON and YAML files - one per object,
   sheet, variable, load script, etc.
4. The temporary `appId` is replaced with a `<appId>` placeholder so it doesn't create noise in future diffs
5. Volatile fields (`qSavedInProductVersion`, `qLastReloadTime`) are stripped from `app-properties.json`
6. `extract-components.sh` splits master dimensions, measures, and variables into individual named files, and removes `connections.yml`
7. Any embedded images are downloaded and stored alongside the components
8. The components are committed back to the PR branch - reviewers now see text diffs for every changed object

**Resulting repository structure:**

```text
apps/
└── Product A Historical Dashboard/
    ├── Product A Historical Dashboard.qvf   ← binary, triggers the workflow
    ├── metadata.json                         ← version extracted from app description
    └── components/
        ├── app-properties.json
        ├── load-script.qvs
        ├── sheets/
        │   ├── sheet-1.json
        │   └── sheet-2.json
        ├── dimensions/
        │   └── Sales_by_Region-ABC123.json   ← one file per master dimension
        ├── measures/
        │   └── Total_Revenue-DEF456.json     ← one file per master measure
        ├── variables/
        │   └── vEnvironment-GHI789.json      ← one file per variable
        └── images/
            └── logo.png
```

#### Step 3: Test space promotion and review

**Apps automatically deployed to Test managed space:**

```text
// Test space after automated promotion
Development Tenant
└── Managed Space: "Test"
    ├── Product A Historical Dashboard  (from version control)
    ├── Product A Monthly Performance Dashboard  (from version control)
    └── Product A Live Wallboard  (from version control)
```

**Testing process:**

1. **Automated deployment** - App automatically appears in Test space from version control workflow
2. **App evaluation** - Run app evaluation to establish performance baseline and identify issues
3. **Integration testing** - Testers validate functionality with realistic data
4. **Performance validation** - Ensure no performance degradation
5. **Review pull request** - Team reviews version control diffs
6. **Approve or reject** - Human approval required to proceed

**Use App Evaluation feature:**

```text
// App evaluation in Test space
- Check app performance metrics
- Identify slow-loading sheets
- Detect calculation bottlenecks
- Compare against baseline performance
- Flag any degradations introduced
```

[Learn more about App Evaluation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/app-performance-evaluation.htm)

#### Step 4: Merge to main and Acceptance promotion

**Human verification: Merge pull request**

After successful testing and approval:

1. **Reviewer approves PR** - Human decision gate
2. **Merge to main branch** - Human action in version control
3. **Automated promotion to Acceptance** - Workflow triggered by merge
4. **App appears in Acceptance space** - Ready for final review

```text
// Acceptance space after merge to main
Development Tenant
└── Managed Space: "Acceptance"
    ├── Product A Historical Dashboard  (from main branch)
    ├── Product A Monthly Performance Dashboard  (from main branch)
    └── Product A Live Wallboard  (from main branch)
```

**Acceptance review process:**

1. **Manual review required** - Stakeholders review the app
2. **App evaluation** - Final performance verification
3. **Sign-off** - Formal approval to deploy to production
4. **Production readiness** - Confirm app is ready for customers

#### Step 5: Production deployment via Automate

**Human verification: Deploy to customer tenants**

After acceptance sign-off:

1. **Human triggers deployment** - Manual action to deploy
2. **Qlik Automate workflow** - Deploys to customer tenants
3. **Stepped rollout** - Pilot → Limited → Broad → Full
4. **Monitor deployments** - Track success across tenants

```text
// Qlik Automate: Deploy to production
Trigger: Manual approval
Actions:
  1. Get app from Acceptance space or repository release (by app name)
  2. Export app without data
  3. Deploy to customer tenants (stepped rollout)
     - Pilot customers (1-3 tenants)
     - Limited rollout (10-20%)
     - Broad rollout (50%)
     - Full rollout (100%)
  4. Trigger reloads with customer-specific variables
  5. Monitor and alert on any failures
```

### Data connection best practices across environments

#### Use relative data connection names

**Recommended approach:** Use relative data connection names so apps work seamlessly across Development, Test, and
Acceptance spaces without modification.

**Why this matters:**

- Apps can move between spaces without updating connection paths
- No need to modify data connection references during promotion
- Consistent connection names across all environments
- Reduces deployment complexity and errors

**Example: Relative connection naming**

Omitting a space name and using a single colon (:) prior to the connection name will look for a data connection in the
same space that the app is stored in.

```text
// In your load script, use the same connection name across all environments

LOAD * FROM [lib://:ProductADataConnection/sales.parquet] (parquet);
```

**Setup:** Create data connections with the same name in each space:

- Development space: "ProductADataConnection" → points to dev data
- Test space: "ProductADataConnection" → points to test data
- Acceptance space: "ProductADataConnection" → points to acceptance data
- Production space: "ProductADataConnection" → points to production data (for the customer tenant)

The app uses `lib://:ProductADataConnection/` everywhere, and it automatically connects to the right environment's data
by using the connection definition in the space.

#### Dynamic connection paths with GetSysAttr()

If consistent connection naming across spaces is not an option, use
[GetSysAttr()](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetSysAttr.htm)
to detect which space the app is running in and branch accordingly:

```javascript
LET vSpaceName = GetSysAttr('spaceName');
LET vTenantName = GetSysAttr('tenantName');
LET vTenantID = GetSysAttr('tenantId');
LET vTenantRegion = GetSysAttr('tenantRegion');

IF '$(vSpaceName)' = 'Test' THEN
    LET vDataConnection = 'lib://TestData';
ELSEIF '$(vSpaceName)' = 'Acceptance' THEN
    LET vDataConnection = 'lib://AcceptanceData';
ELSEIF Index('$(vSpaceName)', 'Development') > 0 THEN
    LET vDataConnection = 'lib://DevData';
ELSE
    // Production deployment (customer tenant)
    LET vDataConnection = 'lib://ProductionData';
END IF

// Log environment details for troubleshooting
TRACE Running on tenant: [$(vTenantName)] [$(vTenantID)] region: [$(vTenantRegion)] space: [$(vSpaceName)].;

LOAD * FROM [$(vDataConnection)/sales.parquet] (parquet);
```

The `TRACE` statements write to the reload log and are useful for diagnosing environment mismatches.
For the full list of available `GetSysAttr()` values, see the
[GetSysAttr() documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetSysAttr.htm).

#### Tag connections with the release version

When deploying data connections to customer tenants, tag each connection with the release version used to create it.
This makes it straightforward to identify and remove connections that belong to an older release during
[monthly maintenance](https://qlik.dev/manage/oem/operate/maintenance/#remove-unused-data-connections).

Use the [Data Connections API](https://qlik.dev/apis/rest/data-connections/) to set tags at deployment time:

```bash
# Create a connection tagged with the release version
curl "https://<TENANT>/api/v1/data-connections" ^
  -X POST ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Content-Type: application/json" ^
  -d "{
        \"datasourceID\": \"snowflake\",
        \"qName\": \"ProductADataConnection\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
          \"server\": \"<HOST>\",
          \"database\": \"<DATABASE_NAME>\",
          \"schema\": \"<SCHEMA_NAME>\",
          \"warehouse\": \"<WAREHOUSE_NAME>\",
          \"username\": \"<USERNAME>\",
          \"password\": \"<PASSWORD>\"
        },
        \"tags\": [\"release:v2.4.0\"]
      }"
```

During maintenance, iterate all connections across tenants and remove any not tagged with the current release version.
This eliminates accumulation of stale connections without needing to track individual connection IDs.

## Next steps

With your environments configured, you're ready to design your application structure.

**Continue to next step:** → [Structure your applications](https://qlik.dev/manage/oem/product-development/app-architecture/)
