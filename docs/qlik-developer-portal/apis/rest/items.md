# Items

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Items provides a list of core resources in the Qlik platform, including resources such as apps, automations, and data sets that a user has access to.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/items`](#get-apiv1items) | Lists items that the user has access to. |
| `GET` | [`/api/v1/items/{itemId}`](#get-apiv1itemsitemid) | Finds and returns an item. |
| `PUT` | [`/api/v1/items/{itemId}`](#put-apiv1itemsitemid) | Updates an item. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value. |
| `DELETE` | [`/api/v1/items/{itemId}`](#delete-apiv1itemsitemid) | Deletes an item and removes the item from all collections. |
| `GET` | [`/api/v1/items/{itemId}/collections`](#get-apiv1itemsitemidcollections) | Finds and returns the collections (and tags) of an item. This endpoint does not return the user's favorites collection. |
| `GET` | [`/api/v1/items/{itemId}/publisheditems`](#get-apiv1itemsitemidpublisheditems) | Finds and returns the published items for a given item. This endpoint is particularly useful for finding the published copies of an app or a qvapp when you want to replace the content of a published copy with new information from the source item. |
| `GET` | [`/api/v1/items/settings`](#get-apiv1itemssettings) | Finds and returns the items service settings for the current tenant. Currently used to enable or disable usage metrics in the tenant. |
| `PATCH` | [`/api/v1/items/settings`](#patch-apiv1itemssettings) | Updates the settings provided in the patch body. Currently used to enable or disable usage metrics in the tenant. |

## API Reference

### GET /api/v1/items

Lists items that the user has access to.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | No | The collection's unique identifier. Used to filter for items with a specific tag (collection type `public`), or collection. |
| `createdByUserId` | string | No | User's unique identifier. |
| `id` | string | No | The item's unique identifier. |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `name` | string | No | The case-insensitive string used to search for a resource by name. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `notCreatedByUserId` | string | No | User's unique identifier. |
| `notOwnerId` | string | No | Owner identifier. |
| `ownerId` | string | No | Owner identifier. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `query` | string | No | The case-insensitive string used to search for a resource by name or description. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceIds` | string | No | The case-sensitive strings used to search for an item by resourceIds. The maximum number of resourceIds it supports is 100. If resourceIds is provided, then resourceType must be provided. For example '?resourceIds=appId1,appId2' |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceSubType` | string | No | the case-sensitive string used to filter items by resourceSubType(s). For example '?resourceSubType=chart-monitoring,qix-df,qvd'. Will return a 400 error if used in conjuction with the square bracket syntax for resourceSubType filtering in the 'resourceType' query parameter. |
| `resourceType` | string | No | The case-sensitive string used to filter items by resourceType(s). For example '?resourceType=app,qvapp'. Additionally, a optional resourceSubType filter can be added to each resourceType. For example '?resourceType=app[qvd,chart-monitoring],qvapp'. An trailing comma can be used to include the empty resourceSubType, e.g. '?resourceType=app[qvd,chart-monitoring,]', or, to include only empty resourceSubTypes, '?resourceType=app[]' This syntax replaces the 'resourceSubType' query param, and using both in the same query will result in a 400 error. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `sort` | string | No | The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, recentlyUsed and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively. Enum: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt", "+recentlyUsed", "-recentlyUsed" |
| `spaceId` | string | No | The space's unique identifier (supports \'personal\' as spaceId). |
| `spaceType` | string | No | The case-sensitive string used to filter items on space type(s). For example '?spaceType=shared,personal'. Enum: "shared", "managed", "personal", "data" |
| `shared` | boolean | No | _(deprecated)_ Whether or not to return items in a shared space. |
| `noActions` | boolean | No | If set to true, the user's available actions for each item will not be evaluated meaning the actions-array will be omitted from the response (reduces response time). |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The item's unique identifier. |
| `meta` | object | Yes | Item metadata and computed fields. |
| `name` | string | Yes |  |
| `links` | object | Yes |  |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `ownerId` | string | No | The ID of the user who owns the item. |
| `spaceId` | string | No | The space's unique identifier. |
| `tenantId` | string | Yes | The ID of the tenant that owns the item. This is populated using the JWT. |
| `createdAt` | string | Yes | The RFC3339 datetime when the item was created. |
| `creatorId` | string | No | The ID of the user who created the item. This is only populated if the JWT contains a userId. |
| `itemViews` | object | No |  |
| `updatedAt` | string | Yes | The RFC3339 datetime when the item was last updated. |
| `updaterId` | string | No | ID of the user who last updated the item. This is only populated if the JWT contains a userId. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `description` | string | No |  |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |
| `thumbnailId` | string | No | The item thumbnail's unique identifier. This is optional for internal resources. |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceSize` | object | No |  |
| `resourceType` | string | Yes | The case-sensitive string defining the item's type. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `collectionIds` | string[] | Yes | The ID of the collections that the item has been added to. |
| `resourceSubType` | string | No | Optional field defining the item's subtype, if any. |
| `resourceCreatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was created. |
| `resourceUpdatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was last updated. |
| `resourceAttributes` | object | Yes |  |
| `resourceReloadStatus` | string | No | If the resource last reload was successful or not. |
| `resourceReloadEndTime` | string | No | The RFC3339 datetime when the resource last reload ended. |
| `resourceCustomAttributes` | object | Yes |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tags` | object[] | Yes | An array of tags that the item is part of. |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `collections` | object[] | Yes | An array of collections that the item is part of. |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |

<details>
<summary>Properties of `tags`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `collections`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `open` | object | No |  |
| `self` | object | No |  |
| `qvPlugin` | object | No |  |
| `thumbnail` | object | No |  |
| `collections` | object | No |  |

<details>
<summary>Properties of `open`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `qvPlugin`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `thumbnail`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `collections`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `itemViews`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `week` | object[] | No |  |
| `total` | integer | No | Total number of views the resource got during the last 28 days. |
| `trend` | number | No | Trend in views over the last 4 weeks. The trend value is a float number representing a linear regression slope (the x-coefficient) calculated from the weekly unique users views in the preceding 4 weeks. |
| `unique` | integer | No | Number of unique users who viewed the resource during the last 28 days. |
| `usedBy` | integer | No | Number of apps this dataset is used in (datasets only). |

<details>
<summary>Properties of `week`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `resourceSize`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appFile` | number | No | Size of the app on disk in bytes. |
| `appMemory` | number | No | Size of the app in memory in bytes. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |
| `collection` | object | No |  |

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
<summary>Properties of `collection`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not Found response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/items` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/items', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/items yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "meta": {
        "tags": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "actions": [
          "string"
        ],
        "collections": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "isFavorited": true
      },
      "name": "string",
      "links": {
        "open": {
          "href": "string"
        },
        "self": {
          "href": "string"
        },
        "qvPlugin": {
          "href": "string"
        },
        "thumbnail": {
          "href": "string"
        },
        "collections": {
          "href": "string"
        }
      },
      "actions": [
        "string"
      ],
      "ownerId": "string",
      "spaceId": "string",
      "tenantId": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "creatorId": "string",
      "itemViews": {
        "week": [
          {
            "start": "2018-10-30T07:06:22Z",
            "total": 42,
            "unique": 42
          }
        ],
        "total": 42,
        "trend": -4.2,
        "unique": 42,
        "usedBy": 42
      },
      "updatedAt": "2018-10-30T07:06:22Z",
      "updaterId": "string",
      "resourceId": "string",
      "description": "string",
      "isFavorited": true,
      "thumbnailId": "string",
      "resourceLink": "string",
      "resourceSize": {
        "appFile": 42,
        "appMemory": 42
      },
      "resourceType": "app",
      "collectionIds": [
        "string"
      ],
      "resourceSubType": "string",
      "resourceCreatedAt": "2018-10-30T07:06:22Z",
      "resourceUpdatedAt": "2018-10-30T07:06:22Z",
      "resourceAttributes": {},
      "resourceReloadStatus": "string",
      "resourceReloadEndTime": "2018-10-30T07:06:22Z",
      "resourceCustomAttributes": {}
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
    },
    "collection": {
      "href": "string"
    }
  }
}
```

---

### GET /api/v1/items/{itemId}

Finds and returns an item.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemId` | string | Yes | The item's unique identifier |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The item's unique identifier. |
| `meta` | object | Yes | Item metadata and computed fields. |
| `name` | string | Yes |  |
| `links` | object | Yes |  |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `ownerId` | string | No | The ID of the user who owns the item. |
| `spaceId` | string | No | The space's unique identifier. |
| `tenantId` | string | Yes | The ID of the tenant that owns the item. This is populated using the JWT. |
| `createdAt` | string | Yes | The RFC3339 datetime when the item was created. |
| `creatorId` | string | No | The ID of the user who created the item. This is only populated if the JWT contains a userId. |
| `itemViews` | object | No |  |
| `updatedAt` | string | Yes | The RFC3339 datetime when the item was last updated. |
| `updaterId` | string | No | ID of the user who last updated the item. This is only populated if the JWT contains a userId. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `description` | string | No |  |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |
| `thumbnailId` | string | No | The item thumbnail's unique identifier. This is optional for internal resources. |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceSize` | object | No |  |
| `resourceType` | string | Yes | The case-sensitive string defining the item's type. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `collectionIds` | string[] | Yes | The ID of the collections that the item has been added to. |
| `resourceSubType` | string | No | Optional field defining the item's subtype, if any. |
| `resourceCreatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was created. |
| `resourceUpdatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was last updated. |
| `resourceAttributes` | object | Yes |  |
| `resourceReloadStatus` | string | No | If the resource last reload was successful or not. |
| `resourceReloadEndTime` | string | No | The RFC3339 datetime when the resource last reload ended. |
| `resourceCustomAttributes` | object | Yes |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tags` | object[] | Yes | An array of tags that the item is part of. |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `collections` | object[] | Yes | An array of collections that the item is part of. |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |

<details>
<summary>Properties of `tags`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the tag/collection. |
| `name` | string | Yes | The name of the tag/collection. |

</details>

<details>
<summary>Properties of `collections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the tag/collection. |
| `name` | string | Yes | The name of the tag/collection. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `open` | object | No |  |
| `self` | object | No |  |
| `qvPlugin` | object | No |  |
| `thumbnail` | object | No |  |
| `collections` | object | No |  |

<details>
<summary>Properties of `open`</summary>

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
<summary>Properties of `qvPlugin`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `thumbnail`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `collections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `itemViews`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `week` | object[] | No |  |
| `total` | integer | No | Total number of views the resource got during the last 28 days. |
| `trend` | number | No | Trend in views over the last 4 weeks. The trend value is a float number representing a linear regression slope (the x-coefficient) calculated from the weekly unique users views in the preceding 4 weeks. |
| `unique` | integer | No | Number of unique users who viewed the resource during the last 28 days. |
| `usedBy` | integer | No | Number of apps this dataset is used in (datasets only). |

<details>
<summary>Properties of `week`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `start` | string | No | The RFC3339 datetime representing the start of the referenced week. |
| `total` | integer | No | Total number of views the resource got during the referenced week. |
| `unique` | integer | No | Number of unique users who viewed the resource during the referenced week. |

</details>

</details>

<details>
<summary>Properties of `resourceSize`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appFile` | number | No | Size of the app on disk in bytes. |
| `appMemory` | number | No | Size of the app in memory in bytes. |

</details>

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not Found response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/items/{itemId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/{itemId}',
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
# qlik-cli has not implemented support for GET /api/v1/items/{itemId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/{itemId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "meta": {
    "tags": [
      {
        "id": "string",
        "name": "string"
      }
    ],
    "actions": [
      "string"
    ],
    "collections": [
      {
        "id": "string",
        "name": "string"
      }
    ],
    "isFavorited": true
  },
  "name": "string",
  "links": {
    "open": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "qvPlugin": {
      "href": "string"
    },
    "thumbnail": {
      "href": "string"
    },
    "collections": {
      "href": "string"
    }
  },
  "actions": [
    "string"
  ],
  "ownerId": "string",
  "spaceId": "string",
  "tenantId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "creatorId": "string",
  "itemViews": {
    "week": [
      {
        "start": "2018-10-30T07:06:22Z",
        "total": 42,
        "unique": 42
      }
    ],
    "total": 42,
    "trend": -4.2,
    "unique": 42,
    "usedBy": 42
  },
  "updatedAt": "2018-10-30T07:06:22Z",
  "updaterId": "string",
  "resourceId": "string",
  "description": "string",
  "isFavorited": true,
  "thumbnailId": "string",
  "resourceLink": "string",
  "resourceSize": {
    "appFile": 42,
    "appMemory": 42
  },
  "resourceType": "app",
  "collectionIds": [
    "string"
  ],
  "resourceSubType": "string",
  "resourceCreatedAt": "2018-10-30T07:06:22Z",
  "resourceUpdatedAt": "2018-10-30T07:06:22Z",
  "resourceAttributes": {},
  "resourceReloadStatus": "string",
  "resourceReloadEndTime": "2018-10-30T07:06:22Z",
  "resourceCustomAttributes": {}
}
```

---

### PUT /api/v1/items/{itemId}

Updates an item. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemId` | string | Yes | The item's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `spaceId` | string | No | The space's unique identifier. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `description` | string | No |  |
| `thumbnailId` | string | No | The item thumbnail's unique identifier. This is optional for internal resources. |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceType` | string | Yes | The case-sensitive string defining the item's type. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `resourceSubType` | string | No | Optional field defining the item's subtype, if any. |
| `resourceUpdatedAt` | string | No | The RFC3339 datetime when the resource that the item references was last updated. |
| `resourceAttributes` | object | No |  |
| `resourceCustomAttributes` | object | No |  |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The item's unique identifier. |
| `meta` | object | Yes | Item metadata and computed fields. |
| `name` | string | Yes |  |
| `links` | object | Yes |  |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `ownerId` | string | No | The ID of the user who owns the item. |
| `spaceId` | string | No | The space's unique identifier. |
| `tenantId` | string | Yes | The ID of the tenant that owns the item. This is populated using the JWT. |
| `createdAt` | string | Yes | The RFC3339 datetime when the item was created. |
| `creatorId` | string | No | The ID of the user who created the item. This is only populated if the JWT contains a userId. |
| `itemViews` | object | No |  |
| `updatedAt` | string | Yes | The RFC3339 datetime when the item was last updated. |
| `updaterId` | string | No | ID of the user who last updated the item. This is only populated if the JWT contains a userId. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `description` | string | No |  |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |
| `thumbnailId` | string | No | The item thumbnail's unique identifier. This is optional for internal resources. |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceSize` | object | No |  |
| `resourceType` | string | Yes | The case-sensitive string defining the item's type. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `collectionIds` | string[] | Yes | The ID of the collections that the item has been added to. |
| `resourceSubType` | string | No | Optional field defining the item's subtype, if any. |
| `resourceCreatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was created. |
| `resourceUpdatedAt` | string | Yes | The RFC3339 datetime when the resource that the item references was last updated. |
| `resourceAttributes` | object | Yes |  |
| `resourceReloadStatus` | string | No | If the resource last reload was successful or not. |
| `resourceReloadEndTime` | string | No | The RFC3339 datetime when the resource last reload ended. |
| `resourceCustomAttributes` | object | Yes |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tags` | object[] | Yes | An array of tags that the item is part of. |
| `actions` | string[] | Yes | The actions that the user can perform on the item. |
| `collections` | object[] | Yes | An array of collections that the item is part of. |
| `isFavorited` | boolean | Yes | The flag that indicates if item is in the user's favorites collection. |

<details>
<summary>Properties of `tags`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the tag/collection. |
| `name` | string | Yes | The name of the tag/collection. |

</details>

<details>
<summary>Properties of `collections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the tag/collection. |
| `name` | string | Yes | The name of the tag/collection. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `open` | object | No |  |
| `self` | object | No |  |
| `qvPlugin` | object | No |  |
| `thumbnail` | object | No |  |
| `collections` | object | No |  |

<details>
<summary>Properties of `open`</summary>

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
<summary>Properties of `qvPlugin`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `thumbnail`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `collections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `itemViews`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `week` | object[] | No |  |
| `total` | integer | No | Total number of views the resource got during the last 28 days. |
| `trend` | number | No | Trend in views over the last 4 weeks. The trend value is a float number representing a linear regression slope (the x-coefficient) calculated from the weekly unique users views in the preceding 4 weeks. |
| `unique` | integer | No | Number of unique users who viewed the resource during the last 28 days. |
| `usedBy` | integer | No | Number of apps this dataset is used in (datasets only). |

<details>
<summary>Properties of `week`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `start` | string | No | The RFC3339 datetime representing the start of the referenced week. |
| `total` | integer | No | Total number of views the resource got during the referenced week. |
| `unique` | integer | No | Number of unique users who viewed the resource during the referenced week. |

</details>

</details>

<details>
<summary>Properties of `resourceSize`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appFile` | number | No | Size of the app on disk in bytes. |
| `appMemory` | number | No | Size of the app in memory in bytes. |

</details>

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 403

Forbidden response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not Found response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 409

Conflict response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/items/{itemId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/{itemId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      spaceId: 'string',
      resourceId: 'string',
      description: 'string',
      thumbnailId: 'string',
      resourceLink: 'string',
      resourceType: 'app',
      resourceSubType: 'string',
      resourceUpdatedAt: '2018-10-30T07:06:22Z',
      resourceAttributes: {},
      resourceCustomAttributes: {},
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/items/{itemId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/{itemId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","spaceId":"string","resourceId":"string","description":"string","thumbnailId":"string","resourceLink":"string","resourceType":"app","resourceSubType":"string","resourceUpdatedAt":"2018-10-30T07:06:22Z","resourceAttributes":{},"resourceCustomAttributes":{}}'
```

**Example Response:**

```json
{
  "id": "string",
  "meta": {
    "tags": [
      {
        "id": "string",
        "name": "string"
      }
    ],
    "actions": [
      "string"
    ],
    "collections": [
      {
        "id": "string",
        "name": "string"
      }
    ],
    "isFavorited": true
  },
  "name": "string",
  "links": {
    "open": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "qvPlugin": {
      "href": "string"
    },
    "thumbnail": {
      "href": "string"
    },
    "collections": {
      "href": "string"
    }
  },
  "actions": [
    "string"
  ],
  "ownerId": "string",
  "spaceId": "string",
  "tenantId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "creatorId": "string",
  "itemViews": {
    "week": [
      {
        "start": "2018-10-30T07:06:22Z",
        "total": 42,
        "unique": 42
      }
    ],
    "total": 42,
    "trend": -4.2,
    "unique": 42,
    "usedBy": 42
  },
  "updatedAt": "2018-10-30T07:06:22Z",
  "updaterId": "string",
  "resourceId": "string",
  "description": "string",
  "isFavorited": true,
  "thumbnailId": "string",
  "resourceLink": "string",
  "resourceSize": {
    "appFile": 42,
    "appMemory": 42
  },
  "resourceType": "app",
  "collectionIds": [
    "string"
  ],
  "resourceSubType": "string",
  "resourceCreatedAt": "2018-10-30T07:06:22Z",
  "resourceUpdatedAt": "2018-10-30T07:06:22Z",
  "resourceAttributes": {},
  "resourceReloadStatus": "string",
  "resourceReloadEndTime": "2018-10-30T07:06:22Z",
  "resourceCustomAttributes": {}
}
```

---

### DELETE /api/v1/items/{itemId}

Deletes an item and removes the item from all collections.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemId` | string | Yes | The item's unique identifier. |

#### Responses

##### 204

No Content response.

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 403

Forbidden response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not Found response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/items/{itemId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/{itemId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/items/{itemId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/{itemId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/items/{itemId}/collections

Finds and returns the collections (and tags) of an item. This endpoint does not return the user's favorites collection.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemId` | string | Yes | The item's unique identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `name` | string | No | The case-sensitive string used to search for a collection by name. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `query` | string | No | The case-insensitive string used to search for a resource by name or description. |
| `sort` | string | No | The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively. Enum: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt" |
| `type` | string | No | The case-sensitive string used to search for a collection by type. Enum: "private", "public", "publicgoverned" |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | A collection. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The collection's unique identifier. |
| `full` | boolean | No | States if a collection has reached its items limit or not |
| `meta` | object | No | Collection metadata and computed fields. |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "private", "public", "favorite", "publicgoverned" |
| `links` | object | Yes |  |
| `tenantId` | string | Yes | The ID of the tenant that owns the collection. This property is populated by using JWT. |
| `createdAt` | string | Yes | The RFC3339 datetime when the collection was created. |
| `creatorId` | string | No | The ID of the user who created the collection. This property is only populated if the JWT contains a userId. |
| `itemCount` | integer | Yes | The number of items that have been added to the collection that the user has access to. |
| `updatedAt` | string | Yes | The RFC3339 datetime when the collection was last updated. |
| `updaterId` | string | No | The ID of the user who last updated the collection. This property is only populated if the JWT contains a userId. |
| `description` | string | No |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `items` | object | No | Multiple items. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No |  |
| `items` | object | No |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `item`</summary>

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

</details>

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not found response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/items/{itemId}/collections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/{itemId}/collections',
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
# qlik-cli has not implemented support for GET /api/v1/items/{itemId}/collections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/{itemId}/collections" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "full": true,
      "meta": {
        "items": {
          "data": [
            {
              "id": "string",
              "meta": {
                "tags": [
                  {
                    "id": "string",
                    "name": "string"
                  }
                ],
                "actions": [
                  "string"
                ],
                "collections": [
                  {
                    "id": "string",
                    "name": "string"
                  }
                ],
                "isFavorited": true
              },
              "name": "string",
              "links": {
                "open": {
                  "href": "string"
                },
                "self": {
                  "href": "string"
                },
                "qvPlugin": {
                  "href": "string"
                },
                "thumbnail": {
                  "href": "string"
                },
                "collections": {
                  "href": "string"
                }
              },
              "actions": [
                "string"
              ],
              "ownerId": "string",
              "spaceId": "string",
              "tenantId": "string",
              "createdAt": "2018-10-30T07:06:22Z",
              "creatorId": "string",
              "itemViews": {
                "week": [
                  {
                    "start": "2018-10-30T07:06:22Z",
                    "total": 42,
                    "unique": 42
                  }
                ],
                "total": 42,
                "trend": -4.2,
                "unique": 42,
                "usedBy": 42
              },
              "updatedAt": "2018-10-30T07:06:22Z",
              "updaterId": "string",
              "resourceId": "string",
              "description": "string",
              "isFavorited": true,
              "thumbnailId": "string",
              "resourceLink": "string",
              "resourceSize": {
                "appFile": 42,
                "appMemory": 42
              },
              "resourceType": "app",
              "collectionIds": [
                "string"
              ],
              "resourceSubType": "string",
              "resourceCreatedAt": "2018-10-30T07:06:22Z",
              "resourceUpdatedAt": "2018-10-30T07:06:22Z",
              "resourceAttributes": {},
              "resourceReloadStatus": "string",
              "resourceReloadEndTime": "2018-10-30T07:06:22Z",
              "resourceCustomAttributes": {}
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
            },
            "collection": {
              "href": "string"
            }
          }
        }
      },
      "name": "string",
      "type": "private",
      "links": {
        "self": {
          "href": "string"
        },
        "items": {
          "href": "string"
        }
      },
      "tenantId": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "creatorId": "string",
      "itemCount": 42,
      "updatedAt": "2018-10-30T07:06:22Z",
      "updaterId": "string",
      "description": "string"
    }
  ],
  "links": {
    "item": {
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
    }
  }
}
```

---

### GET /api/v1/items/{itemId}/publisheditems

Finds and returns the published items for a given item. This endpoint is particularly useful for finding the published copies of an app or a qvapp when you want to replace the content of a published copy with new information from the source item.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemId` | string | Yes | The item's unique identifier |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `resourceType` | string | No | The case-sensitive string used to search for an item by resourceType. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `sort` | string | No | The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively. Enum: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt" |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | A collection. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The collection's unique identifier. |
| `full` | boolean | No | States if a collection has reached its items limit or not |
| `meta` | object | No | Collection metadata and computed fields. |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "private", "public", "favorite", "publicgoverned" |
| `links` | object | Yes |  |
| `tenantId` | string | Yes | The ID of the tenant that owns the collection. This property is populated by using JWT. |
| `createdAt` | string | Yes | The RFC3339 datetime when the collection was created. |
| `creatorId` | string | No | The ID of the user who created the collection. This property is only populated if the JWT contains a userId. |
| `itemCount` | integer | Yes | The number of items that have been added to the collection that the user has access to. |
| `updatedAt` | string | Yes | The RFC3339 datetime when the collection was last updated. |
| `updaterId` | string | No | The ID of the user who last updated the collection. This property is only populated if the JWT contains a userId. |
| `description` | string | No |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `items` | object | No | Multiple items. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No |  |
| `items` | object | No |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `item`</summary>

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

</details>

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 404

Not Found response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/items/{itemId}/publisheditems` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/{itemId}/publisheditems',
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
# qlik-cli has not implemented support for GET /api/v1/items/{itemId}/publisheditems yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/{itemId}/publisheditems" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "full": true,
      "meta": {
        "items": {
          "data": [
            {
              "id": "string",
              "meta": {
                "tags": [
                  {
                    "id": "string",
                    "name": "string"
                  }
                ],
                "actions": [
                  "string"
                ],
                "collections": [
                  {
                    "id": "string",
                    "name": "string"
                  }
                ],
                "isFavorited": true
              },
              "name": "string",
              "links": {
                "open": {
                  "href": "string"
                },
                "self": {
                  "href": "string"
                },
                "qvPlugin": {
                  "href": "string"
                },
                "thumbnail": {
                  "href": "string"
                },
                "collections": {
                  "href": "string"
                }
              },
              "actions": [
                "string"
              ],
              "ownerId": "string",
              "spaceId": "string",
              "tenantId": "string",
              "createdAt": "2018-10-30T07:06:22Z",
              "creatorId": "string",
              "itemViews": {
                "week": [
                  {
                    "start": "2018-10-30T07:06:22Z",
                    "total": 42,
                    "unique": 42
                  }
                ],
                "total": 42,
                "trend": -4.2,
                "unique": 42,
                "usedBy": 42
              },
              "updatedAt": "2018-10-30T07:06:22Z",
              "updaterId": "string",
              "resourceId": "string",
              "description": "string",
              "isFavorited": true,
              "thumbnailId": "string",
              "resourceLink": "string",
              "resourceSize": {
                "appFile": 42,
                "appMemory": 42
              },
              "resourceType": "app",
              "collectionIds": [
                "string"
              ],
              "resourceSubType": "string",
              "resourceCreatedAt": "2018-10-30T07:06:22Z",
              "resourceUpdatedAt": "2018-10-30T07:06:22Z",
              "resourceAttributes": {},
              "resourceReloadStatus": "string",
              "resourceReloadEndTime": "2018-10-30T07:06:22Z",
              "resourceCustomAttributes": {}
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
            },
            "collection": {
              "href": "string"
            }
          }
        }
      },
      "name": "string",
      "type": "private",
      "links": {
        "self": {
          "href": "string"
        },
        "items": {
          "href": "string"
        }
      },
      "tenantId": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "creatorId": "string",
      "itemCount": 42,
      "updatedAt": "2018-10-30T07:06:22Z",
      "updaterId": "string",
      "description": "string"
    }
  ],
  "links": {
    "item": {
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
    }
  }
}
```

---

### GET /api/v1/items/settings

Finds and returns the items service settings for the current tenant. Currently used to enable or disable usage metrics in the tenant.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usageMetricsEnabled` | boolean | Yes | Decides if the usage metrics will be shown in the hub UI. |

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/items/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/settings',
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
# qlik-cli has not implemented support for GET /api/v1/items/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "usageMetricsEnabled": true
}
```

---

### PATCH /api/v1/items/settings

Updates the settings provided in the patch body. Currently used to enable or disable usage metrics in the tenant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Only "replace" is supported. Enum: "replace" |
| `path` | string | Yes | Field of Settings to be patched (updated). Enum: "/usageMetricsEnabled" |
| `value` | boolean | Yes | The value to be used within the operations. |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usageMetricsEnabled` | boolean | Yes | Decides if the usage metrics will be shown in the hub UI. |

##### 400

Bad Request response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 401

Unauthorized response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 403

Forbidden response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

##### 500

Internal Server Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Code is a unique identifier for this error class. |
| `meta` | object | No |  |
| `title` | string | No | Title is the name of this class of errors. |
| `detail` | string | No | Detail is a human-readable explanation specific to this occurrence of the problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fault` | boolean | No | Is the error a server-side fault? |
| `explain` | object | No | Further explanation of the error |
| `timeout` | boolean | No | Is the error a timeout? |
| `temporary` | boolean | No | Is the error temporary? |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/items/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/items/settings',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/usageMetricsEnabled',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/items/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/items/settings" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/usageMetricsEnabled","value":true}]'
```

**Example Response:**

```json
{
  "usageMetricsEnabled": true
}
```

---
