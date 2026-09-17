# ODAG requests

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Submit, track, and manage on-demand analytics generation requests and their generated applications.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/analytics/odag-requests/{requestId}`](#get-apianalyticsodag-requestsrequestid) | Retrieves the current status and details of an ODAG request, including its state (`queued`, `loading`, `succeeded`, `failed`), generated Analytics Application ID, and error information. For multi-application generation requests, includes nested status for each sub-request. |
| `PUT` | [`/api/analytics/odag-requests/{requestId}`](#put-apianalyticsodag-requestsrequestid) | Performs actions on ODAG requests such as pausing, resuming, or canceling them. Cancel actions are effective only before the data loading phase. For multi-application generation requests, actions apply only to sub-requests that have not yet started loading. Automatic acknowledgment  option simplifies state transitions. |
| `DELETE` | [`/api/analytics/odag-requests/{requestId}/app`](#delete-apianalyticsodag-requestsrequestidapp) | Deletes the generated Analytics Application associated with a completed request. Only the request owner or ODAG link creator can delete generated Analytics Applications. |
| `POST` | [`/api/analytics/odag-requests/{requestId}/reload-app`](#post-apianalyticsodag-requestsrequestidreload-app) | Reloads data in a generated Analytics Application from the underlying data sources. Only the request owner or ODAG link creator can reload generated Analytics Applications. |
| `POST` | [`/api/analytics/odag-requests/{requestId}/rename-app`](#post-apianalyticsodag-requestsrequestidrename-app) | Renames a generated Analytics Application. Only the request owner or ODAG link creator can rename generated Analytics Applications. |
| `GET` | [`/api/analytics/odag-requests/{requestId}/selections`](#get-apianalyticsodag-requestsrequestidselections) | Retrieves the selection state (selected and optional field values) that was active when the Analytics Application generation request was submitted. |

## API Reference

### GET /api/analytics/odag-requests/{requestId}

Retrieves the current status and details of an ODAG request, including its state (`queued`, `loading`, `succeeded`, `failed`), generated Analytics Application ID, and error information. For multi-application generation requests, includes nested status for each sub-request.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the ODAG request whose status is to be returned. |

#### Responses

##### 200

Successful response - see request status in response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-requests/{requestId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}',
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
# qlik-cli has not implemented support for GET /api/analytics/odag-requests/{requestId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "kind": "single",
  "link": "string",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "state": "validating",
  "loadState": {
    "status": "pending",
    "loadHost": "string",
    "startedAt": "2025-11-11T13:45:30Z",
    "finishedAt": "2025-11-11T13:45:30Z"
  },
  "sheetname": "string",
  "purgeAfter": "2025-11-11T13:45:30Z",
  "timeToLive": 42,
  "validation": [
    "string"
  ],
  "createdDate": "2025-11-11T13:45:30Z",
  "targetSheet": "string",
  "templateApp": "string",
  "actualRowEst": 42,
  "errorMessage": "string",
  "generatedApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "selectionApp": "string",
  "curRowEstExpr": "string",
  "retentionTime": 42,
  "parentRequestId": "string",
  "templateAppName": "appname",
  "bindingStateHash": 42,
  "generatedAppName": "appname",
  "selectionAppName": "appname",
  "curRowEstLowBound": 42,
  "curRowEstHighBound": 42,
  "selectionStateHash": 42
}
```

---

### PUT /api/analytics/odag-requests/{requestId}

Performs actions on ODAG requests such as pausing, resuming, or canceling them. Cancel actions are effective only before the data loading phase. For multi-application generation requests, actions apply only to sub-requests that have not yet started loading. Automatic acknowledgment  option simplifies state transitions.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the request whose status is to be returned. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | string | Yes | The action to perform on the request. One of: (1) `cancel` a pending or in-flight request; (2) `pause` a request that has not started (still in the `queued` state); (3) `resume` a paused request; (4) acknowledge a prior cancellation; or (5) acknowledge a prior failure. Enum: "cancel", "pause", "resume", "ackcancel", "ackfailure" |
| `autoAck` | boolean | No | Optional flag used with the `cancel` action. When `autoAck` is `true`, a canceled request automatically transitions to the `canceledAck` state after cancellation completes. When `autoAck` is `false`, the request transitions to `canceled`, and you must call this endpoint again with `action=ackcancel` to acknowledge the cancellation. |
| `delGenApp` | boolean | No | Optional flag that deletes the generated Analytics Application after an `action` of `cancel` (with `autoAck=true`), `ackcancel`, or `ackfailure`. |
| `ignoreSucceeded` | boolean | No | Optional flag used with the `cancel` action. When `true`, the API does not return an error if the request reaches the `succeeded` state while the cancellation request is in progress. |

#### Responses

##### 200

Successful response - see request status in response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/analytics/odag-requests/{requestId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/analytics/odag-requests/{requestId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}" \
-X PUT \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "kind": "single",
  "link": "string",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "state": "validating",
  "loadState": {
    "status": "pending",
    "loadHost": "string",
    "startedAt": "2025-11-11T13:45:30Z",
    "finishedAt": "2025-11-11T13:45:30Z"
  },
  "sheetname": "string",
  "purgeAfter": "2025-11-11T13:45:30Z",
  "timeToLive": 42,
  "validation": [
    "string"
  ],
  "createdDate": "2025-11-11T13:45:30Z",
  "targetSheet": "string",
  "templateApp": "string",
  "actualRowEst": 42,
  "errorMessage": "string",
  "generatedApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "selectionApp": "string",
  "curRowEstExpr": "string",
  "retentionTime": 42,
  "parentRequestId": "string",
  "templateAppName": "appname",
  "bindingStateHash": 42,
  "generatedAppName": "appname",
  "selectionAppName": "appname",
  "curRowEstLowBound": 42,
  "curRowEstHighBound": 42,
  "selectionStateHash": 42
}
```

---

### DELETE /api/analytics/odag-requests/{requestId}/app

Deletes the generated Analytics Application associated with a completed request. Only the request owner or ODAG link creator can delete generated Analytics Applications.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the request. |

#### Responses

##### 204

Successful response - No Content.

##### 403

Insufficient privilege to delete the generated Analytics Application. User must be either owner of the request or the ODAG link.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID or generated Analytics Application not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/analytics/odag-requests/{requestId}/app` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}/app',
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
# qlik-cli has not implemented support for DELETE /api/analytics/odag-requests/{requestId}/app yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}/app" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/analytics/odag-requests/{requestId}/reload-app

Reloads data in a generated Analytics Application from the underlying data sources. Only the request owner or ODAG link creator can reload generated Analytics Applications.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the request. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `copyRequest` | boolean | No | Determines whether the request should be copied along with the generated Analytics Application. |
| `actualRowEst` | integer | No | The current row estimate value calculated by the link's `rowEstExpr` property in the context of the selection Analytics Application. |
| `selectionState` | object[] | No | A collection of FieldSelectionStateV2 objects. |
| `bindSelectionState` | object[] | No | A collection of FieldSelectionStateV2 objects. |

<details>
<summary>Properties of `selectionState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The list of values in the selection state for this field. |
| `selectedSize` | integer | No | The actual number of selected values. Not used for `bindSelectionState`. |
| `selectionAppParamName` | string | Yes | The name of a variable or field that corresponds to one or more bindings having a matching `selectAppParamName` used to generate Analytics Applications. |
| `selectionAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |

<details>
<summary>Properties of `values`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numValue` | string | No |  |
| `strValue` | string | Yes |  |
| `selStatus` | string | Yes | The valid set of selection states that a specific field value can be in. One of: `S` (selected), `O` (optional), or `X` (excluded). Enum: "S", "O", "X" |

</details>

</details>

<details>
<summary>Properties of `bindSelectionState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The list of values in the selection state for this field. |
| `selectedSize` | integer | No | The actual number of selected values. Not used for `bindSelectionState`. |
| `selectionAppParamName` | string | Yes | The name of a variable or field that corresponds to one or more bindings having a matching `selectAppParamName` used to generate Analytics Applications. |
| `selectionAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |

<details>
<summary>Properties of `values`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numValue` | string | No |  |
| `strValue` | string | Yes |  |
| `selStatus` | string | Yes | The valid set of selection states that a specific field value can be in. One of: `S` (selected), `O` (optional), or `X` (excluded). Enum: "S", "O", "X" |

</details>

</details>

#### Responses

##### 200

Successful response. Returns the updated request state.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 403

Insufficient privilege to reload the generated Analytics Application. User must be either owner of the request or the ODAG link.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID or generated Analytics Application not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/odag-requests/{requestId}/reload-app` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}/reload-app',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      copyRequest: true,
      actualRowEst: 42,
      selectionState: [
        {
          values: [
            {
              numValue: 'string',
              strValue: 'string',
              selStatus: 'S',
            },
          ],
          selectedSize: 42,
          selectionAppParamName: 'string',
          selectionAppParamType: 'Field',
        },
      ],
      bindSelectionState: [
        {
          values: [
            {
              numValue: 'string',
              strValue: 'string',
              selStatus: 'S',
            },
          ],
          selectedSize: 42,
          selectionAppParamName: 'string',
          selectionAppParamType: 'Field',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/odag-requests/{requestId}/reload-app yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}/reload-app" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"copyRequest":true,"actualRowEst":42,"selectionState":[{"values":[{"numValue":"string","strValue":"string","selStatus":"S"}],"selectedSize":42,"selectionAppParamName":"string","selectionAppParamType":"Field"}],"bindSelectionState":[{"values":[{"numValue":"string","strValue":"string","selStatus":"S"}],"selectedSize":42,"selectionAppParamName":"string","selectionAppParamType":"Field"}]}'
```

**Example Response:**

```json
{
  "id": "string",
  "kind": "single",
  "link": "string",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "state": "validating",
  "loadState": {
    "status": "pending",
    "loadHost": "string",
    "startedAt": "2025-11-11T13:45:30Z",
    "finishedAt": "2025-11-11T13:45:30Z"
  },
  "sheetname": "string",
  "purgeAfter": "2025-11-11T13:45:30Z",
  "timeToLive": 42,
  "validation": [
    "string"
  ],
  "createdDate": "2025-11-11T13:45:30Z",
  "targetSheet": "string",
  "templateApp": "string",
  "actualRowEst": 42,
  "errorMessage": "string",
  "generatedApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "selectionApp": "string",
  "curRowEstExpr": "string",
  "retentionTime": 42,
  "parentRequestId": "string",
  "templateAppName": "appname",
  "bindingStateHash": 42,
  "generatedAppName": "appname",
  "selectionAppName": "appname",
  "curRowEstLowBound": 42,
  "curRowEstHighBound": 42,
  "selectionStateHash": 42
}
```

---

### POST /api/analytics/odag-requests/{requestId}/rename-app

Renames a generated Analytics Application. Only the request owner or ODAG link creator can rename generated Analytics Applications.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the request. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appName` | string | Yes | The new name of the generated Analytics Application. |

#### Responses

##### 200

Successful response. Returns the updated request state.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 403

Insufficient privilege to rename the generated Analytics Application. User must be either owner of the request or the ODAG link.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID or generated Analytics Application not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/odag-requests/{requestId}/rename-app` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}/rename-app',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ appName: 'string' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/odag-requests/{requestId}/rename-app yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}/rename-app" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"appName":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "kind": "single",
  "link": "string",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "state": "validating",
  "loadState": {
    "status": "pending",
    "loadHost": "string",
    "startedAt": "2025-11-11T13:45:30Z",
    "finishedAt": "2025-11-11T13:45:30Z"
  },
  "sheetname": "string",
  "purgeAfter": "2025-11-11T13:45:30Z",
  "timeToLive": 42,
  "validation": [
    "string"
  ],
  "createdDate": "2025-11-11T13:45:30Z",
  "targetSheet": "string",
  "templateApp": "string",
  "actualRowEst": 42,
  "errorMessage": "string",
  "generatedApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "selectionApp": "string",
  "curRowEstExpr": "string",
  "retentionTime": 42,
  "parentRequestId": "string",
  "templateAppName": "appname",
  "bindingStateHash": 42,
  "generatedAppName": "appname",
  "selectionAppName": "appname",
  "curRowEstLowBound": 42,
  "curRowEstHighBound": 42,
  "selectionStateHash": 42
}
```

---

### GET /api/analytics/odag-requests/{requestId}/selections

Retrieves the selection state (selected and optional field values) that was active when the Analytics Application generation request was submitted.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestId` | string | Yes | The ID of the request. |

#### Responses

##### 200

Successful response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The list of values in the selection state for this field. |
| `selectedSize` | integer | No | The actual number of selected values. Not used for `bindSelectionState`. |
| `selectionAppParamName` | string | Yes | The name of a variable or field that corresponds to one or more bindings having a matching `selectAppParamName` used to generate Analytics Applications. |
| `selectionAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |

<details>
<summary>Properties of `values`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numValue` | string | No |  |
| `strValue` | string | Yes |  |
| `selStatus` | string | Yes | The valid set of selection states that a specific field value can be in. One of: `S` (selected), `O` (optional), or `X` (excluded). Enum: "S", "O", "X" |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid request ID.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-requests/{requestId}/selections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-requests/{requestId}/selections',
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
# qlik-cli has not implemented support for GET /api/analytics/odag-requests/{requestId}/selections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests/{requestId}/selections" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "values": [
      {
        "numValue": "string",
        "strValue": "string",
        "selStatus": "S"
      }
    ],
    "selectedSize": 42,
    "selectionAppParamName": "string",
    "selectionAppParamType": "Field"
  }
]
```

---
