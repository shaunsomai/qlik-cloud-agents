---
source: https://qlik.dev/manage/platform-operations/authenticate-platform-ops/
last_updated: 2026-05-27T18:16:42+01:00
---

# Authenticate for Platform Operations

## Generate OAuth credentials

The primary method used to authenticate for Platform Operations is OAuth2.
Specifically, you need to generate a machine-to-machine OAuth client - these are
available at [multiple tiers in Qlik Cloud](https://qlik.dev/authenticate/oauth/#what-oauth-client-tiers-are-available-for-registration),
depending on your subscription.

> **Note:** This section relates to the use of machine-to-machine OAuth to support Platform Operations.
> For a general overview of OAuth, refer to the [OAuth2 Overview](https://qlik.dev/authenticate/oauth/).

Tenant provisioning is handled by [My Qlik](https://account.myqlik.qlik.com/account), the
subscription management portal for Qlik Cloud. If you are entitled to a single
tenant, then you will use this portal to create your tenant interactively, before
logging into that tenant to create an OAuth client to continue with this
tutorial series. If you are entitled to multiple tenants, then the portal will
be used to procure region level OAuth clients for your entitlement.

If you are planning to deploy multiple tenants and you haven't used these features
before, please reach out to your Qlik account manager as it's likely that you
will need changes made to your Qlik entitlement before you begin.

## How to create a tenant level OAuth client

If you have only one tenant, then you will want to create a tenant level OAuth
client. First ensure the tenant has been created and sign in to it with a user
assigned with a TenantAdmin role.

Then review the [create a new OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client) guide.

## How to create a region level OAuth client

If you will have more than one tenant, create a region level OAuth client. You need
to be the Service Account Owner of a subscription with an entitlement for more than one
tenant.

Learn how to [create a region level OAuth client](https://qlik.dev/authenticate/oauth/create/create-region-oauth-client)
in My Qlik.

## How to create an organization-level OAuth client

If you manage tenants across multiple subscriptions or regions, create an
organization-level OAuth client.
These clients are managed from the Cloud console at
[https://console.qlikcloud.com](https://console.qlikcloud.com) rather than from My Qlik, which
is why they are sometimes referred to as Cloud console OAuth clients.

Organization-level OAuth clients authenticate against the
[Organization REST APIs](https://qlik.dev/apis/org-rest/), which expose a single endpoint to list all tenants
across all your subscriptions and regions. You can filter the results by subscription, region,
or status from there, giving you a complete inventory of your tenant estate without querying
subscriptions one by one.

Only the Service Account Owner (SAO) of a subscription can create and manage organization-level
OAuth clients.

Learn how to [create an organization-level OAuth client](https://qlik.dev/authenticate/oauth/create/create-organization-level-oauth-client).

## Next steps

To begin the provisioning workflow and start spinning up tenants with code, see [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant).

If you prefer a no-code workflow, begin your journey with
the [Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview).
