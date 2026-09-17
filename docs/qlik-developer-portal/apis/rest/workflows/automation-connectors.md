# Automation connectors

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Automation connectors let you integrate third-party services and applications into your data analytics workflows. Use this API to discover available connectors and understand billing characteristics.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/workflows/automation-connectors`](#get-apiworkflowsautomation-connectors) | Retrieves a list of automation connectors. |
| `GET` | [`/api/workflows/automation-connectors/{connectorId}`](#get-apiworkflowsautomation-connectorsconnectorid) | Retrieves the full details of an automation connector, including its connection parameters, blocks, and snippets. |
| `GET` | [`/api/workflows/automation-connectors/{connectorId}/webhooks/configuration`](#get-apiworkflowsautomation-connectorsconnectoridwebhooksconfiguration) | Retrieves the webhook configuration for an automation connector, including its events and event parameters. |

## API Reference

### GET /api/workflows/automation-connectors

Retrieves a list of automation connectors.

- **Replaces:** "GET:/v1/automation-connectors"
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
// qlik-api has not implemented support for `GET /api/workflows/automation-connectors` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/workflows/automation-connectors',
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
# qlik-cli has not implemented support for GET /api/workflows/automation-connectors yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/workflows/automation-connectors" \
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

### GET /api/workflows/automation-connectors/{connectorId}

Retrieves the full details of an automation connector, including its connection parameters, blocks, and snippets.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | string | Yes | The unique identifier of the automation connector. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No | The name of the automation connector. |
| `blocks` | object[] | No | The available blocks (endpoints) for this connector. |
| `params` | object[] | No | The connection parameters required to authenticate with this connector. |
| `billable` | boolean | No | Indicates if the connector is billable. |
| `snippets` | object[] | No | The available snippet templates for this connector. |
| `description` | string | No | The description of the automation connector. |
| `hasWebhooks` | boolean | No | Indicates if the connector supports webhooks. |
| `connectDocumentation` | string | No | Documentation for setting up a connection with this connector. |

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the block. |
| `name` | string | No | The name of the block. |
| `role` | string | No | The role of the block. |
| `inputs` | object[] | No | The input parameters for this block. |
| `objectType` | string | No | The object type this block operates on. |
| `description` | string | No | The description of the block. |
| `exampleOutput` | object \| array \| string | No | An example of the output this block produces. |

<details>
<summary>Properties of `inputs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the parameter. |
| `name` | string | No | The name of the parameter. |
| `options` | string[] | No | The available options for the parameter. |
| `setting` | boolean | No | Indicates whether the parameter is a setting. |
| `optional` | boolean | No | Indicates whether the parameter is optional. |
| `fieldType` | string | No | The field type of the parameter. |
| `description` | string | No | The description of the parameter. |
| `exampleValue` | string | No | An example value for the parameter. |

</details>

<details>
<summary>Properties of `exampleOutput`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object,string,number,boolean[] | No |  |

<details>
<summary>Properties of `properties`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

**Option 3:**

_Properties truncated due to depth limit._

**Option 4:**

_Properties truncated due to depth limit._

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the parameter. |
| `name` | string | No | The name of the parameter. |
| `options` | string[] | No | The available options for the parameter. |
| `setting` | boolean | No | Indicates whether the parameter is a setting. |
| `optional` | boolean | No | Indicates whether the parameter is optional. |
| `fieldType` | string | No | The field type of the parameter. |
| `description` | string | No | The description of the parameter. |
| `exampleValue` | string | No | An example value for the parameter. |

</details>

<details>
<summary>Properties of `snippets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the snippet. |
| `name` | string | No | The name of the snippet. |
| `role` | string | No | The role of the snippet. |
| `inputs` | object[] | No | The input fields for this snippet. |
| `objectType` | string | No | The object type this snippet operates on. |
| `description` | string | No | The description of the snippet. |
| `exampleOutput` | object \| array \| string | No | An example of the output this snippet produces. |

<details>
<summary>Properties of `inputs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the snippet input. |
| `name` | string | No | The display name (prompt) of the input. |
| `options` | object \| array | No | The available options for this input. |
| `optional` | boolean | No | Indicates whether the input is optional. |
| `fieldType` | string | No | The field type of the input. |
| `description` | string | No | The help text for this input. |

<details>
<summary>Properties of `options`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `exampleOutput`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object,string,number,boolean[] | No |  |

<details>
<summary>Properties of `properties`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

**Option 3:**

_Properties truncated due to depth limit._

**Option 4:**

_Properties truncated due to depth limit._

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

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
// qlik-api has not implemented support for `GET /api/workflows/automation-connectors/{connectorId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/workflows/automation-connectors/{connectorId}',
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
# qlik-cli has not implemented support for GET /api/workflows/automation-connectors/{connectorId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/workflows/automation-connectors/{connectorId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
  "name": "Airtable",
  "blocks": [
    {
      "id": "9d94bef0-b28c-11eb-8dba-01593c457362",
      "name": "List Records",
      "role": "list",
      "inputs": [
        {
          "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
          "name": "API Key",
          "options": [
            "string"
          ],
          "setting": false,
          "optional": false,
          "fieldType": "text",
          "description": "string",
          "exampleValue": "string"
        }
      ],
      "objectType": "Record",
      "description": "string",
      "exampleOutput": {}
    }
  ],
  "params": [
    {
      "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
      "name": "API Key",
      "options": [
        "string"
      ],
      "setting": false,
      "optional": false,
      "fieldType": "text",
      "description": "string",
      "exampleValue": "string"
    }
  ],
  "billable": true,
  "snippets": [
    {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Sync Records",
      "role": "string",
      "inputs": [
        {
          "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "name": "Table Name",
          "options": {},
          "optional": false,
          "fieldType": "text",
          "description": "string"
        }
      ],
      "objectType": "Record",
      "description": "string",
      "exampleOutput": {}
    }
  ],
  "description": "string",
  "hasWebhooks": true,
  "connectDocumentation": "string"
}
```

---

### GET /api/workflows/automation-connectors/{connectorId}/webhooks/configuration

Retrieves the webhook configuration for an automation connector, including its events and event parameters.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | string | Yes | The unique identifier of the automation connector. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the webhook configuration. |
| `events` | object[] | No | The available webhook events for this connector. |
| `automatic` | boolean | No | Indicates whether the webhook is set up automatically. |

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the webhook event. |
| `name` | string | No | The name of the webhook event. |
| `role` | string | No | The role of the webhook event. |
| `params` | object[] | No | The parameters available for this webhook event. |
| `description` | string | No | The description of the webhook event. |
| `exampleOutput` | object \| array \| string | No | An example of the payload this event produces. |

<details>
<summary>Properties of `params`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the webhook event parameter. |
| `name` | string | No | The name of the parameter. |
| `type` | string | No | The type of the parameter. |
| `options` | string[] | No | The available options for this parameter. |
| `required` | boolean | No | Indicates whether the parameter is required. |

</details>

<details>
<summary>Properties of `exampleOutput`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object,string,number,boolean[] | No |  |

<details>
<summary>Properties of `properties`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

**Option 3:**

_Properties truncated due to depth limit._

**Option 4:**

_Properties truncated due to depth limit._

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

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
// qlik-api has not implemented support for `GET /api/workflows/automation-connectors/{connectorId}/webhooks/configuration` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/workflows/automation-connectors/{connectorId}/webhooks/configuration',
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
# qlik-cli has not implemented support for GET /api/workflows/automation-connectors/{connectorId}/webhooks/configuration yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/workflows/automation-connectors/{connectorId}/webhooks/configuration" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
  "events": [
    {
      "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
      "name": "Record Created",
      "role": "create",
      "params": [
        {
          "id": "0d87347d-27c0-11ea-921c-022e6b5ea1e2",
          "name": "table_id",
          "type": "text",
          "options": [
            "string"
          ],
          "required": true
        }
      ],
      "description": "string",
      "exampleOutput": {}
    }
  ],
  "automatic": true
}
```

---
