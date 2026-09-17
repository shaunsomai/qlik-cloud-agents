---
source: https://qlik.dev/apis/event/groups/
last_updated: 2026-04-10T12:07:03Z
---

# Groups

Events emitted when groups are created, updated, deleted, or have their user membership modified in a Qlik Cloud tenant.

## Table of Contents

### system-events.groups

- [com.qlik.v1.group.created](#comqlikv1groupcreated)
- [com.qlik.v1.group.deleted](#comqlikv1groupdeleted)
- [com.qlik.v1.group.updated](#comqlikv1groupupdated)
- [com.qlik.v1.group.users.modified](#comqlikv1groupusersmodified)

## Events published on the `system-events.groups` channel

### com.qlik.v1.group.created

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.group.created". |
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
| `assignedRoles` | `assignedRoles[]` | No | Represents a role entity stored in the database. |
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
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.group.created",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "string",
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
    "description": "string",
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


### com.qlik.v1.group.deleted

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.group.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: default = "com.qlik/groups". |
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
| `assignedRoles` | `assignedRoles[]` | No | Represents a role entity stored in the database. |
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
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.group.deleted",
  "source": "com.qlik/groups",
  "specversion": "1.0",
  "datacontenttype": "string",
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
    "description": "string",
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


### com.qlik.v1.group.updated

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.group.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `updateObject` | No | Represents a group. |

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
| `assignedRoles` | `assignedRoles[]` | No | Represents a role entity stored in the database. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |
| `updates` | `object[]` | No | Collection of updates performed on the resource. |

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
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `string` | No | Value of the field after the update. |
| `oldValue` | `string` | No | Value of the field before the update. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.group.updated",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "string",
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
    "description": "string",
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
    "updates": [
      {
        "path": "/attributePath",
        "newValue": "Dan",
        "oldValue": "Dylan"
      }
    ]
  }
}
```


### com.qlik.v1.group.users.modified

**Title:** Multiple users' assigned groups have been modified

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.group.users.modified". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `updateObject` | No | Represents a group. |

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
| `assignedRoles` | `assignedRoles[]` | No | Represents a role entity stored in the database. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the group was last updated in the platform. Metadata: format = "date-time". |
| `updates` | `object[]` | No | Collection of updates performed on the resource. |
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
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `string` | No | Value of the field after the update. |
| `oldValue` | `string` | No | Value of the field before the update. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.group.users.modified",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "string",
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
    "description": "string",
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
    "updates": [
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
| `assignedRoles` | `assignedRoles[]` | No | Represents a role entity stored in the database. |
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
| `updates` | `object[]` | No | Collection of updates performed on the resource. |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `string` | No | Value of the field after the update. |
| `oldValue` | `string` | No | Value of the field before the update. |

</details>


