# Audits

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Audits provides access to events emitted upon each action taken in your tenant, providing detailed access to what's happening in your tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/audits`](#get-apiv1audits) | Retrieves list of events for subscribed services for your tenant. Stores events for 90 days, after which they can be accessed via `/v1/audits/archive`. |
| `GET` | [`/api/v1/audits/{id}`](#get-apiv1auditsid) | Finds and returns a specific audit events for the given event ID. |
| `POST` | [`/api/v1/audits/actions/fetch-consumption-app`](#post-apiv1auditsactionsfetch-consumption-app) | Returns a Qlik Sense application (QVF file) containing usage data for the tenant's subscription. Requesting user must be assigned the `TenantAdmin` role. Available only for Capacity subscriptions. Consumption report is updated once per day. |
| `GET` | [`/api/v1/audits/archive`](#get-apiv1auditsarchive) | Retrieves audit events from long-term storage. Returns all archived audit events for the specified date and tenant, formatted as a JSON array. |
| `GET` | [`/api/v1/audits/settings`](#get-apiv1auditssettings) | Returns the server configuration options. It includes options that represent the server configuration state and parameters that were used to run the server with certain functionality. |
| `GET` | [`/api/v1/audits/sources`](#get-apiv1auditssources) | Finds and returns the list of possible event sources for this tenant. |
| `GET` | [`/api/v1/audits/types`](#get-apiv1auditstypes) | Finds and returns the list of possible event types for this tenant. |

## API Reference

### GET /api/v1/audits

Retrieves list of events for subscribed services for your tenant. Stores events for 90 days, after which they can be accessed via `/v1/audits/archive`.

- **Rate Limit:** Special (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTime` | string | No | The start/end time interval formatted in ISO 8601 to search by eventTime. For example, "?eventTime=2021-07-14T18:41:15.00Z/2021-07-14T18:41:15.99Z". |
| `eventType` | string | No | The case-sensitive string used to search by eventType. Retrieve a list of possible eventTypes with `/v1/audits/types`. |
| `id` | string | No | The comma separated list of audit unique identifiers. |
| `limit` | integer | No | The maximum number of resources to return for a request. |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |
| `sort` | string | No | The property of a resource to sort on (default sort is -eventTime). The supported properties are source, eventType, and eventTime. A property must be prefixed by + or - to indicate ascending or descending sort order respectively. |
| `source` | string | No | The case-sensitive string used to search by source. Retrieve a list of possible sources with `/v1/audits/sources`. |
| `userId` | string | No | The case-sensitive string used to search by userId. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | List of audit items. |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The resource item's unique identifier. |
| `data` | object | No | Additional information about the event's details. The structure depends on the type and version of the event. |
| `links` | object | No |  |
| `source` | string | No | The source of the event message, usually the producing service. |
| `userId` | string | No | The ID of the user who performed the action that triggered the event. |
| `eventId` | string | No | The event's unique identifier. |
| `tenantId` | string | No | The ID of the tenant that owns the item. This is populated using the JWT. |
| `eventTime` | string | No | The RFC3339 datetime when the event happened. |
| `eventType` | string | No | The type of event that describes committed action. |
| `extensions` | object | No | The availability of the properties depends on the event and the context it was triggered in. |
| `contentType` | string | No | The type that content is encoded in, always "application/json". |
| `eventTypeVersion` | string | No | The version of the event type. |

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

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | object | No | Specifies the entity performing the action on behalf of another party listed as triggering the action. |
| `ownerId` | string | No | Id of the owner of the resource affected by the eventContext. |
| `spaceId` | string | No | Id of the space related to the action performed on the eventContext. |
| `updates` | any | No | Might be present if the action is of type "updated" and should contain information about the changes made to the resource. |
| `topLevelResourceId` | string | No | If the event originated from a sub resource the topLevelResourceId contains the id of the top level resource associated with the sub resource. |

<details>
<summary>Properties of `actor`</summary>

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

Bad Request

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/audits', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/audits yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "data": {},
      "links": {
        "self": {
          "href": "string"
        }
      },
      "source": "string",
      "userId": "string",
      "eventId": "string",
      "tenantId": "string",
      "eventTime": "2018-10-30T07:06:22Z",
      "eventType": "string",
      "extensions": {
        "actor": {
          "sub": "string",
          "subType": "string"
        },
        "ownerId": "string",
        "spaceId": "string",
        "topLevelResourceId": "string"
      },
      "contentType": "string",
      "eventTypeVersion": "string"
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

### GET /api/v1/audits/{id}

Finds and returns a specific audit events for the given event ID.

- **Rate Limit:** Special (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The audit item's unique identifier. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The resource item's unique identifier. |
| `data` | object | No | Additional information about the event's details. The structure depends on the type and version of the event. |
| `links` | object | No |  |
| `source` | string | No | The source of the event message, usually the producing service. |
| `userId` | string | No | The ID of the user who performed the action that triggered the event. |
| `eventId` | string | No | The event's unique identifier. |
| `tenantId` | string | No | The ID of the tenant that owns the item. This is populated using the JWT. |
| `eventTime` | string | No | The RFC3339 datetime when the event happened. |
| `eventType` | string | No | The type of event that describes committed action. |
| `extensions` | object | No | The availability of the properties depends on the event and the context it was triggered in. |
| `contentType` | string | No | The type that content is encoded in, always "application/json". |
| `eventTypeVersion` | string | No | The version of the event type. |

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

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | object | No | Specifies the entity performing the action on behalf of another party listed as triggering the action. |
| `ownerId` | string | No | Id of the owner of the resource affected by the eventContext. |
| `spaceId` | string | No | Id of the space related to the action performed on the eventContext. |
| `updates` | any | No | Might be present if the action is of type "updated" and should contain information about the changes made to the resource. |
| `topLevelResourceId` | string | No | If the event originated from a sub resource the topLevelResourceId contains the id of the top level resource associated with the sub resource. |

<details>
<summary>Properties of `actor`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sub` | string | No | Opaque value identifying impersonating entity. |
| `subType` | string | No | The type of the impersonating entity. |

</details>

</details>

##### 400

Bad Request

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

##### 404

Not Found

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/audits/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "data": {},
  "links": {
    "self": {
      "href": "string"
    }
  },
  "source": "string",
  "userId": "string",
  "eventId": "string",
  "tenantId": "string",
  "eventTime": "2018-10-30T07:06:22Z",
  "eventType": "string",
  "extensions": {
    "actor": {
      "sub": "string",
      "subType": "string"
    },
    "ownerId": "string",
    "spaceId": "string",
    "topLevelResourceId": "string"
  },
  "contentType": "string",
  "eventTypeVersion": "string"
}
```

---

### POST /api/v1/audits/actions/fetch-consumption-app

Returns a Qlik Sense application (QVF file) containing usage data for the tenant's subscription. Requesting user must be assigned the `TenantAdmin` role. Available only for Capacity subscriptions. Consumption report is updated once per day.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `*/*` | string | No |  |

##### 400

Bad Request

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

Forbidden.

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

Not Found

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `POST /api/v1/audits/actions/fetch-consumption-app` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/actions/fetch-consumption-app',
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
# qlik-cli has not implemented support for POST /api/v1/audits/actions/fetch-consumption-app yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/actions/fetch-consumption-app" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
"string"
```

---

### GET /api/v1/audits/archive

Retrieves audit events from long-term storage. Returns all archived audit events for the specified date and tenant, formatted as a JSON array.
Archived events are retained for the full lifetime of the tenant, and are not removed or size-limited.


- **Rate Limit:** Special (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `date` | string | Yes | Date to be used as filter and criteria during extraction. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT is used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | List of archived events. The structure of the events depend on their type and version. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Additional information about the event's details. The structure depends on the type and version of the event. |
| `source` | string | No | The source of the event message, usually the producing service. |
| `userId` | string | No | The ID of the user who performed the action that triggered the event. |
| `eventId` | string | No | The event's unique identifier. |
| `tenantId` | string | No | The ID of the tenant that owns the item. This is populated using the JWT. |
| `eventTime` | string | No | The RFC3339 datetime when the event happened. |
| `eventType` | string | No | The type of event that describes committed action. |
| `extensions` | object | No | The availability of the properties depends on the event and the context it was triggered in. |
| `contentType` | string | No | The type that content is encoded in, always "application/json". |
| `eventTypeVersion` | string | No | The version of the event type. |

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | object | No | Specifies the entity performing the action on behalf of another party listed as triggering the action. |
| `ownerId` | string | No | Id of the owner of the resource affected by the eventContext. |
| `spaceId` | string | No | Id of the space related to the action performed on the eventContext. |
| `updates` | any | No | Might be present if the action is of type "updated" and should contain information about the changes made to the resource. |
| `topLevelResourceId` | string | No | If the event originated from a sub resource the topLevelResourceId contains the id of the top level resource associated with the sub resource. |

<details>
<summary>Properties of `actor`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad Request

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

##### 404

Not Found

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits/archive` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/archive',
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
# qlik-cli has not implemented support for GET /api/v1/audits/archive yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/archive" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "data": {},
      "source": "string",
      "userId": "string",
      "eventId": "string",
      "tenantId": "string",
      "eventTime": "2018-10-30T07:06:22Z",
      "eventType": "string",
      "extensions": {
        "actor": {
          "sub": "string",
          "subType": "string"
        },
        "ownerId": "string",
        "spaceId": "string",
        "topLevelResourceId": "string"
      },
      "contentType": "string",
      "eventTypeVersion": "string"
    }
  ]
}
```

---

### GET /api/v1/audits/settings

Returns the server configuration options. It includes options that represent the server configuration state and parameters that were used to run the server with certain functionality.

- **Rate Limit:** Special (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Server configuration options. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `EventTTL` | integer | No | The events TTL in seconds. |
| `ArchiveEnabled` | boolean | No | Is Long Term Storage archiving enabled?. |

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/settings',
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
# qlik-cli has not implemented support for GET /api/v1/audits/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "EventTTL": 42,
    "ArchiveEnabled": true
  }
}
```

---

### GET /api/v1/audits/sources

Finds and returns the list of possible event sources for this tenant.

- **Rate Limit:** Special (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | string[] | No | List of requested resources. |
| `links` | object | No |  |

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits/sources` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/sources',
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
# qlik-cli has not implemented support for GET /api/v1/audits/sources yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/sources" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    "string"
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

### GET /api/v1/audits/types

Finds and returns the list of possible event types for this tenant.

- **Rate Limit:** Special (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | string[] | No | List of requested resources. |
| `links` | object | No |  |

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

##### 500

Internal Server Error

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
// qlik-api has not implemented support for `GET /api/v1/audits/types` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/audits/types',
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
# qlik-cli has not implemented support for GET /api/v1/audits/types yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/audits/types" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    "string"
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
