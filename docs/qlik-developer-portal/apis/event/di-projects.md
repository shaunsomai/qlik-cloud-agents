---
source: https://qlik.dev/apis/event/di-projects/
last_updated: 2026-04-10T12:07:03Z
---

# Data integration projects

Monitor data integration pipeline task execution and track project events.

## Table of Contents

### system-events.di-projects.di-tasks

- [com.qlik.v1.di-projects.di-tasks.completed](#comqlikv1di-projectsdi-taskscompleted)
- [com.qlik.v1.di-projects.di-tasks.failed](#comqlikv1di-projectsdi-tasksfailed)
- [com.qlik.v1.di-projects.di-tasks.started](#comqlikv1di-projectsdi-tasksstarted)
- [com.qlik.v1.di-projects.di-tasks.stopped](#comqlikv1di-projectsdi-tasksstopped)

## Events published on the `system-events.di-projects.di-tasks` channel

### com.qlik.v1.di-projects.di-tasks.completed

**Title:** Data task completed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Publish an event when a data task has completed successfully

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique CloudEvent identifier. |
| `data` | `TaskCompletedDataPayload` | Yes | The event-specific data payload for a completed task. |
| `time` | `string` | Yes | CloudEvent timestamp. Metadata: format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.completed. Metadata: default = "com.qlik.v1.di-projects.di-tasks.completed". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `userid` | `string` | Yes | Identifier for the user associated with the event. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `tenantid` | `string` | Yes | Identifier for the tenant. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |
| `extensions` | `QlikEventExtensions` | Yes | Qlik-specific extension attributes for the event. |
| `specversion` | `string` | Yes | CloudEvents spec version. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | Yes | Content type of the event payload. Metadata: default = "application/json". |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `object` | Yes | Information about the actor. |
| `updates` | `object[]` | Yes | List of updates related to the event. |

</details>


**Example**

```json
{
  "id": "02eae54e-396f-456c-bb6e-4ef1793504d9",
  "data": {
    "endTime": "2025-05-26T11:47:17.893Z",
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "LANDING",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:47:17.425Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER"
  },
  "time": "2025-05-26T11:47:18.045Z",
  "type": "com.qlik.v1.di-projects.di-tasks.completed",
  "source": "com.qlik/data-app-design",
  "userid": "6819cec4fb2b973f77b77383",
  "subject": "some-subject",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "dataschema": "https://example.com/schema",
  "extensions": {
    "actor": {},
    "updates": [
      {}
    ]
  },
  "specversion": "1.0",
  "datacontenttype": "application/json"
}
```


### com.qlik.v1.di-projects.di-tasks.failed

**Title:** Data task failed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Publish an event when a data task has failed

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique CloudEvent identifier. |
| `data` | `TaskFailedDataPayload` | Yes | The event-specific data payload for a failed task. |
| `time` | `string` | Yes | CloudEvent timestamp. Metadata: format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.failed. Metadata: default = "com.qlik.v1.di-projects.di-tasks.failed". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `userid` | `string` | Yes | Identifier for the user associated with the event. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `tenantid` | `string` | Yes | Identifier for the tenant. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |
| `extensions` | `QlikEventExtensions` | Yes | Qlik-specific extension attributes for the event. |
| `specversion` | `string` | Yes | CloudEvents spec version. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | Yes | Content type of the event payload. Metadata: default = "application/json". |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended (failed). Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `errorDetails` | `ErrorDetails` | Yes | Detailed information about an error. |
| `errorMessage` | `string` | Yes | Summary of the error. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

<details>
<summary>Properties of `errorDetails`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes |  |
| `title` | `string` | Yes |  |
| `source` | `string` | Yes |  |
| `status` | `integer` | Yes |  |

</details>

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `object` | Yes | Information about the actor. |
| `updates` | `object[]` | Yes | List of updates related to the event. |

</details>


**Example**

```json
{
  "id": "c946fcdf-8e9c-464f-80dd-a08483d31f36",
  "data": {
    "endTime": "2025-05-26T11:48:22.025Z",
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "LANDING",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER",
    "errorDetails": {
      "code": "QDI-DW-STORAGE-TABLE-IN-BATCH-ERROR",
      "title": "The batch run failed due to one or more tables that failed to load",
      "source": "com.qlik/qdi-app-manager",
      "status": 500
    },
    "errorMessage": "The following tables failed to load: 'Order Details, Customers, Orders, Employees, Products, Categories, Region, Territories, Suppliers, Shippers'"
  },
  "time": "2025-05-26T11:48:27.521Z",
  "type": "com.qlik.v1.di-projects.di-tasks.failed",
  "source": "com.qlik/data-app-design",
  "userid": "6819cec4fb2b973f77b77383",
  "subject": "some-subject",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "dataschema": "https://example.com/schema",
  "extensions": {
    "actor": {},
    "updates": [
      {}
    ]
  },
  "specversion": "1.0",
  "datacontenttype": "application/json"
}
```


### com.qlik.v1.di-projects.di-tasks.started

**Title:** Data task started

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Publish an event when a data task is started

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique CloudEvent identifier. |
| `data` | `TaskStartedDataPayload` | Yes | The event-specific data payload for a started task. |
| `time` | `string` | Yes | CloudEvent timestamp. Metadata: format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.started. Metadata: default = "com.qlik.v1.di-projects.di-tasks.started". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `userid` | `string` | Yes | Identifier for the user associated with the event. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `tenantid` | `string` | Yes | Identifier for the tenant. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |
| `extensions` | `QlikEventExtensions` | Yes | Qlik-specific extension attributes for the event. |
| `specversion` | `string` | Yes | CloudEvents spec version. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | Yes | Content type of the event payload. Metadata: default = "application/json". |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `object` | Yes | Information about the actor. |
| `updates` | `object[]` | Yes | List of updates related to the event. |

</details>


**Example**

```json
{
  "id": "8b6adb1b-d6dd-47bd-ab3d-17d231166ba7",
  "data": {
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "LANDING",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER"
  },
  "time": "2025-05-26T11:48:15.004Z",
  "type": "com.qlik.v1.di-projects.di-tasks.started",
  "source": "com.qlik/data-app-design",
  "userid": "string",
  "subject": "some-subject",
  "tenantid": "string",
  "dataschema": "https://example.com/schema",
  "extensions": {
    "actor": {},
    "updates": [
      {}
    ]
  },
  "specversion": "1.0",
  "datacontenttype": "application/json"
}
```


### com.qlik.v1.di-projects.di-tasks.stopped

**Title:** Data task stopped

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Publish an event when a data task has been stopped

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique CloudEvent identifier. |
| `data` | `TaskStoppedDataPayload` | Yes | The event-specific data payload for a stopped task. |
| `time` | `string` | Yes | CloudEvent timestamp. Metadata: format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.stopped. Metadata: default = "com.qlik.v1.di-projects.di-tasks.stopped". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `userid` | `string` | Yes | Identifier for the user associated with the event. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `tenantid` | `string` | Yes | Identifier for the tenant. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |
| `extensions` | `QlikEventExtensions` | Yes | Qlik-specific extension attributes for the event. |
| `specversion` | `string` | Yes | CloudEvents spec version. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | Yes | Content type of the event payload. Metadata: default = "application/json". |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task was originally started. Metadata: format = "date-time". |
| `stoppedBy` | `string` | Yes | Identifier of the user who stopped the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `stoppedTime` | `string` | Yes | Timestamp when the task was stopped. Metadata: format = "date-time". |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>

<details>
<summary>Properties of `extensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `object` | Yes | Information about the actor. |
| `updates` | `object[]` | Yes | List of updates related to the event. |

</details>


**Example**

```json
{
  "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
  "data": {
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "LANDING",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "stoppedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER",
    "stoppedTime": "2025-05-26T11:49:59.000Z"
  },
  "time": "2025-05-26T11:50:00.000Z",
  "type": "com.qlik.v1.di-projects.di-tasks.stopped",
  "source": "com.qlik/data-app-design",
  "userid": "6819cec4fb2b973f77b77383",
  "subject": "some-subject",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "dataschema": "https://example.com/schema",
  "extensions": {
    "actor": {},
    "updates": [
      {}
    ]
  },
  "specversion": "1.0",
  "datacontenttype": "application/json"
}
```


## Schemas

### DataTaskInfo

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |



### datatasktype

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datatasktype` | `string` | No | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |



### ErrorDetails

Detailed information about an error.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes |  |
| `title` | `string` | Yes |  |
| `source` | `string` | Yes |  |
| `status` | `integer` | Yes |  |



### QlikEventExtensions

Qlik-specific extension attributes.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `object` | Yes | Information about the actor. |
| `updates` | `object[]` | Yes | List of updates related to the event. |



### StartMethod

Method by which the task was started

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |



### TaskCompletedDataPayload

Payload for data task completed event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>



### TaskFailedDataPayload

Payload for data task failed event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended (failed). Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `errorDetails` | `ErrorDetails` | Yes | Detailed information about an error. |
| `errorMessage` | `string` | Yes | Summary of the error. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

<details>
<summary>Properties of `errorDetails`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes |  |
| `title` | `string` | Yes |  |
| `source` | `string` | Yes |  |
| `status` | `integer` | Yes |  |

</details>



### TaskStartedDataPayload

Payload for data task started event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>



### TaskStoppedDataPayload

Payload for data task stopped event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task was originally started. Metadata: format = "date-time". |
| `stoppedBy` | `string` | Yes | Identifier of the user who stopped the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `stoppedTime` | `string` | Yes | Timestamp when the task was stopped. Metadata: format = "date-time". |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| ICEBERG_STORAGE \| MIRROR. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>


