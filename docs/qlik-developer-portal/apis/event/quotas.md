---
source: https://qlik.dev/apis/event/quotas/
last_updated: 2026-09-11T16:13:57Z
---

# Large app quotas

Track Large App quota consumption and allocation events across your Qlik Cloud tenant.

## Table of Contents

### system-events.quota

- [com.qlik.v1.quota.allocation-failed](#comqlikv1quotaallocation-failed)
- [com.qlik.v1.quota.consumed](#comqlikv1quotaconsumed)
- [com.qlik.v1.quota.released](#comqlikv1quotareleased)

## Events published on the `system-events.quota` channel

### com.qlik.v1.quota.allocation-failed

**Title:** Quota Allocation Failed Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The quota allocation-failed event contains information of a quota allocation-failed record.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.v1.quota.allocation-failed". |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `reason` | `string` | No | The reason why the event is triggered. |
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
| `data` | `quotaAllocationFailed` | No | data of a quota allocation failed event |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `limit` | `integer` | Yes | The limit of the quota |
| `consumed` | `integer` | No | The amount of quota consumed |
| `requested` | `integer` | Yes | The amount of quota requested |

</details>


**Example**

```json
{
  "id": "id123",
  "host": "qlik.example.com",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.quota.allocation-failed",
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
  "authclaims": "{ \"iss\": \"qlik.api.internal/qix-sessions\", \"sub\": \"qix-sessions\", \"subType\": \"service\" }",
  "tracestate": "b3=f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-1",
  "traceparent": "00-f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-01",
  "toplevelresourceid": "id123",
  "data": {
    "unit": "byte",
    "appId": "id123",
    "quota": "appSizeTotalDefault",
    "spaceId": "id123",
    "appSizeQuotaGroup": "reloads",
    "limit": 30,
    "consumed": 30,
    "requested": 30
  }
}
```


### com.qlik.v1.quota.consumed

**Title:** Quota Consumption Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The quota consumption event contains information of a quota consumption.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.v1.quota.consumed". |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `reason` | `string` | No | The reason why the event is triggered. |
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
| `data` | `quotaConsumed` | No | data of a quota consumption event |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `consumed` | `integer` | Yes | The amount of quota consumed |

</details>


**Example**

```json
{
  "id": "id123",
  "host": "qlik.example.com",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.quota.consumed",
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
  "authclaims": "{ \"iss\": \"qlik.api.internal/qix-sessions\", \"sub\": \"qix-sessions\", \"subType\": \"service\" }",
  "tracestate": "b3=f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-1",
  "traceparent": "00-f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-01",
  "toplevelresourceid": "id123",
  "data": {
    "unit": "byte",
    "appId": "id123",
    "quota": "appSizeTotalDefault",
    "spaceId": "id123",
    "appSizeQuotaGroup": "reloads",
    "consumed": 42
  }
}
```


### com.qlik.v1.quota.released

**Title:** Quota Released Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The quota released event contains information of a quota released record.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Unique identifier for the event type. Metadata: default = "com.qlik.v1.quota.released". |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `reason` | `string` | No | The reason why the event is triggered. |
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
| `data` | `quotaReleased` | No | data of a quota released event |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `released` | `integer` | Yes | The amount of quota released |

</details>


**Example**

```json
{
  "id": "id123",
  "host": "qlik.example.com",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.quota.released",
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
  "authclaims": "{ \"iss\": \"qlik.api.internal/qix-sessions\", \"sub\": \"qix-sessions\", \"subType\": \"service\" }",
  "tracestate": "b3=f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-1",
  "traceparent": "00-f0cc846cd24db3f68e384e9ccdfbf225-226ac0c507065555-01",
  "toplevelresourceid": "id123",
  "data": {
    "unit": "byte",
    "appId": "id123",
    "quota": "appSizeTotalDefault",
    "spaceId": "id123",
    "appSizeQuotaGroup": "reloads",
    "released": 30
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `host` | `string` | No | The host of the event. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `type` | `string` | No | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/qix-sessions". |
| `ownerid` | `string` | No | The owner ID of the event. |
| `originip` | `string` | No | The origin IP of the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |



### cloudEventsQlikExtensionsAttributes

Additional metadata and custom fields

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reason` | `string` | No | The reason why the event is triggered. |
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



### quotaAllocationFailed

data of a quota allocation failed event

**Type:** `quotaInfo`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `limit` | `integer` | Yes | The limit of the quota |
| `consumed` | `integer` | No | The amount of quota consumed |
| `requested` | `integer` | Yes | The amount of quota requested |



### quotaConsumed

data of a quota consumption event

**Type:** `quotaInfo`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `consumed` | `integer` | Yes | The amount of quota consumed |



### quotaInfo

data of a quota information

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |



### quotaReleased

data of a quota released event

**Type:** `quotaInfo`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | The unit of the usage |
| `appId` | `string` | Yes | The ID of the app that consumes the quota. |
| `quota` | `string` | Yes | The name of a quota |
| `spaceId` | `string` | Yes | The ID of the space in which app is. |
| `appSizeQuotaGroup` | `string` | Yes | The appSizeQuotaGroup name of request. |
| `released` | `integer` | Yes | The amount of quota released |


