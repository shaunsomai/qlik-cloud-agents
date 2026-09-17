---
source: https://qlik.dev/apis/event/core/group-settings/
last_updated: 2026-08-31T15:18:51+02:00
---

# Group settings

Events emitted when group settings are updated in a Qlik Cloud tenant.

## Table of Contents

### system-events.groups

- [com.qlik.core.group-setting.updated](#comqlikcoregroup-settingupdated)

## Events published on the `system-events.groups` channel

### com.qlik.core.group-setting.updated

**Title:** Group settings updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the group settings are updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.group-setting.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `updateObject` | No | The event data payload containing the updated group settings and the `_updates` field-level change set. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `created` | `string` | No | Timestamp when the group settings record was created. Metadata: format = "date-time". |
| `tenantId` | `string` | Yes | Unique identifier for the tenant. Metadata: format = "uid". |
| `lastUpdated` | `string` | No | Timestamp when the group settings record was last updated. Metadata: format = "date-time". |
| `syncIdpGroups` | `boolean` | No | Deprecated. Previously controlled whether groups from the identity provider were synchronized into Qlik Cloud. No longer used; group synchronization is now governed by autoCreateGroups. |
| `autoCreateGroups` | `boolean` | Yes | Whether to automatically create groups in Qlik Cloud when they appear in the identity provider. |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `` | No | JSON value of the field after the update. The value can be a scalar, array, object, or null, depending on the field. |
| `oldValue` | `` | No | JSON value of the field before the update. The value can be a scalar, array, object, or null, depending on the field. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-04-05T17:31:00Z",
  "type": "com.qlik.core.group-setting.updated",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "created": "2018-10-30T07:06:22Z",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "lastUpdated": "2018-10-30T07:06:22Z",
    "syncIdpGroups": false,
    "autoCreateGroups": false,
    "_updates": [
      {
        "path": "/attributePath",
        "newValue": "Dan",
        "oldValue": "Dylan"
      }
    ]
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
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### groupSettings

Group settings for a tenant.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `created` | `string` | No | Timestamp when the group settings record was created. Metadata: format = "date-time". |
| `tenantId` | `string` | Yes | Unique identifier for the tenant. Metadata: format = "uid". |
| `lastUpdated` | `string` | No | Timestamp when the group settings record was last updated. Metadata: format = "date-time". |
| `syncIdpGroups` | `boolean` | No | Deprecated. Previously controlled whether groups from the identity provider were synchronized into Qlik Cloud. No longer used; group synchronization is now governed by autoCreateGroups. |
| `autoCreateGroups` | `boolean` | Yes | Whether to automatically create groups in Qlik Cloud when they appear in the identity provider. |



### updateObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `` | No | JSON value of the field after the update. The value can be a scalar, array, object, or null, depending on the field. |
| `oldValue` | `` | No | JSON value of the field before the update. The value can be a scalar, array, object, or null, depending on the field. |

</details>


