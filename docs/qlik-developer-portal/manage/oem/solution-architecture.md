---
source: https://qlik.dev/manage/oem/solution-architecture/
last_updated: 2026-05-27T18:16:42+01:00
---

# Solution architecture overview

Before you start building, there are six architectural decisions to make. Getting these right
up front avoids costly rework - they influence each other and, together, determine how you build
every component of your integration.

## The six decisions

**Tenancy model:** Decide whether each customer gets their own isolated Qlik Cloud tenant, or
whether multiple customers share one. This choice drives data isolation, compliance posture,
customization flexibility, and how you manage the lifecycle of each deployment.
Most production OEM deployments use a tenant per customer. See
[Single vs. multiple tenants](https://qlik.dev/manage/oem/solution-architecture/single-multi-tenant/).

**Access route:** Decide whether analytics appear embedded inside your application using
[qlik-embed](https://qlik.dev/embed/qlik-embed/) web components, or whether users are given a direct link
to the Qlik Cloud hub. Embedding takes more development effort but keeps users in your product
and hides the Qlik-hosted interface. Native access requires minimal code but gives users a
Qlik-branded experience. A hybrid of both is also valid for different user segments.
See [Embedded vs. native experience](https://qlik.dev/manage/oem/solution-architecture/access-route/).

**Branding:** Decide how much of the Qlik interface your customers will see and what you want
to replace. Tenant-level branding (logo, favicon, color) is applied via API. App-level theming
controls colors and fonts inside Qlik Sense applications. The available options differ between
embedded and native access patterns, so this decision connects back to your access route choice.
See [Brand Qlik Cloud](https://qlik.dev/manage/oem/solution-architecture/brand-customize/).

**Data modeling:** Decide how Qlik Sense applications are structured: whether all customers
share a single app with row-level security, or each customer gets a template instance with
isolated data. This affects both security and your ability to customize the experience per customer.
See [Data modeling](https://qlik.dev/manage/oem/solution-architecture/data-modeling/).

**Data architecture:** Decide how your customers' data lands in Qlik Cloud - whether each
tenant reloads from a data source directly, whether you stage data centrally and distribute it,
or whether you land it in cloud storage close to each tenant. This decision sets your reload
complexity, concurrency requirements, and cost profile.
See [Data architecture](https://qlik.dev/manage/oem/solution-architecture/data-architecture/).

**Automation strategy:** Decide how you automate tenant provisioning and updates across your
customer base. Qlik Automate provides no-code workflow templates that cover the most common
operations out of the box. As your maturity grows, you can layer in CI/CD pipelines that trigger
Automate workflows or call Qlik's REST APIs directly.
See [Design automation](https://qlik.dev/manage/oem/solution-architecture/design-automation/).

## Working through the decisions

The decisions are not independent - your tenancy model shapes what branding options make sense,
your data architecture constrains what modeling approaches are practical, and your automation
strategy determines how much development investment you'll need for ongoing operations.
Work through them in the order presented in the playbook, revisiting earlier choices as later
ones reveal constraints.

## Next steps

Start with the foundational choice: [Single or multiple tenants](https://qlik.dev/manage/oem/solution-architecture/single-multi-tenant/)
