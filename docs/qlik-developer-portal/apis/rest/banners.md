# Banners

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Banners display short messages at the top of the client interface to share tenant-wide information, warnings, or issues. When embedding content, banners aren't shown inside qlik-embed UIs. The only embedding method that displays banners is an iFrame generated using the App Integration API.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/banners`](#get-apiv1banners) | Retrieves announcement banner configuration for the tenant, including content, scheduling, and link information for display at the top of the client interface. |
| `POST` | [`/api/v1/banners/actions/upsert`](#post-apiv1bannersactionsupsert) | Sets content, scheduling, and optional action links for the tenant-wide announcement banner. Requires `TenantAdmin` role. |

## API Reference

### GET /api/v1/banners

Retrieves announcement banner configuration for the tenant, including content, scheduling, and link information for display at the top of the client interface.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Banner retrieval was successful.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "info", "warning", "error", "resolved" |
| `enabled` | boolean | Yes |  |
| `endTime` | string | Yes | date-time in UTC. |
| `linkUrl` | string | No |  |
| `message` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the banner |
| `linkLabel` | string | No |  |
| `startTime` | string | Yes | date-time in UTC. |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | Yes | userId of the user who last modified the banner |
| `linkEnabled` | boolean | Yes |  |

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
| `status` | integer | No |  |

</details>

##### 401

Unauthorized

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
| `status` | integer | No |  |

</details>

##### 403

Forbidden

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
| `status` | integer | No |  |

</details>

##### 404

Not found

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
| `status` | integer | No |  |

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
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/banners` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/banners', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/banners yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/banners" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "info",
  "enabled": true,
  "endTime": "2024-01-01T00:00:00.000Z",
  "linkUrl": "string",
  "message": "string",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "linkLabel": "string",
  "startTime": "2024-01-01T00:00:00.000Z",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "linkEnabled": true
}
```

---

### POST /api/v1/banners/actions/upsert

Sets content, scheduling, and optional action links for the tenant-wide announcement banner. Requires `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "info", "warning", "error", "resolved" |
| `enabled` | boolean | Yes |  |
| `endTime` | string | Yes | date-time in UTC. |
| `linkUrl` | string | No |  |
| `message` | string | Yes |  |
| `linkLabel` | string | No |  |
| `startTime` | string | Yes | date-time in UTC. |
| `linkEnabled` | boolean | Yes |  |

#### Responses

##### 201

The banner has been successfully upserted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "info", "warning", "error", "resolved" |
| `enabled` | boolean | Yes |  |
| `endTime` | string | Yes | date-time in UTC. |
| `linkUrl` | string | No |  |
| `message` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the banner |
| `linkLabel` | string | No |  |
| `startTime` | string | Yes | date-time in UTC. |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | Yes | userId of the user who last modified the banner |
| `linkEnabled` | boolean | Yes |  |

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
| `status` | integer | No |  |

</details>

##### 401

Unauthorized

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
| `status` | integer | No |  |

</details>

##### 403

Forbidden

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
| `status` | integer | No |  |

</details>

##### 404

Not found

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
| `status` | integer | No |  |

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
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/banners/actions/upsert` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/banners/actions/upsert',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'info',
      enabled: true,
      endTime: '2024-01-01T00:00:00.000Z',
      linkUrl: 'string',
      message: 'string',
      linkLabel: 'string',
      startTime: '2024-01-01T00:00:00.000Z',
      linkEnabled: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/banners/actions/upsert yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/banners/actions/upsert" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"info","enabled":true,"endTime":"2024-01-01T00:00:00.000Z","linkUrl":"string","message":"string","linkLabel":"string","startTime":"2024-01-01T00:00:00.000Z","linkEnabled":true}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "info",
  "enabled": true,
  "endTime": "2024-01-01T00:00:00.000Z",
  "linkUrl": "string",
  "message": "string",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "linkLabel": "string",
  "startTime": "2024-01-01T00:00:00.000Z",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "linkEnabled": true
}
```

---
