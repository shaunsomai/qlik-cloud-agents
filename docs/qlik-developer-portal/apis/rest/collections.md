# Collections

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Collections provide the framework to catalog various content a user has access to using tags, public and private collections, and favorites.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/collections`](#get-apiv1collections) | Retrieves the collections that the user has access to. This endpoint does not return the user's favorites collection, which can be retrieved with `/v1/collections/favorites`. |
| `POST` | [`/api/v1/collections`](#post-apiv1collections) | Creates and returns a new collection. Collections of type `public` (shown as tags in the user interface) must have unique names. Other collection types can reuse names. |
| `GET` | [`/api/v1/collections/{collectionId}`](#get-apiv1collectionscollectionid) | Finds and returns a collection. |
| `PATCH` | [`/api/v1/collections/{collectionId}`](#patch-apiv1collectionscollectionid) | Updates the name, description, or type fields provided in the patch body. Can be used to publish a `private` collection as a `publicgoverned` collection by patching `/type` with `publicgoverned` once the collection contains at least 1 item. Can also be used to return a `publicgoverned` collection to `private`. Cannot be used to change between `public` (tag) and `private / publicgoverned` (collection). |
| `PUT` | [`/api/v1/collections/{collectionId}`](#put-apiv1collectionscollectionid) | Updates a collection's name and description and returns the updated collection. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value. |
| `DELETE` | [`/api/v1/collections/{collectionId}`](#delete-apiv1collectionscollectionid) | Deletes a collection and removes all items from the collection. |
| `GET` | [`/api/v1/collections/{collectionId}/items`](#get-apiv1collectionscollectioniditems) | Retrieves items from a collection that the user has access to. |
| `POST` | [`/api/v1/collections/{collectionId}/items`](#post-apiv1collectionscollectioniditems) | Adds an item to a collection and returns the item. |
| `GET` | [`/api/v1/collections/{collectionId}/items/{itemId}`](#get-apiv1collectionscollectioniditemsitemid) | Finds and returns an item in a specific collection. See GET `/items/{id}`. |
| `DELETE` | [`/api/v1/collections/{collectionId}/items/{itemId}`](#delete-apiv1collectionscollectioniditemsitemid) | Removes an item from a collection. |
| `GET` | [`/api/v1/collections/favorites`](#get-apiv1collectionsfavorites) | Lists the user's favorites collection. |

## API Reference

### GET /api/v1/collections

Retrieves the collections that the user has access to. This endpoint does not return the user's favorites collection, which can be retrieved with `/v1/collections/favorites`.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `creatorId` | string | No | The case-sensitive string used to search for a resource by creatorId. |
| `id` | string | No | The collection's unique identifier. |
| `includeItems` | string | No | Includes the list of items belonging to the collections. Supported parameters are 'limit', 'sort' and 'resourceType'. Supported formats are json formatted string or deep object style using square brackets. |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `name` | string | No | The case-sensitive string used to search for a collection by name. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `query` | string | No | The case-insensitive string used to search for a resource by name or description. |
| `sort` | string | No | The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or - to indicate ascending or descending sort order respectively.  Enum: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt" |
| `type` | string | No | The case-sensitive string used to filter for a collection by type. Retrieve private collections with `private`, public collections with `publicgoverned`, and tags with `public`.  Enum: "private", "public", "publicgoverned" |
| `types` | string[] | No | A comma-separated case-sensitive string used to filter by multiple types. Enum: "private", "public", "publicgoverned" |

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
// qlik-api has not implemented support for `GET /api/v1/collections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections',
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
# qlik-cli has not implemented support for GET /api/v1/collections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections" \
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

### POST /api/v1/collections

Creates and returns a new collection. Collections of type `public` (shown as tags in the user interface) must have unique names. Other collection types can reuse names.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | For `public` collections (tags), if name already exists in the tenant as a `public` collection, this call will fail with a `409` response. |
| `type` | string | Yes | Enum: "private", "public", "publicgoverned" |
| `description` | string | No |  |

#### Responses

##### 201

Created response.

**Content-Type:** `application/json`

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `items`</summary>

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
// qlik-api has not implemented support for `POST /api/v1/collections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      type: 'private',
      description: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/collections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","type":"private","description":"string"}'
```

**Example Response:**

```json
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
```

---

### GET /api/v1/collections/{collectionId}

Finds and returns a collection.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `items`</summary>

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
// qlik-api has not implemented support for `GET /api/v1/collections/{collectionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}',
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
# qlik-cli has not implemented support for GET /api/v1/collections/{collectionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
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
```

---

### PATCH /api/v1/collections/{collectionId}

Updates the name, description, or type fields provided in the patch body. Can be used to publish a `private` collection as a `publicgoverned` collection by patching `/type` with `publicgoverned` once the collection contains at least 1 item. Can also be used to return a `publicgoverned` collection to `private`. Cannot be used to change between `public` (tag) and `private / publicgoverned` (collection).

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | Field of collection to be patched. Enum: "/name", "/description", "/type" |
| `value` | string | Yes | The value to be used within the operations. - name: The name of the collection. Must not be "". - description: The description of the collection. Empty string "" is allowed. - type: The type of the collection. Via this path the collection type can be toggled between "private" and "publicgoverned". |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `items`</summary>

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
// qlik-api has not implemented support for `PATCH /api/v1/collections/{collectionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/collections/{collectionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"string"}]'
```

**Example Response:**

```json
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
```

---

### PUT /api/v1/collections/{collectionId}

Updates a collection's name and description and returns the updated collection. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `description` | string | No |  |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `items`</summary>

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
// qlik-api has not implemented support for `PUT /api/v1/collections/{collectionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      description: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/collections/{collectionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","description":"string"}'
```

**Example Response:**

```json
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
```

---

### DELETE /api/v1/collections/{collectionId}

Deletes a collection and removes all items from the collection.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |

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
// qlik-api has not implemented support for `DELETE /api/v1/collections/{collectionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/collections/{collectionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/collections/{collectionId}/items

Retrieves items from a collection that the user has access to.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. (This query also supports 'favorites' as the collectionID). |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `name` | string | No | The case-insensitive string used to search for a resource by name. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `query` | string | No | The case-insensitive string used to search for a resource by name or description. |
| `resourceId` | string | No | The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceLink` | string | No | The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both. |
| `resourceType` | string | No | The case-sensitive string used to search for an item by resourceType. Enum: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page" |
| `sort` | string | No | The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively. Enum: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt" |
| `spaceId` | string | No | The space's unique identifier (supports \'personal\' as spaceId). |
| `shared` | boolean | No | _(deprecated)_ Whether or not to return items in a shared space. |
| `noActions` | boolean | No | If set to true, the user's available actions for each item will not be evaluated meaning the actions-array will be omitted from the response (reduces response time). |

#### Responses

##### 200

OK response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An item. |

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
// qlik-api has not implemented support for `GET /api/v1/collections/{collectionId}/items` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}/items',
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
# qlik-cli has not implemented support for GET /api/v1/collections/{collectionId}/items yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}/items" \
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
  ]
}
```

---

### POST /api/v1/collections/{collectionId}/items

Adds an item to a collection and returns the item.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The item's unique identifier. |

#### Responses

##### 201

Created response.

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
// qlik-api has not implemented support for `POST /api/v1/collections/{collectionId}/items` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}/items',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ id: 'string' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/collections/{collectionId}/items yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}/items" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string"}'
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

### GET /api/v1/collections/{collectionId}/items/{itemId}

Finds and returns an item in a specific collection. See GET `/items/{id}`.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |
| `itemId` | string | Yes | The item's unique identifier. |

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
// qlik-api has not implemented support for `GET /api/v1/collections/{collectionId}/items/{itemId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}/items/{itemId}',
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
# qlik-cli has not implemented support for GET /api/v1/collections/{collectionId}/items/{itemId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}/items/{itemId}" \
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

### DELETE /api/v1/collections/{collectionId}/items/{itemId}

Removes an item from a collection.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collectionId` | string | Yes | The collection's unique identifier. |
| `itemId` | string | Yes | The item's unique identifier. |

#### Responses

##### 204

No Content response.

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
// qlik-api has not implemented support for `DELETE /api/v1/collections/{collectionId}/items/{itemId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/{collectionId}/items/{itemId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/collections/{collectionId}/items/{itemId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/{collectionId}/items/{itemId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/collections/favorites

Lists the user's favorites collection.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 302

Found response.

**Content-Type:** `application/json`


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
// qlik-api has not implemented support for `GET /api/v1/collections/favorites` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/collections/favorites',
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
# qlik-cli has not implemented support for GET /api/v1/collections/favorites yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/collections/favorites" \
-H "Authorization: Bearer <access_token>"
```

---
