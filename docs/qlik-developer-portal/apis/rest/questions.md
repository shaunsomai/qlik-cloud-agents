# Natural language

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Ask natural languages questions and context aware partial questions against applications enabled for conversational analytics or a specific app to receive Insight Advisor generated responses and suggestions

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/questions/actions/ask`](#post-apiv1questionsactionsask) |  |
| `POST` | [`/api/v1/questions/actions/filter`](#post-apiv1questionsactionsfilter) |  |

## API Reference

### POST /api/v1/questions/actions/ask

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-web-integration-id` | string | No | This header is only required for external clients or mashups for QCS, this value of this property should be the id of the web integration set up for the external client/mashup |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `app` | object | No |  |
| `lang` | string | No | The language to assume when parsing, specified as an ISO-639-1 code. Defaults to 'en' (English). |
| `text` | string | Yes | The sentence that will be parsed. |
| `disableFollowups` | boolean | No | The flag specifies whether to disable follow-up recommendations. |
| `disableNarrative` | boolean | No | Flag that specifies whether the narratives should be generated for the user query or not. |
| `recommendationId` | string | No | property that contains the Id of the recommendation for which the response should be generated. |
| `clearEntityContext` | boolean | No | Flag that clears the entity context. |
| `visualizationTypes` | string[] | No | Specify visualizationTypes for only which visualization object should be provided if enableVisualizations is set to true. For eg. ['linechart', 'barchart'] |
| `enableVisualizations` | boolean | No | Flag that specifies whether visualization object should be provided or not. |
| `disableConversationContext` | boolean | No | Flag that specifies either to enable converastion context. |

<details>
<summary>Properties of `app`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |

</details>

#### Responses

##### 200

The sentence is not created as an app was not specified, but matching apps are suggested

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apps` | object[] | No |  |
| `errors` | object[] | No | An error object. |
| `nluInfo` | object | No |  |
| `conversationalResponse` | object | No |  |

<details>
<summary>Properties of `apps`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |

</details>

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

<details>
<summary>Properties of `nluInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `elements` | object[] | No |  |

<details>
<summary>Properties of `elements`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No |  |
| `type` | string | No |  |
| `entity` | boolean | No |  |
| `isFilter` | boolean | No |  |
| `typeName` | string | No |  |
| `errorText` | string | No |  |
| `filterText` | string | No |  |
| `typeTranslated` | string | No |  |
| `filterFieldName` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `conversationalResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apps` | object[] | No |  |
| `responses` | object[] | No |  |
| `contextInfo` | string | No | For contextual responses, this string contains a list of entities that are used to produce the response. |
| `drillDownURI` | string | No | The URL with the query injected to insight advisor of the app to which the query belongs. |
| `sentenceWithMatches` | string | No |  |

<details>
<summary>Properties of `apps`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |

</details>

<details>
<summary>Properties of `responses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `imageUrl` | string | No |  |
| `infoType` | string | No |  |
| `sentence` | object | No |  |
| `narrative` | object | No |  |
| `infoValues` | array[] | No |  |
| `errorMessage` | string | No |  |
| `followupSentence` | string | No |  |
| `renderVisualization` | object | No |  |

<details>
<summary>Properties of `sentence`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `narrative`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `infoValues`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `renderVisualization`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 201

The sentence created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apps` | object[] | No |  |
| `nluInfo` | object | No |  |
| `conversationalResponse` | object[] | No | A list of conversational responses. |

<details>
<summary>Properties of `apps`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |

</details>

<details>
<summary>Properties of `nluInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `elements` | object[] | No |  |

<details>
<summary>Properties of `elements`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No |  |
| `type` | string | No |  |
| `entity` | boolean | No |  |
| `isFilter` | boolean | No |  |
| `typeName` | string | No |  |
| `errorText` | string | No |  |
| `filterText` | string | No |  |
| `typeTranslated` | string | No |  |
| `filterFieldName` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `conversationalResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apps` | object[] | No |  |
| `responses` | object[] | No |  |
| `contextInfo` | string | No | For contextual responses, this string contains a list of entities that are used to produce the response. |
| `drillDownURI` | string | No | The URL with the query injected to insight advisor of the app to which the query belongs. |
| `sentenceWithMatches` | string | No |  |

<details>
<summary>Properties of `apps`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |

</details>

<details>
<summary>Properties of `responses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `imageUrl` | string | No |  |
| `infoType` | string | No |  |
| `sentence` | object | No |  |
| `narrative` | object | No |  |
| `infoValues` | array[] | No |  |
| `errorMessage` | string | No |  |
| `followupSentence` | string | No |  |
| `renderVisualization` | object | No |  |

<details>
<summary>Properties of `sentence`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `narrative`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `infoValues`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `renderVisualization`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad request. The payload is not formed correctly.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

User is not authorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 422

Unprocessable entity. The payload contains fields
that are invalid, such as too long of a query.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/questions/actions/ask` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/questions/actions/ask',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      app: { id: 'string', name: 'string' },
      lang: 'string',
      text: 'string',
      disableFollowups: false,
      disableNarrative: false,
      recommendationId: 'string',
      clearEntityContext: false,
      visualizationTypes: ['string'],
      enableVisualizations: false,
      disableConversationContext: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/questions/actions/ask yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/questions/actions/ask" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"app":{"id":"string","name":"string"},"lang":"string","text":"string","disableFollowups":false,"disableNarrative":false,"recommendationId":"string","clearEntityContext":false,"visualizationTypes":["string"],"enableVisualizations":false,"disableConversationContext":false}'
```

**Example Response:**

```json
{
  "apps": [
    {
      "id": "string",
      "name": "string"
    }
  ],
  "errors": [
    {
      "code": "string",
      "meta": {},
      "title": "string",
      "detail": "string",
      "source": {
        "pointer": "string",
        "parameter": "string"
      }
    }
  ],
  "nluInfo": {
    "elements": [
      {
        "text": "string",
        "type": "string",
        "entity": true,
        "isFilter": true,
        "typeName": "string",
        "errorText": "string",
        "filterText": "string",
        "typeTranslated": "string",
        "filterFieldName": "string"
      }
    ]
  },
  "conversationalResponse": {
    "apps": [
      {
        "id": "string",
        "name": "string"
      }
    ],
    "responses": [
      {
        "type": "string",
        "imageUrl": "string",
        "infoType": "string",
        "sentence": {
          "text": "string"
        },
        "narrative": {
          "text": "string"
        },
        "infoValues": [
          [
            "string"
          ]
        ],
        "errorMessage": "string",
        "followupSentence": "string",
        "renderVisualization": {
          "data": {},
          "language": "string"
        }
      }
    ],
    "contextInfo": "string",
    "drillDownURI": "string",
    "sentenceWithMatches": "string"
  }
}
```

---

### POST /api/v1/questions/actions/filter

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The preferred number of entries returned |
| `page` | string | No | A cursor pointing to the page of data to retrieve. |
| `sort` | string | No | A single field from the data model on which to sort the response. The '+' or '-' operator may be used to specify ascending or desending order.  Enum: "createdAt", "updatedAt", "+createdAt", "+updatedAt", "-createdAt", "-updatedAt" |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | Yes | The advanced filtering to use for the query. Refer to [RFC 7644](https://www.rfc-editor.org/rfc/rfc7644#section-3.4.2.2) for the syntax.  Filter on createdAt and updatedAt fields are encouraged and support `eq`, `ne`, `gt`, `ge`, `lt`, `le` comparison operators along with `and` and `or` logical operators.  Filter on tenantId field is not supported.  `co`, `sw` and `ew` operators are not supported.  Examples: ``` appId eq 'appId1' ``` ``` (appId eq 'appId1' or appId eq 'appId2') ``` ``` (appId eq 'appId1' or appId eq 'appId2') and (createdAt gt '2022-08-03T00:00:00.000Z' and createdAt lt '2022-08-04T00:00:00.000Z') ```  ``` (appId eq 'appId1') and (createdAt ge '2022-08-03T00:00:00.000Z') ```  ``` (appId eq 'appId1') and (createdAt le '2022-08-23:59:59.000Z') ```  ``` (appId eq 'appId1') and (questionId eq '12345') ``` |

#### Responses

##### 200

If the user has access to any of the provided app id

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique record id stored in database |
| `apps` | object[] | No | Metadata for app |
| `lang` | string | No | language selected for query from insight advisor or insight advisor chat or third party api |
| `appId` | string | Yes | Qlik sense app id that is being used to answer the question |
| `appName` | string | No | Qlik sense app name that is being used to answer the question |
| `nluInfo` | object[] | No | Contains break down of the asked question in the form of tokens with their classification. |
| `version` | string | Yes | Version of the metric model |
| `feedback` | object[] | No | Any feedback from the user about a given recommendation |
| `tenantId` | string | No | Qlik sense tenant Id |
| `channelId` | string | No | Source from which conversation is happening |
| `chartType` | string | No | Chart type for given query. For insight advisor it would be 'native' and for insight advisor chat, it could be 'static' or 'responsive' |
| `createdAt` | string | Yes | Record created date |
| `createdBy` | string | No | Qlik sense user id who is interacting with insight advisor or insight advisor chat or third party api |
| `queryText` | string | No | Query asked by user in insight advisor or insight advisor or third party api |
| `queryType` | string | No | Nature of query being asked during the conversation e.g. query, applist, measurelist, dimensionlist Enum: "appList", "appSuggested", "dimensionList", "exploreThisFurther", "followup", "greetings", "measureList", "query", "sampleQuestion" |
| `responses` | object | No | Provides info what was included in response for given query |
| `stopWords` | string[] | No | Tokens from question parsed which are ignored |
| `updatedAt` | string | Yes | Record modified date |
| `queryError` | boolean | No |  |
| `questionId` | string | Yes | Unique id assigned to user query |
| `queryOrigin` | string | No | Refers to source from where narrative request is called Enum: "askQuestion", "iaAnalysis", "iaAssetsPanel" |
| `recommendations` | object[] | No | Visualisation recommendation specs for the query |
| `isContextualQuery` | boolean | No | Boolean value indicates whether given query is contextual or not. It would be false for insight advisor |
| `unmatchedEntities` | string[] | No | Tokens parsed as entities but not matched with app's field/dimension/measure |

<details>
<summary>Properties of `apps`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No |  |
| `space_id` | string | No |  |
| `space_name` | string | No |  |
| `space_type` | string | No |  |
| `limited_access` | boolean | No |  |
| `last_reload_date` | string | No |  |

</details>

<details>
<summary>Properties of `nluInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the token or phrase from query Enum: "dimension", "measure", "date" |
| `text` | string | No | Matching token or phrase from query |
| `type` | string | No | Type of token from query Enum: "field", "filter", "master_dimension", "master_measure", "custom_analysis" |
| `fieldName` | string | No | Qlik sense application field selected for given token or phrase |
| `fieldValue` | string | No | Filter value found from query |

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `comment` | string | No |  |
| `chartType` | string | No |  |
| `analysisType` | string | No |  |
| `recommendationLiked` | boolean | Yes |  |
| `recommendationDisliked` | boolean | Yes |  |
| `recommendationAddedToHub` | boolean | Yes |  |
| `recommendationAddedToSheet` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `responses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hasChart` | boolean | No | Chart was provided |
| `hasInsights` | boolean | No | Narrative was provided |
| `hasSuggestions` | boolean | No | Suggestion questions was provided |
| `hasMetadataApps` | boolean | No | App list was provided |
| `hasSampleQueries` | boolean | No | Sample questions was provided |
| `hasMetadataMeasures` | boolean | No | Measures list was provided |
| `hasMetadataDimensions` | boolean | No | Dimensions list was provided |

</details>

<details>
<summary>Properties of `recommendations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dims` | string[] | No | Dimension(s) considered for recommendation |
| `msrs` | string[] | No | Measure(s) considered for recommendation |
| `analysis` | string | No | Enum: "breakdown", "changePoint", "comparison", "contribution", "correlation", "fact", "mutualInfo", "rank", "spike", "trend", "values" |
| `chartType` | string | No | Chart type given to current recommendation Enum: "barchart", "combochart", "distributionplot", "kpi", "linechart", "map", "scatterplot", "table" |
| `relevance` | number | No |  |
| `analysisGroup` | string | No | Enum: "anomaly", "brekadown", "comparison", "correl", "fact", "list", "mutualInfo", "rank" |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | Yes | The total number of metrics matching the current filter. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request. The payload is not formed correctly.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

User is not authorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 422

Unprocessable entity. The payload contains fields
that are invalid, such as too long of a query.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/questions/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/questions/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ filter: 'string' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/questions/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/questions/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"filter":"string"}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "apps": [
        {
          "id": "string",
          "name": "string",
          "space_id": "string",
          "space_name": "string",
          "space_type": "string",
          "limited_access": true,
          "last_reload_date": "2018-10-30T07:06:22Z"
        }
      ],
      "lang": "string",
      "appId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "appName": "string",
      "nluInfo": [
        {
          "role": "dimension",
          "text": "string",
          "type": "field",
          "fieldName": "string",
          "fieldValue": "string"
        }
      ],
      "version": "string",
      "feedback": [
        {
          "comment": "string",
          "chartType": "string",
          "analysisType": "string",
          "recommendationLiked": true,
          "recommendationDisliked": true,
          "recommendationAddedToHub": true,
          "recommendationAddedToSheet": true
        }
      ],
      "tenantId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "channelId": "string",
      "chartType": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "queryText": "string",
      "queryType": "appList",
      "responses": {
        "hasChart": true,
        "hasInsights": true,
        "hasSuggestions": true,
        "hasMetadataApps": true,
        "hasSampleQueries": true,
        "hasMetadataMeasures": true,
        "hasMetadataDimensions": true
      },
      "stopWords": [
        "string"
      ],
      "updatedAt": "2018-10-30T07:06:22Z",
      "queryError": false,
      "questionId": "string",
      "queryOrigin": "askQuestion",
      "recommendations": [
        {
          "dims": [
            "string"
          ],
          "msrs": [
            "string"
          ],
          "analysis": "breakdown",
          "chartType": "barchart",
          "relevance": 42,
          "analysisGroup": "anomaly"
        }
      ],
      "isContextualQuery": false,
      "unmatchedEntities": [
        "string"
      ]
    }
  ],
  "meta": {
    "total": 42
  },
  "links": {
    "next": {
      "href": "http://example.com"
    },
    "prev": {
      "href": "http://example.com"
    },
    "self": {
      "href": "http://example.com"
    }
  }
}
```

---
