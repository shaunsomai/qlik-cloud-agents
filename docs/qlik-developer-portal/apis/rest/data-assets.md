# Data assets

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data assets are part of the catalog in Qlik Cloud. A data asset is a member of a data store, and may contain multiple data sets.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/data-assets`](#post-apiv1data-assets) |  |
| `DELETE` | [`/api/v1/data-assets`](#delete-apiv1data-assets) |  |
| `GET` | [`/api/v1/data-assets/{data-asset-id}`](#get-apiv1data-assetsdata-asset-id) |  |
| `PATCH` | [`/api/v1/data-assets/{data-asset-id}`](#patch-apiv1data-assetsdata-asset-id) |  |
| `PUT` | [`/api/v1/data-assets/{data-asset-id}`](#put-apiv1data-assetsdata-asset-id) |  |

## API Reference

### POST /api/v1/data-assets

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

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
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `dataFreshness` | string | No | The date-time when the source data was last changed |
| `dataStoreInfo` | object | No |  |
| `technicalName` | string | Yes |  |
| `technicalDescription` | string | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |

</details>

#### Responses

##### 201

Created new data asset successfully.

**Content-Type:** `application/json`

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
// qlik-api has not implemented support for `POST /api/v1/data-assets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-assets',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      name: 'string',
      tags: ['string'],
      appId: 'string',
      appType: 'string',
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      properties: {},
      description: 'string',
      dataFreshness: '2018-10-30T07:06:22Z',
      dataStoreInfo: { id: 'string' },
      technicalName: 'string',
      technicalDescription: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-assets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","name":"string","tags":["string"],"appId":"string","appType":"string","ownerId":"string","spaceId":"string","version":42,"properties":{},"description":"string","dataFreshness":"2018-10-30T07:06:22Z","dataStoreInfo":{"id":"string"},"technicalName":"string","technicalDescription":"string"}'
```

**Example Response:**

```json
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
```

---

### DELETE /api/v1/data-assets

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | string[] | No |  |

#### Responses

##### 204

Deleted data asset with all child objects.

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
// qlik-api has not implemented support for `DELETE /api/v1/data-assets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-assets',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-assets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets" \
-X DELETE \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ids":["string"]}'
```

---

### GET /api/v1/data-assets/{data-asset-id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-asset-id` | string | Yes |  |

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
// qlik-api has not implemented support for `GET /api/v1/data-assets/{data-asset-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-assets/{data-asset-id}',
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
# qlik-cli has not implemented support for GET /api/v1/data-assets/{data-asset-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets/{data-asset-id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
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
```

---

### PATCH /api/v1/data-assets/{data-asset-id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-asset-id` | string | Yes |  |

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

Patched data asset successfully.

**Content-Type:** `application/json`

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

##### 204

Patched data asset successfully.

**Content-Type:** `application/json`

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
// qlik-api has not implemented support for `PATCH /api/v1/data-assets/{data-asset-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-assets/{data-asset-id}',
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
# qlik-cli has not implemented support for PATCH /api/v1/data-assets/{data-asset-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets/{data-asset-id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","from":"string","path":"string","value":{}}]'
```

**Example Response:**

```json
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
```

---

### PUT /api/v1/data-assets/{data-asset-id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-asset-id` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

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
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `dataFreshness` | string | No | The date-time when the source data was last changed |
| `dataStoreInfo` | object | No |  |
| `technicalName` | string | Yes |  |
| `technicalDescription` | string | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |

</details>

#### Responses

##### 200

Updated data asset successfully.

**Content-Type:** `application/json`

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
// qlik-api has not implemented support for `PUT /api/v1/data-assets/{data-asset-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-assets/{data-asset-id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      name: 'string',
      tags: ['string'],
      appId: 'string',
      appType: 'string',
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      properties: {},
      description: 'string',
      dataFreshness: '2018-10-30T07:06:22Z',
      dataStoreInfo: { id: 'string' },
      technicalName: 'string',
      technicalDescription: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-assets/{data-asset-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets/{data-asset-id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","name":"string","tags":["string"],"appId":"string","appType":"string","ownerId":"string","spaceId":"string","version":42,"properties":{},"description":"string","dataFreshness":"2018-10-30T07:06:22Z","dataStoreInfo":{"id":"string"},"technicalName":"string","technicalDescription":"string"}'
```

**Example Response:**

```json
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
```

---
