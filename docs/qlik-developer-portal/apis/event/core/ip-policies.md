---
source: https://qlik.dev/apis/event/core/ip-policies/
last_updated: 2026-08-31T15:18:51+02:00
---

# IP policies

Events emitted when IP policies are created, updated, or deleted in your tenant.

## Table of Contents

### system-events.ip-policy

- [com.qlik.core.ip-policy.created](#comqlikcoreip-policycreated)
- [com.qlik.core.ip-policy.deleted](#comqlikcoreip-policydeleted)
- [com.qlik.core.ip-policy.updated](#comqlikcoreip-policyupdated)

## Events published on the `system-events.ip-policy` channel

### com.qlik.core.ip-policy.created

**Title:** IP Policy Created Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

This event will be published when an IP Policy is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.ip-policy.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: default = "com.qlik/iam-resources". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `ipPolicy` | No | IP Policy resource object. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the IP Policy. |
| `name` | `string` | No | Descriptive name for the IP Policy. |
| `enabled` | `boolean` | No | Indicates whether the IP policy is enabled. |
| `editable` | `boolean` | No | Indicates whether the IP policy can be updated. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the IP Policy belongs to. |
| `createdAt` | `string` | No | The timestamp for when the IP Policy was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | the unique identifier of the user who created the IP Policy. |
| `deletable` | `boolean` | No | Indicates whether the IP policy can be deleted. |
| `updatedAt` | `string` | No | The timestamp for when the IP Policy was last updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | the unique identifier of the user who updated the IP Policy. |
| `allowedIps` | `string[]` | No | An array of allowed IP addresses. |
| `toggleable` | `boolean` | No | Indicates whether the IP policy can be enabled/disabled.. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.ip-policy.created",
  "source": "com.qlik/iam-resources",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "5be59decca62aa00097268a4",
    "name": "Allow access from office IP addresses",
    "enabled": true,
    "editable": true,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "5be59decca62aa00097268a4",
    "deletable": true,
    "updatedAt": "2021-03-22T10:01:02Z",
    "updatedBy": "5be59decca62aa00097268a4",
    "allowedIps": [
      "61.254.213.190/24",
      "1dbd:f66e:4267:d665:2539:6062:efa0:2afe/128"
    ],
    "toggleable": true
  }
}
```


### com.qlik.core.ip-policy.deleted

**Title:** IP Policy Deleted Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

This event will be published when an IP Policy is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.ip-policy.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: default = "com.qlik/iam-resources". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `ipPolicy` | No | IP Policy resource object. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the IP Policy. |
| `name` | `string` | No | Descriptive name for the IP Policy. |
| `enabled` | `boolean` | No | Indicates whether the IP policy is enabled. |
| `editable` | `boolean` | No | Indicates whether the IP policy can be updated. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the IP Policy belongs to. |
| `createdAt` | `string` | No | The timestamp for when the IP Policy was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | the unique identifier of the user who created the IP Policy. |
| `deletable` | `boolean` | No | Indicates whether the IP policy can be deleted. |
| `updatedAt` | `string` | No | The timestamp for when the IP Policy was last updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | the unique identifier of the user who updated the IP Policy. |
| `allowedIps` | `string[]` | No | An array of allowed IP addresses. |
| `toggleable` | `boolean` | No | Indicates whether the IP policy can be enabled/disabled.. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.ip-policy.deleted",
  "source": "com.qlik/iam-resources",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "5be59decca62aa00097268a4",
    "name": "Allow access from office IP addresses",
    "enabled": true,
    "editable": true,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "5be59decca62aa00097268a4",
    "deletable": true,
    "updatedAt": "2021-03-22T10:01:02Z",
    "updatedBy": "5be59decca62aa00097268a4",
    "allowedIps": [
      "61.254.213.190/24",
      "1dbd:f66e:4267:d665:2539:6062:efa0:2afe/128"
    ],
    "toggleable": true
  }
}
```


### com.qlik.core.ip-policy.updated

**Title:** IP Policy Updated Event

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

This event will be published when an IP Policy is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.ip-policy.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: default = "com.qlik/iam-resources". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `ipPolicy` | No | IP Policy resource object. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the IP Policy. |
| `name` | `string` | No | Descriptive name for the IP Policy. |
| `enabled` | `boolean` | No | Indicates whether the IP policy is enabled. |
| `editable` | `boolean` | No | Indicates whether the IP policy can be updated. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the IP Policy belongs to. |
| `createdAt` | `string` | No | The timestamp for when the IP Policy was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | the unique identifier of the user who created the IP Policy. |
| `deletable` | `boolean` | No | Indicates whether the IP policy can be deleted. |
| `updatedAt` | `string` | No | The timestamp for when the IP Policy was last updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | the unique identifier of the user who updated the IP Policy. |
| `allowedIps` | `string[]` | No | An array of allowed IP addresses. |
| `toggleable` | `boolean` | No | Indicates whether the IP policy can be enabled/disabled.. |
| `_updates` | `object[]` | No | An attribute update object that contains the change of an attribute. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | The updated attribute path. |
| `newValue` | `` | Yes | The new JSON value of the updated attribute. |
| `oldValue` | `` | Yes | The old JSON value of the updated attribute. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.ip-policy.updated",
  "source": "com.qlik/iam-resources",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "5be59decca62aa00097268a4",
    "name": "Allow access from office IP addresses",
    "enabled": true,
    "editable": true,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "5be59decca62aa00097268a4",
    "deletable": true,
    "updatedAt": "2021-03-22T10:01:02Z",
    "updatedBy": "5be59decca62aa00097268a4",
    "allowedIps": [
      "61.254.213.190/24",
      "1dbd:f66e:4267:d665:2539:6062:efa0:2afe/128"
    ],
    "toggleable": true,
    "_updates": [
      {
        "path": "/userSessionInactivityTimeoutMinutes",
        "newValue": 30,
        "oldValue": 60
      }
    ]
  }
}
```


## Schemas

### attributeUpdate

An attribute update object that contains the change of an attribute.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | The updated attribute path. |
| `newValue` | `` | Yes | The new JSON value of the updated attribute. |
| `oldValue` | `` | Yes | The old JSON value of the updated attribute. |



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
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### ipPolicy

IP Policy resource object.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the IP Policy. |
| `name` | `string` | No | Descriptive name for the IP Policy. |
| `enabled` | `boolean` | No | Indicates whether the IP policy is enabled. |
| `editable` | `boolean` | No | Indicates whether the IP policy can be updated. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the IP Policy belongs to. |
| `createdAt` | `string` | No | The timestamp for when the IP Policy was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | the unique identifier of the user who created the IP Policy. |
| `deletable` | `boolean` | No | Indicates whether the IP policy can be deleted. |
| `updatedAt` | `string` | No | The timestamp for when the IP Policy was last updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | the unique identifier of the user who updated the IP Policy. |
| `allowedIps` | `string[]` | No | An array of allowed IP addresses. |
| `toggleable` | `boolean` | No | Indicates whether the IP policy can be enabled/disabled.. |


