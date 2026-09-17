# AutoML real-time predictions

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Use your ML deployment to generate real-time results returned as JSON in a synchronous manner to predict future outcomes on new data.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/automl-deployments/{deploymentId}/realtime-predictions`](#post-apiv1automl-deploymentsdeploymentidrealtime-predictions) | Generates predictions in a synchronous request and response. |

## API Reference

### POST /api/v1/automl-deployments/{deploymentId}/realtime-predictions _(deprecated)_

Generates predictions in a synchronous request and response.

- **Rate Limit:** Special (300 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02. This endpoint has been replaced by a new version

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | The ID of the ML deployed model that will be employed to produce predictions. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeNotPredictedReason` | boolean | No | If true, will include a column with the reason why a prediction was not produced. |
| `includeShap` | boolean | No | If true, the shapley values will be included in the response. |
| `includeSource` | boolean | No | If true, the source data will be included in the response |
| `index` | string | No | The name of the feature in the source data to use as an index in the response data. The column will be included with its original name and values. This is intended to allow the caller to join results with source data. |

#### Request Body

Request payload containing the dataset for predictions. Date features must be in ISO 8601 format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rows` | array[] | No | The rows of the dataset to produce predictions from. Date features must be in ISO 8601 format. |
| `schema` | object[] | No | The schema of the input dataset. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of a feature in the dataset. |

</details>

#### Responses

##### 200

Stream of combined prediction output returned successfully.

##### 400

Received a bad argument

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

Access forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

Resource not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 409

Resource conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

Resource unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `meta` | object | No |  |
| `issue` | string | No | The issue code |
| `title` | string | No | A summary of what went wrong |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automl-deployments/{deploymentId}/realtime-predictions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-deployments/{deploymentId}/realtime-predictions',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      rows: [['string']],
      schema: [{ name: 'string' }],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automl-deployments/{deploymentId}/realtime-predictions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-deployments/{deploymentId}/realtime-predictions" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"rows":[["string"]],"schema":[{"name":"string"}]}'
```

---
