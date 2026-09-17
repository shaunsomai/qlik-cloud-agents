---
source: https://qlik.dev/apis/event/core/roles/
last_updated: 2026-08-31T15:18:51+02:00
---

# Roles

Events emitted when roles are created, updated, or deleted in your tenant.

## Table of Contents

### system-events.roles

- [com.qlik.core.role.created](#comqlikcorerolecreated)
- [com.qlik.core.role.deleted](#comqlikcoreroledeleted)
- [com.qlik.core.role.synced](#comqlikcorerolesynced)
- [com.qlik.core.role.updated](#comqlikcoreroleupdated)

## Events published on the `system-events.roles` channel

### com.qlik.core.role.created

**Title:** Role created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a role is created.
Permission lists are not included in the payload due to payload size limits, but assigned scopes for custom roles will be included.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.role.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `role` | No | Represents a role entity. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. Custom roles can have user-defined names. |
| `type` | `string` | No | Indicates whether role is system/default or custom. Allowed values: default \| custom. |
| `level` | `string` | Yes | Indicates whether it is a user or admin-level role. Allowed values: admin \| user. |
| `canEdit` | `boolean` | No | Indicates whether role can be edited by users or not. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given role. Metadata: format = "uid". |
| `canDelete` | `boolean` | No | Indicates whether role can be deleted by users or not. |
| `createdAt` | `string` | No | Timestamp when the role was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created the role. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated the role. |
| `description` | `string` | No | Description of the role. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the role was last updated. Metadata: format = "date-time". |
| `assignedScopes` | `string[]` | No | Selection of scopes added to this role. |
| `userEntitlementType` | `string` | No | Indicates whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-03-22T10:01:02Z",
  "type": "com.qlik.core.role.created",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "aBcDeFgH1jKlMnOpQrStUvWxYz012345",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "TenantAdmin",
    "type": "default",
    "level": "admin",
    "canEdit": false,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "canDelete": false,
    "createdAt": "2021-03-22T10:01:02Z",
    "createdBy": "6228c560543c200449c13255",
    "updatedBy": "6228c560543c200449c13255",
    "description": "Administrator role for the tenant",
    "lastUpdatedAt": "2026-03-22T10:01:02Z",
    "assignedScopes": [
      "scope.read",
      "scope.update"
    ],
    "userEntitlementType": "fullUser"
  }
}
```


### com.qlik.core.role.deleted

**Title:** Role deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a role is deleted.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.role.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `role` | No | Represents a role entity. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. Custom roles can have user-defined names. |
| `type` | `string` | No | Indicates whether role is system/default or custom. Allowed values: default \| custom. |
| `level` | `string` | Yes | Indicates whether it is a user or admin-level role. Allowed values: admin \| user. |
| `canEdit` | `boolean` | No | Indicates whether role can be edited by users or not. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given role. Metadata: format = "uid". |
| `canDelete` | `boolean` | No | Indicates whether role can be deleted by users or not. |
| `createdAt` | `string` | No | Timestamp when the role was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created the role. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated the role. |
| `description` | `string` | No | Description of the role. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the role was last updated. Metadata: format = "date-time". |
| `assignedScopes` | `string[]` | No | Selection of scopes added to this role. |
| `userEntitlementType` | `string` | No | Indicates whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-03-22T10:01:02Z",
  "type": "com.qlik.core.role.deleted",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "aBcDeFgH1jKlMnOpQrStUvWxYz012345",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "TenantAdmin",
    "type": "default",
    "level": "admin",
    "canEdit": false,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "canDelete": false,
    "createdAt": "2021-03-22T10:01:02Z",
    "createdBy": "6228c560543c200449c13255",
    "updatedBy": "6228c560543c200449c13255",
    "description": "Administrator role for the tenant",
    "lastUpdatedAt": "2026-03-22T10:01:02Z",
    "assignedScopes": [
      "scope.read",
      "scope.update"
    ],
    "userEntitlementType": "fullUser"
  }
}
```


### com.qlik.core.role.synced

**Title:** Role synced

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when role definitions are synchronized across the platform.
Permission lists are not included in the payload due to payload size limits. Retrieve them from the roles API when required.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.role.synced". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Payload containing the roles that were synced. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | `object[]` | No | Represents a role entity. |

<details>
<summary>Properties of `roles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. Custom roles can have user-defined names. |
| `type` | `string` | No | Indicates whether role is system/default or custom. Allowed values: default \| custom. |
| `level` | `string` | Yes | Indicates whether it is a user or admin-level role. Allowed values: admin \| user. |
| `canEdit` | `boolean` | No | Indicates whether role can be edited by users or not. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given role. Metadata: format = "uid". |
| `canDelete` | `boolean` | No | Indicates whether role can be deleted by users or not. |
| `createdAt` | `string` | No | Timestamp when the role was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created the role. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated the role. |
| `description` | `string` | No | Description of the role. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the role was last updated. Metadata: format = "date-time". |
| `assignedScopes` | `string[]` | No | Selection of scopes added to this role. |
| `userEntitlementType` | `string` | No | Indicates whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-03-22T10:01:02Z",
  "type": "com.qlik.core.role.synced",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "aBcDeFgH1jKlMnOpQrStUvWxYz012345",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "roles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "TenantAdmin",
        "type": "default",
        "level": "admin",
        "canEdit": false,
        "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
        "canDelete": false,
        "createdAt": "2021-03-22T10:01:02Z",
        "createdBy": "6228c560543c200449c13255",
        "updatedBy": "6228c560543c200449c13255",
        "description": "Administrator role for the tenant",
        "lastUpdatedAt": "2026-03-22T10:01:02Z",
        "assignedScopes": [
          "scope.read",
          "scope.update"
        ],
        "userEntitlementType": "fullUser"
      }
    ]
  }
}
```


### com.qlik.core.role.updated

**Title:** Role updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a role is updated.
Permission lists are not included in the payload due to payload size limits.


**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.role.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `role` | No | The event data payload containing the updated role and the `_updates` field-level change set. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |
| `id` | `string` | Yes | Unique identifier for the role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. Custom roles can have user-defined names. |
| `type` | `string` | No | Indicates whether role is system/default or custom. Allowed values: default \| custom. |
| `level` | `string` | Yes | Indicates whether it is a user or admin-level role. Allowed values: admin \| user. |
| `canEdit` | `boolean` | No | Indicates whether role can be edited by users or not. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given role. Metadata: format = "uid". |
| `canDelete` | `boolean` | No | Indicates whether role can be deleted by users or not. |
| `createdAt` | `string` | No | Timestamp when the role was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created the role. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated the role. |
| `description` | `string` | No | Description of the role. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the role was last updated. Metadata: format = "date-time". |
| `assignedScopes` | `string[]` | No | Selection of scopes added to this role. |
| `userEntitlementType` | `string` | No | Indicates whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. |

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
  "time": "2026-03-22T10:01:02Z",
  "type": "com.qlik.core.role.updated",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "aBcDeFgH1jKlMnOpQrStUvWxYz012345",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "_updates": [
      {
        "path": "/attributePath",
        "newValue": "Dan",
        "oldValue": "Dylan"
      }
    ],
    "id": "507f191e810c19729de860ea",
    "name": "TenantAdmin",
    "type": "default",
    "level": "admin",
    "canEdit": false,
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "canDelete": false,
    "createdAt": "2021-03-22T10:01:02Z",
    "createdBy": "6228c560543c200449c13255",
    "updatedBy": "6228c560543c200449c13255",
    "description": "Administrator role for the tenant",
    "lastUpdatedAt": "2026-03-22T10:01:02Z",
    "assignedScopes": [
      "scope.read",
      "scope.update"
    ],
    "userEntitlementType": "fullUser"
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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### role

Represents a role entity.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the role. Metadata: format = "uid". |
| `name` | `string` | Yes | Name of the role. Custom roles can have user-defined names. |
| `type` | `string` | No | Indicates whether role is system/default or custom. Allowed values: default \| custom. |
| `level` | `string` | Yes | Indicates whether it is a user or admin-level role. Allowed values: admin \| user. |
| `canEdit` | `boolean` | No | Indicates whether role can be edited by users or not. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant associated with the given role. Metadata: format = "uid". |
| `canDelete` | `boolean` | No | Indicates whether role can be deleted by users or not. |
| `createdAt` | `string` | No | Timestamp when the role was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Unique identifier for the user who created the role. |
| `updatedBy` | `string` | No | Unique identifier for the user who last updated the role. |
| `description` | `string` | No | Description of the role. |
| `lastUpdatedAt` | `string` | Yes | Timestamp when the role was last updated. Metadata: format = "date-time". |
| `assignedScopes` | `string[]` | No | Selection of scopes added to this role. |
| `userEntitlementType` | `string` | No | Indicates whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. |



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


