---
source: https://qlik.dev/apis/event/spaces/
last_updated: 2026-06-02T09:50:42Z
---

# Spaces

Events emitted when spaces are created, updated, deleted, or when space members are modified.

## Table of Contents

### system-events.spaces

- [com.qlik.space.assignment.created](#comqlikspaceassignmentcreated)
- [com.qlik.space.assignment.deleted](#comqlikspaceassignmentdeleted)
- [com.qlik.space.assignment.updated](#comqlikspaceassignmentupdated)
- [com.qlik.space.created](#comqlikspacecreated)
- [com.qlik.space.deleted](#comqlikspacedeleted)
- [com.qlik.space.groups.cache.invalidated](#comqlikspacegroupscacheinvalidated)
- [com.qlik.space.settings.updated](#comqlikspacesettingsupdated)
- [com.qlik.space.share.created](#comqlikspacesharecreated)
- [com.qlik.space.share.deleted](#comqlikspacesharedeleted)
- [com.qlik.space.share.session.attached](#comqlikspacesharesessionattached)
- [com.qlik.space.share.updated](#comqlikspaceshareupdated)
- [com.qlik.space.updated](#comqlikspaceupdated)

## Events published on the `system-events.spaces` channel

### com.qlik.space.assignment.created  _(deprecated)_

**Title:** Space assignment created

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a user or group is assigned to a space.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.assignment.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created assignment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the assignment. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the assignment belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant the space belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the assignment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the assignment. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned to the Space. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.assignment.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "roles": [
      "facilitator"
    ],
    "spaceId": "string",
    "tenantId": "string",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "assigneeId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.space.assignment.deleted  _(deprecated)_

**Title:** Space assignment deleted

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space assignment is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.assignment.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted assignment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the assignment. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `spaceId` | `string` | Yes | Identifier of the space the assignment belongs to. |
| `spaceName` | `string` | Yes | Name of the space. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned to the space. |
| `description` | `string` | No | Description of the assignment. |
| `spaceDelete` | `boolean` | Yes | If true the assignment was deleted because its parent space was deleted. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.assignment.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "spaceId": "string",
    "spaceName": "string",
    "assigneeId": "string",
    "description": "string",
    "spaceDelete": true
  }
}
```


### com.qlik.space.assignment.updated  _(deprecated)_

**Title:** Space assignment updated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space assignment is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.assignment.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated assignment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the assignment. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the assignment belongs to. |
| `updatedAt` | `string` | Yes | Timestamp when the assignment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | Yes | Identifier of the user who updated the assignment. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned to the space. |
| `description` | `string` | No |  |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.assignment.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "roles": [
      "facilitator"
    ],
    "spaceId": "string",
    "updatedAt": "2025-03-07T23:47:53Z",
    "updatedBy": "string",
    "assigneeId": "string",
    "description": "string"
  }
}
```


### com.qlik.space.created  _(deprecated)_

**Title:** Space created

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is created in the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the space. |
| `name` | `string` | No | Name of the space. |
| `type` | `string` | Yes | Allowed values: managed \| shared \| data. |
| `ownerId` | `string` | Yes | Identifier of the space owner. |
| `tenantId` | `string` | Yes | Identifier of the tenant the space belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the space was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the space. |
| `description` | `string` | No | Description of the space. |
| `environment` | `object` | No | Environment details if the space belongs to an environment. |
| `environmentId` | `string` | No | Identifier of the environment the space belongs to. |

<details>
<summary>Properties of `environment`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Identifier of the environment. |
| `name` | `string` | No | Name of the environment. |
| `tenantId` | `string` | No | Identifier of the tenant. |
| `createdAt` | `string` | No | Timestamp when the environment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the environment. |
| `updatedAt` | `string` | No | Timestamp when the environment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | Identifier of the user who last updated the environment. |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the environment. |

<details>
<summary>Properties of `variables`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Public space",
    "type": "managed",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "description": "Publicly available space",
    "environment": {
      "id": "00000000-0000-0000-0000-000000000000",
      "name": "Production",
      "tenantId": "00000000-0000-0000-0000-000000000000",
      "createdAt": "2025-03-07T23:47:53Z",
      "createdBy": "00000000-0000-0000-0000-000000000000",
      "updatedAt": "2025-03-07T23:47:53Z",
      "updatedBy": "00000000-0000-0000-0000-000000000000",
      "variables": [
        {
          "key": "string",
          "value": "string"
        }
      ],
      "description": "Production environment"
    },
    "environmentId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.space.deleted  _(deprecated)_

**Title:** Space deleted

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is deleted from the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the deleted space. |
| `name` | `string` | No |  |
| `ownerId` | `string` | No |  |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "string",
    "ownerId": "string"
  }
}
```


### com.qlik.space.groups.cache.invalidated  _(deprecated)_

**Title:** Space groups cache invalidated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when the groups cache is invalidated for a user.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.groups.cache.invalidated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the groups cache invalidation. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | Yes | Identifier of the user related to the event. |
| `tenantId` | `string` | Yes | Identifier of the tenant related to the event. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.groups.cache.invalidated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "userId": "00000000-0000-0000-0000-000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.space.settings.updated  _(deprecated)_

**Title:** Space settings updated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when the space settings are updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.settings.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated space settings. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant. |
| `allowShares` | `boolean` | Yes | Whether app sharing is allowed in the space. |
| `allowOffline` | `boolean` | Yes | Whether offline usage is allowed from shared or managed spaces. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.settings.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "allowShares": true,
    "allowOffline": true
  }
}
```


### com.qlik.space.share.created  _(deprecated)_

**Title:** Space share created

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a new space share is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.share.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created share. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the share belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant. |
| `createdAt` | `string` | Yes | Timestamp when the share was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the share. |
| `spaceType` | `string` | Yes | Allowed values: managed \| shared \| data. |
| `assigneeId` | `string` | Yes | Unique identifier for the user or group assigned the share. |
| `resourceId` | `string` | Yes | Identifier for the resource being shared. |
| `description` | `string` | No | Description of the share. |
| `resourceName` | `string` | Yes | Name of the resource being shared. |
| `resourceType` | `string` | Yes | All supported resource types for sharing. Allowed values: app \| note. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.share.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "roles": [
      "facilitator"
    ],
    "spaceId": "00000000-0000-0000-0000-000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "spaceType": "managed",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "resourceId": "string",
    "description": "Shared app for science",
    "resourceName": "string",
    "resourceType": "app"
  }
}
```


### com.qlik.space.share.deleted  _(deprecated)_

**Title:** Space share deleted

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space share is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.share.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted share. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `spaceId` | `string` | Yes | Identifier of the space the share belongs to. |
| `spaceName` | `string` | Yes | Name of the space. |
| `assigneeId` | `string` | Yes | Unique identifier for the user or group assigned the share. |
| `resourceId` | `string` | Yes |  |
| `description` | `string` | No | Description of the share. |
| `spaceDelete` | `boolean` | Yes | If true the share was deleted because its parent space was deleted. |
| `resourceName` | `string` | Yes | Name of the resource being shared. |
| `resourceType` | `string` | Yes | All supported resource types for sharing. Allowed values: app \| note. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.share.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "spaceId": "00000000-0000-0000-0000-000000000000",
    "spaceName": "Accounting",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "resourceId": "string",
    "description": "Shared app for science",
    "spaceDelete": true,
    "resourceName": "string",
    "resourceType": "app"
  }
}
```


### com.qlik.space.share.session.attached  _(deprecated)_

**Title:** Space share session attached

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a session is attached to a space share.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.share.session.attached". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the share session attachment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `sessionId` | `string` | Yes | Identifier of the session. |
| `assigneeId` | `string` | Yes | Unique identifier for the user or group assigned the share. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.share.session.attached",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "sessionId": "00000000-0000-0000-0000-000000000000",
    "assigneeId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.space.share.updated  _(deprecated)_

**Title:** Space share updated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space share is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.share.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated share. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `linkId` | `string` | Yes | Identifier of the share link. |
| `spaceId` | `string` | Yes | Identifier of the space the share belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant related to the event. |
| `createdAt` | `string` | Yes | Timestamp when the share was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the share. |
| `spaceType` | `string` | Yes | Allowed values: managed \| shared \| data. |
| `updatedAt` | `string` | Yes | Timestamp when the share was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | Identifier of the user who updated the share. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned the share. |
| `resourceId` | `string` | Yes | Identifier for the resource being shared. |
| `resourceName` | `string` | Yes | Name of the resource being shared. |
| `resourceType` | `string` | Yes | All supported resource types for sharing. Allowed values: app \| note. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.share.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "roles": [
      "facilitator"
    ],
    "linkId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "00000000-0000-0000-0000-000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "spaceType": "managed",
    "updatedAt": "2025-03-07T23:47:53Z",
    "updatedBy": "00000000-0000-0000-0000-000000000000",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "resourceId": "00000000-0000-0000-0000-000000000000",
    "resourceName": "SomeApp",
    "resourceType": "app"
  }
}
```


### com.qlik.space.updated  _(deprecated)_

**Title:** Space updated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.space.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the space. |
| `name` | `string` | No | Name of the space. |
| `type` | `string` | No | Allowed values: managed \| shared \| data. |
| `ownerId` | `string` | Yes | Identifier of the space owner. |
| `createdAt` | `string` | No | Timestamp when the space was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the space was updated. Metadata: format = "date-time". |
| `description` | `string` | No | Description of the space. |
| `environment` | `object` | No | Environment details if the space belongs to an environment. |
| `environmentId` | `string` | No | Identifier of the environment the space belongs to. |

<details>
<summary>Properties of `environment`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Identifier of the environment. |
| `name` | `string` | No | Name of the environment. |
| `tenantId` | `string` | No | Identifier of the tenant. |
| `createdAt` | `string` | No | Timestamp when the environment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the environment. |
| `updatedAt` | `string` | No | Timestamp when the environment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | Identifier of the user who last updated the environment. |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the environment. |

<details>
<summary>Properties of `variables`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.space.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Public space",
    "type": "managed",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "updatedAt": "2025-03-07T23:47:53Z",
    "description": "Publicly available space",
    "environment": {
      "id": "00000000-0000-0000-0000-000000000000",
      "name": "Production",
      "tenantId": "00000000-0000-0000-0000-000000000000",
      "createdAt": "2025-03-07T23:47:53Z",
      "createdBy": "00000000-0000-0000-0000-000000000000",
      "updatedAt": "2025-03-07T23:47:53Z",
      "updatedBy": "00000000-0000-0000-0000-000000000000",
      "variables": [
        {
          "key": "string",
          "value": "string"
        }
      ],
      "description": "Production environment"
    },
    "environmentId": "00000000-0000-0000-0000-000000000000"
  }
}
```


## Schemas

### assignmentTypes

Type of assignee for a space assignment.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assignmentTypes` | `string` | No | Type of assignee for a space assignment. Allowed values: user \| group. |



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

Additional metadata and custom fields

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### shareResourceTypes

All supported resource types for sharing.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shareResourceTypes` | `string` | No | All supported resource types for sharing. Allowed values: app \| note. |



### spaceRoles

**Type:** `string[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceRoles` | `string[]` | No | Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |



### spaceTypes

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceTypes` | `string` | No | Allowed values: managed \| shared \| data. |



### variable

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |


