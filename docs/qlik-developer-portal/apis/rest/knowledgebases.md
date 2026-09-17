# Knowledgebases

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Knowledgebases are collections of individual data sources, that are indexed for use in generating responses to user questions via Assistants for Qlik Answers.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/knowledgebases`](#get-apiv1knowledgebases) | Returns a list of all knowledgebases the user has access to. |
| `POST` | [`/api/v1/knowledgebases`](#post-apiv1knowledgebases) | Creates a new knowledgebase. |
| `GET` | [`/api/v1/knowledgebases/{id}`](#get-apiv1knowledgebasesid) | Retrieves a specific knowledgebase. |
| `PATCH` | [`/api/v1/knowledgebases/{id}`](#patch-apiv1knowledgebasesid) | Updates properties of a specific knowledgebase. |
| `DELETE` | [`/api/v1/knowledgebases/{id}`](#delete-apiv1knowledgebasesid) | Deletes a knowledgebase and all of its resources. |
| `POST` | [`/api/v1/knowledgebases/{id}/actions/search`](#post-apiv1knowledgebasesidactionssearch) | Execute search with either `SIMPLE` or `FULL` mode. SIMPLE does semantic search while FULL will also do reranking and include keyword based chunks. Use topN to control number of chunks in response, max limit is 50. Default to 5. |
| `POST` | [`/api/v1/knowledgebases/{id}/datasources`](#post-apiv1knowledgebasesiddatasources) | Adds a datasource to a knowledgebase. |
| `PUT` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}`](#put-apiv1knowledgebasesiddatasourcesdatasourceid) | Updates a specified datasource. |
| `DELETE` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}`](#delete-apiv1knowledgebasesiddatasourcesdatasourceid) | Deletes a specified datasource and all its resources. |
| `POST` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel`](#post-apiv1knowledgebasesiddatasourcesdatasourceidactionscancel) | Cancels ongoing sync for a specified datasource. |
| `POST` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download`](#post-apiv1knowledgebasesiddatasourcesdatasourceidactionsdownload) | Downloads a specified reference. |
| `POST` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync`](#post-apiv1knowledgebasesiddatasourcesdatasourceidactionssync) | Starts syncing a specified datasource to a specified knowledgebase index. |
| `GET` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories`](#get-apiv1knowledgebasesiddatasourcesdatasourceidhistories) | Retrieves sync history for a specified datasource in a knowledgebase. Returns a `404` if there is no sync history, or if the calling user doesn't have access to the datasource. |
| `GET` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId}`](#get-apiv1knowledgebasesiddatasourcesdatasourceidhistoriessyncid) | Retrieves detailed sync history for a specified datasource. |
| `GET` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules`](#get-apiv1knowledgebasesiddatasourcesdatasourceidschedules) | Returns a datasource schedule. |
| `POST` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules`](#post-apiv1knowledgebasesiddatasourcesdatasourceidschedules) | Creates or updates a specified datasource schedule. |
| `DELETE` | [`/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules`](#delete-apiv1knowledgebasesiddatasourcesdatasourceidschedules) | Deletes a datasource schedule. |
| `GET` | [`/api/v1/knowledgebases/{id}/histories`](#get-apiv1knowledgebasesidhistories) | Retrieves sync history for the specified knowledgebase. Will return a `404` if no sync history exists, or if the calling user does not have access to synced datasources. |

## API Reference

### GET /api/v1/knowledgebases

Returns a list of all knowledgebases the user has access to.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of knowledgebases to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, eg. name. Can be prefixed with - to set descending order, defaults to ascending. Enum: "NAME", "-NAME", "DESCRIPTION", "-DESCRIPTION", "CREATED", "-CREATED", "UPDATED", "-UPDATED" |
| `countTotal` | boolean | No | _(deprecated)_ Optional parameter to request total count for query |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the knowledgebase |
| `name` | string | Yes | Name of the knowledgebase |
| `tags` | string[] | Yes | List of tags associated with the knowledgebase. |
| `ownerId` | string | Yes | The unique identifier of the knowledgebase owner |
| `spaceId` | string | Yes | The unique identifier of the space containing the knowledgebase |
| `tenantId` | string | No | Unique identifier of the tenant |
| `createdAt` | string | Yes | Datetime when the knowledgebase was created |
| `createdBy` | string | Yes | Unique identifier of the user who created the knowledgebase |
| `updatedAt` | string | Yes | Datetime when the knowledgebase was updated |
| `updatedBy` | string | Yes | The unique identifier of the user who last updated the knowledgebase |
| `description` | string | Yes | Description of the knowledgebase |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed |
| `contentSummary` | object | Yes |  |
| `advancedIndexing` | boolean | No | User opt in to advanced parsing and chunking pipeline. Default is false, which will run legacy parsing and chunking. |
| `selectedErrorsCount` | integer | No | Number of selected errors to store in the case of any failed datasources. |

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

</details>

</details>

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "name": "Organization wide knowledgebase",
      "tags": [
        "Red",
        "Sales"
      ],
      "ownerId": "507f191e810c19729de860ea",
      "spaceId": "507f191e810c19729de860ea",
      "tenantId": "507f191e810c19729de860ea",
      "createdAt": "2021-10-02T14:20:50.52Z",
      "createdBy": "507f191e810c19729de860ea",
      "updatedAt": "2021-10-02T14:20:50.52Z",
      "updatedBy": "507f191e810c19729de860ea",
      "description": "This knowledgebase is used for...",
      "lastIndexedAt": "2021-10-02T14:20:50.52Z",
      "contentSummary": {
        "fileSize": 42,
        "textSize": 42,
        "fileCount": 42,
        "effectivePages": 42
      },
      "advancedIndexing": true,
      "selectedErrorsCount": 10
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

### POST /api/v1/knowledgebases

Creates a new knowledgebase.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the knowledgebase |
| `tags` | string[] | No | List of tags for knowledgebase |
| `spaceId` | string | Yes | Unique identifier of the space to contain the knowledgebase |
| `description` | string | No | Description of the knowledgebase |
| `advancedIndexing` | boolean | No | User opt in to advanced parsing and chunking pipeline. Default is false, which will run legacy parsing and chunking. |
| `selectedErrorsCount` | integer | No | Number of selected errors to store in the case of any failed datasources. Optional value with a default of 10. |

#### Responses

##### 201

Successfully created a new knowledgebase.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the knowledgebase |
| `name` | string | Yes | Name of the knowledgebase |
| `tags` | string[] | Yes | List of tags associated with the knowledgebase. |
| `ownerId` | string | Yes | The unique identifier of the knowledgebase owner |
| `spaceId` | string | Yes | The unique identifier of the space containing the knowledgebase |
| `tenantId` | string | No | Unique identifier of the tenant |
| `createdAt` | string | Yes | Datetime when the knowledgebase was created |
| `createdBy` | string | Yes | Unique identifier of the user who created the knowledgebase |
| `updatedAt` | string | Yes | Datetime when the knowledgebase was updated |
| `updatedBy` | string | Yes | The unique identifier of the user who last updated the knowledgebase |
| `description` | string | Yes | Description of the knowledgebase |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed |
| `contentSummary` | object | Yes |  |
| `advancedIndexing` | boolean | No | User opt in to advanced parsing and chunking pipeline. Default is false, which will run legacy parsing and chunking. |
| `selectedErrorsCount` | integer | No | Number of selected errors to store in the case of any failed datasources. |

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Organization wide knowledgebase',
      tags: ['Red', 'Sales'],
      spaceId: '507f191e810c19729de860ea',
      description:
        'This knowledgebase is used for...',
      advancedIndexing: true,
      selectedErrorsCount: 10,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Organization wide knowledgebase","tags":["Red","Sales"],"spaceId":"507f191e810c19729de860ea","description":"This knowledgebase is used for...","advancedIndexing":true,"selectedErrorsCount":10}'
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "name": "Organization wide knowledgebase",
  "tags": [
    "Red",
    "Sales"
  ],
  "ownerId": "507f191e810c19729de860ea",
  "spaceId": "507f191e810c19729de860ea",
  "tenantId": "507f191e810c19729de860ea",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "createdBy": "507f191e810c19729de860ea",
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "updatedBy": "507f191e810c19729de860ea",
  "description": "This knowledgebase is used for...",
  "lastIndexedAt": "2021-10-02T14:20:50.52Z",
  "contentSummary": {
    "fileSize": 42,
    "textSize": 42,
    "fileCount": 42,
    "effectivePages": 42
  },
  "advancedIndexing": true,
  "selectedErrorsCount": 10
}
```

---

### GET /api/v1/knowledgebases/{id}

Retrieves a specific knowledgebase.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the knowledgebase to retrieve. |

#### Responses

##### 200

Successfully retrieved the knowledgebase.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the knowledgebase |
| `name` | string | Yes | Name of the knowledgebase |
| `tags` | string[] | Yes | List of tags associated with the knowledgebase. |
| `ownerId` | string | Yes | The unique identifier of the knowledgebase owner |
| `spaceId` | string | Yes | The unique identifier of the space containing the knowledgebase |
| `tenantId` | string | No | Unique identifier of the tenant |
| `createdAt` | string | Yes | Datetime when the knowledgebase was created |
| `createdBy` | string | Yes | Unique identifier of the user who created the knowledgebase |
| `updatedAt` | string | Yes | Datetime when the knowledgebase was updated |
| `updatedBy` | string | Yes | The unique identifier of the user who last updated the knowledgebase |
| `description` | string | Yes | Description of the knowledgebase |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed |
| `contentSummary` | object | Yes |  |
| `advancedIndexing` | boolean | No | User opt in to advanced parsing and chunking pipeline. Default is false, which will run legacy parsing and chunking. |
| `selectedErrorsCount` | integer | No | Number of selected errors to store in the case of any failed datasources. |
| `datasources` | object[] | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

</details>

<details>
<summary>Properties of `datasources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the datasource |
| `name` | string | No | Name of the datasource |
| `type` | string | Yes | Enum: "file", "web", "database" |
| `spaceId` | string | No | The unique identifier of the space containing the datasource |
| `chunking` | object | No |  |
| `syncInfo` | object | No |  |
| `fileConfig` | object | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |
| `sourceCount` | integer | No | The number of times that a datasource was referenced as a source in an answer |
| `contentSummary` | object | Yes |  |

<details>
<summary>Properties of `chunking`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | Yes | Size of chunks |
| `type` | string | Yes | Chunking strategy |
| `overlap` | integer | Yes | Chunk overlap, should be less than size |
| `separators` | string[] | Yes | List of separators to chunk by |
| `keepSeparator` | boolean | Yes | Allows to keep or remove separators used |

</details>

<details>
<summary>Properties of `syncInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Sync status Enum: "neverIndexed", "progress", "completed", "completedWithError", "toAdd", "toDelete" |
| `startedAt` | string | Yes | Datetime when the sync task was started |
| `lastSyncId` | string | No | sync Id |
| `completedAt` | string | Yes | Datetime when the sync task was completed |

</details>

<details>
<summary>Properties of `fileConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `files` | string[] | No |  |
| `scope` | object | No | Scope for the file crawler. |
| `folder` | string | No | Root folder for traversing. |
| `userId` | string | Yes | userId of the owner of the datasource fileConfig |
| `connectionId` | string | Yes | connection id to be used to retrieve the raw data |
| `crawlPatterns` | object[] | No | Pattern matching links to crawl |

<details>
<summary>Properties of `scope`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `crawlPatterns`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

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

</details>

##### 403

The operation failed due to insufficient permissions.

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

</details>

##### 404

The knowledgebase is not found

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "name": "Organization wide knowledgebase",
  "tags": [
    "Red",
    "Sales"
  ],
  "ownerId": "507f191e810c19729de860ea",
  "spaceId": "507f191e810c19729de860ea",
  "tenantId": "507f191e810c19729de860ea",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "createdBy": "507f191e810c19729de860ea",
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "updatedBy": "507f191e810c19729de860ea",
  "description": "This knowledgebase is used for...",
  "lastIndexedAt": "2021-10-02T14:20:50.52Z",
  "contentSummary": {
    "fileSize": 42,
    "textSize": 42,
    "fileCount": 42,
    "effectivePages": 42
  },
  "advancedIndexing": true,
  "selectedErrorsCount": 10,
  "datasources": [
    {
      "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "name": "string",
      "type": "file",
      "spaceId": "507f191e810c19729de860ea",
      "chunking": {
        "size": 1024,
        "type": "recursive",
        "overlap": 20,
        "separators": [
          "\n",
          ".",
          " "
        ],
        "keepSeparator": false
      },
      "syncInfo": {
        "status": "neverIndexed",
        "startedAt": "2021-10-02T14:20:50.52Z",
        "lastSyncId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
        "completedAt": "2021-10-02T14:20:50.52Z"
      },
      "fileConfig": {
        "files": [
          "string"
        ],
        "scope": {
          "depth": 1,
          "maxSize": 1000000,
          "extensions": [
            "pdf"
          ],
          "maxFilesTotal": 50,
          "modifiedAfter": "2021-10-02T14:20:50.52Z",
          "maxFilesPerFolder": 100
        },
        "folder": "folderA/folderB",
        "userId": "507f191e810c19729de860ea",
        "connectionId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
        "crawlPatterns": [
          {
            "type": "include",
            "pattern": "(.*)example(.*)"
          }
        ]
      },
      "sourceCount": 10,
      "contentSummary": {
        "fileSize": 42,
        "textSize": 42,
        "fileCount": 42,
        "effectivePages": 42
      }
    }
  ]
}
```

---

### PATCH /api/v1/knowledgebases/{id}

Updates properties of a specific knowledgebase.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The knowledgebase id. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `if-match` | string | No | Optional header to do conditional updates. Using the Etag value that was returned the last time the knowledgebase was fetched. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "REPLACE" |
| `path` | string | Yes | A JSON Pointer. |
| `value` | string \| number \| boolean | Yes | The value to be used for this operation. |

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
| `` | number | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

</details>

#### Responses

##### 204

Knowledgebase updated successfully.

##### 400

Bad request. Payload could not be parsed to a JSON Patch or Patch operations are invalid.

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

</details>

##### 401

Not authorized.

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

</details>

##### 403

The operation failed due to insufficient permissions.

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

</details>

##### 404

The term to patch was not found.

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

</details>

##### 429

Request has been rate limited.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/knowledgebases/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'new name',
      },
      {
        op: 'replace',
        path: '/description',
        value: 'new description',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/knowledgebases/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"new name"},{"op":"replace","path":"/description","value":"new description"}]'
```

---

### DELETE /api/v1/knowledgebases/{id}

Deletes a knowledgebase and all of its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the knowledgebase to delete. |

#### Responses

##### 204

Successful Operation.

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

</details>

##### 403

The operation failed due to insufficient permissions.

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

</details>

##### 404

The knowledgebase is not found

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/knowledgebases/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/knowledgebases/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/knowledgebases/{id}/actions/search

Execute search with either `SIMPLE` or `FULL` mode. SIMPLE does semantic search while FULL will also do reranking and include keyword based chunks. Use topN to control number of chunks in response, max limit is 50. Default to 5.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the knowledgebase |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `topN` | integer | No | Number of chunks to return in results. |
| `prompt` | string | Yes | Query text or question to search. |
| `searchMode` | string | No | Search mode to use.   Allowed values: `SIMPLE` and `FULL`.   Default: `SIMPLE`.  Enum: "SIMPLE", "FULL" |

#### Responses

##### 200

Chunks retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | Retrieved document chunks |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | Yes | Text content of the chunk |
| `chunkMeta` | object | Yes | Metadata about the chunk |
| `tfidfScore` | number | No | Score from keyword search |
| `searchSource` | string | No | search method for the chunk, e.g. `semantic search`, `keyword search` or `semantic and keyword search` |
| `semanticScore` | number | No | Similarity score from embedding match |

<details>
<summary>Properties of `chunkMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | Yes | source of chunk |
| `chunkId` | string | Yes | chunkId |
| `documentId` | string | Yes | documentId of chunk |
| `datasourceId` | string | Yes | datasourceId of chunk |
| `knowledgeBaseId` | string | Yes | knowledgeBaseId of chunk |

</details>

</details>

##### 400

The request is in incorrect format

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The user does not have privileges to perform the requested action.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Knowledgebase is not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 405

Method is not allowed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Prompt processing error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/actions/search` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/actions/search',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      topN: 20,
      prompt: 'What is LLM?',
      searchMode: 'SIMPLE',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/actions/search yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/actions/search" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"topN":20,"prompt":"What is LLM?","searchMode":"SIMPLE"}'
```

**Example Response:**

```json
{
  "chunks": [
    {
      "text": "LLM stands for Large Language Model",
      "chunkMeta": {
        "source": "string",
        "chunkId": "string",
        "documentId": "string",
        "datasourceId": "string",
        "knowledgeBaseId": "string"
      },
      "tfidfScore": 0.9,
      "searchSource": "string",
      "semanticScore": 0.63
    }
  ]
}
```

---

### POST /api/v1/knowledgebases/{id}/datasources

Adds a datasource to a knowledgebase.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the knowledgebase. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the datasource |
| `type` | string | Yes | Enum: "file", "web", "database" |
| `fileConfig` | object | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |

<details>
<summary>Properties of `fileConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `files` | string[] | No |  |
| `scope` | object | No | Scope for the file crawler. |
| `folder` | string | No | Root folder for traversing. |
| `userId` | string | Yes | userId of the owner of the datasource fileConfig |
| `connectionId` | string | Yes | connection id to be used to retrieve the raw data |
| `crawlPatterns` | object[] | No | Pattern matching links to crawl |

<details>
<summary>Properties of `scope`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `depth` | integer | Yes | The number of levels of sub folders that should be considered |
| `maxSize` | integer | No | Optional parameter. Max size of downloaded files in bytes |
| `extensions` | string[] | No | list of file extensions to be considered |
| `maxFilesTotal` | integer | No | Total number of files that should be considered |
| `modifiedAfter` | string | No | only files modified after this time should be indexed. If set older files will be removed from index. |
| `maxFilesPerFolder` | integer | No | Maximum number of files per folder that should be considered |

</details>

<details>
<summary>Properties of `crawlPatterns`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | include or exclude Enum: "include", "exclude" |
| `pattern` | string | Yes | Regex patterna to filter links on |

</details>

</details>

#### Responses

##### 201

Successfully added a datasource to the knowledgebase.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the datasource |
| `name` | string | No | Name of the datasource |
| `type` | string | Yes | Enum: "file", "web", "database" |
| `spaceId` | string | No | The unique identifier of the space containing the datasource |
| `chunking` | object | No |  |
| `syncInfo` | object | No |  |
| `fileConfig` | object | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |
| `sourceCount` | integer | No | The number of times that a datasource was referenced as a source in an answer |
| `contentSummary` | object | Yes |  |

<details>
<summary>Properties of `chunking`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | Yes | Size of chunks |
| `type` | string | Yes | Chunking strategy |
| `overlap` | integer | Yes | Chunk overlap, should be less than size |
| `separators` | string[] | Yes | List of separators to chunk by |
| `keepSeparator` | boolean | Yes | Allows to keep or remove separators used |

</details>

<details>
<summary>Properties of `syncInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Sync status Enum: "neverIndexed", "progress", "completed", "completedWithError", "toAdd", "toDelete" |
| `startedAt` | string | Yes | Datetime when the sync task was started |
| `lastSyncId` | string | No | sync Id |
| `completedAt` | string | Yes | Datetime when the sync task was completed |

</details>

<details>
<summary>Properties of `fileConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `files` | string[] | No |  |
| `scope` | object | No | Scope for the file crawler. |
| `folder` | string | No | Root folder for traversing. |
| `userId` | string | Yes | userId of the owner of the datasource fileConfig |
| `connectionId` | string | Yes | connection id to be used to retrieve the raw data |
| `crawlPatterns` | object[] | No | Pattern matching links to crawl |

<details>
<summary>Properties of `scope`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `depth` | integer | Yes | The number of levels of sub folders that should be considered |
| `maxSize` | integer | No | Optional parameter. Max size of downloaded files in bytes |
| `extensions` | string[] | No | list of file extensions to be considered |
| `maxFilesTotal` | integer | No | Total number of files that should be considered |
| `modifiedAfter` | string | No | only files modified after this time should be indexed. If set older files will be removed from index. |
| `maxFilesPerFolder` | integer | No | Maximum number of files per folder that should be considered |

</details>

<details>
<summary>Properties of `crawlPatterns`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | include or exclude Enum: "include", "exclude" |
| `pattern` | string | Yes | Regex patterna to filter links on |

</details>

</details>

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The knowledgebase is not found.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/datasources` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      type: 'file',
      fileConfig: {
        files: ['string'],
        scope: {
          depth: 1,
          maxSize: 1000000,
          extensions: ['pdf'],
          maxFilesTotal: 50,
          modifiedAfter:
            '2021-10-02T14:20:50.52Z',
          maxFilesPerFolder: 100,
        },
        folder: 'folderA/folderB',
        userId: '507f191e810c19729de860ea',
        connectionId:
          'f256b3e4-03e0-4f74-ae46-a4d43882ee5d',
        crawlPatterns: [
          {
            type: 'include',
            pattern: '(.*)example(.*)',
          },
        ],
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/datasources yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","type":"file","fileConfig":{"files":["string"],"scope":{"depth":1,"maxSize":1000000,"extensions":["pdf"],"maxFilesTotal":50,"modifiedAfter":"2021-10-02T14:20:50.52Z","maxFilesPerFolder":100},"folder":"folderA/folderB","userId":"507f191e810c19729de860ea","connectionId":"f256b3e4-03e0-4f74-ae46-a4d43882ee5d","crawlPatterns":[{"type":"include","pattern":"(.*)example(.*)"}]}}'
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "name": "string",
  "type": "file",
  "spaceId": "507f191e810c19729de860ea",
  "chunking": {
    "size": 1024,
    "type": "recursive",
    "overlap": 20,
    "separators": [
      "\n",
      ".",
      " "
    ],
    "keepSeparator": false
  },
  "syncInfo": {
    "status": "neverIndexed",
    "startedAt": "2021-10-02T14:20:50.52Z",
    "lastSyncId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
    "completedAt": "2021-10-02T14:20:50.52Z"
  },
  "fileConfig": {
    "files": [
      "string"
    ],
    "scope": {
      "depth": 1,
      "maxSize": 1000000,
      "extensions": [
        "pdf"
      ],
      "maxFilesTotal": 50,
      "modifiedAfter": "2021-10-02T14:20:50.52Z",
      "maxFilesPerFolder": 100
    },
    "folder": "folderA/folderB",
    "userId": "507f191e810c19729de860ea",
    "connectionId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
    "crawlPatterns": [
      {
        "type": "include",
        "pattern": "(.*)example(.*)"
      }
    ]
  },
  "sourceCount": 10,
  "contentSummary": {
    "fileSize": 42,
    "textSize": 42,
    "fileCount": 42,
    "effectivePages": 42
  }
}
```

---

### PUT /api/v1/knowledgebases/{id}/datasources/{datasourceId}

Updates a specified datasource.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource to update. |
| `id` | string | Yes | The id of a knowledgebase. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the datasource |
| `name` | string | No | Name of the datasource |
| `type` | string | Yes | Enum: "file", "web", "database" |
| `spaceId` | string | No | The unique identifier of the space containing the datasource |
| `chunking` | object | No |  |
| `syncInfo` | object | No |  |
| `fileConfig` | object | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |
| `sourceCount` | integer | No | The number of times that a datasource was referenced as a source in an answer |
| `contentSummary` | object | Yes |  |

<details>
<summary>Properties of `chunking`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | Yes | Size of chunks |
| `type` | string | Yes | Chunking strategy |
| `overlap` | integer | Yes | Chunk overlap, should be less than size |
| `separators` | string[] | Yes | List of separators to chunk by |
| `keepSeparator` | boolean | Yes | Allows to keep or remove separators used |

</details>

<details>
<summary>Properties of `syncInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lastSyncId` | string | No | sync Id |

</details>

<details>
<summary>Properties of `fileConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `files` | string[] | No |  |
| `scope` | object | No | Scope for the file crawler. |
| `folder` | string | No | Root folder for traversing. |
| `userId` | string | Yes | userId of the owner of the datasource fileConfig |
| `connectionId` | string | Yes | connection id to be used to retrieve the raw data |
| `crawlPatterns` | object[] | No | Pattern matching links to crawl |

<details>
<summary>Properties of `scope`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `depth` | integer | Yes | The number of levels of sub folders that should be considered |
| `maxSize` | integer | No | Optional parameter. Max size of downloaded files in bytes |
| `extensions` | string[] | No | list of file extensions to be considered |
| `maxFilesTotal` | integer | No | Total number of files that should be considered |
| `modifiedAfter` | string | No | only files modified after this time should be indexed. If set older files will be removed from index. |
| `maxFilesPerFolder` | integer | No | Maximum number of files per folder that should be considered |

</details>

<details>
<summary>Properties of `crawlPatterns`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | include or exclude Enum: "include", "exclude" |
| `pattern` | string | Yes | Regex patterna to filter links on |

</details>

</details>

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

</details>

#### Responses

##### 200

Successfully updated the datasource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the datasource |
| `name` | string | No | Name of the datasource |
| `type` | string | Yes | Enum: "file", "web", "database" |
| `spaceId` | string | No | The unique identifier of the space containing the datasource |
| `chunking` | object | No |  |
| `syncInfo` | object | No |  |
| `fileConfig` | object | No | Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided. |
| `sourceCount` | integer | No | The number of times that a datasource was referenced as a source in an answer |
| `contentSummary` | object | Yes |  |

<details>
<summary>Properties of `chunking`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | Yes | Size of chunks |
| `type` | string | Yes | Chunking strategy |
| `overlap` | integer | Yes | Chunk overlap, should be less than size |
| `separators` | string[] | Yes | List of separators to chunk by |
| `keepSeparator` | boolean | Yes | Allows to keep or remove separators used |

</details>

<details>
<summary>Properties of `syncInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Sync status Enum: "neverIndexed", "progress", "completed", "completedWithError", "toAdd", "toDelete" |
| `startedAt` | string | Yes | Datetime when the sync task was started |
| `lastSyncId` | string | No | sync Id |
| `completedAt` | string | Yes | Datetime when the sync task was completed |

</details>

<details>
<summary>Properties of `fileConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `files` | string[] | No |  |
| `scope` | object | No | Scope for the file crawler. |
| `folder` | string | No | Root folder for traversing. |
| `userId` | string | Yes | userId of the owner of the datasource fileConfig |
| `connectionId` | string | Yes | connection id to be used to retrieve the raw data |
| `crawlPatterns` | object[] | No | Pattern matching links to crawl |

<details>
<summary>Properties of `scope`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `depth` | integer | Yes | The number of levels of sub folders that should be considered |
| `maxSize` | integer | No | Optional parameter. Max size of downloaded files in bytes |
| `extensions` | string[] | No | list of file extensions to be considered |
| `maxFilesTotal` | integer | No | Total number of files that should be considered |
| `modifiedAfter` | string | No | only files modified after this time should be indexed. If set older files will be removed from index. |
| `maxFilesPerFolder` | integer | No | Maximum number of files per folder that should be considered |

</details>

<details>
<summary>Properties of `crawlPatterns`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | include or exclude Enum: "include", "exclude" |
| `pattern` | string | Yes | Regex patterna to filter links on |

</details>

</details>

<details>
<summary>Properties of `contentSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileSize` | integer | Yes |  |
| `textSize` | integer | Yes |  |
| `fileCount` | integer | Yes |  |
| `effectivePages` | integer | Yes |  |

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

</details>

##### 403

The operation failed due to insufficient permissions.

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

</details>

##### 404

The record is not found

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/knowledgebases/{id}/datasources/{datasourceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'f256b3e4-03e0-4f74-ae46-a4d43882ee5d',
      name: 'string',
      type: 'file',
      spaceId: '507f191e810c19729de860ea',
      chunking: {
        size: 1024,
        type: 'recursive',
        overlap: 20,
        separators: ['\n', '.', ' '],
        keepSeparator: false,
      },
      syncInfo: {
        lastSyncId:
          'f256b3e4-03e0-4f74-ae46-a4d43882ee5d',
      },
      fileConfig: {
        files: ['string'],
        scope: {
          depth: 1,
          maxSize: 1000000,
          extensions: ['pdf'],
          maxFilesTotal: 50,
          modifiedAfter:
            '2021-10-02T14:20:50.52Z',
          maxFilesPerFolder: 100,
        },
        folder: 'folderA/folderB',
        userId: '507f191e810c19729de860ea',
        connectionId:
          'f256b3e4-03e0-4f74-ae46-a4d43882ee5d',
        crawlPatterns: [
          {
            type: 'include',
            pattern: '(.*)example(.*)',
          },
        ],
      },
      sourceCount: 10,
      contentSummary: {
        fileSize: 42,
        textSize: 42,
        fileCount: 42,
        effectivePages: 42,
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/knowledgebases/{id}/datasources/{datasourceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"f256b3e4-03e0-4f74-ae46-a4d43882ee5d","name":"string","type":"file","spaceId":"507f191e810c19729de860ea","chunking":{"size":1024,"type":"recursive","overlap":20,"separators":["\n","."," "],"keepSeparator":false},"syncInfo":{"lastSyncId":"f256b3e4-03e0-4f74-ae46-a4d43882ee5d"},"fileConfig":{"files":["string"],"scope":{"depth":1,"maxSize":1000000,"extensions":["pdf"],"maxFilesTotal":50,"modifiedAfter":"2021-10-02T14:20:50.52Z","maxFilesPerFolder":100},"folder":"folderA/folderB","userId":"507f191e810c19729de860ea","connectionId":"f256b3e4-03e0-4f74-ae46-a4d43882ee5d","crawlPatterns":[{"type":"include","pattern":"(.*)example(.*)"}]},"sourceCount":10,"contentSummary":{"fileSize":42,"textSize":42,"fileCount":42,"effectivePages":42}}'
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "name": "string",
  "type": "file",
  "spaceId": "507f191e810c19729de860ea",
  "chunking": {
    "size": 1024,
    "type": "recursive",
    "overlap": 20,
    "separators": [
      "\n",
      ".",
      " "
    ],
    "keepSeparator": false
  },
  "syncInfo": {
    "status": "neverIndexed",
    "startedAt": "2021-10-02T14:20:50.52Z",
    "lastSyncId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
    "completedAt": "2021-10-02T14:20:50.52Z"
  },
  "fileConfig": {
    "files": [
      "string"
    ],
    "scope": {
      "depth": 1,
      "maxSize": 1000000,
      "extensions": [
        "pdf"
      ],
      "maxFilesTotal": 50,
      "modifiedAfter": "2021-10-02T14:20:50.52Z",
      "maxFilesPerFolder": 100
    },
    "folder": "folderA/folderB",
    "userId": "507f191e810c19729de860ea",
    "connectionId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
    "crawlPatterns": [
      {
        "type": "include",
        "pattern": "(.*)example(.*)"
      }
    ]
  },
  "sourceCount": 10,
  "contentSummary": {
    "fileSize": 42,
    "textSize": 42,
    "fileCount": 42,
    "effectivePages": 42
  }
}
```

---

### DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId}

Deletes a specified datasource and all its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource to delete. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |

#### Responses

##### 204

Successful Operation.

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

</details>

##### 403

The operation failed due to insufficient permissions.

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

</details>

##### 404

The knowledgebase is not found

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel

Cancels ongoing sync for a specified datasource.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource to cancel sync for. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |

#### Responses

##### 200

Successfully cancelled sync.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the sync |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d"
}
```

---

### POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download

Downloads a specified reference.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource to download from. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | file path to the file to downlaod. |

#### Responses

##### 200

Download a file from a datasource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | URL to download the file. |
| `name` | string | Yes | The requested file name. |
| `spaceId` | string | Yes | Space id the file belongs in. |
| `fileSize` | integer | Yes | Size of downloaded file. |
| `mimeType` | string | Yes | The mimetype of the file. |
| `lastUpdatedAt` | string | Yes | Date for last time the file was modified. |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      path: 'folder/file.pdf',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/download" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"path":"folder/file.pdf"}'
```

**Example Response:**

```json
{
  "url": "/v1/temp-contents/65f4287d785c400fe6d1e861",
  "name": "stories/content/billy.txt",
  "spaceId": "507f191e810c19729de860ea",
  "fileSize": 542,
  "mimeType": "text/plain",
  "lastUpdatedAt": "2020-04-16T23:17:28Z"
}
```

---

### POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync

Starts syncing a specified datasource to a specified knowledgebase index.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource to sync. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `migrate` | boolean | No | Optional parameter to migrate indexed files to docdetails collection |

#### Responses

##### 202

Successfully started sync.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the sync |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/actions/sync" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d"
}
```

---

### GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories

Retrieves sync history for a specified datasource in a knowledgebase. Returns a `404` if there is no sync history, or if the calling user doesn't have access to the datasource.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of knowledgebases to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, eg. name. Can be prefixed with - to set descending order, defaults to ascending. Enum: "COMPLETED", "-COMPLETED" |

#### Responses

##### 200

List of sync items ordered by the completed time.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | sync id |
| `status` | string | Yes | Sync status Enum: "neverIndexed", "progress", "completed", "completedWithError" |
| `docStats` | object | Yes | Summary of documents processed |
| `startedAt` | string | Yes | Datetime when the sync task was started |
| `completedAt` | string | No | Datetime when the sync task was completed |
| `triggerType` | string | Yes | Datasource trigger type, was it manually or automatically synced |
| `connectionId` | string | Yes | Connection id that the datasource used |
| `datasourceId` | string | Yes | datasource id |
| `errorSummary` | object[] | No | Aggregated, deduplicated view of failures grouped by error code. Lets the UI surface a smart summary (e.g. "1000 files failed to parse") instead of a flat list of raw error strings. |
| `selectedErrors` | string[] | No | populated with up to the first selectedErrorsCount errors if there were any during sync |

<details>
<summary>Properties of `docStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `added` | integer | Yes |  |
| `errors` | integer | Yes |  |
| `deleted` | integer | Yes |  |
| `updated` | integer | Yes |  |
| `deltaBytes` | integer | Yes |  |
| `deltaTextSize` | integer | Yes |  |
| `largestFileSize` | integer | Yes |  |
| `deltaEffectivePages` | integer | Yes |  |
| `totalBytesProcessed` | integer | Yes |  |

</details>

<details>
<summary>Properties of `errorSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Stable, machine-readable error category shared across services and the UI. Enum: "unknown", "file_size_exceeded", "download_failed", "parse_failed", "parse_timeout", "chunk_failed", "chunk_timeout", "guardrail_blocked", "unsupported_file", "index_verification_failed", "file_not_found", "document_has_macros", "scan_failed", "pages_limit_exceeded", "pages_enforcement_failed", "governance_budget_exceeded" |
| `count` | integer | Yes | Number of files that failed with this error code. |
| `sample` | string | No | A representative (sanitized) error message for this category. |
| `sources` | string[] | No | Up to selectedErrorsCount example sources that failed with this code. |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

</details>

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The datasource is not found, the datasource has no sync history (no syncs have been run), or the calling user doesn't have access to this datasource in the knowledgebase.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "status": [
        "neverIndexed | progress | completed | completedWithError"
      ],
      "docStats": {
        "added": 1,
        "errors": 0,
        "deleted": 0,
        "updated": 0,
        "deltaBytes": 0,
        "deltaTextSize": 0,
        "largestFileSize": 123044444,
        "deltaEffectivePages": 0,
        "totalBytesProcessed": 123044444
      },
      "startedAt": "2021-10-02T14:20:50.52Z",
      "completedAt": "2021-10-02T14:20:50.52Z",
      "triggerType": [
        "manual | schedule"
      ],
      "connectionId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "datasourceId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "errorSummary": [
        {
          "code": "string",
          "count": 1000,
          "sample": "failed to parse document",
          "sources": [
            "myfile.pdf"
          ]
        }
      ],
      "selectedErrors": [
        "unsupported file extension"
      ]
    }
  ],
  "meta": {
    "countTotal": 42
  },
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

### GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId} _(deprecated)_

Retrieves detailed sync history for a specified datasource.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource. |
| `id` | string | Yes | The id of the knowledgebase the datasource belongs to. |
| `syncId` | string | Yes | The sync identifier. |

#### Responses

##### 200

List of sync items ordered by the start time.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | document Id |
| `error` | string | No | error if one happened during sync |
| `action` | string | Yes | acion performed Enum: "add", "delete", "update" |
| `chunks` | integer | No | number of chunks |
| `source` | string | Yes | Source of the document |
| `syncId` | string | Yes | sync Id |
| `duration` | object | No |  |
| `fileSize` | integer | No | file size |
| `syncedAt` | string | Yes | Datetime when the sync task was executed |
| `chunkSize` | integer | No | chunk size |
| `errorCode` | string | No | Stable, machine-readable error category for the failure, allowing the UI to map it to a friendly message without brittle string matching. Only populated when the file failed to index. Enum: "unknown", "file_size_exceeded", "download_failed", "parse_failed", "parse_timeout", "chunk_failed", "chunk_timeout", "guardrail_blocked", "unsupported_file", "index_verification_failed", "file_not_found", "document_has_macros", "scan_failed", "pages_limit_exceeded", "pages_enforcement_failed", "governance_budget_exceeded" |
| `explicitPages` | integer | Yes | page count |
| `fileStartedAt` | string | No | Datetime when the file processing started |
| `fileCompletedAt` | string | No | Datetime when the file processing finished |
| `fileLastModified` | string | No | Datetime when the file was last modified |

<details>
<summary>Properties of `duration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunk` | integer | Yes |  |
| `embed` | integer | Yes |  |
| `parse` | integer | Yes |  |
| `store` | integer | Yes |  |
| `download` | integer | Yes |  |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId}',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/histories/{syncId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "error": "unsupported file extension",
  "action": "add",
  "chunks": 10,
  "source": "myfile.pdf",
  "syncId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "duration": {
    "chunk": 0,
    "embed": 996,
    "parse": 0,
    "store": 3653363805,
    "download": 207
  },
  "fileSize": 123044444,
  "syncedAt": "2021-10-02T14:20:50.52Z",
  "chunkSize": 14721,
  "errorCode": "string",
  "explicitPages": 42,
  "fileStartedAt": "2021-10-02T14:20:50.52Z",
  "fileCompletedAt": "2021-10-02T14:21:50.52Z",
  "fileLastModified": "2024-02-16T20:06:02Z"
}
```

---

### GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules

Returns a datasource schedule.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource the schedule belongs to. |
| `id` | string | Yes | The id of the knowledgebase the schedule belongs to. |

#### Responses

##### 200

Successfully created a schedule.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | Yes |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `calendars` | object[] | Yes | An event specification relative to the calendar, similar to a traditional cron specification. |
| `intervals` | object[] | No | For example, an `every` of 1 hour with `offset` of zero would match every hour, on the hour. The same `every` but an `offset` of 19 minutes would match every `xx:19:00`. |
| `datasourceId` | string | No |  |
| `knowledgebaseId` | string | Yes |  |

<details>
<summary>Properties of `calendars`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hour` | object[] | Yes | Hour range to match (0-23). Default matches 0 |
| `year` | object[] | Yes | Year range to match. Default matches all years |
| `month` | object[] | Yes | Month range to match (1-12). Default matches all months |
| `minute` | object[] | Yes | Minute range to match (0-59). Default matches 0 |
| `second` | object[] | Yes | Second range to match (0-59). Default matches 0 |
| `comment` | string | Yes | Description of the intention of this schedule |
| `dayOfWeek` | object[] | Yes | DayOfWeek range to match (0-6; 0 is Sunday). Default matches all days of the week |
| `dayOfMonth` | object[] | Yes | DayOfMonth range to match (1-31). Default matches all days |

<details>
<summary>Properties of `hour`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `year`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `month`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `minute`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `second`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfWeek`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfMonth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

</details>

<details>
<summary>Properties of `intervals`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `every` | string | Yes | The period to repeat the interval |
| `offset` | string | No | A fixed offset added to the intervals period. Optional, defaults to 0 |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "ownerId": "507f191e810c19729de860ed",
  "spaceId": "507f191e810c19729de860ec",
  "tenantId": "507f191e810c19729de860eb",
  "calendars": [
    {
      "hour": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "year": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "month": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "minute": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "second": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "comment": "string",
      "dayOfWeek": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "dayOfMonth": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ]
    }
  ],
  "intervals": [
    {
      "every": "5h30m",
      "offset": "0s"
    }
  ],
  "datasourceId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "knowledgebaseId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d"
}
```

---

### POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules

Creates or updates a specified datasource schedule.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource the schedule belongs to. |
| `id` | string | Yes | The id of the knowledgebase the schedule belongs to. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `calendars` | object[] | No | An event specification relative to the calendar, similar to a traditional cron specification. |
| `intervals` | object[] | No | For example, an `every` of 1 hour with `offset` of zero would match every hour, on the hour. The same `every` but an `offset` of 19 minutes would match every `xx:19:00`. |

<details>
<summary>Properties of `calendars`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hour` | object[] | Yes | Hour range to match (0-23). Default matches 0 |
| `year` | object[] | Yes | Year range to match. Default matches all years |
| `month` | object[] | Yes | Month range to match (1-12). Default matches all months |
| `minute` | object[] | Yes | Minute range to match (0-59). Default matches 0 |
| `second` | object[] | Yes | Second range to match (0-59). Default matches 0 |
| `comment` | string | Yes | Description of the intention of this schedule |
| `dayOfWeek` | object[] | Yes | DayOfWeek range to match (0-6; 0 is Sunday). Default matches all days of the week |
| `dayOfMonth` | object[] | Yes | DayOfMonth range to match (1-31). Default matches all days |

<details>
<summary>Properties of `hour`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `year`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `month`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `minute`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `second`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfWeek`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfMonth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

</details>

<details>
<summary>Properties of `intervals`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `every` | string | Yes | The period to repeat the interval |
| `offset` | string | No | A fixed offset added to the intervals period. Optional, defaults to 0 |

</details>

#### Responses

##### 200

Successfully created a schedule.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | Yes |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `calendars` | object[] | Yes | An event specification relative to the calendar, similar to a traditional cron specification. |
| `intervals` | object[] | No | For example, an `every` of 1 hour with `offset` of zero would match every hour, on the hour. The same `every` but an `offset` of 19 minutes would match every `xx:19:00`. |
| `datasourceId` | string | No |  |
| `knowledgebaseId` | string | Yes |  |

<details>
<summary>Properties of `calendars`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hour` | object[] | Yes | Hour range to match (0-23). Default matches 0 |
| `year` | object[] | Yes | Year range to match. Default matches all years |
| `month` | object[] | Yes | Month range to match (1-12). Default matches all months |
| `minute` | object[] | Yes | Minute range to match (0-59). Default matches 0 |
| `second` | object[] | Yes | Second range to match (0-59). Default matches 0 |
| `comment` | string | Yes | Description of the intention of this schedule |
| `dayOfWeek` | object[] | Yes | DayOfWeek range to match (0-6; 0 is Sunday). Default matches all days of the week |
| `dayOfMonth` | object[] | Yes | DayOfMonth range to match (1-31). Default matches all days |

<details>
<summary>Properties of `hour`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `year`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `month`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `minute`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `second`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfWeek`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfMonth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

</details>

<details>
<summary>Properties of `intervals`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `every` | string | Yes | The period to repeat the interval |
| `offset` | string | No | A fixed offset added to the intervals period. Optional, defaults to 0 |

</details>

##### 201

Successfully created a schedule.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | Yes |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `calendars` | object[] | Yes | An event specification relative to the calendar, similar to a traditional cron specification. |
| `intervals` | object[] | No | For example, an `every` of 1 hour with `offset` of zero would match every hour, on the hour. The same `every` but an `offset` of 19 minutes would match every `xx:19:00`. |
| `datasourceId` | string | No |  |
| `knowledgebaseId` | string | Yes |  |

<details>
<summary>Properties of `calendars`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hour` | object[] | Yes | Hour range to match (0-23). Default matches 0 |
| `year` | object[] | Yes | Year range to match. Default matches all years |
| `month` | object[] | Yes | Month range to match (1-12). Default matches all months |
| `minute` | object[] | Yes | Minute range to match (0-59). Default matches 0 |
| `second` | object[] | Yes | Second range to match (0-59). Default matches 0 |
| `comment` | string | Yes | Description of the intention of this schedule |
| `dayOfWeek` | object[] | Yes | DayOfWeek range to match (0-6; 0 is Sunday). Default matches all days of the week |
| `dayOfMonth` | object[] | Yes | DayOfMonth range to match (1-31). Default matches all days |

<details>
<summary>Properties of `hour`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `year`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `month`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `minute`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `second`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfWeek`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

<details>
<summary>Properties of `dayOfMonth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | integer | No | End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start |
| `step` | integer | No | Step to be take between each value. Optional, defaulted to 1 |
| `start` | integer | Yes | Start of the range (inclusive) |

</details>

</details>

<details>
<summary>Properties of `intervals`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `every` | string | Yes | The period to repeat the interval |
| `offset` | string | No | A fixed offset added to the intervals period. Optional, defaults to 0 |

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      calendars: [
        {
          hour: [{ end: 42, step: 1, start: 42 }],
          year: [{ end: 42, step: 1, start: 42 }],
          month: [
            { end: 42, step: 1, start: 42 },
          ],
          minute: [
            { end: 42, step: 1, start: 42 },
          ],
          second: [
            { end: 42, step: 1, start: 42 },
          ],
          comment: 'string',
          dayOfWeek: [
            { end: 42, step: 1, start: 42 },
          ],
          dayOfMonth: [
            { end: 42, step: 1, start: 42 },
          ],
        },
      ],
      intervals: [
        { every: '5h30m', offset: '0s' },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"calendars":[{"hour":[{"end":42,"step":1,"start":42}],"year":[{"end":42,"step":1,"start":42}],"month":[{"end":42,"step":1,"start":42}],"minute":[{"end":42,"step":1,"start":42}],"second":[{"end":42,"step":1,"start":42}],"comment":"string","dayOfWeek":[{"end":42,"step":1,"start":42}],"dayOfMonth":[{"end":42,"step":1,"start":42}]}],"intervals":[{"every":"5h30m","offset":"0s"}]}'
```

**Example Response:**

```json
{
  "ownerId": "507f191e810c19729de860ed",
  "spaceId": "507f191e810c19729de860ec",
  "tenantId": "507f191e810c19729de860eb",
  "calendars": [
    {
      "hour": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "year": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "month": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "minute": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "second": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "comment": "string",
      "dayOfWeek": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ],
      "dayOfMonth": [
        {
          "end": 42,
          "step": 1,
          "start": 42
        }
      ]
    }
  ],
  "intervals": [
    {
      "every": "5h30m",
      "offset": "0s"
    }
  ],
  "datasourceId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
  "knowledgebaseId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d"
}
```

---

### DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules

Deletes a datasource schedule.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasourceId` | string | Yes | The id of the datasource the schedule belongs to. |
| `id` | string | Yes | The id of the knowledgebase the schedule belongs to. |

#### Responses

##### 204

Successfully deleted a schedule.

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The resource does not exist.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules',
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
# qlik-cli has not implemented support for DELETE /api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/datasources/{datasourceId}/schedules" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/knowledgebases/{id}/histories

Retrieves sync history for the specified knowledgebase. Will return a `404` if no sync history exists, or if the calling user does not have access to synced datasources.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the knowledgebase. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of sync histories to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, eg. name. Can be prefixed with - to set descending order, defaults to ascending. Enum: "COMPLETED", "-COMPLETED" |

#### Responses

##### 200

List of sync items ordered by the completed time.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | sync id |
| `status` | string | Yes | Sync status Enum: "neverIndexed", "progress", "completed", "completedWithError" |
| `docStats` | object | Yes | Summary of documents processed |
| `startedAt` | string | Yes | Datetime when the sync task was started |
| `completedAt` | string | No | Datetime when the sync task was completed |
| `triggerType` | string | Yes | Datasource trigger type, was it manually or automatically synced |
| `connectionId` | string | Yes | Connection id that the datasource used |
| `datasourceId` | string | Yes | datasource id |
| `errorSummary` | object[] | No | Aggregated, deduplicated view of failures grouped by error code. Lets the UI surface a smart summary (e.g. "1000 files failed to parse") instead of a flat list of raw error strings. |
| `selectedErrors` | string[] | No | populated with up to the first selectedErrorsCount errors if there were any during sync |

<details>
<summary>Properties of `docStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `added` | integer | Yes |  |
| `errors` | integer | Yes |  |
| `deleted` | integer | Yes |  |
| `updated` | integer | Yes |  |
| `deltaBytes` | integer | Yes |  |
| `deltaTextSize` | integer | Yes |  |
| `largestFileSize` | integer | Yes |  |
| `deltaEffectivePages` | integer | Yes |  |
| `totalBytesProcessed` | integer | Yes |  |

</details>

<details>
<summary>Properties of `errorSummary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Stable, machine-readable error category shared across services and the UI. Enum: "unknown", "file_size_exceeded", "download_failed", "parse_failed", "parse_timeout", "chunk_failed", "chunk_timeout", "guardrail_blocked", "unsupported_file", "index_verification_failed", "file_not_found", "document_has_macros", "scan_failed", "pages_limit_exceeded", "pages_enforcement_failed", "governance_budget_exceeded" |
| `count` | integer | Yes | Number of files that failed with this error code. |
| `sample` | string | No | A representative (sanitized) error message for this category. |
| `sources` | string[] | No | Up to selectedErrorsCount example sources that failed with this code. |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

</details>

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

</details>

##### 403

The user does not have privileges to perform the requested action.

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

</details>

##### 404

The knowledgebase is not found, the knowledgebase has no sync history, or the calling user doesn't have access to the datasources in the knowledgebase.

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/knowledgebases/{id}/histories` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/knowledgebases/{id}/histories',
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
# qlik-cli has not implemented support for GET /api/v1/knowledgebases/{id}/histories yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases/{id}/histories" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "status": [
        "neverIndexed | progress | completed | completedWithError"
      ],
      "docStats": {
        "added": 1,
        "errors": 0,
        "deleted": 0,
        "updated": 0,
        "deltaBytes": 0,
        "deltaTextSize": 0,
        "largestFileSize": 123044444,
        "deltaEffectivePages": 0,
        "totalBytesProcessed": 123044444
      },
      "startedAt": "2021-10-02T14:20:50.52Z",
      "completedAt": "2021-10-02T14:20:50.52Z",
      "triggerType": [
        "manual | schedule"
      ],
      "connectionId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "datasourceId": "f256b3e4-03e0-4f74-ae46-a4d43882ee5d",
      "errorSummary": [
        {
          "code": "string",
          "count": 1000,
          "sample": "failed to parse document",
          "sources": [
            "myfile.pdf"
          ]
        }
      ],
      "selectedErrors": [
        "unsupported file extension"
      ]
    }
  ],
  "meta": {
    "countTotal": 42
  },
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
