# Tasks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/scheduling/tasks`](#get-apischedulingtasks) | Retrieves a paginated list of tasks the requesting user has access to. Results include task metadata such as owner, resource, space, and last run status. Use the `filter` parameter to narrow results by field values, or `sort` to control the ordering. |
| `POST` | [`/api/scheduling/tasks`](#post-apischedulingtasks) | Creates a new task for the specified resource. The task is owned by the requesting user and is disabled by default until explicitly enabled. The `resourceId` is derived automatically from the task's state definitions and cannot be set directly in the request body. |
| `GET` | [`/api/scheduling/tasks/{id}`](#get-apischedulingtasksid) | Retrieves the full definition and metadata for a specific task, including its trigger configuration, state definitions, owner, and last run status. Use this operation to inspect a task before updating or starting it. |
| `PATCH` | [`/api/scheduling/tasks/{id}`](#patch-apischedulingtasksid) | Partially updates a specific task using a JSON Patch document (RFC 6902). Only the fields included in the patch operations are modified. All other fields remain unchanged. If the task is owned by another user, ownership is transferred to the requesting user. |
| `PUT` | [`/api/scheduling/tasks/{id}`](#put-apischedulingtasksid) | Replaces the full definition of a specific task with the supplied payload. All fields not included in the request body are reset to their defaults. If the task is owned by another user, ownership is transferred to the requesting user. Use `PATCH` instead to apply a partial update. |
| `DELETE` | [`/api/scheduling/tasks/{id}`](#delete-apischedulingtasksid) | Deletes a specific task and cancels any scheduled or pending runs associated with it. This action cannot be undone. Tenant admins can delete tasks owned by other users. |
| `POST` | [`/api/scheduling/tasks/{id}/actions/start`](#post-apischedulingtasksidactionsstart) | Triggers an immediate run of the specified task outside its normal schedule. The optional `source` parameter identifies what initiated the run, which is recorded in the run history for auditing purposes. |
| `GET` | [`/api/scheduling/tasks/{id}/graphs/ancestors`](#get-apischedulingtasksidgraphsancestors) | Retrieves the ancestor subgraph for a specific task, with the requested task as the root vertex. Traverses parent relationships breadth-first up to the depth specified by `level`. Use this to understand all upstream dependencies of a task. |
| `GET` | [`/api/scheduling/tasks/{id}/graphs/children`](#get-apischedulingtasksidgraphschildren) | Retrieves a paginated list of tasks that are direct children of the specified task in the dependency graph. A child task is one that is triggered when the parent task completes successfully. |
| `GET` | [`/api/scheduling/tasks/{id}/graphs/descendants`](#get-apischedulingtasksidgraphsdescendants) | Retrieves the descendant subgraph for a specific task, with the requested task as the root vertex. Traverses child relationships breadth-first down to the depth specified by `level`. Use this to identify all downstream tasks that will be triggered when this task completes. |
| `GET` | [`/api/scheduling/tasks/{id}/graphs/parents`](#get-apischedulingtasksidgraphsparents) | Retrieves a paginated list of tasks that are direct parents of the specified task in the dependency graph. A parent task is one whose completion triggers the current task. |
| `GET` | [`/api/scheduling/tasks/{id}/graphs/subgraph`](#get-apischedulingtasksidgraphssubgraph) | Retrieves the combined ancestor-and-descendant subgraph for a specific task, with the requested task as the root vertex. Traverses both parent and child relationships breadth-first up to the depth specified by `level`. Use this to see the full dependency context for a task in one request. |
| `GET` | [`/api/scheduling/tasks/{id}/runs`](#get-apischedulingtasksidruns) | Retrieves a paginated list of execution runs for the specified task, ordered by most recent run by default. Each run record includes the start and end time, status, and the identity that triggered it. |
| `GET` | [`/api/scheduling/tasks/{id}/runs/{runId}/log`](#get-apischedulingtasksidrunsrunidlog) | Retrieves the execution log for a specific task run. Set the `Accept` header to `text/plain` to receive the raw log as a downloadable file, or `application/json` (default) to receive it wrapped in a JSON object with a `logContent` field. |
| `GET` | [`/api/scheduling/tasks/{id}/runs/last`](#get-apischedulingtasksidrunslast) | Retrieves the most recent execution run for the specified task. Returns a 404 response if the task has never been run. Use this operation to quickly check whether the last run succeeded or failed without paginating through the full run history. |
| `GET` | [`/api/scheduling/tasks/resources/{id}/runs`](#get-apischedulingtasksresourcesidruns) | Retrieves a paginated list of task runs for a given resource, identified by `id`. Returns run history across all tasks associated with that resource, ordered by the most recent run by default. |

## API Reference

### GET /api/scheduling/tasks

Retrieves a paginated list of tasks the requesting user has access to. Results include task metadata such as owner, resource, space, and last run status. Use the `filter` parameter to narrow results by field values, or `sort` to control the ordering.

- **Replaces:** "GET:/v1/tasks"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Advanced filter expression using RFC 7644 SCIM syntax. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for syntax details. All comparisons are case-insensitive. Supported fields: `name`, `enabled`, `resourceId`, `ownerId`, `spaceId`, `createdAt`, `updatedAt`, `updatedBy`, `lastStatus`, `lastTriggeredBy`, `lastStartedAt`, `lastEndedAt`, `lastExecutedAs`, and `triggerType`. |
| `limit` | integer | No | Maximum number of tasks to return per page. |
| `page` | string | No | Cursor token for fetching the next page of results. |
| `resourceId` | string | No | The unique identifier of the resource to filter tasks by. |
| `sort` | string | No | Field and direction to sort results by. Prefix the field name with `+` for ascending or `-` for descending order. Defaults to `-updatedAt`.  Enum: "+createdAt", "-createdAt", "+enabled", "-enabled", "+name", "-name", "+ownerId", "-ownerId", "+resourceId", "-resourceId", "+spaceId", "-spaceId", "+updatedAt", "-updatedAt", "+updatedBy", "-updatedBy", "+lastStatus", "-lastStatus", "+lastTriggeredBy", "-lastTriggeredBy", "+lastStartedAt", "-lastStartedAt", "+lastEndedAt", "-lastEndedAt", "+lastExecutedAs", "-lastExecutedAs", "+triggerType", "-triggerType" |

#### Responses

##### 200

Tasks retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `timeouts`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

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
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "TaskExample",
      "events": [
        {
          "name": "event1",
          "type": "com.qlik/active-analytics-orch",
          "source": "dataset.updated",
          "correlation": [
            {
              "contextAttributeName": "appId",
              "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
          ]
        }
      ],
      "states": [
        {
          "end": true,
          "name": "Reload",
          "type": "event",
          "onEvents": [
            {
              "actions": [
                {
                  "name": "app.reload",
                  "functionRef": {
                    "refName": "app.reload",
                    "arguments": {
                      "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                      "partial": false
                    }
                  }
                }
              ],
              "eventRefs": [
                "app1-dataset-updated"
              ]
            }
          ],
          "exclusive": false
        }
      ],
      "enabled": true,
      "version": "1.0.0",
      "metadata": {
        "usage": "ANALYTICS",
        "ownerId": 0,
        "spaceId": "",
        "trigger": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 4
        },
        "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "createdAt": "2025-08-31T23:22:27.929Z",
        "createdBy": 0,
        "updatedAt": "2025-08-31T23:27:51.207Z",
        "orchestration": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 3,
          "attrs": {
            "last_run_status": "SUCCEEDED",
            "last_run_endedAt": "2025-08-31T23:28:06Z",
            "last_run_startedAt": "2025-08-31T23:28:04Z",
            "last_run_worker_type": "reloads"
          }
        }
      },
      "keepActive": false,
      "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "description": "this is an example of task response",
      "specVersion": "1.16.0"
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

### POST /api/scheduling/tasks

Creates a new task for the specified resource. The task is owned by the requesting user and is disabled by default until explicitly enabled. The `resourceId` is derived automatically from the task's state definitions and cannot be set directly in the request body.

- **Replaces:** "POST:/v1/tasks"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

Task created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `POST /api/scheduling/tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
      name: 'TaskExample',
      events: [
        {
          name: 'event1',
          type: 'com.qlik/active-analytics-orch',
          source: 'dataset.updated',
          correlation: [
            {
              contextAttributeName: 'appId',
              contextAttributeValue:
                'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
            },
          ],
        },
      ],
      states: [
        {
          end: true,
          name: 'Reload',
          type: 'event',
          onEvents: [
            {
              actions: [
                {
                  name: 'app.reload',
                  functionRef: {
                    refName: 'app.reload',
                    arguments: {
                      appId:
                        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                      partial: false,
                    },
                  },
                },
              ],
              eventRefs: ['app1-dataset-updated'],
            },
          ],
          exclusive: false,
        },
      ],
      enabled: true,
      version: '1.0.0',
      metadata: {
        usage: 'ANALYTICS',
        ownerId: 0,
        spaceId: '',
        trigger: {
          id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
          type: 4,
        },
        tenantId:
          'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        createdAt: '2025-08-31T23:22:27.929Z',
        createdBy: 0,
        updatedAt: '2025-08-31T23:27:51.207Z',
        orchestration: {
          id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
          type: 3,
          attrs: {
            last_run_status: 'SUCCEEDED',
            last_run_endedAt:
              '2025-08-31T23:28:06Z',
            last_run_startedAt:
              '2025-08-31T23:28:04Z',
            last_run_worker_type: 'reloads',
          },
        },
      },
      keepActive: false,
      resourceId:
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
      description:
        'this is an example of task response',
      specVersion: '1.16.0',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/scheduling/tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","name":"TaskExample","events":[{"name":"event1","type":"com.qlik/active-analytics-orch","source":"dataset.updated","correlation":[{"contextAttributeName":"appId","contextAttributeValue":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]}],"states":[{"end":true,"name":"Reload","type":"event","onEvents":[{"actions":[{"name":"app.reload","functionRef":{"refName":"app.reload","arguments":{"appId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","partial":false}}}],"eventRefs":["app1-dataset-updated"]}],"exclusive":false}],"enabled":true,"version":"1.0.0","metadata":{"usage":"ANALYTICS","ownerId":0,"spaceId":"","trigger":{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","type":4},"tenantId":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","createdAt":"2025-08-31T23:22:27.929Z","createdBy":0,"updatedAt":"2025-08-31T23:27:51.207Z","orchestration":{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","type":3,"attrs":{"last_run_status":"SUCCEEDED","last_run_endedAt":"2025-08-31T23:28:06Z","last_run_startedAt":"2025-08-31T23:28:04Z","last_run_worker_type":"reloads"}}},"keepActive":false,"resourceId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","description":"this is an example of task response","specVersion":"1.16.0"}'
```

**Example Response:**

```json
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "name": "TaskExample",
  "events": [
    {
      "name": "event1",
      "type": "com.qlik/active-analytics-orch",
      "source": "dataset.updated",
      "correlation": [
        {
          "contextAttributeName": "appId",
          "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "Reload",
      "type": "event",
      "onEvents": [
        {
          "actions": [
            {
              "name": "app.reload",
              "functionRef": {
                "refName": "app.reload",
                "arguments": {
                  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                  "partial": false
                }
              }
            }
          ],
          "eventRefs": [
            "app1-dataset-updated"
          ]
        }
      ],
      "exclusive": false
    }
  ],
  "enabled": true,
  "version": "1.0.0",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": 0,
    "spaceId": "",
    "trigger": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 4
    },
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "createdAt": "2025-08-31T23:22:27.929Z",
    "createdBy": 0,
    "updatedAt": "2025-08-31T23:27:51.207Z",
    "orchestration": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 3,
      "attrs": {
        "last_run_status": "SUCCEEDED",
        "last_run_endedAt": "2025-08-31T23:28:06Z",
        "last_run_startedAt": "2025-08-31T23:28:04Z",
        "last_run_worker_type": "reloads"
      }
    }
  },
  "keepActive": false,
  "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "description": "this is an example of task response",
  "specVersion": "1.16.0"
}
```

---

### GET /api/scheduling/tasks/{id}

Retrieves the full definition and metadata for a specific task, including its trigger configuration, state definitions, owner, and last run status. Use this operation to inspect a task before updating or starting it.

- **Replaces:** "GET:/v1/tasks/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task to retrieve. |

#### Responses

##### 200

Task details retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "name": "TaskExample",
  "events": [
    {
      "name": "event1",
      "type": "com.qlik/active-analytics-orch",
      "source": "dataset.updated",
      "correlation": [
        {
          "contextAttributeName": "appId",
          "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "Reload",
      "type": "event",
      "onEvents": [
        {
          "actions": [
            {
              "name": "app.reload",
              "functionRef": {
                "refName": "app.reload",
                "arguments": {
                  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                  "partial": false
                }
              }
            }
          ],
          "eventRefs": [
            "app1-dataset-updated"
          ]
        }
      ],
      "exclusive": false
    }
  ],
  "enabled": true,
  "version": "1.0.0",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": 0,
    "spaceId": "",
    "trigger": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 4
    },
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "createdAt": "2025-08-31T23:22:27.929Z",
    "createdBy": 0,
    "updatedAt": "2025-08-31T23:27:51.207Z",
    "orchestration": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 3,
      "attrs": {
        "last_run_status": "SUCCEEDED",
        "last_run_endedAt": "2025-08-31T23:28:06Z",
        "last_run_startedAt": "2025-08-31T23:28:04Z",
        "last_run_worker_type": "reloads"
      }
    }
  },
  "keepActive": false,
  "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "description": "this is an example of task response",
  "specVersion": "1.16.0"
}
```

---

### PATCH /api/scheduling/tasks/{id}

Partially updates a specific task using a JSON Patch document (RFC 6902). Only the fields included in the patch operations are modified. All other fields remain unchanged. If the task is owned by another user, ownership is transferred to the requesting user.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task to update. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The patch operation to perform. Enum: "add", "remove", "replace", "move", "copy" |
| `path` | string | Yes | A JSON Pointer (RFC 6901) identifying the field to patch. |
| `value` | string \| number \| integer \| boolean \| array \| object | No | The value to use in a JSON Patch operation. |

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
| `` | integer | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 5:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | undefined[] | No |  |

**Option 6:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

</details>

#### Responses

##### 200

Task updated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 204

Task updated with no content to return.

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `PATCH /api/scheduling/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: 'string',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/scheduling/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"string","value":"string"}]'
```

**Example Response:**

```json
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "name": "TaskExample",
  "events": [
    {
      "name": "event1",
      "type": "com.qlik/active-analytics-orch",
      "source": "dataset.updated",
      "correlation": [
        {
          "contextAttributeName": "appId",
          "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "Reload",
      "type": "event",
      "onEvents": [
        {
          "actions": [
            {
              "name": "app.reload",
              "functionRef": {
                "refName": "app.reload",
                "arguments": {
                  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                  "partial": false
                }
              }
            }
          ],
          "eventRefs": [
            "app1-dataset-updated"
          ]
        }
      ],
      "exclusive": false
    }
  ],
  "enabled": true,
  "version": "1.0.0",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": 0,
    "spaceId": "",
    "trigger": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 4
    },
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "createdAt": "2025-08-31T23:22:27.929Z",
    "createdBy": 0,
    "updatedAt": "2025-08-31T23:27:51.207Z",
    "orchestration": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 3,
      "attrs": {
        "last_run_status": "SUCCEEDED",
        "last_run_endedAt": "2025-08-31T23:28:06Z",
        "last_run_startedAt": "2025-08-31T23:28:04Z",
        "last_run_worker_type": "reloads"
      }
    }
  },
  "keepActive": false,
  "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "description": "this is an example of task response",
  "specVersion": "1.16.0"
}
```

---

### PUT /api/scheduling/tasks/{id}

Replaces the full definition of a specific task with the supplied payload. All fields not included in the request body are reset to their defaults. If the task is owned by another user, ownership is transferred to the requesting user. Use `PATCH` instead to apply a partial update.

- **Replaces:** "PUT:/v1/tasks/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task to replace. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 200

Task replaced successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | string \| object | Yes |  |
| `stateName` | string | No | The name of the starting workflow state. |

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
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contextAttributeName` | string | Yes | The name of the CloudEvent extension context attribute to match on. Enum: "id", "status", "appId", "spaceId", "datasetId" |
| `contextAttributeValue` | string | No | The expected value of the CloudEvent extension context attribute. |

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | object[] | No | Actions to perform when the matched events are consumed. |
| `eventRefs` | string[] | Yes | References to one or more unique event names defined in the workflow events list. |
| `actionMode` | string | No | Specifies whether actions are performed sequentially or in parallel. Enum: "SEQUENTIAL", "PARALLEL" |

<details>
<summary>Properties of `actions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `timeouts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventTimeout` | string | No | The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `stateExecTimeout` | string | No | The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one. |
| `actionExecTimeout` | string | No | The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one. |

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

##### 409

The request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `PUT /api/scheduling/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
      name: 'TaskExample',
      events: [
        {
          name: 'event1',
          type: 'com.qlik/active-analytics-orch',
          source: 'dataset.updated',
          correlation: [
            {
              contextAttributeName: 'appId',
              contextAttributeValue:
                'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
            },
          ],
        },
      ],
      states: [
        {
          end: true,
          name: 'Reload',
          type: 'event',
          onEvents: [
            {
              actions: [
                {
                  name: 'app.reload',
                  functionRef: {
                    refName: 'app.reload',
                    arguments: {
                      appId:
                        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                      partial: false,
                    },
                  },
                },
              ],
              eventRefs: ['app1-dataset-updated'],
            },
          ],
          exclusive: false,
        },
      ],
      enabled: true,
      version: '1.0.0',
      metadata: {
        usage: 'ANALYTICS',
        ownerId: 0,
        spaceId: '',
        trigger: {
          id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
          type: 4,
        },
        tenantId:
          'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        createdAt: '2025-08-31T23:22:27.929Z',
        createdBy: 0,
        updatedAt: '2025-08-31T23:27:51.207Z',
        orchestration: {
          id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
          type: 3,
          attrs: {
            last_run_status: 'SUCCEEDED',
            last_run_endedAt:
              '2025-08-31T23:28:06Z',
            last_run_startedAt:
              '2025-08-31T23:28:04Z',
            last_run_worker_type: 'reloads',
          },
        },
      },
      keepActive: false,
      resourceId:
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
      description:
        'this is an example of task response',
      specVersion: '1.16.0',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/scheduling/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","name":"TaskExample","events":[{"name":"event1","type":"com.qlik/active-analytics-orch","source":"dataset.updated","correlation":[{"contextAttributeName":"appId","contextAttributeValue":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]}],"states":[{"end":true,"name":"Reload","type":"event","onEvents":[{"actions":[{"name":"app.reload","functionRef":{"refName":"app.reload","arguments":{"appId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","partial":false}}}],"eventRefs":["app1-dataset-updated"]}],"exclusive":false}],"enabled":true,"version":"1.0.0","metadata":{"usage":"ANALYTICS","ownerId":0,"spaceId":"","trigger":{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","type":4},"tenantId":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","createdAt":"2025-08-31T23:22:27.929Z","createdBy":0,"updatedAt":"2025-08-31T23:27:51.207Z","orchestration":{"id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","type":3,"attrs":{"last_run_status":"SUCCEEDED","last_run_endedAt":"2025-08-31T23:28:06Z","last_run_startedAt":"2025-08-31T23:28:04Z","last_run_worker_type":"reloads"}}},"keepActive":false,"resourceId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","description":"this is an example of task response","specVersion":"1.16.0"}'
```

**Example Response:**

```json
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "name": "TaskExample",
  "events": [
    {
      "name": "event1",
      "type": "com.qlik/active-analytics-orch",
      "source": "dataset.updated",
      "correlation": [
        {
          "contextAttributeName": "appId",
          "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
      ]
    }
  ],
  "states": [
    {
      "end": true,
      "name": "Reload",
      "type": "event",
      "onEvents": [
        {
          "actions": [
            {
              "name": "app.reload",
              "functionRef": {
                "refName": "app.reload",
                "arguments": {
                  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                  "partial": false
                }
              }
            }
          ],
          "eventRefs": [
            "app1-dataset-updated"
          ]
        }
      ],
      "exclusive": false
    }
  ],
  "enabled": true,
  "version": "1.0.0",
  "metadata": {
    "usage": "ANALYTICS",
    "ownerId": 0,
    "spaceId": "",
    "trigger": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 4
    },
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "createdAt": "2025-08-31T23:22:27.929Z",
    "createdBy": 0,
    "updatedAt": "2025-08-31T23:27:51.207Z",
    "orchestration": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": 3,
      "attrs": {
        "last_run_status": "SUCCEEDED",
        "last_run_endedAt": "2025-08-31T23:28:06Z",
        "last_run_startedAt": "2025-08-31T23:28:04Z",
        "last_run_worker_type": "reloads"
      }
    }
  },
  "keepActive": false,
  "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "description": "this is an example of task response",
  "specVersion": "1.16.0"
}
```

---

### DELETE /api/scheduling/tasks/{id}

Deletes a specific task and cancels any scheduled or pending runs associated with it. This action cannot be undone. Tenant admins can delete tasks owned by other users.

- **Replaces:** "DELETE:/v1/tasks/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task to delete. |

#### Responses

##### 204

Task deleted successfully.

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `DELETE /api/scheduling/tasks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}',
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
# qlik-cli has not implemented support for DELETE /api/scheduling/tasks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/scheduling/tasks/{id}/actions/start

Triggers an immediate run of the specified task outside its normal schedule. The optional `source` parameter identifies what initiated the run, which is recorded in the run history for auditing purposes.

- **Replaces:** "POST:/v1/tasks/{id}/actions/start"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task to start. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | No | The origin of the trigger. Defaults to `manual`. For event-triggered tasks, this can be the name of the triggering task. |

#### Responses

##### 200

Task started successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No |  |

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `POST /api/scheduling/tasks/{id}/actions/start` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/actions/start',
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
# qlik-cli has not implemented support for POST /api/scheduling/tasks/{id}/actions/start yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/actions/start" \
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

### GET /api/scheduling/tasks/{id}/graphs/ancestors

Retrieves the ancestor subgraph for a specific task, with the requested task as the root vertex. Traverses parent relationships breadth-first up to the depth specified by `level`. Use this to understand all upstream dependencies of a task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `level` | integer | No | Maximum ancestor depth to traverse breadth-first. |
| `withTask` | boolean | No | When `true`, includes the full task document for each accessible vertex in the response. |

#### Responses

##### 200

Ancestor graph retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `edges` | object[] | No |  |
| `taskId` | string | No |  |
| `vertices` | object[] | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attrs` | object | No |  |
| `source` | string | No |  |
| `target` | string | No |  |

</details>

<details>
<summary>Properties of `vertices`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task` | object | No |  |
| `attrs` | object | No |  |
| `taskId` | string | No |  |

<details>
<summary>Properties of `task`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `events`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `states`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/graphs/ancestors` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/graphs/ancestors',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/graphs/ancestors yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/graphs/ancestors" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "edges": [
    {
      "attrs": {
        "depth": 1
      },
      "source": "22222222-2222-2222-2222-222222222222",
      "target": "11111111-1111-1111-1111-111111111111"
    }
  ],
  "taskId": "11111111-1111-1111-1111-111111111111",
  "vertices": [
    {
      "attrs": {
        "depth": 0,
        "isChild": false,
        "isParent": true
      },
      "taskId": "11111111-1111-1111-1111-111111111111"
    },
    {
      "attrs": {
        "depth": 1,
        "isChild": true,
        "isParent": false
      },
      "taskId": "22222222-2222-2222-2222-222222222222"
    }
  ]
}
```

---

### GET /api/scheduling/tasks/{id}/graphs/children

Retrieves a paginated list of tasks that are direct children of the specified task in the dependency graph. A child task is one that is triggered when the parent task completes successfully.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the parent task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Advanced filter expression using RFC 7644 SCIM syntax. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for syntax details. All comparisons are case-insensitive. Supported fields: `name`, `enabled`, `resourceId`, `ownerId`, `spaceId`, `createdAt`, `updatedAt`, `updatedBy`, `lastStatus`, `lastTriggeredBy`, `lastStartedAt`, `lastEndedAt`, `lastExecutedAs`, and `triggerType`. |
| `limit` | integer | No | Maximum number of tasks to return per page. |
| `page` | string | No | Cursor token for fetching the next page of results. |
| `sort` | string | No | Field and direction to sort results by. Prefix the field name with `+` for ascending or `-` for descending order. Defaults to `-updatedAt`.  Enum: "+createdAt", "-createdAt", "+enabled", "-enabled", "+name", "-name", "+ownerId", "-ownerId", "+resourceId", "-resourceId", "+spaceId", "-spaceId", "+updatedAt", "-updatedAt", "+updatedBy", "-updatedBy", "+lastStatus", "-lastStatus", "+lastTriggeredBy", "-lastTriggeredBy", "+lastStartedAt", "-lastStartedAt", "+lastEndedAt", "-lastEndedAt", "+lastExecutedAs", "-lastExecutedAs", "+triggerType", "-triggerType" |

#### Responses

##### 200

Child tasks retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `timeouts`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

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
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/graphs/children` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/graphs/children',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/graphs/children yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/graphs/children" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "TaskExample",
      "events": [
        {
          "name": "event1",
          "type": "com.qlik/active-analytics-orch",
          "source": "dataset.updated",
          "correlation": [
            {
              "contextAttributeName": "appId",
              "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
          ]
        }
      ],
      "states": [
        {
          "end": true,
          "name": "Reload",
          "type": "event",
          "onEvents": [
            {
              "actions": [
                {
                  "name": "app.reload",
                  "functionRef": {
                    "refName": "app.reload",
                    "arguments": {
                      "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                      "partial": false
                    }
                  }
                }
              ],
              "eventRefs": [
                "app1-dataset-updated"
              ]
            }
          ],
          "exclusive": false
        }
      ],
      "enabled": true,
      "version": "1.0.0",
      "metadata": {
        "usage": "ANALYTICS",
        "ownerId": 0,
        "spaceId": "",
        "trigger": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 4
        },
        "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "createdAt": "2025-08-31T23:22:27.929Z",
        "createdBy": 0,
        "updatedAt": "2025-08-31T23:27:51.207Z",
        "orchestration": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 3,
          "attrs": {
            "last_run_status": "SUCCEEDED",
            "last_run_endedAt": "2025-08-31T23:28:06Z",
            "last_run_startedAt": "2025-08-31T23:28:04Z",
            "last_run_worker_type": "reloads"
          }
        }
      },
      "keepActive": false,
      "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "description": "this is an example of task response",
      "specVersion": "1.16.0"
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

### GET /api/scheduling/tasks/{id}/graphs/descendants

Retrieves the descendant subgraph for a specific task, with the requested task as the root vertex. Traverses child relationships breadth-first down to the depth specified by `level`. Use this to identify all downstream tasks that will be triggered when this task completes.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `level` | integer | No | Maximum descendant depth to traverse breadth-first. |
| `withTask` | boolean | No | When `true`, includes the full task document for each accessible vertex in the response. |

#### Responses

##### 200

Descendant graph retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `edges` | object[] | No |  |
| `taskId` | string | No |  |
| `vertices` | object[] | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attrs` | object | No |  |
| `source` | string | No |  |
| `target` | string | No |  |

</details>

<details>
<summary>Properties of `vertices`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task` | object | No |  |
| `attrs` | object | No |  |
| `taskId` | string | No |  |

<details>
<summary>Properties of `task`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `events`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `states`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/graphs/descendants` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/graphs/descendants',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/graphs/descendants yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/graphs/descendants" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "edges": [
    {
      "attrs": {
        "depth": 1
      },
      "source": "22222222-2222-2222-2222-222222222222",
      "target": "11111111-1111-1111-1111-111111111111"
    }
  ],
  "taskId": "11111111-1111-1111-1111-111111111111",
  "vertices": [
    {
      "attrs": {
        "depth": 0,
        "isChild": false,
        "isParent": true
      },
      "taskId": "11111111-1111-1111-1111-111111111111"
    },
    {
      "attrs": {
        "depth": 1,
        "isChild": true,
        "isParent": false
      },
      "taskId": "22222222-2222-2222-2222-222222222222"
    }
  ]
}
```

---

### GET /api/scheduling/tasks/{id}/graphs/parents

Retrieves a paginated list of tasks that are direct parents of the specified task in the dependency graph. A parent task is one whose completion triggers the current task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the child task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | Advanced filter expression using RFC 7644 SCIM syntax. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for syntax details. All comparisons are case-insensitive. Supported fields: `name`, `enabled`, `resourceId`, `ownerId`, `spaceId`, `createdAt`, `updatedAt`, `updatedBy`, `lastStatus`, `lastTriggeredBy`, `lastStartedAt`, `lastEndedAt`, `lastExecutedAs`, and `triggerType`. |
| `limit` | integer | No | Maximum number of tasks to return per page. |
| `page` | string | No | Cursor token for fetching the next page of results. |
| `sort` | string | No | Field and direction to sort results by. Prefix the field name with `+` for ascending or `-` for descending order. Defaults to `-updatedAt`.  Enum: "+createdAt", "-createdAt", "+enabled", "-enabled", "+name", "-name", "+ownerId", "-ownerId", "+resourceId", "-resourceId", "+spaceId", "-spaceId", "+updatedAt", "-updatedAt", "+updatedBy", "-updatedBy", "+lastStatus", "-lastStatus", "+lastTriggeredBy", "-lastTriggeredBy", "+lastStartedAt", "-lastStartedAt", "+lastEndedAt", "-lastEndedAt", "+lastExecutedAs", "-lastExecutedAs", "+triggerType", "-triggerType" |

#### Responses

##### 200

Parent tasks retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | A scheduled workflow start definition. |

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | A unique name identifying this event definition within the workflow. |
| `type` | string | No | The CloudEvents type attribute identifying the kind of event. Enum: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch" |
| `source` | string | No | The CloudEvents source attribute identifying the origin of the event. Enum: "system-events.task", "dataset.updated" |
| `dataOnly` | boolean | No | When `true`, only the event payload is accessible to consuming workflow states. When `false`, both the payload and context attributes are accessible. |
| `correlation` | object[] | No | Correlation definitions used to match incoming CloudEvents to this workflow instance. |

<details>
<summary>Properties of `correlation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `states`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `end` | boolean | No | Marks this state as a terminal state in the workflow. |
| `name` | string | No | The name of this state, unique within the workflow. |
| `type` | string | No | The state type. Must be `EVENT` for event-driven states. Enum: "EVENT" |
| `onEvents` | object[] | No | The events to consume and the optional actions to perform when they are received. |
| `timeouts` | object | No | State-specific timeout durations. |
| `exclusive` | boolean | No | When `true`, consuming any one of the defined events causes its associated actions to execute. When `false`, all defined events must be consumed before actions are performed. |
| `compensatedBy` | string | No | The unique name of a workflow state responsible for compensating this state if it fails. |

<details>
<summary>Properties of `onEvents`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `timeouts`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

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
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/graphs/parents` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/graphs/parents',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/graphs/parents yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/graphs/parents" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "TaskExample",
      "events": [
        {
          "name": "event1",
          "type": "com.qlik/active-analytics-orch",
          "source": "dataset.updated",
          "correlation": [
            {
              "contextAttributeName": "appId",
              "contextAttributeValue": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
          ]
        }
      ],
      "states": [
        {
          "end": true,
          "name": "Reload",
          "type": "event",
          "onEvents": [
            {
              "actions": [
                {
                  "name": "app.reload",
                  "functionRef": {
                    "refName": "app.reload",
                    "arguments": {
                      "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                      "partial": false
                    }
                  }
                }
              ],
              "eventRefs": [
                "app1-dataset-updated"
              ]
            }
          ],
          "exclusive": false
        }
      ],
      "enabled": true,
      "version": "1.0.0",
      "metadata": {
        "usage": "ANALYTICS",
        "ownerId": 0,
        "spaceId": "",
        "trigger": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 4
        },
        "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "createdAt": "2025-08-31T23:22:27.929Z",
        "createdBy": 0,
        "updatedAt": "2025-08-31T23:27:51.207Z",
        "orchestration": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "type": 3,
          "attrs": {
            "last_run_status": "SUCCEEDED",
            "last_run_endedAt": "2025-08-31T23:28:06Z",
            "last_run_startedAt": "2025-08-31T23:28:04Z",
            "last_run_worker_type": "reloads"
          }
        }
      },
      "keepActive": false,
      "resourceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "description": "this is an example of task response",
      "specVersion": "1.16.0"
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

### GET /api/scheduling/tasks/{id}/graphs/subgraph

Retrieves the combined ancestor-and-descendant subgraph for a specific task, with the requested task as the root vertex. Traverses both parent and child relationships breadth-first up to the depth specified by `level`. Use this to see the full dependency context for a task in one request.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `level` | integer | No | Maximum ancestor and descendant depth to traverse breadth-first. |
| `withTask` | boolean | No | When `true`, includes the full task document for each accessible vertex in the response. |

#### Responses

##### 200

Task subgraph retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `edges` | object[] | No |  |
| `taskId` | string | No |  |
| `vertices` | object[] | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attrs` | object | No |  |
| `source` | string | No |  |
| `target` | string | No |  |

</details>

<details>
<summary>Properties of `vertices`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task` | object | No |  |
| `attrs` | object | No |  |
| `taskId` | string | No |  |

<details>
<summary>Properties of `task`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier assigned to the task by the service. |
| `key` | string | No | An optional expression used to generate a domain-specific workflow instance identifier. |
| `name` | string | Yes | The name that identifies the workflow definition. Combined with `version`, the name forms a unique identifier for the task. |
| `start` | object | No | The start definition for a workflow, including optional schedule configuration. |
| `events` | object[] | No | CloudEvent definitions for the workflow. Defines the events that can be consumed or produced by the workflow. |
| `states` | object[] | No | The list of state definitions that compose the workflow. |
| `enabled` | boolean | No | Indicates whether the task is enabled. Disabled tasks will not trigger automatically. |
| `version` | string | No | The semantic version of the workflow definition. |
| `metadata` | object | No |  |
| `keepActive` | boolean | No | When `true`, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured `workflowExecTimeout`. |
| `resourceId` | string | No | The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from `states`. |
| `annotations` | string[] | No | A list of terms describing the workflow's intended purpose, subject areas, or other important qualities. |
| `description` | string | No | A human-readable description of the workflow's purpose. |
| `specVersion` | string | Yes | The Serverless Workflow specification version used by this task. |

<details>
<summary>Properties of `start`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `events`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `states`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/graphs/subgraph` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/graphs/subgraph',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/graphs/subgraph yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/graphs/subgraph" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "edges": [
    {
      "attrs": {
        "depth": 1
      },
      "source": "22222222-2222-2222-2222-222222222222",
      "target": "11111111-1111-1111-1111-111111111111"
    }
  ],
  "taskId": "11111111-1111-1111-1111-111111111111",
  "vertices": [
    {
      "attrs": {
        "depth": 0,
        "isChild": false,
        "isParent": true
      },
      "taskId": "11111111-1111-1111-1111-111111111111"
    },
    {
      "attrs": {
        "depth": 1,
        "isChild": true,
        "isParent": false
      },
      "taskId": "22222222-2222-2222-2222-222222222222"
    }
  ]
}
```

---

### GET /api/scheduling/tasks/{id}/runs

Retrieves a paginated list of execution runs for the specified task, ordered by most recent run by default. Each run record includes the start and end time, status, and the identity that triggered it.

- **Replaces:** "GET:/v1/tasks/{id}/runs"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Maximum number of task runs to return per page. |
| `page` | string | No | Cursor token for fetching the next page of results. |
| `sort` | string | No | Field and direction to sort results by. Prefix the field name with `+` for ascending or `-` for descending order. Defaults to `-startedAt`.  Enum: "+startedAt", "-startedAt", "+endedAt", "-endedAt", "+status", "-status", "+taskId", "-taskId", "+actionId", "-actionId" |

#### Responses

##### 200

Task runs retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task run. |
| `status` | string | Yes | The current status of the task run. Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `endedAt` | string | No | The UTC timestamp when the task run ended. |
| `workerId` | string | Yes | The unique identifier of the worker that executed the job. For example, a reload run carries the reload ID from the engine, and an automation run carries the automation run ID. |
| `startedAt` | string | No | The UTC timestamp when the task run started. |
| `executedAs` | string | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | string | Yes | The type or name of the target system that executed the run. |
| `triggeredBy` | string | Yes | The identity or event that triggered the task run. |
| `log` | string | No | The raw log output from the task run. |
| `taskId` | string | Yes | The unique identifier of the task. |
| `actionId` | string | Yes | The unique identifier of the action that was executed. |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | The name of the task at the time it was run. |
| `resourceId` | string | Yes | The unique identifier of the resource the task operated on. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

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
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/runs',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/runs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
      "status": "SUCCEEDED",
      "endedAt": "2018-03-20T09:12:28Z",
      "workerId": "550e8400-e29b-41d4-a716-446655440000",
      "startedAt": "2018-03-20T09:12:28Z",
      "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
      "workerType": "reloads",
      "triggeredBy": "manual",
      "log": "string",
      "taskId": "string",
      "actionId": "string",
      "taskMeta": {
        "usage": "ANALYTICS",
        "ownerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
        "spaceId": "434f9f7c-4eeb-43f0-8f08-88b91f357c07",
        "trigger": {
          "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
          "type": 1
        },
        "tenantId": "rpxzti_ptV0RS4eGPSsaI0SCKl-6h2a",
        "topology": {
          "isChild": false,
          "isParent": true
        },
        "createdAt": "2018-03-20T09:12:28Z",
        "createdBy": "LP_LlaXYhUUWMr5csy8pFfTHecXePH5Z",
        "deletedAt": "2018-03-20T09:12:28Z",
        "spaceType": "shared",
        "updatedAt": "2018-03-20T09:12:28Z",
        "disabledCode": "MANUALLY",
        "migratedFrom": "c7dba73-dd5a-4725-9dd2-8bd9c8d126d7",
        "resourceName": "sample app",
        "resourceType": "app",
        "orchestration": {
          "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
          "type": 3,
          "attrs": {
            "last_run_status": "SUCCEEDED",
            "last_run_worker_type": "reloads"
          },
          "lastRun": {
            "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
            "status": "SUCCEEDED",
            "endedAt": "2018-03-20T09:12:28Z",
            "workerId": "550e8400-e29b-41d4-a716-446655440000",
            "startedAt": "2018-03-20T09:12:28Z",
            "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
            "workerType": "reloads",
            "triggeredBy": "manual"
          }
        },
        "scriptOwnerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
        "resourceSubType": "script"
      },
      "taskName": "string",
      "resourceId": "string"
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

### GET /api/scheduling/tasks/{id}/runs/{runId}/log

Retrieves the execution log for a specific task run. Set the `Accept` header to `text/plain` to receive the raw log as a downloadable file, or `application/json` (default) to receive it wrapped in a JSON object with a `logContent` field.

- **Replaces:** "GET:/v1/tasks/{id}/runs/{runId}/log"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |
| `runId` | string | Yes | The unique identifier of the task run. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | The preferred response format for the log content. Enum: "application/json", "text/plain" |

#### Responses

##### 200

Task run log retrieved successfully.

**Content-Type:** `text/plain`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `logContent` | string | No |  |

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `logContent` | string | No | Log content in plain text format. |

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/runs/{runId}/log` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/runs/{runId}/log',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/runs/{runId}/log yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/runs/{runId}/log" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```text
[object Object]
```

---

### GET /api/scheduling/tasks/{id}/runs/last

Retrieves the most recent execution run for the specified task. Returns a 404 response if the task has never been run. Use this operation to quickly check whether the last run succeeded or failed without paginating through the full run history.

- **Replaces:** "GET:/v1/tasks/{id}/runs/last"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task. |

#### Responses

##### 200

Last task run retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task run. |
| `status` | string | Yes | The current status of the task run. Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `endedAt` | string | No | The UTC timestamp when the task run ended. |
| `workerId` | string | Yes | The unique identifier of the worker that executed the job. For example, a reload run carries the reload ID from the engine, and an automation run carries the automation run ID. |
| `startedAt` | string | No | The UTC timestamp when the task run started. |
| `executedAs` | string | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | string | Yes | The type or name of the target system that executed the run. |
| `triggeredBy` | string | Yes | The identity or event that triggered the task run. |
| `log` | string | No | The raw log output from the task run. |
| `taskId` | string | Yes | The unique identifier of the task. |
| `actionId` | string | Yes | The unique identifier of the action that was executed. |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | The name of the task at the time it was run. |
| `resourceId` | string | Yes | The unique identifier of the resource the task operated on. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the trigger associated with this task. |
| `type` | integer | Yes | The type identifier of the trigger associated with this task. Enum: 0, 1, 2, 3, 4 |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | boolean | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | boolean | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | integer | Yes | The type identifier of the orchestration system handling this task. Enum: 0, 1, 2, 3 |
| `attrs` | object | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | object | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/{id}/runs/last` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/{id}/runs/last',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/{id}/runs/last yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/{id}/runs/last" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
  "status": "SUCCEEDED",
  "endedAt": "2018-03-20T09:12:28Z",
  "workerId": "550e8400-e29b-41d4-a716-446655440000",
  "startedAt": "2018-03-20T09:12:28Z",
  "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
  "workerType": "reloads",
  "triggeredBy": "manual",
  "log": "string",
  "taskId": "string",
  "actionId": "string",
  "taskMeta": {
    "usage": "ANALYTICS",
    "ownerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
    "spaceId": "434f9f7c-4eeb-43f0-8f08-88b91f357c07",
    "trigger": {
      "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
      "type": 1
    },
    "tenantId": "rpxzti_ptV0RS4eGPSsaI0SCKl-6h2a",
    "topology": {
      "isChild": false,
      "isParent": true
    },
    "createdAt": "2018-03-20T09:12:28Z",
    "createdBy": "LP_LlaXYhUUWMr5csy8pFfTHecXePH5Z",
    "deletedAt": "2018-03-20T09:12:28Z",
    "spaceType": "shared",
    "updatedAt": "2018-03-20T09:12:28Z",
    "disabledCode": "MANUALLY",
    "migratedFrom": "c7dba73-dd5a-4725-9dd2-8bd9c8d126d7",
    "resourceName": "sample app",
    "resourceType": "app",
    "orchestration": {
      "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
      "type": 3,
      "attrs": {
        "last_run_status": "SUCCEEDED",
        "last_run_worker_type": "reloads"
      },
      "lastRun": {
        "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
        "status": "SUCCEEDED",
        "endedAt": "2018-03-20T09:12:28Z",
        "workerId": "550e8400-e29b-41d4-a716-446655440000",
        "startedAt": "2018-03-20T09:12:28Z",
        "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
        "workerType": "reloads",
        "triggeredBy": "manual"
      }
    },
    "scriptOwnerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
    "resourceSubType": "script"
  },
  "taskName": "string",
  "resourceId": "string"
}
```

---

### GET /api/scheduling/tasks/resources/{id}/runs

Retrieves a paginated list of task runs for a given resource, identified by `id`. Returns run history across all tasks associated with that resource, ordered by the most recent run by default.

- **Replaces:** "GET:/v1/tasks/resources/{id}/runs"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the resource to retrieve task runs for. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Maximum number of task runs to return per page. |
| `page` | string | No | Cursor token for fetching the next page of results. |
| `sort` | string | No | Field and direction to sort results by. Prefix the field name with `+` for ascending or `-` for descending order. Defaults to `-startedAt`.  Enum: "+startedAt", "-startedAt", "+endedAt", "-endedAt", "+status", "-status", "+taskId", "-taskId", "+actionId", "-actionId" |

#### Responses

##### 200

Task runs retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the task run. |
| `status` | string | Yes | The current status of the task run. Enum: "RUNNING", "SUCCEEDED", "FAILED" |
| `endedAt` | string | No | The UTC timestamp when the task run ended. |
| `workerId` | string | Yes | The unique identifier of the worker that executed the job. For example, a reload run carries the reload ID from the engine, and an automation run carries the automation run ID. |
| `startedAt` | string | No | The UTC timestamp when the task run started. |
| `executedAs` | string | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | string | Yes | The type or name of the target system that executed the run. |
| `triggeredBy` | string | Yes | The identity or event that triggered the task run. |
| `log` | string | No | The raw log output from the task run. |
| `taskId` | string | Yes | The unique identifier of the task. |
| `actionId` | string | Yes | The unique identifier of the action that was executed. |
| `taskMeta` | object | Yes |  |
| `taskName` | string | Yes | The name of the task at the time it was run. |
| `resourceId` | string | Yes | The unique identifier of the resource the task operated on. |

<details>
<summary>Properties of `taskMeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | The product domain in which the resource is used. Defaults to `ANALYTICS` when not present. Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP" |
| `ownerId` | string | No | The user ID of the task owner. |
| `spaceId` | string | No | The unique identifier of the space the task operates in. |
| `trigger` | object | No |  |
| `tenantId` | string | No | The unique identifier of the tenant the task operates in. |
| `topology` | object | No | Indicates the task's position in a dependency graph. |
| `createdAt` | string | No | The UTC timestamp when the task was created. |
| `createdBy` | string | No | The user ID of the user who created the task. |
| `deletedAt` | string | No | The UTC timestamp when the task was deleted. |
| `spaceType` | string | No | The type of space the task operates in. Enum: "personal", "shared", "managed" |
| `updatedAt` | string | No | The UTC timestamp when the task was last updated. |
| `disabledCode` | string | No | The reason the task is currently disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE", "OWNER-MOVED" |
| `migratedFrom` | string | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | string | No | The name of the resource on which the task was created. |
| `resourceType` | string | No | The type of resource on which the task was created. |
| `orchestration` | object | No |  |
| `scriptOwnerId` | string | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | string | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

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
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL of the linked resource. |

</details>

</details>

##### 400

The request is malformed or contains invalid parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Authentication credentials are missing or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

Access denied. You lack permission to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

An unexpected error occurred on the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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

The service is temporarily unavailable. Retry the request after a short delay.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A trace identifier for correlating the error to a specific service request. |

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
// qlik-api has not implemented support for `GET /api/scheduling/tasks/resources/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/scheduling/tasks/resources/{id}/runs',
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
# qlik-cli has not implemented support for GET /api/scheduling/tasks/resources/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks/resources/{id}/runs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
      "status": "SUCCEEDED",
      "endedAt": "2018-03-20T09:12:28Z",
      "workerId": "550e8400-e29b-41d4-a716-446655440000",
      "startedAt": "2018-03-20T09:12:28Z",
      "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
      "workerType": "reloads",
      "triggeredBy": "manual",
      "log": "string",
      "taskId": "string",
      "actionId": "string",
      "taskMeta": {
        "usage": "ANALYTICS",
        "ownerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
        "spaceId": "434f9f7c-4eeb-43f0-8f08-88b91f357c07",
        "trigger": {
          "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
          "type": 1
        },
        "tenantId": "rpxzti_ptV0RS4eGPSsaI0SCKl-6h2a",
        "topology": {
          "isChild": false,
          "isParent": true
        },
        "createdAt": "2018-03-20T09:12:28Z",
        "createdBy": "LP_LlaXYhUUWMr5csy8pFfTHecXePH5Z",
        "deletedAt": "2018-03-20T09:12:28Z",
        "spaceType": "shared",
        "updatedAt": "2018-03-20T09:12:28Z",
        "disabledCode": "MANUALLY",
        "migratedFrom": "c7dba73-dd5a-4725-9dd2-8bd9c8d126d7",
        "resourceName": "sample app",
        "resourceType": "app",
        "orchestration": {
          "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
          "type": 3,
          "attrs": {
            "last_run_status": "SUCCEEDED",
            "last_run_worker_type": "reloads"
          },
          "lastRun": {
            "id": "0c42b269-51d4-453a-a8ea-55734d209aa9",
            "status": "SUCCEEDED",
            "endedAt": "2018-03-20T09:12:28Z",
            "workerId": "550e8400-e29b-41d4-a716-446655440000",
            "startedAt": "2018-03-20T09:12:28Z",
            "executedAs": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
            "workerType": "reloads",
            "triggeredBy": "manual"
          }
        },
        "scriptOwnerId": "z1w_5hWRq-wIxXON_slIRrsF0YxpYjA",
        "resourceSubType": "script"
      },
      "taskName": "string",
      "resourceId": "string"
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
