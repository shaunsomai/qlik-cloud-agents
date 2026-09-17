---
source: https://qlik.dev/manage/key-concepts/
last_updated: 2026-04-20T13:34:03+01:00
---

# Key concepts

This page explains the core concepts you need before using Manage APIs at scale.

Your tenant URL has the form `yourtenant.region.qlikcloud.com` (for example `mycompany.us.qlikcloud.com`).
For URI structure and request model details, see [REST APIs - URI structure](https://qlik.dev/apis/rest/#uri-structure).

> **Choose the right interface pattern:** You can use different interfaces to manage the same platform capabilities:
> direct REST calls, the `@qlik/api` framework for typed calls and auth helpers,
> `qlik-cli` for shell automation, Qlik Automate for no-code orchestration,
> or MCP-based workflows for assistant-driven operations.
> See [REST APIs](https://qlik.dev/apis/rest/), [qlik-api overview](https://qlik.dev/toolkits/qlik-api),
> [qlik-cli](https://qlik.dev/toolkits/qlik-cli/), [No-code overview](https://qlik.dev/toolkits/no-code/),
> and [Qlik MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm).

## Tenant

A **tenant** is your Qlik Cloud instance. It is identified by a hostname such as
`mycompany.us.qlikcloud.com`. All users, spaces, apps, data connections, and
data files in that instance belong to the tenant. When you call Manage APIs,
you send requests to your tenant's base URL.

## Space

A **space** is a logical container within a tenant used to organize and secure
content. Spaces can be personal (undefined), shared, or managed. Data
connections, data files, and apps are stored in spaces. Access is controlled by
space-level roles. Most Manage API operations that create or list resources
require a space ID when the resource is space-scoped.

## Data connection

A **data connection** is a configured link from your tenant to an external data
source (for example a database, REST API, or cloud storage). Data connections
are stored in spaces and are used by Qlik Cloud Analytics apps and by Qlik
Talend Data Integration projects to load data. Each space has a built-in
**DataFiles** connection for uploaded files. You can create additional
connections for other sources.

## Data file

A **data file** is a file (such as CSV, XLSX, or QVD) that you upload or create
within a space. Data files appear in the DataFiles connection and in the
catalog. When you upload a data file, Qlik Cloud also creates catalog metadata
(data set) so the data can be discovered and used in apps.

For data files, catalog metadata is organized as follows:

- **Data store** - A top-level container. By default, a tenant has a data store
  named `DataFilesStore` that holds metadata for all data files across spaces.
- **Data asset** - A container within a data store, often corresponding to a
  space. Each space has a data asset under `DataFilesStore`.
- **Data set** - A single data source's metadata (for example one data file).
  Data sets belong to a data asset and contain field and schema information.

## Core REST API themes

All published Qlik Cloud REST APIs are listed in the
[REST API reference](https://qlik.dev/apis/rest/). Most Manage use cases align to a few common
patterns:

- **Identity and authorization**: Who can call which APIs, and with what scope.
- **Tenant and configuration management**: Tenant-level settings, features,
  governance controls, and deployment metadata.
- **Content and resource lifecycle**: Create, read, update, move, and delete
  resources such as spaces, apps, files, tasks, and reports.
- **Data and metadata management**: Connections, files, datasets, stores, assets, lineage graphs, and data products.
- **Operational reliability**: Pagination, filtering, retries, idempotent design, and rate-limit aware scripts.

When building automation, start with a small test sequence for each domain, then combine those sequences into broader
workflows. Before you automate at scale, see [API operations checklist](https://qlik.dev/manage/api-operations-checklist) for essential
pre-flight checks.

## Understanding authentication methods

Qlik Cloud offers three methods to authenticate API calls, each suited to different use cases:

- **OAuth SPA** (recommended for apps and interactive use): Generates short-lived access tokens
  and supports [scoped access](https://qlik.dev/authenticate/oauth/scopes/) to grant least privilege. Best for
  browser-based applications and interactive workflows. To get started, see
  [Create an OAuth SPA client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa).

- **OAuth M2M** (for server-side automation and bots): Designed for scripts, CI/CD pipelines, and
  multi-tenant provisioning. Uses OAuth credentials to generate access tokens for automation.
  For more information, see [Get started with OAuth machine-to-machine](https://qlik.dev/authenticate/oauth/getting-started-oauth-m2m)
  and [Authenticate for Platform Operations](https://qlik.dev/manage/platform-operations/authenticate-platform-ops).

- **API key** (for quick testing and one-off scripting): Simple to set up but less secure than OAuth.
  API keys cannot have scopes applied and grant full user-level access. Avoid for production
  automation. To get started, see [Generate your first API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key).
  > **Caution:** Avoid API keys with full user-level access as they increase risk: if exposed, they can be reused until rotated or
  > revoked. Because API keys do not support scopes, you cannot enforce least privilege.

For multi-tenant deployments and entitlements, see [Platform Operations overview](https://qlik.dev/manage/platform-operations/overview).
