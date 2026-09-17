# Automation connectors

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Automation connectors let you integrate third-party services and applications into your data analytics workflows. Use this API to discover available connectors and understand billing characteristics.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/automation-connectors`](#get-apiv1automation-connectors) | Retrieves a list of automation connectors. |

## API Reference

### GET /api/v1/automation-connectors

Retrieves a list of automation connectors.

- **Replaced by:** "GET:/workflows/automation-connectors"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | string | No | Pagination cursor returned from a previous request. |
| `filter` | string | No | Filters the result based on the specified criteria: name. |
| `limit` | integer | No | The number of automation connectors to retrieve. |
| `sort` | string | No | The field to sort by, with +- prefix indicating sort order. (`?sort=-name` => sort on the `name` field using descending order). Enum: "id", "-id", "+id", "name", "+name", "-name" |

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
| `id` | string | No |  |
| `name` | string | No | The name of an automation connector. |
| `billable` | boolean | No | Indicates if the connector is billable. |
| `logoLarge` | string | No | The URL to the large logo of the connector. |
| `logoSmall` | string | No | The URL to the small logo of the connector. |
| `logoMedium` | string | No | The URL to the medium logo of the connector. |
| `description` | string | No | The description of the automation connector. |
| `hasWebhooks` | boolean | No | Indicates if the connector supports webhooks. |

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
// qlik-api has not implemented support for `GET /api/v1/automation-connectors` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automation-connectors',
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
# qlik-cli has not implemented support for GET /api/v1/automation-connectors yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connectors" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
      "name": "Airtable",
      "billable": "true",
      "logoLarge": "https://cdn.qlikcloud.com/automations/logos/a2649cabda63b339ebc68a0c8d028f08.png",
      "logoSmall": "https://cdn.qlikcloud.com/automations/logos/a14638b5bf73f6d360f3c2732cf94bd9.png",
      "logoMedium": "https://cdn.qlikcloud.com/automations/logos/db2e3454fd01a6c3a53c09609a0b504f.png",
      "description": "Airtable is a cloud collaboration service.",
      "hasWebhooks": "true"
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
