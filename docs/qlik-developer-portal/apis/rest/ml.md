# Machine Learning

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

The Machine Learning API allows you to generate profile insights to analyze datasets, create and manage machine learning experiments, deploy models, and run predictions.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/ml/deployments`](#get-apiv1mldeployments) |  |
| `POST` | [`/api/v1/ml/deployments`](#post-apiv1mldeployments) |  |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}`](#get-apiv1mldeploymentsdeploymentid) |  |
| `PATCH` | [`/api/v1/ml/deployments/{deploymentId}`](#patch-apiv1mldeploymentsdeploymentid) |  |
| `DELETE` | [`/api/v1/ml/deployments/{deploymentId}`](#delete-apiv1mldeploymentsdeploymentid) |  |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/actions/activate-models`](#post-apiv1mldeploymentsdeploymentidactionsactivate-models) | Activates the deployed model on this deployment's default alias. The |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/actions/deactivate-models`](#post-apiv1mldeploymentsdeploymentidactionsdeactivate-models) | Deactivates the deployed model on this deployment's default alias. |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}/aliases`](#get-apiv1mldeploymentsdeploymentidaliases) | Retrieves a list of aliases based on filter parameters for a deployment. |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/aliases`](#post-apiv1mldeploymentsdeploymentidaliases) | Creates an alias for a deployment. |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}`](#get-apiv1mldeploymentsdeploymentidaliasesaliasid) | Retrieves an alias that exists on the deployment. |
| `PATCH` | [`/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}`](#patch-apiv1mldeploymentsdeploymentidaliasesaliasid) | Updates an alias for a deployment. |
| `DELETE` | [`/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}`](#delete-apiv1mldeploymentsdeploymentidaliasesaliasid) | Delete an alias from a deployment. |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run`](#post-apiv1mldeploymentsdeploymentidaliasesaliasnamerealtime-predictionsactionsrun) |  |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions`](#get-apiv1mldeploymentsdeploymentidbatch-predictions) |  |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions`](#post-apiv1mldeploymentsdeploymentidbatch-predictions) |  |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}`](#get-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionid) |  |
| `PATCH` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}`](#patch-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionid) |  |
| `DELETE` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}`](#delete-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionid) |  |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict`](#post-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionidactionspredict) |  |
| `GET` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule`](#get-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionidschedule) | Retrieves the schedule for a batch prediction. |
| `PATCH` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule`](#patch-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionidschedule) | Updates the schedule for a batch prediction. |
| `PUT` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule`](#put-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionidschedule) | Adds a schedule to a batch prediction. |
| `DELETE` | [`/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule`](#delete-apiv1mldeploymentsdeploymentidbatch-predictionsbatchpredictionidschedule) | Deletes the schedule from a batch prediction. |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/models/actions/add`](#post-apiv1mldeploymentsdeploymentidmodelsactionsadd) |  |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/models/actions/remove`](#post-apiv1mldeploymentsdeploymentidmodelsactionsremove) |  |
| `POST` | [`/api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run`](#post-apiv1mldeploymentsdeploymentidrealtime-predictionsactionsrun) |  |
| `GET` | [`/api/v1/ml/experiments`](#get-apiv1mlexperiments) | Retrieves a list of experiments based on provided filter and sort |
| `POST` | [`/api/v1/ml/experiments`](#post-apiv1mlexperiments) |  |
| `GET` | [`/api/v1/ml/experiments/{experimentId}`](#get-apiv1mlexperimentsexperimentid) |  |
| `PATCH` | [`/api/v1/ml/experiments/{experimentId}`](#patch-apiv1mlexperimentsexperimentid) |  |
| `DELETE` | [`/api/v1/ml/experiments/{experimentId}`](#delete-apiv1mlexperimentsexperimentid) |  |
| `POST` | [`/api/v1/ml/experiments/{experimentId}/actions/recommend-models`](#post-apiv1mlexperimentsexperimentidactionsrecommend-models) | Returns model recommendations for a specified experiment, including the best-performing, fastest, and most accurate models based on evaluation metrics. |
| `GET` | [`/api/v1/ml/experiments/{experimentId}/models`](#get-apiv1mlexperimentsexperimentidmodels) |  |
| `GET` | [`/api/v1/ml/experiments/{experimentId}/models/{modelId}`](#get-apiv1mlexperimentsexperimentidmodelsmodelid) |  |
| `GET` | [`/api/v1/ml/experiments/{experimentId}/versions`](#get-apiv1mlexperimentsexperimentidversions) |  |
| `POST` | [`/api/v1/ml/experiments/{experimentId}/versions`](#post-apiv1mlexperimentsexperimentidversions) | Creates an experiment version. |
| `GET` | [`/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}`](#get-apiv1mlexperimentsexperimentidversionsexperimentversionid) |  |
| `PATCH` | [`/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}`](#patch-apiv1mlexperimentsexperimentidversionsexperimentversionid) |  |
| `DELETE` | [`/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}`](#delete-apiv1mlexperimentsexperimentidversionsexperimentversionid) |  |
| `POST` | [`/api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel`](#post-apiv1mljobscorrtypecorridactionscancel) | Cancels jobs for an experiment version or batch prediction. |
| `POST` | [`/api/v1/ml/profile-insights`](#post-apiv1mlprofile-insights) | Starts creating profile insights for an experiment dataset. |
| `GET` | [`/api/v1/ml/profile-insights/{dataSetId}`](#get-apiv1mlprofile-insightsdatasetid) | Retrieves profile insights for the specified dataset. If you received a |

## API Reference

### GET /api/v1/ml/deployments

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Deployment fields by which you can filter responses.<br><br> - `spaceId` ID string (or empty string for personal space) - ID of space in which deployment(s) exist - `modelId` UUID string - By model ID - `createdBy` ID string - `ownerId` ID string - `experimentId` UUID string - ID of experiment in which model(s) exist - `experimentVersionId` UUID string - ID of experiment version in which model(s) exist - `predictionId` UUID string - ID of prediction which exists on deployment - `predictionEnabled` boolean - Are predictions enabled - `exactName` string - Deployments with exact name. Names may not be unique. - `nameContains` string - Deployments where name includes this. Names may not be unique - `experimentType` string - Deployments that have models of the experiment type |
| `sort` | string | No | Field(s) by which to sort response  Enum: "createdAt", "+createdAt", "-createdAt", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "deployment" |
| `attributes` | object | Yes | A deployed model against which you can run predictions |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | Yes | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `modelId` | string | Yes | ID of the model |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity. |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deprecated` | boolean | Yes | Whether this deployment is deprecated |
| `description` | string | Yes | Description of this entity |
| `errorMessage` | string | No | JSON string of error object |
| `deployedModelIds` | string[] | No | IDs of all models deployed to the deployment |
| `enablePredictions` | boolean | Yes | Whether to allow predictions |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "deployment",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "modelId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "ownerId": "string",
        "spaceId": "string",
        "createdAt": "string",
        "createdBy": "string",
        "updatedAt": "string",
        "deprecated": true,
        "description": "string",
        "errorMessage": "string",
        "deployedModelIds": [
          "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        ],
        "enablePredictions": true
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/ml/deployments

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "deployment" |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of this entity |
| `modelId` | string | Yes | ID of the model |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `deprecated` | boolean | No | Whether this deployment is deprecated |
| `description` | string | No | Description of this entity |
| `enablePredictions` | boolean | No | Whether to allow real-time predictions |

</details>

</details>

#### Responses

##### 201

`Created`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "deployment" |
| `attributes` | object | Yes | A deployed model against which you can run predictions |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | Yes | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `modelId` | string | Yes | ID of the model |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity. |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deprecated` | boolean | Yes | Whether this deployment is deprecated |
| `description` | string | Yes | Description of this entity |
| `errorMessage` | string | No | JSON string of error object |
| `deployedModelIds` | string[] | No | IDs of all models deployed to the deployment |
| `enablePredictions` | boolean | Yes | Whether to allow predictions |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'deployment',
        attributes: {
          name: 'string',
          modelId:
            'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
          spaceId: 'string',
          deprecated: true,
          description: 'string',
          enablePredictions: true,
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/deployments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"deployment","attributes":{"name":"string","modelId":"c35f4b70-3ce4-4a30-b62b-2aef16943bc4","spaceId":"string","deprecated":true,"description":"string","enablePredictions":true}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "deployment",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "modelId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "ownerId": "string",
      "spaceId": "string",
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "deprecated": true,
      "description": "string",
      "errorMessage": "string",
      "deployedModelIds": [
        "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      ],
      "enablePredictions": true
    }
  }
}
```

---

### GET /api/v1/ml/deployments/{deploymentId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "deployment" |
| `attributes` | object | Yes | A deployed model against which you can run predictions |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | Yes | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `modelId` | string | Yes | ID of the model |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity. |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deprecated` | boolean | Yes | Whether this deployment is deprecated |
| `description` | string | Yes | Description of this entity |
| `errorMessage` | string | No | JSON string of error object |
| `deployedModelIds` | string[] | No | IDs of all models deployed to the deployment |
| `enablePredictions` | boolean | Yes | Whether to allow predictions |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "deployment",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "modelId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "ownerId": "string",
      "spaceId": "string",
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "deprecated": true,
      "description": "string",
      "errorMessage": "string",
      "deployedModelIds": [
        "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      ],
      "enablePredictions": true
    }
  }
}
```

---

### PATCH /api/v1/ml/deployments/{deploymentId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the property you want to update Enum: "/name", "/description", "/spaceId" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/deployments/{deploymentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New Name',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/deployments/{deploymentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New Name"}]'
```

---

### DELETE /api/v1/ml/deployments/{deploymentId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/deployments/{deploymentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/deployments/{deploymentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/deployments/{deploymentId}/actions/activate-models

Activates the deployed model on this deployment's default alias. The
response reports which model was targeted and whether its state
actually changed via the `qlik-model-id` and `qlik-state-change`
response headers. If the model was already active, the request still
succeeds but `qlik-state-change` is `NO_CHANGE`.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/actions/activate-models` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/actions/activate-models',
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
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/actions/activate-models yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/actions/activate-models" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/deployments/{deploymentId}/actions/deactivate-models

Deactivates the deployed model on this deployment's default alias.
The response reports which model was targeted and whether its state
actually changed via the `qlik-model-id` and `qlik-state-change`
response headers. If the model was already inactive, the request
still succeeds but `qlik-state-change` is `NO_CHANGE`.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/actions/deactivate-models` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/actions/deactivate-models',
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
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/actions/deactivate-models yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/actions/deactivate-models" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/ml/deployments/{deploymentId}/aliases

Retrieves a list of aliases based on filter parameters for a deployment.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Alias fields by which you can filter responses - `name` string - Aliases with exact name - `modelId` UUID string - By model ID - `mode` enum string - Mode by which alias is set to |
| `sort` | string | No | Field(s) by which to sort response  Enum: "name", "+name", "-name" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "alias" |
| `attributes` | object | Yes | An AutoML alias |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `mode` | string | Yes | The mode of an alias. Default mode means the model assigned to that alias will be used if alias is not specified Enum: "default", "undefined" |
| `name` | string | Yes | Name of this entity |
| `models` | object[] | Yes | Model information stored on an alias |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deploymentId` | string | Yes | ID of a model deployment |

<details>
<summary>Properties of `models`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}/aliases` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId}/aliases yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "alias",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "mode": "default",
        "name": "string",
        "models": [
          {
            "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
          }
        ],
        "createdAt": "string",
        "createdBy": "string",
        "updatedAt": "string",
        "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/ml/deployments/{deploymentId}/aliases

Creates an alias for a deployment.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "alias" |
| `attributes` | object | Yes |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of this entity |
| `models` | object[] | Yes | Model information stored on an alias |

<details>
<summary>Properties of `models`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

`Created`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "alias" |
| `attributes` | object | Yes | An AutoML alias |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `mode` | string | Yes | The mode of an alias. Default mode means the model assigned to that alias will be used if alias is not specified Enum: "default", "undefined" |
| `name` | string | Yes | Name of this entity |
| `models` | object[] | Yes | Model information stored on an alias |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deploymentId` | string | Yes | ID of a model deployment |

<details>
<summary>Properties of `models`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/aliases` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'alias',
        attributes: {
          name: 'string',
          models: [
            {
              id: 'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
            },
          ],
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/aliases yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"alias","attributes":{"name":"string","models":[{"id":"c35f4b70-3ce4-4a30-b62b-2aef16943bc4"}]}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "alias",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "mode": "default",
      "name": "string",
      "models": [
        {
          "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
    }
  }
}
```

---

### GET /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}

Retrieves an alias that exists on the deployment.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `aliasId` | string | Yes | ID of the alias |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "alias" |
| `attributes` | object | Yes | An AutoML alias |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `mode` | string | Yes | The mode of an alias. Default mode means the model assigned to that alias will be used if alias is not specified Enum: "default", "undefined" |
| `name` | string | Yes | Name of this entity |
| `models` | object[] | Yes | Model information stored on an alias |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `deploymentId` | string | Yes | ID of a model deployment |

<details>
<summary>Properties of `models`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "alias",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "mode": "default",
      "name": "string",
      "models": [
        {
          "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
    }
  }
}
```

---

### PATCH /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}

Updates an alias for a deployment.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `aliasId` | string | Yes | ID of the alias |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the property you want to update Enum: "/name", "/models" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New Name',
      },
      {
        op: 'replace',
        path: '/models',
        value: 'modelId',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New Name"},{"op":"replace","path":"/models","value":"modelId"}]'
```

---

### DELETE /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}

Delete an alias from a deployment.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `aliasId` | string | Yes | ID of the alias |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/deployments/{deploymentId}/aliases/{aliasId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases/{aliasId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `aliasName` | string | Yes | The name of the ML Deployment Alias that will be used to determine which model should be used to produce predictions |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeNotPredictedReason` | boolean | No | If true, reason why a prediction was not produced included response |
| `includeShap` | boolean | No | If true, shap values included in response |
| `includeSource` | boolean | No | If true, source data included in response |
| `index` | string | No | The name of the feature in the source data to use as an index in the response data. The column will be included with its original name and values. This is intended to allow the caller to join results with source data. |

#### Request Body

Request payload containing the dataset for predictions. Date features
must be in ISO 8601 format.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rows` | array[] | No | Rows of the dataset from which to produce predictions. Date features must be in ISO 8601 format. |
| `schema` | object[] | No | List of features in the dataset. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of a feature in the dataset |

</details>

#### Responses

##### 200

Stream of combined prediction output returned successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "realtime-prediction" |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rows` | array[] | No | Rows of the dataset from which to produce predictions |
| `schema` | object[] | No | List of features in the dataset |

<details>
<summary>Properties of `schema`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 409

`Conflict`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run',
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
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"rows":[["string"]],"schema":[{"name":"string"}]}'
```

**Example Response:**

```json
{
  "data": {
    "type": "realtime-prediction",
    "attributes": {
      "rows": [
        [
          "string"
        ]
      ],
      "schema": [
        {
          "name": "string"
        }
      ]
    }
  }
}
```

---

### GET /api/v1/ml/deployments/{deploymentId}/batch-predictions

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Batch prediction fields by which you can filter responses.<br><br> - `aliasId` UUID string - ID of an alias within the batch prediction - `createdBy` ID string - `deploymentId` UUID string - ID of a deployment of a model associated with the experiment - `experimentId` UUID string - ID of experiment in which model(s) exist - `experimentVersionId` UUID string - ID of experiment version in which model(s) exist - `modelId` UUID string - By model ID - `ownerId` ID string of batch prediction owner |
| `sort` | string | No | Field(s) by which to sort response  Enum: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "batch-prediction" |
| `attributes` | object | Yes | A batch prediction job configuration |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | No | Status of this batch prediction Enum: "modified", "ready", "error", "cancelled", "pending" |
| `aliasId` | string | No | ID of an alias |
| `ownerId` | string | No | ID of owner/user for this entity |
| `schedule` | object | No | Batch prediction job schedule |
| `createdAt` | string | No | Timestamp when this was created |
| `createdBy` | string | No | ID of the owner/user that ran this prediction batch |
| `dataSetId` | string | No | The Qlik catalog dataset ID |
| `datasetId` | string | No | ID of the dataset with the prediction results |
| `updatedAt` | string | No | Timestamp when this was updated |
| `writeback` | object | No | Sets which files, file names, and spaces are used to write results of batch predictions (output files) to the catalog.  Note that for predictions based on time series models, `dstShapName` and `dstCoordShapName` do not apply and will be ignored if set. |
| `indexColumn` | string | No | A optional column name upon which to create an index. Must be unique for every row. If not included, Qlik will create a unique index column. |
| `deploymentId` | string | No | ID of a model deployment |
| `errorMessage` | string | No | JSON string of error object |
| `outputDataset` | string | No | Where to output dataset |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `schedule`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `writeback`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}/batch-predictions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId}/batch-predictions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "batch-prediction",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "status": "modified",
        "aliasId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "ownerId": "string",
        "schedule": {
          "status": "pending",
          "timezone": "America/Toronto",
          "recurrence": [
            [
              "Daily at 11:10:00 AM [\"RRULE:FREQ=DAILY;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]",
              "Weekly on Mondays at 11:10:00 AM [\"RRULE:FREQ=WEEKLY;INTERVAL:1;BYDAY=MO;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]"
            ]
          ],
          "endDateTime": "string",
          "chronosJobId": "string",
          "startDateTime": "string",
          "failureAttempts": 42,
          "applyDatasetChangeOnly": true,
          "lastSuccessfulDateTime": "string"
        },
        "createdAt": "string",
        "createdBy": "string",
        "dataSetId": "672e55cfcadfb8a18281523e",
        "datasetId": "string",
        "updatedAt": "string",
        "writeback": {
          "format": "parquet",
          "dstName": "string",
          "spaceId": "string",
          "dstShapName": "string",
          "dstSourceName": "string",
          "dstCoordShapName": "string",
          "dstNotPredictedName": "string"
        },
        "indexColumn": "string",
        "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "errorMessage": "string",
        "outputDataset": "string"
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/ml/deployments/{deploymentId}/batch-predictions

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "batch-prediction" |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of this entity |
| `aliasId` | string | No | ID of an alias |
| `schedule` | object | No | Configuration to schedule a batch prediction |
| `dataSetId` | string | No | The Qlik catalog dataset ID |
| `writeback` | object | No | Sets which files, file names, and spaces are used to write results of batch predictions (output files) to the catalog.  Note that for predictions based on time series models, `dstShapName` and `dstCoordShapName` do not apply and will be ignored if set. |
| `description` | string | No |  |
| `indexColumn` | string | No | A optional column name upon which to create an index. Must be unique for every row. If not included, Qlik will create a unique index column. |
| `deploymentId` | string | No | ID of a model deployment |

<details>
<summary>Properties of `schedule`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `writeback`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

`Created`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "batch-prediction" |
| `attributes` | object | Yes | A batch prediction job configuration |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | No | Status of this batch prediction Enum: "modified", "ready", "error", "cancelled", "pending" |
| `aliasId` | string | No | ID of an alias |
| `ownerId` | string | No | ID of owner/user for this entity |
| `schedule` | object | No | Batch prediction job schedule |
| `createdAt` | string | No | Timestamp when this was created |
| `createdBy` | string | No | ID of the owner/user that ran this prediction batch |
| `dataSetId` | string | No | The Qlik catalog dataset ID |
| `datasetId` | string | No | ID of the dataset with the prediction results |
| `updatedAt` | string | No | Timestamp when this was updated |
| `writeback` | object | No | Sets which files, file names, and spaces are used to write results of batch predictions (output files) to the catalog.  Note that for predictions based on time series models, `dstShapName` and `dstCoordShapName` do not apply and will be ignored if set. |
| `indexColumn` | string | No | A optional column name upon which to create an index. Must be unique for every row. If not included, Qlik will create a unique index column. |
| `deploymentId` | string | No | ID of a model deployment |
| `errorMessage` | string | No | JSON string of error object |
| `outputDataset` | string | No | Where to output dataset |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `schedule`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `writeback`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/batch-predictions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'batch-prediction',
        attributes: {
          name: 'string',
          aliasId:
            'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
          schedule: {
            timezone: 'America/Toronto',
            recurrence: [
              'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=16;BYMINUTE=30;BYSECOND=0',
            ],
            endDateTime: '2035-12-31T23:59:00',
            startDateTime: '2035-12-25T00:00:00',
            applyDatasetChangeOnly: true,
          },
          dataSetId: '672e55cfcadfb8a18281523e',
          writeback: {
            format: 'parquet',
            dstName: 'string',
            spaceId: 'string',
            dstShapName: 'string',
            dstSourceName: 'string',
            dstCoordShapName: 'string',
            dstNotPredictedName: 'string',
          },
          description: 'string',
          indexColumn: 'string',
          deploymentId:
            'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/batch-predictions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"batch-prediction","attributes":{"name":"string","aliasId":"c35f4b70-3ce4-4a30-b62b-2aef16943bc4","schedule":{"timezone":"America/Toronto","recurrence":["RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=16;BYMINUTE=30;BYSECOND=0"],"endDateTime":"2035-12-31T23:59:00","startDateTime":"2035-12-25T00:00:00","applyDatasetChangeOnly":true},"dataSetId":"672e55cfcadfb8a18281523e","writeback":{"format":"parquet","dstName":"string","spaceId":"string","dstShapName":"string","dstSourceName":"string","dstCoordShapName":"string","dstNotPredictedName":"string"},"description":"string","indexColumn":"string","deploymentId":"c35f4b70-3ce4-4a30-b62b-2aef16943bc4"}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "batch-prediction",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "status": "modified",
      "aliasId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "ownerId": "string",
      "schedule": {
        "status": "pending",
        "timezone": "America/Toronto",
        "recurrence": [
          [
            "Daily at 11:10:00 AM [\"RRULE:FREQ=DAILY;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]",
            "Weekly on Mondays at 11:10:00 AM [\"RRULE:FREQ=WEEKLY;INTERVAL:1;BYDAY=MO;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]"
          ]
        ],
        "endDateTime": "string",
        "chronosJobId": "string",
        "startDateTime": "string",
        "failureAttempts": 42,
        "applyDatasetChangeOnly": true,
        "lastSuccessfulDateTime": "string"
      },
      "createdAt": "string",
      "createdBy": "string",
      "dataSetId": "672e55cfcadfb8a18281523e",
      "datasetId": "string",
      "updatedAt": "string",
      "writeback": {
        "format": "parquet",
        "dstName": "string",
        "spaceId": "string",
        "dstShapName": "string",
        "dstSourceName": "string",
        "dstCoordShapName": "string",
        "dstNotPredictedName": "string"
      },
      "indexColumn": "string",
      "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "errorMessage": "string",
      "outputDataset": "string"
    }
  }
}
```

---

### GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "batch-prediction" |
| `attributes` | object | Yes | A batch prediction job configuration |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | No | Status of this batch prediction Enum: "modified", "ready", "error", "cancelled", "pending" |
| `aliasId` | string | No | ID of an alias |
| `ownerId` | string | No | ID of owner/user for this entity |
| `schedule` | object | No | Batch prediction job schedule |
| `createdAt` | string | No | Timestamp when this was created |
| `createdBy` | string | No | ID of the owner/user that ran this prediction batch |
| `dataSetId` | string | No | The Qlik catalog dataset ID |
| `datasetId` | string | No | ID of the dataset with the prediction results |
| `updatedAt` | string | No | Timestamp when this was updated |
| `writeback` | object | No | Sets which files, file names, and spaces are used to write results of batch predictions (output files) to the catalog.  Note that for predictions based on time series models, `dstShapName` and `dstCoordShapName` do not apply and will be ignored if set. |
| `indexColumn` | string | No | A optional column name upon which to create an index. Must be unique for every row. If not included, Qlik will create a unique index column. |
| `deploymentId` | string | No | ID of a model deployment |
| `errorMessage` | string | No | JSON string of error object |
| `outputDataset` | string | No | Where to output dataset |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `schedule`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `writeback`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "batch-prediction",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "status": "modified",
      "aliasId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "ownerId": "string",
      "schedule": {
        "status": "pending",
        "timezone": "America/Toronto",
        "recurrence": [
          [
            "Daily at 11:10:00 AM [\"RRULE:FREQ=DAILY;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]",
            "Weekly on Mondays at 11:10:00 AM [\"RRULE:FREQ=WEEKLY;INTERVAL:1;BYDAY=MO;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]"
          ]
        ],
        "endDateTime": "string",
        "chronosJobId": "string",
        "startDateTime": "string",
        "failureAttempts": 42,
        "applyDatasetChangeOnly": true,
        "lastSuccessfulDateTime": "string"
      },
      "createdAt": "string",
      "createdBy": "string",
      "dataSetId": "672e55cfcadfb8a18281523e",
      "datasetId": "string",
      "updatedAt": "string",
      "writeback": {
        "format": "parquet",
        "dstName": "string",
        "spaceId": "string",
        "dstShapName": "string",
        "dstSourceName": "string",
        "dstCoordShapName": "string",
        "dstNotPredictedName": "string"
      },
      "indexColumn": "string",
      "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "errorMessage": "string",
      "outputDataset": "string"
    }
  }
}
```

---

### PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the property you want to update Enum: "/name", "/description", "/dataSetId", "/indexColumn", "/applyDatasetChangeOnly", "/ownerId", "/writeback/spaceId", "/writeback/format", "/writeback/dstName", "/writeback/dstShapName", "/writeback/dstCoordShapName", "/writeback/dstNotPredictedName", "/writeback/dstSourceName" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New Name',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New Name"}]'
```

---

### DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Responses

##### 202

`Accepted`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "job" |
| `attributes` | object | Yes |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | Yes |  |
| `corrId` | string | Yes | The ID of a correlated resource of corrType |
| `status` | string | Yes | Status of this job Enum: "pending", "completed", "cancelled", "error", "deleted_resource" |
| `details` | object | Yes |  |
| `jobType` | string | Yes | The type for this job Enum: "prediction" |
| `modelId` | string | Yes | ID of the model |
| `success` | boolean | Yes |  |
| `trigger` | string | Yes |  |
| `corrType` | string | Yes | Types names of correlated resources (batch 'prediction' and experiment_version)  Enum: "batch-prediction", "experiment-version" |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `createdAt` | string | Yes | Timestamp when this was created |
| `createdBy` | string | Yes | ID of the owner/user that created this entity |
| `deletedAt` | string | Yes | Timestamp when this is deleted |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `parentName` | string | Yes |  |
| `parentJobId` | string | No | ID of the current job's parent |
| `deploymentId` | string | Yes | ID of a model deployment |
| `rowsPredicted` | number | No |  |
| `experimentVersionNumber` | string | No |  |

<details>
<summary>Properties of `details`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict',
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
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/actions/predict" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "job",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "corrId": "string",
      "status": "pending",
      "details": {
        "isScheduled": true,
        "outputFiles": [
          {
            "key": "string",
            "path": "string",
            "spaceId": "string",
            "fileName": "string",
            "fileType": "qvd, parquet, csv"
          }
        ],
        "lineageSchemaUpdated": true
      },
      "jobType": "prediction",
      "modelId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "success": true,
      "trigger": "string",
      "corrType": "batch-prediction",
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "createdAt": "string",
      "createdBy": "string",
      "deletedAt": "string",
      "updatedAt": "string",
      "parentName": "string",
      "parentJobId": "string",
      "deploymentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "rowsPredicted": 42,
      "experimentVersionNumber": "string"
    }
  }
}
```

---

### GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule

Retrieves the schedule for a batch prediction.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "batch-prediction-schedule" |
| `attributes` | object | Yes | Batch prediction job schedule |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The status of the schedule Enum: "pending", "active", "error", "error_scheduler_unreachable", "error_scheduler_callback_error", "licence_advanced_features_required", "failing_schedule_permission" |
| `timezone` | string | No | Timezone used for the date-time fields |
| `recurrence` | string[] | No | Recurrence rules. Maximum is DAILY but you can specify the hour, minute, and second it runs each day. One string per rule. |
| `endDateTime` | string | No | When the job finished |
| `chronosJobId` | string | No | The ID of the chronos job |
| `startDateTime` | string | No | When the job is scheduled to start |
| `failureAttempts` | number | No | Number of times a scheduled prediction job has failed |
| `applyDatasetChangeOnly` | boolean | No | If true, only run prediction if dataset has changed to avoid duplicates. If set to false, re-runs predictions on unchanged datasets. |
| `lastSuccessfulDateTime` | string | No | When the last successful job happened |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule',
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
# qlik-cli has not implemented support for GET /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "batch-prediction-schedule",
    "attributes": {
      "status": "pending",
      "timezone": "America/Toronto",
      "recurrence": [
        [
          "Daily at 11:10:00 AM [\"RRULE:FREQ=DAILY;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]",
          "Weekly on Mondays at 11:10:00 AM [\"RRULE:FREQ=WEEKLY;INTERVAL:1;BYDAY=MO;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]"
        ]
      ],
      "endDateTime": "string",
      "chronosJobId": "string",
      "startDateTime": "string",
      "failureAttempts": 42,
      "applyDatasetChangeOnly": true,
      "lastSuccessfulDateTime": "string"
    }
  }
}
```

---

### PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule

Updates the schedule for a batch prediction.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the property you want to update Enum: "/startDateTime", "/endDateTime", "/timezone", "/recurrence", "/applyDatasetChangeOnly" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/startDateTime',
        value: '2022-09-14T12:00:00',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/startDateTime","value":"2022-09-14T12:00:00"}]'
```

---

### PUT /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule

Adds a schedule to a batch prediction.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "batch-prediction-schedule" |
| `attributes` | object | No | Configuration to schedule a batch prediction |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | Yes | Timezone used for the date-time fields |
| `recurrence` | string[] | Yes | Recurrence rules. Maximum is DAILY but you can specify the hour, minute, and second it runs each day. One string per rule. |
| `endDateTime` | string | No | When the job is scheduled to finish, date needs to be now or in future |
| `startDateTime` | string | Yes | When the job is scheduled to start, date needs to be now or in future |
| `applyDatasetChangeOnly` | boolean | Yes | If true, only run prediction if dataset has changed to avoid duplicates. If set to false, re-runs predictions on unchanged datasets. |

</details>

</details>

#### Responses

##### 201

`Created`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "batch-prediction-schedule" |
| `attributes` | object | Yes | Batch prediction job schedule |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The status of the schedule Enum: "pending", "active", "error", "error_scheduler_unreachable", "error_scheduler_callback_error", "licence_advanced_features_required", "failing_schedule_permission" |
| `timezone` | string | No | Timezone used for the date-time fields |
| `recurrence` | string[] | No | Recurrence rules. Maximum is DAILY but you can specify the hour, minute, and second it runs each day. One string per rule. |
| `endDateTime` | string | No | When the job finished |
| `chronosJobId` | string | No | The ID of the chronos job |
| `startDateTime` | string | No | When the job is scheduled to start |
| `failureAttempts` | number | No | Number of times a scheduled prediction job has failed |
| `applyDatasetChangeOnly` | boolean | No | If true, only run prediction if dataset has changed to avoid duplicates. If set to false, re-runs predictions on unchanged datasets. |
| `lastSuccessfulDateTime` | string | No | When the last successful job happened |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PUT /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'batch-prediction-schedule',
        attributes: {
          timezone: 'America/Toronto',
          recurrence: [
            'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=16;BYMINUTE=30;BYSECOND=0',
          ],
          endDateTime: '2035-12-31T23:59:00',
          startDateTime: '2035-12-25T00:00:00',
          applyDatasetChangeOnly: true,
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"batch-prediction-schedule","attributes":{"timezone":"America/Toronto","recurrence":["RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=16;BYMINUTE=30;BYSECOND=0"],"endDateTime":"2035-12-31T23:59:00","startDateTime":"2035-12-25T00:00:00","applyDatasetChangeOnly":true}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "batch-prediction-schedule",
    "attributes": {
      "status": "pending",
      "timezone": "America/Toronto",
      "recurrence": [
        [
          "Daily at 11:10:00 AM [\"RRULE:FREQ=DAILY;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]",
          "Weekly on Mondays at 11:10:00 AM [\"RRULE:FREQ=WEEKLY;INTERVAL:1;BYDAY=MO;BYHOUR=11;BYMINUTE=10;BYSECOND=0\"]"
        ]
      ],
      "endDateTime": "string",
      "chronosJobId": "string",
      "startDateTime": "string",
      "failureAttempts": 42,
      "applyDatasetChangeOnly": true,
      "lastSuccessfulDateTime": "string"
    }
  }
}
```

---

### DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule

Deletes the schedule from a batch prediction.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |
| `batchPredictionId` | string | Yes | ID of the batch prediction |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/batch-predictions/{batchPredictionId}/schedule" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/deployments/{deploymentId}/models/actions/add

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "deployed-models" |
| `attributes` | object | Yes |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deployedModelIds` | string[] | Yes | IDs of all models deployed to the deployment |

</details>

</details>

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/models/actions/add` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/models/actions/add',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'deployed-models',
        attributes: {
          deployedModelIds: [
            'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
          ],
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/models/actions/add yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/models/actions/add" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"deployed-models","attributes":{"deployedModelIds":["c35f4b70-3ce4-4a30-b62b-2aef16943bc4"]}}}'
```

---

### POST /api/v1/ml/deployments/{deploymentId}/models/actions/remove

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "deployed-models" |
| `attributes` | object | Yes |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deployedModelIds` | string[] | Yes | IDs of all models deployed to the deployment |

</details>

</details>

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/models/actions/remove` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/models/actions/remove',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'deployed-models',
        attributes: {
          deployedModelIds: [
            'c35f4b70-3ce4-4a30-b62b-2aef16943bc4',
          ],
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/models/actions/remove yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/models/actions/remove" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"deployed-models","attributes":{"deployedModelIds":["c35f4b70-3ce4-4a30-b62b-2aef16943bc4"]}}}'
```

---

### POST /api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deploymentId` | string | Yes | ID of the deployment |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeNotPredictedReason` | boolean | No | If true, reason why a prediction was not produced included response |
| `includeShap` | boolean | No | If true, shapley values included in response |
| `includeSource` | boolean | No | If true, source data included in response |
| `index` | string | No | The name of the feature in the source data to use as an index in the response data. The column will be included with its original name and values. This is intended to allow the caller to join results with source data. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rows` | array[] | No | Rows of the dataset from which to produce predictions. Date features must be in ISO 8601 format. |
| `schema` | object[] | No | List of features in the dataset. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of a feature in the dataset |

</details>

#### Responses

##### 200

Stream of combined prediction output returned successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "realtime-prediction" |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rows` | array[] | No | Rows of the dataset from which to produce predictions |
| `schema` | object[] | No | List of features in the dataset |

<details>
<summary>Properties of `schema`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 409

`Conflict`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run',
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
# qlik-cli has not implemented support for POST /api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments/{deploymentId}/realtime-predictions/actions/run" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"rows":[["string"]],"schema":[{"name":"string"}]}'
```

**Example Response:**

```json
{
  "data": {
    "type": "realtime-prediction",
    "attributes": {
      "rows": [
        [
          "string"
        ]
      ],
      "schema": [
        {
          "name": "string"
        }
      ]
    }
  }
}
```

---

### GET /api/v1/ml/experiments

Retrieves a list of experiments based on provided filter and sort
parameters.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Experiment fields by which you can filter responses within this tenant - `ownerId` ID string - ID of the owner/user that created the experiment - `spaceId` ID string (or empty string for personal space) - ID of the space where the experiment is saved. - `experimentVersionId` UUID string - ID of an experiment version in the experiment - `modelId` UUID string - ID of a model associated with the experiment - `deploymentId` UUID string - ID of a deployment of a model associated with the experiment |
| `sort` | string | No | Field(s) by which to sort response  Enum: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment" |
| `attributes` | object | Yes | An AutoML experiment |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `createdAt` | string | Yes | Timestamp when this was created |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `description` | string | No | Description of this entity |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "experiment",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "ownerId": "string",
        "spaceId": "string",
        "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "createdAt": "string",
        "updatedAt": "string",
        "description": "string"
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/ml/experiments

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Data container for ExperimentInput |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "experiment" |
| `attributes` | object | No | Experiment input attributes |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `description` | string | No | Description of this entity |

</details>

</details>

#### Responses

##### 201

`Created`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment" |
| `attributes` | object | Yes | An AutoML experiment |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `createdAt` | string | Yes | Timestamp when this was created |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `description` | string | No | Description of this entity |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/experiments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'experiment',
        attributes: {
          name: 'string',
          spaceId: 'string',
          description: 'string',
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/experiments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"experiment","attributes":{"name":"string","spaceId":"string","description":"string"}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "experiment",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "ownerId": "string",
      "spaceId": "string",
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "createdAt": "string",
      "updatedAt": "string",
      "description": "string"
    }
  }
}
```

---

### GET /api/v1/ml/experiments/{experimentId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment" |
| `attributes` | object | Yes | An AutoML experiment |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `spaceId` | string | Yes | Space ID for this entity (empty string for personal space) |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `createdAt` | string | Yes | Timestamp when this was created |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `description` | string | No | Description of this entity |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments/{experimentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments/{experimentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "experiment",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "ownerId": "string",
      "spaceId": "string",
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "createdAt": "string",
      "updatedAt": "string",
      "description": "string"
    }
  }
}
```

---

### PATCH /api/v1/ml/experiments/{experimentId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the property you want to update Enum: "/name", "/description", "/spaceId" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/experiments/{experimentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New name',
      },
      {
        op: 'replace',
        path: '/description',
        value: 'New description',
      },
      {
        op: 'replace',
        path: '/spaceId',
        value: 'NEW_SPACE_ID',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/experiments/{experimentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New name"},{"op":"replace","path":"/description","value":"New description"},{"op":"replace","path":"/spaceId","value":"NEW_SPACE_ID"}]'
```

---

### DELETE /api/v1/ml/experiments/{experimentId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/experiments/{experimentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/experiments/{experimentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/experiments/{experimentId}/actions/recommend-models

Returns model recommendations for a specified experiment, including the best-performing, fastest, and most accurate models based on evaluation metrics.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deployed` | boolean | No | Whether to only consider models that are already deployed |
| `algorithms` | string[] | No | The model algorithms to consider Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `fullSampling` | boolean | No | Whether to only consider models with 100% sampling |
| `versionNumbers` | integer[] | No | The versionNumbers of the experiment versions to consider models from |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "model-recommendation" |
| `attributes` | object | Yes | Model recommendations |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `bestModel` | object | No | A model based on an algorithm within an experiment version. |
| `fastestModel` | object | No | A model based on an algorithm within an experiment version. |
| `mostAccurateModel` | object | No | A model based on an algorithm within an experiment version. |

<details>
<summary>Properties of `bestModel`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `fastestModel`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `mostAccurateModel`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/experiments/{experimentId}/actions/recommend-models` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/actions/recommend-models',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      deployed: true,
      algorithms: ['catboost_classifier'],
      fullSampling: true,
      versionNumbers: [1],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/experiments/{experimentId}/actions/recommend-models yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/actions/recommend-models" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"deployed":true,"algorithms":["catboost_classifier"],"fullSampling":true,"versionNumbers":[1]}'
```

**Example Response:**

```json
{
  "data": {
    "type": "model-recommendation",
    "attributes": {
      "bestModel": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "hpoNum": 42,
        "seqNum": 42,
        "status": "pending",
        "columns": [
          "string"
        ],
        "metrics": {
          "predictionSpeed": 42
        },
        "batchNum": 42,
        "algoAbbrv": "CATBC",
        "algorithm": "string",
        "createdAt": "string",
        "updatedAt": "string",
        "modelState": "pending",
        "description": "string",
        "anomalyRatio": 42,
        "errorMessage": "string",
        "samplingRatio": 42,
        "binningFeatures": [
          "string"
        ],
        "droppedFeatures": [
          {
            "name": "string",
            "reason": "highly_correlated"
          }
        ],
        "experimentVersionId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "powerTransformFeatures": [
          "string"
        ],
        "binaryImbalanceSampling": {
          "sampleClass": "string",
          "sampleRatio": 42,
          "sampleDirection": "up"
        }
      },
      "fastestModel": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "hpoNum": 42,
        "seqNum": 42,
        "status": "pending",
        "columns": [
          "string"
        ],
        "metrics": {
          "predictionSpeed": 42
        },
        "batchNum": 42,
        "algoAbbrv": "CATBC",
        "algorithm": "string",
        "createdAt": "string",
        "updatedAt": "string",
        "modelState": "pending",
        "description": "string",
        "anomalyRatio": 42,
        "errorMessage": "string",
        "samplingRatio": 42,
        "binningFeatures": [
          "string"
        ],
        "droppedFeatures": [
          {
            "name": "string",
            "reason": "highly_correlated"
          }
        ],
        "experimentVersionId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "powerTransformFeatures": [
          "string"
        ],
        "binaryImbalanceSampling": {
          "sampleClass": "string",
          "sampleRatio": 42,
          "sampleDirection": "up"
        }
      },
      "mostAccurateModel": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "hpoNum": 42,
        "seqNum": 42,
        "status": "pending",
        "columns": [
          "string"
        ],
        "metrics": {
          "predictionSpeed": 42
        },
        "batchNum": 42,
        "algoAbbrv": "CATBC",
        "algorithm": "string",
        "createdAt": "string",
        "updatedAt": "string",
        "modelState": "pending",
        "description": "string",
        "anomalyRatio": 42,
        "errorMessage": "string",
        "samplingRatio": 42,
        "binningFeatures": [
          "string"
        ],
        "droppedFeatures": [
          {
            "name": "string",
            "reason": "highly_correlated"
          }
        ],
        "experimentVersionId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "powerTransformFeatures": [
          "string"
        ],
        "binaryImbalanceSampling": {
          "sampleClass": "string",
          "sampleRatio": 42,
          "sampleDirection": "up"
        }
      }
    }
  }
}
```

---

### GET /api/v1/ml/experiments/{experimentId}/models

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Model fields you can filter by:<br><br>  - `experimentVersionId` UUID string - Find by experiment version ID - `batchNum` UUID string - Search by batch number - `isHpo` boolean - Is hyperparameter optimization used? - `isMetrics` boolean - Are metrics for regression, binary, or multiclass are used? - `id` UUID string - Find by model ID - `algorithm` enum string - Find by algorithm<br><br>    - Valid algorithms: catboost_classifier, catboost_regression,     elasticnet_regression, gaussian_nb, kneighbors_classifier,     lasso_regression, lasso, lgbm_classifier, lgbm_regression,     linear_regression, logistic_regression, random_forest_classifier,     random_forest_regression, sgd_regression, xgb_classifier,     xgb_regression<br><br>  - `status` enum string - find by status<br><br>   - Valid statuses: pending, training_requested, training_done, ready, error<br><br> - `hasDeployment` boolean - Models that are part of a deployment - `nameContains` string - Models with name includes this case-insensitive string - `exactName` string - Models with exact name. Model names may not be unique - `samplingRatio` number - Find models by sampling ratio - `modelState` enum string - State by which to find models<br><br>   - Valid states: `pending, enabled, disabled, inactive` |
| `sort` | string | No | Field(s) by which to sort response  Enum: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "model" |
| `attributes` | object | Yes | A model based on an algorithm within an experiment version. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `hpoNum` | number | No | Version number of the hyperparameter optimization |
| `seqNum` | number | No | Model sequence number within the experiment version |
| `status` | string | No | Model status. These are the status of the model in relation to experiments (i.e. training status).  Enum: "pending", "training_requested", "training_done", "ready", "error" |
| `columns` | string[] | No | Dataset columns selected as features |
| `metrics` | object | No | Model metrics based on the type of model |
| `batchNum` | number | No | Batch number indicates the index of the experiment version fold (most relevant when HPO is enabled) |
| `algoAbbrv` | string | No | Model algorithm name abbreviation Enum: "CATBC", "CATBR", "ELNC", "GNBC", "LGBMC", "LGBMR", "LINR", "LOGC", "LSOC", "RAFC", "RAFR", "SGDR", "XGBC", "XGBR" |
| `algorithm` | string | No | The algorithm used by this model |
| `createdAt` | string | No | Timestamp when this was created |
| `updatedAt` | string | No | Timestamp when this was updated |
| `modelState` | string | No | Model state. These are the state of the model in relation to deployments.  Enum: "pending", "enabled", "disabled", "inactive" |
| `description` | string | No | Description of this entity |
| `anomalyRatio` | number | No |  |
| `errorMessage` | string | No | JSON string of error object |
| `samplingRatio` | number | No | Ratio of sample data in relation to the dataset |
| `binningFeatures` | string[] | No |  |
| `droppedFeatures` | object[] | No | Features dropped because they're unsuitable |
| `experimentVersionId` | string | No | ID of the experiment version |
| `powerTransformFeatures` | string[] | No |  |
| `binaryImbalanceSampling` | object | No |  |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metrics`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `droppedFeatures`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `binaryImbalanceSampling`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments/{experimentId}/models` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/models',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments/{experimentId}/models yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/models" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "model",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "hpoNum": 42,
        "seqNum": 42,
        "status": "pending",
        "columns": [
          "string"
        ],
        "metrics": {
          "binary": {
            "f1": 42,
            "auc": 42,
            "mcc": 42,
            "npv": 42,
            "f1Test": 42,
            "recall": 42,
            "aucTest": 42,
            "fallout": 42,
            "logLoss": 42,
            "mccTest": 42,
            "npvTest": 42,
            "accuracy": 42,
            "missRate": 42,
            "precision": 42,
            "threshold": 42,
            "recallTest": 42,
            "falloutTest": 42,
            "logLossTest": 42,
            "specificity": 42,
            "accuracyTest": 42,
            "missRateTest": 42,
            "trueNegative": 42,
            "truePositive": 42,
            "falseNegative": 42,
            "falsePositive": 42,
            "precisionTest": 42,
            "thresholdTest": 42,
            "specificityTest": 42,
            "trueNegativeTest": 42,
            "truePositiveTest": 42,
            "falseNegativeTest": 42,
            "falsePositiveTest": 42
          },
          "multiclass": {
            "f1Macro": 42,
            "f1Micro": 42,
            "accuracy": 42,
            "f1Weighted": 42,
            "f1MacroTest": 42,
            "f1MicroTest": 42,
            "accuracyTest": 42,
            "f1WeightedTest": 42,
            "confusionMatrix": "string",
            "confusionMatrixTest": "string"
          },
          "regression": {
            "r2": 42,
            "mae": 42,
            "mse": 42,
            "rmse": 42,
            "r2Test": 42,
            "maeTest": 42,
            "mseTest": 42,
            "rmseTest": 42
          },
          "timeseries": {
            "mae": 42,
            "mape": 42,
            "mase": 42,
            "rmse": 42,
            "mdape": 42,
            "smape": 42,
            "wmape": 42,
            "mnrmse": 42,
            "maeTest": 42,
            "mdnrmse": 42,
            "mapeTest": 42,
            "maseTest": 42,
            "rmseTest": 42,
            "mdapeTest": 42,
            "smapeTest": 42,
            "wmapeTest": 42,
            "mnrmseTest": 42,
            "mdnrmseTest": 42
          }
        },
        "batchNum": 42,
        "algoAbbrv": "CATBC",
        "algorithm": "string",
        "createdAt": "string",
        "updatedAt": "string",
        "modelState": "pending",
        "description": "string",
        "anomalyRatio": 42,
        "errorMessage": "string",
        "samplingRatio": 42,
        "binningFeatures": [
          "string"
        ],
        "droppedFeatures": [
          {
            "name": "string",
            "reason": "highly_correlated"
          }
        ],
        "experimentVersionId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "powerTransformFeatures": [
          "string"
        ],
        "binaryImbalanceSampling": {
          "sampleClass": "string",
          "sampleRatio": 42,
          "sampleDirection": "up"
        }
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### GET /api/v1/ml/experiments/{experimentId}/models/{modelId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |
| `modelId` | string | Yes | ID of the model |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "model" |
| `attributes` | object | Yes | A model based on an algorithm within an experiment version. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `hpoNum` | number | No | Version number of the hyperparameter optimization |
| `seqNum` | number | No | Model sequence number within the experiment version |
| `status` | string | No | Model status. These are the status of the model in relation to experiments (i.e. training status).  Enum: "pending", "training_requested", "training_done", "ready", "error" |
| `columns` | string[] | No | Dataset columns selected as features |
| `metrics` | object | No | Model metrics based on the type of model |
| `batchNum` | number | No | Batch number indicates the index of the experiment version fold (most relevant when HPO is enabled) |
| `algoAbbrv` | string | No | Model algorithm name abbreviation Enum: "CATBC", "CATBR", "ELNC", "GNBC", "LGBMC", "LGBMR", "LINR", "LOGC", "LSOC", "RAFC", "RAFR", "SGDR", "XGBC", "XGBR" |
| `algorithm` | string | No | The algorithm used by this model |
| `createdAt` | string | No | Timestamp when this was created |
| `updatedAt` | string | No | Timestamp when this was updated |
| `modelState` | string | No | Model state. These are the state of the model in relation to deployments.  Enum: "pending", "enabled", "disabled", "inactive" |
| `description` | string | No | Description of this entity |
| `anomalyRatio` | number | No |  |
| `errorMessage` | string | No | JSON string of error object |
| `samplingRatio` | number | No | Ratio of sample data in relation to the dataset |
| `binningFeatures` | string[] | No |  |
| `droppedFeatures` | object[] | No | Features dropped because they're unsuitable |
| `experimentVersionId` | string | No | ID of the experiment version |
| `powerTransformFeatures` | string[] | No |  |
| `binaryImbalanceSampling` | object | No |  |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metrics`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `droppedFeatures`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `binaryImbalanceSampling`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments/{experimentId}/models/{modelId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/models/{modelId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments/{experimentId}/models/{modelId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/models/{modelId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "model",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "hpoNum": 42,
      "seqNum": 42,
      "status": "pending",
      "columns": [
        "string"
      ],
      "metrics": {
        "binary": {
          "f1": 42,
          "auc": 42,
          "mcc": 42,
          "npv": 42,
          "f1Test": 42,
          "recall": 42,
          "aucTest": 42,
          "fallout": 42,
          "logLoss": 42,
          "mccTest": 42,
          "npvTest": 42,
          "accuracy": 42,
          "missRate": 42,
          "precision": 42,
          "threshold": 42,
          "recallTest": 42,
          "falloutTest": 42,
          "logLossTest": 42,
          "specificity": 42,
          "accuracyTest": 42,
          "missRateTest": 42,
          "trueNegative": 42,
          "truePositive": 42,
          "falseNegative": 42,
          "falsePositive": 42,
          "precisionTest": 42,
          "thresholdTest": 42,
          "specificityTest": 42,
          "trueNegativeTest": 42,
          "truePositiveTest": 42,
          "falseNegativeTest": 42,
          "falsePositiveTest": 42
        },
        "multiclass": {
          "f1Macro": 42,
          "f1Micro": 42,
          "accuracy": 42,
          "f1Weighted": 42,
          "f1MacroTest": 42,
          "f1MicroTest": 42,
          "accuracyTest": 42,
          "f1WeightedTest": 42,
          "confusionMatrix": "string",
          "confusionMatrixTest": "string"
        },
        "regression": {
          "r2": 42,
          "mae": 42,
          "mse": 42,
          "rmse": 42,
          "r2Test": 42,
          "maeTest": 42,
          "mseTest": 42,
          "rmseTest": 42
        },
        "timeseries": {
          "mae": 42,
          "mape": 42,
          "mase": 42,
          "rmse": 42,
          "mdape": 42,
          "smape": 42,
          "wmape": 42,
          "mnrmse": 42,
          "maeTest": 42,
          "mdnrmse": 42,
          "mapeTest": 42,
          "maseTest": 42,
          "rmseTest": 42,
          "mdapeTest": 42,
          "smapeTest": 42,
          "wmapeTest": 42,
          "mnrmseTest": 42,
          "mdnrmseTest": 42
        }
      },
      "batchNum": 42,
      "algoAbbrv": "CATBC",
      "algorithm": "string",
      "createdAt": "string",
      "updatedAt": "string",
      "modelState": "pending",
      "description": "string",
      "anomalyRatio": 42,
      "errorMessage": "string",
      "samplingRatio": 42,
      "binningFeatures": [
        "string"
      ],
      "droppedFeatures": [
        {
          "name": "string",
          "reason": "highly_correlated"
        }
      ],
      "experimentVersionId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "powerTransformFeatures": [
        "string"
      ],
      "binaryImbalanceSampling": {
        "sampleClass": "string",
        "sampleRatio": 42,
        "sampleDirection": "up"
      }
    }
  }
}
```

---

### GET /api/v1/ml/experiments/{experimentId}/versions

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Experiment version filter options - `isRunning` boolean - Is the experiment version running (training models)? - `isSettled` boolean - Is the experiment version settled? - `status` enum string - Status to filter by. Omit to get models of any status.   - Valid statuses: pending, ready, error, cancelled - `modelId` UUID string - ID of a model associated with the experiment |
| `sort` | string | No | Field(s) by which to sort response  Enum: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "experimentMode", "+experimentMode", "-experimentMode", "experimentType", "+experimentType", "-experimentType", "name", "+name", "-name", "status", "+status", "-status", "updatedAt", "+updatedAt", "-updatedAt", "versionNumber", "+versionNumber", "-versionNumber" |
| `limit` | integer | No | Number of results per page. Default is 32. |
| `offset` | integer | No | Number of rows to skip before getting page[size] |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No | Meta for FIND operations |
| `links` | object | Yes | Resource links included in paginated responses |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment-version" |
| `attributes` | object | Yes | An AutoML experiment version. This is a configuration for training models within an experiment. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | Yes | Current status of this entity Enum: "ready", "error", "cancelled", "pending", "dataprep_requested", "datasync_requested", "datasync_done" |
| `target` | string | Yes | The target field in the dataset |
| `pipeline` | object | No | Pipeline metadata including transformations to apply to columns and specific schema configuration data |
| `createdAt` | string | Yes | Timestamp when this was created |
| `dataSetId` | string | Yes | The Qlik catalog dataset ID |
| `profileId` | string | No | ID of the dataset profile with metadata about source data |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `algorithms` | string[] | No | List of algorithms selected for model training in this version  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `topModelId` | string | No | ID of the top model (based on training scores) in this experiment version |
| `dateIndexes` | string[] | No | A optional date column name to index |
| `errorMessage` | string | No | JSON string of error object |
| `experimentId` | string | Yes | ID of the experiment |
| `featuresList` | object[] | No | List of features from your dataset for creating Experiment Versions. This appears in from ProfileInsights response (in the defaultVersionConfig). You can adjust the default settings before using it as input to create or update Experiment Versions. |
| `lastBatchNum` | integer | No | Number of the last batch |
| `datasetOrigin` | string | No | Whether this is a new or other dataset Enum: "new", "changed", "refreshed", "same" |
| `versionNumber` | integer | No | 1-based sequential version number within the experiment |
| `experimentMode` | string | No | The model training mode for the experiment version Enum: "intelligent", "manual", "manual_hpo" |
| `experimentType` | string | Yes | Experiment type Enum: "binary", "multiclass", "regression" |
| `createdByUserId` | string | Yes | ID of owner/user for this entity |
| `trainingDuration` | integer | No | Optional training duration in seconds. If not provided, max value used. If provided, min 900 (15m) and max 21600 (6h). |
| `preprocessedInsights` | object[] | No | Preprocessed insights. Like feature insights but with fewer details. |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pipeline`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `featuresList`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `preprocessedInsights`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | Yes |  |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |
| `first` | object | Yes |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the last set of responses from `limit` minus `offset` to `limit` |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next set of responses |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous set of responses |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current set of responses |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the first set of responses from `offset` 0 to count `limit`` |

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments/{experimentId}/versions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/versions',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments/{experimentId}/versions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/versions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "type": "experiment-version",
      "attributes": {
        "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "name": "string",
        "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
        "status": "pending",
        "target": "TargetColumn",
        "pipeline": {
          "transforms": [
            {
              "column": {
                "name": "string",
                "changeType": "string"
              }
            }
          ]
        },
        "createdAt": "string",
        "dataSetId": "672e55cfcadfb8a18281523e",
        "profileId": "string",
        "updatedAt": "string",
        "algorithms": [
          "catboost_classifier"
        ],
        "topModelId": "string",
        "dateIndexes": [
          "string"
        ],
        "errorMessage": "string",
        "experimentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "featuresList": [
          {
            "name": "ColumnA",
            "include": true,
            "dataType": "STRING",
            "changeType": null,
            "featureType": "categorical",
            "parentFeature": null
          }
        ],
        "lastBatchNum": 42,
        "datasetOrigin": "new",
        "versionNumber": 42,
        "experimentMode": "intelligent",
        "experimentType": "binary",
        "createdByUserId": "string",
        "trainingDuration": 900,
        "preprocessedInsights": [
          {
            "name": "string",
            "insights": [],
            "willBeDropped": true
          }
        ]
      }
    }
  ],
  "meta": {
    "count": 42
  },
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/ml/experiments/{experimentId}/versions

Creates an experiment version.
Poll this version and check its `status` field to determine when models
are finished training.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "experiment-version" |
| `attributes` | object | Yes |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `target` | string | Yes | The target field in the dataset. Set in first experiment version and can't be changed in subsequent versions. |
| `pipeline` | object | No | Pipeline metadata including transformations to apply to columns and specific schema configuration data |
| `dataSetId` | string | Yes | The Qlik catalog dataset ID |
| `algorithms` | string[] | No | Algorithms used for model training in this version. See documentation for valid algorithms for each `experimentType`.  If not provided, defaults to all valid algorithms for your experimentType.  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `dateIndexes` | string[] | No | A optional date column name to index |
| `featuresList` | object[] | Yes | List of features from your dataset for creating Experiment Versions. This appears in from ProfileInsights response (in the defaultVersionConfig). You can adjust the default settings before using it as input to create or update Experiment Versions. |
| `datasetOrigin` | string | No | Whether this is a new or other dataset Enum: "new", "changed", "refreshed", "same" |
| `experimentMode` | string | Yes | The model training mode for the experiment version Enum: "intelligent", "manual", "manual_hpo" |
| `experimentType` | string | Yes | Experiment type Enum: "binary", "multiclass", "regression" |
| `trainingDuration` | integer | No | Optional training duration in seconds. If not provided, max value used. If provided, min 900 (15m) and max 21600 (6h). |

<details>
<summary>Properties of `pipeline`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `featuresList`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

`Accepted`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment-version" |
| `attributes` | object | Yes | An AutoML experiment version. This is a configuration for training models within an experiment. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | Yes | Current status of this entity Enum: "ready", "error", "cancelled", "pending", "dataprep_requested", "datasync_requested", "datasync_done" |
| `target` | string | Yes | The target field in the dataset |
| `pipeline` | object | No | Pipeline metadata including transformations to apply to columns and specific schema configuration data |
| `createdAt` | string | Yes | Timestamp when this was created |
| `dataSetId` | string | Yes | The Qlik catalog dataset ID |
| `profileId` | string | No | ID of the dataset profile with metadata about source data |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `algorithms` | string[] | No | List of algorithms selected for model training in this version  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `topModelId` | string | No | ID of the top model (based on training scores) in this experiment version |
| `dateIndexes` | string[] | No | A optional date column name to index |
| `errorMessage` | string | No | JSON string of error object |
| `experimentId` | string | Yes | ID of the experiment |
| `featuresList` | object[] | No | List of features from your dataset for creating Experiment Versions. This appears in from ProfileInsights response (in the defaultVersionConfig). You can adjust the default settings before using it as input to create or update Experiment Versions. |
| `lastBatchNum` | integer | No | Number of the last batch |
| `datasetOrigin` | string | No | Whether this is a new or other dataset Enum: "new", "changed", "refreshed", "same" |
| `versionNumber` | integer | No | 1-based sequential version number within the experiment |
| `experimentMode` | string | No | The model training mode for the experiment version Enum: "intelligent", "manual", "manual_hpo" |
| `experimentType` | string | Yes | Experiment type Enum: "binary", "multiclass", "regression" |
| `createdByUserId` | string | Yes | ID of owner/user for this entity |
| `trainingDuration` | integer | No | Optional training duration in seconds. If not provided, max value used. If provided, min 900 (15m) and max 21600 (6h). |
| `preprocessedInsights` | object[] | No | Preprocessed insights. Like feature insights but with fewer details. |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pipeline`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `featuresList`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `preprocessedInsights`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/experiments/{experimentId}/versions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/versions',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'experiment-version',
        attributes: {
          name: 'Experiment version name. Defaults to current date.',
          target: 'TargetColumn',
          pipeline: {
            transforms: [
              {
                column: {
                  name: 'string',
                  changeType: 'string',
                },
              },
            ],
          },
          dataSetId: '672e55cfcadfb8a18281523e',
          algorithms: ['catboost_classifier'],
          dateIndexes: ['string'],
          featuresList: [
            {
              name: 'ColumnA',
              include: true,
              dataType: 'STRING',
              changeType: null,
              featureType: 'categorical',
              parentFeature: null,
            },
          ],
          datasetOrigin: 'new',
          experimentMode: 'intelligent',
          experimentType: 'binary',
          trainingDuration: 900,
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/experiments/{experimentId}/versions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/versions" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"experiment-version","attributes":{"name":"Experiment version name. Defaults to current date.","target":"TargetColumn","pipeline":{"transforms":[{"column":{"name":"string","changeType":"string"}}]},"dataSetId":"672e55cfcadfb8a18281523e","algorithms":["catboost_classifier"],"dateIndexes":["string"],"featuresList":[{"name":"ColumnA","include":true,"dataType":"STRING","changeType":null,"featureType":"categorical","parentFeature":null}],"datasetOrigin":"new","experimentMode":"intelligent","experimentType":"binary","trainingDuration":900}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "experiment-version",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "status": "pending",
      "target": "TargetColumn",
      "pipeline": {
        "transforms": [
          {
            "column": {
              "name": "string",
              "changeType": "string"
            }
          }
        ]
      },
      "createdAt": "string",
      "dataSetId": "672e55cfcadfb8a18281523e",
      "profileId": "string",
      "updatedAt": "string",
      "algorithms": [
        "catboost_classifier"
      ],
      "topModelId": "string",
      "dateIndexes": [
        "string"
      ],
      "errorMessage": "string",
      "experimentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "featuresList": [
        {
          "name": "ColumnA",
          "include": true,
          "dataType": "STRING",
          "changeType": null,
          "featureType": "categorical",
          "parentFeature": null
        }
      ],
      "lastBatchNum": 42,
      "datasetOrigin": "new",
      "versionNumber": 42,
      "experimentMode": "intelligent",
      "experimentType": "binary",
      "createdByUserId": "string",
      "trainingDuration": 900,
      "preprocessedInsights": [
        {
          "name": "string",
          "insights": [],
          "willBeDropped": true
        }
      ]
    }
  }
}
```

---

### GET /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |
| `experimentVersionId` | string | Yes | ID of the experiment version |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "experiment-version" |
| `attributes` | object | Yes | An AutoML experiment version. This is a configuration for training models within an experiment. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `name` | string | No | Name of this entity |
| `errors` | object[] | No | JSON string with list of error objects |
| `status` | string | Yes | Current status of this entity Enum: "ready", "error", "cancelled", "pending", "dataprep_requested", "datasync_requested", "datasync_done" |
| `target` | string | Yes | The target field in the dataset |
| `pipeline` | object | No | Pipeline metadata including transformations to apply to columns and specific schema configuration data |
| `createdAt` | string | Yes | Timestamp when this was created |
| `dataSetId` | string | Yes | The Qlik catalog dataset ID |
| `profileId` | string | No | ID of the dataset profile with metadata about source data |
| `updatedAt` | string | Yes | Timestamp when this was updated |
| `algorithms` | string[] | No | List of algorithms selected for model training in this version  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `topModelId` | string | No | ID of the top model (based on training scores) in this experiment version |
| `dateIndexes` | string[] | No | A optional date column name to index |
| `errorMessage` | string | No | JSON string of error object |
| `experimentId` | string | Yes | ID of the experiment |
| `featuresList` | object[] | No | List of features from your dataset for creating Experiment Versions. This appears in from ProfileInsights response (in the defaultVersionConfig). You can adjust the default settings before using it as input to create or update Experiment Versions. |
| `lastBatchNum` | integer | No | Number of the last batch |
| `datasetOrigin` | string | No | Whether this is a new or other dataset Enum: "new", "changed", "refreshed", "same" |
| `versionNumber` | integer | No | 1-based sequential version number within the experiment |
| `experimentMode` | string | No | The model training mode for the experiment version Enum: "intelligent", "manual", "manual_hpo" |
| `experimentType` | string | Yes | Experiment type Enum: "binary", "multiclass", "regression" |
| `createdByUserId` | string | Yes | ID of owner/user for this entity |
| `trainingDuration` | integer | No | Optional training duration in seconds. If not provided, max value used. If provided, min 900 (15m) and max 21600 (6h). |
| `preprocessedInsights` | object[] | No | Preprocessed insights. Like feature insights but with fewer details. |

<details>
<summary>Properties of `errors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pipeline`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `featuresList`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `preprocessedInsights`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "experiment-version",
    "attributes": {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "string",
      "errors": "[{\"code\":\"AML-145\",\"title\":\"datasync dependent service error, service profile\",\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\",\"meta\":{\"errorId\":\"c1546687-ad5d-4002-87f6-8c9711298db1\"}}]\n",
      "status": "pending",
      "target": "TargetColumn",
      "pipeline": {
        "transforms": [
          {
            "column": {
              "name": "string",
              "changeType": "string"
            }
          }
        ]
      },
      "createdAt": "string",
      "dataSetId": "672e55cfcadfb8a18281523e",
      "profileId": "string",
      "updatedAt": "string",
      "algorithms": [
        "catboost_classifier"
      ],
      "topModelId": "string",
      "dateIndexes": [
        "string"
      ],
      "errorMessage": "string",
      "experimentId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "featuresList": [
        {
          "name": "ColumnA",
          "include": true,
          "dataType": "STRING",
          "changeType": null,
          "featureType": "categorical",
          "parentFeature": null
        }
      ],
      "lastBatchNum": 42,
      "datasetOrigin": "new",
      "versionNumber": 42,
      "experimentMode": "intelligent",
      "experimentType": "binary",
      "createdByUserId": "string",
      "trainingDuration": 900,
      "preprocessedInsights": [
        {
          "name": "string",
          "insights": [],
          "willBeDropped": true
        }
      ]
    }
  }
}
```

---

### PATCH /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |
| `experimentVersionId` | string | Yes | ID of the experiment version |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | All patch requests use the replace operation Enum: "replace" |
| `path` | string | Yes | Path for the properties you can update.  Enum: "/name" |
| `value` | any | Yes | Use for fields that can be `any` type (string, number, etc.) |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `PATCH /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New name',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"New name"}]'
```

---

### DELETE /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentId` | string | Yes | ID of the experiment |
| `experimentVersionId` | string | Yes | ID of the experiment version |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `DELETE /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/experiments/{experimentId}/versions/{experimentVersionId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel

Cancels jobs for an experiment version or batch prediction.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `corrType` | string | Yes | The type of a resource paired with a corrId Enum: "batch-prediction", "experiment-version" |
| `corrId` | string | Yes | The ID of a correlated resource of corrType |

#### Responses

##### 204

`No Content`

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 405

`Method Not Allowed`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel',
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
# qlik-cli has not implemented support for POST /api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/jobs/{corrType}/{corrId}/actions/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ml/profile-insights

Starts creating profile insights for an experiment dataset.
This is an asynchronous operation. A `202 Accepted` response indicates
that the process has started successfully. Use the link in the response
to check the status.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Data wrapper for request input |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "profile-insights" |
| `attributes` | object | No | The request body for this resource |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `target` | string | No | Optional selected target provided on subsequent requests |
| `include` | string | No | Fields to include in the response.  Currently only supported value is `dataSetProfile`.  When `dataSetProfile` is specified, the response includes the full dataset profile.  Enum: "dataSetProfile" |
| `dataSetId` | string | No | The Qlik catalog dataset ID |
| `shouldWait` | boolean | No | Whether the server should or client should manage polling/waiting |
| `experimentType` | string | No | Experiment type Enum: "binary", "multiclass", "regression" |

</details>

</details>

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "profile-insights" |
| `attributes` | object | Yes | Insights (metadata) about an experiment dataset |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of profile insights. Not available until `ready`.  Enum: "pending", "error", "ready" |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `insights` | object[] | No | List of feature insights object, one per feature in the dataset |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `algorithms` | string[] | No | List of algorithms available for the selected experiment type  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `isLargeCsv` | boolean | No | Is this a CSV dataset > 1GB? |
| `sizeInBytes` | integer | No | Size of the profiled dataset in bytes. |
| `numberOfRows` | number | No | Number of rows in the dataset.  When isLargeCsv is true, this is an estimate since their metadata is based on a sample rather than the full dataset.  For datasets over 1GB, multiply `rows` (this) by `columns` (features included in experiment version) to calculate total `cells` to ensure it stays under your license limit. Large CSVs have a hard 100M cell limit. |
| `dataSetProfile` | object | No | Full dataset profile from the Profile Service. |
| `experimentVersionId` | string | No | Optional experiment version ID. When included, it indicates that this dataset profile is a snapshot from a previous version. |
| `defaultVersionConfig` | object | No | Default configuration for creating an experiment version from this dataset. Not returned when `experimentVersionId` is provided. |

<details>
<summary>Properties of `insights`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dataSetProfile`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `defaultVersionConfig`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 202

`Accepted`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "profile-insights" |
| `attributes` | object | Yes | Insights (metadata) about an experiment dataset |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of profile insights. Not available until `ready`.  Enum: "pending", "error", "ready" |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `insights` | object[] | No | List of feature insights object, one per feature in the dataset |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `algorithms` | string[] | No | List of algorithms available for the selected experiment type  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `isLargeCsv` | boolean | No | Is this a CSV dataset > 1GB? |
| `sizeInBytes` | integer | No | Size of the profiled dataset in bytes. |
| `numberOfRows` | number | No | Number of rows in the dataset.  When isLargeCsv is true, this is an estimate since their metadata is based on a sample rather than the full dataset.  For datasets over 1GB, multiply `rows` (this) by `columns` (features included in experiment version) to calculate total `cells` to ensure it stays under your license limit. Large CSVs have a hard 100M cell limit. |
| `dataSetProfile` | object | No | Full dataset profile from the Profile Service. |
| `experimentVersionId` | string | No | Optional experiment version ID. When included, it indicates that this dataset profile is a snapshot from a previous version. |
| `defaultVersionConfig` | object | No | Default configuration for creating an experiment version from this dataset. Not returned when `experimentVersionId` is provided. |

<details>
<summary>Properties of `insights`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dataSetProfile`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `defaultVersionConfig`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `POST /api/v1/ml/profile-insights` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/profile-insights',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data: {
        type: 'profile-insights',
        attributes: {
          target: 'string',
          include: 'dataSetProfile',
          dataSetId: '672e55cfcadfb8a18281523e',
          shouldWait: false,
          experimentType: 'binary',
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ml/profile-insights yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/profile-insights" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"data":{"type":"profile-insights","attributes":{"target":"string","include":"dataSetProfile","dataSetId":"672e55cfcadfb8a18281523e","shouldWait":false,"experimentType":"binary"}}}'
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "profile-insights",
    "attributes": {
      "status": "pending",
      "ownerId": "string",
      "insights": [
        {
          "name": "string",
          "insights": [
            "constant"
          ],
          "willBeDropped": true,
          "cannotBeTarget": true,
          "experimentTypes": [
            "binary"
          ],
          "defaultFeatureType": "categorical",
          "engineeredFeatures": "[\n  `${featureName}.YEAR`,\n  `${featureName}.MONTH`\n]\n",
          "estimatedMaxForecastHorizon": 42
        }
      ],
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "algorithms": [
        "catboost_classifier"
      ],
      "isLargeCsv": true,
      "sizeInBytes": 42,
      "numberOfRows": 42,
      "dataSetProfile": {
        "meta": {
          "status": "FINISHED",
          "messages": [
            "string"
          ],
          "dataSetId": "672e55cfcadfb8a18281523e",
          "resultType": "NORMAL",
          "connectionId": "string",
          "lastLoadTime": "string",
          "maxSizeBytes": 42,
          "computationEndTime": "string",
          "computationStartTime": "string"
        },
        "samples": [
          {
            "name": "string",
            "records": [
              {
                "values": [
                  "string"
                ]
              }
            ],
            "fieldNames": [
              "string"
            ]
          }
        ],
        "profiles": [
          {
            "name": "string",
            "sizeInBytes": 42,
            "numberOfRows": 42,
            "fieldProfiles": [
              {
                "name": "string",
                "tags": [
                  "string"
                ],
                "index": 42,
                "median": 42,
                "average": 42,
                "dataType": "string",
                "kurtosis": 42,
                "skewness": 42,
                "fractiles": [
                  42
                ],
                "sampleValues": [
                  "string"
                ],
                "technicalName": "string",
                "classification": {
                  "pii": true,
                  "tags": [
                    {
                      "tag": "string",
                      "score": 42
                    }
                  ],
                  "sensitive": true,
                  "obfuscation": "string"
                },
                "nullValueCount": 42,
                "textValueCount": 42,
                "zeroValueCount": 42,
                "maxNumericValue": 42,
                "maxStringLength": 42,
                "minNumericValue": 42,
                "minStringLength": 42,
                "sumStringLength": 42,
                "emptyStringCount": 42,
                "sumNumericValues": 42,
                "numericValueCount": 42,
                "standardDeviation": 42,
                "distinctValueCount": 42,
                "mostFrequentValues": [
                  {
                    "value": "string",
                    "frequency": 42
                  }
                ],
                "negativeValueCount": 42,
                "positiveValueCount": 42,
                "averageStringLength": 42,
                "frequencyDistribution": [
                  {
                    "binEdge": 42,
                    "frequency": 42
                  }
                ],
                "lastSortedStringValue": "string",
                "firstSortedStringValue": "string",
                "sumSquaredNumericValues": 42
              }
            ]
          }
        ]
      },
      "experimentVersionId": "string",
      "defaultVersionConfig": {
        "name": "Experiment version name. Defaults to current date/time.",
        "dataSetId": "672e55cfcadfb8a18281523e",
        "featuresList": [
          {
            "name": "ColumnA",
            "include": true,
            "dataType": "STRING",
            "changeType": null,
            "featureType": "categorical",
            "parentFeature": null
          }
        ],
        "datasetOrigin": "new",
        "experimentMode": "intelligent"
      }
    }
  }
}
```

---

### GET /api/v1/ml/profile-insights/{dataSetId}

Retrieves profile insights for the specified dataset. If you received a
`202 Accepted` response from `POST /ml/profile-insights`, poll this
endpoint until a `200 OK` response with `ready` status is returned.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSetId` | string | Yes | The Qlik catalog dataset ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `experimentVersionId` | string | No | The optional experimentVersionId query parameter for profile-insights GET requests. When provided after a version has been trained, it gets the profile insights snapshot used in previous versions rather than new results. |
| `target` | string | No | The optional target feature for profile-insights GET requests after this is known. |
| `experimentType` | string | No | The optional experiment type for profile-insights GET requests after this is known.  Enum: "binary", "multiclass", "regression" |

#### Responses

##### 200

`OK`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of this entity |
| `type` | string | Yes | Enum: "profile-insights" |
| `attributes` | object | Yes | Insights (metadata) about an experiment dataset |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of profile insights. Not available until `ready`.  Enum: "pending", "error", "ready" |
| `ownerId` | string | Yes | ID of owner/user for this entity |
| `insights` | object[] | No | List of feature insights object, one per feature in the dataset |
| `tenantId` | string | Yes | Tenant ID for this entity |
| `algorithms` | string[] | No | List of algorithms available for the selected experiment type  Enum: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression" |
| `isLargeCsv` | boolean | No | Is this a CSV dataset > 1GB? |
| `sizeInBytes` | integer | No | Size of the profiled dataset in bytes. |
| `numberOfRows` | number | No | Number of rows in the dataset.  When isLargeCsv is true, this is an estimate since their metadata is based on a sample rather than the full dataset.  For datasets over 1GB, multiply `rows` (this) by `columns` (features included in experiment version) to calculate total `cells` to ensure it stays under your license limit. Large CSVs have a hard 100M cell limit. |
| `dataSetProfile` | object | No | Full dataset profile from the Profile Service. |
| `experimentVersionId` | string | No | Optional experiment version ID. When included, it indicates that this dataset profile is a snapshot from a previous version. |
| `defaultVersionConfig` | object | No | Default configuration for creating an experiment version from this dataset. Not returned when `experimentVersionId` is provided. |

<details>
<summary>Properties of `insights`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dataSetProfile`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `defaultVersionConfig`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

`Bad Request`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 401

`Unauthorized`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 403

`Forbidden`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 404

`Not Found`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 500

`Internal Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 502

`Bad Gateway`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### 503

`Service Unavailable`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
| `details` | string | No | Extra details for what may have caused the error |
| `errorId` | string | No | The unique id of the error instance |
| `argument` | string | No | The argument |
| `resource` | string | No | The resource type that the error occurred on |
| `resourceId` | string | No | The resource id that the error occurred on |

</details>

</details>

##### default

`Unexpected Error`

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | An error object |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Qlik error code (not HTTP response status code) |
| `meta` | object | No | Additional details about the error. These may vary by error. |
| `title` | string | Yes | Short summary of error |
| `detail` | string | No | Description of the error |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `issue` | string | No | The issue code |
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
// qlik-api has not implemented support for `GET /api/v1/ml/profile-insights/{dataSetId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ml/profile-insights/{dataSetId}',
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
# qlik-cli has not implemented support for GET /api/v1/ml/profile-insights/{dataSetId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ml/profile-insights/{dataSetId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "type": "profile-insights",
    "attributes": {
      "status": "pending",
      "ownerId": "string",
      "insights": [
        {
          "name": "string",
          "insights": [
            "constant"
          ],
          "willBeDropped": true,
          "cannotBeTarget": true,
          "experimentTypes": [
            "binary"
          ],
          "defaultFeatureType": "categorical",
          "engineeredFeatures": "[\n  `${featureName}.YEAR`,\n  `${featureName}.MONTH`\n]\n",
          "estimatedMaxForecastHorizon": 42
        }
      ],
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "algorithms": [
        "catboost_classifier"
      ],
      "isLargeCsv": true,
      "sizeInBytes": 42,
      "numberOfRows": 42,
      "dataSetProfile": {
        "meta": {
          "status": "FINISHED",
          "messages": [
            "string"
          ],
          "dataSetId": "672e55cfcadfb8a18281523e",
          "resultType": "NORMAL",
          "connectionId": "string",
          "lastLoadTime": "string",
          "maxSizeBytes": 42,
          "computationEndTime": "string",
          "computationStartTime": "string"
        },
        "samples": [
          {
            "name": "string",
            "records": [
              {
                "values": [
                  "string"
                ]
              }
            ],
            "fieldNames": [
              "string"
            ]
          }
        ],
        "profiles": [
          {
            "name": "string",
            "sizeInBytes": 42,
            "numberOfRows": 42,
            "fieldProfiles": [
              {
                "name": "string",
                "tags": [
                  "string"
                ],
                "index": 42,
                "median": 42,
                "average": 42,
                "dataType": "string",
                "kurtosis": 42,
                "skewness": 42,
                "fractiles": [
                  42
                ],
                "sampleValues": [
                  "string"
                ],
                "technicalName": "string",
                "classification": {
                  "pii": true,
                  "tags": [
                    {
                      "tag": "string",
                      "score": 42
                    }
                  ],
                  "sensitive": true,
                  "obfuscation": "string"
                },
                "nullValueCount": 42,
                "textValueCount": 42,
                "zeroValueCount": 42,
                "maxNumericValue": 42,
                "maxStringLength": 42,
                "minNumericValue": 42,
                "minStringLength": 42,
                "sumStringLength": 42,
                "emptyStringCount": 42,
                "sumNumericValues": 42,
                "numericValueCount": 42,
                "standardDeviation": 42,
                "distinctValueCount": 42,
                "mostFrequentValues": [
                  {
                    "value": "string",
                    "frequency": 42
                  }
                ],
                "negativeValueCount": 42,
                "positiveValueCount": 42,
                "averageStringLength": 42,
                "frequencyDistribution": [
                  {
                    "binEdge": 42,
                    "frequency": 42
                  }
                ],
                "lastSortedStringValue": "string",
                "firstSortedStringValue": "string",
                "sumSquaredNumericValues": 42
              }
            ]
          }
        ]
      },
      "experimentVersionId": "string",
      "defaultVersionConfig": {
        "name": "Experiment version name. Defaults to current date/time.",
        "dataSetId": "672e55cfcadfb8a18281523e",
        "featuresList": [
          {
            "name": "ColumnA",
            "include": true,
            "dataType": "STRING",
            "changeType": null,
            "featureType": "categorical",
            "parentFeature": null
          }
        ],
        "datasetOrigin": "new",
        "experimentMode": "intelligent"
      }
    }
  }
}
```

---
