# Direct Access Agents

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

API for remotely managing configuration settings of Direct Access Gateway agents.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/direct-access-agents/{agentId}/actions/{agentAction}`](#post-apiv1direct-access-agentsagentidactionsagentaction) | Restarts the specified agent. If a reload is in `RELOADING` status the `restart` action will be ignored. Use `force-restart` to restart the agent even if a reload is in `RELOADING` status. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `POST` | [`/api/v1/direct-access-agents/{agentId}/benchmarks`](#post-apiv1direct-access-agentsagentidbenchmarks) | Starts a background benchmark task to measure the performance of a Direct Access agent. Use this endpoint to evaluate agent throughput and latency for capacity planning and performance optimization. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}`](#get-apiv1direct-access-agentsagentidbenchmarksbenchmarkid) | Retrieves the current status and progress of a running or completed benchmark task. Use this endpoint to monitor benchmark execution and retrieve performance metrics once the task is completed. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `POST` | [`/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel`](#post-apiv1direct-access-agentsagentidbenchmarksbenchmarkidcancel) | Requests a cancellation on a running benchmark by id for the specified agent. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/configurations`](#get-apiv1direct-access-agentsagentidconfigurations) | Retrieves the connector agent configuration from the specified agent. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `PATCH` | [`/api/v1/direct-access-agents/{agentId}/configurations`](#patch-apiv1direct-access-agentsagentidconfigurations) | Makes changes to the local agent configuration using JSON Patch. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files`](#get-apiv1direct-access-agentsagentidconnectorsconnectortypefiles) | Retrieves the configuration files associated with the connector. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}`](#get-apiv1direct-access-agentsagentidconnectorsconnectortypefilesfiletype) | Retrieves the configuration items in the flat file for the specified connector. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}`](#put-apiv1direct-access-agentsagentidconnectorsconnectortypefilesfiletype) | Completely replaces the contents of the connector's configuration file. Partial updates are not supported. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths`](#get-apiv1direct-access-agentsagentidconnectorsfile-connectorfilesallowed-paths) | Retrieves the allowed paths settings for the File Connector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.6+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths`](#put-apiv1direct-access-agentsagentidconnectorsfile-connectorfilesallowed-paths) | Completely replaces the contents of the allowed paths configuration file for the File Connector. Partial updates are not supported. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.6+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings`](#get-apiv1direct-access-agentsagentidconnectorsodbc-connectorfilescustom-data-type-mappings) | Retrieves the custom data type mapping settings for the Generic ODBC Connector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.5+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings`](#put-apiv1direct-access-agentsagentidconnectorsodbc-connectorfilescustom-data-type-mappings) | Completely replaces the contents of the custom data type mapping configuration file for the Generic ODBC connector. Partial updates are not supported. There are property naming differences between the API and the file contents. Use the API property format when making changes. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.5+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration`](#get-apiv1direct-access-agentsagentidtoolsmetrics-collectorconfiguration) | Retrieves the settings for the metrics collector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.9+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration`](#put-apiv1direct-access-agentsagentidtoolsmetrics-collectorconfiguration) | Completely replaces the contents of the metrics collector settings configuration file. Partial updates are not supported.  Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.9+. |

## API Reference

### POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction}

Restarts the specified agent. If a reload is in `RELOADING` status the `restart` action will be ignored. Use `force-restart` to restart the agent even if a reload is in `RELOADING` status. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentAction` | string | Yes | The type of action to perform. Permitted values are `restart` (will not restart the agent if a reload is in `RELOADING` status) and `force-restart` (will restart the agent even if a reload is in `RELOADING` status). |
| `agentId` | string | Yes | The agent ID |

#### Responses

##### 204

Service restarted successfully.

##### 400

Error restarting the service.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Service doesn't exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/actions/{agentAction}',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/actions/{agentAction}" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/direct-access-agents/{agentId}/benchmarks

Starts a background benchmark task to measure the performance of a Direct Access agent. Use this endpoint to evaluate agent throughput and latency for capacity planning and performance optimization. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `force` | boolean | No | Forces the benchmark to start regardless of the state of the agent. Does not override QCS resource limits. Use with caution. |
| `gigaBytesToTransfer` | integer | No | The volume of data in GB to transfer during the throughput measurement part of the benchmark. |

#### Responses

##### 201

Benchmark task created successfully with a unique identifier.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `benchmarkId` | string | No |  |

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

The agent was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 501

All or part of the request has not yet been implemented.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/benchmarks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/benchmarks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "benchmarkId": "string"
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}

Retrieves the current status and progress of a running or completed benchmark task. Use this endpoint to monitor benchmark execution and retrieve performance metrics once the task is completed. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |
| `benchmarkId` | string | Yes | The benchmark ID |

#### Responses

##### 200

Benchmark status and performance metrics retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The benchmark status |
| `results` | object | No |  |
| `benchmarkId` | string | No | The benchmark ID |
| `statusMessage` | string | No | Additional details about the benchmark status |
| `benchmarkEndTime` | string | No | The ISO 8601 formatted timestamp when the benchmark task completed or was cancelled |
| `benchmarkStartTime` | string | No | The ISO 8601 formatted timestamp when the benchmark task started execution |
| `totalBytesRequested` | integer | No | The total bytes requested to be transferred during the benchmark |

<details>
<summary>Properties of `results`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | integer | No | The latency in ms measured during data transmission |
| `throughput` | integer | No | The data throughput in KB/s measured during data transmission |
| `totalBytesTransferred` | integer | No | The total number of bytes successfully transferred during data transmission |
| `dataTransmissionEndTime` | string | No | The ISO 8601 formatted timestamp when data transmission completed |
| `dataTransmissionStartTime` | string | No | The ISO 8601 formatted timestamp when data transmission start |

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

The benchmark was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "string",
  "results": {
    "latency": 42,
    "throughput": 42,
    "totalBytesTransferred": 42,
    "dataTransmissionEndTime": "string",
    "dataTransmissionStartTime": "string"
  },
  "benchmarkId": "string",
  "statusMessage": "string",
  "benchmarkEndTime": "string",
  "benchmarkStartTime": "string",
  "totalBytesRequested": 42
}
```

---

### POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel

Requests a cancellation on a running benchmark by id for the specified agent. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |
| `benchmarkId` | string | Yes | The benchmark ID |

#### Responses

##### 202

The cancellation was requested successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |
| `statusUrl` | object | No |  |

<details>
<summary>Properties of `statusUrl`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to the related resource |

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

The benchmark was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "string",
  "statusUrl": {
    "href": "string"
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/configurations

Retrieves the connector agent configuration from the specified agent. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `queryProperties` | string[] | No | Individual properties within the agent configuration |

#### Responses

##### 200

The dictionary of key/value pairs retrieved from the configuration file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectors` | object[] | No |  |
| `dcaasSettings` | object[] | No |  |
| `connectorAgentSettings` | object[] | No |  |

<details>
<summary>Properties of `connectors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `settings` | object[] | No |  |
| `connectorName` | string | No |  |

<details>
<summary>Properties of `settings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

_Properties truncated due to depth limit._

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `dcaasSettings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `value` | string | No |  |
| `connector` | string | No |  |
| `uiActions` | string[] | No | Enum: "Read", "Write" |
| `apiActions` | string[] | No | Enum: "Read", "Write" |
| `description` | string | No |  |
| `displayName` | string | No |  |
| `defaultValue` | string | No |  |
| `pendingValue` | string | No |  |
| `permittedRangeEnd` | integer | No |  |
| `pendingApplication` | boolean | No |  |
| `allowMultipleValues` | boolean | No |  |
| `applyWithoutRestart` | boolean | No |  |
| `permittedRangeStart` | integer | No |  |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `value` | string | No |  |
| `connector` | string | No |  |
| `uiActions` | string[] | No | Enum: "Read", "Write" |
| `apiActions` | string[] | No | Enum: "Read", "Write" |
| `description` | string | No |  |
| `displayName` | string | No |  |
| `defaultValue` | string | No |  |
| `pendingValue` | string | No |  |
| `permittedValues` | string[] | No |  |
| `pendingApplication` | boolean | No |  |
| `allowMultipleValues` | boolean | No |  |
| `applyWithoutRestart` | boolean | No |  |

</details>

</details>

<details>
<summary>Properties of `connectorAgentSettings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `value` | string | No |  |
| `connector` | string | No |  |
| `uiActions` | string[] | No | Enum: "Read", "Write" |
| `apiActions` | string[] | No | Enum: "Read", "Write" |
| `description` | string | No |  |
| `displayName` | string | No |  |
| `defaultValue` | string | No |  |
| `pendingValue` | string | No |  |
| `permittedRangeEnd` | integer | No |  |
| `pendingApplication` | boolean | No |  |
| `allowMultipleValues` | boolean | No |  |
| `applyWithoutRestart` | boolean | No |  |
| `permittedRangeStart` | integer | No |  |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No |  |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `value` | string | No |  |
| `connector` | string | No |  |
| `uiActions` | string[] | No | Enum: "Read", "Write" |
| `apiActions` | string[] | No | Enum: "Read", "Write" |
| `description` | string | No |  |
| `displayName` | string | No |  |
| `defaultValue` | string | No |  |
| `pendingValue` | string | No |  |
| `permittedValues` | string[] | No |  |
| `pendingApplication` | boolean | No |  |
| `allowMultipleValues` | boolean | No |  |
| `applyWithoutRestart` | boolean | No |  |

</details>

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/configurations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/configurations',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/configurations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/configurations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "connectors": [
    {
      "settings": [
        {
          "name": "string",
          "value": "string",
          "connector": "string",
          "uiActions": [
            "Read"
          ],
          "apiActions": [
            "Read"
          ],
          "description": "string",
          "displayName": "string",
          "defaultValue": "string",
          "pendingValue": "string",
          "permittedRangeEnd": 42,
          "pendingApplication": true,
          "allowMultipleValues": true,
          "applyWithoutRestart": true,
          "permittedRangeStart": 42
        }
      ],
      "connectorName": "string"
    }
  ],
  "dcaasSettings": [
    {
      "name": "string",
      "value": "string",
      "connector": "string",
      "uiActions": [
        "Read"
      ],
      "apiActions": [
        "Read"
      ],
      "description": "string",
      "displayName": "string",
      "defaultValue": "string",
      "pendingValue": "string",
      "permittedRangeEnd": 42,
      "pendingApplication": true,
      "allowMultipleValues": true,
      "applyWithoutRestart": true,
      "permittedRangeStart": 42
    }
  ],
  "connectorAgentSettings": [
    {
      "name": "string",
      "value": "string",
      "connector": "string",
      "uiActions": [
        "Read"
      ],
      "apiActions": [
        "Read"
      ],
      "description": "string",
      "displayName": "string",
      "defaultValue": "string",
      "pendingValue": "string",
      "permittedRangeEnd": 42,
      "pendingApplication": true,
      "allowMultipleValues": true,
      "applyWithoutRestart": true,
      "permittedRangeStart": 42
    }
  ]
}
```

---

### PATCH /api/v1/direct-access-agents/{agentId}/configurations

Makes changes to the local agent configuration using JSON Patch. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |

#### Request Body

The JSON Patch document

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "add", "replace", "remove" |
| `path` | string | Yes | Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS" |
| `value` | string | Yes |  |

**Content-Type:** `application/json-patch+json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "add", "replace", "remove" |
| `path` | string | Yes | Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS" |
| `value` | string | Yes |  |

#### Responses

##### 204

Patch applied.

##### 207

Patch applied, validation results show success or failure of each individual patch operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `errorMessage` | string | No |  |
| `httpStatusCode` | integer | No |  |
| `failedPatchError` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `valid` | boolean | No |  |
| `operation` | object | No |  |
| `validationResult` | string | No |  |

<details>
<summary>Properties of `operation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "add", "replace", "remove" |
| `path` | string | Yes | Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS" |
| `value` | string | Yes |  |

</details>

</details>

<details>
<summary>Properties of `failedPatchError`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 415

Unsupported content-type. This endpoint must include `application/json` as a valid content-type for API compliance, but C# JsonPatchDocument doesn't support it. Requests must use `application/json-patch+json`.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `PATCH /api/v1/direct-access-agents/{agentId}/configurations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/configurations',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: 'AGENT_LOG_LEVEL',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/direct-access-agents/{agentId}/configurations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/configurations" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"AGENT_LOG_LEVEL","value":"string"}]'
```

**Example Response:**

```json
{
  "data": [
    {
      "valid": true,
      "operation": {
        "op": "add",
        "path": "AGENT_LOG_LEVEL",
        "value": "string"
      },
      "validationResult": "string"
    }
  ],
  "errorMessage": "string",
  "httpStatusCode": 42,
  "failedPatchError": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files

Retrieves the configuration files associated with the connector. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |
| `connectorType` | string | Yes | The connector to retrieve the list of files for Enum: "file-connector", "rest-connector", "odbc-connector" |

#### Responses

##### 200

The list of files for the specified connector.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | string[] | No |  |
| `errorMessage` | object | No |  |

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    "string"
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}

Retrieves the configuration items in the flat file for the specified connector. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |
| `connectorType` | string | Yes | The connector type to retrieve Enum: "file-connector", "rest-connector", "odbc-connector" |
| `fileType` | string | Yes | The type of file to retrieve Enum: "CustomTypesMapping", "PlainTextConfiguration", "AllowedPaths", "AllowedDrivers", "AllowedDsns", "CustomAllowedExtensions" |

#### Responses

##### 200

The list of configuration values from the file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | string[] | No |  |
| `errorMessage` | object | No |  |

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 403

The requestor does not have the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    "string"
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}

Completely replaces the contents of the connector's configuration file. Partial updates are not supported. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |
| `connectorType` | string | Yes | The connector type to update Enum: "file-connector", "rest-connector", "odbc-connector" |
| `fileType` | string | Yes | The file type to update Enum: "CustomTypesMapping", "PlainTextConfiguration", "AllowedPaths", "AllowedDrivers", "AllowedDsns", "CustomAllowedExtensions" |

#### Request Body

The contents of the file to be updated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contentsToSave` | string[] | No | Individual lines of the file. Must be escaped when sending as json. |

#### Responses

##### 204

Updated.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 409

Conflict.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      contentsToSave: ['C:\\\\filepath'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"contentsToSave":["C:\\\\filepath"]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths

Retrieves the allowed paths settings for the File Connector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.6+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID |

#### Responses

##### 200

The list of configuration values from the file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object[] | No |  |
| `errorMessage` | object | No |  |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The Path property in the File connector allowed paths file. |
| `spaces` | string[] | No | The Spaces property in the Odbc custom type mappings file. |

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    {
      "path": "\\\\\\\\Server\\\\Share\\\\example",
      "spaces": [
        "Foo",
        "Bar"
      ]
    }
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths

Completely replaces the contents of the allowed paths configuration file for the File Connector. Partial updates are not supported. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.6+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent id |

#### Request Body

The contents of the file to be updated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnectorAllowedPaths` | object[] | No |  |

<details>
<summary>Properties of `fileConnectorAllowedPaths`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The Path property in the File connector allowed paths file. |
| `spaces` | string[] | No | The Spaces property in the Odbc custom type mappings file. |

</details>

#### Responses

##### 204

Updated.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 409

Conflict.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      fileConnectorAllowedPaths: [
        {
          path: '\\\\\\\\Server\\\\Share\\\\example',
          spaces: ['Foo', 'Bar'],
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"fileConnectorAllowedPaths":[{"path":"\\\\\\\\Server\\\\Share\\\\example","spaces":["Foo","Bar"]}]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings

Retrieves the custom data type mapping settings for the Generic ODBC Connector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.5+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID. |

#### Responses

##### 200

The list of configuration values from the file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object[] | No |  |
| `errorMessage` | object | No |  |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The Identifier property in the ODBC custom data type mapping file. |
| `bit` | boolean | No | The IsBit property in the ODBC custom data type mapping file. |
| `size` | integer | No | The Size property in the ODBC custom data type mapping file. |
| `qlikDataType` | string | Yes | The QlikDataType property in the ODBC custom data type mapping file. |
| `nativeDataType` | string | Yes | The NativeDataType property in the ODBC custom data type mapping file. |

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    {
      "id": "Amazon Athena ODBC (x64)",
      "bit": true,
      "size": 0,
      "qlikDataType": "String",
      "nativeDataType": "varchar"
    }
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings

Completely replaces the contents of the custom data type mapping configuration file for the Generic ODBC connector. Partial updates are not supported. There are property naming differences between the API and the file contents. Use the API property format when making changes. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.5+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID. |

#### Request Body

The contents of the file to be updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `odbcCustomDataTypes` | object[] | No |  |

<details>
<summary>Properties of `odbcCustomDataTypes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The Identifier property in the ODBC custom data type mapping file. |
| `bit` | boolean | No | The IsBit property in the ODBC custom data type mapping file. |
| `size` | integer | No | The Size property in the ODBC custom data type mapping file. |
| `qlikDataType` | string | Yes | The QlikDataType property in the ODBC custom data type mapping file. |
| `nativeDataType` | string | Yes | The NativeDataType property in the ODBC custom data type mapping file. |

</details>

#### Responses

##### 204

Updated.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 409

Conflict.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      odbcCustomDataTypes: [
        {
          id: 'Amazon Athena ODBC (x64)',
          bit: true,
          size: 0,
          qlikDataType: 'String',
          nativeDataType: 'varchar',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"odbcCustomDataTypes":[{"id":"Amazon Athena ODBC (x64)","bit":true,"size":0,"qlikDataType":"String","nativeDataType":"varchar"}]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration

Retrieves the settings for the metrics collector. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.9+.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID. |

#### Responses

##### 200

The list of configuration values from the file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object | No |  |
| `errorMessage` | object | No |  |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorConfigurations` | object | No |  |
| `metricsCollectorSettings` | object | No |  |

<details>
<summary>Properties of `connectorConfigurations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnector` | object | No |  |
| `odbcConnector` | object | No |  |
| `restConnector` | object | No |  |
| `systemMetrics` | object | No |  |
| `connectorAgent` | object | No |  |
| `sapBwConnector` | object | No |  |
| `sapSqlConnector` | object | No |  |
| `sapPackageConnector` | object | No |  |

<details>
<summary>Properties of `fileConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `odbcConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `restConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `systemMetrics`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `connectorAgent`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapBwConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapSqlConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapPackageConnector`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metricsCollectorSettings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `port` | integer | Yes | The port number that the metrics collector API will run on. This must match the port that the SYSTEM connector runs on to enable network metrics collection. |
| `enabled` | boolean | Yes | Indicates whether the metrics collector is enabled. |
| `localDataRetentionDays` | integer | Yes | The number of days to retain local data. |
| `baseScrapeIntervalSeconds` | integer | Yes | The base interval in seconds for the metrics collection loop. This defines how frequently the collector checks whether to scrape each connector, not the interval at which each connector is scraped. Must be equal to or less than the lowest individual connector scrape interval. |
| `localDatabaseFileLocation` | string | No | The file location for the local metrics database. If not specified, defaults to `C:\ProgramData\Qlik\Gateway\tmp`. |
| `dataRetentionCheckIntervalMinutes` | integer | Yes | The interval in minutes the metrics collector checks for and deletes old data. |
| `localDataRetentionDatabaseSizeInMb` | integer | No | The maximum size of the local database in megabytes. |

</details>

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": {
    "connectorConfigurations": {
      "fileConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "odbcConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "restConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "systemMetrics": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "connectorAgent": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapBwConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapSqlConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapPackageConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      }
    },
    "metricsCollectorSettings": {
      "port": 5052,
      "enabled": false,
      "localDataRetentionDays": 30,
      "baseScrapeIntervalSeconds": 1,
      "localDatabaseFileLocation": "",
      "dataRetentionCheckIntervalMinutes": 60,
      "localDataRetentionDatabaseSizeInMb": 500
    }
  },
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration

Completely replaces the contents of the metrics collector settings configuration file. Partial updates are not supported.  Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.9+.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The agent ID. |

#### Request Body

The contents of the file to be updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorConfigurations` | object | Yes |  |
| `metricsCollectorSettings` | object | Yes |  |

<details>
<summary>Properties of `connectorConfigurations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnector` | object | Yes |  |
| `odbcConnector` | object | Yes |  |
| `restConnector` | object | Yes |  |
| `systemMetrics` | object | Yes |  |
| `connectorAgent` | object | Yes |  |
| `sapBwConnector` | object | Yes |  |
| `sapSqlConnector` | object | Yes |  |
| `sapPackageConnector` | object | Yes |  |

<details>
<summary>Properties of `fileConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `odbcConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `restConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `systemMetrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `connectorAgent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapBwConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapSqlConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapPackageConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

</details>

<details>
<summary>Properties of `metricsCollectorSettings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `port` | integer | Yes | The port number that the metrics collector API will run on. This must match the port that the SYSTEM connector runs on to enable network metrics collection. |
| `enabled` | boolean | Yes | Indicates whether the metrics collector is enabled. |
| `localDataRetentionDays` | integer | Yes | The number of days to retain local data. |
| `baseScrapeIntervalSeconds` | integer | Yes | The base interval in seconds for the metrics collection loop. This defines how frequently the collector checks whether to scrape each connector, not the interval at which each connector is scraped. Must be equal to or less than the lowest individual connector scrape interval. |
| `localDatabaseFileLocation` | string | Yes | The file location for the local metrics database. If not specified, defaults to `C:\ProgramData\Qlik\Gateway\tmp`. |
| `dataRetentionCheckIntervalMinutes` | integer | Yes | The interval in minutes the metrics collector checks for and deletes old data. |
| `localDataRetentionDatabaseSizeInMb` | integer | No | The maximum size of the local database in megabytes. Default is 500 MB. |

</details>

#### Responses

##### 204

Updated.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Configuration file not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 409

Conflict.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |
| `hasErrors` | boolean | No |  |

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
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      connectorConfigurations: {
        fileConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        odbcConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        restConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        systemMetrics: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        connectorAgent: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapBwConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapSqlConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapPackageConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
      },
      metricsCollectorSettings: {
        port: 5052,
        enabled: false,
        localDataRetentionDays: 30,
        baseScrapeIntervalSeconds: 1,
        localDatabaseFileLocation: '',
        dataRetentionCheckIntervalMinutes: 60,
        localDataRetentionDatabaseSizeInMb: 500,
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"connectorConfigurations":{"fileConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"odbcConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"restConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"systemMetrics":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"connectorAgent":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapBwConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapSqlConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapPackageConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false}},"metricsCollectorSettings":{"port":5052,"enabled":false,"localDataRetentionDays":30,"baseScrapeIntervalSeconds":1,"localDatabaseFileLocation":"","dataRetentionCheckIntervalMinutes":60,"localDataRetentionDatabaseSizeInMb":500}}'
```

---
