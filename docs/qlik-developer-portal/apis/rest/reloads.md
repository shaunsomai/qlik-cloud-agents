# Reloads

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Reloads allows for triggering reloads of apps to refresh its data. Traditionally this has only been possible through the JSON-RPC WebSocket API, but can now also be done by using this REST API.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/reloads`](#get-apiv1reloads) | Finds and returns the reloads that the user has access to. |
| `POST` | [`/api/v1/reloads`](#post-apiv1reloads) | Reloads an app specified by an app ID. |
| `GET` | [`/api/v1/reloads/{reloadId}`](#get-apiv1reloadsreloadid) | Finds and returns a reload record. |
| `POST` | [`/api/v1/reloads/{reloadId}/actions/cancel`](#post-apiv1reloadsreloadidactionscancel) | Cancels a reload that is in progress or has been queued |

## API Reference

### GET /api/v1/reloads

Finds and returns the reloads that the user has access to.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The UUID formatted string used to search for an app's reload history entries. TenantAdmin users may omit this parameter to list all reload history in the tenant. |
| `filter` | string | No | SCIM filter expression used to search for reloads. The filter syntax is defined in RFC 7644 section 3.4.2.2  Supported attributes: - status: see #schemas/Status - partial: see #schemas/Partial - type: see #schemas/Type  Supported operators: - eq |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `log` | boolean | No | The boolean value used to include the log field or not, set log=true to include the log field. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `partial` | boolean | No | The boolean value used to search for a reload is partial or not. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `sort` | string | No | The field to sort by, with +/- prefix indicating sort order Enum: "creationTime", "+creationTime", "-creationTime", "status", "+status", "-status", "startTime", "+startTime", "-startTime", "endTime", "+endTime", "-endTime" |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 200

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the reload. |
| `log` | string | No | The log describing the result of the latest reload execution from the request. |
| `type` | string | Yes | What initiated the reload: hub = one-time reload manually triggered in hub, chronos = time based scheduled reload triggered by chronos, external = reload triggered via external API request, automations = reload triggered in automation, data-refresh = reload triggered by refresh of data, choreographer = reload triggered by choreographer. Enum: "hub", "external", "chronos", "automations", "data-refresh", "choreographer" |
| `appId` | string | Yes | The ID of the app. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the reload. There are seven statuses. `QUEUED`, `RELOADING`, `CANCELING` are the active statuses. `SUCCEEDED`, `FAILED`, `CANCELED`, `EXCEEDED_LIMIT` are the end statuses. Enum: "QUEUED", "RELOADING", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED", "EXCEEDED_LIMIT" |
| `userId` | string | Yes | The ID of the user who created the reload. |
| `weight` | integer | No | The weight of the reload for the same tenant. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1. |
| `endTime` | string | No | The time the reload job finished. |
| `partial` | boolean | No | The boolean value used to present the reload is partial or not. |
| `tenantId` | string | Yes | The ID of the tenant who owns the reload. |
| `errorCode` | string | No | The error code when the status is FAILED. |
| `startTime` | string | No | The time the reload job was consumed from the queue. |
| `engineTime` | string | No | The timestamp returned from the Sense engine upon successful reload. |
| `resourceId` | string | No | The String field identifying the specific resource ID within that service |
| `creationTime` | string | Yes | The time the reload job was created. |
| `errorMessage` | string | No | The error message when the status is FAILED. |
| `resourceType` | string | No | The String field identifying the service type that triggered the reload, e.g. "api" Enum: "api", "reload-tasks", "tasks", "automate" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No |  |

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
| `self` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `self`</summary>

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

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for retrieval of this reload(error code: RELOADS-003).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reloads` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/reloads', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/reloads yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reloads" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "5be59decca62aa00097268a4",
      "log": "ReloadID: 5be59decca62aa00097268a4\\nStarted loading\\n(A detailed script progress log can be downloaded when the reload is finished)\\nApp saved\\nFinished successfully\\n",
      "type": "chronos",
      "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
      "links": {
        "self": {
          "href": "http://example.com"
        }
      },
      "status": "FAILED",
      "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
      "weight": 1,
      "endTime": "2020-11-03T17:00:11.865Z",
      "partial": false,
      "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
      "errorCode": "EngineConnectionError",
      "startTime": "2020-11-03T17:00:06.351Z",
      "engineTime": "2020-11-03T17:00:07.048Z",
      "resourceId": "5be59decca62aa00097268a4",
      "creationTime": "2020-11-03T17:00:00.164Z",
      "errorMessage": "failed to complete reload: unexpected EOF",
      "resourceType": "api"
    }
  ],
  "links": {
    "self": {
      "href": "http://example.com"
    },
    "next": {
      "href": "http://example.com"
    },
    "prev": {
      "href": "http://example.com"
    }
  }
}
```

---

### POST /api/v1/reloads

Reloads an app specified by an app ID.

- **Rate Limit:** Special (50 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Request Body

**Required**

Request body specifying ID of app to be reloaded.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app to be reloaded. |
| `weight` | integer | No | The weight of the reload for the same tenant. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1. |
| `partial` | boolean | No | The boolean value used to present the reload is partial or not |
| `variables` | object | No | The variables to be used in the load script. Maximum of 20 variables allowed with a maximum length of 256 characters for each name/value. |
| `resourceId` | string | No | The String field identifying the specific resource ID within that service |
| `resourceType` | string | No | The String field identifying the service type that triggered the reload, e.g. "api" Enum: "api", "reload-tasks", "tasks", "automate" |

#### Responses

##### 201

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the reload. |
| `log` | string | No | The log describing the result of the latest reload execution from the request. |
| `type` | string | Yes | What initiated the reload: hub = one-time reload manually triggered in hub, chronos = time based scheduled reload triggered by chronos, external = reload triggered via external API request, automations = reload triggered in automation, data-refresh = reload triggered by refresh of data, choreographer = reload triggered by choreographer. Enum: "hub", "external", "chronos", "automations", "data-refresh", "choreographer" |
| `appId` | string | Yes | The ID of the app. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the reload. There are seven statuses. `QUEUED`, `RELOADING`, `CANCELING` are the active statuses. `SUCCEEDED`, `FAILED`, `CANCELED`, `EXCEEDED_LIMIT` are the end statuses. Enum: "QUEUED", "RELOADING", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED", "EXCEEDED_LIMIT" |
| `userId` | string | Yes | The ID of the user who created the reload. |
| `weight` | integer | No | The weight of the reload for the same tenant. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1. |
| `endTime` | string | No | The time the reload job finished. |
| `partial` | boolean | No | The boolean value used to present the reload is partial or not. |
| `tenantId` | string | Yes | The ID of the tenant who owns the reload. |
| `errorCode` | string | No | The error code when the status is FAILED. |
| `startTime` | string | No | The time the reload job was consumed from the queue. |
| `engineTime` | string | No | The timestamp returned from the Sense engine upon successful reload. |
| `resourceId` | string | No | The String field identifying the specific resource ID within that service |
| `creationTime` | string | Yes | The time the reload job was created. |
| `errorMessage` | string | No | The error message when the status is FAILED. |
| `resourceType` | string | No | The String field identifying the service type that triggered the reload, e.g. "api" Enum: "api", "reload-tasks", "tasks", "automate" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for execution of this reload(error code: RELOADS-003) or the reload frequency quota has been met.(error code: RELOADS-013).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 429

Too many requests, a pending reload request already exists for this app.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/reloads` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/reloads', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    appId: '116dbfae-7fb9-4983-8e23-5ccd8c508722',
    weight: 1,
    partial: false,
    variables: { var1: 'value1', var2: 'value2' },
    resourceId: '5be59decca62aa00097268a4',
    resourceType: 'api',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/reloads yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reloads" \
-X POST \
-H "Authorization: Bearer <access_token>" \
-H "Content-type: application/json" \
-d '{"appId":"116dbfae-7fb9-4983-8e23-5ccd8c508722","weight":1,"partial":false,"variables":{"var1":"value1","var2":"value2"},"resourceId":"5be59decca62aa00097268a4","resourceType":"api"}'
```

**Example Response:**

```json
{
  "id": "5be59decca62aa00097268a4",
  "log": "ReloadID: 5be59decca62aa00097268a4\\nStarted loading\\n(A detailed script progress log can be downloaded when the reload is finished)\\nApp saved\\nFinished successfully\\n",
  "type": "chronos",
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "links": {
    "self": {
      "href": "http://example.com"
    }
  },
  "status": "FAILED",
  "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
  "weight": 1,
  "endTime": "2020-11-03T17:00:11.865Z",
  "partial": false,
  "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
  "errorCode": "EngineConnectionError",
  "startTime": "2020-11-03T17:00:06.351Z",
  "engineTime": "2020-11-03T17:00:07.048Z",
  "resourceId": "5be59decca62aa00097268a4",
  "creationTime": "2020-11-03T17:00:00.164Z",
  "errorMessage": "failed to complete reload: unexpected EOF",
  "resourceType": "api"
}
```

---

### GET /api/v1/reloads/{reloadId}

Finds and returns a reload record.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadId` | string | Yes | The unique identifier of the reload. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 200

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the reload. |
| `log` | string | No | The log describing the result of the latest reload execution from the request. |
| `type` | string | Yes | What initiated the reload: hub = one-time reload manually triggered in hub, chronos = time based scheduled reload triggered by chronos, external = reload triggered via external API request, automations = reload triggered in automation, data-refresh = reload triggered by refresh of data, choreographer = reload triggered by choreographer. Enum: "hub", "external", "chronos", "automations", "data-refresh", "choreographer" |
| `appId` | string | Yes | The ID of the app. |
| `links` | object | No |  |
| `status` | string | Yes | The status of the reload. There are seven statuses. `QUEUED`, `RELOADING`, `CANCELING` are the active statuses. `SUCCEEDED`, `FAILED`, `CANCELED`, `EXCEEDED_LIMIT` are the end statuses. Enum: "QUEUED", "RELOADING", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED", "EXCEEDED_LIMIT" |
| `userId` | string | Yes | The ID of the user who created the reload. |
| `weight` | integer | No | The weight of the reload for the same tenant. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1. |
| `endTime` | string | No | The time the reload job finished. |
| `partial` | boolean | No | The boolean value used to present the reload is partial or not. |
| `tenantId` | string | Yes | The ID of the tenant who owns the reload. |
| `errorCode` | string | No | The error code when the status is FAILED. |
| `startTime` | string | No | The time the reload job was consumed from the queue. |
| `engineTime` | string | No | The timestamp returned from the Sense engine upon successful reload. |
| `resourceId` | string | No | The String field identifying the specific resource ID within that service |
| `creationTime` | string | Yes | The time the reload job was created. |
| `errorMessage` | string | No | The error message when the status is FAILED. |
| `resourceType` | string | No | The String field identifying the service type that triggered the reload, e.g. "api" Enum: "api", "reload-tasks", "tasks", "automate" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow to find or get a reload(error code: RELOADS-003).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reloads/{reloadId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reloads/{reloadId}',
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
# qlik-cli has not implemented support for GET /api/v1/reloads/{reloadId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reloads/{reloadId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5be59decca62aa00097268a4",
  "log": "ReloadID: 5be59decca62aa00097268a4\\nStarted loading\\n(A detailed script progress log can be downloaded when the reload is finished)\\nApp saved\\nFinished successfully\\n",
  "type": "chronos",
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "links": {
    "self": {
      "href": "http://example.com"
    }
  },
  "status": "FAILED",
  "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
  "weight": 1,
  "endTime": "2020-11-03T17:00:11.865Z",
  "partial": false,
  "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
  "errorCode": "EngineConnectionError",
  "startTime": "2020-11-03T17:00:06.351Z",
  "engineTime": "2020-11-03T17:00:07.048Z",
  "resourceId": "5be59decca62aa00097268a4",
  "creationTime": "2020-11-03T17:00:00.164Z",
  "errorMessage": "failed to complete reload: unexpected EOF",
  "resourceType": "api"
}
```

---

### POST /api/v1/reloads/{reloadId}/actions/cancel

Cancels a reload that is in progress or has been queued

- **Rate Limit:** Special (50 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadId` | string | Yes | The unique identifier of the reload. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 202

Reload is being cancelled.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The status of the reload. Enum: "QUEUED", "RELOADING", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED", "EXCEEDED_LIMIT" |

##### 204

Reload has been cancelled.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow to cancel a reload(error code: RELOADS-003).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

The specified reload record could not be found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 409

Reload is not in a cancellable state.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes | The error code is in form of 'RELOADS-xxx'. ranges from 'RELOADS-001' to 'RELOADS-013'. |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/reloads/{reloadId}/actions/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reloads/{reloadId}/actions/cancel',
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
# qlik-cli has not implemented support for POST /api/v1/reloads/{reloadId}/actions/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reloads/{reloadId}/actions/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "RELOADING"
}
```

---
