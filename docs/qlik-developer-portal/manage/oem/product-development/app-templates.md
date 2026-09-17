---
source: https://qlik.dev/manage/oem/product-development/app-templates/
last_updated: 2026-05-27T18:16:42+01:00
---

# App templates and customization

## Template applications

In an OEM deployment, you build a template application once and deploy it to every customer tenant. The template
contains the load script, data model, sheets, and visualizations - built against test data and stored in version control
without data. Customer-specific values are injected as variables at deployment or reload time.

```text
// Customer configuration variables set at deployment or reload
LET vCustomerID = '$(vCustomerID)';
LET vCustomerName = '$(vCustomerName)';
LET vDataPath = 'lib://:CustomerData/$(vCustomerID)';
LET vDaysHistory = '$(vDaysHistory)';

// Use variables throughout the load script
LOAD * FROM [$(vDataPath)/sales.parquet] (parquet)
WHERE date >= Today() - $(vDaysHistory);
```

The deployment workflow is: build against test data → store in version control (without data) → deploy template to
customer tenants → reload with customer-specific variables. For the full CI/CD pipeline, see
[DTAP environments](https://qlik.dev/manage/oem/product-development/dtap-environments/).

## Variable injection methods

### Method 1: Replace load script at deployment (recommended for fixed deployments)

Hard-code customer values into the script at deployment time. The script is deployed to each tenant with
customer-specific values already set. Works with Qlik Cloud's built-in scheduling UI - no programmatic reload needed.

### Method 2: Reload-time variables (recommended for dynamic scenarios)

Pass variables with each reload request via the Reloads API. The same template script is used across all tenants;
configuration can vary between reloads. Requires programmatic reload triggering but gives you flexibility for
per-reload overrides.

```bash
# Trigger reload with customer-specific variables
curl "https://<TENANT>/api/v1/reloads" ^
  -X POST ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Content-type: application/json" ^
  -d "{
        \"appId\": \"<APP_ID>\",
        \"variables\": {
          \"vCustomerID\": \"ACME_001\",
          \"vCustomerName\": \"ACME Corporation\",
          \"vDaysHistory\": \"90\",
          \"vRegion\": \"EMEA\"
        }
      }"
```

See [reload-time variables](https://qlik.dev/changelog/149-api-updates-reload-time-variables-constraints/) for the full API reference.

### Method 3: Hybrid (recommended for most deployments)

Hard-code fixed configuration (customer ID, name, region) into the script at deployment so regular scheduled reloads
work without any API calls. Add reload-time variable support for exceptions - forcing a full reload, loading extra
history during an incident, or testing a configuration change. This is the simplest setup for day-to-day operation
with the flexibility you occasionally need.

## Customization layers

OEM deployments typically have three levels of customization:

- **Data** - customer-specific data sources, custom KPIs, regional data variations. Handled by template variables and
  per-customer data connections.
- **Visual** - custom themes and branding, customer-specific layouts, role-based visualizations. Handled by the
  [Qlik Cloud themes API](https://qlik.dev/apis/rest/themes/) and tenant branding configuration.
- **Functional** - custom extensions, specialized workflows, integrations with customer systems. Requires additional
  deployment and maintenance consideration (see [Extensions](#extensions-and-custom-components) below).

Common variables for data and visual customization:

| Variable             | Purpose                                   |
| -------------------- | ----------------------------------------- |
| `vCustomerID`        | Customer identifier for data isolation    |
| `vCustomerName`      | Display name used throughout the app      |
| `vDataPath`          | Customer-specific data location           |
| `vDaysHistory`       | Historical data window (30, 90, 365 days) |
| `vRegion`            | Customer region (EMEA, APAC, AMER)        |
| `vReportingCurrency` | Currency for financial reporting          |

## Naming conventions

### Applications

Name applications by function only - no customer name, environment name, or version number in the app name. The app
name is the unique identifier that links a deployed instance back to its source template in version control. Consistent
names across all customer tenants make automated deployment and tracking straightforward.

Good examples: `Sales Analytics`, `Customer Dashboard`, `Executive Reporting`, `Operations Monitor`.

### Versions

Track versions in the app description field using the format `{v2.1.0}`. This is readable in the Qlik Cloud Hub without
needing to manage tags, and it can be extracted programmatically by your automation - the convention is to read from
the first `{v` to the closing `}`. For monitoring and system apps installed by automated installers, also apply version
tags for easy filtering in the hub and monitoring apps.

### Sheets and fields

Use plain language for sheet names - no underscores or dashes. `Sales Overview` not `Sales_Overview`. For field names,
use consistent prefixes for related fields (for example, `Sales.Amount`, `Sales.Quantity`) and avoid special characters
and spaces. Use descriptive, business-friendly names that users will understand without training.

## Extensions and custom components

Use extensions only when native Qlik objects cannot meet the requirement. Extensions add maintenance overhead, may not
be compatible with all native Qlik services (such as the Qlik Reporting Service), and require ongoing testing as Qlik
Cloud releases updates.

When you do use extensions:

- Document all extension dependencies in your repository
- Version control the extension files alongside your app templates
- Run automated validation on a daily schedule to catch compatibility regressions early

## Next steps

**Continue:** → [Managing your OEM deployment](https://qlik.dev/manage/oem/operate/)
