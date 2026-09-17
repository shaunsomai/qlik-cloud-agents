---
source: https://qlik.dev/manage/tenants/delete-tenants/
last_updated: 2025-07-08T16:09:30Z
---

# Deactivate and delete tenants

> **Warning:** Deleting a tenant is permanent.
> Once a tenant has been purged from Qlik Cloud, neither you nor Qlik can restore its data.\
> Use this capability with caution.

## Overview

Tenants are the highest level of logical separation in Qlik Cloud available to
Qlik customers. When using a multitenant entitlement, you gain the ability to
programmatically create and delete tenants via API, which is not possible for
single tenant entitlements.

The most common use case for tenant deletion is in an OEM context where you
create a tenant per end customer and offboard customers and delete their tenant
as their contracts with you come to an end. To learn more about the lifecycle
of OEM in Qlik Cloud, review the [Platform Operations tutorial series](https://qlik.dev/manage/platform-operations/overview).

> **Note:** A region-level OAuth client is required to request the deletion of tenants.
> This is not available if you have a single tenant entitlement.

## Tenant deletion

Tenant deletion is a process that is designed to reduce the risk of accidental
data loss through human or system error.

The process is:

1. You send a request to the deletion endpoint. To do this, you will need:
   - Regional OAuth client credentials. For more information on these credentials,
     refer to the [Authenticate for Platform Operations guide](https://qlik.dev/manage/platform-operations/authenticate-platform-ops)
     and review how to deploy regional OAuth clients for the tenant which you wish to delete.
   - The hostname for the tenant which you wish to delete.
   - The tenant ID for the tenant which you wish to delete.
   - The number of days that the tenant will be in a deactivated state before being
     deleted. This can be 10-90 days; the default is 30 days.
2. At any point up until the estimated purge date (calculated using your input
   for the number of days the tenant will remain in deactivated state) you may
   reactivate the tenant or reset the countdown timer with no loss of data.
3. After the estimated purge date has passed, neither you nor Qlik will be able to
   retrieve any data from the tenant.

It is not possible to immediately delete a tenant from Qlik Cloud via this API;
the minimum purge delay is 10 days. If you require immediate removal,
contact Qlik.

## Entitlements and usage

If you have a limit on the number of tenants that can be created on your entitlement,
then each tenant deleted will permit you to create a new tenant to replace it.

Deleting a tenant will not deallocate user-based entitlements assigned on that
tenant - you should do this activity using
the [licenses API](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fassignments%2Factions%2Fdelete-post).
Any entitlements consumed in the month, such as Automate runs, will
still be counted in your overall monthly consumption.

## Prerequisites

- A regional OAuth client and a tenant that you wish to delete.
- Development environment or terminal for running examples on the command-line.
- cURL for running the inline examples.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable                  | Description                                                                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`                | The domain for the tenant that this tutorial will request deletion for. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                          |
| `<TENANT_ID>`             | The Qlik Cloud ID for tenant `<TENANT>`.                                                                                                                                                |
| `<REGISTRATION_TENANT>`   | The registration endpoint used for requesting deletion of Qlik Cloud tenants (the same as for creating new tenants). Equivalent to `register.<REGION>.qlikcloud.com`                    |
| `<REGION>`                | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore, and `us` for North America. |
| `<REGISTER_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<REGISTRATION_TENANT>` endpoint.                                                                                                |

## Generate credentials & retrieve an access token

To send tenant deactivation and reactivation requests, you require an access token
valid for the `<REGISTRATION_TENANT>`. These can be generated from the relevant
regional OAuth clients. For a reminder of
how to do this, review [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant).
Save the access token as `<REGISTER_ACCESS_TOKEN>`.

## Deactivating a tenant

To schedule a tenant for deletion, it must be deactivated. Deactivate the tenant
by issuing a request to the tenant registration endpoint, adding the following
information:

- The tenant ID, `<TENANT_ID>`, needs to be in the URL path.
- The tenant hostname, `<TENANT>`, needs to be in the `qlik-confirm-hostname` header
  to confirm the tenant that you wish to deactivate.
- If you wish to set a purge period different than the default of 30 days, you should
  set this value in the `POST` body in the `purgeAfterDays` attribute.

> **Note:** If you need to retrieve the tenant ID, review how
> to [obtain the tenant ID](https://qlik.dev/manage/platform-operations/configure-a-tenant/#obtain-the-tenant-id).

This example demonstrates a 10-day grace period after the API call is made before
the tenant is deleted. After this period has passed, there will be no way of recovering
the tenant. You can set `purgeAfterDays` to a value between 10 and 90 days.

Using cURL, send the request:

```bash
curl -L "https://<REGISTRATION_TENANT>/api/v1/tenants/<TENANT_ID>/actions/deactivate" ^
-H "Authorization: Bearer <REGISTER_ACCESS_TOKEN>" ^
-H "qlik-confirm-hostname: <TENANT>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{\"purgeAfterDays\": 10}"
```

The result is a JSON object confirming the new tenant state:

```json
{
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "status": "disabled",
    "estimatedPurgeDate": "2023-07-30T14:01:22.000Z"
}
```

The tenant will be permanently deleted from Qlik Cloud around
the `estimatedPurgeDate`. Until that date, you can re-enable the tenant.
For more information, see [Manage tenants](https://qlik.dev/manage/tenants).

## Reactivating a tenant

A tenant in the deactivated state can be reactivated at any point until the
estimated purge date, with no loss of data.

To reactivate a tenant, send the following request:

```bash
curl -L "https://<REGISTRATION_TENANT>/api/v1/tenants/<TENANT_ID>/actions/reactivate" ^
-H "Authorization: Bearer <REGISTER_ACCESS_TOKEN>" ^
-H "qlik-confirm-hostname: <TENANT>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The result is a JSON object informing you that the tenant has been reactivated.

```json
{
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "status": "active"
}
```

## Tracking tenant deletion events

If you schedule a tenant for deletion, attempting to access that tenant will result
in a message similar to:

```json
{
    "errors": [
        {
            "title": "Tenant has been deactivated. Contact your administrator for more details.",
            "code": "TENANT_DISABLED",
            "status": "401"
        }
    ],
    "traceId": "00000000000000009a3a5a25531c1e2d"
}
```

It will not be possible to access any data on this tenant while deactivated. If you
subsequently choose to reactivate the tenant, you will be able to review prior
deletion requests using the [Audits API](https://qlik.dev/apis/rest/audits) by filtering
on `eventType` of `com.qlik.v1.tenant.deactivated` for deactivations
and `com.qlik.v1.tenant.reactivated` for reactivations.

A deactivation event will appear as `com.qlik.v1.tenant.deactivated` with:

```json
{
    "hostnames": [
        "xzoau8xi93gyfo0.us.qlikcloud.com",
        "tenantname.us.qlikcloud.com"
    ],
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "name": "tenant name",
    "purgeAfterDays": "2023-07-30T04:31:29.000Z"
}
```

A reactivation event will appear as `com.qlik.v1.tenant.reactivated` with:

```json
{
    "hostnames": [
        "xzoau8xi93gyfo0.us.qlikcloud.com",
        "tenantname.us.qlikcloud.com"
    ],
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "name": "tenant name"
}
```
