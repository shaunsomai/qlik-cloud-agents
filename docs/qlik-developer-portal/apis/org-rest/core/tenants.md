# Tenants

**Base URL:** `https://console.qlikcloud.com`

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/core/tenants`](#get-apicoretenants) | Use this operation to retrieve a list of tenants across multiple organizations. Filter results using SCIM filter expressions and sort by supported fields. Returns paginated results with optional total count. |
| `GET` | [`/api/core/tenants/{tenantId}`](#get-apicoretenantstenantid) | Use this operation to retrieve a specific Qlik Cloud tenant by its identifier. |
| `GET` | [`/api/core/tenants/actions/count`](#get-apicoretenantsactionscount) | Use this operation to count Qlik Cloud tenants matching a SCIM filter expression. Primarily used for subscription-based queries. The `subscriptionId` attribute is required in the filter expression. |
| `POST` | [`/api/core/tenants/actions/filter`](#post-apicoretenantsactionsfilter) | Use this operation to search and filter Qlik Cloud tenants using a SCIM filter expression provided in the request body. Supports complex queries with logical and comparison operators. |

## API Reference

### GET /api/core/tenants

Use this operation to retrieve a list of tenants across multiple organizations. Filter results using SCIM filter expressions and sort by supported fields. Returns paginated results with optional total count.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | SCIM filter expression.  Supported attributes are `subscriptionId` (required), `regionCode`, `countryCode`, `name`, `hostnames`, `createdAt`, `updatedAt`, `id`, `status`, and `originalId`.  Supports logical operators (`and`, `or`, `not`) and comparison operators (`eq`, `ne`, `gt`, `ge`, `lt`, `le`, `co`).  Operator support varies by attribute. For example: - `regionCode`, `status`: support `eq`, `ne` - `subscriptionId`, `name`, `hostnames`, `id`, `originalId`: support `eq` only |
| `limit` | integer | No | Maximum number of results to return (0-100, default 20). |
| `next` | string | No | Cursor for the next page of results (tenant ObjectId). |
| `prev` | string | No | Cursor for the previous page of results (tenant ObjectId). |
| `sort` | string | No | Comma-separated list of fields to sort by. Prefix with `-` for descending order, `+` or no prefix for ascending. Supported fields are `name`, `regionCode`, `countryCode`, `hostnames`, `createdAt`, `updatedAt`, `status`, `subscriptionId`. |
| `totalResults` | string | No | When set to `true`, includes the total count of matching tenants in the response. Default is `false`. Enum: "true", "false" |

#### Responses

##### 200

Tenants retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | A tenant resource representing a Qlik Cloud tenant. |
| `links` | object | No |  |
| `totalResults` | integer | No | Total number of tenants matching the query. Only included when the `totalResults` query parameter is set to `true`. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the tenant (`originalId`). |
| `name` | string | No | The display name of the tenant. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the tenant. Enum: "active", "disabled", "deleted", "deactivated" |
| `createdAt` | string | Yes | The timestamp for when the tenant was created. |
| `createdBy` | string | No | The identifier of the user who created the tenant. |
| `hostnames` | string[] | Yes | List of case-insensitive hostnames mapped to the tenant. |
| `updatedAt` | string | Yes | The timestamp for when the tenant was last updated. |
| `regionCode` | string | Yes | The region code where the tenant is located. Enum: "us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-central-1", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-south-1", "il-central-1", "me-central-1", "sa-east-1", "ca-central-1" |
| `countryCode` | string | Yes | The country code for the tenant. Enum: "US", "IE", "GB", "DE", "SG", "AU", "JP", "IN", "IL", "AE", "BR", "FR", "SE", "CA" |
| `licenseEndsAt` | string | No | The date when the license ends. |
| `licenseNumber` | string | No | The license number associated with the tenant. |
| `subscriptionId` | string | No | The parent subscription ID (license number) for the tenant. |
| `licenseStartsAt` | string | No | The date when the license starts. |
| `deletionStartsAt` | string | No | The scheduled date for tenant deletion. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | A link to this tenant. |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the next page of results. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the previous page of results. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the current request. |

</details>

</details>

##### 400

Bad request. The request contains invalid query parameters or an invalid SCIM filter expression.

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

Forbidden. The user does not have permission to access tenants, or the feature is not enabled.

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

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/tenants" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/tenants',
  method: 'GET',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "QlikTenant",
      "links": {
        "self": {
          "href": "http://foo.example/api/v1/tenants/TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
        }
      },
      "status": "active",
      "createdAt": "2023-01-15T10:30:00.000Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy7A",
      "hostnames": [
        "example-tenant.us.qlikcloud.com",
        "example-tenant.example.com"
      ],
      "updatedAt": "2023-06-20T14:45:00.000Z",
      "regionCode": "us-east-1",
      "countryCode": "US",
      "licenseEndsAt": "2024-12-31",
      "licenseNumber": "1234567890123456",
      "subscriptionId": "9876543210987654",
      "licenseStartsAt": "2023-01-01",
      "deletionStartsAt": "2024-06-30T00:00:00.000Z"
    }
  ],
  "links": {
    "next": {
      "href": "https://api.qlikcloud.com/core/tenants?limit=20&next=507f191e810c19729de860ea"
    },
    "prev": {
      "href": "https://api.qlikcloud.com/core/tenants?limit=20&prev=507f1f77bcf86cd799439011"
    },
    "self": {
      "href": "https://api.qlikcloud.com/core/tenants"
    }
  },
  "totalResults": 150
}
```

---

### GET /api/core/tenants/{tenantId}

Use this operation to retrieve a specific Qlik Cloud tenant by its identifier.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The identifier of the tenant to retrieve. |

#### Responses

##### 200

Tenant retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | A tenant resource representing a Qlik Cloud tenant. |
| `links` | object | No |  |
| `totalResults` | integer | No | Total number of tenants matching the query. Only included when the `totalResults` query parameter is set to `true`. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the tenant (`originalId`). |
| `name` | string | No | The display name of the tenant. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the tenant. Enum: "active", "disabled", "deleted", "deactivated" |
| `createdAt` | string | Yes | The timestamp for when the tenant was created. |
| `createdBy` | string | No | The identifier of the user who created the tenant. |
| `hostnames` | string[] | Yes | List of case-insensitive hostnames mapped to the tenant. |
| `updatedAt` | string | Yes | The timestamp for when the tenant was last updated. |
| `regionCode` | string | Yes | The region code where the tenant is located. Enum: "us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-central-1", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-south-1", "il-central-1", "me-central-1", "sa-east-1", "ca-central-1" |
| `countryCode` | string | Yes | The country code for the tenant. Enum: "US", "IE", "GB", "DE", "SG", "AU", "JP", "IN", "IL", "AE", "BR", "FR", "SE", "CA" |
| `licenseEndsAt` | string | No | The date when the license ends. |
| `licenseNumber` | string | No | The license number associated with the tenant. |
| `subscriptionId` | string | No | The parent subscription ID (license number) for the tenant. |
| `licenseStartsAt` | string | No | The date when the license starts. |
| `deletionStartsAt` | string | No | The scheduled date for tenant deletion. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | A link to this tenant. |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the next page of results. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the previous page of results. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the current request. |

</details>

</details>

##### 400

Bad request. The request contains an invalid tenant identifier.

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

Forbidden. The user does not have permission to access this tenant, or the feature is not enabled.

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

The requested tenant was not found.

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

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/tenants/{tenantId}" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/tenants/{tenantId}',
  method: 'GET',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "QlikTenant",
      "links": {
        "self": {
          "href": "http://foo.example/api/v1/tenants/TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
        }
      },
      "status": "active",
      "createdAt": "2023-01-15T10:30:00.000Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy7A",
      "hostnames": [
        "example-tenant.us.qlikcloud.com",
        "example-tenant.example.com"
      ],
      "updatedAt": "2023-06-20T14:45:00.000Z",
      "regionCode": "us-east-1",
      "countryCode": "US",
      "licenseEndsAt": "2024-12-31",
      "licenseNumber": "1234567890123456",
      "subscriptionId": "9876543210987654",
      "licenseStartsAt": "2023-01-01",
      "deletionStartsAt": "2024-06-30T00:00:00.000Z"
    }
  ],
  "links": {
    "next": {
      "href": "https://api.qlikcloud.com/core/tenants?limit=20&next=507f191e810c19729de860ea"
    },
    "prev": {
      "href": "https://api.qlikcloud.com/core/tenants?limit=20&prev=507f1f77bcf86cd799439011"
    },
    "self": {
      "href": "https://api.qlikcloud.com/core/tenants"
    }
  },
  "totalResults": 150
}
```

---

### GET /api/core/tenants/actions/count

Use this operation to count Qlik Cloud tenants matching a SCIM filter expression. Primarily used for subscription-based queries. The `subscriptionId` attribute is required in the filter expression.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | Yes | SCIM filter query string. Must include the `subscriptionId` attribute. |

#### Responses

##### 200

Tenant count retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | Yes | The total number of tenants matching the filter criteria. |

##### 400

Bad request. The request contains an invalid filter expression or is missing the required `subscriptionId` attribute.

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

Forbidden. The user does not have permission to count tenants.

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

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/tenants/actions/count" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/tenants/actions/count',
  method: 'GET',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "total": 42
}
```

---

### POST /api/core/tenants/actions/filter

Use this operation to search and filter Qlik Cloud tenants using a SCIM filter expression provided in the request body. Supports complex queries with logical and comparison operators.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Maximum number of results to return (0-100, default 20). |
| `next` | string | No | Cursor for the next page of results (tenant ObjectId). |
| `prev` | string | No | Cursor for the previous page of results (tenant ObjectId). |
| `sort` | string | No | Comma-separated list of fields to sort by. Prefix with `-` for descending order, `+` or no prefix for ascending. Supported fields are `name`, `regionCode`, `countryCode`, `hostnames`, `createdAt`, `updatedAt`, `status`, `subscriptionId`. |
| `totalResults` | string | No | When set to `true`, includes the total count of matching tenants in the response. Default is `false`. Enum: "true", "false" |

#### Request Body

**Required**

Request body containing the SCIM filter expression used to select tenants.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | SCIM filter expression.  Supported attributes are `subscriptionId` (required), `regionCode`, `countryCode`, `name`, `hostnames`, `createdAt`, `updatedAt`, `id`, `status`, and `originalId`.  Supports logical operators (`and`, `or`, `not`) and comparison operators (`eq`, `ne`, `gt`, `ge`, `lt`, `le`, `co`).  Operator support varies by attribute. For example: - `regionCode`, `status`: support `eq`, `ne` - `subscriptionId`, `name`, `hostnames`, `id`, `originalId`: support `eq` only |

#### Responses

##### 200

Tenants filtered successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | A tenant resource representing a Qlik Cloud tenant. |
| `links` | object | No |  |
| `totalResults` | integer | No | Total number of tenants matching the filter. Only included when the `totalResults` query parameter is set to `true`. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the tenant (`originalId`). |
| `name` | string | No | The display name of the tenant. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the tenant. Enum: "active", "disabled", "deleted", "deactivated" |
| `createdAt` | string | Yes | The timestamp for when the tenant was created. |
| `createdBy` | string | No | The identifier of the user who created the tenant. |
| `hostnames` | string[] | Yes | List of case-insensitive hostnames mapped to the tenant. |
| `updatedAt` | string | Yes | The timestamp for when the tenant was last updated. |
| `regionCode` | string | Yes | The region code where the tenant is located. Enum: "us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-central-1", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-south-1", "il-central-1", "me-central-1", "sa-east-1", "ca-central-1" |
| `countryCode` | string | Yes | The country code for the tenant. Enum: "US", "IE", "GB", "DE", "SG", "AU", "JP", "IN", "IL", "AE", "BR", "FR", "SE", "CA" |
| `licenseEndsAt` | string | No | The date when the license ends. |
| `licenseNumber` | string | No | The license number associated with the tenant. |
| `subscriptionId` | string | No | The parent subscription ID (license number) for the tenant. |
| `licenseStartsAt` | string | No | The date when the license starts. |
| `deletionStartsAt` | string | No | The scheduled date for tenant deletion. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | A link to this tenant. |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the next page of results. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the previous page of results. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the current request. |

</details>

</details>

##### 400

Bad request. The request contains an invalid SCIM filter or invalid query parameters.

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

Forbidden. The user does not have permission to filter tenants, or the feature is not enabled.

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

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/tenants/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"filter":"subscriptionId eq \"9876543210987654\" and status eq \"active\""}'
```

**Node.js:**

```javascript
const https = require('https')

const data = JSON.stringify({
  filter:
    'subscriptionId eq "9876543210987654" and status eq "active"',
})
const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/tenants/actions/filter',
  method: 'POST',
  headers: {
    'Content-type': 'application/json',
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)
req.write(data)

```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "QlikTenant",
      "links": {
        "self": {
          "href": "http://foo.example/api/v1/tenants/TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
        }
      },
      "status": "active",
      "createdAt": "2023-01-15T10:30:00.000Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy7A",
      "hostnames": [
        "example-tenant.us.qlikcloud.com",
        "example-tenant.example.com"
      ],
      "updatedAt": "2023-06-20T14:45:00.000Z",
      "regionCode": "us-east-1",
      "countryCode": "US",
      "licenseEndsAt": "2024-12-31",
      "licenseNumber": "1234567890123456",
      "subscriptionId": "9876543210987654",
      "licenseStartsAt": "2023-01-01",
      "deletionStartsAt": "2024-06-30T00:00:00.000Z"
    }
  ],
  "links": {
    "next": {
      "href": "https://api.qlikcloud.com/core/tenants/actions/filter?limit=20&next=507f191e810c19729de860ea"
    },
    "prev": {
      "href": "https://api.qlikcloud.com/core/tenants/actions/filter?limit=20&prev=507f1f77bcf86cd799439011"
    },
    "self": {
      "href": "https://api.qlikcloud.com/core/tenants/actions/filter"
    }
  },
  "totalResults": 42
}
```

---
