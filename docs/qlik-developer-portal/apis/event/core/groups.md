---
source: https://qlik.dev/apis/event/core/groups/
last_updated: 2026-08-31T15:18:51+02:00
---

# Groups

Events emitted when groups are created, updated, deleted, or have their user membership modified in a Qlik Cloud tenant.

## Table of Contents

### system-events.groups

- [com.qlik.core.group.created](#comqlikcoregroupcreated)
- [com.qlik.core.group.deleted](#comqlikcoregroupdeleted)
- [com.qlik.core.group.updated](#comqlikcoregroupupdated)
- [com.qlik.core.group.users.modified](#comqlikcoregroupusersmodified)

## Events published on the `system-events.groups` channel

### com.qlik.core.group.created

**Title:** Group created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a group is created in the tenant.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.group.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `groupData` | No | Represents a group. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the group. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the group as it appears in the identity provider. |
| `idpId` | `string` | No | Unique identifier for the source identity provider. Metadata: format = "uid". |
| `status` | `string` | Yes | Current status for the group within the platform. Allowed values: active \| disabled. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given group. Metadata: format = "uid". |
| `createdAt` | `string` | Yes | Timestamp when the group was created in the platform. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created this group. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated this group. |
| `description` | `string` | No | User-defined description for custom groups. |
| `providerType` | `string` | No | The type of provider for the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the group. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-04-05T17:31:00Z",
  "type": "com.qlik.core.group.created",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "Development",
    "idpId": "4ecbe7f9e8c1c9092c000027",
    "status": "active",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "string",
    "updatedBy": "string",
    "description": "Development team group",
    "providerType": "idp",
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "2021-03-22T10:01:02Z"
  }
}
```


### com.qlik.core.group.deleted

**Title:** Group deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a group is removed from the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.group.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `groupData` | No | Represents a group. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the group. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the group as it appears in the identity provider. |
| `idpId` | `string` | No | Unique identifier for the source identity provider. Metadata: format = "uid". |
| `status` | `string` | Yes | Current status for the group within the platform. Allowed values: active \| disabled. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given group. Metadata: format = "uid". |
| `createdAt` | `string` | Yes | Timestamp when the group was created in the platform. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created this group. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated this group. |
| `description` | `string` | No | User-defined description for custom groups. |
| `providerType` | `string` | No | The type of provider for the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the group. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-04-05T17:31:00Z",
  "type": "com.qlik.core.group.deleted",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "Development",
    "idpId": "4ecbe7f9e8c1c9092c000027",
    "status": "active",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "string",
    "updatedBy": "string",
    "description": "Development team group",
    "providerType": "idp",
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "2021-03-22T10:01:02Z"
  }
}
```


### com.qlik.core.group.updated

**Title:** Group updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a group is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.group.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `updateObject` | No | The event data payload containing the updated group and the `_updates` field-level change set. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the group. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the group as it appears in the identity provider. |
| `idpId` | `string` | No | Unique identifier for the source identity provider. Metadata: format = "uid". |
| `status` | `string` | Yes | Current status for the group within the platform. Allowed values: active \| disabled. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given group. Metadata: format = "uid". |
| `createdAt` | `string` | Yes | Timestamp when the group was created in the platform. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created this group. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated this group. |
| `description` | `string` | No | User-defined description for custom groups. |
| `providerType` | `string` | No | The type of provider for the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the group. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |

</details>

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
  "type": "com.qlik.core.group.updated",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "Development",
    "idpId": "4ecbe7f9e8c1c9092c000027",
    "status": "active",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "string",
    "updatedBy": "string",
    "description": "Development team group",
    "providerType": "idp",
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "2021-03-22T10:01:02Z",
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


### com.qlik.core.group.users.modified

**Title:** Group modified affecting multiple users

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a group has been updated or deleted, with a list of affected users.
For large groups, multiple events are sent, each with different `affectedUsers`, for
the same group update/delete event. Check `fullyProcessed` to determine if additional events are coming.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.group.users.modified". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `updateObject` | No | The event data payload containing the modified group, affected users, processing status, deletion status, and the `_updates` field-level change set. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the group. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the group as it appears in the identity provider. |
| `idpId` | `string` | No | Unique identifier for the source identity provider. Metadata: format = "uid". |
| `status` | `string` | Yes | Current status for the group within the platform. Allowed values: active \| disabled. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given group. Metadata: format = "uid". |
| `createdAt` | `string` | Yes | Timestamp when the group was created in the platform. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created this group. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated this group. |
| `description` | `string` | No | User-defined description for custom groups. |
| `providerType` | `string` | No | The type of provider for the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the group. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |
| `deleted` | `boolean` | No | Describes whether the group was deleted (true) or only updated (false). |
| `affectedUsers` | `string[]` | No | A list of user original IDs affected by this group update or delete. |
| `fullyProcessed` | `boolean` | No | Describes whether all affected users are included in this event or if additional events will be sent for the same group change. |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |

</details>

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
  "type": "com.qlik.core.group.users.modified",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "Development",
    "idpId": "4ecbe7f9e8c1c9092c000027",
    "status": "active",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "createdAt": "2021-03-21T17:32:28Z",
    "createdBy": "string",
    "updatedBy": "string",
    "description": "Development team group",
    "providerType": "idp",
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "2021-03-22T10:01:02Z",
    "_updates": [
      {
        "path": "/attributePath",
        "newValue": "Dan",
        "oldValue": "Dylan"
      }
    ],
    "deleted": true,
    "affectedUsers": [
      "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT"
    ],
    "fullyProcessed": true
  }
}
```


## Schemas

### assignedRoles

**Type:** `object[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |



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



### groupData

Represents a group.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the group. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the group as it appears in the identity provider. |
| `idpId` | `string` | No | Unique identifier for the source identity provider. Metadata: format = "uid". |
| `status` | `string` | Yes | Current status for the group within the platform. Allowed values: active \| disabled. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given group. Metadata: format = "uid". |
| `createdAt` | `string` | Yes | Timestamp when the group was created in the platform. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created this group. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated this group. |
| `description` | `string` | No | User-defined description for custom groups. |
| `providerType` | `string` | No | The type of provider for the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the group. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for this role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. |
| `type` | `string` | Yes | Whether the role is a default Qlik role or a custom role. Allowed values: default \| custom. |
| `level` | `string` | Yes | Role level (admin or user). Allowed values: admin \| user. |

</details>



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


