---
source: https://qlik.dev/apis/event/notification-digests/
last_updated: 2026-09-11T16:13:57Z
---

# Notification digests

Events related to notification digest compilation and delivery.

## Table of Contents

### system-events.notification-digest

- [com.qlik.notification-digest.updated](#comqliknotification-digestupdated)

## Events published on the `system-events.notification-digest` channel

### com.qlik.notification-digest.updated

**Title:** A notification digest has been updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a notification digest configuration is updated. Includes frequency and enabled status. Use this to track digest configuration changes.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.notification-digest.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enabled` | `boolean` | No | Whether the notification digest is enabled or not. |
| `frequency` | `string` | No | The frequency of the notification digest. |
| `chronosJobID` | `string` | No | The identifier of the Chronos job responsible for generating the notification digest. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.notification-digest.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "enabled": true,
    "frequency": "string",
    "chronosJobID": "string"
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema.

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

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |


