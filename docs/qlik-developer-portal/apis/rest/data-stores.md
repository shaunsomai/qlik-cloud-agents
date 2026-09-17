# Data stores

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data stores are part of the catalog in Qlik Cloud. A data store may contain one or more data stores, which in turn may contain multiple data sets.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-stores`](#get-apiv1data-stores) |  |
| `POST` | [`/api/v1/data-stores`](#post-apiv1data-stores) |  |
| `DELETE` | [`/api/v1/data-stores`](#delete-apiv1data-stores) |  |
| `GET` | [`/api/v1/data-stores/{data-store-id}`](#get-apiv1data-storesdata-store-id) |  |
| `PATCH` | [`/api/v1/data-stores/{data-store-id}`](#patch-apiv1data-storesdata-store-id) |  |
| `PUT` | [`/api/v1/data-stores/{data-store-id}`](#put-apiv1data-storesdata-store-id) |  |
| `GET` | [`/api/v1/data-stores/{data-store-ids}/data-assets`](#get-apiv1data-storesdata-store-idsdata-assets) |  |
| `DELETE` | [`/api/v1/data-stores/{data-store-ids}/data-assets`](#delete-apiv1data-storesdata-store-idsdata-assets) |  |
| `GET` | [`/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets`](#get-apiv1data-storesdata-store-idsdata-assetsdata-asset-idsdata-sets) |  |
| `DELETE` | [`/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets`](#delete-apiv1data-storesdata-store-idsdata-assetsdata-asset-idsdata-sets) |  |

## API Reference

### GET /api/v1/data-stores

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Page size limit. |
| `page` | integer | No |  |
| `projections` | string[] | No | Comma-separated fields to return in the response. |
| `sort` | string[] | No | Comma-separated fields and field start with '-' character sorts the result set in descending order. |

#### Responses

##### 200

Successful Operation

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `page` | integer | No |  |
| `limit` | integer | No |  |
| `links` | object | No |  |
| `pages` | integer | No |  |
| `total` | integer | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |
| `first` | object | No |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-stores` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores',
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
# qlik-cli has not implemented support for GET /api/v1/data-stores yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "uri": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "type": "string",
      "ownerId": "string",
      "spaceId": "string",
      "version": 42,
      "tenantId": "string",
      "createdBy": "string",
      "properties": {},
      "createdTime": "2018-10-30T07:06:22Z",
      "description": "string",
      "technicalName": "string",
      "lastModifiedBy": "string",
      "lastModifiedTime": "2018-10-30T07:06:22Z",
      "technicalDescription": "string"
    }
  ],
  "page": 42,
  "limit": 42,
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  },
  "pages": 42,
  "total": 42
}
```

---

### POST /api/v1/data-stores

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `technicalDescription` | string | No |  |

#### Responses

##### 201

Created new data store successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-stores` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      uri: 'string',
      name: 'string',
      tags: ['string'],
      type: 'string',
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      properties: {},
      description: 'string',
      technicalName: 'string',
      technicalDescription: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-stores yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","uri":"string","name":"string","tags":["string"],"type":"string","ownerId":"string","spaceId":"string","version":42,"properties":{},"description":"string","technicalName":"string","technicalDescription":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "uri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "technicalName": "string",
  "lastModifiedBy": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "technicalDescription": "string"
}
```

---

### DELETE /api/v1/data-stores

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | string[] | No |  |

#### Responses

##### 204

Deleted empty data stores.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-stores` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ ids: ['string'] }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/data-stores yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores" \
-X DELETE \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ids":["string"]}'
```

---

### GET /api/v1/data-stores/{data-store-id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-store-id` | string | Yes |  |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projections` | string[] | No | Comma-separated fields to return in the response. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-stores/{data-store-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-id}',
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
# qlik-cli has not implemented support for GET /api/v1/data-stores/{data-store-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "uri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "technicalName": "string",
  "lastModifiedBy": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "technicalDescription": "string"
}
```

---

### PATCH /api/v1/data-stores/{data-store-id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-store-id` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "add", "remove", "replace", "move", "copy", "test" |
| `from` | string | No | A JSON Pointer path pointing to the location to move/copy from. |
| `path` | string | Yes | A JSON pointer to the property being affected. |
| `value` | object | No | The value to add, replace or test. |

#### Responses

##### 200

Patched data store successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

##### 204

Patched data store successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/data-stores/{data-store-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        from: 'string',
        path: 'string',
        value: {},
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/data-stores/{data-store-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","from":"string","path":"string","value":{}}]'
```

**Example Response:**

```json
{
  "id": "string",
  "uri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "technicalName": "string",
  "lastModifiedBy": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "technicalDescription": "string"
}
```

---

### PUT /api/v1/data-stores/{data-store-id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-store-id` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `technicalDescription` | string | No |  |

#### Responses

##### 200

Updated data store successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `uri` | string | No |  |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/data-stores/{data-store-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      uri: 'string',
      name: 'string',
      tags: ['string'],
      type: 'string',
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      properties: {},
      description: 'string',
      technicalName: 'string',
      technicalDescription: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-stores/{data-store-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","uri":"string","name":"string","tags":["string"],"type":"string","ownerId":"string","spaceId":"string","version":42,"properties":{},"description":"string","technicalName":"string","technicalDescription":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "uri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "technicalName": "string",
  "lastModifiedBy": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "technicalDescription": "string"
}
```

---

### GET /api/v1/data-stores/{data-store-ids}/data-assets

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-store-ids` | string[] | Yes | Comma-separated data store IDs or * to include all data stores. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Page size limit. |
| `page` | integer | No |  |
| `projections` | string[] | No | Comma-separated fields to return in the response. |
| `sort` | string[] | No | Comma-separated fields and field start with '-' character sorts the result set in descending order. |

#### Responses

##### 200

Successful Operation

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `page` | integer | No |  |
| `limit` | integer | No |  |
| `links` | object | No |  |
| `pages` | integer | No |  |
| `total` | integer | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `appId` | string | No |  |
| `appType` | string | Yes |  |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `dataFreshness` | string | No | The date-time when the source data was last changed |
| `dataStoreInfo` | object | No |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `technicalDescription` | string | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |
| `first` | object | No |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-stores/{data-store-ids}/data-assets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-ids}/data-assets',
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
# qlik-cli has not implemented support for GET /api/v1/data-stores/{data-store-ids}/data-assets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-ids}/data-assets" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "appId": "string",
      "appType": "string",
      "ownerId": "string",
      "spaceId": "string",
      "version": 42,
      "tenantId": "string",
      "createdBy": "string",
      "properties": {},
      "createdTime": "2018-10-30T07:06:22Z",
      "description": "string",
      "dataFreshness": "2018-10-30T07:06:22Z",
      "dataStoreInfo": {
        "id": "string",
        "name": "string",
        "type": "string"
      },
      "technicalName": "string",
      "lastModifiedBy": "string",
      "lastModifiedTime": "2018-10-30T07:06:22Z",
      "technicalDescription": "string"
    }
  ],
  "page": 42,
  "limit": 42,
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  },
  "pages": 42,
  "total": 42
}
```

---

### DELETE /api/v1/data-stores/{data-store-ids}/data-assets

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-store-ids` | string[] | Yes | Comma-separated data store IDs or * to include all data stores. |

#### Responses

##### 204

Deleted data assets successfully.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-stores/{data-store-ids}/data-assets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-ids}/data-assets',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-stores/{data-store-ids}/data-assets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-ids}/data-assets" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-asset-ids` | string[] | Yes | Comma-separated data asset IDs or * to include all data assets. |
| `data-store-ids` | string[] | Yes | Comma-separated data store IDs or * to include all data stores. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Page size limit. |
| `page` | integer | No |  |
| `projections` | string[] | No | Comma-separated fields to return in the response. |
| `sort` | string[] | No | Comma-separated fields and field start with '-' character sorts the result set in descending order. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `page` | integer | No |  |
| `limit` | integer | No |  |
| `links` | object | No |  |
| `pages` | integer | No |  |
| `total` | integer | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |
| `first` | object | No |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets',
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
# qlik-cli has not implemented support for GET /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "qri": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "type": "string",
      "schema": {
        "anomalies": [
          "string"
        ],
        "dataFields": [
          {
            "name": "string",
            "tags": [
              "string"
            ],
            "alias": "string",
            "index": 42,
            "orphan": true,
            "dataType": {
              "type": "DATE",
              "properties": {},
              "originalType": "string"
            },
            "nullable": true,
            "userTags": [
              {
                "id": "string",
                "name": "string"
              }
            ],
            "encrypted": true,
            "sensitive": true,
            "primaryKey": true,
            "properties": {},
            "description": "string",
            "ordinalPositionInKey": 42
          }
        ],
        "schemaName": "string",
        "loadOptions": {},
        "effectiveDate": "2018-10-30T07:06:22Z",
        "overrideSchemaAnomalies": true
      },
      "ownerId": "string",
      "spaceId": "string",
      "version": 42,
      "tenantId": "string",
      "createdBy": "string",
      "secureQri": "string",
      "properties": {},
      "createdTime": "2018-10-30T07:06:22Z",
      "description": "string",
      "operational": {
        "size": 42,
        "status": "string",
        "endDate": "2018-10-30T07:06:22Z",
        "location": "string",
        "rowCount": 42,
        "startDate": "2018-10-30T07:06:22Z",
        "logMessage": "string",
        "tableOwner": "string",
        "lastLoadTime": "2018-10-30T07:06:22Z",
        "contentUpdated": true,
        "lastUpdateTime": "2018-10-30T07:06:22Z",
        "tableConnectionInfo": {
          "tableName": "string",
          "selectionScript": "string",
          "additionalProperties": {}
        }
      },
      "dataAssetInfo": {
        "id": "string",
        "name": "string",
        "dataStoreInfo": {
          "id": "string",
          "name": "string",
          "type": "string"
        }
      },
      "technicalName": "string",
      "lastModifiedBy": "string",
      "appTypeOverride": "string",
      "lastModifiedTime": "2018-10-30T07:06:22Z",
      "additionalSchemas": [
        {
          "anomalies": [
            "string"
          ],
          "dataFields": [
            {
              "name": "string",
              "tags": [
                "string"
              ],
              "alias": "string",
              "index": 42,
              "orphan": true,
              "dataType": {
                "type": "DATE",
                "properties": {},
                "originalType": "string"
              },
              "nullable": true,
              "userTags": [
                {
                  "id": "string",
                  "name": "string"
                }
              ],
              "encrypted": true,
              "sensitive": true,
              "primaryKey": true,
              "properties": {},
              "description": "string",
              "ordinalPositionInKey": 42
            }
          ],
          "schemaName": "string",
          "loadOptions": {},
          "effectiveDate": "2018-10-30T07:06:22Z",
          "overrideSchemaAnomalies": true
        }
      ],
      "technicalDescription": "string",
      "createdByConnectionId": "string"
    }
  ],
  "page": 42,
  "limit": 42,
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  },
  "pages": 42,
  "total": 42
}
```

---

### DELETE /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-asset-ids` | string[] | Yes | Comma-separated data asset IDs or * to include all data assets. |
| `data-store-ids` | string[] | Yes | Comma-separated data store IDs or * to include all data stores. |

#### Responses

##### 204

Deleted data sets.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores/{data-store-ids}/data-assets/{data-asset-ids}/data-sets" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
