# Data sources

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Lists data sources available on the tenant for the creation of data connections.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-sources`](#get-apiv1data-sources) | Gets the list of data sources available on the node. |
| `GET` | [`/api/v1/data-sources/{dataSourceId}/api-specs`](#get-apiv1data-sourcesdatasourceidapi-specs) |  |
| `GET` | [`/api/v1/data-sources/{dataSourceId}/gateways`](#get-apiv1data-sourcesdatasourceidgateways) |  |
| `GET` | [`/api/v1/data-sources/{dataSourceId}/settings`](#get-apiv1data-sourcesdatasourceidsettings) | Retrieves the settings for a data source. |
| `PUT` | [`/api/v1/data-sources/{dataSourceId}/settings`](#put-apiv1data-sourcesdatasourceidsettings) | Updates the settings for a data source. |

## API Reference

### GET /api/v1/data-sources

Gets the list of data sources available on the node.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSourceId` | string | No | Filtering on datasourceID, when multiple dataSourceId are set in query, last dataSourceId will be used |
| `detail` | boolean | No | Determines if provider detail is returned |
| `includeDisabled` | boolean | No | When true, disabled datasources are also included in the response |
| `includeui` | boolean | No | Determines if UI info is returned |

#### Responses

##### 200

An array of data source info

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSources` | object[] | Yes | List of datasources metadata object |
| `lastUpdated` | string | Yes | Time stamp of last updated |
| `connectorNodes` | object[] | No | List of connector nodes (only present when query parameter 'detail' is set to true) |

<details>
<summary>Properties of `dataSources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Datasource name |
| `uiInfo` | object | No | UI related metadata (only present when 'includeui' is set to true in query) |
| `disabled` | boolean | No | Indicates whether the datasource is disabled |
| `provider` | string | Yes | Connector provider |
| `capabilities` | string[] | No | List of capabilities supported by the datasource |
| `dataSourceId` | string | Yes | Unique identifier of datasource |
| `providerName` | string | Yes | Provider name |
| `qriDefinition` | object | No | Qri definition template |
| `dataSourceType` | string | No | Type of datasource |
| `dataLoadUrlOverride` | string | No | Override value of dataload URL (could be null) |
| `dataSourcePropertyName` | string | No | Datasource property name (could be null) |

<details>
<summary>Properties of `uiInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `iframe` | boolean | No | If support iframe |
| `selectUrl` | string | No | Select URL |
| `connectUrl` | string | No | Connect URL |
| `iconRectUrl` | string | No | Icon URL |
| `iconSquareUrl` | string | No | Square icon URL |
| `credentialsUrl` | string | No | Credentials URL |
| `connectorMainUrl` | string | No | Connector main URL |
| `loadModelSupport` | string | No | Indicate if the datasource supports load model |

</details>

<details>
<summary>Properties of `qriDefinition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `itemPart` | object | No | Connection part of Qri template |
| `pathPart` | object | Yes | Connection part of Qri template |
| `qriPrefix` | string | Yes | Qri prefix |
| `connectionPart` | object | Yes | Connection part of Qri template |

<details>
<summary>Properties of `itemPart`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pathPart`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `connectionPart`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `connectorNodes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | URL of connector node |
| `state` | string | Yes | State of the connector node |
| `contractType` | number | Yes | Contract type used to communicate with the connector (between 0 and 3) |
| `providerName` | string | Yes | Connector provider name |
| `cachedDataSources` | string[] | No | List of datasource IDs provided by the provider |
| `dataSourcesUpdated` | boolean | Yes | Indicates whether the datasources are up to date |

</details>

##### 401

Unauthorized request (Bad JWT token etc)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 404

Datasource not found or it is not enabled

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 500

Internal errors

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-sources` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sources',
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
# qlik-cli has not implemented support for GET /api/v1/data-sources yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "dataSources": [
    {
      "name": "Qlik® REST Connector",
      "uiInfo": {
        "iframe": true,
        "selectUrl": "/customdata/64/QvRestConnector/web/standalone/select-dialog.html",
        "connectUrl": "/customdata/64/QvRestConnector/web/standalone/connect-dialog.html",
        "iconRectUrl": "/customdata/64/QvRestConnector/web/Icons/rest.png",
        "iconSquareUrl": "/customdata/64/QvRestConnector/web/Icons/rest-square.png",
        "credentialsUrl": "/customdata/64/QvRestConnector/web/standalone/credentials-dialog.html",
        "connectorMainUrl": "/customdata/64/QvRestConnector/web/connector-main-iframe.js",
        "loadModelSupport": "false"
      },
      "disabled": true,
      "provider": "QvRestConnector.exe",
      "capabilities": [
        "datasource-specific-capabity"
      ],
      "dataSourceId": "rest",
      "providerName": "Qlik® REST Connector",
      "qriDefinition": {
        "itemPart": {
          "prefix": "#",
          "template": "{schema}.{table}",
          "properties": [
            "schema"
          ]
        },
        "pathPart": {
          "prefix": "#",
          "template": "{schema}.{table}",
          "properties": [
            "schema"
          ]
        },
        "qriPrefix": "qri:db:sap-sql://",
        "connectionPart": {
          "template": "{schema}.{table}",
          "properties": [
            "schema"
          ]
        }
      },
      "dataSourceType": "connector",
      "dataLoadUrlOverride": "ml-endpoints:50055",
      "dataSourcePropertyName": "sourceType"
    }
  ],
  "lastUpdated": "2023-11-03T15:45:14.195Z",
  "connectorNodes": [
    {
      "url": "localhost:50060",
      "state": "READY",
      "contractType": 2,
      "providerName": "Qlik® REST Connector",
      "cachedDataSources": [
        "rest"
      ],
      "dataSourcesUpdated": "true"
    }
  ]
}
```

---

### GET /api/v1/data-sources/{dataSourceId}/api-specs

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSourceId` | string | Yes | Datasource ID |

#### Responses

##### 200

API spec returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorVersion` | string | Yes | Datasource provider (i.e. connector) version |
| `connectorProvider` | string | Yes | Datasource provider |
| `connectionProperties` | object | Yes | List of properties required for the given datasource |

##### 401

Unauthorized request (Bad JWT token etc)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 404

Datasource not found or it is not enabled

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 500

Internal errors

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 503

Service unavailable, happens when request to connector or down stream services fails

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-sources/{dataSourceId}/api-specs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sources/{dataSourceId}/api-specs',
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
# qlik-cli has not implemented support for GET /api/v1/data-sources/{dataSourceId}/api-specs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources/{dataSourceId}/api-specs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "connectorVersion": "1.180.0",
  "connectorProvider": "QvRestConnector.exe",
  "connectionProperties": "{\"property1\": \"value\", \"property2\": \"value2\"}"
}
```

---

### GET /api/v1/data-sources/{dataSourceId}/gateways

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSourceId` | string | Yes | Datasource ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `forceRefresh` | boolean | No | Force to get a refreshed list from backend. Cached list will be returned if not set or set to false. |

#### Responses

##### 200

Gateways list returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `gateways` | object[] | No | List of gateway ID's for given datasource ID |
| `refreshedAt` | string | No | Time stamp when the gateways data were refreshed |

<details>
<summary>Properties of `gateways`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gateway ID |
| `name` | string | No | Gateway name |
| `default` | boolean | No | Whether the gateway is default |

</details>

##### 401

Unauthorized request (Bad JWT token etc)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 404

Datasource not found (or not enabled), or no gateway is configured for the tenant

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 500

General internal errors

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-sources/{dataSourceId}/gateways` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sources/{dataSourceId}/gateways',
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
# qlik-cli has not implemented support for GET /api/v1/data-sources/{dataSourceId}/gateways yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources/{dataSourceId}/gateways" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "gateways": [
    {
      "id": "051YTx0OGDlfQ_66H3NyXwK24HEEyyJI::a6CxFtkInvsJnrNXCOVWR8pQOwaphpU0",
      "name": "MyGateway",
      "default": true
    }
  ],
  "refreshedAt": "2024-01-18T02:25:59.521Z"
}
```

---

### GET /api/v1/data-sources/{dataSourceId}/settings

Retrieves the settings for a data source.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSourceId` | string | Yes | Datasource ID |

#### Responses

##### 200

A JSON object containing the data source settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disabled` | boolean | No | Indicates whether the data source is disabled. |

##### 400

Bad request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 401

Unauthorized request (Bad JWT token etc)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 404

Data source not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 500

Internal errors

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-sources/{dataSourceId}/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sources/{dataSourceId}/settings',
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
# qlik-cli has not implemented support for GET /api/v1/data-sources/{dataSourceId}/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources/{dataSourceId}/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "disabled": false
}
```

---

### PUT /api/v1/data-sources/{dataSourceId}/settings

Updates the settings for a data source.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSourceId` | string | Yes | Datasource ID |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disabled` | boolean | Yes | Indicates whether the data source is disabled. |

#### Responses

##### 200

Data source settings updated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disabled` | boolean | No | Indicates whether the data source is disabled. |

##### 400

Bad request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 401

Unauthorized request (Bad JWT token etc)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 404

Data source not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

##### 500

Internal errors

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A service specific error code string |
| `meta` | object | No | Additional metadata associated with the error |
| `title` | string | Yes | Summary of the error |
| `detail` | string | No | Concrete detail about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/data-sources/{dataSourceId}/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sources/{dataSourceId}/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ disabled: false }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-sources/{dataSourceId}/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources/{dataSourceId}/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"disabled":false}'
```

**Example Response:**

```json
{
  "disabled": false
}
```

---
