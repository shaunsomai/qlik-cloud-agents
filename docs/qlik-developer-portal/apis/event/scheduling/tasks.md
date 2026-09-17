---
source: https://qlik.dev/apis/event/scheduling/tasks/
last_updated: 2026-06-18T10:30:42+01:00
---

# Tasks

## Table of Contents

### system-events.task

- [com.qlik.scheduling.task.created](#comqlikschedulingtaskcreated)
- [com.qlik.scheduling.task.deleted](#comqlikschedulingtaskdeleted)
- [com.qlik.scheduling.task.updated](#comqlikschedulingtaskupdated)

## Events published on the `system-events.task` channel

### com.qlik.scheduling.task.created

**Title:** Task created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new task is created. The event includes the task ID, owner, associated resource, and the scheduled action.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |
| `eventType` | `string` | No | Unique identifier for the event type. Allowed values: com.qlik.scheduling.task.created. |
| `extensions` | `cloudEventsQlikExtensionsAttributes` | No | Additional event metadata. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `usage` | `string` | No | The product domain in which the associated resource is used, such as `ANALYTICS` or `DATA_PREPARATION`. Defaults to `ANALYTICS` when not specified. Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The status in which the task run finished. One of `succeeded`, `failed`, or `aborted`. Allowed values: succeeded \| failed \| aborted. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `duration` | `string` | No | The task execution duration in ISO 8601 format. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `string[]` | No | The list of parameters for the action. |
| `disabledCode` | `string` | No | The reason the task was disabled. Allowed values: MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.tasks.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "usage": "ANALYTICS",
    "action": "string",
    "status": "succeeded",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "duration": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": [
      "string"
    ],
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string"
  },
  "eventType": "com.qlik.scheduling.task.created",
  "extensions": {
    "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
    "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
    "toplevelresourceid": "string"
  }
}
```


### com.qlik.scheduling.task.deleted

**Title:** Task deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a task is deleted. The event includes the full task state at the time of deletion, including the task ID and owner.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |
| `eventType` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.scheduling.task.deleted". |
| `extensions` | `cloudEventsQlikExtensionsAttributes` | No | Additional event metadata. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `usage` | `string` | No | The product domain in which the associated resource is used, such as `ANALYTICS` or `DATA_PREPARATION`. Defaults to `ANALYTICS` when not specified. Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The status in which the task run finished. One of `succeeded`, `failed`, or `aborted`. Allowed values: succeeded \| failed \| aborted. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `duration` | `string` | No | The task execution duration in ISO 8601 format. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `string[]` | No | The list of parameters for the action. |
| `disabledCode` | `string` | No | The reason the task was disabled. Allowed values: MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.tasks.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "usage": "ANALYTICS",
    "action": "string",
    "status": "succeeded",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "duration": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": [
      "string"
    ],
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string"
  },
  "eventType": "com.qlik.scheduling.task.deleted",
  "extensions": {
    "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
    "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
    "toplevelresourceid": "string"
  }
}
```


### com.qlik.scheduling.task.updated

**Title:** Task updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a task's configuration or properties are updated. The event includes the updated task state along with a list of changed fields in `_updates`, identifying what was modified and the old and new values. Use this to detect configuration drift or audit changes to scheduled tasks.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |
| `eventType` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.scheduling.task.updated". |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `usage` | `string` | No | The product domain in which the associated resource is used, such as `ANALYTICS` or `DATA_PREPARATION`. Defaults to `ANALYTICS` when not specified. Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The status in which the task run finished. One of `succeeded`, `failed`, or `aborted`. Allowed values: succeeded \| failed \| aborted. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `duration` | `string` | No | The task execution duration in ISO 8601 format. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `string[]` | No | The list of parameters for the action. |
| `disabledCode` | `string` | No | The reason the task was disabled. Allowed values: MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |
| `_updates` | `object[]` | No | The list of fields updated in this task, with the old and new values for each changed field. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | The JSON path of the field that was updated. |
| `newValue` | `string` | No | The new value of the field after the update. |
| `oldValue` | `string` | No | The previous value of the field before the update. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.tasks.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "usage": "ANALYTICS",
    "action": "string",
    "status": "succeeded",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "duration": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "deletedAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": [
      "string"
    ],
    "disabledCode": "MANUALLY",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string",
    "_updates": [
      {
        "path": "string",
        "newValue": "string",
        "oldValue": "string"
      }
    ]
  },
  "eventType": "com.qlik.scheduling.task.updated"
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

Additional event metadata.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |



### taskEntryObject

Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `usage` | `string` | No | The product domain in which the associated resource is used, such as `ANALYTICS` or `DATA_PREPARATION`. Defaults to `ANALYTICS` when not specified. Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The status in which the task run finished. One of `succeeded`, `failed`, or `aborted`. Allowed values: succeeded \| failed \| aborted. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `duration` | `string` | No | The task execution duration in ISO 8601 format. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `string[]` | No | The list of parameters for the action. |
| `disabledCode` | `string` | No | The reason the task was disabled. Allowed values: MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |


