# Automation connections

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Automation Connections are used by Qlik Automate connectors during automation execution.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/automation-connections`](#get-apiv1automation-connections) | Retrieves a list of automation connections the requesting user has access to. |
| `POST` | [`/api/v1/automation-connections`](#post-apiv1automation-connections) | Creates a new connection object from an automation connector. |
| `GET` | [`/api/v1/automation-connections/{id}`](#get-apiv1automation-connectionsid) | Returns details about the specified automation connection. |
| `PUT` | [`/api/v1/automation-connections/{id}`](#put-apiv1automation-connectionsid) | Updates the specified properties of an automation connection. |
| `DELETE` | [`/api/v1/automation-connections/{id}`](#delete-apiv1automation-connectionsid) | Deletes the specified automation connection. |
| `POST` | [`/api/v1/automation-connections/{id}/actions/change-owner`](#post-apiv1automation-connectionsidactionschange-owner) | Changes the owner of an automation connection by specifying a new owner. |
| `POST` | [`/api/v1/automation-connections/{id}/actions/change-space`](#post-apiv1automation-connectionsidactionschange-space) | Changes the space of an automation connection by specifying a new space. |
| `POST` | [`/api/v1/automation-connections/{id}/actions/check`](#post-apiv1automation-connectionsidactionscheck) | Tries to validate and checks the connection status of an automation connection. |

## API Reference

### GET /api/v1/automation-connections

Retrieves a list of automation connections the requesting user has access to.

- **Replaced by:** "GET:/workflows/automation-connections"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | string | No | Pagination cursor returned from a previous request. |
| `filter` | string | No | Filters the result based on the specified criteria: name, connectorId, ownerId, or spaceId. |
| `limit` | integer | No | The number of automation connections to retrieve. |
| `listAll` | boolean | No | When true, list all connections. Restricted to tenant admins and analytics admins. |
| `sort` | string | No | The field to sort by, with +- prefix indicating sort order. (`?sort=-name` => sort on the `name` field using descending order). Enum: "id", "name", "createdAt", "updatedAt", "+id", "+name", "+createdAt", "+updatedAt", "-id", "-name", "-createdAt", "-updatedAt" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of an automation connection. |
| `name` | string | No | The name of an automation connection. |
| `ownerId` | string | No | The unique identifier of the owner of the automation connection. |
| `spaceId` | string | No | The space ID of the automation connection. |
| `createdAt` | string | No | The timestamp when the automation connection is created. |
| `updatedAt` | string | No | The timestamp when the automation connection is updated. |
| `connectorId` | string | No | The unique identifier of the connector the automation connection is created from. |
| `isConnected` | boolean | No | Returns true if the automtion connection is connected. |

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
| `href` | string | No | The URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automation-connections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections',
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
# qlik-cli has not implemented support for GET /api/v1/automation-connections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
      "name": "auto conn",
      "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
      "spaceId": "5f0f78b239ff4f0001234567",
      "createdAt": "2021-12-23T12:28:21.000000Z",
      "updatedAt": "2021-12-23T12:28:21.000000Z",
      "connectorId": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
      "isConnected": true
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

### POST /api/v1/automation-connections

Creates a new connection object from an automation connector.

- **Replaced by:** "POST:/workflows/automation-connections"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The automation object to create.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of the created automation connection. |
| `params` | object[] | No |  |
| `spaceId` | string | No | The unique identifier of the space in which the automation connection is created. |
| `connectorId` | string | Yes | The unique identifier of the connector from which the automation connection is created. |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of the automation connection parameter. |
| `value` | string | No | The value of the automation connection parameter option. |

</details>

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection. |
| `name` | string | No | The name of the automation connection. |
| `error` | object | No | This contains the error message if a connection is being created with an issue. |
| `params` | object[] | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation connection. |
| `spaceId` | string | No | The space ID of the automation connection. |
| `redirect` | string | No | The redirect of the OAuth account. |
| `createdAt` | string | No | The timestamp when the automation connection was created. |
| `updatedAt` | string | No | The timestamp when the automation connection was updated. |
| `connectorId` | string | No | The unique identifier of the automation connector. |
| `isConnected` | boolean | No | The connection status of the automation connection. When true, the automation connection is connected. |
| `oauthAccountName` | string | No | The name of the OAuth account associated with the automation connection. |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter. |
| `meta` | undefined[] | No | The metadata of the automation connection parameter. |
| `name` | string | No | The name of the automation connection parameter. |
| `order` | integer | No | The order that the automation connection configuration fields should be displayed in. |
| `value` | string | No | The value of the automation connection parameter. |
| `fieldType` | string | No | The field type of the automation connection parameter. |
| `isOptional` | boolean | No | When true, the parameter is optional. |
| `exampleValue` | string | No | The example value of the automation connection parameter. |
| `paramOptions` | object[] | No |  |
| `documentation` | string | No | The documentation of the automation connection parameter. |

<details>
<summary>Properties of `paramOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter option. |
| `value` | string | No | The value of the automation connection parameter option. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automation-connections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'connection',
      params: [
        { name: 'username', value: 'string' },
      ],
      spaceId: '5f0f78b239ff4f0001234567',
      connectorId:
        '3004e850-1985-11ee-b6df-8d800b305320',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automation-connections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"connection","params":[{"name":"username","value":"string"}],"spaceId":"5f0f78b239ff4f0001234567","connectorId":"3004e850-1985-11ee-b6df-8d800b305320"}'
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "connection",
  "error": {},
  "params": [
    {
      "id": "39a90780-8874-11ee-b16c-89512345678",
      "meta": [],
      "name": "region",
      "order": 1,
      "value": "string",
      "fieldType": "enum",
      "isOptional": "false",
      "exampleValue": "string",
      "paramOptions": [
        {
          "id": "39a90780-8874-11ee-b16c-89512345678",
          "value": "string"
        }
      ],
      "documentation": "string"
    }
  ],
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "spaceId": "5f0f78b239ff4f0001234567",
  "redirect": "string",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "connectorId": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "isConnected": true,
  "oauthAccountName": "oauth"
}
```

---

### GET /api/v1/automation-connections/{id}

Returns details about the specified automation connection.

- **Replaced by:** "GET:/workflows/automation-connections/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection. |
| `name` | string | No | The name of the automation connection. |
| `error` | object | No | This contains the error message if a connection is being created with an issue. |
| `params` | object[] | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation connection. |
| `spaceId` | string | No | The space ID of the automation connection. |
| `redirect` | string | No | The redirect of the OAuth account. |
| `createdAt` | string | No | The timestamp when the automation connection was created. |
| `updatedAt` | string | No | The timestamp when the automation connection was updated. |
| `connectorId` | string | No | The unique identifier of the automation connector. |
| `isConnected` | boolean | No | The connection status of the automation connection. When true, the automation connection is connected. |
| `oauthAccountName` | string | No | The name of the OAuth account associated with the automation connection. |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter. |
| `meta` | undefined[] | No | The metadata of the automation connection parameter. |
| `name` | string | No | The name of the automation connection parameter. |
| `order` | integer | No | The order that the automation connection configuration fields should be displayed in. |
| `value` | string | No | The value of the automation connection parameter. |
| `fieldType` | string | No | The field type of the automation connection parameter. |
| `isOptional` | boolean | No | When true, the parameter is optional. |
| `exampleValue` | string | No | The example value of the automation connection parameter. |
| `paramOptions` | object[] | No |  |
| `documentation` | string | No | The documentation of the automation connection parameter. |

<details>
<summary>Properties of `paramOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter option. |
| `value` | string | No | The value of the automation connection parameter option. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automation-connections/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/automation-connections/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "connection",
  "error": {},
  "params": [
    {
      "id": "39a90780-8874-11ee-b16c-89512345678",
      "meta": [],
      "name": "region",
      "order": 1,
      "value": "string",
      "fieldType": "enum",
      "isOptional": "false",
      "exampleValue": "string",
      "paramOptions": [
        {
          "id": "39a90780-8874-11ee-b16c-89512345678",
          "value": "string"
        }
      ],
      "documentation": "string"
    }
  ],
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "spaceId": "5f0f78b239ff4f0001234567",
  "redirect": "string",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "connectorId": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "isConnected": true,
  "oauthAccountName": "oauth"
}
```

---

### PUT /api/v1/automation-connections/{id}

Updates the specified properties of an automation connection.

- **Replaced by:** "PUT:/workflows/automation-connections/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Request Body

**Required**

The automation connection object to update.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The new name of the automation connection to be renamed to. |
| `params` | object[] | No |  |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter option. |
| `value` | string | No | The value of the automation connection parameter option. |

</details>

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection. |
| `name` | string | No | The name of the automation connection. |
| `error` | object | No | This contains the error message if a connection is being created with an issue. |
| `params` | object[] | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation connection. |
| `spaceId` | string | No | The space ID of the automation connection. |
| `redirect` | string | No | The redirect of the OAuth account. |
| `createdAt` | string | No | The timestamp when the automation connection was created. |
| `updatedAt` | string | No | The timestamp when the automation connection was updated. |
| `connectorId` | string | No | The unique identifier of the automation connector. |
| `isConnected` | boolean | No | The connection status of the automation connection. When true, the automation connection is connected. |
| `oauthAccountName` | string | No | The name of the OAuth account associated with the automation connection. |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter. |
| `meta` | undefined[] | No | The metadata of the automation connection parameter. |
| `name` | string | No | The name of the automation connection parameter. |
| `order` | integer | No | The order that the automation connection configuration fields should be displayed in. |
| `value` | string | No | The value of the automation connection parameter. |
| `fieldType` | string | No | The field type of the automation connection parameter. |
| `isOptional` | boolean | No | When true, the parameter is optional. |
| `exampleValue` | string | No | The example value of the automation connection parameter. |
| `paramOptions` | object[] | No |  |
| `documentation` | string | No | The documentation of the automation connection parameter. |

<details>
<summary>Properties of `paramOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the automation connection parameter option. |
| `value` | string | No | The value of the automation connection parameter option. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/automation-connections/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'connection',
      params: [
        {
          id: '39a90780-8874-11ee-b16c-89512345678',
          value: 'string',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/automation-connections/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"connection","params":[{"id":"39a90780-8874-11ee-b16c-89512345678","value":"string"}]}'
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "connection",
  "error": {},
  "params": [
    {
      "id": "39a90780-8874-11ee-b16c-89512345678",
      "meta": [],
      "name": "region",
      "order": 1,
      "value": "string",
      "fieldType": "enum",
      "isOptional": "false",
      "exampleValue": "string",
      "paramOptions": [
        {
          "id": "39a90780-8874-11ee-b16c-89512345678",
          "value": "string"
        }
      ],
      "documentation": "string"
    }
  ],
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "spaceId": "5f0f78b239ff4f0001234567",
  "redirect": "string",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "connectorId": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "isConnected": true,
  "oauthAccountName": "oauth"
}
```

---

### DELETE /api/v1/automation-connections/{id}

Deletes the specified automation connection.

- **Replaced by:** "DELETE:/workflows/automation-connections/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `forced` | boolean | No | When true, the automation connection will be deleted regardless of its usage by any automations. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/automation-connections/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/automation-connections/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automation-connections/{id}/actions/change-owner

Changes the owner of an automation connection by specifying a new owner.

- **Replaced by:** "POST:/workflows/automation-connections/{id}/actions/change-owner"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Request Body

**Required**

The new owner of the automation connection.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | No | The unique identifier of the new owner. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automation-connections/{id}/actions/change-owner` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}/actions/change-owner',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      userId: 'sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automation-connections/{id}/actions/change-owner yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}/actions/change-owner" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"userId":"sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy"}'
```

---

### POST /api/v1/automation-connections/{id}/actions/change-space

Changes the space of an automation connection by specifying a new space.

- **Replaced by:** "POST:/workflows/automation-connections/{id}/actions/change-space"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Request Body

**Required**

The new space of the automation connection.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | No | The unique identifier of the new space. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automation-connections/{id}/actions/change-space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}/actions/change-space',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      spaceId: '5f0f78b239ff4f0001234567',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automation-connections/{id}/actions/change-space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}/actions/change-space" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"spaceId":"5f0f78b239ff4f0001234567"}'
```

---

### POST /api/v1/automation-connections/{id}/actions/check

Tries to validate and checks the connection status of an automation connection.

- **Replaced by:** "POST:/workflows/automation-connections/{id}/actions/check"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation connection. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connected` | boolean | No | The connection status of the automation connection. When true, the automation connection is connected. |
| `is_connected` | boolean | No | The connection status of the automation connection. When true, the automation connection is connected. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automation-connections/{id}/actions/check` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connections/{id}/actions/check',
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
# qlik-cli has not implemented support for POST /api/v1/automation-connections/{id}/actions/check yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections/{id}/actions/check" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "connected": true,
  "is_connected": true
}
```

---
