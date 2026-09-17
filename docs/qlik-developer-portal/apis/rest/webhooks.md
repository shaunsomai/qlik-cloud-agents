# Webhooks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Webhooks are a way for Qlik Cloud to provide other applications with real-time information.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/webhooks`](#get-apiv1webhooks) | Retrieves all webhooks entries for a tenant that the user has access to. Users assigned the `TenantAdmin` role can retrieve all webhooks. A user can have up to 150 webhooks at one time. |
| `POST` | [`/api/v1/webhooks`](#post-apiv1webhooks) | Creates a new webhook. User must be assigned the `TenantAdmin` role to create `tenant` level webhooks. |
| `GET` | [`/api/v1/webhooks/{id}`](#get-apiv1webhooksid) | Returns details for a specific webhook. |
| `PATCH` | [`/api/v1/webhooks/{id}`](#patch-apiv1webhooksid) | Patches a webhook to update one or more properties. |
| `PUT` | [`/api/v1/webhooks/{id}`](#put-apiv1webhooksid) | Updates a webhook, any omitted fields will be cleared, returns updated webhook. |
| `DELETE` | [`/api/v1/webhooks/{id}`](#delete-apiv1webhooksid) | Deletes a specific webhook. |
| `GET` | [`/api/v1/webhooks/{id}/deliveries`](#get-apiv1webhooksiddeliveries) | Returns deliveries for a specific webhook. Delivery history is stored for 1 week. |
| `GET` | [`/api/v1/webhooks/{id}/deliveries/{deliveryId}`](#get-apiv1webhooksiddeliveriesdeliveryid) | Returns details for a specific delivery. |
| `POST` | [`/api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend`](#post-apiv1webhooksiddeliveriesdeliveryidactionsresend) | Resends the delivery with the same payload. |
| `GET` | [`/api/v1/webhooks/event-types`](#get-apiv1webhooksevent-types) | Lists event-types that are possible to subscribe to. |

## API Reference

### GET /api/v1/webhooks

Retrieves all webhooks entries for a tenant that the user has access to. Users assigned the `TenantAdmin` role can retrieve all webhooks. A user can have up to 150 webhooks at one time.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `createdByUserId` | string | No | Filter resources by user that created it. |
| `enabled` | boolean | No | Filter resources by enabled true/false. |
| `eventTypes` | string | No | Filter resources by event-type/types, a single webhook item can have multiple event-types. |
| `level` | string | No | Filter resources by level that user has access to (either user or level). |
| `limit` | number | No | Maximum number of webhooks to retrieve. |
| `name` | string | No | Filter resources by name (wildcard and case insensitive). |
| `next` | string | No | Cursor to the next page. |
| `origins` | string | No | Filter resources by origins, supports multiorigin. Enum: "api", "automations", "management-console" |
| `ownerId` | string | No | Filter resources by user that owns it, only applicable for user level webhooks. |
| `prev` | string | No | Cursor to the previous page. |
| `sort` | string | No | Field to sort by, prefix with -/+ to indicate order. Enum: "name", "+name", "-name", "url", "+url", "-url", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt" |
| `updatedByUserId` | string | No | Filter resources by user that last updated the webhook. |
| `url` | string | No | Filter resources by URL (wildcard and case insensitive). |

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
| `id` | string | No | The webhook's unique identifier. |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `createdAt` | string | No | The UTC timestamp when the webhook was created. |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `disabledReason` | string | No | The reason for the webhook to be disabled. |
| `secretKeyAdded` | boolean | No | Provides status of the string used as secret for calculating HMAC hash sent as header is already added or not. |
| `createdByUserId` | string | No | The id of the user that created the webhook. |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook. |
| `encryptedHeaders` | string[] | No | Additional encrypted headers in the post request. Maximum size: 2048 bytes for encrypted headers. |
| `disabledReasonCode` | string | No | The unique code for the reason. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose. Enum: "api", "automations", "management-console" |

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
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/webhooks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/webhooks', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/webhooks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "url": "string",
      "name": "string",
      "level": "tenant",
      "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
      "enabled": false,
      "headers": {
        "headerName": "headerValue"
      },
      "ownerId": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "updatedAt": "2018-10-30T07:06:22Z",
      "eventTypes": [
        "string"
      ],
      "description": "string",
      "disabledReason": "string",
      "secretKeyAdded": true,
      "createdByUserId": "string",
      "updatedByUserId": "string",
      "encryptedHeaders": [
        "header1",
        "header2"
      ],
      "disabledReasonCode": "string",
      "enableCloudEventDelivery": true,
      "checkCertificateRevocation": false,
      "origin": "api"
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

### POST /api/v1/webhooks

Creates a new webhook. User must be assigned the `TenantAdmin` role to create `tenant` level webhooks.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `secret` | string | No | String used as secret for calculating HMAC hash sent as header. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request (webhook delivery). Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `encryptedHeaders` | object | No | These headers are persisted encrypted and decrypted to be sent as normal headers in post request (webhook delivery), in case of URL change these headers will need to be re-entered. Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for encrypted headers. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose. Enum: "api", "automations", "management-console" |

#### Responses

##### 201

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier. |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `createdAt` | string | No | The UTC timestamp when the webhook was created. |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `disabledReason` | string | No | The reason for the webhook to be disabled. |
| `secretKeyAdded` | boolean | No | Provides status of the string used as secret for calculating HMAC hash sent as header is already added or not. |
| `createdByUserId` | string | No | The id of the user that created the webhook. |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook. |
| `encryptedHeaders` | string[] | No | Additional encrypted headers in the post request. Maximum size: 2048 bytes for encrypted headers. |
| `disabledReasonCode` | string | No | The unique code for the reason. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose. Enum: "api", "automations", "management-console" |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/webhooks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/webhooks', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    url: 'string',
    name: 'string',
    level: 'tenant',
    filter:
      'id eq "id123" or spaceId eq "spaceId123" or spaceId eq "spaceId456" or topLevelResourceId eq "id789"',
    secret: 'string',
    enabled: false,
    headers: { headerName: 'headerValue' },
    ownerId: 'string',
    eventTypes: ['string'],
    description: 'string',
    encryptedHeaders: {
      headerName: 'sensitiveHeaderValue',
    },
    enableCloudEventDelivery: true,
    checkCertificateRevocation: false,
    origin: 'api',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/webhooks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"url":"string","name":"string","level":"tenant","filter":"id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"","secret":"string","enabled":false,"headers":{"headerName":"headerValue"},"ownerId":"string","eventTypes":["string"],"description":"string","encryptedHeaders":{"headerName":"sensitiveHeaderValue"},"enableCloudEventDelivery":true,"checkCertificateRevocation":false,"origin":"api"}'
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "updatedAt": "2018-10-30T07:06:22Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### GET /api/v1/webhooks/{id}

Returns details for a specific webhook.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier. |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `createdAt` | string | No | The UTC timestamp when the webhook was created. |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `disabledReason` | string | No | The reason for the webhook to be disabled. |
| `secretKeyAdded` | boolean | No | Provides status of the string used as secret for calculating HMAC hash sent as header is already added or not. |
| `createdByUserId` | string | No | The id of the user that created the webhook. |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook. |
| `encryptedHeaders` | string[] | No | Additional encrypted headers in the post request. Maximum size: 2048 bytes for encrypted headers. |
| `disabledReasonCode` | string | No | The unique code for the reason. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose. Enum: "api", "automations", "management-console" |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "updatedAt": "2018-10-30T07:06:22Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### PATCH /api/v1/webhooks/{id}

Patches a webhook to update one or more properties.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "add", "remove", "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/name", "/description", "/url", "/eventTypes", "/headers", "/enabled", "/secret", "/encryptedHeaders", "/enableCloudEventDelivery" |
| `value` | boolean \| integer \| object \| string | No | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | integer | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

</details>

#### Responses

##### 204

No Content response.

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: '/description',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/description","value":true}]'
```

---

### PUT /api/v1/webhooks/{id}

Updates a webhook, any omitted fields will be cleared, returns updated webhook.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `secret` | string | No | String used as secret for calculating HMAC hash sent as header. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request (webhook delivery). Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `encryptedHeaders` | object | No | These headers are persisted encrypted and decrypted to be sent as normal headers in post request (webhook delivery), in case of URL change these headers will need to be re-entered. Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for encrypted headers. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier. |
| `url` | string | Yes | Target URL for webhook HTTPS requests. |
| `name` | string | Yes | The name for the webhook. |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests. |
| `headers` | object | No | Additional headers in the post request. Maximum size: 2048 bytes for non-encrypted headers. |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks. |
| `createdAt` | string | No | The UTC timestamp when the webhook was created. |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated. |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/v1/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook. |
| `disabledReason` | string | No | The reason for the webhook to be disabled. |
| `secretKeyAdded` | boolean | No | Provides status of the string used as secret for calculating HMAC hash sent as header is already added or not. |
| `createdByUserId` | string | No | The id of the user that created the webhook. |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook. |
| `encryptedHeaders` | string[] | No | Additional encrypted headers in the post request. Maximum size: 2048 bytes for encrypted headers. |
| `disabledReasonCode` | string | No | The unique code for the reason. |
| `enableCloudEventDelivery` | boolean | No | If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose. Enum: "api", "automations", "management-console" |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      url: 'string',
      name: 'string',
      level: 'tenant',
      filter:
        'id eq "id123" or spaceId eq "spaceId123" or spaceId eq "spaceId456" or topLevelResourceId eq "id789"',
      secret: 'string',
      enabled: false,
      headers: { headerName: 'headerValue' },
      ownerId: 'string',
      eventTypes: ['string'],
      description: 'string',
      encryptedHeaders: {
        headerName: 'sensitiveHeaderValue',
      },
      enableCloudEventDelivery: true,
      checkCertificateRevocation: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"url":"string","name":"string","level":"tenant","filter":"id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"","secret":"string","enabled":false,"headers":{"headerName":"headerValue"},"ownerId":"string","eventTypes":["string"],"description":"string","encryptedHeaders":{"headerName":"sensitiveHeaderValue"},"enableCloudEventDelivery":true,"checkCertificateRevocation":false}'
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "updatedAt": "2018-10-30T07:06:22Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### DELETE /api/v1/webhooks/{id}

Deletes a specific webhook.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 204

No Content response.

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/webhooks/{id}/deliveries

Returns deliveries for a specific webhook. Delivery history is stored for 1 week.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventType` | string | No | Filter resources by event-type. |
| `limit` | number | No | Maximum number of deliveries to retrieve. |
| `next` | string | No | Cursor to the next page. |
| `prev` | string | No | Cursor to the previous page. |
| `sort` | string | No | Field to sort by, prefix with -/+ to indicate order. Enum: "status", "+status", "-status", "triggeredAt", "+triggeredAt", "-triggeredAt" |
| `status` | string | No | Filter resources by status (success or fail). Enum: "success", "fail" |

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
| `id` | string | Yes | The delivery's unique identifier. |
| `status` | string | Yes | The status of delivery. Enum: "success", "fail" |
| `request` | object | No | Request details for the delivery. |
| `response` | object | No | Response details for the delivery. |
| `eventType` | string | Yes | The name of the triggering event-type. |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for. |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered. |
| `statusMessage` | string | No | The status message of the delivery. |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery. |
| `body` | object | No | The sent body/payload of the delivery. |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery. |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response. |

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
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/webhooks/{id}/deliveries` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}/deliveries',
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
# qlik-cli has not implemented support for GET /api/v1/webhooks/{id}/deliveries yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}/deliveries" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "status": "success",
      "request": {
        "url": "string",
        "body": {},
        "headers": {
          "headerName": "headerValue",
          "encryptedHeadersName": "**OMITTED**"
        }
      },
      "response": {
        "body": "string",
        "headers": {
          "headerName": "headerValue",
          "encryptedHeadersName": "**OMITTED**"
        },
        "statusCode": 42
      },
      "eventType": "string",
      "webhookId": "string",
      "triggeredAt": "2018-10-30T07:06:22Z",
      "statusMessage": "string"
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

### GET /api/v1/webhooks/{id}/deliveries/{deliveryId}

Returns details for a specific delivery.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deliveryId` | string | Yes | The delivery's unique identifier. |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The delivery's unique identifier. |
| `status` | string | Yes | The status of delivery. Enum: "success", "fail" |
| `request` | object | No | Request details for the delivery. |
| `response` | object | No | Response details for the delivery. |
| `eventType` | string | Yes | The name of the triggering event-type. |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for. |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered. |
| `statusMessage` | string | No | The status message of the delivery. |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery. |
| `body` | object | No | The sent body/payload of the delivery. |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery. |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/webhooks/{id}/deliveries/{deliveryId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}/deliveries/{deliveryId}',
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
# qlik-cli has not implemented support for GET /api/v1/webhooks/{id}/deliveries/{deliveryId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}/deliveries/{deliveryId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "status": "success",
  "request": {
    "url": "string",
    "body": {},
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    }
  },
  "response": {
    "body": "string",
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    },
    "statusCode": 42
  },
  "eventType": "string",
  "webhookId": "string",
  "triggeredAt": "2018-10-30T07:06:22Z",
  "statusMessage": "string"
}
```

---

### POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend

Resends the delivery with the same payload.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deliveryId` | string | Yes | The delivery's unique identifier. |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 201

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The delivery's unique identifier. |
| `status` | string | Yes | The status of delivery. Enum: "success", "fail" |
| `request` | object | No | Request details for the delivery. |
| `response` | object | No | Response details for the delivery. |
| `eventType` | string | Yes | The name of the triggering event-type. |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for. |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered. |
| `statusMessage` | string | No | The status message of the delivery. |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery. |
| `body` | object | No | The sent body/payload of the delivery. |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery. |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend',
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
# qlik-cli has not implemented support for POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "status": "success",
  "request": {
    "url": "string",
    "body": {},
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    }
  },
  "response": {
    "body": "string",
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    },
    "statusCode": 42
  },
  "eventType": "string",
  "webhookId": "string",
  "triggeredAt": "2018-10-30T07:06:22Z",
  "statusMessage": "string"
}
```

---

### GET /api/v1/webhooks/event-types

Lists event-types that are possible to subscribe to.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the event type. |
| `title` | string | No | Title of the event type. |
| `levels` | string[] | No | Specifies which levels that are supported for this event type. |
| `category` | string | No | Category of the event type. |
| `description` | string | No | Description of the event type. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/webhooks/event-types` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/webhooks/event-types',
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
# qlik-cli has not implemented support for GET /api/v1/webhooks/event-types yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks/event-types" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "name": "string",
      "title": "string",
      "levels": [
        "string"
      ],
      "category": "string",
      "description": "string"
    }
  ]
}
```

---
