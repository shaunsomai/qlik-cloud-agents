---
source: https://qlik.dev/apis/event/hub-dashboards/
last_updated: 2026-05-12T12:27:38+01:00
---

# Hub dashboards

Track hub dashboard updates to audit changes to activity center home page layouts.

## Table of Contents

### system-events.hub-dashboards

- [com.qlik.v1.hub-dashboard.updated](#comqlikv1hub-dashboardupdated)

## Events published on the `system-events.hub-dashboards` channel

### com.qlik.v1.hub-dashboard.updated

**Title:** Dashboard updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a hub dashboard is updated. The event includes the dashboard ID, source (`user` for personal dashboards or `tenant` for tenant-wide dashboards), and a list of changed fields. Use this to keep external catalogs or monitoring systems up to date with dashboard changes.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event related to the originating occurrence. Metadata: default = "com.qlik.v1.hub-dashboard.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `updates` | `resourceUpdates[]` | No | Additional metadata about a resource update |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `dashboardUpdateData` | Yes | Dashboard specific data related to the event. |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON pointer to the field that has been updated |
| `newValue` | `string` | No | The new value of the field |
| `oldValue` | `string` | No | The value the field had before the update was applied |

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier for the dashboard. |
| `source` | `string` | No | The source of the dashboard. `user` is a user's personal dashboard. `tenant` is a tenant-wide dashboard configured by admins and curators. Allowed values: user \| tenant. Metadata: default = "user". |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.hub-dashboard.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "updates": [
    {
      "path": "string",
      "newValue": "string",
      "oldValue": "string"
    }
  ],
  "authtype": "string",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "id": "string",
    "source": "user"
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
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `updates` | `object[]` | No | List of updates, follow fast json patch schema |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON pointer to the field that has been updated |
| `newValue` | `string` | No | The new value of the field |
| `oldValue` | `string` | No | The value the field had before the update was applied |

</details>



### dashboardUpdateData

Data representing a dashboard

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier for the dashboard. |
| `source` | `string` | No | The source of the dashboard. `user` is a user's personal dashboard. `tenant` is a tenant-wide dashboard configured by admins and curators. Allowed values: user \| tenant. Metadata: default = "user". |



### resourceUpdate

Additional metadata about a resource update

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON pointer to the field that has been updated |
| `newValue` | `string` | No | The new value of the field |
| `oldValue` | `string` | No | The value the field had before the update was applied |



### resourceUpdates

**Type:** `object[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON pointer to the field that has been updated |
| `newValue` | `string` | No | The new value of the field |
| `oldValue` | `string` | No | The value the field had before the update was applied |


