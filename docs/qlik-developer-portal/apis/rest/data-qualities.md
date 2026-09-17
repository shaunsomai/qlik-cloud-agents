# Data qualities

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

API for triggering data quality computations and retrieving global results to assess the quality of your datasets.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/data-qualities/computations`](#post-apiv1data-qualitiescomputations) | Triggers a full data quality computation for a dataset, running profile calculation followed by data quality |
| `GET` | [`/api/v1/data-qualities/computations/{computationId}`](#get-apiv1data-qualitiescomputationscomputationid) | Retrieves the current execution status of a data quality computation. Poll this endpoint after triggering a |
| `GET` | [`/api/v1/data-qualities/global-results`](#get-apiv1data-qualitiesglobal-results) | Retrieves the global quality results for a dataset, showing counts of valid, invalid, empty, and total |

## API Reference

### POST /api/v1/data-qualities/computations _(deprecated)_

Triggers a full data quality computation for a dataset, running profile calculation followed by data quality
assessment. Returns a `computationId` that can be used to track progress via the computation status endpoint
(`GET /data-qualities/computations/{computationId}`). The computation runs asynchronously.
Poll the status endpoint until `status` is `SUCCEEDED` or `FAILED`.


- **Replaced by:** "POST:/data-governance/data-qualities/computations"
- **Rate Limit:** Special (10 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The ID of the dataset |
| `connectionId` | string | No | The ID of the connection |
| `sampleMode` | string | No | Specifies how the dataset is sampled. `ABSOLUTE` represents a fixed number of rows, while `RELATIVE` refers to a percentage of the total dataset rows. Enum: "ABSOLUTE", "RELATIVE" |
| `sampleSize` | integer | No | The actual value of the selected sampling method size (either a fixed number for `ABSOLUTE` mode or a percentage for `RELATIVE` mode). Maximum allowed value for `ABSOLUTE` mode is `100000`. |
| `executionMode` | string | No | Specifies where the data quality computation takes place. In `PUSHDOWN` mode, it runs within the Cloud Data Warehouse (e.g., Snowflake, Databricks), whereas in `PULLUP` mode, it runs in Qlik Cloud. Enum: "PUSHDOWN", "PULLUP" |

#### Responses

##### 202

Computation triggered. The response body contains the `computationId` for tracking progress.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `computationId` | string | Yes | The unique identifier of the triggered computation. Use this value to poll for status. |

##### 400

The request is in incorrect format.

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

User does not have valid authentication credentials.

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

User does not have access to the resource.

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

Internal Server Error.

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

##### 503

Requested service is not available.

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
// qlik-api has not implemented support for `POST /api/v1/data-qualities/computations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-qualities/computations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasetId: '669144f5aa2d642638ef1dd0',
      sampleMode: 'ABSOLUTE',
      sampleSize: 10000,
      connectionId:
        '2b855c3d-426c-4aac-90cf-0edf9fc294d3',
      executionMode: 'PULLUP',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-qualities/computations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-qualities/computations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasetId":"669144f5aa2d642638ef1dd0","sampleMode":"ABSOLUTE","sampleSize":10000,"connectionId":"2b855c3d-426c-4aac-90cf-0edf9fc294d3","executionMode":"PULLUP"}'
```

**Example Response:**

```json
{
  "computationId": "string"
}
```

---

### GET /api/v1/data-qualities/computations/{computationId} _(deprecated)_

Retrieves the current execution status of a data quality computation. Poll this endpoint after triggering a
computation to determine when results are available. The `status` field returns one of `REQUESTED`,
`SUBMITTED`, `PROFILE_REQUESTED`, `SUCCEEDED`, `FAILED`, or `PROFILE_FAILED`.


- **Replaced by:** "GET:/data-governance/data-qualities/computations/{computationId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `computationId` | string | Yes | The unique identifier of the computation, as returned by `POST /data-governance/data-qualities/computations`. |

#### Responses

##### 200

Current execution status of the computation

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Enum: "PROFILE_REQUESTED", "PROFILE_FAILED", "REQUESTED", "SUBMITTED", "SUCCEEDED", "FAILED" |

##### 400

The request is in incorrect format.

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

User does not have valid authentication credentials.

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

User does not have access to the resource.

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

No computation found with the specified `computationId`.

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

Internal Server Error.

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

##### 503

Requested service is not available.

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
// qlik-api has not implemented support for `GET /api/v1/data-qualities/computations/{computationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-qualities/computations/{computationId}',
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
# qlik-cli has not implemented support for GET /api/v1/data-qualities/computations/{computationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-qualities/computations/{computationId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "PROFILE_REQUESTED"
}
```

---

### GET /api/v1/data-qualities/global-results _(deprecated)_

Retrieves the global quality results for a dataset, showing counts of valid, invalid, empty, and total
sample cells.


- **Replaced by:** "GET:/data-governance/data-qualities/global-results"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The unique identifier of the dataset. |
| `connectionId` | string | No | The unique identifier of the connection. |

#### Responses

##### 200

Global quality results for the dataset, including counts of valid, invalid, empty, and total sample cells per connection.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The unique identifier of the dataset. |
| `qualities` | object[] | Yes |  |

<details>
<summary>Properties of `qualities`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quality` | object | Yes |  |
| `connectionId` | string | Yes | The unique identifier of the connection. |

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `empty` | integer | Yes | Number of empty sample cells. |
| `total` | integer | Yes | Total number of cells in the sample. |
| `valid` | integer | Yes | Number of valid sample cells. |
| `invalid` | integer | Yes | Number of invalid sample cells. |
| `updatedAt` | string | Yes | Timestamp of the most recent data quality computation for this dataset and connection. |

</details>

</details>

##### 400

The request is in incorrect format.

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

User does not have valid authentication credentials.

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

User does not have access to the resource.

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

No quality results found for the specified dataset.

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

Internal Server Error.

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

##### 503

Requested service is not available.

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
// qlik-api has not implemented support for `GET /api/v1/data-qualities/global-results` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-qualities/global-results',
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
# qlik-cli has not implemented support for GET /api/v1/data-qualities/global-results yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-qualities/global-results" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "datasetId": "string",
  "qualities": [
    {
      "quality": {
        "empty": 42,
        "total": 42,
        "valid": 42,
        "invalid": 42,
        "updatedAt": "2018-10-30T07:06:22Z"
      },
      "connectionId": "string"
    }
  ]
}
```

---
