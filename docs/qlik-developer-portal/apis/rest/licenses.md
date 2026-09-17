# Licenses

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Licenses define tenant and user entitlements, and can be used in conjunction with the consumption API to get a picture of entitlement usage.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/licenses/assignments`](#get-apiv1licensesassignments) |  |
| `POST` | [`/api/v1/licenses/assignments/actions/add`](#post-apiv1licensesassignmentsactionsadd) |  |
| `POST` | [`/api/v1/licenses/assignments/actions/delete`](#post-apiv1licensesassignmentsactionsdelete) |  |
| `POST` | [`/api/v1/licenses/assignments/actions/update`](#post-apiv1licensesassignmentsactionsupdate) |  |
| `GET` | [`/api/v1/licenses/consumption`](#get-apiv1licensesconsumption) |  |
| `GET` | [`/api/v1/licenses/overview`](#get-apiv1licensesoverview) |  |
| `GET` | [`/api/v1/licenses/settings`](#get-apiv1licensessettings) |  |
| `PUT` | [`/api/v1/licenses/settings`](#put-apiv1licensessettings) |  |
| `GET` | [`/api/v1/licenses/status`](#get-apiv1licensesstatus) |  |

## API Reference

### GET /api/v1/licenses/assignments

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The filter for finding entries. |
| `limit` | integer | No | The preferred number of entries to return. |
| `orphans` | boolean | No | Only return assignments which are 'orphans' in the current tenant. |
| `page` | string | No | The requested page. |
| `sort` | string | No | The field to sort on; can be prefixed with +/- for ascending/descending sort order. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Responses

##### 200

List of assignments.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Allotment type |
| `excess` | boolean | Yes | Assignment excess status. |
| `created` | string | Yes | Assignment created date. |
| `subject` | string | Yes | Subject |

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
| `href` | string | No | link |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | link |

</details>

</details>

##### 400

Bad request, invalid query.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/licenses/assignments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/assignments',
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
# qlik-cli has not implemented support for GET /api/v1/licenses/assignments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/assignments" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "type": "analyzer",
      "excess": false,
      "created": "2020-12-03T09:24:48.114Z",
      "subject": "qlik\\kalle"
    },
    {
      "type": false,
      "created": "2020-12-03T09:24:48.114Z",
      "subject": "qlik\\nalle"
    }
  ],
  "links": {
    "next": {
      "href": "http://license/v1/licenses/assignments?limit=4&page=bmV4dDpGZ0FBQUFkZmFXUUFYOHBUcTlpM1U4UU1YWHZrQUE%3D"
    },
    "prev": {
      "href": "http://license/v1/licenses/assignments?limit=4&page=cHJldjpGZ0FBQUFkZmFXUUFYOHBUcTlpM1U4UU1YWHZ0QUE%3D"
    }
  }
}
```

---

### POST /api/v1/licenses/assignments/actions/add

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Request Body

**Required**

List of subjects to allocate assignments for.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `add` | object[] | Yes |  |

<details>
<summary>Properties of `add`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | _(deprecated)_ User name |
| `type` | string | Yes | Allotment type |
| `userId` | string | No | _(deprecated)_ User ID |
| `subject` | string | Yes | User subject |

</details>

#### Responses

##### 207

Processed. (The status of the individual assignments is found in the response body)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code |
| `type` | string | No | Allotment type |
| `title` | string | No | Error title |
| `status` | integer | Yes | Response status |
| `subject` | string | Yes | Subject |

</details>

##### 400

Body is invalid or missing.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/licenses/assignments/actions/add` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/assignments/actions/add',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      add: [
        {
          type: 'professional',
          subject: 'qlik\\kalle',
        },
        {
          type: 'analyzer',
          subject: 'qlik\\nalle',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/licenses/assignments/actions/add yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/assignments/actions/add" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"add":[{"type":"professional","subject":"qlik\\kalle"},{"type":"analyzer","subject":"qlik\\nalle"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "type": "professional",
      "status": 201,
      "subject": "qlik\\kalle"
    },
    {
      "code": "LICENSES-011",
      "type": "analyzer",
      "title": "No available allotment error, No available allotment.",
      "status": 403,
      "subject": "qlik\\nalle"
    }
  ]
}
```

---

### POST /api/v1/licenses/assignments/actions/delete

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Request Body

**Required**

List of assignments to delete.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `delete` | object[] | Yes |  |

<details>
<summary>Properties of `delete`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Allotment type |
| `subject` | string | Yes | User subject |

</details>

#### Responses

##### 207

Processed. (The status of the individual assignments is found in the response body)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code |
| `type` | string | No | Allotment type |
| `title` | string | No | Error title |
| `status` | integer | Yes | Response status |
| `subject` | string | No | Subject |

</details>

##### 400

Body is invalid or missing.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/licenses/assignments/actions/delete` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/assignments/actions/delete',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      delete: [
        {
          type: 'analyzer',
          subject: 'qlik\\malik',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/licenses/assignments/actions/delete yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/assignments/actions/delete" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"delete":[{"type":"analyzer","subject":"qlik\\malik"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "type": "professional",
      "status": 200,
      "subject": "qlik\\malik"
    },
    {
      "code": "LICENSES-016",
      "type": "analyzer",
      "title": "Assignment not found.",
      "status": 404,
      "subject": "qlik\\no"
    }
  ]
}
```

---

### POST /api/v1/licenses/assignments/actions/update

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Request Body

**Required**

List of assignments to update.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `update` | object[] | Yes |  |

<details>
<summary>Properties of `update`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Target assignment type. |
| `subject` | string | Yes | User subject, the current or the desired after the patch. |
| `sourceType` | string | No | Current assignment type. |
| `sourceSubject` | string | No | The current user subject, in case that should be patched. |

</details>

#### Responses

##### 207

Processed. (The status of the individual assignments is found in the response body)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code |
| `type` | string | No | Target allotment type. |
| `title` | string | No | Error title |
| `status` | integer | Yes | HTTP status code indicating the result of the individual assignment operation. A value of 200 represents a successful update, while 201 indicates a new resource was created due to a subject update. Any 400-level status codes indicate an error. |
| `subject` | string | No | Target subject. |
| `sourceType` | string | No | Current allotment type. |
| `sourceSubject` | string | No | Current subject. |

</details>

##### 400

Body is invalid or missing.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/licenses/assignments/actions/update` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/assignments/actions/update',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      update: [
        {
          type: 'professional',
          subject: 'qlik\\malik',
          sourceType: 'analyzer',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/licenses/assignments/actions/update yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/assignments/actions/update" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"update":[{"type":"professional","subject":"qlik\\malik","sourceType":"analyzer"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "type": "professional",
      "status": 200,
      "subject": "qlik\\malik",
      "sourceType": "analyzer"
    },
    {
      "code": "LICENSES-016",
      "title": "Assignment not found.",
      "status": 404,
      "subject": "qlik/sara",
      "sourceType": "analyzer"
    }
  ]
}
```

---

### GET /api/v1/licenses/consumption

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The SCIM filter for the query. Filterable property is "endTime". |
| `limit` | integer | No | The preferred number of entries to return. |
| `page` | string | No | The requested page. |
| `sort` | string | No | The field to sort on; can be prefixed with +/- for ascending/descending sort order. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Responses

##### 200

Successful

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID |
| `appId` | string | No | App ID |
| `userId` | string | No | User ID |
| `endTime` | string | No | Engine session end time. |
| `duration` | string | No | Engine session duration. |
| `sessionId` | string | No | Engine session ID. |
| `allotmentId` | string | No | Allotment ID |
| `minutesUsed` | integer | No | Analyzer capacity minutes consumed. |
| `capacityUsed` | integer | No | Analyzer capacity chunks consumed. |
| `licenseUsage` | string | No | License usage |

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
| `href` | string | No | link |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | link |

</details>

</details>

##### 400

Bad request, malformed query.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/licenses/consumption` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/consumption',
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
# qlik-cli has not implemented support for GET /api/v1/licenses/consumption yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/consumption" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "appId": "string",
      "userId": "string",
      "endTime": "string",
      "duration": "string",
      "sessionId": "string",
      "allotmentId": "string",
      "minutesUsed": 42,
      "capacityUsed": 42,
      "licenseUsage": "string"
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    }
  }
}
```

---

### GET /api/v1/licenses/overview

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token. |

#### Responses

##### 200

Licenses overview info.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trial` | boolean | Yes | Boolean indicating if it is a trial license. |
| `valid` | string | Yes | Period that the license is currently set to be active. Represented as an ISO 8601 time interval with start and end. |
| `origin` | string | Yes | Origin of license key. Enum: "Internal", "External" |
| `status` | string | Yes | Enum with status of license. Only status Ok grants license. access. Enum: "Ok", "Blacklisted", "Expired" |
| `product` | string | Yes | The product the license is valid for. |
| `updated` | string | Yes | An ISO 8601 timestamp for when the license was last updated. |
| `version` | string | Yes | The version of the license definition, used to track whether changes have propagated. Typically a content hash; its exact form depends on the origin. |
| `allotments` | object[] | Yes |  |
| `changeTime` | string | No | An ISO 8601 timestamp for when the license was last changed. |
| `customerId` | string | No | Customer ID |
| `licenseKey` | string | Yes |  |
| `parameters` | object[] | Yes | The license parameters. |
| `licenseType` | string | No |  |
| `licenseNumber` | string | Yes |  |
| `latestValidTime` | string | No | An ISO 8601 timestamp for when the latest time the license has been known to be valid, a missing value indicates the indefinite future. |
| `secondaryNumber` | string | Yes | The secondary number of a definition. |
| `capabilityBankId` | string | No | the capability bank id |
| `parentLicenseNumber` | string | No | the parent number of the license. can be shared by multiple license numbers |

<details>
<summary>Properties of `allotments`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Enum: "professional", "analyzer", "analyzer_time" |
| `units` | integer | Yes |  |
| `overage` | integer | No | Overage value; -1 means unbounded overage. |
| `unitsUsed` | integer | Yes |  |
| `usageClass` | string | Yes |  |

</details>

<details>
<summary>Properties of `parameters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Parameter set (provision) name. |
| `valid` | string | Yes | Time interval for parameter validity. |
| `access` | object | No | Parameters for licenses to control access to the parameters. |
| `values` | object | No | Parameter values |

<details>
<summary>Properties of `access`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `allotment` | string | No | Name of an allotment that the user must have access to. to |

</details>

</details>

##### 400

invalid tenant

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 404

License not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/licenses/overview` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/overview',
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
# qlik-cli has not implemented support for GET /api/v1/licenses/overview yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/overview" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "trial": false,
  "valid": "2018-01-01/2018-12-31",
  "origin": "Internal",
  "status": "Ok",
  "product": "Qlik Sense Enterprise SaaS",
  "version": "A1B2-C3D4-E5F6-G7H8-J9K0",
  "allotments": [
    {
      "name": "analyzer_time",
      "units": 300,
      "overage": 100,
      "unitsUsed": 242,
      "usageClass": "time"
    },
    {
      "name": "professional",
      "units": 200,
      "unitsUsed": 15,
      "usageClass": "assigned"
    }
  ],
  "licenseKey": "hejhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IktFWTEifQ.eyJqdGkiOiIxZjZkZTc0Zi04MDcyLTRjMTQtYjc1OS02ZjlkYmJmYWM5MjAiLCJsaWNlbnNlIjoiOTk5OTAwMDAwMDAwMTIzNCJ9.fwa6l6gY1MR_Ja2OMnV65V68fbzQYW5OAKUFnLfG9oZjNAbjhdDkZvS2S2zHaBnSrSva1ARh5iq_S0KTBOKKcJJDTb7jRVURyaAvbCuBDk_0ITrUudHaT9U_Mc9EKkfT8mR6vthhZxVzEhyYPFS7gDw7M6bav2ntpDsoJFPgous",
  "parameters": [
    {
      "name": "qlikAlerting",
      "valid": "./.",
      "values": {
        "saas_alerting": "FULL"
      }
    }
  ],
  "licenseNumber": "9999000000001204",
  "secondaryNumber": "12345"
}
```

---

### GET /api/v1/licenses/settings

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Responses

##### 200

Auto assign settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `autoAssignAnalyzer` | boolean | No | If analyzer users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |
| `autoAssignProfessional` | boolean | No | If professional users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |

##### 400

Missing or invalid tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Not allowed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/licenses/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/settings',
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
# qlik-cli has not implemented support for GET /api/v1/licenses/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "autoAssignAnalyzer": true,
  "autoAssignProfessional": false
}
```

---

### PUT /api/v1/licenses/settings

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Request Body

Dynamic assignment settings for professional and analyzer users. If professional users and analyzer users are both set, professional users will be automatically assigned, if available. Otherwise, analyzer users will be assigned. If neither of those users are available, analyzer capacity will be assigned, if available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `autoAssignAnalyzer` | boolean | No | If analyzer users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |
| `autoAssignProfessional` | boolean | No | If professional users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |

#### Responses

##### 200

Auto assign settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `autoAssignAnalyzer` | boolean | No | If analyzer users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |
| `autoAssignProfessional` | boolean | No | If professional users are available, they will be automatically assigned. Otherwise, analyzer capacity will be assigned, if available. |

##### 400

Missing or invalid tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Action not allowed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 403

Insufficient access

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/licenses/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      autoAssignAnalyzer: true,
      autoAssignProfessional: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/licenses/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"autoAssignAnalyzer":true,"autoAssignProfessional":false}'
```

**Example Response:**

```json
{
  "autoAssignAnalyzer": true,
  "autoAssignProfessional": false
}
```

---

### GET /api/v1/licenses/status

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authorization` | string | No | Authentication token |

#### Responses

##### 200

License status info.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Type of license key. Enum: "Signed", "Plain", "2.0" |
| `trial` | boolean | Yes | Boolean indicating if it is a trial license. |
| `valid` | string | Yes | Period that the license is currently set to be active. Represented as an ISO 8601 time interval with start and end. |
| `origin` | string | Yes | Origin of license key. Enum: "Internal", "External" |
| `status` | string | Yes | Enum with status of license. Only status Ok grants license. access. Enum: "Ok", "Blacklisted", "Expired", "Missing" |
| `product` | string | Yes | The product the license is valid for. |
| `deactivated` | boolean | Yes | Boolean indicating if the license is deactivated. |
| `extensionStatus` | string | Yes | Enum with extension status of license. access. Enum: "Unavailable", "Pending", "Available" |

##### 400

invalid tenant

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

##### 401

Unauthorized (invalid token).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | Yes | _(deprecated)_ Error type |
| `errors` | object[] | Yes |  |
| `message` | string | Yes | _(deprecated)_ Error message |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code |
| `title` | string | Yes | Error title |
| `detail` | string | No | Additional error detail. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/licenses/status` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/licenses/status',
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
# qlik-cli has not implemented support for GET /api/v1/licenses/status yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/status" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "type": "Signed",
  "trial": false,
  "valid": "2018-01-01/2018-12-31",
  "origin": "Internal",
  "status": "Ok",
  "product": "Qlik Sense Business",
  "extensionStatus": "Unavailable"
}
```

---
