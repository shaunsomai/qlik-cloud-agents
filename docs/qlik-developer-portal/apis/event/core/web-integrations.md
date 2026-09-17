---
source: https://qlik.dev/apis/event/core/web-integrations/
last_updated: 2026-08-31T15:18:51+02:00
---

# Web integrations

Events related to web integration configuration and CORS settings changes.

## Table of Contents

### system-events.web-integrations

- [com.qlik.core.web-integration.created](#comqlikcoreweb-integrationcreated)
- [com.qlik.core.web-integration.deleted](#comqlikcoreweb-integrationdeleted)
- [com.qlik.core.web-integration.updated](#comqlikcoreweb-integrationupdated)

## Events published on the `system-events.web-integrations` channel

### com.qlik.core.web-integration.created

**Title:** Web integration created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a web integration is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.web-integration.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session of the user triggering the event. Present only when a session identifier is available. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Web integration details. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Web integration identifier. |
| `name` | `string` | Yes | Web integration name. |
| `validOrigins` | `string[]` | Yes | List of valid origins (URLs) allowed to use the web integration for CORS requests. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.web-integration.created",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "UZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "tenants",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\"sub\":\"auth0|abc123\",\"scope\":\"user_default\"}",
  "tracestate": "b3=00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "data": {
    "id": "id123",
    "name": "Web integration 1",
    "validOrigins": [
      "http://unicorn.com",
      "http://foo.example"
    ]
  }
}
```


### com.qlik.core.web-integration.deleted

**Title:** Web integration deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a web integration is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.web-integration.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session of the user triggering the event. Present only when a session identifier is available. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Web integration details. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Web integration identifier. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.web-integration.deleted",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "UZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "tenants",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\"sub\":\"auth0|abc123\",\"scope\":\"user_default\"}",
  "tracestate": "b3=00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "data": {
    "id": "id123"
  }
}
```


### com.qlik.core.web-integration.updated

**Title:** Web integration updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a web integration is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.web-integration.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session of the user triggering the event. Present only when a session identifier is available. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Web integration details. Contains the full web integration object plus the list of updates that were applied. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Web integration identifier. |
| `name` | `string` | No | Web integration name. |
| `_updates` | `object[]` | Yes | Collection of updates performed on the resource. |
| `validOrigins` | `string[]` | No | List of valid origins (URLs) allowed to use the web integration for CORS requests. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON Pointer path of the property that has changed. |
| `newValue` | `oneOf(Option 1 \| Option 2)` | No | Value of the field after the update. A string for scalar fields, or an array of strings for list fields such as validOrigins. |
| `oldValue` | `oneOf(Option 1 \| Option 2)` | No | Value of the field before the update. A string for scalar fields, or an array of strings for list fields such as validOrigins. |

<details>
<summary>Properties of `newValue`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `oldValue`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.web-integration.updated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "UZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "tenants",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\"sub\":\"auth0|abc123\",\"scope\":\"user_default\"}",
  "tracestate": "b3=00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "data": {
    "id": "id123",
    "name": "Web integration 2",
    "_updates": [
      {
        "path": "/name",
        "newValue": "Web integration 2",
        "oldValue": "Web integration 1"
      }
    ],
    "validOrigins": [
      "http://unicorn.com"
    ]
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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session of the user triggering the event. Present only when a session identifier is available. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |


