---
source: https://qlik.dev/manage/platform-operations/delete-a-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Delete a tenant

## Overview

In an earlier tutorial step, you [created a new tenant](https://qlik.dev/manage/platform-operations/create-a-tenant) in Qlik Cloud as
part of new customer provisioning.

In this tutorial, you are going to delete this tenant programmatically to support
customer offboarding, ensuring that all data, users, and apps are removed
from Qlik Cloud.

For more information on how to manage the deletion of tenants, how the
deactivation and purge period work, and how to reactivate a tenant before the
estimated purge date, see [Deactivate and delete tenants](https://qlik.dev/manage/tenants/delete-tenants).

> **Warning:** Deleting a tenant is permanent.
> Once a tenant has been purged from Qlik Cloud, neither you nor Qlik can restore its data.\
> Use this capability with caution.

> **Note:** A region level OAuth client is required to request the deletion of tenants.

## Code examples

Code examples for bash are included in this tutorial.

## Prerequisites

- A tenant that you wish to delete
- A region level OAuth client
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
| `<TARGET_TENANT>`         | The domain for the tenant that this tutorial will request deletion for. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                          |
| `<TARGET_TENANT_ID>`      | The Qlik Cloud ID for tenant `<TARGET_TENANT>`.                                                                                                                                         |
| `<REGISTRATION_TENANT>`   | The registration endpoint used for requesting deletion of Qlik Cloud tenants (the same as for creating new tenants). Equivalent to `register.<REGION>.qlikcloud.com`                    |
| `<REGION>`                | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore, and `us` for North America. |
| `<CLIENT_ID>`             | The client ID for an OAuth client, specific to the region or tenant you're sending requests to.                                                                                         |
| `<CLIENT_SECRET>`         | The client secret for the specific OAuth `<CLIENT_ID>`.                                                                                                                                 |
| `<REGISTER_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<REGISTRATION_TENANT>` endpoint.                                                                                                |

## 1 Generate credentials & retrieve an access token

Generate an access token for the `<REGISTRATION_TENANT>`. For a reminder of
how to do this, review [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant).

## 2 Deactivate the tenant

Deactivate the tenant by issuing a request to the tenant registration endpoint.

Include the `<TARGET_TENANT_ID>` in the URL, and the
`<TARGET_TENANT>` in the `qlik-confirm-hostname` header to confirm the tenant
that you wish to deactivate.

> **Note:** If you need to retrieve the tenant ID, review how to
> [obtain the tenant ID](https://qlik.dev/manage/platform-operations/configure-a-tenant/#obtain-the-tenant-id).

This example demonstrates a 10-day grace period after the API call is made before
the tenant is deleted. Once this period has passed, there will be no way of recovering
the tenant. You can set `purgeAfterDays` to a value between 10 and 90 days. If not
specified, the default is 30 days.

Using cURL, send the request:

```bash
curl -L "https://<REGISTRATION_TENANT>/api/v1/tenants/<TARGET_TENANT_ID>/actions/deactivate" ^
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

## 3 Send an API request to the tenant

To see the message that users will experience now that the tenant is deactivated,
send an API request to the tenant. This can be on any API, in this case on
the `oauth` API, attempting to request a new access token for the tenant.

```bash
curl -L "https://<TENANT>/oauth/token" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"client_id\": \"<CLIENT_ID>\", \"client_secret\": \"<CLIENT_SECRET>\", \"grant_type\": \"client_credentials\"}"
```

The result is a JSON object informing you that the tenant has been deactivated.

```json
{
    "errors": [
        {
            "title": "Tenant has been deactivated. Contact your administrator for more details.",
            "code": "TENANT_DEACTIVATED",
            "status": "401"
        }
    ],
    "traceId": "00000000000000009a3a5a25531c1e2d"
}
```

## Next steps

Now that you have learned how to orchestrate Qlik Cloud via raw APIs, consider
reviewing the [no-code pathway](https://qlik.dev/manage/platform-operations/no-code/overview) to manage tenants.
