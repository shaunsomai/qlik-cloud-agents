# Tenants

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Tenants are the highest level of logical container, with this API supporting configuration of several key tenant settings.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/tenants`](#post-apiv1tenants) | Creates a tenant in the requested region, linked to the provided license key. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants` if interacting with tenants in the `us` region. |
| `GET` | [`/api/v1/tenants/{tenantId}`](#get-apiv1tenantstenantid) | Retrieves a specific tenant by ID. |
| `PATCH` | [`/api/v1/tenants/{tenantId}`](#patch-apiv1tenantstenantid) | Updates properties of a specific tenant by ID. |
| `POST` | [`/api/v1/tenants/{tenantId}/actions/deactivate`](#post-apiv1tenantstenantidactionsdeactivate) | Deactivates a specific tenant. Once deactivated, tenant will be deleted on or after `estimatedPurgeDate`. Tenant can be reactivated using `/v1/tenants/{tenantId}/actions/reactivate` until this date. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants/{tenantId}/actions/deactivate` if interacting with tenants in the `us` region. |
| `POST` | [`/api/v1/tenants/{tenantId}/actions/reactivate`](#post-apiv1tenantstenantidactionsreactivate) | Reactivates a deactivated tenant. Tenants can be reactivated until the `estimatedPurgeDate` provided at time of deactivation. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants/{tenantId}/actions/reactivate` if interacting with tenants in the `us` region. |
| `GET` | [`/api/v1/tenants/me`](#get-apiv1tenantsme) | Redirects to current tenant. |

## API Reference

### POST /api/v1/tenants

Creates a tenant in the requested region, linked to the provided license key. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants` if interacting with tenants in the `us` region.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datacenter` | string | No | The datacenter where the tenant is located.  Supported locations for commercial licenses: - `ap-northeast-1`: Japan (jp) - `ap-southeast-1`: Australia (ap) - `ap-southeast-2`: Singapore (sg) - `eu-central-1`: Germany (de) - `eu-west-1`: Ireland (eu) - `eu-west-2`: United Kingdom (uk) - `us-east-1`: United States of America (us) |
| `licenseKey` | string | No | The signed license key of the license that will be associated with the created tenant. |

#### Responses

##### 201

Tenant created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique tenant identifier. |
| `name` | string | Yes | The display name of the tenant. |
| `links` | object | No |  |
| `region` | string | No | The region where the tenant is located. |
| `status` | string | No | The status of the tenant. Enum: "active", "disabled", "deleted", "user-access-disabled" |
| `created` | string | No | The timestamp for when the tenant record was created (1970-01-01T00:00:00.001Z for static tenants). |
| `hostnames` | string[] | No | List of case insensitive hostnames that are mapped to the tenant. The first record maps to the display name and the subsequent entries are aliases. |
| `datacenter` | string | No | The datacenter where the tenant is located. |
| `lastUpdated` | string | No | The timestamp for when the tenant record was last updated (1970-01-01T00:00:00.001Z for static tenants). |
| `createdByUser` | string | No | The user ID who created the tenant. |
| `statusLastUpdatedAt` | string | No | The timestamp for when the tenant status was last changed. |
| `enableAnalyticCreation` | boolean | No | _(deprecated)_ |
| `enableAppOpeningFeedback` | boolean | No |  |
| `autoAssignCreateSharedSpacesRoleToProfessionals` | boolean | No |  |
| `autoAssignDataServicesContributorRoleToProfessionals` | boolean | No |  |
| `autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals` | boolean | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this tenant. |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenants` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/tenants', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    datacenter: 'us-east-1',
    licenseKey: 1234567890,
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenants yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datacenter":"us-east-1","licenseKey":1234567890}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "QlikTenant",
  "links": {
    "self": {
      "href": "http://foo.example/api/v1/tenants/TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
    }
  },
  "region": "us",
  "status": "active",
  "created": "string",
  "hostnames": [
    "foo.example"
  ],
  "datacenter": "us-east-1",
  "lastUpdated": "string",
  "createdByUser": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy7A",
  "statusLastUpdatedAt": "2023-08-18T12:34:56.789Z",
  "enableAnalyticCreation": false,
  "enableAppOpeningFeedback": false,
  "autoAssignCreateSharedSpacesRoleToProfessionals": true,
  "autoAssignDataServicesContributorRoleToProfessionals": true,
  "autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals": true
}
```

---

### GET /api/v1/tenants/{tenantId}

Retrieves a specific tenant by ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The ID of the tenant to retrieve |

#### Responses

##### 200

Tenant found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique tenant identifier. |
| `name` | string | Yes | The display name of the tenant. |
| `links` | object | No |  |
| `region` | string | No | The region where the tenant is located. |
| `status` | string | No | The status of the tenant. Enum: "active", "disabled", "deleted", "user-access-disabled" |
| `created` | string | No | The timestamp for when the tenant record was created (1970-01-01T00:00:00.001Z for static tenants). |
| `hostnames` | string[] | No | List of case insensitive hostnames that are mapped to the tenant. The first record maps to the display name and the subsequent entries are aliases. |
| `datacenter` | string | No | The datacenter where the tenant is located. |
| `lastUpdated` | string | No | The timestamp for when the tenant record was last updated (1970-01-01T00:00:00.001Z for static tenants). |
| `createdByUser` | string | No | The user ID who created the tenant. |
| `statusLastUpdatedAt` | string | No | The timestamp for when the tenant status was last changed. |
| `enableAnalyticCreation` | boolean | No | _(deprecated)_ |
| `enableAppOpeningFeedback` | boolean | No |  |
| `autoAssignCreateSharedSpacesRoleToProfessionals` | boolean | No |  |
| `autoAssignDataServicesContributorRoleToProfessionals` | boolean | No |  |
| `autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals` | boolean | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this tenant. |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 404

Tenant not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tenants/{tenantId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenants/{tenantId}',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/tenants/{tenantId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants/{tenantId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "QlikTenant",
  "links": {
    "self": {
      "href": "http://foo.example/api/v1/tenants/TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
    }
  },
  "region": "us",
  "status": "active",
  "created": "string",
  "hostnames": [
    "foo.example"
  ],
  "datacenter": "us-east-1",
  "lastUpdated": "string",
  "createdByUser": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy7A",
  "statusLastUpdatedAt": "2023-08-18T12:34:56.789Z",
  "enableAnalyticCreation": false,
  "enableAppOpeningFeedback": false,
  "autoAssignCreateSharedSpacesRoleToProfessionals": true,
  "autoAssignDataServicesContributorRoleToProfessionals": true,
  "autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals": true
}
```

---

### PATCH /api/v1/tenants/{tenantId}

Updates properties of a specific tenant by ID.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The ID of the tenant to update |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | A JSON Pointer value that references a location within the target document where the operation is performed. Enum: "/name", "/hostnames/1", "/autoAssignCreateSharedSpacesRoleToProfessionals", "/autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals", "/autoAssignDataServicesContributorRoleToProfessionals", "/enableAnalyticCreation", "/enableAppOpeningFeedback" |
| `value` | string \| boolean | Yes | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

</details>

#### Responses

##### 204

Tenant updated successfully

##### 400

Invalid PATCH request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object \| array | No |  |
| `title` | string | Yes | Summary of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `meta`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `TenantSingleMetaErrorDetail` | object | No |  |

<details>
<summary>Properties of `TenantSingleMetaErrorDetail`</summary>

_Properties truncated due to depth limit._

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `TenantMultipleMetaErrorsDetail` | object[] | No |  |

<details>
<summary>Properties of `TenantMultipleMetaErrorsDetail`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Tenant not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/tenants/{tenantId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenants/{tenantId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'Corp',
      },
      {
        op: 'replace',
        path: '/hostnames/1',
        value: 'example-tenant.us.qlikcloud.com',
      },
      {
        op: 'replace',
        path: '/autoAssignCreateSharedSpacesRoleToProfessionals',
        value: true,
      },
      {
        op: 'replace',
        path: '/autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals',
        value: false,
      },
      {
        op: 'replace',
        path: '/autoAssignDataServicesContributorRoleToProfessionals',
        value: true,
      },
      {
        op: 'replace',
        path: '/enableAnalyticCreation',
        value: false,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/tenants/{tenantId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants/{tenantId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"Corp"},{"op":"replace","path":"/hostnames/1","value":"example-tenant.us.qlikcloud.com"},{"op":"replace","path":"/autoAssignCreateSharedSpacesRoleToProfessionals","value":true},{"op":"replace","path":"/autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals","value":false},{"op":"replace","path":"/autoAssignDataServicesContributorRoleToProfessionals","value":true},{"op":"replace","path":"/enableAnalyticCreation","value":false}]'
```

---

### POST /api/v1/tenants/{tenantId}/actions/deactivate

Deactivates a specific tenant. Once deactivated, tenant will be deleted on or after `estimatedPurgeDate`. Tenant can be reactivated using `/v1/tenants/{tenantId}/actions/reactivate` until this date. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants/{tenantId}/actions/deactivate` if interacting with tenants in the `us` region.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The id of the tenant to deactivate |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-confirm-hostname` | string | Yes | A confirmation string that should match the hostname associated with the tenant resource to be deactivated. Example: unicorn.eu.qlikcloud.com |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `purgeAfterDays` | integer | No | Sets the number of days to purge the tenant after deactivation. Only available to OEMs. |

#### Responses

##### 200

Tenant deactivated successfully

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique tenant identifier. |
| `status` | string | No | The status of the tenant. Enum: "disabled" |
| `estimatedPurgeDate` | string | No | The estimated date time of when tenant will be purged. |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Tenant Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 412

Precondition Failed (invalid qlik-confirm-hostname value)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenants/{tenantId}/actions/deactivate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenants/{tenantId}/actions/deactivate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ purgeAfterDays: 30 }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenants/{tenantId}/actions/deactivate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants/{tenantId}/actions/deactivate" \
-X POST \
-H "qlik-confirm-hostname: unicorn.eu.qlikcloud.com" \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"purgeAfterDays":30}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "status": "disabled",
  "estimatedPurgeDate": "2023-08-18T00:00:00.000Z"
}
```

---

### POST /api/v1/tenants/{tenantId}/actions/reactivate

Reactivates a deactivated tenant. Tenants can be reactivated until the `estimatedPurgeDate` provided at time of deactivation. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants/{tenantId}/actions/reactivate` if interacting with tenants in the `us` region.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The id of the tenant to reactivate |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-confirm-hostname` | string | Yes | A confirmation string that should match one of the hostnames of the tenant resource to be reactivated. Example: unicorn.eu.qlikcloud.com |

#### Request Body

**Content-Type:** `application/json`


#### Responses

##### 200

Tenant reactivated successfully

**Content-Type:** `application/json`


##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 412

Precondition Failed (invalid qlik-confirm-hostname value)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the error. |
| `source` | object | No | References to the source of the error. |
| `status` | string | Yes | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenants/{tenantId}/actions/reactivate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenants/{tenantId}/actions/reactivate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({}),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenants/{tenantId}/actions/reactivate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants/{tenantId}/actions/reactivate" \
-X POST \
-H "qlik-confirm-hostname: unicorn.us.qlikcloud.com" \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{}'
```

**Example Response:**

```json
{}
```

---

### GET /api/v1/tenants/me

Redirects to current tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 302

Successful redirect.

**Content-Type:** `text/html`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/html` | string | No |  |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tenants/me` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenants/me',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/tenants/me yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenants/me" \
-H "Authorization: Bearer <access_token>"
```

---
