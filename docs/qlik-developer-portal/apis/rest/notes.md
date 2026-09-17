# Notes

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Notes provide a collaborative experience to support analytics consumption in your tenant. This API enables or disables notes.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/notes/settings`](#get-apiv1notessettings) |  |
| `PUT` | [`/api/v1/notes/settings`](#put-apiv1notessettings) |  |

## API Reference

### GET /api/v1/notes/settings _(deprecated)_

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Responses

##### 200

Notes enablement status.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reason` | string | No | The possible states for the status of notes configuration GET or POST operation Enum: "deployment", "toggle", "license" |
| `available` | boolean | Yes | 'true' if the note feature is enabled for this tenant and user otherwise 'false'. |
| `lastFetch` | string | No | The timestamp for the last time this users notes settings were fetched from downstream services. |

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/notes/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/notes/settings',
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
# qlik-cli has not implemented support for GET /api/v1/notes/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/notes/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "reason": "deployment",
  "available": true,
  "lastFetch": "string"
}
```

---

### PUT /api/v1/notes/settings _(deprecated)_

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Request Body

**Required**

A JSON payload containing note settings to put.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `toggledOn` | boolean | No | pass 'true' to enable the note toggle for the tenant, 'false' to disable the toggle (other values are ignore). |

#### Responses

##### 200

The newly applied note settings for the tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `toggleOn` | boolean | No | 'true' if the note feature is enabled for this tenant and user otherwise 'false'. |

##### 400

Request content error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 403

Unauthorized user.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | An optional traceId |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to notes broker service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/notes/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/notes/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ toggledOn: true }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/notes/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/notes/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"toggledOn":true}'
```

**Example Response:**

```json
{
  "toggleOn": true
}
```

---
