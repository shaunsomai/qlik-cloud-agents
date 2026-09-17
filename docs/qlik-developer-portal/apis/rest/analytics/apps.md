# Apps

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/analytics/apps/{appId}/actions/restore`](#post-apianalyticsappsappidactionsrestore) | Restores a soft-deleted Qlik Cloud Analytics application to the same space with the same app ID, retaining the properties it had at the time of deletion. |
| `GET` | [`/api/analytics/apps/{guid}/evaluations`](#get-apianalyticsappsguidevaluations) | Returns a paginated list of historical evaluations for the specified app. Use |
| `POST` | [`/api/analytics/apps/{guid}/evaluations`](#post-apianalyticsappsguidevaluations) | Queues a performance and scalability evaluation for the specified app, scheduling |
| `GET` | [`/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}`](#get-apianalyticsappsevaluationsbaselineidcomparecomparisonid) | Compares exactly two app evaluations, a baseline and a comparison, returning a structured |
| `GET` | [`/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download`](#get-apianalyticsappsevaluationsbaselineidcomparecomparisonidactionsdownload) | Downloads a comparison log for the two specified app evaluations (baseline and comparison), |
| `GET` | [`/api/analytics/apps/evaluations/{id}`](#get-apianalyticsappsevaluationsid) | Retrieves a single app evaluation by its unique identifier. Use the `all` parameter |
| `GET` | [`/api/analytics/apps/evaluations/{id}/actions/download`](#get-apianalyticsappsevaluationsidactionsdownload) | Downloads the evaluation log for the specified app evaluation, defaulting to XML |

## API Reference

### POST /api/analytics/apps/{appId}/actions/restore

Restores a soft-deleted Qlik Cloud Analytics application to the same space with the same app ID, retaining the properties it had at the time of deletion.
This operation is available to the app owner and Tenant Admins. The app owner can restore the app only if the original space still exists and they still have delete permission in the space; otherwise, a 403 Forbidden error is returned.
Associated resources such as data alerts, subscriptions, collections, notes, and tags are deleted when the app is deleted and cannot be restored.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | Application attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `state` | string | No | Promotion state of the app. Promotion state of an app. One of: * EMPTY * PROMOTED * DISTRIBUTED Enum: "EMPTY", "PROMOTED", "DISTRIBUTED" |
| `usage` | string | No | Indicates the use for the app.  One of: * ANALYTICS * DATA_PREPARATION * DATAFLOW_PREP * SINGLE_TABLE_PREP * DIRECT_QUERY_MODE Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `ownerId` | string | No | Identifier of the app owner. |
| `spaceId` | string | No | The ID of the app's space. |
| `createdAt` | string | No | The date and time when the app was created. |
| `updatedAt` | string | No | The date and time when the app was modified. |
| `promotedAt` | string | No | The date and time when the app was promoted, empty if not promoted. Use to determine if an app is promoted in Qlik Cloud. |
| `reloadedAt` | string | No | Date and time of the last reload of the app. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for promoted apps. |
| `resourceType` | string | No | App resource type. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured. |

</details>

##### 400

Bad request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of all errors that occurred during the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A unique code for the error. |
| `title` | string | Yes | A human-readable description of the error. |
| `detail` | string | No | Additional information about the error. |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of all errors that occurred during the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A unique code for the error. |
| `title` | string | Yes | A human-readable description of the error. |
| `detail` | string | No | Additional information about the error. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of all errors that occurred during the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A unique code for the error. |
| `title` | string | Yes | A human-readable description of the error. |
| `detail` | string | No | Additional information about the error. |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of all errors that occurred during the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A unique code for the error. |
| `title` | string | Yes | A human-readable description of the error. |
| `detail` | string | No | Additional information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/apps/{appId}/actions/restore` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/{appId}/actions/restore',
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
# qlik-cli has not implemented support for POST /api/analytics/apps/{appId}/actions/restore yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/{appId}/actions/restore" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "state": "string",
    "usage": "string",
    "ownerId": "string",
    "spaceId": "string",
    "createdAt": "2019-01-01T00:00:00.000Z",
    "updatedAt": "2019-01-01T00:00:00.000Z",
    "promotedAt": "2019-01-01T00:00:00.000Z",
    "reloadedAt": "2019-01-01T00:00:00.000Z",
    "description": "string",
    "originAppId": "string",
    "resourceType": "string",
    "hasSectionAccess": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/analytics/apps/{guid}/evaluations

Returns a paginated list of historical evaluations for the specified app. Use
the `next` and `prev` cursor values from the response links to navigate through
pages of results.


- **Replaces:** "GET:/v1/apps/{guid}/evaluations"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | string | Yes | The unique identifier of the app. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | When `true`, includes full evaluation details in each result. When `false`, detail fields are omitted. |
| `fileMode` | boolean | No | When `true`, adds file download headers to the response. |
| `format` | string | No | The output format for the response. Accepts `json` or `xml`. |
| `limit` | integer | No | Maximum number of results to return per page. |
| `next` | string | No | A cursor token for fetching the next page of results. |
| `prev` | string | No | A cursor token for fetching the previous page of results. |
| `sort` | string | No | The field to sort results by. Prefix with `-` for descending order or `+` for ascending. Enum: "started", "+started", "-started" |

#### Responses

##### 200

App evaluations retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `engine` | object | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `openAppProgress` | object | No |  |
| `reloadInformation` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `openApp` | object | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `sheetsCached` | object[] | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `openApp`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objNoCache`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `openAppProgress`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `messages` | object[] | No |  |

<details>
<summary>Properties of `messages`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `reloadInformation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

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

</details>

##### 400

Bad request. The request contains invalid or missing parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 403

Access denied. You lack the required permissions to list evaluations for this app.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 404

The specified app was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/apps/{guid}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/{guid}/evaluations',
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
# qlik-cli has not implemented support for GET /api/analytics/apps/{guid}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/{guid}/evaluations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "5ecb5e65028d1f0001a98071",
      "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
      "ended": "2022-02-09T06:58:40.575Z",
      "engine": {
        "shortName": "OAPE-40"
      },
      "events": [
        {
          "message": "An object failed",
          "sheetId": "gregFG",
          "objectId": "adfRFr",
          "severity": "warning",
          "errorCode": "ERR-GOPHERCISER",
          "objectType": "linechart",
          "sheetTitle": "mysheet",
          "objectTitle": "profit",
          "objectVisualization": "linechart"
        }
      ],
      "result": {
        "openApp": {
          "steps": [
            {
              "name": "loadingFields",
              "durationMilliseconds": 1234
            }
          ],
          "totalDurationMilliseconds": 12345
        },
        "rowCount": 20000,
        "objNoCache": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "sheetCount": 5,
        "objectCount": 33,
        "sheetsCached": [
          {
            "sheet": {
              "id": "fjETFn",
              "title": "my chart",
              "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
              "objectType": "table",
              "sheetTitle": "my sheet",
              "timeoutStatusCode": "CALC-TIMEOUT",
              "responseTimeSeconds": 12.3
            },
            "objectCount": 1,
            "sheetObjects": [
              {
                "id": "fjETFn",
                "title": "my chart",
                "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
                "objectType": "table",
                "sheetTitle": "my sheet",
                "timeoutStatusCode": "CALC-TIMEOUT",
                "responseTimeSeconds": 12.3
              }
            ]
          }
        ],
        "objSlowCached": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "objMemoryLimit": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "memoryLimitStatusCode": "OUT-OF-MEMORY"
          }
        ],
        "sheetsUncached": [
          {
            "sheet": {
              "id": "fjETFn",
              "title": "my chart",
              "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
              "objectType": "table",
              "sheetTitle": "my sheet",
              "timeoutStatusCode": "CALC-TIMEOUT",
              "responseTimeSeconds": 12.3
            },
            "objectCount": 1,
            "sheetObjects": [
              {
                "id": "fjETFn",
                "title": "my chart",
                "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
                "objectType": "table",
                "sheetTitle": "my sheet",
                "timeoutStatusCode": "CALC-TIMEOUT",
                "responseTimeSeconds": 12.3
              }
            ]
          }
        ],
        "documentSizeMiB": 12.3,
        "objSlowUncached": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "hasSectionAccess": false,
        "topFieldsByBytes": [
          {
            "name": "some field/table",
            "byteSize": 12873,
            "isSystem": false
          }
        ],
        "topTablesByBytes": [
          {
            "name": "some field/table",
            "byteSize": 12873,
            "isSystem": false
          }
        ],
        "objSingleThreaded": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "cpuQuotients": [
              12.3
            ],
            "responseTimeSeconds": 12.3
          }
        ]
      },
      "status": "finished",
      "appName": "my app",
      "details": {
        "errors": [
          "this is an error"
        ],
        "warnings": [
          "this is a warning"
        ],
        "objectMetrics": {},
        "engineHasCache": false,
        "concurrentReload": false
      },
      "started": "2022-02-09T06:58:40.575Z",
      "version": 1,
      "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
      "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
      "timestamp": "2022-02-09T06:58:40.575Z",
      "openAppProgress": {
        "messages": [
          {
            "message": "TODO",
            "timeSinceStartMilliseconds": "TODO"
          }
        ]
      },
      "reloadInformation": {
        "reloadmeta": {
          "cpuspent": "123983",
          "peakmemorybytes": 112
        },
        "amountofrows": 1423423234,
        "amountoffields": 12,
        "amountoftables": 7,
        "staticbytesize": 1444234,
        "hassectionaccess": false,
        "amountoffieldvalues": 144423433,
        "amountofcardinalfieldvalues": 14442
      }
    }
  ],
  "links": {
    "next": {
      "href": "/analytics/apps/evaluations/appId=a84c22cf-31e5-41fe-9e8f-544b85513484&prev=5f5201908b3fc5fc132dbd35"
    },
    "prev": {
      "href": "/analytics/apps/evaluations/appId=a84c22cf-31e5-41fe-9e8f-544b85513484&prev=5f5201908b3fc5fc132dbd35"
    }
  }
}
```

---

### POST /api/analytics/apps/{guid}/evaluations

Queues a performance and scalability evaluation for the specified app, scheduling
it for execution by the evaluation engine. The evaluation measures object response
times, CPU usage, document size, and data model metrics. Once queued, use the
returned `id` with the retrieval operations to poll for results.


- **Replaces:** "POST:/v1/apps/{guid}/evaluations"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | string | Yes | The unique identifier of the app to evaluate. |

#### Request Body

Optional evaluation settings. The body may be omitted entirely.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `engineSizeHint` | string | No | Overrides the automatic engine size calculation with the supplied number of GiB. The value is forwarded to the engine session request when acquiring an engine. Optional. |

#### Responses

##### 201

App evaluation queued successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `engine` | object | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `openAppProgress` | object | No |  |
| `reloadInformation` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `openApp` | object | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `sheetsCached` | object[] | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `openApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `steps` | object[] | No |  |
| `totalDurationMilliseconds` | number | No |  |

<details>
<summary>Properties of `steps`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `cpuQuotients` | number[] | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `openAppProgress`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `messages` | object[] | No |  |

<details>
<summary>Properties of `messages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `timeSinceStartMilliseconds` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `reloadInformation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 400

Bad request. The app identifier is missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 403

Access denied. You lack the required permissions to evaluate the app.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 404

The specified app was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 429

The rate limit has been exceeded.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/apps/{guid}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/{guid}/evaluations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      engineSizeHint: '80',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/apps/{guid}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/{guid}/evaluations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"engineSizeHint":"80"}'
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "engine": {
    "shortName": "OAPE-40"
  },
  "events": [
    {
      "message": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "openApp": {
      "steps": [
        {
          "name": "loadingFields",
          "durationMilliseconds": 1234
        }
      ],
      "totalDurationMilliseconds": 12345
    },
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "sheetsCached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "sheetsUncached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "cpuQuotients": [
          12.3
        ],
        "responseTimeSeconds": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "openAppProgress": {
    "messages": [
      {
        "message": "TODO",
        "timeSinceStartMilliseconds": "TODO"
      }
    ]
  },
  "reloadInformation": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  }
}
```

---

### GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}

Compares exactly two app evaluations, a baseline and a comparison, returning a structured
diff of performance metrics between them. Use this operation to detect regressions
after app changes or engine upgrades. Both evaluations must belong to the same app.


- **Replaces:** "GET:/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `baselineId` | string | Yes | The unique identifier of the baseline app evaluation. |
| `comparisonId` | string | Yes | The unique identifier of the comparison app evaluation. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | When `true`, includes all comparison entries regardless of significance. |
| `format` | string | No | The output format for the response. Accepts `json` or `xml`. |

#### Responses

##### 200

Comparison completed successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `engine` | object | No |  |
| `rowCount` | object | No |  |
| `objNoCache` | object | No |  |
| `sheetCount` | object | No |  |
| `objectCount` | object | No |  |
| `sheetsCached` | object | No |  |
| `objSlowCached` | object | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object | No |  |
| `documentSizeMiB` | object | No |  |
| `objSlowUncached` | object | No |  |
| `hasSectionAccess` | object | No |  |
| `topFieldsByBytes` | object | No |  |
| `topTablesByBytes` | object | No |  |
| `objSingleThreaded` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `changed` | boolean | No |  |
| `baseline` | object | No |  |
| `comparison` | object | No |  |

<details>
<summary>Properties of `baseline`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `comparison`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `rowCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `sheetCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objectCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `baselineMemoryLimitStatusCode` | string | No |  |
| `comparisonMemoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `documentSizeMiB`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `hasSectionAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | boolean | No |  |
| `comparison` | boolean | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

One or both of the specified app evaluations were not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}',
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
# qlik-cli has not implemented support for GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "engine": {
    "changed": false,
    "baseline": {
      "shortName": "OAPE-40"
    },
    "comparison": {
      "shortName": "OAPE-40"
    }
  },
  "rowCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objNoCache": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "sheetCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objectCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "sheetsCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objSlowCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objMemoryLimit": [
    {
      "id": "fjETFn",
      "title": "my chart",
      "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
      "objectType": "table",
      "sheetTitle": "my sheet",
      "dataSourceStatus": "full",
      "baselineMemoryLimitStatusCode": "OUT-OF-MEMORY",
      "comparisonMemoryLimitStatusCode": "OUT-OF-MEMORY"
    }
  ],
  "sheetsUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "documentSizeMiB": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objSlowUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "hasSectionAccess": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": false,
    "comparison": true
  },
  "topFieldsByBytes": {
    "list": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "topTablesByBytes": {
    "list": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "objSingleThreaded": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  }
}
```

---

### GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download

Downloads a comparison log for the two specified app evaluations (baseline and comparison),
defaulting to XML format. Use the `Accept` header to request JSON output instead.
Both evaluations must belong to the same app.


- **Replaces:** "GET:/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `baselineId` | string | Yes | The unique identifier of the baseline app evaluation. |
| `comparisonId` | string | Yes | The unique identifier of the comparison app evaluation. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | The desired response format. Accepts `application/xml` (default) or `application/json`. Enum: "application/xml", "application/json" |

#### Responses

##### 200

Comparison log retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `engine` | object | No |  |
| `rowCount` | object | No |  |
| `objNoCache` | object | No |  |
| `sheetCount` | object | No |  |
| `objectCount` | object | No |  |
| `sheetsCached` | object | No |  |
| `objSlowCached` | object | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object | No |  |
| `documentSizeMiB` | object | No |  |
| `objSlowUncached` | object | No |  |
| `hasSectionAccess` | object | No |  |
| `topFieldsByBytes` | object | No |  |
| `topTablesByBytes` | object | No |  |
| `objSingleThreaded` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `changed` | boolean | No |  |
| `baseline` | object | No |  |
| `comparison` | object | No |  |

<details>
<summary>Properties of `baseline`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `comparison`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `rowCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `sheetCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objectCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `baselineMemoryLimitStatusCode` | string | No |  |
| `comparisonMemoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `documentSizeMiB`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `hasSectionAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | boolean | No |  |
| `comparison` | boolean | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `cardinal` | object | No |  |
| `isSystem` | boolean | No |  |
| `totalCount` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `totalCount`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | object | No |  |
| `isSystem` | boolean | No |  |
| `noOfRows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byteSize`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `noOfRows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

One or both of the specified app evaluations were not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download',
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
# qlik-cli has not implemented support for GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "engine": {
    "changed": false,
    "baseline": {
      "shortName": "OAPE-40"
    },
    "comparison": {
      "shortName": "OAPE-40"
    }
  },
  "rowCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objNoCache": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "sheetCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objectCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "sheetsCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objSlowCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objMemoryLimit": [
    {
      "id": "fjETFn",
      "title": "my chart",
      "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
      "objectType": "table",
      "sheetTitle": "my sheet",
      "dataSourceStatus": "full",
      "baselineMemoryLimitStatusCode": "OUT-OF-MEMORY",
      "comparisonMemoryLimitStatusCode": "OUT-OF-MEMORY"
    }
  ],
  "sheetsUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "documentSizeMiB": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objSlowUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "hasSectionAccess": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": false,
    "comparison": true
  },
  "topFieldsByBytes": {
    "list": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a field name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "totalCount": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "topTablesByBytes": {
    "list": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a table name",
        "byteSize": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "isSystem": false,
        "noOfRows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "objSingleThreaded": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  }
}
```

---

### GET /api/analytics/apps/evaluations/{id}

Retrieves a single app evaluation by its unique identifier. Use the `all` parameter
to include full evaluation details in the response.


- **Replaces:** "GET:/v1/apps/evaluations/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the app evaluation to retrieve. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | When `true`, includes full app evaluation details in the response. |
| `format` | string | No | The output format for the response. Accepts `json` or `xml`. |

#### Responses

##### 200

App evaluation retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `engine` | object | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `openAppProgress` | object | No |  |
| `reloadInformation` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `openApp` | object | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `sheetsCached` | object[] | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `openApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `steps` | object[] | No |  |
| `totalDurationMilliseconds` | number | No |  |

<details>
<summary>Properties of `steps`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `cpuQuotients` | number[] | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `openAppProgress`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `messages` | object[] | No |  |

<details>
<summary>Properties of `messages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `timeSinceStartMilliseconds` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `reloadInformation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 404

The specified app evaluation was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/apps/evaluations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/evaluations/{id}',
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
# qlik-cli has not implemented support for GET /api/analytics/apps/evaluations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/evaluations/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "engine": {
    "shortName": "OAPE-40"
  },
  "events": [
    {
      "message": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "openApp": {
      "steps": [
        {
          "name": "loadingFields",
          "durationMilliseconds": 1234
        }
      ],
      "totalDurationMilliseconds": 12345
    },
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "sheetsCached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "sheetsUncached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "cpuQuotients": [
          12.3
        ],
        "responseTimeSeconds": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "openAppProgress": {
    "messages": [
      {
        "message": "TODO",
        "timeSinceStartMilliseconds": "TODO"
      }
    ]
  },
  "reloadInformation": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  }
}
```

---

### GET /api/analytics/apps/evaluations/{id}/actions/download

Downloads the evaluation log for the specified app evaluation, defaulting to XML
format. Use the `Accept` header to request JSON output instead.


- **Replaces:** "GET:/v1/apps/evaluations/{id}/actions/download"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the app evaluation to download. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | The desired response format. Accepts `application/xml` (default) or `application/json`. Enum: "application/xml", "application/json" |

#### Responses

##### 200

App evaluation log retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `engine` | object | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `openAppProgress` | object | No |  |
| `reloadInformation` | object | No |  |

<details>
<summary>Properties of `engine`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shortName` | string | No |  |

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `openApp` | object | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `sheetsCached` | object[] | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `openApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `steps` | object[] | No |  |
| `totalDurationMilliseconds` | number | No |  |

<details>
<summary>Properties of `steps`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byteSize` | number | No |  |
| `isSystem` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `cpuQuotients` | number[] | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `openAppProgress`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `messages` | object[] | No |  |

<details>
<summary>Properties of `messages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `timeSinceStartMilliseconds` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `reloadInformation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 404

The specified app evaluation was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/apps/evaluations/{id}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/apps/evaluations/{id}/actions/download',
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
# qlik-cli has not implemented support for GET /api/analytics/apps/evaluations/{id}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/evaluations/{id}/actions/download" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "engine": {
    "shortName": "OAPE-40"
  },
  "events": [
    {
      "message": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "openApp": {
      "steps": [
        {
          "name": "loadingFields",
          "durationMilliseconds": 1234
        }
      ],
      "totalDurationMilliseconds": 12345
    },
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "sheetsCached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "sheetsUncached": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "sheetTitle": "my sheet",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "sheetTitle": "my sheet",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "some field/table",
        "byteSize": 12873,
        "isSystem": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "sheetTitle": "my sheet",
        "cpuQuotients": [
          12.3
        ],
        "responseTimeSeconds": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "openAppProgress": {
    "messages": [
      {
        "message": "TODO",
        "timeSinceStartMilliseconds": "TODO"
      }
    ]
  },
  "reloadInformation": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  }
}
```

---
