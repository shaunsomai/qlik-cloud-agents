# Web notifications

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Web notifications is the resource representing a user's notification

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/web-notifications`](#get-apiv1web-notifications) |  |
| `GET` | [`/api/v1/web-notifications/{notificationId}`](#get-apiv1web-notificationsnotificationid) |  |
| `PATCH` | [`/api/v1/web-notifications/{notificationId}`](#patch-apiv1web-notificationsnotificationid) |  |
| `DELETE` | [`/api/v1/web-notifications/{notificationId}`](#delete-apiv1web-notificationsnotificationid) |  |
| `PATCH` | [`/api/v1/web-notifications/all`](#patch-apiv1web-notificationsall) |  |
| `DELETE` | [`/api/v1/web-notifications/all`](#delete-apiv1web-notificationsall) |  |

## API Reference

### GET /api/v1/web-notifications

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | number | No | The number of notification entries to retrieved. |
| `page` | number | No | Page number |
| `read` | boolean | No | Read status of the notification |
| `resourceType` | string | No | Filter by resource types. If passing more than 1 resource type, use comma seperated string. |
| `sort` | string | No | The field to sort by, with +/- prefix indicating sort order Enum: "+createdAt", "-createdAt", "+updatedAt", "-updatedAt" |

#### Responses

##### 200

An array of notification objects

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `meta` | object | No | Notifications meta data |
| `links` | object | No | Notifications links |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `body` | string | Yes |  |
| `meta` | object | Yes |  |
| `read` | boolean | Yes |  |
| `action` | string | No |  |
| `userId` | string | Yes |  |
| `spaceId` | string | No |  |
| `tenantId` | string | No |  |
| `createdAt` | string | Yes |  |
| `spaceType` | string | No |  |
| `updatedAt` | string | Yes |  |
| `resourceId` | string | No |  |
| `resourceType` | string | No |  |
| `subResourceType` | string | No |  |

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unreadCount` | number | No | The total number of unread notification. |

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

Invalid request parameters for querying users.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/web-notifications` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications',
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
# qlik-cli has not implemented support for GET /api/v1/web-notifications yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "body": "string",
      "meta": {},
      "read": true,
      "action": "string",
      "userId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "createdAt": "string",
      "spaceType": "string",
      "updatedAt": "string",
      "resourceId": "string",
      "resourceType": "string",
      "subResourceType": "string"
    }
  ],
  "meta": {
    "unreadCount": 0
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

### GET /api/v1/web-notifications/{notificationId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `notificationId` | string | Yes | The id of the notification to retrieve. |

#### Responses

##### 200

Successfully got notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `body` | string | Yes |  |
| `meta` | object | Yes |  |
| `read` | boolean | Yes |  |
| `action` | string | No |  |
| `userId` | string | Yes |  |
| `spaceId` | string | No |  |
| `tenantId` | string | No |  |
| `createdAt` | string | Yes |  |
| `spaceType` | string | No |  |
| `updatedAt` | string | Yes |  |
| `resourceId` | string | No |  |
| `resourceType` | string | No |  |
| `subResourceType` | string | No |  |

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Not found when user tries to get notification they do not own.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/web-notifications/{notificationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications/{notificationId}',
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
# qlik-cli has not implemented support for GET /api/v1/web-notifications/{notificationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications/{notificationId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "body": "string",
  "meta": {},
  "read": true,
  "action": "string",
  "userId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "string",
  "spaceType": "string",
  "updatedAt": "string",
  "resourceId": "string",
  "resourceType": "string",
  "subResourceType": "string"
}
```

---

### PATCH /api/v1/web-notifications/{notificationId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `notificationId` | string | Yes | The id of the notification to update. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/read" |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 204

Successfully patched marked notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unreadCount` | number | No | The total number of unread notification. |

##### 400

Unsupported patch request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Notification not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/web-notifications/{notificationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications/{notificationId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/read',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/web-notifications/{notificationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications/{notificationId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/read","value":true}]'
```

**Example Response:**

```json
{
  "unreadCount": 0
}
```

---

### DELETE /api/v1/web-notifications/{notificationId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `notificationId` | string | Yes | The id of the notification to delete. |

#### Responses

##### 204

Successfully deleted notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unreadCount` | number | No | The total number of unread notification. |

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Notification not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/web-notifications/{notificationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications/{notificationId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/web-notifications/{notificationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications/{notificationId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "unreadCount": 0
}
```

---

### PATCH /api/v1/web-notifications/all

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/read" |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 204

Successfully marked all notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unreadCount` | number | No | The total number of unread notification. |

##### 400

Unsupported patch request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/web-notifications/all` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications/all',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/read',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/web-notifications/all yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications/all" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/read","value":true}]'
```

**Example Response:**

```json
{
  "unreadCount": 0
}
```

---

### DELETE /api/v1/web-notifications/all

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 204

Successfully deleted notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unreadCount` | number | No | The total number of unread notification. |

##### 401

Unauthorized request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `status` | integer | No | The HTTP status code. |
| `message` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/web-notifications/all` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/web-notifications/all',
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
# qlik-cli has not implemented support for DELETE /api/v1/web-notifications/all yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications/all" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "unreadCount": 0
}
```

---
