# Web integrations

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

A web integration is a resource representing a list of whitelisted origins that can make requests to a specified tenant. It is the implementation of the CORS mechanism within Qlik Cloud.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/web-integrations`](#get-apiv1web-integrations) | Retrieves web integrations matching the query. |
| `POST` | [`/api/v1/web-integrations`](#post-apiv1web-integrations) | Creates a web integration. |
| `GET` | [`/api/v1/web-integrations/{id}`](#get-apiv1web-integrationsid) | Retrieves a single web integration by ID. |
| `PATCH` | [`/api/v1/web-integrations/{id}`](#patch-apiv1web-integrationsid) | Updates a single web integration by ID. |
| `DELETE` | [`/api/v1/web-integrations/{id}`](#delete-apiv1web-integrationsid) | Deletes a single web integration by ID. |

## API Reference

### GET /api/v1/web-integrations

Retrieves web integrations matching the query.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endingBefore` | string | No | The target web integration ID to start looking before for web integrations. Cannot be used in conjunction with startingAfter. |
| `limit` | number | No | The number of web integration entries to retrieve. |
| `sort` | string | No | The field to sort by. Prefix with +/- to indicate ascending/descending order. Enum: "name", "+name", "-name" |
| `startingAfter` | string | No | The target web integration ID to start looking after for web integrations. Cannot be used in conjunction with endingBefore. |
| `tenantId` | string | No | The tenant ID to filter by. |

#### Responses

##### 200

An array of web integration objects.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Properties of web integrations in a given tenant. |
| `links` | object | No | Pagination links |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique web integration identifier. |
| `name` | string | No | The name of the web integration. |
| `created` | string | No | The time the web integration was created. |
| `tenantId` | string | No | The tenant that the web integration belongs to. |
| `createdBy` | string | No | The user that created the web integration. |
| `lastUpdated` | string | No | The time the web integration was last updated. |
| `validOrigins` | string[] | No | The origins that are allowed to make requests to the tenant. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | Link information for next page. |
| `prev` | object | No | Link information for previous page. |
| `self` | object | Yes | Link information for current page. |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the next page of records. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the previous page of records. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the current page of records. |

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
// qlik-api has not implemented support for `GET /api/v1/web-integrations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-integrations',
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
# qlik-cli has not implemented support for GET /api/v1/web-integrations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "string",
      "created": "2018-10-30T07:06:22Z",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "lastUpdated": "2018-10-30T07:06:22Z",
      "validOrigins": [
        "string"
      ]
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/web-integrations

Creates a web integration.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Properties that the user wants to set for the web integration.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the web integration to create. |
| `validOrigins` | string[] | No | The origins that are allowed to make requests to the tenant. |

#### Responses

##### 201

Web integration created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique web integration identifier. |
| `name` | string | No | The name of the newly created web integration. |
| `links` | object | No | Pagination links |
| `created` | string | No | The time the web integration was created. |
| `tenantId` | string | No | The tenant that the web integration belongs to. |
| `createdBy` | string | No | The user that created the web integration. |
| `lastUpdated` | string | No | The time the web integration was last updated. |
| `validOrigins` | string[] | No | The origins that are allowed to make requests to the tenant. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | Link information for current page. |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the current page of records. |

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

Requestor not allowed to create a web integration.

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
// qlik-api has not implemented support for `POST /api/v1/web-integrations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-integrations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'My Web Integration',
      validOrigins: ['https://thirdPartyApp.com'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/web-integrations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"My Web Integration","validOrigins":["https://thirdPartyApp.com"]}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "My Web Integration",
  "links": {
    "self": {
      "href": "http://mytenant.region.domain/api/v1/web-integrations/id"
    }
  },
  "created": "2018-10-30T07:06:22Z",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "lastUpdated": "2018-10-30T07:06:22Z",
  "validOrigins": [
    "https://thirdPartyApp.com"
  ]
}
```

---

### GET /api/v1/web-integrations/{id}

Retrieves a single web integration by ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the web integration to retrieve. |

#### Responses

##### 200

Web integration found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique web integration identifier. |
| `name` | string | No | The name of the web integration. |
| `created` | string | No | The time the web integration was created. |
| `tenantId` | string | No | The tenant that the web integration belongs to. |
| `createdBy` | string | No | The user that created the web integration. |
| `lastUpdated` | string | No | The time the web integration was last updated. |
| `validOrigins` | string[] | No | The origins that are allowed to make requests to the tenant. |

##### 404

Web integration not found.

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
// qlik-api has not implemented support for `GET /api/v1/web-integrations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-integrations/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/web-integrations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "string",
  "created": "2018-10-30T07:06:22Z",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "lastUpdated": "2018-10-30T07:06:22Z",
  "validOrigins": [
    "string"
  ]
}
```

---

### PATCH /api/v1/web-integrations/{id}

Updates a single web integration by ID.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the web integration to update. |

#### Request Body

**Required**

Properties that the user wants to update for the web integration.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | A JSON Pointer. Enum: "/name", "/validOrigins" |
| `value` | string | Yes | New value to be used for this operation. |

#### Responses

##### 204

Web integration updated successfully.

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

##### 404

Web integration not found.

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
// qlik-api has not implemented support for `PATCH /api/v1/web-integrations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-integrations/{id}',
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
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/web-integrations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New name"}]'
```

---

### DELETE /api/v1/web-integrations/{id}

Deletes a single web integration by ID.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the web integration to delete. |

#### Responses

##### 204

Web integration deleted successfully.

##### 404

Web integration not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/web-integrations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-integrations/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/web-integrations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
