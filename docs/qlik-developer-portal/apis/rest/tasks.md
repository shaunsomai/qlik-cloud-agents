# Tasks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

API for managing tasks and task chains in Qlik Cloud. The requesting user needs the "reload" permission on the target resource to use this set of endpoints. A tenant admin can use GET /v1/tasks and DELETE /v1/tasks/{id} to perform administrative actions, even without the "reload" permission.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/tasks`](#get-apiv1tasks) | Retrieves a list of the tasks that the requesting user has access to. |
| `POST` | [`/api/v1/tasks`](#post-apiv1tasks) | Creates a new task. |
| `GET` | [`/api/v1/tasks/{id}`](#get-apiv1tasksid) | Retrieves details for a specific task. |
| `PUT` | [`/api/v1/tasks/{id}`](#put-apiv1tasksid) | Updates a specific task. If the task is owned by another user, ownership will be transferred to the requesting user. |
| `DELETE` | [`/api/v1/tasks/{id}`](#delete-apiv1tasksid) | Deletes a specific task. |
| `POST` | [`/api/v1/tasks/{id}/actions/start`](#post-apiv1tasksidactionsstart) | Starts the specified task. |
| `GET` | [`/api/v1/tasks/{id}/runs`](#get-apiv1tasksidruns) | Returns runs for the specified task. |
| `GET` | [`/api/v1/tasks/{id}/runs/{runId}/log`](#get-apiv1tasksidrunsrunidlog) | Get specific run log of a task. |
| `GET` | [`/api/v1/tasks/{id}/runs/last`](#get-apiv1tasksidrunslast) | Returns the last run of a specific task. |
| `GET` | [`/api/v1/tasks/resources/{id}/runs`](#get-apiv1tasksresourcesidruns) | Returns a list of task runs for a specified `resourceId`. |

## API Reference

### GET /api/v1/tasks

Retrieves a list of the tasks that the requesting user has access to.

- **Replaced by:** "GET:/scheduling/tasks"
- **Rate Limit:** Special (600 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of resources to return for a request. |
| `page` | string | No | The page cursor. |
| `resourceId` | string | No | Filter tasks by its target resource ID. |
| `sort` | string | No | The property of a resource to sort on (default sort is -updatedAt). A property must be prefixed by + or - to indicate ascending or descending sort order respectively.  Enum: "+createdAt", "-createdAt", "+updatedAt", "-updatedAt" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The choreographer's unique identifier |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

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
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/tasks', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "key": "string",
      "name": "string",
      "start": {
        "schedule": "string",
        "stateName": "string"
      },
      "events": [
        {
          "name": "string",
          "type": "com.qlik.v1.task.run.finished",
          "source": "system-events.task",
          "dataOnly": true,
          "correlation": [
            {
              "contextAttributeName": "id",
              "contextAttributeValue": "string"
            }
          ]
        }
      ],
      "states": [
        {
          "end": true,
          "name": "string",
          "type": "EVENT",
          "onEvents": [
            {
              "actions": [
                {
                  "name": "string",
                  "retryRef": "string",
                  "condition": "string",
                  "functionRef": {},
                  "retryableErrors": [
                    "string"
                  ],
                  "nonRetryableErrors": [
                    "string"
                  ]
                }
              ],
              "eventRefs": [
                "string"
              ],
              "actionMode": "SEQUENTIAL"
            }
          ],
          "timeouts": {
            "eventTimeout": "string",
            "stateExecTimeout": "string",
            "actionExecTimeout": "string"
          },
          "exclusive": true,
          "compensatedBy": "string"
        }
      ],
      "enabled": false,
      "version": "string",
      "metadata": {
        "usage": "ANALYTICS",
        "ownerId": "string",
        "spaceId": "string",
        "trigger": {
          "id": "string",
          "type": 0
        },
        "tenantId": "string",
        "createdAt": "2018-10-30T07:06:22Z",
        "createdBy": "string",
        "deletedAt": "2018-10-30T07:06:22Z",
        "updatedAt": "2018-10-30T07:06:22Z",
        "disabledCode": "MANUALLY",
        "migratedFrom": "string",
        "orchestration": {
          "id": "string",
          "type": 0,
          "attrs": {}
        }
      },
      "keepActive": false,
      "resourceId": "string",
      "annotations": [
        "string"
      ],
      "description": "string",
      "specVersion": "string"
    }
  ],
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

### POST /api/v1/tasks

Creates a new task.

- **Replaced by:** "POST:/scheduling/tasks"
- **Rate Limit:** Special (600 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `migrateFrom` | string | No | ID of the reload-task to migrate from the old system (optional). |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | Name of the starting workflow state |

<details>
<summary>Properties of `schedule`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | CloudEvent Extension Context Attribute name Enum: "id", "status" |
| `contextAttributeValue` | string | No | CloudEvent Extension Context Attribute value |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdBy` | string | No | The user ID of the user that created the task |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

#### Responses

##### 201

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The choreographer's unique identifier |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | Name of the starting workflow state |

<details>
<summary>Properties of `schedule`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | CloudEvent Extension Context Attribute name Enum: "id", "status" |
| `contextAttributeValue` | string | No | CloudEvent Extension Context Attribute value |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/tasks', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    key: 'string',
    name: 'string',
    start: {
      schedule: 'string',
      stateName: 'string',
    },
    events: [
      {
        name: 'string',
        type: 'com.qlik.v1.task.run.finished',
        source: 'system-events.task',
        dataOnly: true,
        correlation: [
          {
            contextAttributeName: 'id',
            contextAttributeValue: 'string',
          },
        ],
      },
    ],
    states: [
      {
        end: true,
        name: 'string',
        type: 'EVENT',
        onEvents: [
          {
            actions: [
              {
                name: 'string',
                retryRef: 'string',
                condition: 'string',
                functionRef: {},
                retryableErrors: ['string'],
                nonRetryableErrors: ['string'],
              },
            ],
            eventRefs: ['string'],
            actionMode: 'SEQUENTIAL',
          },
        ],
        timeouts: {
          eventTimeout: 'string',
          stateExecTimeout: 'string',
          actionExecTimeout: 'string',
        },
        exclusive: true,
        compensatedBy: 'string',
      },
    ],
    enabled: false,
    version: 'string',
    metadata: {
      usage: 'ANALYTICS',
      ownerId: 'string',
      spaceId: 'string',
      trigger: { id: 'string', type: 0 },
      tenantId: 'string',
      createdBy: 'string',
      updatedAt: '2018-10-30T07:06:22Z',
      disabledCode: 'MANUALLY',
      migratedFrom: 'string',
      orchestration: {
        id: 'string',
        type: 0,
        attrs: {},
      },
    },
    keepActive: false,
    resourceId: 'string',
    annotations: ['string'],
    description: 'string',
    specVersion: 'string',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"key":"string","name":"string","start":{"schedule":"string","stateName":"string"},"events":[{"name":"string","type":"com.qlik.v1.task.run.finished","source":"system-events.task","dataOnly":true,"correlation":[{"contextAttributeName":"id","contextAttributeValue":"string"}]}],"states":[{"end":true,"name":"string","type":"EVENT","onEvents":[{"actions":[{"name":"string","retryRef":"string","condition":"string","functionRef":{},"retryableErrors":["string"],"nonRetryableErrors":["string"]}],"eventRefs":["string"],"actionMode":"SEQUENTIAL"}],"timeouts":{"eventTimeout":"string","stateExecTimeout":"string","actionExecTimeout":"string"},"exclusive":true,"compensatedBy":"string"}],"enabled":false,"version":"string","metadata":{"usage":"ANALYTICS","ownerId":"string","spaceId":"string","trigger":{"id":"string","type":0},"tenantId":"string","createdBy":"string","updatedAt":"2018-10-30T07:06:22Z","disabledCode":"MANUALLY","migratedFrom":"string","orchestration":{"id":"string","type":0,"attrs":{}}},"keepActive":false,"resourceId":"string","annotations":["string"],"description":"string","specVersion":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "key": "string",
  "name": "string",
  "start": {
    "schedule": "string",
    "stateName": "string"
  },
  "events": [
    {
      "name": "string",
      "type": "com.qlik.v1.task.run.finished",
      "source": "system-events.task",
      "dataOnly": true,
      "correlation": [
        {
          "contextAttributeName": "id",
          "contextAttributeValue": "string"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "string",
      "type": "EVENT",
      "onEvents": [
        {
          "actions": [
            {
              "name": "string",
              "retryRef": "string",
              "condition": "string",
              "functionRef": {},
              "retryableErrors": [
                "string"
              ],
              "nonRetryableErrors": [
                "string"
              ]
            }
          ],
          "eventRefs": [
            "string"
          ],
          "actionMode": "SEQUENTIAL"
        }
      ],
      "timeouts": {
        "eventTimeout": "string",
        "stateExecTimeout": "string",
        "actionExecTimeout": "string"
      },
      "exclusive": true,
      "compensatedBy": "string"
    }
  ],
  "enabled": false,
  "version": "string",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": "string",
    "spaceId": "string",
    "trigger": {
      "id": "string",
      "type": 0
    },
    "tenantId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "string",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "orchestration": {
      "id": "string",
      "type": 0,
      "attrs": {}
    }
  },
  "keepActive": false,
  "resourceId": "string",
  "annotations": [
    "string"
  ],
  "description": "string",
  "specVersion": "string"
}
```

---

### GET /api/v1/tasks/{id}

Retrieves details for a specific task.

- **Replaced by:** "GET:/scheduling/tasks/{id}"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The choreographer's unique identifier |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | Name of the starting workflow state |

<details>
<summary>Properties of `schedule`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | CloudEvent Extension Context Attribute name Enum: "id", "status" |
| `contextAttributeValue` | string | No | CloudEvent Extension Context Attribute value |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "key": "string",
  "name": "string",
  "start": {
    "schedule": "string",
    "stateName": "string"
  },
  "events": [
    {
      "name": "string",
      "type": "com.qlik.v1.task.run.finished",
      "source": "system-events.task",
      "dataOnly": true,
      "correlation": [
        {
          "contextAttributeName": "id",
          "contextAttributeValue": "string"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "string",
      "type": "EVENT",
      "onEvents": [
        {
          "actions": [
            {
              "name": "string",
              "retryRef": "string",
              "condition": "string",
              "functionRef": {},
              "retryableErrors": [
                "string"
              ],
              "nonRetryableErrors": [
                "string"
              ]
            }
          ],
          "eventRefs": [
            "string"
          ],
          "actionMode": "SEQUENTIAL"
        }
      ],
      "timeouts": {
        "eventTimeout": "string",
        "stateExecTimeout": "string",
        "actionExecTimeout": "string"
      },
      "exclusive": true,
      "compensatedBy": "string"
    }
  ],
  "enabled": false,
  "version": "string",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": "string",
    "spaceId": "string",
    "trigger": {
      "id": "string",
      "type": 0
    },
    "tenantId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "string",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "orchestration": {
      "id": "string",
      "type": 0,
      "attrs": {}
    }
  },
  "keepActive": false,
  "resourceId": "string",
  "annotations": [
    "string"
  ],
  "description": "string",
  "specVersion": "string"
}
```

---

### PUT /api/v1/tasks/{id}

Updates a specific task. If the task is owned by another user, ownership will be transferred to the requesting user.

- **Replaced by:** "PUT:/scheduling/tasks/{id}"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | Name of the starting workflow state |

<details>
<summary>Properties of `schedule`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | CloudEvent Extension Context Attribute name Enum: "id", "status" |
| `contextAttributeValue` | string | No | CloudEvent Extension Context Attribute value |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdBy` | string | No | The user ID of the user that created the task |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The choreographer's unique identifier |
| `key` | string | No | Optional expression that will be used to generate a domain-specific workflow instance identifier |
| `name` | string | Yes | The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier. |
| `start` | object | No |  |
| `events` | object[] | No | Workflow CloudEvent definitions. Defines CloudEvents that can be consumed or produced |
| `states` | object[] | No | State definitions |
| `enabled` | boolean | No | Indicates whether the task is enabled or not |
| `version` | string | No | Workflow version |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout' |
| `resourceId` | string | No | The resource ID of the task. The `Task.resourceId` value from user input is ignored and will be calculated automatically from `Task.states`. |
| `annotations` | string[] | No | List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities |
| `description` | string | No | Workflow description |
| `specVersion` | string | Yes | Serverless Workflow schema version |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Workflow start definition |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | Name of the starting workflow state |

<details>
<summary>Properties of `schedule`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Unique event name |
| `type` | string | No | CloudEvent type Enum: "com.qlik.v1.task.run.finished" |
| `source` | string | No | CloudEvent source Enum: "system-events.task" |
| `dataOnly` | boolean | No | If `true`, only the Event payload is accessible to consuming Workflow states. If `false`, both event payload and context attributes should be accessible |
| `correlation` | object[] | No | CloudEvent correlation definitions |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | CloudEvent Extension Context Attribute name Enum: "id", "status" |
| `contextAttributeValue` | string | No | CloudEvent Extension Context Attribute value |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | any | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      key: 'string',
      name: 'string',
      start: {
        schedule: 'string',
        stateName: 'string',
      },
      events: [
        {
          name: 'string',
          type: 'com.qlik.v1.task.run.finished',
          source: 'system-events.task',
          dataOnly: true,
          correlation: [
            {
              contextAttributeName: 'id',
              contextAttributeValue: 'string',
            },
          ],
        },
      ],
      states: [
        {
          end: true,
          name: 'string',
          type: 'EVENT',
          onEvents: [
            {
              actions: [
                {
                  name: 'string',
                  retryRef: 'string',
                  condition: 'string',
                  functionRef: {},
                  retryableErrors: ['string'],
                  nonRetryableErrors: ['string'],
                },
              ],
              eventRefs: ['string'],
              actionMode: 'SEQUENTIAL',
            },
          ],
          timeouts: {
            eventTimeout: 'string',
            stateExecTimeout: 'string',
            actionExecTimeout: 'string',
          },
          exclusive: true,
          compensatedBy: 'string',
        },
      ],
      enabled: false,
      version: 'string',
      metadata: {
        usage: 'ANALYTICS',
        ownerId: 'string',
        spaceId: 'string',
        trigger: { id: 'string', type: 0 },
        tenantId: 'string',
        createdBy: 'string',
        updatedAt: '2018-10-30T07:06:22Z',
        disabledCode: 'MANUALLY',
        migratedFrom: 'string',
        orchestration: {
          id: 'string',
          type: 0,
          attrs: {},
        },
      },
      keepActive: false,
      resourceId: 'string',
      annotations: ['string'],
      description: 'string',
      specVersion: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"key":"string","name":"string","start":{"schedule":"string","stateName":"string"},"events":[{"name":"string","type":"com.qlik.v1.task.run.finished","source":"system-events.task","dataOnly":true,"correlation":[{"contextAttributeName":"id","contextAttributeValue":"string"}]}],"states":[{"end":true,"name":"string","type":"EVENT","onEvents":[{"actions":[{"name":"string","retryRef":"string","condition":"string","functionRef":{},"retryableErrors":["string"],"nonRetryableErrors":["string"]}],"eventRefs":["string"],"actionMode":"SEQUENTIAL"}],"timeouts":{"eventTimeout":"string","stateExecTimeout":"string","actionExecTimeout":"string"},"exclusive":true,"compensatedBy":"string"}],"enabled":false,"version":"string","metadata":{"usage":"ANALYTICS","ownerId":"string","spaceId":"string","trigger":{"id":"string","type":0},"tenantId":"string","createdBy":"string","updatedAt":"2018-10-30T07:06:22Z","disabledCode":"MANUALLY","migratedFrom":"string","orchestration":{"id":"string","type":0,"attrs":{}}},"keepActive":false,"resourceId":"string","annotations":["string"],"description":"string","specVersion":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "key": "string",
  "name": "string",
  "start": {
    "schedule": "string",
    "stateName": "string"
  },
  "events": [
    {
      "name": "string",
      "type": "com.qlik.v1.task.run.finished",
      "source": "system-events.task",
      "dataOnly": true,
      "correlation": [
        {
          "contextAttributeName": "id",
          "contextAttributeValue": "string"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "string",
      "type": "EVENT",
      "onEvents": [
        {
          "actions": [
            {
              "name": "string",
              "retryRef": "string",
              "condition": "string",
              "functionRef": {},
              "retryableErrors": [
                "string"
              ],
              "nonRetryableErrors": [
                "string"
              ]
            }
          ],
          "eventRefs": [
            "string"
          ],
          "actionMode": "SEQUENTIAL"
        }
      ],
      "timeouts": {
        "eventTimeout": "string",
        "stateExecTimeout": "string",
        "actionExecTimeout": "string"
      },
      "exclusive": true,
      "compensatedBy": "string"
    }
  ],
  "enabled": false,
  "version": "string",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": "string",
    "spaceId": "string",
    "trigger": {
      "id": "string",
      "type": 0
    },
    "tenantId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "string",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "orchestration": {
      "id": "string",
      "type": 0,
      "attrs": {}
    }
  },
  "keepActive": false,
  "resourceId": "string",
  "annotations": [
    "string"
  ],
  "description": "string",
  "specVersion": "string"
}
```

---

### DELETE /api/v1/tasks/{id}

Deletes a specific task.

- **Replaced by:** "DELETE:/scheduling/tasks/{id}"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Responses

##### 204

No Content response.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/tasks/{id}/actions/start

Starts the specified task.

- **Replaced by:** "POST:/scheduling/tasks/{id}/actions/start"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | No | Indicates the origin of the trigger. If not provided, defaults to 'manual'. For event-triggered tasks, this can be the name of the triggering task. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tasks/{id}/actions/start` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}/actions/start',
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
# qlik-cli has not implemented support for POST /api/v1/tasks/{id}/actions/start yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}/actions/start" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "Task started successfully"
}
```

---

### GET /api/v1/tasks/{id}/runs

Returns runs for the specified task.

- **Replaced by:** "GET:/scheduling/tasks/{id}/runs"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of task runs to return for a request. |
| `page` | string | No | The page cursor. |
| `sort` | string | No | The property of a resource to sort on (default sort is -startedAt). A property must be prefixed by + or - to indicate ascending or descending sort order respectively.  Enum: "+startedAt", "-startedAt", "+endedAt", "-endedAt", "+status", "-status", "+taskId", "-taskId", "+actionId", "-actionId" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the task run |
| `log` | string | No | log info of the run |
| `status` | string | Yes | task run status Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `taskId` | string | Yes | The ID of the task |
| `endedAt` | string | No | The UTC timestamp when the task run ended |
| `actionId` | string | Yes | The ID of the action |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | task name |
| `workerId` | string | Yes | The ID of the worker who is carrying out the real job. e.g. App.Reload job is carried out by Reload Engine, in this case, workerId will be reloadId from reload engine. Or, if we are using Automation, workerId will be Automation runId. |
| `startedAt` | string | No | The UTC timestamp when the task run started |
| `executedAs` | string | No | user ID of on behalf of whom the Task was executed. |
| `resourceId` | string | Yes | The ID of the resource |
| `workerType` | string | Yes | worker type or target system |
| `triggeredBy` | string | Yes | Information about who or what triggered the task run. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

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
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}/runs',
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
# qlik-cli has not implemented support for GET /api/v1/tasks/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}/runs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "log": "string",
      "status": "RUNNING",
      "taskId": "string",
      "endedAt": "2018-10-30T07:06:22Z",
      "actionId": "string",
      "taskMeta": {
        "usage": "ANALYTICS",
        "ownerId": "string",
        "spaceId": "string",
        "trigger": {
          "id": "string",
          "type": 0
        },
        "tenantId": "string",
        "createdAt": "2018-10-30T07:06:22Z",
        "createdBy": "string",
        "deletedAt": "2018-10-30T07:06:22Z",
        "updatedAt": "2018-10-30T07:06:22Z",
        "disabledCode": "MANUALLY",
        "migratedFrom": "string",
        "orchestration": {
          "id": "string",
          "type": 0,
          "attrs": {}
        }
      },
      "taskName": "string",
      "workerId": "string",
      "startedAt": "2018-10-30T07:06:22Z",
      "executedAs": "string",
      "resourceId": "string",
      "workerType": "string",
      "triggeredBy": "manual"
    }
  ],
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

### GET /api/v1/tasks/{id}/runs/{runId}/log

Get specific run log of a task.

- **Replaced by:** "GET:/scheduling/tasks/{id}/runs/{runId}/log"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |
| `runId` | string | Yes | The run's unique identifier. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | The acceptable content types. Enum: "application/json", "text/plain" |

#### Responses

##### 200

OK Response

**Content-Type:** `text/plain`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `logContent` | string | No |  |

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `logContent` | string | No | Log content in plain text format |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks/{id}/runs/{runId}/log` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}/runs/{runId}/log',
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
# qlik-cli has not implemented support for GET /api/v1/tasks/{id}/runs/{runId}/log yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}/runs/{runId}/log" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```text
[object Object]
```

---

### GET /api/v1/tasks/{id}/runs/last

Returns the last run of a specific task.

- **Replaced by:** "GET:/scheduling/tasks/{id}/runs/last"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The task's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the task run |
| `log` | string | No | log info of the run |
| `status` | string | Yes | task run status Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `taskId` | string | Yes | The ID of the task |
| `endedAt` | string | No | The UTC timestamp when the task run ended |
| `actionId` | string | Yes | The ID of the action |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | task name |
| `workerId` | string | Yes | The ID of the worker who is carrying out the real job. e.g. App.Reload job is carried out by Reload Engine, in this case, workerId will be reloadId from reload engine. Or, if we are using Automation, workerId will be Automation runId. |
| `startedAt` | string | No | The UTC timestamp when the task run started |
| `executedAs` | string | No | user ID of on behalf of whom the Task was executed. |
| `resourceId` | string | Yes | The ID of the resource |
| `workerType` | string | Yes | worker type or target system |
| `triggeredBy` | string | Yes | Information about who or what triggered the task run. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the Trigger associated with the task in the choreographer |
| `type` | integer | Yes | trigger type Enum: 0, 1, 2, 3 |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the orchestration associated with the task in the choreographer |
| `type` | integer | Yes | orchestration system type Enum: 0, 1, 2, 3 |
| `attrs` | object | No |  |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks/{id}/runs/last` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/{id}/runs/last',
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
# qlik-cli has not implemented support for GET /api/v1/tasks/{id}/runs/last yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/{id}/runs/last" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "log": "string",
  "status": "RUNNING",
  "taskId": "string",
  "endedAt": "2018-10-30T07:06:22Z",
  "actionId": "string",
  "taskMeta": {
    "usage": "ANALYTICS",
    "ownerId": "string",
    "spaceId": "string",
    "trigger": {
      "id": "string",
      "type": 0
    },
    "tenantId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "string",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "orchestration": {
      "id": "string",
      "type": 0,
      "attrs": {}
    }
  },
  "taskName": "string",
  "workerId": "string",
  "startedAt": "2018-10-30T07:06:22Z",
  "executedAs": "string",
  "resourceId": "string",
  "workerType": "string",
  "triggeredBy": "manual"
}
```

---

### GET /api/v1/tasks/resources/{id}/runs

Returns a list of task runs for a specified `resourceId`.

- **Replaced by:** "GET:/scheduling/tasks/resources/{id}/runs"
- **Rate Limit:** Special (600 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Filter tasks by its target resource ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | The maximum number of task runs to return for a request. |
| `page` | string | No | The page cursor. |
| `sort` | string | No | The property of a resource to sort on (default sort is -startedAt). A property must be prefixed by + or - to indicate ascending or descending sort order respectively.  Enum: "+startedAt", "-startedAt", "+endedAt", "-endedAt", "+status", "-status", "+taskId", "-taskId", "+actionId", "-actionId" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the task run |
| `log` | string | No | log info of the run |
| `status` | string | Yes | task run status Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `taskId` | string | Yes | The ID of the task |
| `endedAt` | string | No | The UTC timestamp when the task run ended |
| `actionId` | string | Yes | The ID of the action |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | task name |
| `workerId` | string | Yes | The ID of the worker who is carrying out the real job. e.g. App.Reload job is carried out by Reload Engine, in this case, workerId will be reloadId from reload engine. Or, if we are using Automation, workerId will be Automation runId. |
| `startedAt` | string | No | The UTC timestamp when the task run started |
| `executedAs` | string | No | user ID of on behalf of whom the Task was executed. |
| `resourceId` | string | Yes | The ID of the resource |
| `workerType` | string | Yes | worker type or target system |
| `triggeredBy` | string | Yes | Information about who or what triggered the task run. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of `ANALYTICS` Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the owner of the task |
| `spaceId` | string | No | The space ID that the Task will operate in |
| `trigger` | object | No |  |
| `tenantId` | string | No | The tenant ID that the Task will operate in |
| `createdAt` | string | No | The UTC timestamp when the task was created |
| `createdBy` | string | No | The user ID of the user that created the task |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated |
| `disabledCode` | string | No | why the Task is disabled Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED" |
| `migratedFrom` | string | No | The ID of the reload-task this one was migrated from (if applicable) |
| `orchestration` | object | No |  |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

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
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

<details>
<summary>Properties of `inner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No |  |
| `inner` | object | No |  |
| `title` | string | No |  |
| `result` | any | No |  |
| `context` | string | No |  |
| `timestamp` | string | No |  |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tasks/resources/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tasks/resources/{id}/runs',
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
# qlik-cli has not implemented support for GET /api/v1/tasks/resources/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tasks/resources/{id}/runs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "log": "string",
      "status": "RUNNING",
      "taskId": "string",
      "endedAt": "2018-10-30T07:06:22Z",
      "actionId": "string",
      "taskMeta": {
        "usage": "ANALYTICS",
        "ownerId": "string",
        "spaceId": "string",
        "trigger": {
          "id": "string",
          "type": 0
        },
        "tenantId": "string",
        "createdAt": "2018-10-30T07:06:22Z",
        "createdBy": "string",
        "deletedAt": "2018-10-30T07:06:22Z",
        "updatedAt": "2018-10-30T07:06:22Z",
        "disabledCode": "MANUALLY",
        "migratedFrom": "string",
        "orchestration": {
          "id": "string",
          "type": 0,
          "attrs": {}
        }
      },
      "taskName": "string",
      "workerId": "string",
      "startedAt": "2018-10-30T07:06:22Z",
      "executedAs": "string",
      "resourceId": "string",
      "workerType": "string",
      "triggeredBy": "manual"
    }
  ],
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
