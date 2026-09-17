# IP Policies

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

IP policies let you control which IP addresses can access your Qlik Cloud tenant. Use this API to manage allowlisting rules by creating, listing, updating, and deleting IP policies. When allowlisting is enabled, only users connecting from allowed IPv4 addresses or ranges can access the tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/core/ip-policies`](#get-apicoreip-policies) | Returns a list of IP policies present in the tenant. The user must be assigned the `TenantAdmin` role. |
| `POST` | [`/api/core/ip-policies`](#post-apicoreip-policies) | Creates a new IPv4 IP policy in the tenant. If this is the first enabled policy, IP allowlisting will be enabled and access via other IP addresses will be blocked. The user's IP address must be present in at least one policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role. IPv6 IP addresses are not currently supported. |
| `GET` | [`/api/core/ip-policies/{id}`](#get-apicoreip-policiesid) | Retrieves details for a specific IP policy by policy ID. |
| `PATCH` | [`/api/core/ip-policies/{id}`](#patch-apicoreip-policiesid) | Updates the IP policy. If this is the first enabled policy in the tenant, IP allowlisting will be enabled and access via other IP addresses will be blocked. The user's IP address must be present in at least one policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role. |
| `DELETE` | [`/api/core/ip-policies/{id}`](#delete-apicoreip-policiesid) | Deletes an IP policy by ID. If this is the last enabled policy in the tenant, IP allowlisting will be disabled and access will be permitted via all IP addresses. The user's IP address must be present in at least one other policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/core/ip-policies

Returns a list of IP policies present in the tenant. The user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | string | No | A comma-separated list of fields to limit in the response. |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. All conditional statements within this query parameter are case insensitive.  field "enabled" supports following operators: eq  field "id" supports following operators: eq, ne  field "name" supports following operators: eq, co  field "tenantId" supports following operators: eq |
| `limit` | number | No | The number of IP policies to retrieve. |
| `page` | string | No | The page cursor. Takes precedence over other parameters. |
| `sort` | string | No | Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending. Enum: "enabled", "+enabled", "-enabled", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt", "name", "+name", "-name" |
| `totalResults` | boolean | No | Determines whether to return a count of the total records matched in the query. Defaults to false. |

#### Responses

##### 200

IP policies retrieved successfully. The response includes an array of IP policies and pagination links.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An array of IP policies. |
| `links` | object | Yes | Contains pagination links. self is a link to the current results page, next is a link to the next results page and prev is a link to the previous results page |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the IP policy. |
| `name` | string | No | The descriptive name for the IP policy. |
| `enabled` | boolean | No | Indicates whether the IP policy is enabled. |
| `editable` | boolean | No | Indicates whether the IP policy can be updated. |
| `tenantId` | string | No | The tenant unique identifier associated with the given IP policy. |
| `createdAt` | string | No | The timestamp for when the resource was created. |
| `createdBy` | string | No | The user ID of the user who created the IP policy. |
| `deletable` | boolean | No | Indicates whether the IP policy can be deleted. |
| `updatedAt` | string | No | The timestamp for when the resource was last updated. |
| `updatedBy` | string | No | The user ID of the user who last updated the IP policy. |
| `allowedIps` | string[] | No | An array of allowed IP addresses. |
| `toggleable` | boolean | No | Indicates whether the IP policy can be enabled/disabled. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | A link |
| `prev` | object | No | A link |
| `self` | object | Yes | A link |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Invalid request parameters for querying IP policies.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized, JWT is invalid or not provided.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
// qlik-api has not implemented support for `GET /api/core/ip-policies` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/ip-policies',
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
# qlik-cli has not implemented support for GET /api/core/ip-policies yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "Allow access from office IP addresses.",
      "enabled": true,
      "editable": true,
      "tenantId": "644fd58b846d649c82eba436",
      "createdAt": "2021-03-21T17:32:28Z",
      "createdBy": "507f191e810c19729de860ea",
      "deletable": true,
      "updatedAt": "2021-03-22T10:01:02Z",
      "updatedBy": "507f191e810c19729de860ea",
      "allowedIps": [
        "61.254.213.0/24",
        "22.46.216.142"
      ],
      "toggleable": true
    }
  ],
  "links": {
    "next": {
      "href": "http://mytenant.us.qlikcloud.com/api/core/ip-policies?page=QaFdFYW6pImZvRgFaDyB1UffNgfs4mRd"
    },
    "prev": {
      "href": "http://mytenant.us.qlikcloud.com/api/core/ip-policies?page=QaFdFYW6pImZvRgFaDyB1UffNgfs4mRd"
    },
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/core/ip-policies?page=QaFdFYW6pImZvRgFaDyB1UffNgfs4mRd"
    }
  },
  "totalResults": 42
}
```

---

### POST /api/core/ip-policies

Creates a new IPv4 IP policy in the tenant. If this is the first enabled policy, IP allowlisting will be enabled and access via other IP addresses will be blocked. The user's IP address must be present in at least one policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role. IPv6 IP addresses are not currently supported.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The descriptive name for the IP policy. |
| `enabled` | boolean | No | Indicates whether the IP policy is enabled. |
| `allowedIps` | string[] | Yes | An array of allowed IP IPv4 addresses, either as plain IP addresses, or as CIDR ranges. |

#### Responses

##### 201

Request successfully completed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the IP policy. |
| `name` | string | Yes | The descriptive name for the IP policy. |
| `enabled` | boolean | Yes | Indicates whether the IP policy is enabled. |
| `editable` | boolean | Yes | Indicates whether the IP policy can be updated. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the given IP policy. |
| `createdAt` | string | Yes | The timestamp for when the IP policy was created. |
| `createdBy` | string | Yes | The user ID of the user who created the IP policy. |
| `deletable` | boolean | Yes | Indicates whether the IP policy can be deleted. |
| `updatedAt` | string | Yes | The timestamp for when the IP policy was last updated. |
| `updatedBy` | string | Yes | The user ID of the user who last updated the IP policy. |
| `allowedIps` | string[] | Yes | An array of allowed public IPv4 addresses. |
| `toggleable` | boolean | Yes | Indicates whether the IP policy can be enabled/disabled.. |

##### 400

Invalid request body.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

IP Policy ID not found or Invalid format.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
// qlik-api has not implemented support for `POST /api/core/ip-policies` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/ip-policies',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Allow access from office IP addresses.',
      enabled: false,
      allowedIps: [
        '61.254.213.0/24',
        '22.46.216.142',
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/core/ip-policies yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Allow access from office IP addresses.","enabled":false,"allowedIps":["61.254.213.0/24","22.46.216.142"]}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Allow access from office IP addresses.",
  "enabled": true,
  "editable": true,
  "tenantId": "644fd58b846d649c82eba436",
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "507f191e810c19729de860ea",
  "deletable": true,
  "updatedAt": "2021-03-22T10:01:02Z",
  "updatedBy": "507f191e810c19729de860ea",
  "allowedIps": [
    "61.254.213.0/24",
    "22.46.216.142"
  ],
  "toggleable": true
}
```

---

### GET /api/core/ip-policies/{id}

Retrieves details for a specific IP policy by policy ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The IP policy unique identifier |

#### Responses

##### 200

Request successfully completed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the IP policy. |
| `name` | string | Yes | The descriptive name for the IP policy. |
| `enabled` | boolean | Yes | Indicates whether the IP policy is enabled. |
| `editable` | boolean | Yes | Indicates whether the IP policy can be updated. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the given IP policy. |
| `createdAt` | string | Yes | The timestamp for when the IP policy was created. |
| `createdBy` | string | Yes | The user ID of the user who created the IP policy. |
| `deletable` | boolean | Yes | Indicates whether the IP policy can be deleted. |
| `updatedAt` | string | Yes | The timestamp for when the IP policy was last updated. |
| `updatedBy` | string | Yes | The user ID of the user who last updated the IP policy. |
| `allowedIps` | string[] | Yes | An array of allowed public IPv4 addresses. |
| `toggleable` | boolean | Yes | Indicates whether the IP policy can be enabled/disabled.. |

##### 401

Unauthorized, JWT is invalid or not provided.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

IP Policy ID not found or Invalid format.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
// qlik-api has not implemented support for `GET /api/core/ip-policies/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/ip-policies/{id}',
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
# qlik-cli has not implemented support for GET /api/core/ip-policies/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Allow access from office IP addresses.",
  "enabled": true,
  "editable": true,
  "tenantId": "644fd58b846d649c82eba436",
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "507f191e810c19729de860ea",
  "deletable": true,
  "updatedAt": "2021-03-22T10:01:02Z",
  "updatedBy": "507f191e810c19729de860ea",
  "allowedIps": [
    "61.254.213.0/24",
    "22.46.216.142"
  ],
  "toggleable": true
}
```

---

### PATCH /api/core/ip-policies/{id}

Updates the IP policy. If this is the first enabled policy in the tenant, IP allowlisting will be enabled and access via other IP addresses will be blocked. The user's IP address must be present in at least one policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the IP policy. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | A JSON Pointer. Enum: "/enabled", "/name", "/allowedIps" |
| `value` | string \| boolean \| array | Yes | The value to be used for this operation. |

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

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string[] | No |  |

</details>

#### Responses

##### 204

IP policy updated successfully.

##### 400

Invalid request body.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized, JWT is invalid or not provided.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Access Denied.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

IP policy ID not found or Invalid format.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
// qlik-api has not implemented support for `PATCH /api/core/ip-policies/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/ip-policies/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New name',
      },
      {
        op: 'replace',
        path: '/allowedIps',
        value: [
          '61.254.213.0/24',
          '22.46.216.142',
        ],
      },
      {
        op: 'replace',
        path: '/enabled',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/core/ip-policies/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New name"},{"op":"replace","path":"/allowedIps","value":["61.254.213.0/24","22.46.216.142"]},{"op":"replace","path":"/enabled","value":true}]'
```

---

### DELETE /api/core/ip-policies/{id}

Deletes an IP policy by ID. If this is the last enabled policy in the tenant, IP allowlisting will be disabled and access will be permitted via all IP addresses. The user's IP address must be present in at least one other policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the IP policy. |

#### Responses

##### 204

IP policy deleted successfully.

##### 401

Unauthorized, JWT is invalid or not provided.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Access Denied.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

IP policy ID not found or Invalid format.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

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
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

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
// qlik-api has not implemented support for `DELETE /api/core/ip-policies/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/ip-policies/{id}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/core/ip-policies/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
