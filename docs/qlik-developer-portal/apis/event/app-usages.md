---
source: https://qlik.dev/apis/event/app-usages/
last_updated: 2026-09-11T16:13:57Z
---

# App usages

Track application usage events including opens, closes, and user interactions.

## Table of Contents

### system-events.app-usage

- [com.qlik.v1.app-usage.quota.consumed](#comqlikv1app-usagequotaconsumed)

## Events published on the `system-events.app-usage` channel

### com.qlik.v1.app-usage.quota.consumed

**Title:** App usage quota consumed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when application quota usage is recorded for a tenant. The event provides a snapshot of total quota consumption and per-space usage breakdowns, enabling subscribers to track storage allocation, enforce capacity policies, and optimize resource distribution across spaces.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host that generated the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.v1.app-usage.quota.consumed". |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP address of the event source. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `reason` | `string` | No | The reason why the event was triggered. |
| `userid` | `string` | No | The unique identifier for the user related to the event. |
| `spaceid` | `string` | No | The unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | The unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | The unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs for distributed tracing state. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options in W3C Trace Context format. |
| `toplevelresourceid` | `string` | No | The unique identifier for the top-level resource related to the event. |
| `data` | `appQuotaUsage` | No | Represents a snapshot of the total application quota usage for a tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of measurement for quota usage (currently `byte`). Allowed values: byte. |
| `quota` | `string` | Yes | The name of the quota being reported. Allowed values: appSizeTotalDefault. |
| `usage` | `integer` | Yes | The total quota usage in the specified `unit`. |
| `spaceUsages` | `object[]` | No | The quota usage breakdown per space within the tenant. |

<details>
<summary>Properties of `spaceUsages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | No | The unit of measurement for the space quota usage (currently `byte`). Allowed values: byte. |
| `usage` | `integer` | No | The quota usage for this space in the specified `unit`. |
| `spaceId` | `string` | No | The unique identifier for the space. |

</details>

</details>


**Example**

```json
{
  "id": "id123",
  "host": "qlik.example.com",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.app-usage.quota.consumed",
  "source": "com.qlik/qix-sessions",
  "ownerid": "id123",
  "originip": "192.168.1.1",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "reason": "some reason",
  "userid": "id123",
  "spaceid": "id123",
  "authtype": "service_account",
  "clientid": "id123",
  "tenantid": "id123",
  "sessionid": "id123",
  "authclaims": "{\"iss\": \"qlik.api.internal/qix-sessions\", \"sub\": \"qix-sessions\", \"subType\": \"service\"}",
  "tracestate": "b3=f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-1",
  "traceparent": "00-f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-01",
  "toplevelresourceid": "id123",
  "data": {
    "unit": "byte",
    "quota": "appSizeTotalDefault",
    "usage": 2048
  }
}
```


## Schemas

### appQuotaUsage

Represents a snapshot of the total application quota usage for a tenant.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of measurement for quota usage (currently `byte`). Allowed values: byte. |
| `quota` | `string` | Yes | The name of the quota being reported. Allowed values: appSizeTotalDefault. |
| `usage` | `integer` | Yes | The total quota usage in the specified `unit`. |
| `spaceUsages` | `object[]` | No | The quota usage breakdown per space within the tenant. |

<details>
<summary>Properties of `spaceUsages`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | No | The unit of measurement for the space quota usage (currently `byte`). Allowed values: byte. |
| `usage` | `integer` | No | The quota usage for this space in the specified `unit`. |
| `spaceId` | `string` | No | The unique identifier for the space. |

</details>



### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host that generated the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP address of the event source. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |



### cloudEventsQlikExtensionsAttributes

Additional metadata and custom fields

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reason` | `string` | No | The reason why the event was triggered. |
| `userid` | `string` | No | The unique identifier for the user related to the event. |
| `spaceid` | `string` | No | The unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | The unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | The unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs for distributed tracing state. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options in W3C Trace Context format. |
| `toplevelresourceid` | `string` | No | The unique identifier for the top-level resource related to the event. |



### spaceUsage

Represents a quota usage snapshot for a single space.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | No | The unit of measurement for the space quota usage (currently `byte`). Allowed values: byte. |
| `usage` | `integer` | No | The quota usage for this space in the specified `unit`. |
| `spaceId` | `string` | No | The unique identifier for the space. |


