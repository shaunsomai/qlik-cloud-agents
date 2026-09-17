# ODAG apps

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Retrieve and filter on-demand generated analytics applications by type.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/analytics/odag-apps`](#get-apianalyticsodag-apps) | Retrieves ODAG Analytics Applications filtered by type: `selection` (used as entry points), `template` (source Analytics Application for generation), or `generated` (Analytics Applications created via ODAG requests). |

## API Reference

### GET /api/analytics/odag-apps

Retrieves ODAG Analytics Applications filtered by type: `selection` (used as entry points), `template` (source Analytics Application for generation), or `generated` (Analytics Applications created via ODAG requests).

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | string | Yes | The type of ODAG Analytics Application. Enum: "selection", "template", "generated" |

#### Responses

##### 200

Successful response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |

<details>
<summary>Properties of `data`</summary>

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-apps` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-apps',
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
# qlik-cli has not implemented support for GET /api/analytics/odag-apps yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-apps" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "name": "appname"
    }
  ]
}
```

---
