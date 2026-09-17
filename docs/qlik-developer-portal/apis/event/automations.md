---
source: https://qlik.dev/apis/event/automations/
last_updated: 2026-09-14T20:53:09+02:00
---

# Automations

Events emitted when automations are created, updated, executed, or deleted in Qlik Automate.

## Table of Contents

### system-events.automation

- [com.qlik.v1.automation.run.ended](#comqlikv1automationrunended)

## Events published on the `system-events.automation` channel

### com.qlik.v1.automation.run.ended

**Title:** Run ended

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The run ended event will be published when an automation execution has ended.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of the event. Metadata: default = "com.qlik.v1.automation.run.ended". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/automations". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `ownerid` | `string` | No | Unique identifier for the owner of the resource related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `metricsObject` | No | The automation run that ended, including execution metrics. |
| `toplevelresourceid` | `string` | No | Unique identifier for the automation associated with the execution. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `automation` | `` | No |  |
| `id` | `string` | No | Metadata: format = "uuid". |
| `title` | `string` | No | Title of the automation run. |
| `status` | `string` | No | Status of the automation run. Allowed values: exceeded limit \| failed \| finished \| finished with warnings \| must stop \| not started \| queued \| running \| starting \| stopped. |
| `context` | `string` | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, the "test_run" context will not process all results when listing items). Allowed values: test_run \| editor \| detail \| api_sync \| api_async \| webhook \| lookup \| api \| interactive. |
| `metrics` | `object` | No |  |
| `ownerId` | `string` | No | Unique identifier for the owner of the automation (QCS external user ID). |
| `spaceId` | `string` | No | Unique identifier for the space the run belongs to (empty when the run is not in a space). |
| `testRun` | `boolean` | No | Indicates if this is a test run. Supersedes the legacy `isTestRun` field. |
| `archived` | `boolean` | No | Indicates if the run is archived. Supersedes the legacy `isArchived` field. |
| `billable` | `boolean` | No | Indicates if this automation run is billable (if there are executed blocks that are linked to billable connectors) |
| `stopTime` | `string` | No | Metadata: format = "date-time". |
| `createdAt` | `string` | No | Metadata: format = "date-time". |
| `isTestRun` | `boolean` | No | Indicates whether the run is a test run. |
| `startTime` | `string` | No | Metadata: format = "date-time". |
| `updatedAt` | `string` | No | Metadata: format = "date-time". |
| `isArchived` | `boolean` | No | Indicates whether the run is archived. |
| `executedById` | `string` | No | Id of the executor of the affected resource. |
| `scheduledStartTime` | `string` | No | Metadata: format = "date-time". |
| `blocks` | `object[]` | No | List of blocks used during execution. |
| `network` | `object` | No |  |
| `totalApiCalls` | `integer` | No | The number of API calls made. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | `object[]` | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | `object` | No |  |
| `totalApiCalls` | `integer` | No | The number of API calls made. Metadata: default = 0, default = 0. |

<details>
<summary>Properties of `blocks`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `network`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Type of the block. Allowed values: snippetBlock \| endpointBlock \| baseBlock. |
| `params` | `array` | No | Parameters of the block (only present for base blocks) |
| `rxBytes` | `integer` | No | Total amount of bytes received by the current block. |
| `txBytes` | `integer` | No | Total amount of bytes sent by the current block. |
| `apiCalls` | `integer` | No | API calls to external resources made by the current block. |
| `duration` | `integer` | No | Duration of the block execution. |
| `blockName` | `string` | No | Name of the block (only present for base blocks) |
| `snippetId` | `string` | No | Unique identifier for the snippet block used within the execution. Metadata: format = "uuid". |
| `endpointId` | `string` | No | Unique identifier for the endpoint. Metadata: format = "uuid". |
| `connectorId` | `string` | No | Unique identifier for the connector used within the block of the execution. Metadata: format = "uuid". |

</details>

<details>
<summary>Properties of `network`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rxBytes` | `integer` | No | The number of received bytes. Metadata: default = 0, default = 0. |
| `txBytes` | `integer` | No | The number of sent bytes. Metadata: default = 0, default = 0. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00.000Z",
  "type": "com.qlik.v1.automation.run.ended",
  "source": "com.qlik/automations",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "ownerid": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "spaceid": "68badd085f87029377ff60fa",
  "tenantid": "svua0w_Icu2Kl1-SPshoNwgzAWdVLK0N",
  "data": {
    "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
    "title": "string",
    "status": "exceeded limit",
    "context": "test_run",
    "metrics": {
      "blocks": [
        {
          "type": "endpointBlock",
          "rxBytes": 18329921,
          "txBytes": 18329921,
          "apiCalls": 40,
          "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "network": {
        "rxBytes": 0,
        "txBytes": 0
      },
      "totalApiCalls": 0
    },
    "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
    "spaceId": "68badd085f87029377ff60fa",
    "testRun": true,
    "archived": true,
    "billable": false,
    "stopTime": "2021-12-23T12:28:21.000000Z",
    "createdAt": "2021-12-23T12:28:21.000000Z",
    "isTestRun": true,
    "startTime": "2021-12-23T12:28:21.000000Z",
    "updatedAt": "2021-12-23T12:28:21.000000Z",
    "isArchived": true,
    "executedById": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
    "scheduledStartTime": "2021-12-23T12:28:21.000000Z",
    "blocks": [
      {
        "type": "endpointBlock",
        "params": [],
        "rxBytes": 18329921,
        "txBytes": 18329921,
        "apiCalls": 40,
        "duration": 1000,
        "blockName": "SleepBlock",
        "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      }
    ],
    "network": {
      "rxBytes": 0,
      "txBytes": 0
    },
    "totalApiCalls": 42
  },
  "toplevelresourceid": "00000000-0000-0000-0000-000000000000"
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
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/automations". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `ownerid` | `string` | No | Unique identifier for the owner of the resource related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### metricsObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | `object[]` | No | List of blocks used during execution. |
| `network` | `object` | No |  |
| `totalApiCalls` | `integer` | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Type of the block. Allowed values: snippetBlock \| endpointBlock \| baseBlock. |
| `params` | `array` | No | Parameters of the block (only present for base blocks) |
| `rxBytes` | `integer` | No | Total amount of bytes received by the current block. |
| `txBytes` | `integer` | No | Total amount of bytes sent by the current block. |
| `apiCalls` | `integer` | No | API calls to external resources made by the current block. |
| `duration` | `integer` | No | Duration of the block execution. |
| `blockName` | `string` | No | Name of the block (only present for base blocks) |
| `snippetId` | `string` | No | Unique identifier for the snippet block used within the execution. Metadata: format = "uuid". |
| `endpointId` | `string` | No | Unique identifier for the endpoint. Metadata: format = "uuid". |
| `connectorId` | `string` | No | Unique identifier for the connector used within the block of the execution. Metadata: format = "uuid". |

</details>

<details>
<summary>Properties of `network`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rxBytes` | `integer` | No | The number of received bytes. Metadata: default = 0, default = 0. |
| `txBytes` | `integer` | No | The number of sent bytes. Metadata: default = 0, default = 0. |

</details>



### runObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Metadata: format = "uuid". |
| `title` | `string` | No | Title of the automation run. |
| `status` | `string` | No | Status of the automation run. Allowed values: exceeded limit \| failed \| finished \| finished with warnings \| must stop \| not started \| queued \| running \| starting \| stopped. |
| `context` | `string` | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, the "test_run" context will not process all results when listing items). Allowed values: test_run \| editor \| detail \| api_sync \| api_async \| webhook \| lookup \| api \| interactive. |
| `metrics` | `object` | No |  |
| `ownerId` | `string` | No | Unique identifier for the owner of the automation (QCS external user ID). |
| `spaceId` | `string` | No | Unique identifier for the space the run belongs to (empty when the run is not in a space). |
| `testRun` | `boolean` | No | Indicates if this is a test run. Supersedes the legacy `isTestRun` field. |
| `archived` | `boolean` | No | Indicates if the run is archived. Supersedes the legacy `isArchived` field. |
| `billable` | `boolean` | No | Indicates if this automation run is billable (if there are executed blocks that are linked to billable connectors) |
| `stopTime` | `string` | No | Metadata: format = "date-time". |
| `createdAt` | `string` | No | Metadata: format = "date-time". |
| `isTestRun` | `boolean` | No | Indicates whether the run is a test run. |
| `startTime` | `string` | No | Metadata: format = "date-time". |
| `updatedAt` | `string` | No | Metadata: format = "date-time". |
| `isArchived` | `boolean` | No | Indicates whether the run is archived. |
| `executedById` | `string` | No | Id of the executor of the affected resource. |
| `scheduledStartTime` | `string` | No | Metadata: format = "date-time". |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | `object[]` | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | `object` | No |  |
| `totalApiCalls` | `integer` | No | The number of API calls made. Metadata: default = 0, default = 0. |

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Type of the block. Allowed values: snippetBlock \| endpointBlock. |
| `rxBytes` | `integer` | Yes | Total amount of bytes received by the current block. |
| `txBytes` | `integer` | Yes | Total amount of bytes sent by the current block. |
| `apiCalls` | `integer` | No | API calls to external resources made by the current block. |
| `snippetId` | `string` | No | Unique identifier for the snippet block used within the execution. Metadata: format = "uuid". |
| `endpointId` | `string` | No | Unique identifier for the endpoint. Metadata: format = "uuid". |
| `connectorId` | `string` | Yes | Unique identifier for the connector used within the block of the execution. Metadata: format = "uuid". |

</details>

<details>
<summary>Properties of `network`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rxBytes` | `integer` | No | The number of received bytes. Metadata: default = 0, default = 0. |
| `txBytes` | `integer` | No | The number of sent bytes. Metadata: default = 0, default = 0. |

</details>

</details>


