---
source: https://qlik.dev/manage/oem/product-development/
last_updated: 2026-05-27T18:16:42+01:00
---

# Product development overview

Now that you've completed your architecture and security planning, it's time to build your integration. This section
guides you through the key development decisions and tasks needed to create a production-ready Qlik Cloud OEM solution.

## Development workflow

In OEM deployments, you build **application templates** with load scripts, data models, sheets, and visualizations
using test data. These templates are stored in version control without data and deployed across customer tenants.
Customer-specific variables (such as customer ID, customer name, and feature flags) configure each deployment.

**Template-based deployment workflow:**

1. Develop apps on test data with variable-based configuration
2. Store templates to version control (without data)
3. Deploy templates across customer tenants via automated promotion
4. Trigger reloads with customer-specific variables to populate with real data

For Analytics apps, you can set variables by replacing the load script at deployment time (recommended when using
Qlik's built-in scheduler), or use
[reload-time variables](https://qlik.dev/changelog/149-api-updates-reload-time-variables-constraints/) to pass them
dynamically at reload time (recommended for external schedulers or one-off overrides such as forcing a full reload).

The same template-based deployment workflow applies to all platform components: applications, data pipelines,
automations, and themes.

## Development tasks

### Task 1: Set up your DTAP environments

Configure your Qlik Cloud tenants for each stage of your development lifecycle. This covers the recommended
space-based DTAP setup, automated version control promotion, data connection patterns, and the stepped rollout
strategy for deploying to customer tenants.

**→ [Configure DTAP environments](https://qlik.dev/manage/oem/product-development/dtap-environments/)**

### Task 2: Design your application structure

Decide how to organize your Qlik Sense applications: single app vs multiple apps, which data caching strategy to
use, how to handle large data sets, and how app chaining or summary-detail patterns can improve performance.

**→ [App architecture patterns](https://qlik.dev/manage/oem/product-development/app-architecture/)** - app count decisions, chaining,
summary-detail, ODAG, and data caching strategy

**→ [App templates and customization](https://qlik.dev/manage/oem/product-development/app-templates/)** - reusable templates, variable
injection, naming conventions, and extensions

### Task 3: Build your applications

Once you have your environments and architecture planned, build your applications using the template approach:

- Write data load scripts with customer-specific variables (`vCustomerID`, `vCustomerName`, etc.)
- Build data models optimized for your use cases
- Design visualizations and dashboards
- Apply custom themes and branding
- Configure section access and space permissions
- Test with realistic data volumes
- Store templates to version control without data

**Connecting to data:** For connection management across environments, see
[data connection best practices](https://qlik.dev/manage/oem/product-development/dtap-environments/#data-connection-best-practices-across-environments)
in the DTAP environments guide.

**User access and roles:** For authentication patterns, identity provider setup, and role assignment, see
[data privacy & security](https://qlik.dev/manage/oem/privacy-security/data-access/).

## Next steps

**Ready to start?** → [Configure DTAP environments](https://qlik.dev/manage/oem/product-development/dtap-environments/)
