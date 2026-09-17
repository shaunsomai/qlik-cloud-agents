# Trust scores

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

The Trust Scores API retrieves the Qlik Trust Score™ for datasets in bulk, including overall score and per-axis and per-metric breakdowns.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/data-governance/trust-scores/results/data-sets/actions/filter`](#post-apidata-governancetrust-scoresresultsdata-setsactionsfilter) | Returns the current Trust Score for up to 100 datasets in a single request. Each result includes the overall score, per-axis breakdown (`weight`, `score`, `enabled` state), and per-metric details. Datasets with no computed Trust Score are omitted from the response. Requires `dataset:read` and `dataquality:read` permissions. |

## API Reference

### POST /api/data-governance/trust-scores/results/data-sets/actions/filter

Returns the current Trust Score for up to 100 datasets in a single request. Each result includes the overall score, per-axis breakdown (`weight`, `score`, `enabled` state), and per-metric details. Datasets with no computed Trust Score are omitted from the response. Requires `dataset:read` and `dataquality:read` permissions.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

List of dataset IDs to retrieve Trust Scores for. Maximum 100 IDs per request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetIds` | string[] | Yes | List of dataset IDs to retrieve Trust Scores for. Maximum 100 IDs per request. |
| `recomputeUsage` | boolean | No | When true, refreshes the USAGE and TIMELINESS axes from source before returning the Trust Scores. |

#### Responses

##### 200

Trust Score results for the requested datasets. Datasets with no computed Trust Score are omitted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | List of Trust Score results, one entry per dataset found. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `axes` | object[] | Yes | Per-axis breakdown of the Trust Score. |
| `score` | number | Yes | Overall weighted Trust Score across all enabled axes [0, 100]. |
| `datasetId` | string | Yes | Unique identifier of the dataset this score belongs to. |
| `updatedAt` | string | Yes | Timestamp of the last Trust Score computation for this dataset. |
| `previousScore` | number | No | Overall Trust Score from the previous computation, for change tracking. |

<details>
<summary>Properties of `axes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Defines the axis of the Trust Score. Enum: "VALIDITY", "COMPLETENESS", "USAGE", "DISCOVERABILITY", "ACCURACY", "DIVERSITY", "TIMELINESS" |
| `score` | number | No | Computed score for this axis [0, 100]. Omitted when axis is not applicable. |
| `weight` | integer | Yes | Defines the weight of the axis or metric in the Trust Score. |
| `enabled` | boolean | No | Whether this axis is enabled in the tenant configuration. Disabled axes have a `weight` of `0` and do not affect the overall score. |
| `metrics` | object[] | Yes | Per-metric breakdown contributing to this axis score. |
| `applicable` | boolean | No | Whether this axis is applicable for the dataset. An axis may be enabled but not applicable (for example, `TIMELINESS` when no freshness threshold is set). |
| `previousScore` | number | No | Axis score from the previous computation, for change tracking. |

<details>
<summary>Properties of `metrics`</summary>

_Properties truncated due to depth limit._

</details>

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
| `status` | string | No |  |

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
| `status` | string | No |  |

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
| `status` | string | No |  |

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
| `status` | string | No |  |

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
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/trust-scores/results/data-sets/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/trust-scores/results/data-sets/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasetIds: [
        'Jjk5NNHiUObQe8xTyeLgP5nQjKTpEr8R',
      ],
      recomputeUsage: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/trust-scores/results/data-sets/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/trust-scores/results/data-sets/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasetIds":["Jjk5NNHiUObQe8xTyeLgP5nQjKTpEr8R"],"recomputeUsage":false}'
```

**Example Response:**

```json
{
  "data": [
    {
      "axes": [
        {
          "id": "TIMELINESS",
          "score": 42,
          "weight": 50,
          "enabled": true,
          "metrics": [
            {
              "id": "TIMELINESS_FRESHNESS",
              "score": 42,
              "weight": 50
            }
          ],
          "applicable": true,
          "previousScore": 42
        }
      ],
      "score": 42,
      "datasetId": "Jjk5NNHiUObQe8xTyeLgP5nQjKTpEr8R",
      "updatedAt": "2018-03-20T09:12:28Z",
      "previousScore": 42
    }
  ]
}
```

---
