# Change stores

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Retrieve user-entered changes from write tables for export or further processing.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/analytics/change-stores`](#get-apianalyticschange-stores) | Returns a list of change-stores, accessible to the user. |
| `GET` | [`/api/analytics/change-stores/{storeId}`](#get-apianalyticschange-storesstoreid) | Returns detailed information about a specific change store, such as its configuration and associated charts. |
| `GET` | [`/api/analytics/change-stores/{storeId}/changes`](#get-apianalyticschange-storesstoreidchanges) | Returns a list of changes within the specified change-store. |
| `GET` | [`/api/analytics/change-stores/{storeId}/changes/tabular-views`](#get-apianalyticschange-storesstoreidchangestabular-views) | Returns changes in tabular format, showing modified rows with optional expansion to include all columns. |
| `GET` | [`/api/analytics/change-stores/{storeId}/editable-columns`](#get-apianalyticschange-storesstoreideditable-columns) | Returns a paginated list of editable-columns that belong to the specified change store, supporting optional filtering and sorting. |

## API Reference

### GET /api/analytics/change-stores

Returns a list of change-stores, accessible to the user.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | string | No | Used for cursor-based pagination. |
| `limit` | integer | No | Defines the size of each paged result (maximum 100). |
| `filter` | string | No | A SCIM filter expression used to filter the result. The filter parameter allows complex logical expressions using comparison operators and grouping. - **Supported attributes:** `storeName`, `storeId`, `referenceId`, `usedBy.appId`, `primaryKey`, `isUsedByEmpty` - **Supported operators:** `eq`, `ne`, `co`, `sw`, `ew`, `pr`, `gt`, `ge`, `lt`, `le`   - **Logical operators:** `and`, `or`, `not` |
| `sort` | string | No | Sort results by a field, with optional + (asc) or - (desc) prefix |
| `spaceId` | string | Yes | The space ID to filter change stores by. This parameter is required. For personal spaces, use "personal". For shared spaces, use the actual space ID, e.g. "690b584c5a8011de9079828e". |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

Returns a list of change stores.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | No |  |
| `currentPageCount` | integer | No |  |
| `links` | object | No |  |
| `data` | object[] | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

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

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usedBy` | object[] | No | List of chart/app references. |
| `spaceId` | string | No | The space id where the change store is located. |
| `storeId` | string | No | The id of the change store. |
| `tenantId` | string | No | The tenant id the change store belongs to. |
| `createdAt` | string | No | The time when the change store was created. |
| `createdBy` | string | No | The id of the user who created the change store. |
| `storeName` | string | No | The name of the change store. |
| `updatedAt` | string | No | The time when the change store was last updated. |
| `primaryKey` | string[] | No | The list of primary key columns for the change store. |
| `referenceId` | string | No | The reference id used to identify related editable-columns or change stores. |
| `publishRefId` | string | No | The publish reference id used to map stores across published apps/spaces. |

<details>
<summary>Properties of `usedBy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The id of the app. |
| `chartId` | string | Yes | The id of the chart. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/change-stores` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/change-stores',
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
# qlik-cli has not implemented support for GET /api/analytics/change-stores yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "usedBy": [
        {
          "appId": "af604296-14f6-48c2-8bac-12ce49ba83cc",
          "chartId": "chartId"
        }
      ],
      "spaceId": "456",
      "storeId": "123",
      "tenantId": "tenant789",
      "storeName": "My Change Store",
      "primaryKey": [
        "product",
        "region"
      ],
      "publishRefId": "6835b0135cf7147c01979e5d"
    },
    {
      "usedBy": [
        {
          "appId": "af604296-14f6-48c2-8bac-12ce49ba83cc",
          "chartId": "chartId2"
        }
      ],
      "spaceId": "457",
      "storeId": "124",
      "tenantId": "tenant790",
      "storeName": "Another Change Store",
      "primaryKey": [
        "category",
        "region"
      ],
      "publishRefId": "6835b0135cf7147c01979e5d"
    }
  ],
  "links": {
    "next": {
      "href": "https://example.org/api/analytics/change-stores?page=2"
    },
    "prev": {
      "href": "https://example.org/api/analytics/change-stores?page=1"
    },
    "self": {
      "href": "https://example.org/api/analytics/change-stores?page=1"
    }
  },
  "totalCount": 10,
  "currentPageCount": 2
}
```

---

### GET /api/analytics/change-stores/{storeId}

Returns detailed information about a specific change store, such as its configuration and associated charts.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `storeId` | string | Yes | The id of the change store. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

Returns a specific change store.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usedBy` | object[] | No | List of chart/app references. |
| `spaceId` | string | No | The space id where the change store is located. |
| `storeId` | string | No | The id of the change store. |
| `tenantId` | string | No | The tenant id the change store belongs to. |
| `createdAt` | string | No | The time when the change store was created. |
| `createdBy` | string | No | The id of the user who created the change store. |
| `storeName` | string | No | The name of the change store. |
| `updatedAt` | string | No | The time when the change store was last updated. |
| `primaryKey` | string[] | No | The list of primary key columns for the change store. |
| `referenceId` | string | No | The reference id used to identify related editable-columns or change stores. |
| `publishRefId` | string | No | The publish reference id used to map stores across published apps/spaces. |

<details>
<summary>Properties of `usedBy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The id of the app. |
| `chartId` | string | Yes | The id of the chart. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/change-stores/{storeId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/change-stores/{storeId}',
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
# qlik-cli has not implemented support for GET /api/analytics/change-stores/{storeId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores/{storeId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "usedBy": [
      {
        "appId": "af604296-14f6-48c2-8bac-12ce49ba83cc",
        "chartId": "chartId"
      }
    ],
    "spaceId": "456",
    "storeId": "123",
    "tenantId": "tenant789",
    "storeName": "My Change Store",
    "primaryKey": [
      "product",
      "region"
    ],
    "publishRefId": "6835b0135cf7147c01979e5d"
  }
}
```

---

### GET /api/analytics/change-stores/{storeId}/changes

Returns a list of changes within the specified change-store.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `storeId` | string | Yes | The id of the change store. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | string | No | Used for cursor-based pagination. |
| `limit` | integer | No | Defines the size of each paged result (maximum 100). |
| `filter` | string | No | A SCIM filter expression used to filter the result. The filter parameter allows complex logical expressions using comparison operators and grouping. - **Supported attributes:** `committed`, `cellKey.columnId`, `columnId`, `createdBy`, `createdAt`, `updatedAt` - **Supported operators:** `eq`, `ne`, `co`, `sw`, `ew`, `pr`, `gt`, `ge`, `lt`, `le`   - **Logical operators:** `and`, `or`, `not` |
| `sort` | string | No | Sort results by a field, with optional + (asc) or - (desc) prefix |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

Changes response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | No |  |
| `currentPageCount` | integer | No |  |
| `links` | object | No |  |
| `data` | object[] | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

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

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cellKey` | object | No |  |
| `changes` | object[] | No |  |
| `columnName` | string | No | The name of the column. |

<details>
<summary>Properties of `cellKey`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rowKey` | object | Yes | A map of row keys. |
| `columnId` | string | Yes | The id of the column. |

</details>

<details>
<summary>Properties of `changes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | No | The tenant id. |
| `cellValue` | string | No | The value of the cell. |
| `committed` | boolean | No | Whether the change has been committed. |
| `createdAt` | string | No | The time when a user starts typing in a cell and the row becomes locked. |
| `createdBy` | string | No | The id of the user who created the change. |
| `updatedAt` | string | No | The time when an update to the change has been done. Examples of when this value is updated: - User starts typing in a cell, locking the row. - User edits an unsaved change. - User saves the change. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/change-stores/{storeId}/changes` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/change-stores/{storeId}/changes',
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
# qlik-cli has not implemented support for GET /api/analytics/change-stores/{storeId}/changes yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores/{storeId}/changes" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 10,
  "currentPageCount": 2,
  "links": {
    "next": {
      "href": "https://example.org/api/analytics/change-stores?page=<next-cursor>"
    },
    "prev": {
      "href": "https://example.org/api/analytics/change-stores?page=<previous-cursor>"
    },
    "self": {
      "href": "https://example.org/api/analytics/change-stores?page=<self-cursor>"
    }
  },
  "data": [
    {
      "cellKey": {
        "rowKey": {
          "product": "table"
        },
        "columnId": "690b5975fddd52c0fba8dd10"
      },
      "changes": [
        {
          "meta": {
            "tenantId": "tenant123",
            "createdAt": "2023-01-01T12:00:00Z",
            "createdBy": "user123"
          },
          "committed": true,
          "columnValue": "100"
        }
      ],
      "columnName": "price"
    }
  ]
}
```

---

### GET /api/analytics/change-stores/{storeId}/changes/tabular-views

Returns changes in tabular format, showing modified rows with optional expansion to include all columns.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `storeId` | string | Yes | The id of the change store. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `expandRow` | boolean | No | When set to true, the records returned by this endpoint will include the latest change (if available) for each editable column in the record. This parameter should be used in combination with a filter on updatedAt for use cases that require all editable columns to be included in each response. |
| `page` | string | No | Used for cursor-based pagination. |
| `limit` | integer | No | Defines the size of each paged result (maximum 100). |
| `filter` | string | No | A SCIM filter expression used to filter the result. The filter parameter allows complex logical expressions using comparison operators and grouping. - **Supported attributes:** `committed`, `cellKey.columnId`, `columnId`, `createdBy`, `createdAt`, `updatedAt` - **Supported operators:** `eq`, `ne`, `co`, `sw`, `ew`, `pr`, `gt`, `ge`, `lt`, `le`   - **Logical operators:** `and`, `or`, `not` |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

Returns change-store values in tabular format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | No |  |
| `currentPageCount` | integer | No |  |
| `links` | object | No |  |
| `data` | object[] | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

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

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `updatedAt` | string | No | The timestamp when the row was last updated. |
| `updatedBy` | string | No | The user id that performed the latest update in the row (corresponds to updatedAt). |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/change-stores/{storeId}/changes/tabular-views` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/change-stores/{storeId}/changes/tabular-views',
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
# qlik-cli has not implemented support for GET /api/analytics/change-stores/{storeId}/changes/tabular-views yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores/{storeId}/changes/tabular-views" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 10,
  "currentPageCount": 2,
  "links": {
    "next": {
      "href": "https://example.org/api/analytics/change-stores?page=<next-cursor>"
    },
    "prev": {
      "href": "https://example.org/api/analytics/change-stores?page=<previous-cursor>"
    },
    "self": {
      "href": "https://example.org/api/analytics/change-stores?page=<self-cursor>"
    }
  },
  "data": [
    {
      "Color": "red",
      "Price": "200",
      "Product": "table",
      "updatedAt": "2023-10-01T12:00:00Z",
      "updatedBy": "abc123"
    },
    {
      "Color": "green",
      "Price": "100",
      "Product": "chair",
      "updatedAt": "2023-10-01T13:00:00Z"
    }
  ]
}
```

---

### GET /api/analytics/change-stores/{storeId}/editable-columns

Returns a paginated list of editable-columns that belong to the specified change store, supporting optional filtering and sorting.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `storeId` | string | Yes | The id of the change store. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | string | No | Used for cursor-based pagination. |
| `limit` | integer | No | Defines the size of each paged result (maximum 100). |
| `filter` | string | No | A SCIM filter expression used to filter the result. The filter parameter allows complex logical expressions using comparison operators and grouping. - **Supported attributes:** `referenceId`, `spaceId`, `createdBy`, `type`, `columnName`, `usedBy.appId`, `usedBy.chartId`  - **Supported operators:** `eq`, `ne`, `co`, `sw`, `ew`, `pr`, `gt`, `ge`, `lt`, `le`   - **Logical operators:** `and`, `or`, `not` |
| `sort` | string | No | Sort results by a field, with optional + (asc) or - (desc) prefix |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

Returns a list of editable-columns.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | No |  |
| `currentPageCount` | integer | No |  |
| `links` | object | No |  |
| `data` | object[] | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

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

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id of the editable column. |
| `type` | string | No | Type of the editable column. Enum: "editable-text", "editable-selector", "editable-date" |
| `config` | object | No | Configuration values required for the editable-column type. |
| `usedBy` | object[] | No | List of chart/app references. |
| `spaceId` | string | No | The space id that the editable columns are associated with. |
| `storeId` | string | No | Store id. |
| `tenantId` | string | No | Tenant id. |
| `createdAt` | string | No | Timestamp of creation. |
| `createdBy` | string | No | The user who created the column. |
| `updatedAt` | string | No | Timestamp of last update. |
| `columnName` | string | No | Name of the editable column. |
| `referenceId` | string | No | The unique id used to keep a reference of editable columns in multiple spaces. |
| `publishRefId` | string | No | The publish reference id used to relate editable columns between published apps/spaces. |
| `selectorValues` | object[] | No | List of value/label key/value pairs. |

<details>
<summary>Properties of `config`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `maxDate` | string | No | Maximum selectable date for editable-date columns (ISO 8601 date). |
| `minDate` | string | No | Minimum selectable date for editable-date columns (ISO 8601 date). |
| `selectorType` | string | No | Type of selector. fixed, dynamic or empty if editable-column type is not editable-selector. Enum: "fixed", "dynamic", "" |
| `selectorValues` | object[] | No | List of value/label key/value pairs. |
| `selectorExpression` | string | No | Expression used to create dynamic selector values. |

<details>
<summary>Properties of `selectorValues`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `usedBy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The id of the app. |
| `chartId` | string | Yes | The id of the chart. |

</details>

<details>
<summary>Properties of `selectorValues`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | No | The Label of the selector. |
| `value` | string | No | The Value of the selector. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | list of errors |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/change-stores/{storeId}/editable-columns` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/change-stores/{storeId}/editable-columns',
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
# qlik-cli has not implemented support for GET /api/analytics/change-stores/{storeId}/editable-columns yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores/{storeId}/editable-columns" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 10,
  "currentPageCount": 2,
  "links": {
    "next": {
      "href": "https://example.org/api/analytics/change-stores?page=<next-cursor>"
    },
    "prev": {
      "href": "https://example.org/api/analytics/change-stores?page=<previous-cursor>"
    },
    "self": {
      "href": "https://example.org/api/analytics/change-stores?page=<self-cursor>"
    }
  },
  "data": [
    {
      "id": "6835b0135cf7147c01979e5d",
      "type": "editable-text",
      "config": {
        "maxDate": "2025-12-31",
        "minDate": "2025-01-01",
        "selectorType": "fixed",
        "selectorValues": [
          {
            "label": "label1",
            "value": "value1"
          }
        ],
        "selectorExpression": "BEL~Belgium|DNK~Denmark|SWE~Sweden"
      },
      "usedBy": [
        {
          "appId": "af604296-14f6-48c2-8bac-12ce49ba83cc",
          "chartId": "chartId"
        }
      ],
      "spaceId": "6835b0135cf7147c01979e5d",
      "storeId": "507f1f77bcf86cd799439011",
      "tenantId": "tenantID",
      "createdAt": "2025-05-27T12:29:07.178Z",
      "createdBy": "testUser",
      "updatedAt": "0001-01-01T00:00:00Z",
      "columnName": "Price4",
      "referenceId": "6835b0135cf7147c01979e5d",
      "publishRefId": "6835b0135cf7147c01979e5d",
      "selectorValues": [
        {
          "label": "label1",
          "value": "value1"
        }
      ]
    }
  ]
}
```

---
