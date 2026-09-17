# AutoML dataset predictions

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Use your ML deployment to generate batch data in file format to predict future outcomes on new data.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/automl-predictions/{predictionId}/coordinate-shap`](#get-apiv1automl-predictionspredictionidcoordinate-shap) | Returns a file containing the shapley values in coordinate form that are associated with a prediction ID. |
| `POST` | [`/api/v1/automl-predictions/{predictionId}/jobs`](#post-apiv1automl-predictionspredictionidjobs) | Retrieve jobs that are associated with a prediction. Job with correlation type `prediction`. |
| `GET` | [`/api/v1/automl-predictions/{predictionId}/not-predicted-reasons`](#get-apiv1automl-predictionspredictionidnot-predicted-reasons) | Returns a file containing any rows in a prediction operation where a prediction was unable to be produced. |
| `GET` | [`/api/v1/automl-predictions/{predictionId}/predictions`](#get-apiv1automl-predictionspredictionidpredictions) | Returns a file containing the predicted values that are associated with a prediction ID. |
| `GET` | [`/api/v1/automl-predictions/{predictionId}/shap`](#get-apiv1automl-predictionspredictionidshap) | Returns a file containing the shapley values that are associated with a prediction ID. |
| `GET` | [`/api/v1/automl-predictions/{predictionId}/source`](#get-apiv1automl-predictionspredictionidsource) | Returns a file containing the source values and an index field that are associated with a prediction ID. |

## API Reference

### GET /api/v1/automl-predictions/{predictionId}/coordinate-shap _(deprecated)_

Returns a file containing the shapley values in coordinate form that are associated with a prediction ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `refId` | string | No |  |

#### Responses

##### 200

Stream of coordinate shap values returned successfully.

**Content-Type:** `text/csv`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/csv` | any | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/automl-predictions/{predictionId}/coordinate-shap` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/coordinate-shap',
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
# qlik-cli has not implemented support for GET /api/v1/automl-predictions/{predictionId}/coordinate-shap yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/coordinate-shap" \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automl-predictions/{predictionId}/jobs _(deprecated)_

Retrieve jobs that are associated with a prediction. Job with correlation type `prediction`.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Responses

##### 200

OK Response

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
// qlik-api has not implemented support for `POST /api/v1/automl-predictions/{predictionId}/jobs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/jobs',
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
# qlik-cli has not implemented support for POST /api/v1/automl-predictions/{predictionId}/jobs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/jobs" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/automl-predictions/{predictionId}/not-predicted-reasons _(deprecated)_

Returns a file containing any rows in a prediction operation where a prediction was unable to be produced.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `refId` | string | No |  |

#### Responses

##### 200

Stream of not predicted reasons returned successfully.

**Content-Type:** `text/csv`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/csv` | any | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/automl-predictions/{predictionId}/not-predicted-reasons` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/not-predicted-reasons',
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
# qlik-cli has not implemented support for GET /api/v1/automl-predictions/{predictionId}/not-predicted-reasons yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/not-predicted-reasons" \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/automl-predictions/{predictionId}/predictions _(deprecated)_

Returns a file containing the predicted values that are associated with a prediction ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `refId` | string | No |  |

#### Responses

##### 200

Prediction stream returned succesfully.

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
// qlik-api has not implemented support for `GET /api/v1/automl-predictions/{predictionId}/predictions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/predictions',
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
# qlik-cli has not implemented support for GET /api/v1/automl-predictions/{predictionId}/predictions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/predictions" \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/automl-predictions/{predictionId}/shap _(deprecated)_

Returns a file containing the shapley values that are associated with a prediction ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `refId` | string | No |  |

#### Responses

##### 200

Stream of shap values returned successfully.

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
// qlik-api has not implemented support for `GET /api/v1/automl-predictions/{predictionId}/shap` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/shap',
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
# qlik-cli has not implemented support for GET /api/v1/automl-predictions/{predictionId}/shap yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/shap" \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/automl-predictions/{predictionId}/source _(deprecated)_

Returns a file containing the source values and an index field that are associated with a prediction ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-02.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `predictionId` | string | Yes | The ID of the prediction configuration object that provides parameters to be applied when the prediction is produced. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `refId` | string | No |  |

#### Responses

##### 200

Stream of source values and index field returned successfully.

**Content-Type:** `text/csv`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/csv` | any | No |  |

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
// qlik-api has not implemented support for `GET /api/v1/automl-predictions/{predictionId}/source` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automl-predictions/{predictionId}/source',
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
# qlik-cli has not implemented support for GET /api/v1/automl-predictions/{predictionId}/source yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions/{predictionId}/source" \
-H "Authorization: Bearer <access_token>"
```

---
