# Conditions

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Conditions are used by features such as data alerting and subscriptions to determine when action should be taken, based on data in a Qlik app.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/conditions`](#post-apiv1conditions) |  |
| `GET` | [`/api/v1/conditions/{id}`](#get-apiv1conditionsid) |  |
| `PATCH` | [`/api/v1/conditions/{id}`](#patch-apiv1conditionsid) |  |
| `DELETE` | [`/api/v1/conditions/{id}`](#delete-apiv1conditionsid) |  |
| `POST` | [`/api/v1/conditions/{id}/evaluations`](#post-apiv1conditionsidevaluations) |  |
| `GET` | [`/api/v1/conditions/{id}/evaluations/{evaluationId}`](#get-apiv1conditionsidevaluationsevaluationid) |  |
| `DELETE` | [`/api/v1/conditions/{id}/evaluations/{evaluationId}`](#delete-apiv1conditionsidevaluationsevaluationid) |  |
| `POST` | [`/api/v1/conditions/previews`](#post-apiv1conditionspreviews) | Create condition preview request. |
| `GET` | [`/api/v1/conditions/previews/{id}`](#get-apiv1conditionspreviewsid) | Get condition preview response. |
| `GET` | [`/api/v1/conditions/settings`](#get-apiv1conditionssettings) | Lists api settings. |
| `PUT` | [`/api/v1/conditions/settings`](#put-apiv1conditionssettings) | Updates API configuration. Accessible only by tenant admins. |

## API Reference

### POST /api/v1/conditions

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

The condition create request definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | No | Is history enabled |

</details>

<details>
<summary>Properties of `measures`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | string | No | Measure title |
| `qLibraryId` | string | No | Refers to a measure stored in the library |
| `qNumFormat` | object | No | Format of the field |

</details>

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `field` | string | No | Field referred to the dimension where the selection is made. This may be used to generate deep links. |
| `title` | string | No | Dimension title |
| `qLibraryId` | string | No | Refers to a dimension stored in the library |

</details>

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | number | No | The count |
| `field` | string | No | Field name |
| `selectedSummary` | string[] | No | Array of selected |

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `description` | string | No | Description of the condition |

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `history` | object | No | History properties |
| `conditions` | string[] | No | Array of condition ids |
| `expression` | string | No | Boolean expression made up of variable names defined from the conditions section |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `description` | string | No | Description of the condition |

</details>

</details>

#### Responses

##### 201

Condition created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `condition` | object | No | only one of compoundCondition or dataCondition should be set |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `condition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `ownerId` | string | No | UserID of the condition owner |
| `tenantId` | string | No | The tenant id |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `measures`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dimensions`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selections`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/conditions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'compound',
      dataCondition: {
        headers: ['sumnum'],
        history: { enabled: true },
        measures: [
          {
            title: 'sumnum',
            qLibraryId: 'PgQKNQ',
            qNumFormat: {
              qDec: '.',
              qFmt: '###0',
              qType: 'I',
              qnDec: 0,
              qUseThou: 1,
            },
          },
        ],
        dimensions: [
          {
            field: 'Neighborhood',
            title: 'Neighborhood',
            qLibraryId: 'PgQKNQ',
          },
        ],
        selections: [
          {
            count: 2,
            field: 'SalesTerritoryCountry',
            selectedSummary:
              '[ Germany, Australia ]',
          },
        ],
        conditionBase: {
          type: 'compound',
          appId:
            '4xQ1chLoHkOikyzUGcHJquteNrAfketW',
          bookmarkId:
            'anTjnOABmxlCirVx8IRfhWhLd9IZjENl',
          description: 'My condition',
        },
        conditionData: {},
      },
      compoundCondition: {
        data: {
          history: { enabled: true },
          conditions: [
            'rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2',
            'qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi',
            '4gnz8E6ZruG0lkSKwkau66P24CtORyLr',
            'ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ',
          ],
          expression: '($0 OR $1) AND ($2 OR $3)',
        },
        conditionBase: {
          type: 'compound',
          appId:
            '4xQ1chLoHkOikyzUGcHJquteNrAfketW',
          bookmarkId:
            'anTjnOABmxlCirVx8IRfhWhLd9IZjENl',
          description: 'My condition',
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/conditions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"compound","dataCondition":{"headers":["sumnum"],"history":{"enabled":true},"measures":[{"title":"sumnum","qLibraryId":"PgQKNQ","qNumFormat":{"qDec":".","qFmt":"###0","qType":"I","qnDec":0,"qUseThou":1}}],"dimensions":[{"field":"Neighborhood","title":"Neighborhood","qLibraryId":"PgQKNQ"}],"selections":[{"count":2,"field":"SalesTerritoryCountry","selectedSummary":"[ Germany, Australia ]"}],"conditionBase":{"type":"compound","appId":"4xQ1chLoHkOikyzUGcHJquteNrAfketW","bookmarkId":"anTjnOABmxlCirVx8IRfhWhLd9IZjENl","description":"My condition"},"conditionData":{}},"compoundCondition":{"data":{"history":{"enabled":true},"conditions":["rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2","qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi","4gnz8E6ZruG0lkSKwkau66P24CtORyLr","ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"],"expression":"($0 OR $1) AND ($2 OR $3)"},"conditionBase":{"type":"compound","appId":"4xQ1chLoHkOikyzUGcHJquteNrAfketW","bookmarkId":"anTjnOABmxlCirVx8IRfhWhLd9IZjENl","description":"My condition"}}}'
```

**Example Response:**

```json
{
  "errors": [
    {
      "code": "string",
      "meta": {},
      "title": "string",
      "detail": "string"
    }
  ],
  "condition": {
    "type": "compound",
    "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
    "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
    "dataCondition": {
      "headers": [
        "sumnum"
      ],
      "history": {
        "enabled": true
      },
      "measures": [
        {
          "title": "sumnum",
          "qLibraryId": "PgQKNQ",
          "qNumFormat": {
            "qDec": ".",
            "qFmt": "###0",
            "qType": "I",
            "qnDec": 0,
            "qUseThou": 1
          }
        }
      ],
      "dimensions": [
        {
          "field": "Neighborhood",
          "title": "Neighborhood",
          "qLibraryId": "PgQKNQ"
        }
      ],
      "selections": [
        {
          "count": 2,
          "field": "SalesTerritoryCountry",
          "selectedSummary": "[ Germany, Australia ]"
        }
      ],
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      },
      "conditionData": {}
    },
    "compoundCondition": {
      "data": {
        "history": {
          "enabled": true
        },
        "conditions": [
          "rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2",
          "qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi",
          "4gnz8E6ZruG0lkSKwkau66P24CtORyLr",
          "ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"
        ],
        "expression": "($0 OR $1) AND ($2 OR $3)"
      },
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      }
    }
  }
}
```

---

### GET /api/v1/conditions/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the condition |

#### Responses

##### 200

The condition

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `ownerId` | string | No | UserID of the condition owner |
| `tenantId` | string | No | The tenant id |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | No | Is history enabled |

</details>

<details>
<summary>Properties of `measures`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | string | No | Measure title |
| `qLibraryId` | string | No | Refers to a measure stored in the library |
| `qNumFormat` | object | No | Format of the field |

</details>

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `field` | string | No | Field referred to the dimension where the selection is made. This may be used to generate deep links. |
| `title` | string | No | Dimension title |
| `qLibraryId` | string | No | Refers to a dimension stored in the library |

</details>

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | number | No | The count |
| `field` | string | No | Field name |
| `selectedSummary` | string[] | No | Array of selected |

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `created` | string | No | When the resource was created |
| `ownerId` | string | No | The id of the user the user which owns the condition |
| `updated` | string | No | When the resource was last updated |
| `tenantId` | string | No | The tenant id |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `createdById` | string | No | The id of the user which created the condition |
| `description` | string | No | Description of the condition |
| `lastReloadTime` | string | No | The time of the last reload, if the scan is triggered by a reload. If exists and value does not match app's last reload time, the evaluation will fail. |

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `history` | object | No | History properties |
| `conditions` | string[] | No | Array of condition ids |
| `expression` | string | No | Boolean expression made up of variable names defined from the conditions section |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `created` | string | No | When the resource was created |
| `ownerId` | string | No | The id of the user the user which owns the condition |
| `updated` | string | No | When the resource was last updated |
| `tenantId` | string | No | The tenant id |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `createdById` | string | No | The id of the user which created the condition |
| `description` | string | No | Description of the condition |
| `lastReloadTime` | string | No | The time of the last reload, if the scan is triggered by a reload. If exists and value does not match app's last reload time, the evaluation will fail. |

</details>

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/conditions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/conditions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "type": "compound",
  "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
  "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
  "dataCondition": {
    "headers": [
      "sumnum"
    ],
    "history": {
      "enabled": true
    },
    "measures": [
      {
        "title": "sumnum",
        "qLibraryId": "PgQKNQ",
        "qNumFormat": {
          "qDec": ".",
          "qFmt": "###0",
          "qType": "I",
          "qnDec": 0,
          "qUseThou": 1
        }
      }
    ],
    "dimensions": [
      {
        "field": "Neighborhood",
        "title": "Neighborhood",
        "qLibraryId": "PgQKNQ"
      }
    ],
    "selections": [
      {
        "count": 2,
        "field": "SalesTerritoryCountry",
        "selectedSummary": "[ Germany, Australia ]"
      }
    ],
    "conditionBase": {
      "id": "5f31c6e8476ae50001030fb6",
      "type": "compound",
      "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
      "created": "2006-01-02T15:04:05Z07:00",
      "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
      "updated": "2006-01-02T14:04:05Z07:00",
      "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
      "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
      "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
      "description": "My condition",
      "lastReloadTime": "2006-01-02T15:04:05Z07:00"
    },
    "conditionData": {}
  },
  "compoundCondition": {
    "data": {
      "history": {
        "enabled": true
      },
      "conditions": [
        "rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2",
        "qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi",
        "4gnz8E6ZruG0lkSKwkau66P24CtORyLr",
        "ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"
      ],
      "expression": "($0 OR $1) AND ($2 OR $3)"
    },
    "conditionBase": {
      "id": "5f31c6e8476ae50001030fb6",
      "type": "compound",
      "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
      "created": "2006-01-02T15:04:05Z07:00",
      "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
      "updated": "2006-01-02T14:04:05Z07:00",
      "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
      "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
      "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
      "description": "My condition",
      "lastReloadTime": "2006-01-02T15:04:05Z07:00"
    }
  }
}
```

---

### PATCH /api/v1/conditions/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the condition |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace", "remove", "add" |
| `path` | string | Yes | The path for the given resource field to patch. |
| `value` | object | No | The value to be used for this operation. |

#### Responses

##### 204

The condition was updated

##### 400

A path or value was invalid

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/conditions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/compoundCondition/conditionBase/ownerId',
        value: 'I6mWVd60wRWIbOXZr1ZKV8QTnxhnitbX',
      },
      {
        op: 'replace',
        path: '/dataCondition/conditionBase/description',
        value: 'My description',
      },
      {
        op: 'remove',
        path: '/compoundCondition/data/conditions/0',
      },
      {
        op: 'replace',
        path: '/compoundCondition//data/expression',
        value: '$0 AND $1',
      },
      {
        op: 'replace',
        path: '/dataCondition/conditionData/measure',
        value: 'revenue',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/conditions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/compoundCondition/conditionBase/ownerId","value":"I6mWVd60wRWIbOXZr1ZKV8QTnxhnitbX"},{"op":"replace","path":"/dataCondition/conditionBase/description","value":"My description"},{"op":"remove","path":"/compoundCondition/data/conditions/0"},{"op":"replace","path":"/compoundCondition//data/expression","value":"$0 AND $1"},{"op":"replace","path":"/dataCondition/conditionData/measure","value":"revenue"}]'
```

---

### DELETE /api/v1/conditions/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the condition |

#### Responses

##### 204

The record was deleted.

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/conditions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/conditions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/conditions/{id}/evaluations

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the condition |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | No | The id of the alerting task the condition and evaluation is part of |
| `contextId` | string | Yes | Extra context information to carry through to the result if any |
| `causalEvent` | object | Yes |  |

<details>
<summary>Properties of `causalEvent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No |  |
| `eventID` | string | No | the event id from eventing |
| `extensions` | object | No |  |
| `manualTrigger` | boolean | No |  |
| `manualTriggerID` | string | No | the manual trigger id from eventing if present |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventID` | string | No | the event id from eventing service. |
| `lastReloadTime` | string | No | The time of the last reload |

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userID` | string | No |  |
| `tenantID` | string | No |  |
| `sessionID` | string | No |  |

</details>

</details>

#### Responses

##### 201

Condition evaluation created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `contextId` | string | No | Extra context information to carry through to the result if any |
| `evaluationId` | string | No | Extra context information to carry through to the result if any |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/conditions/{id}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}/evaluations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      alertId: '5f64885b2e11d23982c09e03',
      contextId:
        '795c75ba-7812-4c8f-9ced-551b6b006183',
      causalEvent: {
        data: {
          eventID: 'string',
          lastReloadTime:
            '2006-01-02T15:04:05Z07:00',
        },
        eventID: 'string',
        extensions: {
          userID: 'string',
          tenantID: 'string',
          sessionID: 'string',
        },
        manualTrigger: true,
        manualTriggerID: 'string',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/conditions/{id}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}/evaluations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"alertId":"5f64885b2e11d23982c09e03","contextId":"795c75ba-7812-4c8f-9ced-551b6b006183","causalEvent":{"data":{"eventID":"string","lastReloadTime":"2006-01-02T15:04:05Z07:00"},"eventID":"string","extensions":{"userID":"string","tenantID":"string","sessionID":"string"},"manualTrigger":true,"manualTriggerID":"string"}}'
```

**Example Response:**

```json
{
  "errors": [
    {
      "code": "string",
      "meta": {},
      "title": "string",
      "detail": "string"
    }
  ],
  "contextId": "795c75ba-7812-4c8f-9ced-551b6b006183",
  "evaluationId": "795c75ba-7812-4c8f-9ced-551b6b006183"
}
```

---

### GET /api/v1/conditions/{id}/evaluations/{evaluationId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `evaluationId` | string | Yes | The id of the evaluation |
| `id` | string | Yes | The id of the condition |

#### Responses

##### 200

The evaluation

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `condition` | object | No | only one of compoundCondition or dataCondition should be set |
| `evaluation` | object | No |  |

<details>
<summary>Properties of `condition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `ownerId` | string | No | UserID of the condition owner |
| `tenantId` | string | No | The tenant id |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `measures`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dimensions`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selections`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `evaluation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `errors` | object[] | No |  |
| `result` | boolean | No | The final result of the evalution |
| `status` | string | No | The status of the evaluation execution Enum: "RUNNING", "FAILED", "FINISHED", "DELETING" |
| `alertId` | string | No | The id of the alerting task the condition and evaluation is part of |
| `endTime` | string | No | The time the evaluation ended |
| `ownerId` | string | No | userId of user being impersonated to evaluate the condition |
| `retries` | integer | No | number of retries sent to DCE |
| `tenantId` | string | No | The tenant id |
| `condition` | object | No | only one of compoundCondition or dataCondition should be set |
| `contextId` | string | No | Extra context information to carry through to the result if one was included on when the evaluation was triggered |
| `startTime` | string | No | The time the evaluation started |
| `resultData` | object | No | Condition type specific result, one of dataResult or compoundResult |
| `causalEvent` | object | No | Representation of the event that caused the condition to be evaluated if one was included on when the evaluation was triggered |
| `conditionId` | string | No | The unique id of the associated condition |
| `retryPolicy` | string | No | what kind of retry policy this evaluation has Enum: "NONE", "TOO_MANY_REQUESTS", "GENERIC_ERROR" |
| `reloadEndTime` | string | No | The time when the reload was completed in Engine |
| `byokMigrationId` | string | No | internal identifier used when migrating keys |
| `removalErrorCount` | integer | No | The number of times we have attempted to remove this evaluation data-file |
| `dataConditionEvaluatorId` | string | No | _(deprecated)_ The unique id for the resource given from Data Condition Evaluator. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition smanager. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `status` | any | No | Error status. |

<details>
<summary>Properties of `meta`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `condition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `ownerId` | string | No | UserID of the condition owner |
| `tenantId` | string | No | The tenant id |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/conditions/{id}/evaluations/{evaluationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}/evaluations/{evaluationId}',
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
# qlik-cli has not implemented support for GET /api/v1/conditions/{id}/evaluations/{evaluationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}/evaluations/{evaluationId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "condition": {
    "type": "compound",
    "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
    "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
    "dataCondition": {
      "headers": [
        "sumnum"
      ],
      "history": {
        "enabled": true
      },
      "measures": [
        {
          "title": "sumnum",
          "qLibraryId": "PgQKNQ",
          "qNumFormat": {
            "qDec": ".",
            "qFmt": "###0",
            "qType": "I",
            "qnDec": 0,
            "qUseThou": 1
          }
        }
      ],
      "dimensions": [
        {
          "field": "Neighborhood",
          "title": "Neighborhood",
          "qLibraryId": "PgQKNQ"
        }
      ],
      "selections": [
        {
          "count": 2,
          "field": "SalesTerritoryCountry",
          "selectedSummary": "[ Germany, Australia ]"
        }
      ],
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      },
      "conditionData": {}
    },
    "compoundCondition": {
      "data": {
        "history": {
          "enabled": true
        },
        "conditions": [
          "rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2",
          "qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi",
          "4gnz8E6ZruG0lkSKwkau66P24CtORyLr",
          "ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"
        ],
        "expression": "($0 OR $1) AND ($2 OR $3)"
      },
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      }
    }
  },
  "evaluation": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "errors": [
      {
        "code": "string",
        "meta": {
          "fatal": true
        },
        "title": "string"
      }
    ],
    "result": true,
    "status": "RUNNING",
    "alertId": "5f64885b2e11d23982c09e03",
    "endTime": "string",
    "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "retries": 42,
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "condition": {
      "type": "compound",
      "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
      "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
      "dataCondition": {
        "headers": [
          "sumnum"
        ],
        "history": {
          "enabled": true
        },
        "measures": [
          {
            "title": "sumnum",
            "qLibraryId": "PgQKNQ",
            "qNumFormat": {
              "qDec": ".",
              "qFmt": "###0",
              "qType": "I",
              "qnDec": 0,
              "qUseThou": 1
            }
          }
        ],
        "dimensions": [
          {
            "field": "Neighborhood",
            "title": "Neighborhood",
            "qLibraryId": "PgQKNQ"
          }
        ],
        "selections": [
          {
            "count": 2,
            "field": "SalesTerritoryCountry",
            "selectedSummary": "[ Germany, Australia ]"
          }
        ],
        "conditionBase": {
          "id": "5f31c6e8476ae50001030fb6",
          "type": "compound",
          "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
          "created": "2006-01-02T15:04:05Z07:00",
          "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
          "updated": "2006-01-02T14:04:05Z07:00",
          "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
          "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
          "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
          "description": "My condition",
          "lastReloadTime": "2006-01-02T15:04:05Z07:00"
        },
        "conditionData": {}
      },
      "compoundCondition": {
        "data": {
          "history": {
            "enabled": true
          },
          "conditions": [
            "rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2",
            "qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi",
            "4gnz8E6ZruG0lkSKwkau66P24CtORyLr",
            "ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"
          ],
          "expression": "($0 OR $1) AND ($2 OR $3)"
        },
        "conditionBase": {
          "id": "5f31c6e8476ae50001030fb6",
          "type": "compound",
          "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
          "created": "2006-01-02T15:04:05Z07:00",
          "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
          "updated": "2006-01-02T14:04:05Z07:00",
          "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
          "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
          "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
          "description": "My condition",
          "lastReloadTime": "2006-01-02T15:04:05Z07:00"
        }
      }
    },
    "contextId": "string",
    "startTime": "string",
    "resultData": {},
    "causalEvent": {},
    "conditionId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "retryPolicy": "NONE",
    "reloadEndTime": "string",
    "byokMigrationId": "string",
    "removalErrorCount": 3,
    "dataConditionEvaluatorId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
  }
}
```

---

### DELETE /api/v1/conditions/{id}/evaluations/{evaluationId}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `evaluationId` | string | Yes | The id of the evaluation |
| `id` | string | Yes | The id of the condition |

#### Responses

##### 204

The evaluation was deleted

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/conditions/{id}/evaluations/{evaluationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/{id}/evaluations/{evaluationId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/conditions/{id}/evaluations/{evaluationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/{id}/evaluations/{evaluationId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/conditions/previews

Create condition preview request.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

Create condition preview request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | No | Is history enabled |

</details>

<details>
<summary>Properties of `measures`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | string | No | Measure title |
| `qLibraryId` | string | No | Refers to a measure stored in the library |
| `qNumFormat` | object | No | Format of the field |

</details>

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `field` | string | No | Field referred to the dimension where the selection is made. This may be used to generate deep links. |
| `title` | string | No | Dimension title |
| `qLibraryId` | string | No | Refers to a dimension stored in the library |

</details>

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | number | No | The count |
| `field` | string | No | Field name |
| `selectedSummary` | string[] | No | Array of selected |

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `description` | string | No | Description of the condition |

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `history` | object | No | History properties |
| `conditions` | string[] | No | Array of condition ids |
| `expression` | string | No | Boolean expression made up of variable names defined from the conditions section |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `conditionBase`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Indicates the condition type Enum: "compound", "data" |
| `appId` | string | No | The id of the app the condition is evaluated against |
| `bookmarkId` | string | No | The bookmark corresponding to the selection state to apply to the app at evaluation time |
| `description` | string | No | Description of the condition |

</details>

</details>

#### Responses

##### 201

Condition preview request created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `previewId` | string | No | When the resource was created |

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/conditions/previews` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/previews',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'compound',
      dataCondition: {
        headers: ['sumnum'],
        history: { enabled: true },
        measures: [
          {
            title: 'sumnum',
            qLibraryId: 'PgQKNQ',
            qNumFormat: {
              qDec: '.',
              qFmt: '###0',
              qType: 'I',
              qnDec: 0,
              qUseThou: 1,
            },
          },
        ],
        dimensions: [
          {
            field: 'Neighborhood',
            title: 'Neighborhood',
            qLibraryId: 'PgQKNQ',
          },
        ],
        selections: [
          {
            count: 2,
            field: 'SalesTerritoryCountry',
            selectedSummary:
              '[ Germany, Australia ]',
          },
        ],
        conditionBase: {
          type: 'compound',
          appId:
            '4xQ1chLoHkOikyzUGcHJquteNrAfketW',
          bookmarkId:
            'anTjnOABmxlCirVx8IRfhWhLd9IZjENl',
          description: 'My condition',
        },
        conditionData: {},
      },
      compoundCondition: {
        data: {
          history: { enabled: true },
          conditions: [
            'rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2',
            'qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi',
            '4gnz8E6ZruG0lkSKwkau66P24CtORyLr',
            'ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ',
          ],
          expression: '($0 OR $1) AND ($2 OR $3)',
        },
        conditionBase: {
          type: 'compound',
          appId:
            '4xQ1chLoHkOikyzUGcHJquteNrAfketW',
          bookmarkId:
            'anTjnOABmxlCirVx8IRfhWhLd9IZjENl',
          description: 'My condition',
        },
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/conditions/previews yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/previews" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"compound","dataCondition":{"headers":["sumnum"],"history":{"enabled":true},"measures":[{"title":"sumnum","qLibraryId":"PgQKNQ","qNumFormat":{"qDec":".","qFmt":"###0","qType":"I","qnDec":0,"qUseThou":1}}],"dimensions":[{"field":"Neighborhood","title":"Neighborhood","qLibraryId":"PgQKNQ"}],"selections":[{"count":2,"field":"SalesTerritoryCountry","selectedSummary":"[ Germany, Australia ]"}],"conditionBase":{"type":"compound","appId":"4xQ1chLoHkOikyzUGcHJquteNrAfketW","bookmarkId":"anTjnOABmxlCirVx8IRfhWhLd9IZjENl","description":"My condition"},"conditionData":{}},"compoundCondition":{"data":{"history":{"enabled":true},"conditions":["rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2","qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi","4gnz8E6ZruG0lkSKwkau66P24CtORyLr","ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"],"expression":"($0 OR $1) AND ($2 OR $3)"},"conditionBase":{"type":"compound","appId":"4xQ1chLoHkOikyzUGcHJquteNrAfketW","bookmarkId":"anTjnOABmxlCirVx8IRfhWhLd9IZjENl","description":"My condition"}}}'
```

**Example Response:**

```json
{
  "previewId": "467ea9bc-bbd7-11ea-b3de-0242ac130004"
}
```

---

### GET /api/v1/conditions/previews/{id}

Get condition preview response.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the condition |

#### Responses

##### 200

The evaluation

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `status` | string | No | Enum: "ACCEPTED", "FAILED", "RUNNING", "SUCCESSFUL" |
| `condition` | object | No | only one of compoundCondition or dataCondition should be set |
| `previewId` | string | No | When the resource was created |
| `evaluation` | object | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `condition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicates the condition type Enum: "compound", "data" |
| `ownerId` | string | No | UserID of the condition owner |
| `tenantId` | string | No | The tenant id |
| `dataCondition` | object | No | A condition based on data within an app |
| `compoundCondition` | object | No | A condition made up of other conditions |

<details>
<summary>Properties of `dataCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | string[] | No | List of header labels |
| `history` | object | No | History properties |
| `measures` | object[] | No | List of returned measures |
| `dimensions` | object[] | No | List of returned dimensions |
| `selections` | object[] | No | List of fields according to the bookmark definition |
| `conditionBase` | object | No | A base condition |
| `conditionData` | object | No | List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator |

<details>
<summary>Properties of `history`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `measures`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dimensions`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selections`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `compoundCondition`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | Condition data |
| `conditionBase` | object | No | A base condition |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `conditionBase`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `evaluation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | string | No | The time the evaluation ended |
| `ownerId` | string | No | userId of user being impersonated to evaluate the condition |
| `tenantId` | string | No | The tenant id |
| `resultUrl` | string | No | URL to download the condition results |
| `startTime` | string | No | The time the evaluation started |

</details>

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/conditions/previews/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/previews/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/conditions/previews/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/previews/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "errors": [
    {
      "code": "string",
      "meta": {},
      "title": "string",
      "detail": "string"
    }
  ],
  "status": "ACCEPTED",
  "condition": {
    "type": "compound",
    "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
    "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
    "dataCondition": {
      "headers": [
        "sumnum"
      ],
      "history": {
        "enabled": true
      },
      "measures": [
        {
          "title": "sumnum",
          "qLibraryId": "PgQKNQ",
          "qNumFormat": {
            "qDec": ".",
            "qFmt": "###0",
            "qType": "I",
            "qnDec": 0,
            "qUseThou": 1
          }
        }
      ],
      "dimensions": [
        {
          "field": "Neighborhood",
          "title": "Neighborhood",
          "qLibraryId": "PgQKNQ"
        }
      ],
      "selections": [
        {
          "count": 2,
          "field": "SalesTerritoryCountry",
          "selectedSummary": "[ Germany, Australia ]"
        }
      ],
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      },
      "conditionData": {}
    },
    "compoundCondition": {
      "data": {
        "history": {
          "enabled": true
        },
        "conditions": [
          "rDDAcMEI1V0qzauEWepEVY8oSLJ9fvA2",
          "qFPF1dAtPK4vfPTmKyyuKaqA6iERCwLi",
          "4gnz8E6ZruG0lkSKwkau66P24CtORyLr",
          "ATs--Z0b_NGyuHajcbQkxu7RrajgPaEQ"
        ],
        "expression": "($0 OR $1) AND ($2 OR $3)"
      },
      "conditionBase": {
        "id": "5f31c6e8476ae50001030fb6",
        "type": "compound",
        "appId": "4xQ1chLoHkOikyzUGcHJquteNrAfketW",
        "created": "2006-01-02T15:04:05Z07:00",
        "ownerId": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "updated": "2006-01-02T14:04:05Z07:00",
        "tenantId": "5GI7yWoJk9lvNtuEc66SXCypXVfhbVeH",
        "bookmarkId": "anTjnOABmxlCirVx8IRfhWhLd9IZjENl",
        "createdById": "EIwSIgqjmbHGwQJI0ShQoS3ORdz5nCpA",
        "description": "My condition",
        "lastReloadTime": "2006-01-02T15:04:05Z07:00"
      }
    }
  },
  "previewId": "467ea9bc-bbd7-11ea-b3de-0242ac130004",
  "evaluation": {
    "endTime": "string",
    "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "resultUrl": "string",
    "startTime": "string"
  }
}
```

---

### GET /api/v1/conditions/settings

Lists api settings.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The api settings have been successfully returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | No | These persisted api settings are only available for this tenant. Extracted from request JWT. |
| `enable-conditions` | boolean | Yes | Whether API endpoints for condition manager are enabled |

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/conditions/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/settings',
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
# qlik-cli has not implemented support for GET /api/v1/conditions/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "tenantId": "cgdsAumGmQ6l0Bi7CUKt9V8P_Y9GL0sC",
  "enable-conditions": true
}
```

---

### PUT /api/v1/conditions/settings

Updates API configuration. Accessible only by tenant admins.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | No | The JWT used for authentication. Send the JWT in the AuthRequest header using the Bearer schema. |

#### Request Body

Request for updating the api settings

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enable-conditions` | boolean | Yes | Whether API endpoints for condition manager are enabled |

#### Responses

##### 204

api settings have been successfully updated.

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Array of errors |
| `traceId` | string | No | trace id |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to condition manager. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/conditions/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/conditions/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'enable-conditions': true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/conditions/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/conditions/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"enable-conditions":true}'
```

---
