---
source: https://qlik.dev/apis/event/reloads/
last_updated: 2026-09-11T16:13:57Z
---

# Reloads

Subscribe to reload-related events to monitor and react to app reload activity in real time.

## Table of Contents

### system-events.reload

- [com.qlik.v1.reload.finished](#comqlikv1reloadfinished)

## Events published on the `system-events.reload` channel

### com.qlik.v1.reload.finished

**Title:** Reload Finished Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The reload finished event will be published when a reload has finished. While a reload might be executed multiple times, there will be only one reload finished event.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the event. Metadata: minLength = 1. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.reload.finished". |
| `source` | `string` | Yes | The source of the event. Metadata: default = "com.qlik/reloads". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | Yes | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `reason` | `string` | No | Reason the event was triggered. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | Unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | The session ID of the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | Unique identifier for top level resource related to the event. |
| `data` | `reloadFinishedEventData` | No | Data specific to the reload finished event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Reload ID. |
| `type` | `string` | No | What initiated the reload: hub = one-time reload manually triggered in hub, chronos = time based scheduled reload triggered by chronos, external = reload triggered via external API request, automations = reload triggered in automation, data-refresh = reload triggered by refresh of data, choreographer = reload triggered by choreographer. Allowed values: hub \| chronos \| external \| automations \| data-refresh \| choreographer. |
| `appId` | `string` | Yes | ID of the reloaded app. |
| `status` | `string` | No | The end status of reload. Allowed values: SUCCEEDED \| FAILED \| CANCELED \| EXCEEDED_LIMIT. |
| `taskId` | `string` | No | ID of the app's scheduled reload task. |
| `userId` | `string` | Yes | ID of the requesting user. |
| `weight` | `integer` | No | The weight of the reload. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1.  Metadata: minimum = 1, maximum = 10, default = 1, default = 1. |
| `partial` | `boolean` | No | The partial status of reload. |
| `appUsage` | `string` | No | The app's usage type |
| `tenantId` | `string` | No | ID of the tenant. |
| `errorCode` | `string` | No | Error code, if failed. |
| `startTime` | `string` | No | Reload starting time from engine. Metadata: format = "date-time". |
| `succeeded` | `boolean` | Yes | Success status of reload. |
| `resourceId` | `string` | No | Identifies the specific resource ID within that service. |
| `creationTime` | `string` | No | Reload creation time. Metadata: format = "date-time". |
| `errorMessage` | `string` | No | Error message, if failed. |
| `resourceType` | `string` | No | Identifies the service type that triggered the reload, e.g. "api". |
| `licenseNumber` | `string` | No | License number from the requesting user's JWT. |
| `enginePoolName` | `string` | No | The engine pool that executed the reload. |
| `lastReloadTime` | `string` | No | Last reload time from engine, if succeeded. Metadata: format = "date-time". |
| `durationSeconds` | `number` | No | Duration from engine session acquisition to reload attempt completion (seconds). |
| `requeueCounters` | `object` | No | The number of times the reload has been requeued, and the number of those requeues caused by errors (such as a websocket error). |
| `reloadPacksFactor` | `number` | No | Reload packs factor determined by the engine size used for the reload. Metadata: default = 0, default = 0. |
| `engineSizingReason` | `string` | No | Reason used to determine the engine size for the reload. |
| `reloadPacksConsumed` | `integer` | No | Number of reload packs consumed by the reload. Only populated when the reload packs feature is enabled for the tenant. Metadata: default = 0, default = 0. |
| `crashedOnMaxSizeEngine` | `boolean` | No | Whether the session request failed due to the app previously crashing on a max size engine |

<details>
<summary>Properties of `requeueCounters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requeuesTotal` | `integer` | No | Total number of times the reload has been requeued. Metadata: minimum = 0. |
| `requeuesWithErrors` | `integer` | No | Number of times the reload has been requeued due to an error. Metadata: minimum = 0. |

</details>

</details>


**Example**

```json
{
  "id": "b347fd0d-1321-417f-91ee-90e96c76389c",
  "host": "qlik.example.com",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.reload.finished",
  "source": "com.qlik/reloads",
  "ownerid": "5be59decca62aa00097268a4",
  "originip": "192.168.1.1",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "reason": "User initiated reload",
  "userid": "5be59decca62aa00097268a4",
  "spaceid": "64db65d5970c28d340790f5c",
  "authtype": "token",
  "clientid": "id123",
  "tenantid": "UkeLb6ICti8OA8f3LueRI5kVNtuHc15f",
  "sessionid": "b1fb457e-fca4-3c7d-8436-14380a990aef",
  "authclaims": "{\"sub\":\"5be59decca62aa00097268a4\",\"name\":\"John Doe\",\"email\":\"john.doe@example.com\"}",
  "tracestate": "key1=value1,key2=value2",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "toplevelresourceid": "002ff8c5-3c11-4464-a22b-68fb5e7ee5e8",
  "data": {
    "id": "6a849f7f18ec290e6ceb025d",
    "appId": "002ff8c5-3c11-4464-a22b-68fb5e7ee5e8",
    "userId": "5be59decca62aa00097268a4",
    "succeeded": true
  }
}
```


## Schemas

### cloudEventsContextAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the event. Metadata: minLength = 1. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | The source of the event. Metadata: default = "com.qlik/reloads". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | Yes | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reason` | `string` | No | Reason the event was triggered. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | Unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | The session ID of the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | Unique identifier for top level resource related to the event. |



### reloadFinishedEventData

Data specific to the reload finished event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Reload ID. |
| `type` | `string` | No | What initiated the reload: hub = one-time reload manually triggered in hub, chronos = time based scheduled reload triggered by chronos, external = reload triggered via external API request, automations = reload triggered in automation, data-refresh = reload triggered by refresh of data, choreographer = reload triggered by choreographer. Allowed values: hub \| chronos \| external \| automations \| data-refresh \| choreographer. |
| `appId` | `string` | Yes | ID of the reloaded app. |
| `status` | `string` | No | The end status of reload. Allowed values: SUCCEEDED \| FAILED \| CANCELED \| EXCEEDED_LIMIT. |
| `taskId` | `string` | No | ID of the app's scheduled reload task. |
| `userId` | `string` | Yes | ID of the requesting user. |
| `weight` | `integer` | No | The weight of the reload. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1.  Metadata: minimum = 1, maximum = 10, default = 1, default = 1. |
| `partial` | `boolean` | No | The partial status of reload. |
| `appUsage` | `string` | No | The app's usage type |
| `tenantId` | `string` | No | ID of the tenant. |
| `errorCode` | `string` | No | Error code, if failed. |
| `startTime` | `string` | No | Reload starting time from engine. Metadata: format = "date-time". |
| `succeeded` | `boolean` | Yes | Success status of reload. |
| `resourceId` | `string` | No | Identifies the specific resource ID within that service. |
| `creationTime` | `string` | No | Reload creation time. Metadata: format = "date-time". |
| `errorMessage` | `string` | No | Error message, if failed. |
| `resourceType` | `string` | No | Identifies the service type that triggered the reload, e.g. "api". |
| `licenseNumber` | `string` | No | License number from the requesting user's JWT. |
| `enginePoolName` | `string` | No | The engine pool that executed the reload. |
| `lastReloadTime` | `string` | No | Last reload time from engine, if succeeded. Metadata: format = "date-time". |
| `durationSeconds` | `number` | No | Duration from engine session acquisition to reload attempt completion (seconds). |
| `requeueCounters` | `object` | No | The number of times the reload has been requeued, and the number of those requeues caused by errors (such as a websocket error). |
| `reloadPacksFactor` | `number` | No | Reload packs factor determined by the engine size used for the reload. Metadata: default = 0, default = 0. |
| `engineSizingReason` | `string` | No | Reason used to determine the engine size for the reload. |
| `reloadPacksConsumed` | `integer` | No | Number of reload packs consumed by the reload. Only populated when the reload packs feature is enabled for the tenant. Metadata: default = 0, default = 0. |
| `crashedOnMaxSizeEngine` | `boolean` | No | Whether the session request failed due to the app previously crashing on a max size engine |

<details>
<summary>Properties of `requeueCounters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requeuesTotal` | `integer` | No | Total number of times the reload has been requeued. Metadata: minimum = 0. |
| `requeuesWithErrors` | `integer` | No | Number of times the reload has been requeued due to an error. Metadata: minimum = 0. |

</details>


