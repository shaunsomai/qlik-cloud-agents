---
source: https://qlik.dev/apis/event/ai/mcps/
last_updated: 2026-07-17T09:30:31+02:00
---

# MCPs

Events emitted for Model Context Protocol Server (MCPS) tool executions in Qlik Cloud.

## Table of Contents

### system-events.ai.mcp

- [com.qlik.ai.mcp.tool.calls.aggregated](#comqlikaimcptoolcallsaggregated)
- [com.qlik.ai.mcp.tool.executed](#comqlikaimcptoolexecuted)

## Events published on the `system-events.ai.mcp` channel

### com.qlik.ai.mcp.tool.calls.aggregated

**Title:** Tool calls aggregated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when aggregated tool call metrics are generated after a configured threshold (default 5 tool calls) or timeout. Includes the count of tool calls, total execution latency across all calls in milliseconds, and event IDs of the individual tool execution events. Use this to analyze tool usage patterns and detect performance trends.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.ai.mcp.tool.calls.aggregated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/mcp". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Allowed values: 1.0. Metadata: minLength = 1, default = "1.0". |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | Yes | The unique identifier for the user related to the event. Metadata: format = "uuid". |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. Metadata: format = "uuid". |
| `data` | `object` | No | The aggregated metrics for a batch of tool calls, including the count of tool calls, cumulative latency across all calls, and references to individual tool execution events for traceability. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventIds` | `string[]` | Yes | The list of CloudEvent IDs from individual tool execution events that were aggregated. Provides traceability to the original `toolExecuted` events for detailed analysis. |
| `toolCount` | `integer` | Yes | The number of tool calls aggregated in this event. |
| `totalLatencyMs` | `integer` | Yes | The total execution latency across all aggregated tool calls, in milliseconds. |

</details>


**Example**

```json
{
  "id": "id123",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.ai.mcp.tool.calls.aggregated",
  "source": "com.qlik/mcp",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
  "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
  "data": {
    "eventIds": [
      "550e8400-e29b-41d4-a716-446655440000",
      "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
      "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "88f7f2e9-9c8a-4f9b-a8b5-9d8c7e6f5a4b",
      "99a8b3d4-1e2f-3c4d-8e6f-7a8b9c0d1e2f"
    ],
    "toolCount": 5,
    "totalLatencyMs": 1245
  }
}
```


### com.qlik.ai.mcp.tool.executed

**Title:** Tool executed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a tool is executed in MCP. Includes the tool name, client ID, execution latency in milliseconds, and any error message if execution failed. Optionally includes resource context (resourceId, resourceType, spaceId, subResourceId, subResourceType) when the tool operates on a specific resource. Use this to monitor tool performance and correlate tool calls.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.ai.mcp.tool.executed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/mcp". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Allowed values: 1.0. Metadata: minLength = 1, default = "1.0". |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | Yes | The unique identifier for the user related to the event. Metadata: format = "uuid". |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. Metadata: format = "uuid". |
| `data` | `object` | No | The tool execution details, including the tool name, execution time in milliseconds, and any error encountered during execution. |
| `clientid` | `string` | No | The client ID of the OAuth application that requested the tool execution. Absent when the request was made using an impersonated JWT (act claim) without an OAuth client ID. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | The name of the tool that was executed. |
| `error` | `string` | No | Error message if the tool execution failed. |
| `baggage` | `string` | No | W3C Baggage header value forwarded verbatim from the incoming request. Omitted when no baggage header was present on the incoming request. |
| `latency` | `integer` | Yes | The time it took to execute the tool, in milliseconds. |
| `spaceId` | `string` | No | The ID of the space associated with the tool call. Omitted when not applicable. |
| `billable` | `boolean` | No | Whether this tool call counts toward consumption/billing. False for tools tagged as excluded from billing capture (e.g. status-polling tools). Consumers computing consumption from this stream should ignore events where billable is false. |
| `userAgent` | `string` | No | Optional. The User-Agent header value from the request that triggered the tool execution, or "unknown" when the header is absent. |
| `resourceId` | `string` | No | The ID of the primary resource the tool operated on (e.g. app ID, dataset ID). Omitted when not applicable. |
| `resourceType` | `string` | No | The type of the primary resource (e.g. "app", "dataset", "automation"). Omitted when not applicable. |
| `subResourceId` | `string` | No | The ID of the sub-resource the tool operated on (e.g. sheet ID, chart ID). Omitted when not applicable. |
| `subResourceType` | `string` | No | The type of the sub-resource (e.g. "sheet", "chart", "dimension"). Omitted when not applicable. |

</details>


**Example**

```json
{
  "id": "id123",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.ai.mcp.tool.executed",
  "source": "com.qlik/mcp",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
  "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
  "data": {
    "name": "search_datasets",
    "latency": 123,
    "billable": true
  },
  "clientid": "client_12345"
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/mcp". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Allowed values: 1.0. Metadata: minLength = 1, default = "1.0". |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

Custom extensions for MCP events containing tenant and user context.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | Yes | The unique identifier for the user related to the event. Metadata: format = "uuid". |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. Metadata: format = "uuid". |


