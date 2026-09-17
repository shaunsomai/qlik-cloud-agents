# Data integration projects

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data integration projects are used to group and organize data tasks that move, transform, or prepare data for consumption.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/di-projects`](#get-apiv1di-projects) | List data integration projects. |
| `POST` | [`/api/v1/di-projects`](#post-apiv1di-projects) | Creates a new data integration project in the specified space. |
| `GET` | [`/api/v1/di-projects/{projectId}`](#get-apiv1di-projectsprojectid) | Get a specific data integration project. |
| `POST` | [`/api/v1/di-projects/{projectId}/actions/export`](#post-apiv1di-projectsprojectidactionsexport) | Exports the specified data integration project. |
| `POST` | [`/api/v1/di-projects/{projectId}/actions/import`](#post-apiv1di-projectsprojectidactionsimport) | Imports a data integration project synchronously from a legacy JSON-based `.zip` file. |
| `POST` | [`/api/v1/di-projects/{projectId}/actions/import-async`](#post-apiv1di-projectsprojectidactionsimport-async) | Imports a data integration project from a `.zip` file and returns an action identifier for tracking the background import operation. Accepts both JSON-based (legacy) and YAML-based project formats, making it the recommended endpoint for deploying YAML-defined pipeline definitions programmatically. Poll the import status using `GET /di-projects/actions/{actionId}`. |
| `POST` | [`/api/v1/di-projects/{projectId}/actions/prepare`](#post-apiv1di-projectsprojectidactionsprepare) | Prepares the data integration project and its tasks for execution. |
| `POST` | [`/api/v1/di-projects/{projectId}/actions/validate`](#post-apiv1di-projectsprojectidactionsvalidate) | Validates the data integration project and its tasks. |
| `GET` | [`/api/v1/di-projects/{projectId}/bindings`](#get-apiv1di-projectsprojectidbindings) | Retrieves the export variables for a specific data integration project. |
| `PUT` | [`/api/v1/di-projects/{projectId}/bindings`](#put-apiv1di-projectsprojectidbindings) | Updates the export variables for a specific data integration project. |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks`](#get-apiv1di-projectsprojectiddi-tasks) | Lists data tasks within a given data integration project. |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}`](#get-apiv1di-projectsprojectiddi-tasksdatataskid) | Get a specific data task within a project. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare`](#post-apiv1di-projectsprojectiddi-tasksdatataskidactionsprepare) | Prepares the specified data task for execution. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets`](#post-apiv1di-projectsprojectiddi-tasksdatataskidactionsrecreate-datasets) | Recreates datasets in the specified data task. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload`](#post-apiv1di-projectsprojectiddi-tasksdatataskidactionsrequest-reload) | Registers a request to reload the datasets associated with the specified data task. The reload does not occur immediately; it will take effect on the next scheduled or manual run of the task. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate`](#post-apiv1di-projectsprojectiddi-tasksdatataskidactionsvalidate) | Validates the specified data task. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start`](#post-apiv1di-projectsprojectiddi-tasksdatataskidruntimeactionsstart) | Start a data task on a data integration project. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop`](#post-apiv1di-projectsprojectiddi-tasksdatataskidruntimeactionsstop) | Stop a data task on a data integration project. |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state`](#get-apiv1di-projectsprojectiddi-tasksdatataskidruntimerunsrunidstate) | Returns the state of a specific historical run instance for a data task, including execution progress and any errors encountered. |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets`](#get-apiv1di-projectsprojectiddi-tasksdatataskidruntimerunsrunidstatedatasets) | Returns dataset-level state for a specific historical run instance of a data task. All datasets for the run are returned in a single response; this endpoint does not paginate. |
| `POST` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search`](#post-apiv1di-projectsprojectiddi-tasksdatataskidruntimerunsactionssearch) | Returns a paginated list of historical run instances for the specified data task, filtered by the provided criteria. |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state`](#get-apiv1di-projectsprojectiddi-tasksdatataskidruntimestate) | Get the current runtime state of a data task |
| `GET` | [`/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets`](#get-apiv1di-projectsprojectiddi-tasksdatataskidruntimestatedatasets) | Returns dataset-level runtime state for a data task |
| `GET` | [`/api/v1/di-projects/actions/{actionId}`](#get-apiv1di-projectsactionsactionid) | Retrieves the status of an asynchronous operation. |
| `POST` | [`/api/v1/di-projects/utils/actions/validate-project-definitions`](#post-apiv1di-projectsutilsactionsvalidate-project-definitions) | Validates the project definition files in a `.zip` and returns a structured report of warnings and errors. The validation runs synchronously and completes before the response is returned. Use this operation before importing with `POST /di-projects/{projectId}/actions/import-async` to confirm that YAML-based pipeline definitions are correct. |

## API Reference

### GET /api/v1/di-projects

List data integration projects.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | No | Filter by space id |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projects` | object[] | No |  |

<details>
<summary>Properties of `projects`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No | The type of the project Enum: "DATA_PIPELINE", "DATA_MOVEMENT" |
| `ownerId` | string | No |  |
| `spaceId` | string | No |  |
| `description` | string | No |  |
| `platformType` | string | No | The platform type of the project. Supported values: - SNOWFLAKE: Snowflake - BIGQUERY: Google BigQuery - SYNAPSE: Azure Synapse - DATABRICKS: Databricks - REDSHIFT: Amazon Redshift - MSSQL: Microsoft SQL Server - FABRIC: Microsoft Fabric (OneLake) - QLIK_QVD: Qlik-managed QVD - QLIK_QVD_CUSTOMER_MANAGED: Customer-managed QVD - QLIK_OPEN_LAKEHOUSE: Qlik Open Lakehouse - NONE: No platform (e.g. replication-only projects)  Enum: "SNOWFLAKE", "BIGQUERY", "SYNAPSE", "DATABRICKS", "REDSHIFT", "MSSQL", "FABRIC", "QLIK_QVD", "QLIK_QVD_CUSTOMER_MANAGED", "QLIK_OPEN_LAKEHOUSE", "NONE" |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "projects": [
    {
      "id": "string",
      "name": "string",
      "type": "DATA_PIPELINE",
      "ownerId": "string",
      "spaceId": "string",
      "description": "string",
      "platformType": "SNOWFLAKE"
    }
  ]
}
```

---

### POST /api/v1/di-projects

Creates a new data integration project in the specified space.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The details of the project to create

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of the project |
| `type` | string | No | The type of the project Enum: "DATA_PIPELINE", "DATA_MOVEMENT" |
| `space` | string | No | The ID of the space where the project will be created |
| `description` | string | No | A description of the project |
| `platformType` | string | No | The platform type of the project. Supported values: - SNOWFLAKE: Snowflake - BIGQUERY: Google BigQuery - SYNAPSE: Azure Synapse - DATABRICKS: Databricks - REDSHIFT: Amazon Redshift - MSSQL: Microsoft SQL Server - FABRIC: Microsoft Fabric (OneLake) - QLIK_QVD: Qlik-managed QVD - QLIK_QVD_CUSTOMER_MANAGED: Customer-managed QVD - QLIK_OPEN_LAKEHOUSE: Qlik Open Lakehouse - NONE: No platform (e.g. replication-only projects)  Enum: "SNOWFLAKE", "BIGQUERY", "SYNAPSE", "DATABRICKS", "REDSHIFT", "MSSQL", "FABRIC", "QLIK_QVD", "QLIK_QVD_CUSTOMER_MANAGED", "QLIK_OPEN_LAKEHOUSE", "NONE" |
| `platformConnection` | string | No | The platform connection string |
| `cloudStagingConnection` | string | No | The cloud staging connection string |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No | The type of the project Enum: "DATA_PIPELINE", "DATA_MOVEMENT" |
| `ownerId` | string | No |  |
| `spaceId` | string | No |  |
| `description` | string | No |  |
| `platformType` | string | No | The platform type of the project. Supported values: - SNOWFLAKE: Snowflake - BIGQUERY: Google BigQuery - SYNAPSE: Azure Synapse - DATABRICKS: Databricks - REDSHIFT: Amazon Redshift - MSSQL: Microsoft SQL Server - FABRIC: Microsoft Fabric (OneLake) - QLIK_QVD: Qlik-managed QVD - QLIK_QVD_CUSTOMER_MANAGED: Customer-managed QVD - QLIK_OPEN_LAKEHOUSE: Qlik Open Lakehouse - NONE: No platform (e.g. replication-only projects)  Enum: "SNOWFLAKE", "BIGQUERY", "SYNAPSE", "DATABRICKS", "REDSHIFT", "MSSQL", "FABRIC", "QLIK_QVD", "QLIK_QVD_CUSTOMER_MANAGED", "QLIK_OPEN_LAKEHOUSE", "NONE" |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'New Project',
      type: 'DATA_PIPELINE',
      space: 'space-456',
      description:
        'This is a new data integration project.',
      platformType: 'SNOWFLAKE',
      platformConnection: 'connection-string',
      cloudStagingConnection:
        'storage-connection-string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"New Project","type":"DATA_PIPELINE","space":"space-456","description":"This is a new data integration project.","platformType":"SNOWFLAKE","platformConnection":"connection-string","cloudStagingConnection":"storage-connection-string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "type": "DATA_PIPELINE",
  "ownerId": "string",
  "spaceId": "string",
  "description": "string",
  "platformType": "SNOWFLAKE"
}
```

---

### GET /api/v1/di-projects/{projectId}

Get a specific data integration project.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No | The type of the project Enum: "DATA_PIPELINE", "DATA_MOVEMENT" |
| `ownerId` | string | No |  |
| `spaceId` | string | No |  |
| `description` | string | No |  |
| `platformType` | string | No | The platform type of the project. Supported values: - SNOWFLAKE: Snowflake - BIGQUERY: Google BigQuery - SYNAPSE: Azure Synapse - DATABRICKS: Databricks - REDSHIFT: Amazon Redshift - MSSQL: Microsoft SQL Server - FABRIC: Microsoft Fabric (OneLake) - QLIK_QVD: Qlik-managed QVD - QLIK_QVD_CUSTOMER_MANAGED: Customer-managed QVD - QLIK_OPEN_LAKEHOUSE: Qlik Open Lakehouse - NONE: No platform (e.g. replication-only projects)  Enum: "SNOWFLAKE", "BIGQUERY", "SYNAPSE", "DATABRICKS", "REDSHIFT", "MSSQL", "FABRIC", "QLIK_QVD", "QLIK_QVD_CUSTOMER_MANAGED", "QLIK_OPEN_LAKEHOUSE", "NONE" |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "type": "DATA_PIPELINE",
  "ownerId": "string",
  "spaceId": "string",
  "description": "string",
  "platformType": "SNOWFLAKE"
}
```

---

### POST /api/v1/di-projects/{projectId}/actions/export

Exports the specified data integration project.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | Optional; only 'application/octet-stream' is supported. Enum: "application/octet-stream" |

#### Request Body

Options for the export process

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `mode` | string | No | Defines the export format for the project files. - 'LEGACY': Exports a ZIP of the previous JSON files. Deprecated and will be removed in a future release. - 'MINIMAL': Exports a ZIP of the new YAML files, including only non-default attribute values. - 'ALL': Exports a ZIP of the new YAML files, including all attributes.  Enum: "MINIMAL", "ALL", "LEGACY" |
| `includeBindings` | boolean | No | Include bindings in the exported zip file. If not specified, defaults to `false`. |

#### Responses

##### 200

OK

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/actions/export` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/actions/export',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      mode: 'MINIMAL',
      includeBindings: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/actions/export yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/actions/export" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"mode":"MINIMAL","includeBindings":false}' \
-o "output-file"
```

---

### POST /api/v1/di-projects/{projectId}/actions/import

Imports a data integration project synchronously from a legacy JSON-based `.zip` file.
This endpoint only accepts zips that contain JSON project files (the legacy format). The import is processed synchronously and completes before the response is returned.
Submitting a YAML-based zip to this endpoint returns `400`. To import a YAML-based zip, use `POST /di-projects/{projectId}/actions/import-async` instead.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

The ZIP file containing the JSON-based project to import.

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `zip` | string | No |  |

#### Responses

##### 200

OK — the JSON-based project was imported successfully.

**Content-Type:** `application/json`


##### 400

Bad Request — for example, if a YAML-based zip is submitted to this endpoint.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/actions/import` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/actions/import',
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
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/actions/import yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/actions/import" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "zip=@/path/to/file"
```

**Example Response:**

```json
{}
```

---

### POST /api/v1/di-projects/{projectId}/actions/import-async

Imports a data integration project from a `.zip` file and returns an action identifier for tracking the background import operation. Accepts both JSON-based (legacy) and YAML-based project formats, making it the recommended endpoint for deploying YAML-defined pipeline definitions programmatically. Poll the import status using `GET /di-projects/actions/{actionId}`.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

A `.zip` file containing the project to import. Accepts both JSON-based (legacy) and YAML-based formats.

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `zip` | string | No |  |

#### Responses

##### 202

The project import has started. Poll the returned `actionId` using `GET /di-projects/actions/{actionId}` to track progress.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/actions/import-async` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/actions/import-async',
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
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/actions/import-async yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/actions/import-async" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "zip=@/path/to/file"
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### POST /api/v1/di-projects/{projectId}/actions/prepare

Prepares the data integration project and its tasks for execution.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `allowRecreate` | boolean | No |  |
| `selectedTasks` | object[] | No | Array of tasks to prepare. Leave empty to trigger project-level orchestration using built-in logic (same as in the user interface). |

<details>
<summary>Properties of `selectedTasks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | Task identifier |

</details>

#### Responses

##### 202

Preparation started

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Project not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/actions/prepare` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/actions/prepare',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      allowRecreate: false,
      selectedTasks: [{ taskId: 'string' }],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/actions/prepare yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/actions/prepare" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"allowRecreate":false,"selectedTasks":[{"taskId":"string"}]}'
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### POST /api/v1/di-projects/{projectId}/actions/validate

Validates the data integration project and its tasks.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectedTasks` | object[] | No | Array of tasks to prepare. Leave empty to trigger project-level orchestration using built-in logic (same as in the user interface). |

<details>
<summary>Properties of `selectedTasks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | Task identifier |

</details>

#### Responses

##### 202

Validation started

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Project not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/actions/validate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/actions/validate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      selectedTasks: [{ taskId: 'string' }],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/actions/validate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/actions/validate" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"selectedTasks":[{"taskId":"string"}]}'
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### GET /api/v1/di-projects/{projectId}/bindings

Retrieves the export variables for a specific data integration project.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recalculate` | boolean | No | Recalculate the bindings if true, otherwise saved bindings are returned. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object | No |  |
| `nameToIdMap` | object | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/bindings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/bindings',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/bindings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/bindings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "variables": {},
  "nameToIdMap": {}
}
```

---

### PUT /api/v1/di-projects/{projectId}/bindings

Updates the export variables for a specific data integration project.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

The details of the export variables to update

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`


##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/di-projects/{projectId}/bindings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/bindings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ variables: {} }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/di-projects/{projectId}/bindings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/bindings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"variables":{}}'
```

**Example Response:**

```json
{}
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks

Lists data tasks within a given data integration project.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTasks` | object[] | No |  |

<details>
<summary>Properties of `dataTasks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No | Enum: "LANDING", "STORAGE", "QVD_STORAGE", "TRANSFORM", "DATAMART", "REGISTERED_DATA", "REPLICATION", "DISTRIBUTION", "LAKE_LANDING", "KNOWLEDGE_MART", "FILE_BASED_KNOWLEDGE_MART", "LAKEHOUSE_STORAGE", "LAKEHOUSE_MIRROR", "STREAMING_LAKE_LANDING", "STREAMING_TRANSFORM", "REPLICATE_LANDING" |
| `ownerId` | string | No |  |
| `spaceId` | string | No |  |
| `description` | string | No |  |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "dataTasks": [
    {
      "id": "string",
      "name": "string",
      "type": "LANDING",
      "ownerId": "string",
      "spaceId": "string",
      "description": "string"
    }
  ]
}
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}

Get a specific data task within a project.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No | Enum: "LANDING", "STORAGE", "QVD_STORAGE", "TRANSFORM", "DATAMART", "REGISTERED_DATA", "REPLICATION", "DISTRIBUTION", "LAKE_LANDING", "KNOWLEDGE_MART", "FILE_BASED_KNOWLEDGE_MART", "LAKEHOUSE_STORAGE", "LAKEHOUSE_MIRROR", "STREAMING_LAKE_LANDING", "STREAMING_TRANSFORM", "REPLICATE_LANDING" |
| `ownerId` | string | No |  |
| `spaceId` | string | No |  |
| `description` | string | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "type": "LANDING",
  "ownerId": "string",
  "spaceId": "string",
  "description": "string"
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare

Prepares the specified data task for execution.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `allowRecreate` | boolean | Yes | Allow recreation of existing artifacts |

#### Responses

##### 202

Preparation started

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Task not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      allowRecreate: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"allowRecreate":false}'
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets

Recreates datasets in the specified data task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Content-Type:** `application/json`


#### Responses

##### 202

Started recreating datasets

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Task or project not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({}),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{}'
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload

Registers a request to reload the datasets associated with the specified data task. The reload does not occur immediately; it will take effect on the next scheduled or manual run of the task.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadStrategy` | string | No | Reload strategy (optional, applies to materialized SQL transformations and transformation flows tasks) Enum: "NONE", "TRUNCATE", "COMPARE_AND_APPLY" |
| `selectedDatasets` | object[] | No | Datasets to reload (optional, if omitted or empty, all datasets will be reloaded). |

<details>
<summary>Properties of `selectedDatasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | No |  |

</details>

#### Responses

##### 200

Reload request registered.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `success` | boolean | Yes | Always true when the server successfully registers the request. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      reloadStrategy: 'NONE',
      selectedDatasets: [{ datasetId: 'string' }],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"reloadStrategy":"NONE","selectedDatasets":[{"datasetId":"string"}]}'
```

**Example Response:**

```json
{
  "success": true
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate

Validates the specified data task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Content-Type:** `application/json`


#### Responses

##### 202

Validation started

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier for tracking the action |

##### 400

Invalid request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Task not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({}),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/validate" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{}'
```

**Example Response:**

```json
{
  "actionId": "action-123456"
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start

Start a data task on a data integration project.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `option` | string | No | Task run option for the task (optional, applies to Replication tasks only). Enum: "PROCESS_CHANGES_FROM_TIMESTAMP", "PROCESS_CHANGES_FROM_POSITION", "RECOVER_USING_LOCALLY_STORED_CHECKPOINT" |
| `processChangesFrom` | string | No | The value indicating where to resume the process, either a timestamp or an offset depending on the run option (optional, applies to Replication tasks only). |

#### Responses

##### 204

NO CONTENT

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      option: 'PROCESS_CHANGES_FROM_TIMESTAMP',
      processChangesFrom: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"option":"PROCESS_CHANGES_FROM_TIMESTAMP","processChangesFrom":"string"}'
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop

Stop a data task on a data integration project.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 204

NO CONTENT

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop',
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
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/stop" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state

Returns the state of a specific historical run instance for a data task, including execution progress and any errors encountered.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |
| `runId` | string | Yes | Identifier of the run instance. |

#### Responses

##### 200

Run execution state retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the data task |
| `type` | string | No | Enum: "LANDING", "STORAGE", "QVD_STORAGE", "TRANSFORM", "DATAMART", "REGISTERED_DATA", "REPLICATION", "DISTRIBUTION", "LAKE_LANDING", "KNOWLEDGE_MART", "FILE_BASED_KNOWLEDGE_MART", "LAKEHOUSE_STORAGE", "LAKEHOUSE_MIRROR", "STREAMING_LAKE_LANDING", "STREAMING_TRANSFORM", "REPLICATE_LANDING" |
| `lastRun` | object | No | Represents the execution state of a task instance, including progress metrics, errors, and operation-specific statistics. |
| `runReadiness` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "STARTING", "RUNNING", "COMPLETED", "FAILED", "CANCELED", "STOPPING" |
| `errors` | object[] | No | List of errors encountered during the last run |
| `endTime` | string | No | Timestamp indicating when the task instance ended |
| `general` | object | No | Overall task execution statistics including dataset counts, data freshness timestamps, and infrastructure details. |
| `message` | string | No |  |
| `traceId` | string | No | Trace identifier for the last run, useful for diagnostics and support |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fullLoad` | object | No | Statistics for the full load phase of the task run, tracking dataset processing progress. |
| `cdcStatus` | object | No | Change Data Capture status information for tasks performing incremental updates, including latency and processing counts. |
| `startTime` | string | No | Timestamp indicating when the task instance started |
| `streaming` | object | No | Real-time streaming statistics for tasks that continuously process data streams. |
| `lastBatchOfChanges` | object | No | Statistics for the most recent batch of changes processed during the task run, including timing and throughput metrics. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `general`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `gatewayId` | string | No | For tasks that run on a gateway, this is the id of the gateway |
| `gatewayName` | string | No | For tasks that run on a gateway, this is the name of the gateway |
| `datasetCount` | number | No | Total number of datasets produced by the task, including ones in error |
| `gatewayTaskName` | string | No | For tasks that run on a gateway, this is the internal name of the task on the gateway |
| `dataTaskUpdatedTo` | string | No | The latest point in time the data reflects, based on updates from the source system. |
| `lakehouseClusterId` | string | No | For lakehouse storage tasks, this is the id of the cluster where the task runs |
| `liveViewsUpdatedTo` | string | No | The latest point in time the live views reflect, based on updates from the source system. |
| `datasetsInErrorCount` | number | No | Count of datasets that encountered errors |
| `lakehouseClusterName` | string | No | For lakehouse storage tasks, this is the name of the cluster where the task runs |

</details>

<details>
<summary>Properties of `fullLoad`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errorCount` | number | No | Number of datasets that have failed full load in this task run |
| `queuedCount` | number | No | Number of datasets that are queued for full load in this task run |
| `loadingCount` | number | No | Number of datasets that are currently being loaded in this task run |
| `completedCount` | number | No | Number of datasets that have completed full load in this task run |

</details>

<details>
<summary>Properties of `cdcStatus`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `totalProcessedCount` | number | No |  |
| `applyingChangesCount` | number | No |  |
| `incomingChangesCount` | number | No | Number of incoming changes. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |
| `accumulatingChangesCount` | number | No |  |
| `throughputInKilobytesPerSecond` | number | No | Throughput in kilobytes per second |

</details>

<details>
<summary>Properties of `streaming`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `errorCount` | number | No | Number of streaming datasets that have encountered errors |
| `queuedCount` | number | No | Number of streaming datasets that are queued |
| `runningCount` | number | No | Number of streaming datasets that are currently running |
| `totalProcessedCount` | number | No | Total number of records processed |

</details>

<details>
<summary>Properties of `lastBatchOfChanges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `relatesToRecordsTo` | string | No | This batch ends with operational source changes from this time. |
| `totalProcessedCount` | number | No |  |
| `relatesToRecordsFrom` | string | No | This batch starts with operational source changes from this time. |
| `throughputInRecordsPerSecond` | number | No | Throughput in records per second |

</details>

</details>

<details>
<summary>Properties of `runReadiness`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "READY_TO_RUN", "ALREADY_RUNNING", "NOT_RUNNABLE" |
| `message` | string | No |  |

</details>

##### 400

Invalid request or missing parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Task run not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "name": "string",
  "type": "LANDING",
  "lastRun": {
    "state": "STARTING",
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string",
        "source": {
          "pointer": "string",
          "parameter": "string"
        },
        "status": 42
      }
    ],
    "endTime": "2018-10-30T07:06:22Z",
    "general": {
      "gatewayId": "string",
      "gatewayName": "string",
      "datasetCount": 42,
      "gatewayTaskName": "string",
      "dataTaskUpdatedTo": "2018-10-30T07:06:22Z",
      "lakehouseClusterId": "string",
      "liveViewsUpdatedTo": "2018-10-30T07:06:22Z",
      "datasetsInErrorCount": 42,
      "lakehouseClusterName": "string"
    },
    "message": "string",
    "traceId": "string",
    "duration": "string",
    "fullLoad": {
      "errorCount": 42,
      "queuedCount": 42,
      "loadingCount": 42,
      "completedCount": 42
    },
    "cdcStatus": {
      "latency": "01:30:45",
      "totalProcessedCount": 42,
      "applyingChangesCount": 42,
      "incomingChangesCount": 42,
      "accumulatingChangesCount": 42,
      "throughputInKilobytesPerSecond": 42
    },
    "startTime": "2018-10-30T07:06:22Z",
    "streaming": {
      "latency": "string",
      "errorCount": 42,
      "queuedCount": 42,
      "runningCount": 42,
      "totalProcessedCount": 42
    },
    "lastBatchOfChanges": {
      "relatesToRecordsTo": "2018-10-30T07:06:22Z",
      "totalProcessedCount": 42,
      "relatesToRecordsFrom": "2018-10-30T07:06:22Z",
      "throughputInRecordsPerSecond": 42
    }
  },
  "runReadiness": {
    "state": "READY_TO_RUN",
    "message": "string"
  }
}
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets

Returns dataset-level state for a specific historical run instance of a data task. All datasets for the run are returned in a single response; this endpoint does not paginate.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |
| `runId` | string | Yes | Identifier of the run instance. |

#### Responses

##### 200

Dataset-level state for the specified run instance retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasets` | object[] | No | Represents the execution state of a single dataset within a task run, including full load, CDC, and streaming progress. |

<details>
<summary>Properties of `datasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the dataset |
| `fullLoad` | object | No |  |
| `cdcStatus` | object | No | Change Data Capture state for the dataset, tracking incremental changes applied and any errors. |
| `datasetId` | string | No | Id of the dataset |
| `streaming` | object | No | Real-time streaming state for the dataset, tracking record processing and transformation statistics. |
| `sourceName` | string | No | Original name of the dataset, relevant only for data movement tasks |
| `dataReadiness` | string | No | Is the data ready for use? Enum: "READY", "NOT_READY", "ERROR" |
| `lastBatchOfChanges` | object | No |  |

<details>
<summary>Properties of `fullLoad`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "LOADING", "COMPLETED", "ERROR" |
| `endTime` | string | No |  |
| `message` | string | No |  |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fileStats` | object | No | Statistics for file-based tasks. |
| `startTime` | string | No |  |
| `cachedChangesCount` | number | No | Number of changes captured and cached during full load (CDC landing/replication tasks only) |
| `failedRecordsCount` | number | No | Number of records that failed to load (currently only for knowledge marts) |
| `totalProcessedCount` | number | No | Number of records (or docs in knowledge marts) were loaded. |

<details>
<summary>Properties of `fileStats`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `cdcStatus`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "PROCESSING", "ACCUMULATING_CHANGES", "COMPLETED", "ERROR" |
| `message` | string | No |  |
| `ddlCount` | number | No | Number of DDL statements executed during the last run |
| `deleteCount` | number | No | delete portion of totalProcessedCount. Only available for some task types |
| `insertCount` | number | No | Insert portion of totalProcessedCount. Only available for some task types |
| `updateCount` | number | No | update portion of totalProcessedCount. Only available for some task types |
| `lastProcessed` | string | No |  |
| `totalProcessedCount` | number | No | Total number of changes/DMLs applied to the dataset |
| `incomingChangesCount` | number | No | Number of incoming changes for the dataset. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |
| `unoptimizedRecordsCount` | number | No | Number of records that are queryable via the view, but not yet merged into optimized Iceberg partitions. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |

</details>

<details>
<summary>Properties of `streaming`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "RUNNING", "ERROR" |
| `message` | string | No |  |
| `lastProcessed` | string | No | Timestamp of the latest source record inserted into the target dataset. |
| `parseIssueCount` | number | No | Number of records that had parsing issues |
| `recordsWrittenCount` | number | No | Total number of records written to the dataset |
| `totalProcessedCount` | number | No | Total number of processed changes for the dataset |
| `recordsFilteredCount` | number | No | Total number of records filtered out and not written to the dataset |
| `unoptimizedRecordsCount` | number | No | Queryable records pending merge into optimized Iceberg partitions. |

</details>

<details>
<summary>Properties of `lastBatchOfChanges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "PROCESSING", "COMPLETED", "ERROR" |
| `endTime` | string | No |  |
| `message` | string | No |  |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fileStats` | object | No | Statistics for file-based tasks. |
| `startTime` | string | No |  |
| `operationStats` | object | No | Breakdown of operations for record-oriented tasks. |
| `totalProcessedCount` | number | No |  |
| `throughputInRecordsPerSecond` | number | No | Throughput in records per second |

<details>
<summary>Properties of `fileStats`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `operationStats`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Invalid request or missing parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Task run not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 410

Gone — the dataset state for this run has been purged due to retention policy.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 413

Payload Too Large — the dataset state for this run exceeds the per-response size limit. This is a soft guard against pathologically large tasks; if you hit this consistently, contact support.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "datasets": [
    {
      "name": "string",
      "fullLoad": {
        "state": "QUEUED",
        "endTime": "2018-10-30T07:06:22Z",
        "message": "string",
        "duration": "string",
        "fileStats": {
          "volume": "string",
          "processedCount": 42
        },
        "startTime": "2018-10-30T07:06:22Z",
        "cachedChangesCount": 42,
        "failedRecordsCount": 42,
        "totalProcessedCount": 42
      },
      "cdcStatus": {
        "state": "QUEUED",
        "message": "string",
        "ddlCount": 42,
        "deleteCount": 42,
        "insertCount": 42,
        "updateCount": 42,
        "lastProcessed": "2018-10-30T07:06:22Z",
        "totalProcessedCount": 42,
        "incomingChangesCount": 42,
        "unoptimizedRecordsCount": 42
      },
      "datasetId": "string",
      "streaming": {
        "state": "QUEUED",
        "message": "string",
        "lastProcessed": "2018-10-30T07:06:22Z",
        "parseIssueCount": 42,
        "recordsWrittenCount": 42,
        "totalProcessedCount": 42,
        "recordsFilteredCount": 42,
        "unoptimizedRecordsCount": 42
      },
      "sourceName": "string",
      "dataReadiness": "READY",
      "lastBatchOfChanges": {
        "state": "QUEUED",
        "endTime": "2018-10-30T07:06:22Z",
        "message": "string",
        "duration": "string",
        "fileStats": {
          "volume": "string",
          "processedCount": 42
        },
        "startTime": "2018-10-30T07:06:22Z",
        "operationStats": {
          "deleteCount": 42,
          "failedCount": 42,
          "insertCount": 42,
          "updateCount": 42
        },
        "totalProcessedCount": 42,
        "throughputInRecordsPerSecond": 42
      }
    }
  ]
}
```

---

### POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search

Returns a paginated list of historical run instances for the specified data task, filtered by the provided criteria.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Request Body

**Required**

Search criteria and pagination options for task run history query.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Maximum number of runs to return. |
| `lastId` | string | No | Cursor for paging. Pass the `runId` of the last item from the previous response to fetch the next page; omit on the first request. |
| `filters` | object[] | No | Field filters to apply to the search. |

<details>
<summary>Properties of `filters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `field` | string | Yes | The run-history field to filter on. Enum: "ID", "STATUS", "SUB_STATUS", "PERIOD" |
| `value` | string[] | Yes | Values to match. For `BETWEEN` on `PERIOD`, supply exactly two ISO-8601 timestamps. |
| `operator` | string | Yes | Filter operator. - `IN` / `NOT_IN`: exact match against the values list (recommended for ID, STATUS, SUB_STATUS). - `BETWEEN`: only valid with the `PERIOD` field. The `value` list must contain two ISO-8601 timestamps (start, end).  Enum: "IN", "NOT_IN", "BETWEEN" |

</details>

#### Responses

##### 200

Search results retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `runs` | object[] | No | List of task run instances matching the search. |
| `lastId` | string | No | Identifier of the last run in this page. Pass this value back as `lastId` in the next request to fetch the following page. |
| `nextPageExists` | boolean | No | True when more pages are available after this one; false when this is the last page. |

<details>
<summary>Properties of `runs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `runId` | string | No | Identifier of the run instance. |
| `status` | string | No | Execution status of a task run instance. Enum: "STARTING", "RUNNING", "COMPLETED", "FAILED", "CANCELED", "MISFIRED" |
| `endTime` | string | No | Timestamp indicating when the run ended. |
| `duration` | string | No | Duration of the run in HH:MM:SS format. |
| `startTime` | string | No | Timestamp indicating when the run started. |
| `subStatus` | string | No | Sub-status of the run, when applicable. |
| `errorMessage` | string | No | Error message, if the run failed. |
| `datasetsCount` | integer | No | Total number of datasets processed in this run. |
| `originSubStatus` | string | No | Origin-specific sub-status of the run, when applicable. |
| `datasetsErrorCount` | integer | No | Number of datasets that encountered errors in this run. |

</details>

##### 400

Invalid request. Check parameter formats and filter syntax.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Project or task not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      limit: 50,
      lastId:
        'caf50cbf-d6f8-47c6-a5e0-b31e0d11102a',
      filters: [
        {
          field: 'STATUS',
          value: ['COMPLETED', 'FAILED'],
          operator: 'IN',
        },
        {
          field: 'PERIOD',
          value: [
            '2024-03-01T00:00:00Z',
            '2024-03-31T23:59:59Z',
          ],
          operator: 'BETWEEN',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"limit":50,"lastId":"caf50cbf-d6f8-47c6-a5e0-b31e0d11102a","filters":[{"field":"STATUS","value":["COMPLETED","FAILED"],"operator":"IN"},{"field":"PERIOD","value":["2024-03-01T00:00:00Z","2024-03-31T23:59:59Z"],"operator":"BETWEEN"}]}'
```

**Example Response:**

```json
{
  "runs": [
    {
      "runId": "caf50cbf-d6f8-47c6-a5e0-b31e0d11102a",
      "status": "STARTING",
      "endTime": "2024-03-01T09:30:00Z",
      "duration": "00:30:00",
      "startTime": "2024-03-01T09:00:00Z",
      "subStatus": "string",
      "errorMessage": "",
      "datasetsCount": 10,
      "originSubStatus": "string",
      "datasetsErrorCount": 0
    }
  ],
  "lastId": "caf50cbf-d6f8-47c6-a5e0-b31e0d11102a",
  "nextPageExists": true
}
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state

Get the current runtime state of a data task

- **Rate Limit:** Special (120 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the data task |
| `type` | string | No | Enum: "LANDING", "STORAGE", "QVD_STORAGE", "TRANSFORM", "DATAMART", "REGISTERED_DATA", "REPLICATION", "DISTRIBUTION", "LAKE_LANDING", "KNOWLEDGE_MART", "FILE_BASED_KNOWLEDGE_MART", "LAKEHOUSE_STORAGE", "LAKEHOUSE_MIRROR", "STREAMING_LAKE_LANDING", "STREAMING_TRANSFORM", "REPLICATE_LANDING" |
| `lastRun` | object | No | Represents the execution state of a task instance, including progress metrics, errors, and operation-specific statistics. |
| `runReadiness` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "STARTING", "RUNNING", "COMPLETED", "FAILED", "CANCELED", "STOPPING" |
| `errors` | object[] | No | List of errors encountered during the last run |
| `endTime` | string | No | Timestamp indicating when the task instance ended |
| `general` | object | No | Overall task execution statistics including dataset counts, data freshness timestamps, and infrastructure details. |
| `message` | string | No |  |
| `traceId` | string | No | Trace identifier for the last run, useful for diagnostics and support |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fullLoad` | object | No | Statistics for the full load phase of the task run, tracking dataset processing progress. |
| `cdcStatus` | object | No | Change Data Capture status information for tasks performing incremental updates, including latency and processing counts. |
| `startTime` | string | No | Timestamp indicating when the task instance started |
| `streaming` | object | No | Real-time streaming statistics for tasks that continuously process data streams. |
| `lastBatchOfChanges` | object | No | Statistics for the most recent batch of changes processed during the task run, including timing and throughput metrics. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `general`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `gatewayId` | string | No | For tasks that run on a gateway, this is the id of the gateway |
| `gatewayName` | string | No | For tasks that run on a gateway, this is the name of the gateway |
| `datasetCount` | number | No | Total number of datasets produced by the task, including ones in error |
| `gatewayTaskName` | string | No | For tasks that run on a gateway, this is the internal name of the task on the gateway |
| `dataTaskUpdatedTo` | string | No | The latest point in time the data reflects, based on updates from the source system. |
| `lakehouseClusterId` | string | No | For lakehouse storage tasks, this is the id of the cluster where the task runs |
| `liveViewsUpdatedTo` | string | No | The latest point in time the live views reflect, based on updates from the source system. |
| `datasetsInErrorCount` | number | No | Count of datasets that encountered errors |
| `lakehouseClusterName` | string | No | For lakehouse storage tasks, this is the name of the cluster where the task runs |

</details>

<details>
<summary>Properties of `fullLoad`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errorCount` | number | No | Number of datasets that have failed full load in this task run |
| `queuedCount` | number | No | Number of datasets that are queued for full load in this task run |
| `loadingCount` | number | No | Number of datasets that are currently being loaded in this task run |
| `completedCount` | number | No | Number of datasets that have completed full load in this task run |

</details>

<details>
<summary>Properties of `cdcStatus`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `totalProcessedCount` | number | No |  |
| `applyingChangesCount` | number | No |  |
| `incomingChangesCount` | number | No | Number of incoming changes. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |
| `accumulatingChangesCount` | number | No |  |
| `throughputInKilobytesPerSecond` | number | No | Throughput in kilobytes per second |

</details>

<details>
<summary>Properties of `streaming`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `errorCount` | number | No | Number of streaming datasets that have encountered errors |
| `queuedCount` | number | No | Number of streaming datasets that are queued |
| `runningCount` | number | No | Number of streaming datasets that are currently running |
| `totalProcessedCount` | number | No | Total number of records processed |

</details>

<details>
<summary>Properties of `lastBatchOfChanges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `relatesToRecordsTo` | string | No | This batch ends with operational source changes from this time. |
| `totalProcessedCount` | number | No |  |
| `relatesToRecordsFrom` | string | No | This batch starts with operational source changes from this time. |
| `throughputInRecordsPerSecond` | number | No | Throughput in records per second |

</details>

</details>

<details>
<summary>Properties of `runReadiness`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "READY_TO_RUN", "ALREADY_RUNNING", "NOT_RUNNABLE" |
| `message` | string | No |  |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "name": "string",
  "type": "LANDING",
  "lastRun": {
    "state": "STARTING",
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string",
        "source": {
          "pointer": "string",
          "parameter": "string"
        },
        "status": 42
      }
    ],
    "endTime": "2018-10-30T07:06:22Z",
    "general": {
      "gatewayId": "string",
      "gatewayName": "string",
      "datasetCount": 42,
      "gatewayTaskName": "string",
      "dataTaskUpdatedTo": "2018-10-30T07:06:22Z",
      "lakehouseClusterId": "string",
      "liveViewsUpdatedTo": "2018-10-30T07:06:22Z",
      "datasetsInErrorCount": 42,
      "lakehouseClusterName": "string"
    },
    "message": "string",
    "traceId": "string",
    "duration": "string",
    "fullLoad": {
      "errorCount": 42,
      "queuedCount": 42,
      "loadingCount": 42,
      "completedCount": 42
    },
    "cdcStatus": {
      "latency": "01:30:45",
      "totalProcessedCount": 42,
      "applyingChangesCount": 42,
      "incomingChangesCount": 42,
      "accumulatingChangesCount": 42,
      "throughputInKilobytesPerSecond": 42
    },
    "startTime": "2018-10-30T07:06:22Z",
    "streaming": {
      "latency": "string",
      "errorCount": 42,
      "queuedCount": 42,
      "runningCount": 42,
      "totalProcessedCount": 42
    },
    "lastBatchOfChanges": {
      "relatesToRecordsTo": "2018-10-30T07:06:22Z",
      "totalProcessedCount": 42,
      "relatesToRecordsFrom": "2018-10-30T07:06:22Z",
      "throughputInRecordsPerSecond": 42
    }
  },
  "runReadiness": {
    "state": "READY_TO_RUN",
    "message": "string"
  }
}
```

---

### GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets

Returns dataset-level runtime state for a data task

- **Rate Limit:** Special (120 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTaskId` | string | Yes | Identifier of the data task. |
| `projectId` | string | Yes | Identifier of the data project. |

#### Responses

##### 200

Returns all datasets for the specified data task

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasets` | object[] | No | Represents the execution state of a single dataset within a task run, including full load, CDC, and streaming progress. |

<details>
<summary>Properties of `datasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the dataset |
| `fullLoad` | object | No |  |
| `cdcStatus` | object | No | Change Data Capture state for the dataset, tracking incremental changes applied and any errors. |
| `datasetId` | string | No | Id of the dataset |
| `streaming` | object | No | Real-time streaming state for the dataset, tracking record processing and transformation statistics. |
| `sourceName` | string | No | Original name of the dataset, relevant only for data movement tasks |
| `dataReadiness` | string | No | Is the data ready for use? Enum: "READY", "NOT_READY", "ERROR" |
| `lastBatchOfChanges` | object | No |  |

<details>
<summary>Properties of `fullLoad`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "LOADING", "COMPLETED", "ERROR" |
| `endTime` | string | No |  |
| `message` | string | No |  |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fileStats` | object | No | Statistics for file-based tasks. |
| `startTime` | string | No |  |
| `cachedChangesCount` | number | No | Number of changes captured and cached during full load (CDC landing/replication tasks only) |
| `failedRecordsCount` | number | No | Number of records that failed to load (currently only for knowledge marts) |
| `totalProcessedCount` | number | No | Number of records (or docs in knowledge marts) were loaded. |

<details>
<summary>Properties of `fileStats`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `cdcStatus`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "PROCESSING", "ACCUMULATING_CHANGES", "COMPLETED", "ERROR" |
| `message` | string | No |  |
| `ddlCount` | number | No | Number of DDL statements executed during the last run |
| `deleteCount` | number | No | delete portion of totalProcessedCount. Only available for some task types |
| `insertCount` | number | No | Insert portion of totalProcessedCount. Only available for some task types |
| `updateCount` | number | No | update portion of totalProcessedCount. Only available for some task types |
| `lastProcessed` | string | No |  |
| `totalProcessedCount` | number | No | Total number of changes/DMLs applied to the dataset |
| `incomingChangesCount` | number | No | Number of incoming changes for the dataset. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |
| `unoptimizedRecordsCount` | number | No | Number of records that are queryable via the view, but not yet merged into optimized Iceberg partitions. Only relevant for 'Iceberg Storage' and 'Streaming Transform' tasks. |

</details>

<details>
<summary>Properties of `streaming`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "RUNNING", "ERROR" |
| `message` | string | No |  |
| `lastProcessed` | string | No | Timestamp of the latest source record inserted into the target dataset. |
| `parseIssueCount` | number | No | Number of records that had parsing issues |
| `recordsWrittenCount` | number | No | Total number of records written to the dataset |
| `totalProcessedCount` | number | No | Total number of processed changes for the dataset |
| `recordsFilteredCount` | number | No | Total number of records filtered out and not written to the dataset |
| `unoptimizedRecordsCount` | number | No | Queryable records pending merge into optimized Iceberg partitions. |

</details>

<details>
<summary>Properties of `lastBatchOfChanges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `state` | string | No | Enum: "QUEUED", "PROCESSING", "COMPLETED", "ERROR" |
| `endTime` | string | No |  |
| `message` | string | No |  |
| `duration` | string | No | Duration in HH:MM:SS format (hours:minutes:seconds) |
| `fileStats` | object | No | Statistics for file-based tasks. |
| `startTime` | string | No |  |
| `operationStats` | object | No | Breakdown of operations for record-oriented tasks. |
| `totalProcessedCount` | number | No |  |
| `throughputInRecordsPerSecond` | number | No | Throughput in records per second |

<details>
<summary>Properties of `fileStats`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `operationStats`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "datasets": [
    {
      "name": "string",
      "fullLoad": {
        "state": "QUEUED",
        "endTime": "2018-10-30T07:06:22Z",
        "message": "string",
        "duration": "string",
        "fileStats": {
          "volume": "string",
          "processedCount": 42
        },
        "startTime": "2018-10-30T07:06:22Z",
        "cachedChangesCount": 42,
        "failedRecordsCount": 42,
        "totalProcessedCount": 42
      },
      "cdcStatus": {
        "state": "QUEUED",
        "message": "string",
        "ddlCount": 42,
        "deleteCount": 42,
        "insertCount": 42,
        "updateCount": 42,
        "lastProcessed": "2018-10-30T07:06:22Z",
        "totalProcessedCount": 42,
        "incomingChangesCount": 42,
        "unoptimizedRecordsCount": 42
      },
      "datasetId": "string",
      "streaming": {
        "state": "QUEUED",
        "message": "string",
        "lastProcessed": "2018-10-30T07:06:22Z",
        "parseIssueCount": 42,
        "recordsWrittenCount": 42,
        "totalProcessedCount": 42,
        "recordsFilteredCount": 42,
        "unoptimizedRecordsCount": 42
      },
      "sourceName": "string",
      "dataReadiness": "READY",
      "lastBatchOfChanges": {
        "state": "QUEUED",
        "endTime": "2018-10-30T07:06:22Z",
        "message": "string",
        "duration": "string",
        "fileStats": {
          "volume": "string",
          "processedCount": 42
        },
        "startTime": "2018-10-30T07:06:22Z",
        "operationStats": {
          "deleteCount": 42,
          "failedCount": 42,
          "insertCount": 42,
          "updateCount": 42
        },
        "totalProcessedCount": 42,
        "throughputInRecordsPerSecond": 42
      }
    }
  ]
}
```

---

### GET /api/v1/di-projects/actions/{actionId}

Retrieves the status of an asynchronous operation.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionId` | string | Yes | Identifier of the action. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `detailed` | boolean | No | Specifies whether to include detailed status information in the response. Set to `true` to return detailed information. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the async operation |
| `type` | string | No | Type of action being performed Enum: "PROJECT_PREPARE", "PROJECT_VALIDATE", "TASK_PREPARE", "TASK_VALIDATE", "PROJECT_IMPORT" |
| `error` | object | No |  |
| `state` | string | No | State of the action Enum: "PENDING", "EXECUTING", "COMPLETED", "FAILED", "CANCELED", "SKIPPED" |
| `endTime` | string | No |  |
| `startTime` | string | No |  |
| `taskDetails` | object[] | No |  |
| `taskProgress` | object | No |  |

<details>
<summary>Properties of `error`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code |
| `details` | string | No | Additional error details |
| `message` | string | No | Error message |

</details>

<details>
<summary>Properties of `taskDetails`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `info` | string | No | Additional details about task state |
| `name` | string | No |  |
| `error` | object | No |  |
| `state` | string | No | State of the action Enum: "PENDING", "EXECUTING", "COMPLETED", "FAILED", "CANCELED", "SKIPPED" |
| `taskId` | string | No |  |

<details>
<summary>Properties of `error`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code |
| `details` | string | No | Additional error details |
| `message` | string | No | Error message |

</details>

</details>

<details>
<summary>Properties of `taskProgress`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `failed` | integer | No | Number of tasks that failed |
| `pending` | integer | No | Number of tasks pending execution |
| `skipped` | integer | No | Number of tasks skipped due to conflicts |
| `canceled` | integer | No | Number of tasks canceled |
| `completed` | integer | No | Number of tasks completed successfully |
| `executing` | integer | No | Number of tasks currently executing |

</details>

##### 404

Action not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/di-projects/actions/{actionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/actions/{actionId}',
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
# qlik-cli has not implemented support for GET /api/v1/di-projects/actions/{actionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/actions/{actionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "name": "Prepare project myspace.demoproject",
  "type": "PROJECT_PREPARE",
  "error": {
    "code": "string",
    "details": "string",
    "message": "string"
  },
  "state": "PENDING",
  "endTime": "2018-10-30T07:06:22Z",
  "startTime": "2018-10-30T07:06:22Z",
  "taskDetails": [
    {
      "info": "string",
      "name": "string",
      "error": {
        "code": "string",
        "details": "string",
        "message": "string"
      },
      "state": "PENDING",
      "taskId": "string"
    }
  ],
  "taskProgress": {
    "failed": 42,
    "pending": 42,
    "skipped": 42,
    "canceled": 42,
    "completed": 42,
    "executing": 42
  }
}
```

---

### POST /api/v1/di-projects/utils/actions/validate-project-definitions

Validates the project definition files in a `.zip` and returns a structured report of warnings and errors. The validation runs synchronously and completes before the response is returned. Use this operation before importing with `POST /di-projects/{projectId}/actions/import-async` to confirm that YAML-based pipeline definitions are correct.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

A `.zip` file containing the project definition files to validate.

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `zip` | string | No |  |

#### Responses

##### 200

Validation completed. The response contains a report of warnings and errors found in the project definitions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reports` | object[] | No | List of validation findings. An empty array indicates no issues were found. |

<details>
<summary>Properties of `reports`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | No | Path to the field or file in the project definition where the issue was found. |
| `level` | string | No | Severity of the validation finding. `WARNING` indicates a potential issue that does not block import; `ERROR` indicates a critical issue that must be resolved before importing. Enum: "WARNING", "ERROR" |
| `reason` | string | No | Human-readable description of the validation finding. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of error objects describing what went wrong. |
| `traceId` | string | No | Unique identifier for this error response, useful for tracking and support inquiries. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Machine-readable error code for programmatic handling. |
| `title` | string | No | Brief human-readable summary of the error. |
| `detail` | string | No | Detailed explanation of the error and suggested remediation steps. |
| `source` | object | No | Identifies the location of the error in the request. |
| `status` | integer | No | HTTP status code associated with the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | JSON Pointer (RFC 6901) to the field in the request body that caused the error. |
| `parameter` | string | No | Name of the query parameter or path parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/di-projects/utils/actions/validate-project-definitions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/di-projects/utils/actions/validate-project-definitions',
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
# qlik-cli has not implemented support for POST /api/v1/di-projects/utils/actions/validate-project-definitions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects/utils/actions/validate-project-definitions" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "zip=@/path/to/file"
```

**Example Response:**

```json
{
  "reports": [
    {
      "path": "string",
      "level": "WARNING",
      "reason": "string"
    }
  ]
}
```

---
