# Assistants

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Assistants provide a chat interface for asking questions and getting personalized, relevant answers for Qlik Answers.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/assistants`](#get-apiv1assistants) | Retrieves the list of assistants. The result can be filtered, sorted, and paginated. |
| `POST` | [`/api/v1/assistants`](#post-apiv1assistants) | Creates a new assistant. |
| `POST` | [`/api/v1/assistants/{assistantId}/actions/search`](#post-apiv1assistantsassistantidactionssearch) | Perform search with either `SIMPLE` or `FULL` mode. SIMPLE does semantic search while FULL does semantic search, reranking and hybrid search. Use topN to control number of chunks in response, max limit is 50. Default to 5. |
| `GET` | [`/api/v1/assistants/{assistantId}/feedback`](#get-apiv1assistantsassistantidfeedback) | Retrieves feedback summary for the assistant. |
| `POST` | [`/api/v1/assistants/{assistantId}/sources/plaintexts`](#post-apiv1assistantsassistantidsourcesplaintexts) | Perform a bulk search for the plaintext of source chunks for the assistant. |
| `GET` | [`/api/v1/assistants/{assistantId}/starters`](#get-apiv1assistantsassistantidstarters) | Retrieves the list of starters for the assistant. |
| `POST` | [`/api/v1/assistants/{assistantId}/starters`](#post-apiv1assistantsassistantidstarters) | Creates a new starter for the assistant. |
| `GET` | [`/api/v1/assistants/{assistantId}/starters/{starterId}`](#get-apiv1assistantsassistantidstartersstarterid) | Retrieves the specified starter. |
| `PUT` | [`/api/v1/assistants/{assistantId}/starters/{starterId}`](#put-apiv1assistantsassistantidstartersstarterid) | Updates the specified starter. |
| `DELETE` | [`/api/v1/assistants/{assistantId}/starters/{starterId}`](#delete-apiv1assistantsassistantidstartersstarterid) | Deletes the starter and all of its resources. |
| `PUT` | [`/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}`](#put-apiv1assistantsassistantidstartersstarteridfollowupsfollowupid) | Updates the specified Followup. |
| `DELETE` | [`/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}`](#delete-apiv1assistantsassistantidstartersstarteridfollowupsfollowupid) | Deletes the specified Followup. |
| `GET` | [`/api/v1/assistants/{assistantId}/threads`](#get-apiv1assistantsassistantidthreads) | Retrieves the list of threads for the assistant. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads`](#post-apiv1assistantsassistantidthreads) | Creates a new thread for the assistant. |
| `GET` | [`/api/v1/assistants/{assistantid}/threads/{threadid}`](#get-apiv1assistantsassistantidthreadsthreadid) | Retrieves a thread for the assistant. |
| `PATCH` | [`/api/v1/assistants/{assistantid}/threads/{threadid}`](#patch-apiv1assistantsassistantidthreadsthreadid) | Updates the properties of an existing thread with JSON Patch-formatted data. |
| `DELETE` | [`/api/v1/assistants/{assistantid}/threads/{threadid}`](#delete-apiv1assistantsassistantidthreadsthreadid) | Deletes the specified thread and all of its resources. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke`](#post-apiv1assistantsassistantidthreadsthreadidactionsinvoke) | Execute prompt in synchronous non-streaming mode. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream`](#post-apiv1assistantsassistantidthreadsthreadidactionsstream) | Execute prompt in asynchronous streaming mode. |
| `GET` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions`](#get-apiv1assistantsassistantidthreadsthreadidinteractions) | Retrieves the list of interactions for the thread. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions`](#post-apiv1assistantsassistantidthreadsthreadidinteractions) | Creates a new interaction for the thread. |
| `GET` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}`](#get-apiv1assistantsassistantidthreadsthreadidinteractionsinteractionid) | Retrieves an interaction for the thread. |
| `DELETE` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}`](#delete-apiv1assistantsassistantidthreadsthreadidinteractionsinteractionid) | Deletes the specified interaction and all of its resources. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback`](#post-apiv1assistantsassistantidthreadsthreadidinteractionsinteractionidfeedback) | Creates feedback for the thread. |
| `PATCH` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId}`](#patch-apiv1assistantsassistantidthreadsthreadidinteractionsinteractionidfeedbackfeedbackid) | Updates feedback for the thread. |
| `POST` | [`/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews`](#post-apiv1assistantsassistantidthreadsthreadidinteractionsinteractionidreviews) | Creates feedback review for the thread. |
| `GET` | [`/api/v1/assistants/{id}`](#get-apiv1assistantsid) | Retrieves the specified assistant. |
| `PATCH` | [`/api/v1/assistants/{id}`](#patch-apiv1assistantsid) | Updates the properties of an existing assistant with JSON Patch-formatted data. |
| `DELETE` | [`/api/v1/assistants/{id}`](#delete-apiv1assistantsid) | Deletes the assistant and all of its resources. |

## API Reference

### GET /api/v1/assistants

Retrieves the list of assistants. The result can be filtered, sorted, and paginated.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of assistants to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, e.g. `name`. Can be prefixed with `-` to set descending order; defaults to ascending. Enum: "NAME", "-NAME", "DESCRIPTION", "-DESCRIPTION", "CREATED", "-CREATED", "UPDATED", "-UPDATED" |
| `spaceId` | string | No | Optional parameter to filter assistants by space ID. |
| `countTotal` | boolean | No | _(deprecated)_ Optional parameter to request total count for query. |

#### Responses

##### 200

Successful operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the assistant. |
| `name` | string | Yes | The name of the assistant. |
| `tags` | string[] | Yes | The list of tags associated with the assistant. |
| `title` | string | No | The title of the assistant. |
| `ownerId` | string | Yes | Unique identifier of the assistant owner. |
| `spaceId` | string | Yes | Unique identifier of the space containing the assistant. |
| `tenantId` | string | Yes | Unique identifier of the assistant tenant. |
| `createdAt` | string | Yes | Datetime when the assistant was created. |
| `createdBy` | string | Yes | Unique identifier of the user who created the assistant. |
| `hasAvatar` | boolean | No | Indicates if the assistant has an avatar. |
| `updatedAt` | string | Yes | Datetime when the assistant was updated. |
| `updatedBy` | string | Yes | Unique identifier of the user who last updated the assistant. |
| `description` | string | Yes | The description of the assistant. |
| `systemMessage` | string | No | _(deprecated)_ System prompt setting up conversation context. |
| `knowledgeBases` | string[] | Yes | List of knowledgebases the assistant is using. |
| `welcomeMessage` | string | Yes | Initial message in the chat conversation. |
| `customProperties` | object | Yes | freeform JSON to allow custom customization options. |
| `defaultPromptType` | string | No | Default prompt type for the assistant. Enum: "thread", "oneshot" |
| `orderedStarterIds` | string[] | No | List of starter IDs in the order they will be sorted. |

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

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

##### 403

The user does not have privileges to perform the requested action.

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
// qlik-api has not implemented support for `GET /api/v1/assistants` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants',
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
# qlik-cli has not implemented support for GET /api/v1/assistants yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "Organization-wide Assistant",
      "tags": [
        "Red",
        "Sales"
      ],
      "title": "Assistant for Sales activities",
      "ownerId": "507f191e810c19729de860ea",
      "spaceId": "507f191e810c19729de860ea",
      "tenantId": "507f191e810c19729de860ea",
      "createdAt": "2021-10-02T14:20:50.52Z",
      "createdBy": "507f191e810c19729de860ea",
      "hasAvatar": true,
      "updatedAt": "2021-10-02T14:20:50.52Z",
      "updatedBy": "507f191e810c19729de860ea",
      "description": "This assistant is used for...",
      "systemMessage": "You are helpful Sales assistant. Provide concise and actionable insights.",
      "knowledgeBases": [
        "507f191e810c19729de860ea"
      ],
      "welcomeMessage": "Welcome to Sales process support Assistant.",
      "customProperties": {
        "customErrors": {
          "outsideScopeError": "Outside of scope error",
          "complexQuestionError": "Complex question error",
          "promptInjectionError": "Prompt injection error"
        }
      },
      "defaultPromptType": "thread",
      "orderedStarterIds": [
        "507f191e810c19729de860ea",
        "787f191e810c19729de860er"
      ]
    }
  ],
  "meta": {
    "countTotal": 42
  },
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/assistants

Creates a new assistant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the assistant. |
| `tags` | string[] | Yes | The list of tags for the assistant. |
| `title` | string | Yes | The title of the assistant. |
| `spaceId` | string | Yes | Unique identifier of the space to contain the assistant. |
| `description` | string | Yes | The description of the assistant. |
| `systemMessage` | string | No | _(deprecated)_ System prompt setting up conversation context. |
| `knowledgeBases` | string[] | Yes | List of knowledgebases the assistant is using. |
| `welcomeMessage` | string | Yes | Initial message in the chat conversation. |
| `customProperties` | object | Yes | freeform JSON to allow custom customization options. |
| `defaultPromptType` | string | No | Default prompt type for the assistant. Enum: "thread", "oneshot" |
| `orderedStarterIds` | string[] | No | List of starter IDs in the order they will be sorted. |

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the assistant. |
| `tags` | string[] | Yes | The list of tags for the assistant. |
| `title` | string | Yes | The title of the assistant. |
| `avatar` | string | No | user uploaded avatar, filetype must be png |
| `spaceId` | string | Yes | Unique identifier of the space to contain the assistant. |
| `description` | string | Yes | The description of the assistant. |
| `systemMessage` | string | No | _(deprecated)_ System prompt setting up conversation context. |
| `knowledgeBases` | string[] | Yes | List of knowledgebases the assistant is using. |
| `welcomeMessage` | string | Yes | Initial message in the chat conversation. |
| `customProperties` | object | Yes | freeform JSON to allow custom customization options. |
| `defaultPromptType` | string | No | Default prompt type for the assistant. Enum: "thread", "oneshot" |

#### Responses

##### 201

Successfully created an assistant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the assistant. |
| `name` | string | Yes | The name of the assistant. |
| `tags` | string[] | Yes | The list of tags associated with the assistant. |
| `title` | string | No | The title of the assistant. |
| `ownerId` | string | Yes | Unique identifier of the assistant owner. |
| `spaceId` | string | Yes | Unique identifier of the space containing the assistant. |
| `tenantId` | string | Yes | Unique identifier of the assistant tenant. |
| `createdAt` | string | Yes | Datetime when the assistant was created. |
| `createdBy` | string | Yes | Unique identifier of the user who created the assistant. |
| `hasAvatar` | boolean | No | Indicates if the assistant has an avatar. |
| `updatedAt` | string | Yes | Datetime when the assistant was updated. |
| `updatedBy` | string | Yes | Unique identifier of the user who last updated the assistant. |
| `description` | string | Yes | The description of the assistant. |
| `systemMessage` | string | No | _(deprecated)_ System prompt setting up conversation context. |
| `knowledgeBases` | string[] | Yes | List of knowledgebases the assistant is using. |
| `welcomeMessage` | string | Yes | Initial message in the chat conversation. |
| `customProperties` | object | Yes | freeform JSON to allow custom customization options. |
| `defaultPromptType` | string | No | Default prompt type for the assistant. Enum: "thread", "oneshot" |
| `orderedStarterIds` | string[] | No | List of starter IDs in the order they will be sorted. |

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

##### 403

The user does not have privileges to perform the requested action.

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
// qlik-api has not implemented support for `POST /api/v1/assistants` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Organization-wide assistant',
      tags: ['Red', 'Sales'],
      title: 'Assistant for Sales activities',
      spaceId: '507f191e810c19729de860ea',
      description:
        'This assistant is used for...',
      systemMessage:
        'You are helpful Sales assistant. Provide concise and actionable insights.',
      knowledgeBases: [
        '507f191e810c19729de860ea',
      ],
      welcomeMessage:
        'Welcome to Sales process support Assistant.',
      customProperties: {
        customErrors: {
          outsideScopeError:
            'Outside of scope error',
          complexQuestionError:
            'Complex question error',
          promptInjectionError:
            'Prompt injection error',
        },
      },
      defaultPromptType: 'thread',
      orderedStarterIds: [
        '507f191e810c19729de860ea',
        '787f191e810c19729de860er',
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Organization-wide assistant","tags":["Red","Sales"],"title":"Assistant for Sales activities","spaceId":"507f191e810c19729de860ea","description":"This assistant is used for...","systemMessage":"You are helpful Sales assistant. Provide concise and actionable insights.","knowledgeBases":["507f191e810c19729de860ea"],"welcomeMessage":"Welcome to Sales process support Assistant.","customProperties":{"customErrors":{"outsideScopeError":"Outside of scope error","complexQuestionError":"Complex question error","promptInjectionError":"Prompt injection error"}},"defaultPromptType":"thread","orderedStarterIds":["507f191e810c19729de860ea","787f191e810c19729de860er"]}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Organization-wide Assistant",
  "tags": [
    "Red",
    "Sales"
  ],
  "title": "Assistant for Sales activities",
  "ownerId": "507f191e810c19729de860ea",
  "spaceId": "507f191e810c19729de860ea",
  "tenantId": "507f191e810c19729de860ea",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "createdBy": "507f191e810c19729de860ea",
  "hasAvatar": true,
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "updatedBy": "507f191e810c19729de860ea",
  "description": "This assistant is used for...",
  "systemMessage": "You are helpful Sales assistant. Provide concise and actionable insights.",
  "knowledgeBases": [
    "507f191e810c19729de860ea"
  ],
  "welcomeMessage": "Welcome to Sales process support Assistant.",
  "customProperties": {
    "customErrors": {
      "outsideScopeError": "Outside of scope error",
      "complexQuestionError": "Complex question error",
      "promptInjectionError": "Prompt injection error"
    }
  },
  "defaultPromptType": "thread",
  "orderedStarterIds": [
    "507f191e810c19729de860ea",
    "787f191e810c19729de860er"
  ]
}
```

---

### POST /api/v1/assistants/{assistantId}/actions/search

Perform search with either `SIMPLE` or `FULL` mode. SIMPLE does semantic search while FULL does semantic search, reranking and hybrid search. Use topN to control number of chunks in response, max limit is 50. Default to 5.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID for the Assistant of interest |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `topN` | integer | No | Number of chunks to return in results. |
| `prompt` | string | Yes | Query text or question to search. |
| `searchMode` | string | No | Search mode to use.   Allowed values: `SIMPLE` and `FULL`.   Default: `SIMPLE`.  Enum: "SIMPLE", "FULL" |

#### Responses

##### 200

Chunks retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | Retrieved document chunks |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | Yes | Text content of the chunk |
| `chunkMeta` | object | Yes | Metadata about the chunk |
| `tfidfScore` | number | No | Score from keyword search |
| `searchSource` | string | No | search method for the chunk, e.g. `semantic search`, `keyword search` or `semantic and keyword search` |
| `semanticScore` | number | No | Similarity score from embedding match |

<details>
<summary>Properties of `chunkMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | Yes | source of chunk |
| `chunkId` | string | Yes | chunkId |
| `documentId` | string | Yes | documentId of chunk |
| `datasourceId` | string | Yes | datasourceId of chunk |
| `knowledgeBaseId` | string | Yes | knowledgeBaseId of chunk |

</details>

</details>

##### 400

The request is in incorrect format

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The user does not have privileges to perform the requested action.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Assistant is not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 405

Method is not allowed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Prompt processing error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/actions/search` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/actions/search',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      topN: 20,
      prompt: 'What is LLM?',
      searchMode: 'SIMPLE',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/actions/search yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/actions/search" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"topN":20,"prompt":"What is LLM?","searchMode":"SIMPLE"}'
```

**Example Response:**

```json
{
  "chunks": [
    {
      "text": "LLM stands for Large Language Model",
      "chunkMeta": {
        "source": "string",
        "chunkId": "string",
        "documentId": "string",
        "datasourceId": "string",
        "knowledgeBaseId": "string"
      },
      "tfidfScore": 0.9,
      "searchSource": "string",
      "semanticScore": 0.63
    }
  ]
}
```

---

### GET /api/v1/assistants/{assistantId}/feedback

Retrieves feedback summary for the assistant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant from which to retrieve feedback summary. |

#### Responses

##### 200

Successfully retrieved the feedback summary for the assistant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `likes` | integer | Yes | Amount of likes for a thread or an assistant. |
| `other` | integer | No | Count of answers which users disliked and gave "other" as reason. |
| `reviews` | integer | Yes | Amount of reviews for a thread or an assistant. |
| `dislikes` | integer | Yes | Amount of dislikes for a thread or an assistant. |
| `unhelpful` | integer | No | Count of answers which users marked as "unhelpful". |
| `inaccurate` | integer | No | Count of answers which users marked as "inaccurate". |
| `irrelevant` | integer | No | Count of answers which users marked as "irrelevant". |
| `repetitive` | integer | No | Count of answers which users marked as "repetitive". |
| `unanswered` | integer | No | Count of questions for which the assistant provided no answer. |
| `interactions` | integer | Yes | Amount of interactions for a thread or an assistant. |

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/feedback` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/feedback',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/feedback yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/feedback" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "likes": 42,
  "other": 42,
  "reviews": 42,
  "dislikes": 42,
  "unhelpful": 42,
  "inaccurate": 42,
  "irrelevant": 42,
  "repetitive": 42,
  "unanswered": 42,
  "interactions": 42
}
```

---

### POST /api/v1/assistants/{assistantId}/sources/plaintexts

Perform a bulk search for the plaintext of source chunks for the assistant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to search for source chunks. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunkIds` | string[] | Yes | Unique identifier of the Chunk. |

#### Responses

##### 202

Successfully retrieved plaintext of the chunks.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `textByChunkId` | object | No |  |

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

##### 403

The user does not have privileges to perform the requested action.

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

The resource was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/sources/plaintexts` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/sources/plaintexts',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      chunkIds: [
        'c2ef42d9-7164-4fb0-bdbb-6534ae37263e',
        '486ada2c-f895-4961-8ba5-7995f1026d26',
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/sources/plaintexts yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/sources/plaintexts" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"chunkIds":["c2ef42d9-7164-4fb0-bdbb-6534ae37263e","486ada2c-f895-4961-8ba5-7995f1026d26"]}'
```

**Example Response:**

```json
{
  "textByChunkId": {
    "chunk1_id": "chunk1_text",
    "chunk2_id": "chunk2_text"
  }
}
```

---

### GET /api/v1/assistants/{assistantId}/starters

Retrieves the list of starters for the assistant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant from which to retrieve starters. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of starters to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, e.g. `name`. Can be prefixed with `-` to set descending order; defaults to ascending. Enum: "QUESTION", "-QUESTION", "CREATED", "-CREATED", "UPDATED", "-UPDATED" |

#### Responses

##### 200

Successfully retrieved the assistant's starters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `createdAt` | string | Yes | Datetime when the starter was created. |
| `followups` | object[] | No | List of followups. |
| `updatedAt` | string | Yes | Datetime when the starter was updated. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/starters` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/starters yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "question": "Where was Genghis Khan buried?",
      "createdAt": "2021-10-02T14:20:50.52Z",
      "followups": [
        {
          "id": "507f191e810c19729de860ea",
          "question": "Where was Genghis Khan buried?",
          "additionalContext": "string",
          "recommendedAnswer": {
            "content": "string",
            "contentType": "text | markdown | html"
          }
        }
      ],
      "updatedAt": "2021-10-02T14:20:50.52Z",
      "additionalContext": "string",
      "recommendedAnswer": {
        "content": "string",
        "contentType": "text | markdown | html"
      }
    }
  ],
  "meta": {
    "countTotal": 42
  },
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/assistants/{assistantId}/starters

Creates a new starter for the assistant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to create the starter. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `question` | string | Yes | Starter sample question. |
| `followups` | object[] | No | List of followups. |
| `additionalContext` | string | No | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | No |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

#### Responses

##### 201

Successfully created a new assistant starter.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `createdAt` | string | Yes | Datetime when the starter was created. |
| `followups` | object[] | No | List of followups. |
| `updatedAt` | string | Yes | Datetime when the starter was updated. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

##### 400

The request is in incorrect format or starter limit exceeded.

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

The user does not have privileges to perform the requested action.

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

The assistant was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/starters` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      question: 'Where was Genghis Khan buried?',
      followups: [
        {
          id: '507f191e810c19729de860ea',
          question:
            'Where was Genghis Khan buried?',
          additionalContext: 'string',
          recommendedAnswer: {
            content: 'string',
            contentType: 'text | markdown | html',
          },
        },
      ],
      additionalContext: 'string',
      recommendedAnswer: {
        content: 'string',
        contentType: 'text | markdown | html',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/starters yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"question":"Where was Genghis Khan buried?","followups":[{"id":"507f191e810c19729de860ea","question":"Where was Genghis Khan buried?","additionalContext":"string","recommendedAnswer":{"content":"string","contentType":"text | markdown | html"}}],"additionalContext":"string","recommendedAnswer":{"content":"string","contentType":"text | markdown | html"}}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "question": "Where was Genghis Khan buried?",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "followups": [
    {
      "id": "507f191e810c19729de860ea",
      "question": "Where was Genghis Khan buried?",
      "additionalContext": "string",
      "recommendedAnswer": {
        "content": "string",
        "contentType": "text | markdown | html"
      }
    }
  ],
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "additionalContext": "string",
  "recommendedAnswer": {
    "content": "string",
    "contentType": "text | markdown | html"
  }
}
```

---

### GET /api/v1/assistants/{assistantId}/starters/{starterId}

Retrieves the specified starter.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested starter. |
| `starterId` | string | Yes | The ID of the starter to retrieve. |

#### Responses

##### 200

Successfully retrieved the starter.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `createdAt` | string | Yes | Datetime when the starter was created. |
| `followups` | object[] | No | List of followups. |
| `updatedAt` | string | Yes | Datetime when the starter was updated. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

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

##### 403

The operation failed due to insufficient permissions.

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

The starter was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/starters/{starterId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters/{starterId}',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/starters/{starterId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters/{starterId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "question": "Where was Genghis Khan buried?",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "followups": [
    {
      "id": "507f191e810c19729de860ea",
      "question": "Where was Genghis Khan buried?",
      "additionalContext": "string",
      "recommendedAnswer": {
        "content": "string",
        "contentType": "text | markdown | html"
      }
    }
  ],
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "additionalContext": "string",
  "recommendedAnswer": {
    "content": "string",
    "contentType": "text | markdown | html"
  }
}
```

---

### PUT /api/v1/assistants/{assistantId}/starters/{starterId}

Updates the specified starter.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested starter. |
| `starterId` | string | Yes | The ID of the starter to retrieve. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `followups` | object[] | No | List of followups. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

#### Responses

##### 200

Successfully updated the starter.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `createdAt` | string | Yes | Datetime when the starter was created. |
| `followups` | object[] | No | List of followups. |
| `updatedAt` | string | Yes | Datetime when the starter was updated. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

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

##### 403

The operation failed due to insufficient permissions.

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

The record was not found.

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
// qlik-api has not implemented support for `PUT /api/v1/assistants/{assistantId}/starters/{starterId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters/{starterId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: '507f191e810c19729de860ea',
      question: 'Where was Genghis Khan buried?',
      followups: [
        {
          id: '507f191e810c19729de860ea',
          question:
            'Where was Genghis Khan buried?',
          additionalContext: 'string',
          recommendedAnswer: {
            content: 'string',
            contentType: 'text | markdown | html',
          },
        },
      ],
      additionalContext: 'string',
      recommendedAnswer: {
        content: 'string',
        contentType: 'text | markdown | html',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/assistants/{assistantId}/starters/{starterId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters/{starterId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"507f191e810c19729de860ea","question":"Where was Genghis Khan buried?","followups":[{"id":"507f191e810c19729de860ea","question":"Where was Genghis Khan buried?","additionalContext":"string","recommendedAnswer":{"content":"string","contentType":"text | markdown | html"}}],"additionalContext":"string","recommendedAnswer":{"content":"string","contentType":"text | markdown | html"}}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "question": "Where was Genghis Khan buried?",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "followups": [
    {
      "id": "507f191e810c19729de860ea",
      "question": "Where was Genghis Khan buried?",
      "additionalContext": "string",
      "recommendedAnswer": {
        "content": "string",
        "contentType": "text | markdown | html"
      }
    }
  ],
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "additionalContext": "string",
  "recommendedAnswer": {
    "content": "string",
    "contentType": "text | markdown | html"
  }
}
```

---

### DELETE /api/v1/assistants/{assistantId}/starters/{starterId}

Deletes the starter and all of its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested starter. |
| `starterId` | string | Yes | The ID of the starter to delete. |

#### Responses

##### 204

Successful operation.

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/assistants/{assistantId}/starters/{starterId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters/{starterId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/assistants/{assistantId}/starters/{starterId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters/{starterId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### PUT /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}

Updates the specified Followup.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested Followup. |
| `followupId` | string | Yes | The ID of the Followup to update. |
| `starterId` | string | Yes | The ID of the starter containing the requested Followup. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

#### Responses

##### 200

Successfully updated the Followup.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the starter. |
| `question` | string | Yes | Starter sample question. |
| `createdAt` | string | Yes | Datetime when the starter was created. |
| `followups` | object[] | No | List of followups. |
| `updatedAt` | string | Yes | Datetime when the starter was updated. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `followups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the Followup. |
| `question` | string | Yes | Starter sample question. |
| `additionalContext` | string | Yes | Optional context collected from curated meant to be leveraged by LLM-based question recommendation system. |
| `recommendedAnswer` | object | Yes |  |

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

</details>

</details>

<details>
<summary>Properties of `recommendedAnswer`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | string | Yes | Starter answer content. |
| `contentType` | string | Yes | Answer type of content. |

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

##### 403

The operation failed due to insufficient permissions.

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

The record was not found.

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
// qlik-api has not implemented support for `PUT /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: '507f191e810c19729de860ea',
      question: 'Where was Genghis Khan buried?',
      additionalContext: 'string',
      recommendedAnswer: {
        content: 'string',
        contentType: 'text | markdown | html',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"507f191e810c19729de860ea","question":"Where was Genghis Khan buried?","additionalContext":"string","recommendedAnswer":{"content":"string","contentType":"text | markdown | html"}}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "question": "Where was Genghis Khan buried?",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "followups": [
    {
      "id": "507f191e810c19729de860ea",
      "question": "Where was Genghis Khan buried?",
      "additionalContext": "string",
      "recommendedAnswer": {
        "content": "string",
        "contentType": "text | markdown | html"
      }
    }
  ],
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "additionalContext": "string",
  "recommendedAnswer": {
    "content": "string",
    "contentType": "text | markdown | html"
  }
}
```

---

### DELETE /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}

Deletes the specified Followup.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested Followup. |
| `followupId` | string | Yes | The ID of the Followup to delete. |
| `starterId` | string | Yes | The ID of the starter containing the requested Followup. |

#### Responses

##### 204

Successful operation.

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

##### 403

The operation failed due to insufficient permissions.

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

The Followup was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/starters/{starterId}/followups/{followupId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/assistants/{assistantId}/threads

Retrieves the list of threads for the assistant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant from which to retrieve threads. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Optional parameter to filter threads. |
| `limit` | integer | No | The number of assistants to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, e.g. `name`. Can be prefixed with `-` to set descending order; defaults to ascending. Enum: "NAME", "-NAME", "CREATED", "-CREATED", "UPDATED", "-UPDATED" |

#### Responses

##### 200

Successfully retrieved the threads for the assistant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the thread. |
| `name` | string | Yes | The name of the thread. |
| `ownerId` | string | Yes |  |
| `favorite` | boolean | Yes | If thread is marked as favorite. |
| `createdAt` | string | Yes | Datetime when the thread was created. |
| `deletedAt` | string | No | Datetime when the thread was deleted. |
| `updatedAt` | string | Yes | Datetime when the thread was updated. |
| `hasFeedback` | boolean | Yes | If feedback was provided for a thread interaction. |
| `summaryStats` | object | Yes |  |
| `useUserPreferredLanguage` | boolean | Yes | If the thread should respond in the user's preferred language. |

<details>
<summary>Properties of `summaryStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `likes` | integer | Yes | Amount of likes for a thread or an assistant. |
| `other` | integer | No | Count of answers which users disliked and gave "other" as reason. |
| `reviews` | integer | Yes | Amount of reviews for a thread or an assistant. |
| `dislikes` | integer | Yes | Amount of dislikes for a thread or an assistant. |
| `unhelpful` | integer | No | Count of answers which users marked as "unhelpful". |
| `inaccurate` | integer | No | Count of answers which users marked as "inaccurate". |
| `irrelevant` | integer | No | Count of answers which users marked as "irrelevant". |
| `repetitive` | integer | No | Count of answers which users marked as "repetitive". |
| `unanswered` | integer | No | Count of questions for which the assistant provided no answer. |
| `interactions` | integer | Yes | Amount of interactions for a thread or an assistant. |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/threads` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/threads yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "Initial conversation",
      "ownerId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "favorite": false,
      "createdAt": "2021-10-02T14:20:50.52Z",
      "deletedAt": "2021-10-02T14:20:50.52Z",
      "updatedAt": "2021-10-02T14:20:50.52Z",
      "hasFeedback": false,
      "summaryStats": {
        "likes": 42,
        "other": 42,
        "reviews": 42,
        "dislikes": 42,
        "unhelpful": 42,
        "inaccurate": 42,
        "irrelevant": 42,
        "repetitive": 42,
        "unanswered": 42,
        "interactions": 42
      },
      "useUserPreferredLanguage": false
    }
  ],
  "meta": {
    "countTotal": 42
  },
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/assistants/{assistantId}/threads

Creates a new thread for the assistant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to create the thread. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the thread. |
| `useUserPreferredLanguage` | boolean | No | Whether the thread should use the user's preferred language. |

#### Responses

##### 201

Successfully created a new assistant thread.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the thread. |
| `name` | string | Yes | The name of the thread. |
| `ownerId` | string | Yes |  |
| `favorite` | boolean | Yes | If thread is marked as favorite. |
| `createdAt` | string | Yes | Datetime when the thread was created. |
| `deletedAt` | string | No | Datetime when the thread was deleted. |
| `updatedAt` | string | Yes | Datetime when the thread was updated. |
| `hasFeedback` | boolean | Yes | If feedback was provided for a thread interaction. |
| `summaryStats` | object | Yes |  |
| `useUserPreferredLanguage` | boolean | Yes | If the thread should respond in the user's preferred language. |

<details>
<summary>Properties of `summaryStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `likes` | integer | Yes | Amount of likes for a thread or an assistant. |
| `other` | integer | No | Count of answers which users disliked and gave "other" as reason. |
| `reviews` | integer | Yes | Amount of reviews for a thread or an assistant. |
| `dislikes` | integer | Yes | Amount of dislikes for a thread or an assistant. |
| `unhelpful` | integer | No | Count of answers which users marked as "unhelpful". |
| `inaccurate` | integer | No | Count of answers which users marked as "inaccurate". |
| `irrelevant` | integer | No | Count of answers which users marked as "irrelevant". |
| `repetitive` | integer | No | Count of answers which users marked as "repetitive". |
| `unanswered` | integer | No | Count of questions for which the assistant provided no answer. |
| `interactions` | integer | Yes | Amount of interactions for a thread or an assistant. |

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

##### 403

The user does not have privileges to perform the requested action.

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

The assistant was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Initial conversation',
      useUserPreferredLanguage: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Initial conversation","useUserPreferredLanguage":false}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Initial conversation",
  "ownerId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
  "favorite": false,
  "createdAt": "2021-10-02T14:20:50.52Z",
  "deletedAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "hasFeedback": false,
  "summaryStats": {
    "likes": 42,
    "other": 42,
    "reviews": 42,
    "dislikes": 42,
    "unhelpful": 42,
    "inaccurate": 42,
    "irrelevant": 42,
    "repetitive": 42,
    "unanswered": 42,
    "interactions": 42
  },
  "useUserPreferredLanguage": false
}
```

---

### GET /api/v1/assistants/{assistantid}/threads/{threadid}

Retrieves a thread for the assistant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantid` | string | Yes | The ID of the assistant containing the requested thread. |
| `threadid` | string | Yes | The ID of the thread to retrieve. |

#### Responses

##### 200

Successfully retrieved the thread.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the thread. |
| `name` | string | Yes | The name of the thread. |
| `ownerId` | string | Yes | Unique identifier of the thread owner. |
| `favorite` | boolean | Yes | If thread is marked as favorite. |
| `messages` | object[] | Yes |  |
| `createdAt` | string | Yes | Datetime when the thread was created. |
| `deletedAt` | string | No | Datetime when the thread was deleted. |
| `updatedAt` | string | Yes | Datetime when the thread was updated. |
| `hasFeedback` | boolean | Yes | If feedback was provided for a thread interaction. |
| `summaryStats` | object | Yes |  |
| `useUserPreferredLanguage` | boolean | Yes | If the thread should respond in the user's preferred language. |

<details>
<summary>Properties of `messages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `role` | string | Yes | human or ai role. |
| `content` | string | Yes | Message content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `createdAt` | string | Yes | Datetime when the interaction was created. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `summaryStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `likes` | integer | Yes | Amount of likes for a thread or an assistant. |
| `other` | integer | No | Count of answers which users disliked and gave "other" as reason. |
| `reviews` | integer | Yes | Amount of reviews for a thread or an assistant. |
| `dislikes` | integer | Yes | Amount of dislikes for a thread or an assistant. |
| `unhelpful` | integer | No | Count of answers which users marked as "unhelpful". |
| `inaccurate` | integer | No | Count of answers which users marked as "inaccurate". |
| `irrelevant` | integer | No | Count of answers which users marked as "irrelevant". |
| `repetitive` | integer | No | Count of answers which users marked as "repetitive". |
| `unanswered` | integer | No | Count of questions for which the assistant provided no answer. |
| `interactions` | integer | Yes | Amount of interactions for a thread or an assistant. |

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

##### 403

The operation failed due to insufficient permissions.

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

The thread was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantid}/threads/{threadid}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantid}/threads/{threadid}',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantid}/threads/{threadid} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantid}/threads/{threadid}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Initial conversation",
  "ownerId": "507f191e810c19729de860ea",
  "favorite": false,
  "messages": [
    {
      "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "role": "ai",
      "content": "Somewhere in an unmarked grave",
      "sources": [
        {
          "chunks": [
            {
              "text": "string",
              "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
            }
          ],
          "source": "Reference.md",
          "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
          "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
          "lastIndexedAt": "2021-10-02T14:20:50.52Z",
          "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "createdAt": "2021-10-02T14:20:50.52Z"
    }
  ],
  "createdAt": "2021-10-02T14:20:50.52Z",
  "deletedAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "hasFeedback": false,
  "summaryStats": {
    "likes": 42,
    "other": 42,
    "reviews": 42,
    "dislikes": 42,
    "unhelpful": 42,
    "inaccurate": 42,
    "irrelevant": 42,
    "repetitive": 42,
    "unanswered": 42,
    "interactions": 42
  },
  "useUserPreferredLanguage": false
}
```

---

### PATCH /api/v1/assistants/{assistantid}/threads/{threadid}

Updates the properties of an existing thread with JSON Patch-formatted data.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantid` | string | Yes | The ID of the assistant containing the requested thread. |
| `threadid` | string | Yes | The ID of the thread to retrieve. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace", "add" |
| `path` | string | Yes | A JSON Pointer. |
| `value` | string \| number \| boolean | Yes | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | number | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

</details>

#### Responses

##### 204

Thread updated successfully.

##### 400

Bad request. Payload could not be parsed to a JSON Patch or Patch operations are invalid.

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

Not authorized.

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

The operation failed due to insufficient permissions.

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

The term to patch was not found.

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

##### 429

The request has been rate-limited.

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
// qlik-api has not implemented support for `PATCH /api/v1/assistants/{assistantid}/threads/{threadid}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantid}/threads/{threadid}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'new name',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/assistants/{assistantid}/threads/{threadid} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantid}/threads/{threadid}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"new name"}]'
```

---

### DELETE /api/v1/assistants/{assistantid}/threads/{threadid}

Deletes the specified thread and all of its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantid` | string | Yes | The ID of the assistant containing the requested thread. |
| `threadid` | string | Yes | The ID of the thread to retrieve. |

#### Responses

##### 204

Successful operation.

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/assistants/{assistantid}/threads/{threadid}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantid}/threads/{threadid}',
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
# qlik-cli has not implemented support for DELETE /api/v1/assistants/{assistantid}/threads/{threadid} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantid}/threads/{threadid}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke

Execute prompt in synchronous non-streaming mode.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the Assistant containing requested Thread |
| `threadId` | string | Yes | The ID of the Thread to retrieve |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | object | No |  |

<details>
<summary>Properties of `input`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | string | No | Input prompt string for the Assistant to respond to. |
| `promptType` | string | No | Sets the prompt type to thread. Enum: "thread" |
| `includeText` | boolean | No | Returns text from chunks in sources output. Default value is false. |

</details>

#### Responses

##### 200

Prompt is successfully executed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `output` | string | No | Assistant's response to the prompt |
| `sources` | object[] | No | List of sources used to generate AI messages |
| `question` | string | No | Question asked by the user for assistant to answer |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | No | List of Chunks used for "AI" generated messages |
| `source` | string | No | path to the document used |
| `documentId` | string | No | reference to Document used for "AI" generated messages |
| `datasourceId` | string | No | reference to DataSource used for "AI" generated messages |
| `knowledgebaseId` | string | No | reference to KnowledgeBase used for "AI" generated messages |

</details>

##### 400

The request is in incorrect format

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The user does not have privileges to perform the requested action.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Assistant is not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Prompt processing error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      input: {
        prompt: 'What is a LLM?',
        promptType: 'thread',
        includeText: true,
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"input":{"prompt":"What is a LLM?","promptType":"thread","includeText":true}}'
```

**Example Response:**

```json
{
  "output": "LLM stands for Large Language Model",
  "sources": [
    {
      "chunks": [
        {
          "text": "LLM stands for Large Language Model",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ],
  "question": "What was the primary goal of the Apollo program?"
}
```

---

### POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream

Execute prompt in asynchronous streaming mode.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the Assistant containing requested Thread |
| `threadId` | string | Yes | The ID of the Thread to retrieve |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | object | No |  |

<details>
<summary>Properties of `input`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | string | No | Input prompt string for the Assistant to respond to. |
| `promptType` | string | No | Sets the prompt type to thread. Enum: "thread" |
| `includeText` | boolean | No | Returns text from chunks in sources output. Default value is false. |

</details>

#### Responses

##### 200

Prompt is successfully executed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `output` | string | No | Assistant's response to the prompt |
| `sources` | object[] | No | List of sources used to generate AI messages |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | No | List of Chunks used for "AI" generated messages |
| `source` | string | No | path to the document used |
| `documentId` | string | No | reference to Document used for "AI" generated messages |
| `datasourceId` | string | No | reference to DataSource used for "AI" generated messages |
| `knowledgebaseId` | string | No | reference to KnowledgeBase used for "AI" generated messages |

</details>

##### 400

The request is in incorrect format

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 403

The user does not have privileges to perform the requested action.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Method is not allowed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 405

Assistant is not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Prompt processing error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Custom error codes * AE-1 - Internal processing error * AE-2 - Incorrect request * AE-3 - Authentication issue * AE-4 - Prompt is rejected * AE-5 - Resource is not found * AE-6 - API usage rate limit is exceeded * AE-7 - Method is not allowed |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      input: {
        prompt: 'What is a LLM?',
        promptType: 'thread',
        includeText: true,
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"input":{"prompt":"What is a LLM?","promptType":"thread","includeText":true}}'
```

**Example Response:**

```json
{
  "output": "LLM stands for Large Language Model",
  "sources": [
    {
      "chunks": [
        {
          "text": "LLM stands for Large Language Model",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ]
}
```

---

### GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions

Retrieves the list of interactions for the thread.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant from which to retrieve the interactions. |
| `threadId` | string | Yes | The ID of the thread from which to retrieve the interactions. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The number of feedback to get. |
| `next` | string | No | Optional parameter to request the next page. |
| `prev` | string | No | Optional parameter to request the previous page. |
| `sort` | string | No | Optional resource field name to sort on, case insensitive, e.g. `created`. Can be prefixed with `-` to set descending order; defaults to ascending. Enum: "CREATED", "-CREATED", "UPDATED", "-UPDATED" |

#### Responses

##### 200

Successfully retrieved the thread interactions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `ownerId` | string | Yes | Unique identifier of user which created the interaction. |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `feedback` | object | No |  |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `threadId` | string | Yes | ID of the thread to which the interaction belongs. |
| `createdAt` | string | Yes | Datetime when the interaction was created. |
| `updatedAt` | string | Yes | Datetime when the interaction was updated. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique feedback identifier. |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | Yes | Optional comment for feedback. |
| `reviewedAt` | string | No | Datetime when the feedback was reviewed. |
| `reviewerId` | string | Yes | Unique feedback reviewer identifier. |
| `reviewStatus` | string | Yes | Feedback review status. |

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `countTotal` | integer | No |  |

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

##### 403

The operation failed due to insufficient permissions.

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

The feedback was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "ownerId": "65e310c43fb1cf46654e0878",
      "request": "Where was Genghis Khan buried?",
      "sources": [
        {
          "chunks": [
            {
              "text": "string",
              "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
            }
          ],
          "source": "Reference.md",
          "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
          "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
          "lastIndexedAt": "2021-10-02T14:20:50.52Z",
          "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "feedback": {
        "id": "507f191e810c19729de860ea",
        "vote": 1,
        "reason": "inaccurate | irrelevant | repetitive | unhelpful | other",
        "comment": "string",
        "reviewedAt": "2021-10-02T14:20:50.52Z",
        "reviewerId": "507f191e810c19729de860ea",
        "reviewStatus": "reviewed | unreviewed"
      },
      "rejected": true,
      "response": "Somewhere in an unmarked grave",
      "threadId": "125c24c4-668c-4c97-bef8-30d910169913",
      "createdAt": "2021-10-02T14:20:50.52Z",
      "updatedAt": "2021-10-02T14:20:55.52Z"
    }
  ],
  "meta": {
    "countTotal": 42
  },
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions

Creates a new interaction for the thread.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to create the interaction. |
| `threadId` | string | Yes | The ID of the thread in which to create the interaction. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `rejectionReason` | integer | No | Rejection reason for a question:   * 1 - PROMPT_INJECTION   * 2 - OUT_OF_CONTEXT   * 3 - TOO_COMPLEX  Enum: 1, 2, 3 |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No | Chunk text for "AI" generated message source. |
| `chunkId` | string | Yes | Chunk unique identifier for "AI" generated message source. |

</details>

</details>

#### Responses

##### 201

Successfully created a new thread interaction.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `ownerId` | string | Yes | Unique identifier of user which created the interaction. |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `feedback` | object | No |  |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `threadId` | string | Yes | ID of the thread to which the interaction belongs. |
| `createdAt` | string | Yes | Datetime when the interaction was created. |
| `updatedAt` | string | Yes | Datetime when the interaction was updated. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No | Chunk text for "AI" generated message source. |
| `chunkId` | string | Yes | Chunk unique identifier for "AI" generated message source. |

</details>

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique feedback identifier. |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | Yes | Optional comment for feedback. |
| `reviewedAt` | string | No | Datetime when the feedback was reviewed. |
| `reviewerId` | string | Yes | Unique feedback reviewer identifier. |
| `reviewStatus` | string | Yes | Feedback review status. |

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

##### 403

The user does not have privileges to perform the requested action.

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

The assistant or the thread was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      request: 'Where was Genghis Khan buried?',
      sources: [
        {
          chunks: [
            {
              text: 'string',
              chunkId:
                '10d347c4-f28a-4faf-93f0-48e781aaf303',
            },
          ],
          source: 'Reference.md',
          documentId:
            '10d347c4-f28a-4faf-93f0-48e781aaf303',
          datasourceId:
            '10d347c4-f28a-4faf-93f0-48e781aaf303',
          lastIndexedAt:
            '2021-10-02T14:20:50.52Z',
          knowledgebaseId:
            '10d347c4-f28a-4faf-93f0-48e781aaf303',
        },
      ],
      rejected: true,
      response: 'Somewhere in an unmarked grave',
      rejectionReason: 1,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"request":"Where was Genghis Khan buried?","sources":[{"chunks":[{"text":"string","chunkId":"10d347c4-f28a-4faf-93f0-48e781aaf303"}],"source":"Reference.md","documentId":"10d347c4-f28a-4faf-93f0-48e781aaf303","datasourceId":"10d347c4-f28a-4faf-93f0-48e781aaf303","lastIndexedAt":"2021-10-02T14:20:50.52Z","knowledgebaseId":"10d347c4-f28a-4faf-93f0-48e781aaf303"}],"rejected":true,"response":"Somewhere in an unmarked grave","rejectionReason":1}'
```

**Example Response:**

```json
{
  "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
  "ownerId": "65e310c43fb1cf46654e0878",
  "request": "Where was Genghis Khan buried?",
  "sources": [
    {
      "chunks": [
        {
          "text": "string",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "lastIndexedAt": "2021-10-02T14:20:50.52Z",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ],
  "feedback": {
    "id": "507f191e810c19729de860ea",
    "vote": 1,
    "reason": "inaccurate | irrelevant | repetitive | unhelpful | other",
    "comment": "string",
    "reviewedAt": "2021-10-02T14:20:50.52Z",
    "reviewerId": "507f191e810c19729de860ea",
    "reviewStatus": "reviewed | unreviewed"
  },
  "rejected": true,
  "response": "Somewhere in an unmarked grave",
  "threadId": "125c24c4-668c-4c97-bef8-30d910169913",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:55.52Z"
}
```

---

### GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}

Retrieves an interaction for the thread.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to retrieve the interaction. |
| `interactionId` | string | Yes | The ID of the interaction to retrieve. |
| `threadId` | string | Yes | The ID of the thread in which to retrieve the interaction. |

#### Responses

##### 200

Successfully retrieved the interaction.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `ownerId` | string | Yes | Unique identifier of user which created the interaction. |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `feedback` | object | No |  |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `threadId` | string | Yes | ID of the thread to which the interaction belongs. |
| `createdAt` | string | Yes | Datetime when the interaction was created. |
| `updatedAt` | string | Yes | Datetime when the interaction was updated. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No | Chunk text for "AI" generated message source. |
| `chunkId` | string | Yes | Chunk unique identifier for "AI" generated message source. |

</details>

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique feedback identifier. |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | Yes | Optional comment for feedback. |
| `reviewedAt` | string | No | Datetime when the feedback was reviewed. |
| `reviewerId` | string | Yes | Unique feedback reviewer identifier. |
| `reviewStatus` | string | Yes | Feedback review status. |

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

##### 403

The operation failed due to insufficient permissions.

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

The interaction was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
  "ownerId": "65e310c43fb1cf46654e0878",
  "request": "Where was Genghis Khan buried?",
  "sources": [
    {
      "chunks": [
        {
          "text": "string",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "lastIndexedAt": "2021-10-02T14:20:50.52Z",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ],
  "feedback": {
    "id": "507f191e810c19729de860ea",
    "vote": 1,
    "reason": "inaccurate | irrelevant | repetitive | unhelpful | other",
    "comment": "string",
    "reviewedAt": "2021-10-02T14:20:50.52Z",
    "reviewerId": "507f191e810c19729de860ea",
    "reviewStatus": "reviewed | unreviewed"
  },
  "rejected": true,
  "response": "Somewhere in an unmarked grave",
  "threadId": "125c24c4-668c-4c97-bef8-30d910169913",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:55.52Z"
}
```

---

### DELETE /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}

Deletes the specified interaction and all of its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to delete the interaction. |
| `interactionId` | string | Yes | The ID of the interaction to delete. |
| `threadId` | string | Yes | The ID of the thread in which to delete the interaction. |

#### Responses

##### 204

Successful operation.

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

##### 403

The operation failed due to insufficient permissions.

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

The resource was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback

Creates feedback for the thread.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to create the feedback. |
| `interactionId` | string | Yes | The ID of the interaction in which to create the feedback. |
| `threadId` | string | Yes | The ID of the thread in which to create the feedback. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | No | Optional comment for feedback. |

#### Responses

##### 201

Successfully created a new thread feedback.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `ownerId` | string | Yes | Unique identifier of user which created the interaction. |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `feedback` | object | No |  |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `threadId` | string | Yes | ID of the thread to which the interaction belongs. |
| `createdAt` | string | Yes | Datetime when the interaction was created. |
| `updatedAt` | string | Yes | Datetime when the interaction was updated. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No | Chunk text for "AI" generated message source. |
| `chunkId` | string | Yes | Chunk unique identifier for "AI" generated message source. |

</details>

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique feedback identifier. |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | Yes | Optional comment for feedback. |
| `reviewedAt` | string | No | Datetime when the feedback was reviewed. |
| `reviewerId` | string | Yes | Unique feedback reviewer identifier. |
| `reviewStatus` | string | Yes | Feedback review status. |

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

##### 403

The user does not have privileges to perform the requested action.

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

The resource was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      vote: 1,
      reason:
        'inaccurate | irrelevant | repetitive | unhelpful | other',
      comment: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"vote":1,"reason":"inaccurate | irrelevant | repetitive | unhelpful | other","comment":"string"}'
```

**Example Response:**

```json
{
  "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
  "ownerId": "65e310c43fb1cf46654e0878",
  "request": "Where was Genghis Khan buried?",
  "sources": [
    {
      "chunks": [
        {
          "text": "string",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "lastIndexedAt": "2021-10-02T14:20:50.52Z",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ],
  "feedback": {
    "id": "507f191e810c19729de860ea",
    "vote": 1,
    "reason": "inaccurate | irrelevant | repetitive | unhelpful | other",
    "comment": "string",
    "reviewedAt": "2021-10-02T14:20:50.52Z",
    "reviewerId": "507f191e810c19729de860ea",
    "reviewStatus": "reviewed | unreviewed"
  },
  "rejected": true,
  "response": "Somewhere in an unmarked grave",
  "threadId": "125c24c4-668c-4c97-bef8-30d910169913",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:55.52Z"
}
```

---

### PATCH /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId}

Updates feedback for the thread.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant containing the requested feedback. |
| `feedbackId` | string | Yes | The ID of the feedback to update. |
| `interactionId` | string | Yes | The ID of the interaction containing the requested Feedback. |
| `threadId` | string | Yes | The ID of the thread containing the requested feedback. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace", "add" |
| `path` | string | Yes | A JSON Pointer. |
| `value` | string \| number \| boolean | Yes | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | number | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

</details>

#### Responses

##### 204

Successfully updated the feedback.

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

##### 403

The operation failed due to insufficient permissions.

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

The resource was not found.

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
// qlik-api has not implemented support for `PATCH /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/reason',
        value: 'irrelevant',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/feedback/{feedbackId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/reason","value":"irrelevant"}]'
```

---

### POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews

Creates feedback review for the thread.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assistantId` | string | Yes | The ID of the assistant in which to create the feedback review. |
| `interactionId` | string | Yes | The ID of the interaction in which to create the feedback review. |
| `threadId` | string | Yes | The ID of the thread in which to create the feedback review. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reviewStatus` | string | Yes | Review status. |

#### Responses

##### 201

Successfully created a new thread feedback.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `ownerId` | string | Yes | Unique identifier of user which created the interaction. |
| `request` | string | Yes | Interaction request content. |
| `sources` | object[] | Yes | List of sources used to generate AI messages (interactions). |
| `feedback` | object | No |  |
| `rejected` | boolean | No | Indicator the system marked request as suspicious. |
| `response` | string | Yes | Interaction response content. |
| `threadId` | string | Yes | ID of the thread to which the interaction belongs. |
| `createdAt` | string | Yes | Datetime when the interaction was created. |
| `updatedAt` | string | Yes | Datetime when the interaction was updated. |

<details>
<summary>Properties of `sources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chunks` | object[] | Yes | List of Chunks used for "AI" generated messages. |
| `source` | string | Yes | Path to the document used. |
| `documentId` | string | Yes | Reference to Document used for "AI" generated messages. |
| `datasourceId` | string | Yes | Reference to DataSource used for "AI" generated messages. |
| `lastIndexedAt` | string | No | Datetime when the knowledgebase was last indexed. |
| `knowledgebaseId` | string | Yes | Reference to KnowledgeBase used for "AI" generated messages. |

<details>
<summary>Properties of `chunks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | No | Chunk text for "AI" generated message source. |
| `chunkId` | string | Yes | Chunk unique identifier for "AI" generated message source. |

</details>

</details>

<details>
<summary>Properties of `feedback`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique feedback identifier. |
| `vote` | integer | Yes | Integer representation of feedback given (-1 = negative, 1 = positive). |
| `reason` | string | Yes | Reason for feedback. |
| `comment` | string | Yes | Optional comment for feedback. |
| `reviewedAt` | string | No | Datetime when the feedback was reviewed. |
| `reviewerId` | string | Yes | Unique feedback reviewer identifier. |
| `reviewStatus` | string | Yes | Feedback review status. |

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

##### 403

The user does not have privileges to perform the requested action.

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

A resource was not found.

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
// qlik-api has not implemented support for `POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      reviewStatus: 'reviewed | unreviewed',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{assistantId}/threads/{threadId}/interactions/{interactionId}/reviews" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"reviewStatus":"reviewed | unreviewed"}'
```

**Example Response:**

```json
{
  "id": "10d347c4-f28a-4faf-93f0-48e781aaf303",
  "ownerId": "65e310c43fb1cf46654e0878",
  "request": "Where was Genghis Khan buried?",
  "sources": [
    {
      "chunks": [
        {
          "text": "string",
          "chunkId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
        }
      ],
      "source": "Reference.md",
      "documentId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "datasourceId": "10d347c4-f28a-4faf-93f0-48e781aaf303",
      "lastIndexedAt": "2021-10-02T14:20:50.52Z",
      "knowledgebaseId": "10d347c4-f28a-4faf-93f0-48e781aaf303"
    }
  ],
  "feedback": {
    "id": "507f191e810c19729de860ea",
    "vote": 1,
    "reason": "inaccurate | irrelevant | repetitive | unhelpful | other",
    "comment": "string",
    "reviewedAt": "2021-10-02T14:20:50.52Z",
    "reviewerId": "507f191e810c19729de860ea",
    "reviewStatus": "reviewed | unreviewed"
  },
  "rejected": true,
  "response": "Somewhere in an unmarked grave",
  "threadId": "125c24c4-668c-4c97-bef8-30d910169913",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "updatedAt": "2021-10-02T14:20:55.52Z"
}
```

---

### GET /api/v1/assistants/{id}

Retrieves the specified assistant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the assistant to retrieve. |

#### Responses

##### 200

Successfully retrieved the assistant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the assistant. |
| `name` | string | Yes | The name of the assistant. |
| `tags` | string[] | Yes | The list of tags associated with the assistant. |
| `title` | string | No | The title of the assistant. |
| `ownerId` | string | Yes | Unique identifier of the assistant owner. |
| `spaceId` | string | Yes | Unique identifier of the space containing the assistant. |
| `tenantId` | string | Yes | Unique identifier of the assistant tenant. |
| `createdAt` | string | Yes | Datetime when the assistant was created. |
| `createdBy` | string | Yes | Unique identifier of the user who created the assistant. |
| `hasAvatar` | boolean | No | Indicates if the assistant has an avatar. |
| `updatedAt` | string | Yes | Datetime when the assistant was updated. |
| `updatedBy` | string | Yes | Unique identifier of the user who last updated the assistant. |
| `description` | string | Yes | The description of the assistant. |
| `systemMessage` | string | No | _(deprecated)_ System prompt setting up conversation context. |
| `knowledgeBases` | string[] | Yes | List of knowledgebases the assistant is using. |
| `welcomeMessage` | string | Yes | Initial message in the chat conversation. |
| `customProperties` | object | Yes | freeform JSON to allow custom customization options. |
| `defaultPromptType` | string | No | Default prompt type for the assistant. Enum: "thread", "oneshot" |
| `orderedStarterIds` | string[] | No | List of starter IDs in the order they will be sorted. |

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `GET /api/v1/assistants/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/assistants/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Organization-wide Assistant",
  "tags": [
    "Red",
    "Sales"
  ],
  "title": "Assistant for Sales activities",
  "ownerId": "507f191e810c19729de860ea",
  "spaceId": "507f191e810c19729de860ea",
  "tenantId": "507f191e810c19729de860ea",
  "createdAt": "2021-10-02T14:20:50.52Z",
  "createdBy": "507f191e810c19729de860ea",
  "hasAvatar": true,
  "updatedAt": "2021-10-02T14:20:50.52Z",
  "updatedBy": "507f191e810c19729de860ea",
  "description": "This assistant is used for...",
  "systemMessage": "You are helpful Sales assistant. Provide concise and actionable insights.",
  "knowledgeBases": [
    "507f191e810c19729de860ea"
  ],
  "welcomeMessage": "Welcome to Sales process support Assistant.",
  "customProperties": {
    "customErrors": {
      "outsideScopeError": "Outside of scope error",
      "complexQuestionError": "Complex question error",
      "promptInjectionError": "Prompt injection error"
    }
  },
  "defaultPromptType": "thread",
  "orderedStarterIds": [
    "507f191e810c19729de860ea",
    "787f191e810c19729de860er"
  ]
}
```

---

### PATCH /api/v1/assistants/{id}

Updates the properties of an existing assistant with JSON Patch-formatted data.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The assistant ID. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `if-match` | string | No | Optional header to do conditional updates. Using the Etag value that was returned the last time the assistant was fetched. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace", "add" |
| `path` | string | Yes | A JSON Pointer. |
| `value` | string \| number \| boolean | Yes | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | number | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

</details>

#### Responses

##### 204

Assistant updated successfully.

##### 400

Bad request. Payload could not be parsed to a JSON Patch or Patch operations are invalid.

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

Not authorized.

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

The operation failed due to insufficient permissions.

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

The term to patch was not found.

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

##### 429

The request has been rate-limited.

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
// qlik-api has not implemented support for `PATCH /api/v1/assistants/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'new name',
      },
      {
        op: 'replace',
        path: '/description',
        value: 'new description',
      },
      {
        op: 'add',
        path: '/defaultPromptType',
        value: 'thread',
      },
      { op: 'remove', path: '/avatar' },
      {
        op: 'add',
        path: '/avatar',
        value:
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAlAQAAAAAsYlcCAAAACklEQVR4AWMYBQABAwABRUEDtQAAAABJRU5ErkJggg==',
      },
      {
        op: 'replace',
        path: '/avatar',
        value:
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAlAQAAAAAsYlcCAAAACklEQVR4AWMYBQABAwABRUEDtQAAAABJRU5ErkJggg==',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/assistants/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"new name"},{"op":"replace","path":"/description","value":"new description"},{"op":"add","path":"/defaultPromptType","value":"thread"},{"op":"remove","path":"/avatar"},{"op":"add","path":"/avatar","value":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAlAQAAAAAsYlcCAAAACklEQVR4AWMYBQABAwABRUEDtQAAAABJRU5ErkJggg=="},{"op":"replace","path":"/avatar","value":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAlAQAAAAAsYlcCAAAACklEQVR4AWMYBQABAwABRUEDtQAAAABJRU5ErkJggg=="}]'
```

---

### DELETE /api/v1/assistants/{id}

Deletes the assistant and all of its resources.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the assistant to delete. |

#### Responses

##### 204

Successful operation.

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

##### 403

The operation failed due to insufficient permissions.

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

The assistant was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/assistants/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/assistants/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/assistants/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/assistants/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
