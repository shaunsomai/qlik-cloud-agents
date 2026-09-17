---
source: https://qlik.dev/manage/platform-operations/
last_updated: 2026-05-27T18:16:42+01:00
---

# Overview

For software companies interested in embedding analytics into their SaaS
solutions, they want the data & analytics platform to provide onboarding capabilities
that can be integrated into their own onboarding flows so that the customer
receives the full platform experience from the point of purchase.

If you are an Independent Software Vendor (ISV), Digital Native Business (DNB), or
OEM partner, consider first reviewing the [OEM and ISV Playbook](https://qlik.dev/manage/oem).

For Enterprises wishing to deploy multi-region, continuous integration / continuous
deployment (CICD) or version control patterns, they want the platform to provide
a range of integration points required that allow the flexibility to support
their particular business structure and requirements.

Qlik Platform Operations provides this flexibility via both pro-code (APIs
and programming toolkits) and no-code (via Qlik Automate) methods,
which this series of tutorials will leverage.

## Who this is relevant for

These tutorials are focused on how to deploy and manage multiple tenants, but
the concepts will also apply to single tenant use cases which serve multiple
user groups within an organization.

![Chart of multitenant use cases, showing both single and multiple tenant use cases](https://qlik.dev/_astro/multitenant_use_cases.LUMYyIWx.png)

Example use cases where a single tenant are appropriate include deploying CICD
(Dev/ Test/ Acceptance/ Prod - DTAP) across multiple business units, departments,
or teams within a single organization, and embedding Qlik Analytics into internal
portals. In these scenarios, you will normally deploy spaces within your Qlik Cloud tenant
to ensure logical isolation of content within that tenant, versus deploying new
tenants to implement complete isolation of content and users.

Any use case where users from different organizations need to access content
will require multiple tenants. There are also requirements in some embedded and
DTAP use cases within a single organization which will drive a preference or need
for multiple tenants.

![Diagram of single tenant and multitenant architectures](https://qlik.dev/_astro/multitenant_architectures.ziU1gXU-.png)

Qlik Cloud has been built with a set of APIs that allow provisioning,
configuration, and hydration of Qlik Cloud tenants to serve automated deployment
pipelines alongside your software, development, and customer lifecycles.

The tutorials in this section provide information on how to leverage Qlik Cloud
to support your use cases, as well as covering
important considerations for your deployments. The topics and terminology below
will be explored in more detail as you progress through the tutorials.

## Qlik Cloud's multitenant model

Where you need to provide solutions to one or multiple users from distinct
companies or organizations, you should deploy a multiple tenant solution in
Qlik Cloud. Each tenant is deployed to serve each of these distinct sets of
users, whether that be several, or tens of thousands of sets of users, and
therefore tenants.

If you are deploying to a single organization, you can accommodate multiple teams
and user groups in a single tenant, as Qlik Cloud offers logical separation
of content via [spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm)
for this use case.

Some example deployment use cases for Qlik Cloud leveraging the multiple tenant
pattern include:

- A wealth management firm providing analytics embedded within their customer
  portal, allowing their customers (single user individuals or multi-user
  organizations) to view up-to-date account performance.
- A software company producing fitness and wellness mobile software where they
  provide analytics to their end users (single user individuals) in their mobile
  app.
- A logistics firm leveraging Qlik Analytics for providing tracking analytics to
  their customers (single user individuals or multi-user organizations) via
  embedding analytics in their public website.

Qlik Cloud's multiple tenant deployment pattern is an architecture where a Qlik
partner receives a single entitlement (also known as license), which represents
an organization inside Qlik Cloud. Within this organization, you can deploy
multiple tenants - each a distinct logical instance. Although these tenants are
linked to your organization, they are separate, so you will need to configure
and hydrate these tenants independently.

## Why deploy a tenant per customer?

The entitlements on a Qlik Cloud subscription (for example, the number of
Automate runs that you are permitted to execute) are shared
across tenants in a multiple tenant deployment.

Beyond this entitlement information, each tenant within Qlik Cloud provides
logical separation of users, configurations, data, credentials, content, and any
other assets that you or your users might wish to deploy.

Within a tenant, different asset classes are secured at different levels. For
example:

- Users and user metadata are secured at the tenant level. This means users can
  list and assign content to each other within a tenant for collaboration.
- Extensions and themes are secured at the tenant level. All users have access
  to these components to ensure consistent in-app experiences.
- QlikView and Qlik Sense applications are secured at the space (or user/ group
  share) level. Users must be provided access to the space or to the app to know
  of an app's existence and access it.
- Data connections and data files are secured at the space level. Users
  must have the correct roles assigned in the space in which the assets are located
  to access and consume them.
- Data alerts are secured at the user level, with only the owning user able to manage
  the alert definition (but notifications can be sent to
  other users on evaluation).
- API keys are secured at the user level, with only the owning user able to manage
  the API key.

If you have requirements around securing any tenant-level assets such as users
and user metadata, extensions, themes, then you must leverage a multiple
tenant pattern. You should not deploy multiple organizations to a single Qlik
Cloud tenant.

Other benefits of deploying a tenant per organization include:

- Ability to deploy different IdP configurations per organization.
- Ability to encrypt each organization's data with a separate key.
- Ability to customize the tenant to that organization, for example, through the
  deployment of organization-specific themes or extensions and naming conventions.
- Bypassing single-tenant guardrails, such as limits on the number of spaces, shares,
  report generations, etc.

## Entitlements

Qlik products require entitlements (also known as a license or subscription),
which specify what features of the product are available to a partner. Some
examples of attributes set in an entitlement include:

- Number of professional or analyzer user seats that can be assigned to users
  (for example, 100 professional and 100 analyzer licenses).
- Number of Qlik Cloud tenants that can be provisioned (for example, 1 tenant or
  1,000 tenants)
- Which product features you have access to (for example, access to AutoML and
  Qlik Automate).
- Which tiers of certain products you have access to, such as a paid tier for
  Automate or Reporting Service.

In Qlik Cloud, all tenants in an organization share the same Qlik entitlement.
This means that all attributes of that entitlement will be shared across all
tenants, and by design, any tenant within the organization can request resources
from the entitlement.

As an example, if the entitlement permits you an allowance of up to 10
professional user licenses across 5 tenants, it would be possible to assign all
10 user licenses to a single tenant, leaving no professional licenses for the
other 4 tenants. As such, you must manage these resources during your
provisioning workflows, through disabling settings such as automatic license
assignment.

While each tenant within an organization is logically separated and data and
logs are kept separate, the shared entitlement will mean that a user with access
to the management console on any tenant in the organization will be able to view
the full list of users and any assigned licenses for that organization. This
means that you should not provide access to the management console to your end
customers or users.

## Programmatic provisioning, configuration & hydration in Qlik Cloud

To support the creation, configuration, and hydration of tenants for end
customer onboarding in your applications, this series of tutorials demonstrates
how the APIs can be used to:

- Create a new tenant.
- Configure the new tenant, including:
  - Configure an identity provider, typically either JSON Web Token (JWT) where
    integrating with existing applications, or an interactive provider such as
    Azure AD for other use cases.
  - Pre-provision groups for access control.
  - Configure license and role allocations.
  - Create and configure security on spaces (logical buckets within a tenant for
    securing content).
  - Configure web origin and content security policies for use with integrations
    or embedding.
- Deploy content to the tenant, including:
  - Import visualization extensions, themes and other content types required to
    provide customization of Qlik applications.
  - Import and stage Qlik applications in a shared space.
  - Publish staged applications to production-managed spaces.
  - Republish updated applications.
  - Deploy automations that automatically add new users to spaces (relevant if
    groups are not provided by your IdP for access control).

In addition to raw APIs, Qlik provides
the [Platform Operations connector](https://qlik.dev/toolkits/no-code/)
in [Qlik Automate](https://www.qlik.com/us/products/qlik-automate).
This provides you with a no-code method for deploying and managing content
across your Qlik Cloud estate.

## Next steps

The first step in orchestrating the platform is to generate credentials
for OAuth clients, which you'll use to programmatically authenticate to your
tenants. Learn how to [authenticate
for Platform Operations](https://qlik.dev/manage/platform-operations/authenticate-platform-ops).
