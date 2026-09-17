---
source: https://qlik.dev/manage/oem/key-terms-concepts/
last_updated: 2026-05-27T18:16:42+01:00
---

# Key terms and concepts

This reference guide explains the key Qlik Cloud concepts and terminology used throughout the playbook. You can
refer back to this guide at any point to understand the terms and concepts discussed in other sections.

## Quick navigation

- [Infrastructure concepts](#infrastructure-concepts) - Tenants, spaces, gateways, authentication
- [Analytics concepts](#analytics-concepts) - Qlik Sense, visualizations, embedding, app patterns
- [Automation concepts](#automation-concepts) - Qlik Automate, webhooks, APIs, reload-time variables
- [Data concepts](#data-concepts) - Pipelines, integration, DI projects
- [Management concepts](#management-concepts) - Backup, monitoring, governance, monitoring apps
- [Multi-tenant concepts](#multi-tenant-concepts) - Tenant management, architecture patterns
- [Performance concepts](#performance-and-scalability-concepts) - Associative model, resource governance
- [Development workflow](#development-workflow-concepts) - Version control, CI/CD, unbuild, observability
- [Privacy and security](#privacy-and-security-concepts) - Encryption, secrets, tenant deactivation
- [Tools and frameworks](#tools-and-frameworks) - @qlik/api, qlik-cli, Qlik Automate, and other SDKs

## Infrastructure concepts

### Tenants and spaces

**Tenants**

- **What they are:** Isolated Qlik Cloud environments for different customers
- **Equivalent to:** Separate instances, workspaces, or logical containers
- **Key features:** Complete data isolation, independent configuration, instant deployment and deactivation
- **Developer benefit:** True multi-tenancy with full isolation
- **See also:** [Spaces](#spaces) for organizing content within tenants

**Spaces**

- **What they are:** Logical containers within a tenant for grouping content
- **Equivalent to:** Folders, projects, or departments
- **Types:** Shared spaces (collaborative development), managed spaces (published content with controlled access),
  data spaces (data files and connections)
- **Key features:** Access control, content organization, collaboration
- **Developer benefit:** Logical grouping and permission management
- **See also:** [Tenants](#tenants) for the parent container

**Data gateways**

- **What they are:** Software components deployed on your own infrastructure that allow Qlik Cloud to connect
  to data sources behind a firewall or on a private network
- **Equivalent to:** VPN tunnels or reverse proxies for data access
- **Key features:** Secure tunnel to private data sources, deployed as a virtual machine,
  one gateway connects to one tenant
- **Developer benefit:** Enables data access patterns where data cannot be exposed to the public internet
- **Common use case:** In the distributed data access pattern, a source tenant connects to a firewalled database
  via a gateway, stages data to cloud storage, and customer tenants load from there

### Authentication and authorization

**OAuth SPA (Single Page Application)**

- **What it is:** An OAuth flow where users authenticate through the configured interactive identity provider
  and grant consent to the application
- **How it works:** The browser redirects to the identity provider, the user logs in, and an access token is
  returned to the SPA
- **Best for:** Web apps without a backend, or when you want users to authenticate directly through your
  identity provider
- **Developer benefit:** No secret handling required in the frontend application
- **Simplifying the consent step:** By default, users are shown a consent dialog listing the OAuth scopes
  being requested. For OEM deployments where you control both the application and the tenant, you can eliminate
  this prompt by setting the OAuth client's consent method to **Trusted**: either in the Qlik Cloud management
  console (action menu, Change consent method, Trusted) or via the
  [OAuth Clients API](https://qlik.dev/apis/rest/oauth-clients/) by patching `consentMethod` to `"trusted"`. With a trusted
  client, users are silently authorized on login with no consent screen, which is the typical experience
  expected in an embedded product.

**OAuth machine-to-machine (M2M) impersonation**

- **What it is:** A server-side OAuth flow where your backend uses a client ID and secret to generate tokens
  that impersonate specific users
- **How it works:** Your backend authenticates with Qlik Cloud and requests a token scoped to a user's
  identity, which is then used by the client
- **Best for:** Web apps with a backend where you manage user identity server-side
- **See also:** [Guiding principles for OAuth impersonation](https://qlik.dev/authenticate/oauth/guiding-principles-oauth-impersonation/)

**Interactive identity providers (OIDC / SAML)**

- **What they are:** Standard enterprise identity providers configured on a tenant for users who log in
  directly to Qlik Cloud
- **How it works:** Any unauthenticated request redirects to the configured OIDC or SAML provider; the user
  logs in and is returned to Qlik Cloud with a session
- **Best for:** Granting your internal team or administrators direct access to the tenant; also used as the
  backing identity provider for OAuth SPA flows
- **Recommendation:** Configure your own OIDC or SAML provider on every tenant as soon as it is provisioned.
  Even if only your administrator team uses it, this gives you full control over login auditing and user
  lifecycle

**JWT (JSON Web Token) identity providers**

- **What they are:** A way to establish trust between Qlik Cloud and your application backend using
  public/private key pairs
- **How it works:** Your backend signs JWTs that clients use to authorize access to Qlik Cloud; no redirect
  to an identity provider is required
- **Use cases:** Direct server-to-server access, embedded solutions where you control user identity in your
  own backend
- **Third-party cookie warning:** In browser-based embedded solutions, JWT authentication relies on
  cross-site cookies that are blocked in several major environments regardless of Google's decision not to
  deprecate them in Chrome. Safari and all browsers on iOS have enforced full third-party cookie blocking by
  default since 2020 via
  [WebKit's Intelligent Tracking Prevention (ITP)](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/).
  Firefox enables Enhanced Tracking Protection by default, which blocks third-party tracking cookies.
  Enterprise security teams routinely enforce the same restriction through browser policy. This is an
  industry-wide browser security trend and not a Qlik-specific limitation. Real-world OEM deployments serving
  Safari or iOS users, or enterprise customers with managed browsers, will encounter broken authentication if
  JWT is used without a proxy. **OAuth SPA or OAuth M2M impersonation should be your first choices for
  browser-based embedding**, as both patterns use first-party tokens and are unaffected by third-party cookie
  policies.

**Section access**

- **What it is:** Row-level security mechanism for controlling data access within applications
- **Features:** User-based data filtering, dynamic data reduction based on value allowlisting,
  field level blocklisting
- **Benefits:** Automatic data isolation without custom code
- **Developer implementation:** Qlik Sense load script section access, user mapping

**Identity and entitlements**

- **What it is:** Managing user access and feature permissions across tenants
- **Features:** Subscription management, capability toggles, user provisioning
- **Benefits:** Controlled access, cost management, feature governance
- **Developer implementation:** Qlik Cloud Platform Operations APIs, user management, subscription controls
- **Example:** Each customer tenant has specific feature entitlements based on their subscription tier

## Analytics concepts

### Qlik Sense applications and data models

**Qlik Sense applications (.qvf files)**

- **What they are:** Complete analytics applications containing the in-memory data model, all business logic,
  visualizations, and configuration in a single portable file
- **Equivalent to:** Dashboards, data models, and business logic in other platforms; with the associative
  engine embedded so the entire analytical capability travels with the file
- **Key features:** Self-contained, portable, and includes all necessary components including the full
  associative index definition
- **Developer benefit:** Single file contains everything needed for deployment via Qlik Cloud APIs; no
  separate query layer, aggregation service, or report definition to deploy alongside it
- **See also:** [App unbuild](#app-unbuild) for how to decompose .qvf files for version control. The qlik-cli
  `app unbuild` command is a fast starting point built into the tooling, but if you want to build your own
  implementation see the
  [environments guide](https://qlik.dev/manage/oem/product-development/dtap-environments/#example-github-actions-unbuild-workflow)
  for complete working examples

**Data models**

- **What they are:** The underlying data structure and relationships within an application, held entirely in
  memory after a reload
- **Equivalent to:** Database schemas, data warehouses, or analytical models
- **Key features:** The associative engine indexes every field value and every relationship across the entire
  dataset at load time. When a user makes a selection, the engine instantly propagates that state across all
  related tables and fields; no query is rewritten, no join is re-executed. Everything is already in memory
  and pre-indexed
- **The associative difference:** Unlike SQL-based tools where queries follow predefined filter paths, the
  Qlik associative engine lets users explore data in any direction across any dimension without a developer
  having to anticipate the query. Selections made in one part of the data model immediately reveal what is
  associated and what is excluded everywhere else. This is the core capability that separates Qlik from SQL
  generators and traditional BI tools
- **Developer benefit:** You define the data model once; all analytical paths emerge from it automatically.
  No need to build individual queries, aggregation layers, or predefined drill paths for each user journey

**QVD files (QlikView Data files)**

- **What they are:** Qlik's native binary data file format optimised for fast loading into Qlik Sense
  applications
- **Common use:** Caching intermediate data between reloads: load only recent data from the source, append
  historical data from QVD, write back to QVD for next time
- **Benefits:** Significantly faster reload times, reduced load on source databases, enables incremental load
  patterns
- **See also:** Parquet is often preferred for cloud-based deployments and interoperability

**Master items (master dimensions, master measures, master variables)**

- **What they are:** Reusable definitions for dimensions, measures, and variables that can be shared across
  sheets within an application
- **Equivalent to:** Named constants or shared formulas in a spreadsheet
- **Benefits:** Consistent definitions across all visualizations, single point of update, improved expression
  cache reuse
- **Developer note:** During app unbuild, master dimensions, measures, and variables are extracted to
  separate files for individual diffs in version control

**App evaluation**

- **What it is:** Qlik Cloud's built-in tool for assessing application performance: memory footprint, sheet
  load times, object render times, and bottlenecks
- **When to use:** After each significant change to an app's data model or visualizations, and at each stage
  of the pipeline (test, acceptance) to catch regressions before production
- **Developer benefit:** Provides objective performance baselines to compare against across builds

### Visualizations and sheets

**Sheets**

- **What they are:** Individual dashboard pages containing visualizations
- **Equivalent to:** Dashboard pages, report pages, or canvas areas
- **Types:** Base sheets (created and owned by the app developer), community sheets (published by end users),
  private sheets (unpublished, user-created)
- **Key features:** Interactive, responsive, and customisable for end user self-service authoring
- **Developer benefit:** Modular dashboard components for embedding via Qlik Web Components

**Visualizations**

- **What they are:** Individual charts, tables, and other data displays; more accurately, they are windows
  into the live associative model
- **Equivalent to:** Charts, widgets, or report elements
- **What makes them more than a visual:** Each visualization is the product of several layers working
  together on top of the in-memory model:
  - **Business logic:** measures and dimensions encapsulate KPI definitions, set analysis, and conditional
    logic that execute against the in-memory index
  - **Calculated dimensions and expressions:** derived fields and custom expressions are computed on the fly
    at render time, combining aggregation, bucketing, ranking, and set modifiers without pre-materialising
    results
  - **Associative state:** every object reflects the current selection state instantly; selected, possible,
    and excluded values are resolved across the whole model in memory with no round-trip to a database
  - **Styling and layout:** themes, conditional formatting, responsive sizing, and layout container
    compositions are applied on top, allowing production-quality branded experiences
- **Developer benefit:** Embedding a visualization gives users access to the full depth of the associative
  model, not just a static chart. Selections made in one embedded object immediately propagate to all other
  objects connected to the same app session, whether embedded in your UI or not
- **Styling note:** When using nebula.js directly or `qlik-embed` with `analytics/sheet` or
  `analytics/chart` in default mode, theme and styling support is limited compared to the native Qlik Sense
  client. Setting `preview="true"` on the web component enables full theme matching and support for legacy
  chart types and visualization extensions. See [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/) for details

### Analytics connections

**Analytics connections**

- **What they are:** Configurations for connecting to external data sources for analytics
- **Equivalent to:** Database connections, API endpoints, or data sources
- **Key features:** Secure, reusable, and manageable
- **Developer benefit:** Centralised data source management via Qlik Cloud Data Connections API

**Data refresh (also known as reloads, reload tasks, tasks)**

- **What they are:** Automated processes for updating application data
- **Equivalent to:** ETL processes, data pipelines, or scheduled updates
- **Key features:** Scheduled, incremental, can be API driven
- **Developer benefit:** Automated data freshness without manual intervention via Qlik Cloud Reload API and
  scheduled tasks

**Reload-time variables**

- **What they are:** Variables passed dynamically to a Qlik Sense application at the moment a reload is
  triggered via the API, overriding values defined in the load script
- **Use cases:** Passing customer-specific configuration at reload time, forcing a full historical reload
  without changing the deployed script, dynamically adjusting data filters between runs
- **Best for:** External schedulers, API-driven reloads, or one-off overrides. For regular scheduled reloads
  using Qlik's built-in scheduler, hard-coding variables in the script at deployment is simpler

### Embedding approaches

**Full classic app embedding**

- **What it is:** Embedding the full Qlik Cloud application UI, including navigation, toolbar, and all
  platform UI elements, into your application via an iframe or web component
- **Use cases:** Scenarios where users need access to platform features beyond analytics: alert subscriptions,
  bookmarks, smart search, notes, and other UI surfaces that are not exposed through the JavaScript and
  TypeScript embedding frameworks
- **Key distinction:** All embedding techniques give users access to the same associative engine and the same
  data model. The difference here is access to Qlik's own application chrome and platform UI features, not
  analytical capability
- **Developer implementation:** Single iframe or web component pointing to the app URL; Qlik Cloud manages
  the full UI shell

**Individual visualization embedding**

- **What it is:** Embedding a single chart, table, or other object from an app; the object remains connected
  to the full associative model of that app
- **Use cases:** KPI widgets, specific metrics, integrating individual analytics objects into your own layout
- **Benefits:** Your layout, Qlik's analytical depth. A single embedded chart still responds to selections
  made elsewhere in the same app session, including other embedded objects or programmatic selections you
  make via the API
- **Developer implementation:** Granular control over which objects surface in your UI; each object is backed
  by the same in-memory associative engine as the full sheet
- **Context menu note:** In default mode, nebula.js and `qlik-embed` with `analytics/sheet` or
  `analytics/chart` do not show the Qlik Sense context menu, giving you full freedom to build your own.
  Setting `preview="true"` enables the native context menu and the broader Qlik Sense interaction experience
  for those components. See [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/) for details

**Data embedding**

- **What it is:** Querying the live associative model directly by code, fetching field values, hypercube
  results, or selection states, to drive your own visualizations or UI components
- **Benefits:** Your custom UI stays connected to the same associative session as any embedded Qlik objects;
  selections made anywhere propagate to your data fetch automatically
- **Developer implementation:** Use the Engine API via [@qlik/api](https://qlik.dev/toolkits/qlik-api/) to open hypercubes,
  apply selections, and stream results. This gives you the full associative engine as a data backend without
  being constrained to Qlik's visualization layer

### Application architecture patterns

**App chaining**

- **What it is:** A pattern where multiple smaller Qlik Sense apps are linked together, with user selections
  preserved as they navigate between them
- **How it works:** All apps are pre-loaded when the web application initialises; when a user navigates
  between apps, current selections are read and applied to the target app
- **Use cases:** Segmenting large data sets by region, product line, or time period to stay within standard
  tier memory limits; summary-detail navigation; role-specific apps
- **Benefits:** Each app stays within standard tier size limits (cost-effective), faster load times, better
  performance

**Summary-detail pattern**

- **What it is:** A specific app chaining approach with a fast, highly aggregated summary app (for daily use)
  and a slower, full-granularity detail app (for deep analysis on demand)
- **Benefits:** Most users work entirely in the fast summary app; the detail app loads only when truly
  needed, avoiding over-provisioning

**On-demand app generation (ODAG)**

- **What it is:** Qlik Cloud generates a personalised app on-demand filtered to the user's current
  selections, enabling user-specific isolated data views from a large dataset
- **Use cases:** Scenarios where the full dataset is too large for one app, or where each user needs a
  distinct filtered slice they can work with independently

**Dynamic views**

- **What it is:** A hybrid pattern that connects directly to database views and loads only aggregated data
  into memory, leaving detailed data in the database
- **Use cases:** Large transactional datasets where full in-memory loading is not practical, and
  database query performance is sufficient

**Direct Query**

- **What it is:** Qlik Cloud queries data directly from your database without loading it into memory, using
  SQL generation to push computation down to the source
- **Use cases:** Large datasets (billions of rows), real-time data that changes frequently,
  databases optimised for analytical queries

## Automation concepts

### Qlik Automate

**Qlik Automate**

- **What it is:** Visual workflow automation for Qlik Cloud operations
- **Features:** Pre-built templates, custom workflows, event triggers
- **Benefits:** No-code automation for common tasks
- **Developer implementation:** Qlik Automate workflows, pre-built templates, custom connectors
- **See also:** [Event-driven architecture](#event-driven-architecture) for webhook-based automation
- **Example:** Create a workflow that automatically provisions a new tenant with starter applications

**Automate connections**

- **What they are:** Configurations for connecting Qlik Automate to external systems
- **Features:** Pre-built connectors, custom integrations, API connections
- **Benefits:** Seamless integration with existing tools and workflows
- **Developer implementation:** Qlik Automate connector marketplace, custom connector development

### Automation workflows

**Event-driven architecture**

- **What it is:** Webhook-based automation triggered by Qlik Cloud events such as app created, reload
  finished, and user added
- **Features:** Real-time notifications, custom integrations; events are also available in the Audits API
  for historical queries
- **Benefits:** Reactive automation and monitoring
- **Developer implementation:** Qlik Cloud webhooks, event subscriptions, custom webhook endpoints
- **See also:** [Qlik Automate](#qlik-automate) for visual workflow automation
- **Example:** A webhook triggers an automation when a new tenant is created, provisioning a starter app

**Webhooks**

- **What they are:** HTTP callbacks that Qlik Cloud sends to your endpoint when specific platform events
  occur
- **Common events:** App created/deleted, reload finished/failed, user added/removed, space created
- **Use cases:** Triggering CI/CD pipelines on app changes, alerting external systems to reload failures,
  building event sourcing for multi-tenant observability
- **Note:** Events don't contain full object metadata; supplement with a real-time API call to the relevant
  service before the asset may be deleted

**Platform Operations APIs**

- **What it is:** APIs for creating, configuring, and managing tenants
- **Features:** Automated provisioning, configuration management
- **Benefits:** Programmatic control over tenant lifecycle
- **Developer implementation:** Qlik Cloud Platform Operations APIs, tenant management endpoints

**Application deployment**

- **What it is:** APIs for deploying and managing applications
- **Features:** Bulk deployment, version control, rollback
- **Benefits:** Automated application lifecycle management
- **Developer implementation:** Qlik Cloud Apps API, CI/CD integration, automated deployment pipelines

## Data concepts

### Data pipelines

**Data pipelines**

- **What they are:** Automated processes for moving and transforming data
- **Features:** Extract, transform, load (ETL) operations, scheduling, monitoring
- **Benefits:** Automated data flow, reduced manual intervention
- **Developer implementation:** Qlik Cloud Data Integration, pipeline orchestration, monitoring APIs

**Data integration**

- **What it is:** Connecting and combining data from multiple sources
- **Features:** Real-time and batch processing, data transformation, quality checks
- **Benefits:** Unified data view, improved data quality
- **Developer implementation:** Qlik Cloud Data Integration platform, transformation tools
- **Example:** Connect to customer databases, transform data, and load into Analytics or AI applications

## Management concepts

### Backup and recovery

**Backup strategies**

- **What they are:** Procedures for protecting application templates and customer data
- **Features:** Automated scheduling, version control, disaster recovery
- **Benefits:** Data protection, rapid recovery, business continuity
- **Developer implementation:** Qlik Cloud APIs for backup, automation templates, Qlik-managed disaster
  recovery

**Recovery procedures**

- **What they are:** Processes for restoring applications and data after incidents
- **Features:** Template-based recovery, selective restoration, disaster recovery
- **Benefits:** Minimal downtime, data integrity, business continuity
- **Developer implementation:** Qlik Cloud APIs for restoration, infrastructure resilience managed by Qlik

### Monitoring and observability

**System monitoring**

- **What it is:** Tracking system health and performance across tenants
- **Features:** Infrastructure monitoring, resource utilisation, alerting
- **Benefits:** Proactive issue detection, capacity planning
- **Developer implementation:** Qlik Cloud resource monitoring APIs, infrastructure health checks

**Resource governance**

- **What it is:** Managing resource consumption and performance across tenants
- **Features:** Application sizing, data refresh optimisation, performance monitoring
- **Benefits:** Predictable resource usage, cost control, optimal performance
- **Developer implementation:** Qlik Cloud resource monitoring APIs, application sizing tools, performance
  analytics

### Monitoring apps

**Qlik Cloud monitoring apps suite**

- **What they are:** A set of open source Qlik Sense applications maintained by Qlik that provide
  comprehensive visibility into usage, performance, and health across one or more tenants
- **Where to get them:** [qlik-cloud-monitoring-apps](https://github.com/qlik-oss/qlik-cloud-monitoring-apps),
  deployable programmatically using the Multiple Tenant Installer automation
- **Best practice:** Deploy to a single dedicated tenant to simplify secret management for the cross-tenant
  data store

| App                     | What it monitors                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| **App Analyzer**        | Application performance, load times, data refresh rates, user engagement, orphaned connections |
| **Reload Analyzer**     | Reload success rates, execution times, failure diagnostics, duration trends                    |
| **Automation Analyzer** | Automation execution, success rates, failure diagnostics                                       |
| **Answers Analyzer**    | Qlik Answers usage patterns, knowledge base sizes, question types                              |
| **Report Analyzer**     | Report generation volume, execution durations, breakdowns by app and executor                  |
| **Access Evaluator**    | User access patterns and permissions                                                           |
| **OEM Dashboard**       | Single-pane multi-tenant view: usage, trends, and health across all customer tenants           |

**Data Capacity Reporting App**

- **What it is:** The official capacity consumption report for OEM partners on capacity-based subscriptions,
  showing usage relative to purchased entitlements across all tenants
- **How it works:** Consolidates data from across your tenants; deployable on a schedule using the
  Consumption app deployer automation

**Qlik Answers**

- **What it is:** Qlik Cloud's AI-powered question-and-answer service, backed by knowledge bases of indexed
  documents
- **Relevance for OEM:** Qlik Answers usage (questions asked, pages indexed) is a metered entitlement that
  must be monitored; knowledge base storage grows over time and should be reviewed monthly
- **Monitoring:** Answers Analyzer app; automated entitlement management via Qlik Automate when usage limits
  are approached

## Multi-tenant concepts

### Tenant management

**Tenant provisioning**

- **What it is:** Creating and configuring new customer environments
- **Features:** Automated setup, template deployment, user management
- **Benefits:** Scalable customer onboarding
- **Developer implementation:** Qlik Cloud Platform Operations APIs, tenant provisioning workflows

**Template deployment**

- **What it is:** Deploying standardised applications across tenants
- **Features:** Version control, automated deployment, customisation
- **Benefits:** Consistent customer experience
- **Developer implementation:** Qlik Cloud Apps API, CI/CD integration, automated deployment workflows

### Data architecture patterns

**Single model with logical separation**

- **What it is:** One application serves multiple customers with data filtering
- **Benefits:** Simplified maintenance, cost-effective for large shared models such as benchmarking data
- **Use cases:** Similar data structures, limited sensitive data
- **Developer implementation:** Qlik Sense section access for data filtering

**Template-based per-customer models**

- **What it is:** Each customer gets their own application instance
- **Benefits:** Complete isolation, customisation flexibility
- **Use cases:** Different data structures, limited shared data per customer, compliance requirements
- **Developer implementation:** Qlik Cloud Apps API, automated deployment from templates, CI/CD pipelines

### Reload architecture patterns

**Distributed reloads: direct data access**

- **What it is:** Each customer tenant connects directly to the data source, typically over the public
  internet with IP whitelisting
- **Best for:** All data volumes, scalable cloud data sources, data not behind a firewall
- **Benefits:** Full tenant isolation, no central dependency, no infrastructure cost

**Distributed reloads: distributed data access**

- **What it is:** A source tenant (accessible only to the OEM) connects to private data via a gateway,
  stages data to cloud storage, and customer tenants load from that storage
- **Best for:** Data behind a firewall that cannot be exposed publicly, medium data volumes
- **Benefits:** Single data access point for sensitive sources, each customer tenant remains independently
  isolated

**Centralised reloads**

- **What it is:** A source tenant loads data and the full Qlik Sense app is exported and moved to each
  customer tenant by third-party tooling
- **Best for:** Fewer customers, common datasets across all customers (such as benchmark data), or no access
  to cloud storage
- **Benefits:** All credentials managed in one place, simpler for small estates

## Performance and scalability concepts

### Associative model benefits

**The associative difference**

- **What it is:** Qlik's fundamental architectural distinction from SQL-based analytics tools. Rather than
  executing queries against a database at interaction time, Qlik loads all relevant data into memory at
  reload time and builds a complete index of every field value and every relationship across the entire
  dataset. User interactions resolve against this in-memory index: no SQL is generated, no database is
  queried, no join is re-executed
- **Why it matters for OEM:** You define the data model once. Every analytical path, every combination of
  filters, drill-downs, comparisons, and cross-table lookups your users might want, is available without you
  having to anticipate and pre-build it. This is the core reason Qlik is not a SQL generator: SQL generators
  still run queries per interaction and are limited to paths the developer has defined. Qlik's associative
  engine makes paths that were never explicitly defined work automatically
- **The "green, white, grey" model:** When a user makes a selection, the engine instantly categorises every
  value in every field across the model: selected (green), associated but not selected (white), or excluded
  (grey). This state is resolved in memory across all tables simultaneously. Users see at a glance what is
  related and what is not, across the entire dataset, with no round-trip to any external system
- **Developer benefit:** Dramatically reduces the surface area of what you need to build and maintain. No
  need to design query layers, aggregation APIs, or drill-path logic for each user journey. The analytical
  flexibility is structural, not implemented feature by feature

**Natural data exploration**

- **What it is:** Users can follow any analytical path through the data without a developer having to
  pre-define that path as a query, report, or dashboard
- **Benefits:** No SQL knowledge required for users; no query design required from developers for each use
  case; users can discover relationships in data that were not part of the original dashboard design
- **Developer benefit:** Ship one well-designed data model rather than a library of purpose-built queries
  and reports. Customer analytics needs that were not anticipated at build time can be self-served from
  the loaded model without additional database calls

**Consistent in-memory performance**

- **What it is:** Because all data is in memory and pre-indexed, query response time is governed by CPU and
  memory rather than by database load, network latency, or query complexity. Performance is consistent
  regardless of how many users are active or how complex a selection is
- **Benefits:** No database scaling required to handle user concurrency; no query optimisation required per
  visualization; analytic performance does not degrade as usage grows
- **Developer benefit:** Simplified infrastructure: the analytics tier scales independently of the data tier.
  You do not need to tune queries, add database replicas, or manage cache invalidation to maintain responsive
  analytics for your customers

### Resource governance

**Application sizing**

- **What it is:** Managing application size and memory usage
- **Focus areas:** Data volume, model complexity, refresh performance
- **Benefits:** Predictable resource usage, control of consumption of entitlement
- **Developer implementation:** Qlik Cloud resource metadata APIs, application sizing tools, alerting
  capabilities

**Data refresh optimisation**

- **What it is:** Efficient data loading and processing
- **Focus areas:** Refresh scheduling, data source performance
- **Benefits:** Fresh data with less database impact, while serving cache from memory for optimal end user
  performance
- **Developer implementation:** Qlik Cloud Reload API, automated refresh scheduling, performance monitoring

**Large app support**

- **What it is:** A Qlik Cloud space configuration that allows applications exceeding the standard in-memory
  tier limits (5, 10, or 15 GB depending on subscription) to be opened
- **When needed:** Only when apps cannot be refactored to stay within standard limits through data modelling
  improvements or app chaining
- **Note:** More cost-effective to design apps that stay within standard tiers using patterns like app
  chaining, summary-detail, or incremental loads

## Development workflow concepts

### Development environments

**Development, Test, Acceptance, Production**

- **What it is:** A structured set of stages that application changes pass through before reaching customers:
  Development, Test, Acceptance, and Production
- **How it is implemented in Qlik Cloud:** A single non-production tenant uses spaces to represent
  Development, Test, and Acceptance stages; Production runs on separate per-customer tenants on a separate
  subscription
- **Why separate subscriptions:** Protects production entitlements from being consumed by development
  activity

**Commit space**

- **What it is:** A managed space in the non-production tenant that acts as the trigger point for the
  version control workflow. A developer publishes an app here, automation exports it to version control,
  and the app is then deleted
- **Purpose:** Transient staging only; keeps the space clean and purpose-focused; decouples the development
  flow from the CI/CD trigger

**Test space and Acceptance space**

- **Test space:** A managed space where apps are automatically promoted from version control on each PR,
  enabling integration testing and app evaluation before human review
- **Acceptance space:** A managed space where apps land after a PR is merged to main, giving stakeholders
  a final sign-off environment before production deployment

### Version control integration

Version control can be applied to any Qlik Cloud resource: Qlik Sense apps, data projects, automations,
themes, extensions, and more. The principles are the same across all resource types. Qlik Sense apps receive the
most attention here because they typically contain the most complex business logic and are the highest-value
artifacts to track, review, and roll back.

**App unbuild**

- **What it is:** The process of decomposing a binary `.qvf` file into its constituent text-based
  components: load script, app properties, sheets, objects, master items, variables, and images, for storage
  in version control
- **Why it matters:** Binary `.qvf` diffs are unreadable; unbuilt components produce meaningful text diffs
  that reviewers can understand. For example,
  [this pull request](https://github.com/qlik-oss/qlik-cloud-app-analyzer/pull/56/files) in the Qlik Cloud
  App Analyzer repo shows what standard GitHub review looks like with an unbuilt app: the `.qvf` binary
  carries no reviewable diff, but the unbuilt `script.qvs` shows exactly which load script lines changed,
  and `variables.json` shows the variable additions clearly. Other resource types such as data projects and
  automations are already stored in text-based formats and can be committed directly
- **How it works:** Import the app via the [Apps API](https://qlik.dev/apis/rest/apps/), then use the
  [Engine API](https://qlik.dev/apis/json-rpc/qix/) to extract each component. The
  `app unbuild` command in qlik-cli is one example implementation, but you can achieve the same result with
  any language or toolchain using raw API calls
- **Recommendation:** Build your unbuild process around the APIs directly so you control the output
  structure and are not tied to a specific tool. The environments guide includes a
  [reference GitHub Actions implementation](https://qlik.dev/manage/oem/product-development/dtap-environments/#example-github-actions-unbuild-workflow)
  using qlik-cli as a starting point, not a prescription

**Stepped rollout**

- **What it is:** A staged production deployment strategy where changes are released to an increasing
  percentage of customer tenants, with validation between each step
- **Typical stages:** Pilot (1-3 tenants), Limited (10-20%), Broad (50%), Full (100%)
- **Purpose:** Limits blast radius if a deployment has unexpected issues; allows human review at
  each gate

**Relative data connection names**

- **What they are:** Data connection references in load scripts that omit the space name (using
  `lib://:ConnectionName/`) so the app connects to whichever connection by that name exists in its current
  space
- **Why they matter:** The same app template can move between Development, Test, Acceptance, and Production
  spaces without any script changes. Each space has its own connection with the same name pointing to the
  appropriate data source

### Development observability

**Application monitoring**

- **What it is:** Tracking application performance and usage across tenants
- **Features:** Built-in monitoring apps, custom dashboards, alerting
- **Benefits:** Proactive issue detection, performance optimisation
- **Developer implementation:** Qlik Cloud Monitoring Apps, App Evaluation API
- **Example:** A webhook triggers an automation when a new application version is deployed, triggering a
  performance evaluation of the application

**User activity tracking**

- **What it is:** Monitoring user engagement and feature usage
- **Features:** Usage analytics, user behavior tracking
- **Benefits:** Product insights, user experience optimisation
- **Developer implementation:** Qlik Cloud usage analytics APIs, user behavior tracking, custom reporting
- **Example:** Track which sheets users interact with most to optimise dashboard design

### Version control and CI/CD

**Application lifecycle**

- **What it is:** Managing applications through development, testing, and production
- **Features:** Version control, automated deployment, rollback
- **Benefits:** Consistent deployments, reduced errors
- **Developer implementation:** Qlik Cloud Apps API, Git-based workflows, automated deployment pipelines

**Template management**

- **What it is:** Maintaining standardised application templates
- **Features:** Version control, automated deployment, customisation
- **Benefits:** Consistent customer experience, efficient maintenance
- **Developer implementation:** Qlik Cloud Apps API, template-based deployment pipelines, version control

## Privacy and security concepts

**Tenant encryption**

- **What it is:** Every Qlik Cloud tenant encrypts data at rest by default. Optionally, you can bring your
  own encryption key (BYOK) for scenarios with stricter key management requirements, for example HIPAA
- **Developer implementation:** Customer-managed encryption keys configured via the Qlik Cloud
  administration console or APIs

**Secret rotation**

- **What it is:** The process of periodically replacing secrets (OAuth client secrets, API keys, automation
  execution tokens) across your tenants to limit exposure windows
- **Key patterns:**
  - *OAuth client secrets:* create a new secret alongside the existing one, cut services across, then delete
    the old secret
  - *API keys:* create a new key, migrate consumers, delete the old key (or let it expire)
  - *Automation execution tokens:* duplicate the automation (which generates a new token), update callers,
    delete the original
- **Developer benefit:** A consistent rotation approach prevents service interruptions and maintains
  compliance

**Tenant deactivation and purge**

- **What they are:** A two-phase offboarding process for removing a customer's environment at the end of
  their contract
  - *Deactivation:* blocks all logins and pauses all activity; tenant remains recoverable for 10-90 days
  - *Purge:* permanently and irreversibly removes all content, credentials, and usage history from
    Qlik Cloud
- **Developer responsibility:** Export any audit logs or usage data needed for compliance before purge;
  revoke secrets used by the tenant in your own systems as part of offboarding

**Data residency**

- **What it is:** The requirement that data remains within a specific geographic region or jurisdiction
- **How Qlik Cloud addresses it:** Each Qlik Cloud region is a physically distinct AWS deployment; tenants
  cannot be migrated between regions; regional deployment gives you control over where each customer's data
  resides
- **Compliance note:** Review the [Qlik Trust page](https://www.qlik.com/us/trust) for current regional
  coverage and certifications

## Tools and frameworks

**@qlik/api**

- **What it is:** Qlik's TypeScript/JavaScript library for communicating with the Qlik Associative Engine
  and accessing all Qlik Cloud REST APIs
- **Key capabilities:** Open apps, read and write data models, manage selections, fetch hypercube data,
  automate platform operations
- **When to use:** Custom analytics experiences, app chaining selection sync, platform automation from
  JavaScript/TypeScript
- **Documentation:** [@qlik/api overview](https://qlik.dev/toolkits/qlik-api/)

**qlik-cli**

- **What it is:** A command-line interface for Qlik Cloud providing access to public APIs through the
  command line, covering both REST API operations and Engine API operations
- **Key capabilities:** App import/export/unbuild, context management across multiple tenants, raw API
  calls, scripting for CI/CD pipelines
- **Common use in OEM deployments:** Driving the unbuild step in GitHub Actions workflows, scripting tenant
  setup, app lifecycle management in CI/CD
- **Cross-platform:** Supports both Qlik Cloud and Qlik Sense Enterprise Client-managed
- **Documentation:** [qlik-cli overview](https://qlik.dev/toolkits/qlik-cli/)

**Other SDKs and libraries**

For teams working outside JavaScript/TypeScript, Qlik provides additional libraries for Engine API access.
Start with [@qlik/api](https://qlik.dev/toolkits/qlik-api/) if possible; use these when your language or environment
requires it:

- [enigma-go](https://qlik.dev/toolkits/enigma-go/) - Engine API access for Go
- [enigma.js](https://qlik.dev/toolkits/enigma-js/) - Low-level Engine API access for JavaScript, without the higher-level
  abstractions in @qlik/api
- [Qlik Sense .NET SDK](https://qlik.dev/toolkits/net-sdk/) - Engine API and REST API access for C# and .NET
- [Platform SDK](https://qlik.dev/toolkits/platform-sdk/) - Tenant and platform management APIs for JavaScript/TypeScript
  and Python

**No-code (Qlik Automate)**

- **What it is:** Qlik's visual no-code interface for building automated analytics and data workflows
  without writing code
- **Key capabilities:** Pre-built connector marketplace, template library for common operations, webhook
  triggers, integration with external systems
- **When to use:** Rapid deployment of tenant lifecycle automation, teams without DevOps expertise, or as
  the Qlik-specific operations layer within a broader CI/CD pipeline
- **Documentation:** [No-code overview](https://qlik.dev/toolkits/no-code/)

## Next steps

**Ready to start designing?** → [Solution architecture](https://qlik.dev/manage/oem/solution-architecture/)
