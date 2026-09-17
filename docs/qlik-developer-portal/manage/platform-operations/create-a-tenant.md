---
source: https://qlik.dev/manage/platform-operations/create-a-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Create a tenant

## Create a tenant

Qlik Cloud enables partners to integrate the tenant provisioning process
directly into their onboarding flows with a tenant creation API endpoint. In
this tutorial, you are going to create a tenant programmatically.

> **Note:** A region level OAuth client is required to create new tenants.

## Code examples

Complete script examples for creating a tenant using qlik-cli, curl,
Python, and API collections are available
in the [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations).

## Prerequisites

- An OAuth client and existing source tenant
- Development environment or terminal for running examples on the command-line.
- cURL for running the inline examples.

> **Notes:**
>
> - The initial tenant that you created interactively
>   will be referred to as the `<SOURCE_TENANT>`. You can use the source
>   tenant to create Qlik Sense applications, data sets, and other assets (referred
>   to as `content`) for deployment to one or multiple end customer tenants referred
>   to as `<TARGET_TENANT>` through this tutorial series.
> - The cURL examples in this tutorial show the command syntax for
>   Windows Command Prompt. If you are using another command line interface,
>   different syntax may be required for line continuation. You may also need to
>   adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable                   | Description                                                                                                                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`          | The domain for the initial tenant created during account onboarding. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                            |
| `<TARGET_TENANT>`          | The domain for the new tenant that this tutorial will create. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                                   |
| `<TENANT_REGISTRATION>`    | The registration endpoint used for requesting new Qlik Cloud tenants. Equivalent to `register.<REGION>.qlikcloud.com`                                                                  |
| `<REGION>`                 | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore and `us` for North America. |
| `<CLIENT_ID>`              | The client ID for an OAuth client, specific to the region or tenant you're sending requests to.                                                                                        |
| `<CLIENT_SECRET>`          | The client secret for the specific OAuth `<CLIENT_ID>`.                                                                                                                                |
| `<SOURCE_ACCESS_TOKEN>`    | A bearer token for authorizing `https` requests to the `<SOURCE_TENANT>`.                                                                                                              |
| `<TARGET_ACCESS_TOKEN>`    | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`.                                                                                                              |
| `<REGISTER_ACCESS_TOKEN>`  | A bearer token for authorizing `https` requests to the `<TENANT_REGISTRATION>` endpoint.                                                                                               |
| `<SIGNED_ENTITLEMENT_KEY>` | The signed key required to create tenants, linked to your entitlement or subscription.                                                                                                 |

## 1 Generate credentials

Locate the `<CLIENT_ID>` and `<CLIENT_SECRET>` for the Qlik Cloud region you
wish to create the new tenant in.\
If you need new clients, review how to [generate OAuth credentials](https://qlik.dev/manage/platform-operations/authenticate-platform-ops) .

> **Note:** This tutorial assumes that you wish to create your new `<TARGET_TENANT>` in the same Qlik Cloud region as your
> existing `<SOURCE_TENANT>`.
> If these regions are different, you should modify the examples below to pass in the correct OAuth client
> (`<CLIENT_ID>` and `<CLIENT_SECRET>`) and region for each command.

## 2 Obtain the signed entitlement key

The `<SIGNED_ENTITLEMENT_KEY>` is needed to create additional tenants. To obtain the
`<SIGNED_ENTITLEMENT_KEY>`, you are going to request an access token from the
`<SOURCE_TENANT>`, and use that access token to request the `<SIGNED_ENTITLEMENT_KEY>`.

### Request an access token

> **Note:** Access tokens are scoped to individual tenants.
> This means that you need to retrieve an access token via the `/oauth/token` endpoint for each tenant.
>
> An access token that's generated for a given tenant can be used an unlimited number of times.
> However, the token expires six hours after its issued.
> If your scripts run longer than six hours you'll need to retrieve a new access token during script execution.

Request an access token from the `<SOURCE_TENANT>` using the `<CLIENT_ID>` and
`<CLIENT_SECRET>`, and OAuth `client_credentials` grant type in a JSON object:

```json
{
  "client_id": "<CLIENT_ID>",
  "client_secret": "<CLIENT_SECRET>",
  "grant_type": "client_credentials"
}
```

Send a request to the OAuth token endpoint on the `<SOURCE_TENANT>`:

```bash
curl -L -X POST "https://<SOURCE_TENANT>/oauth/token" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"client_id\":\"<CLIENT_ID>\", \"client_secret\":\"<CLIENT_SECRET>\", \"grant_type\":\"client_credentials\"}"
```

The result is a JSON object displaying the `<SOURCE_ACCESS_TOKEN>` for the
built-in user that represents the OAuth client that you used to make the
request. This built-in user is known as a `bot user`.

```json
{
  "access_token": "<SOURCE_ACCESS_TOKEN>",
  "token_type": "bearer",
  "expires_at": "2022-06-03T20:52:08.000Z",
  "expires_in": 21600
}
```

### Retrieve the signed entitlement key

To obtain the signed entitlement key, make a request to the `licenses/overview`
endpoint with the `<SOURCE_ACCESS_TOKEN>`:

```bash
curl -L "https://<SOURCE_TENANT>/api/v1/licenses/overview" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json"
```

The result is a JSON object containing the signed entitlement key:

```json
  {
    "licenseNumber": "012345678912345678",
    "licenseKey": "<SIGNED_ENTITLEMENT_KEY>",
    "valid": "./2023-05-30",
    "status": "Ok",
    "origin": "Internal",
    "updated": "0001-01-01T00:00:00Z",
    "trial": false,
    "allotments": [
    {
        "name": "professional",
        "usageClass": "assigned",
        "units": 25,
        "unitsUsed": 1,
        "overage": 0
    },
    ]...
  }
```

Record the `licenseKey` value as the `<SIGNED_ENTITLEMENT_KEY>` and
store it someplace safe for future use.

## 3 Obtain an access token for creating tenants

Creating tenants requires an access token from a publicly available
`<TENANT_REGISTRATION>` endpoint in each Qlik Cloud region. Once you obtain an
access token from the `<TENANT_REGISTRATION>` endpoint, you can contact the
endpoint to create new tenants.

To obtain an access token for creating tenants, issue a REST request to the
`<TENANT_REGISTRATION>` from the same region that you created the OAuth client ID
and secret in.

```json
  {
    "client_id": "<CLIENT_ID>",
    "client_secret": "<CLIENT_SECRET>",
    "grant_type": "client_credentials"
  }
```

Using cURL, send the request:

```bash
curl -L -X POST "https://<TENANT_REGISTRATION>/oauth/token" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"client_id\":\"<CLIENT_ID>\", \"client_secret\":\"<CLIENT_SECRET>\", \"grant_type\":\"client_credentials\"}"
```

The result is a JSON object with an access token that you will use to create a tenant:

```json
{
  "access_token": "<REGISTER_ACCESS_TOKEN>",
  "token_type": "bearer",
  "expires_at": "2022-06-03T18:29:45.000Z",
  "expires_in": 21600
}
```

With the `<SIGNED_ENTITLEMENT_KEY>` and `<REGISTER_ACCESS_TOKEN>` in hand, you're
ready to create a tenant programmatically.

## 4 Create a tenant

Create a tenant by issuing a request to the tenant registration endpoint
(`https://<TENANT_REGISTRATION>/api/v1/tenants`). Include the `<REGISTER_ACCESS_TOKEN>`
in the `Authorization` header and the `<SIGNED_ENTITLEMENT_KEY>`
as a JSON object in the request body.

Using cURL, send the request:

```bash
curl -L -X POST "https://<TENANT_REGISTRATION>/api/v1/tenants" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"licenseKey\":\"<SIGNED_ENTITLEMENT_KEY>\"}"
```

The result is a JSON object with the new tenant hostname:

```json
{
  "id": "TZXk9rFMoKgp7sgAwvczdAlKSSWuaa3e",
  "name": "ire7t7hg58avbmx",
  "hostnames": ["<TARGET_TENANT>"],
  "createdByUser": "",
  "datacenter": "us-east-1",
  "created": "2022-06-02T13:51:58.503Z",
  "lastUpdated": "2022-06-02T13:51:58.503Z",
  "status": "active",
  "autoAssignCreateSharedSpacesRoleToProfessionals": true,
  "enableAnalyticCreation": false,
  "links": {
    "self": {
      "href": "https://<TENANT_REGISTRATION>/api/v1/tenants/TZXk9rFMoKgp7sgAwvczdAlKSSWuaa3e"
    }
  }
}
```

Record the first value of the `hostnames` array (there should be only one value)
as the `<TARGET_TENANT>` value for later use.

## 5 Request an access token for the tenant

Now that the target tenant has been created, you need to obtain an access token
from the tenant to make REST requests using the client ID, client secret, and
OAuth credential grant type in a JSON object.

```json
{
  "client_id": "<CLIENT_ID>",
  "client_secret": "<CLIENT_SECRET>",
  "grant_type": "client_credentials"
}
```

Send a request to the OAuth token endpoint on the new tenant:

```bash
curl -L -X POST "https://<TARGET_TENANT>/oauth/token" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"client_id\":\"<CLIENT_ID>\", \"client_secret\":\"<CLIENT_SECRET>\", \"grant_type\":\"client_credentials\"}"
```

The result is a JSON object containing the `<TARGET_ACCESS_TOKEN>`.

```json
{
  "access_token": "<TARGET_ACCESS_TOKEN>",
  "token_type": "bearer",
  "expires_at": "2022-06-03T20:52:08.000Z",
  "expires_in": 21600
}
```

## 6 Send an API request to the tenant

The tenant access token authorizes the API requests you make to the tenant you
created. Test the connectivity and access to the new tenant by making a request
to the users endpoint.

Using cURL, send the request to the
`https://<TARGET_TENANT>/api/v1/users/me` endpoint with the tenant
access token in the `Authorization` header:

```bash
curl -L "https://<TARGET_TENANT>/api/v1/users/me" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json"
```

The result is a JSON object displaying the metadata for the built-in `bot` user.

```json
{
  "id": "629a20185b4a5194788d9c1e",
  "tenantId": "7WZ_qyWDvlS8AvNkye9y20dn-miC0URf",
  "clientId": "<CLIENT_ID>",
  "status": "active",
  "subject": "qlikbot\\00cbb22c600e823ed278d5e3d976f85b",
  "name": "US OAuth Client",
  "roles": ["TenantAdmin"],
  "assignedRoles": [...],
  "assignedGroups": [],
  "groups": [],
  "createdAt": "2022-06-03T14:52:08.925Z",
  "lastUpdatedAt": "2022-06-03T14:52:08.925Z",
  "created": "2022-06-03T14:52:08.925Z",
  "lastUpdated": "2022-06-03T14:52:08.925Z",
  "links": {...}
}
```

## Next steps

If you want to validate that the tenant you created is operational, you can
[add an interactive user to the tenant](https://qlik.dev/manage/platform-operations/add-an-interactive-user-to-a-tenant)
and log in through your browser.
Otherwise, you are ready to [configure the tenant](https://qlik.dev/manage/platform-operations/configure-a-tenant) for use.
