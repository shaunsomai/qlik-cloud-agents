---
source: https://qlik.dev/apis/event/core/spaces/
last_updated: 2026-08-31T15:18:51+02:00
---

# Spaces

Events emitted when spaces are created, updated, deleted, or when space members are modified.

## Table of Contents

### system-events.spaces

- [com.qlik.core.space.assignment.created](#comqlikcorespaceassignmentcreated)
- [com.qlik.core.space.assignment.deleted](#comqlikcorespaceassignmentdeleted)
- [com.qlik.core.space.assignment.updated](#comqlikcorespaceassignmentupdated)
- [com.qlik.core.space.created](#comqlikcorespacecreated)
- [com.qlik.core.space.deleted](#comqlikcorespacedeleted)
- [com.qlik.core.space.request.approved](#comqlikcorespacerequestapproved)
- [com.qlik.core.space.request.created](#comqlikcorespacerequestcreated)
- [com.qlik.core.space.request.deleted](#comqlikcorespacerequestdeleted)
- [com.qlik.core.space.settings.updated](#comqlikcorespacesettingsupdated)
- [com.qlik.core.space.share.created](#comqlikcorespacesharecreated)
- [com.qlik.core.space.share.deleted](#comqlikcorespacesharedeleted)
- [com.qlik.core.space.share.updated](#comqlikcorespaceshareupdated)
- [com.qlik.core.space.updated](#comqlikcorespaceupdated)

## Events published on the `system-events.spaces` channel

### com.qlik.core.space.assignment.created

**Title:** Space assignment created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user or group is assigned to a space.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.assignment.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created assignment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the assignment. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the assignment belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant the space belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the assignment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the assignment. |
| `spaceType` | `string` | No | The type of the space. Allowed values: managed \| shared \| data. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned to the space. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.assignment.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
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
    "assigneeId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.core.space.assignment.deleted

**Title:** Space assignment deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space assignment is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.assignment.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
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
  "type": "com.qlik.core.space.assignment.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
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


### com.qlik.core.space.assignment.updated

**Title:** Space assignment updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space assignment is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.assignment.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated assignment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the assignment. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the assignment belongs to. |
| `updatedAt` | `string` | Yes | Timestamp when the assignment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | Yes | Identifier of the user who updated the assignment. |
| `assigneeId` | `string` | Yes | Identifier of the user or group assigned to the space. |
| `description` | `string` | No | Description of the assignment. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.assignment.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "roles": [
      "facilitator"
    ],
    "spaceId": "00000000-0000-0000-0000-000000000000",
    "updatedAt": "2025-03-07T23:47:53Z",
    "updatedBy": "string",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "description": "string"
  }
}
```


### com.qlik.core.space.created

**Title:** Space created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is created in the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the space. |
| `name` | `string` | No | Name of the space. |
| `type` | `string` | Yes | The type of the space. Allowed values: managed \| shared \| data. |
| `ownerId` | `string` | Yes | Identifier of the space owner. |
| `tenantId` | `string` | Yes | Identifier of the tenant the space belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the space was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the space. |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the space. |
| `environment` | `object` | No | Environment details if the space belongs to an environment. |
| `environmentId` | `string` | No | Identifier of the environment the space belongs to. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |

</details>

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
| `spaceCount` | `integer` | No | Number of spaces in the environment. |
| `description` | `string` | No | Description of the environment. |
| `permissions` | `string[]` | No | Permissions the requesting user has on the environment. |
| `defaultDesignEnvironment` | `boolean` | No | Whether this is the default design environment. |
| `environmentConfiguration` | `string` | No | Configuration of the environment. |

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
  "type": "com.qlik.core.space.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Public space",
    "type": "managed",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "variables": [
      {
        "key": "string",
        "value": "string",
        "updatedAt": "2025-03-07T23:47:53Z"
      }
    ],
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
          "value": "string",
          "updatedAt": "2025-03-07T23:47:53Z"
        }
      ],
      "spaceCount": 5,
      "description": "Production environment",
      "permissions": [
        "read",
        "update"
      ],
      "defaultDesignEnvironment": false,
      "environmentConfiguration": "{\"key\":\"value\"}"
    },
    "environmentId": "00000000-0000-0000-0000-000000000000"
  }
}
```


### com.qlik.core.space.deleted

**Title:** Space deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is deleted from the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the deleted space. |
| `name` | `string` | No | Name of the space. |
| `ownerId` | `string` | No | Identifier of the space owner. |
| `description` | `string` | No | Description of the space. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "string",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "description": "Publicly available space"
  }
}
```


### com.qlik.core.space.request.approved

**Title:** Space request approved

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space access request is approved.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.request.approved". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the approved request. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the request. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space related to the request. |
| `tenantId` | `string` | Yes | Identifier of the tenant the request belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the request was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who approved the access request. |
| `assigneeId` | `string` | Yes | Identifier of the user who is assigned the resource. |
| `resourceId` | `string` | No | Identifier of the resource related to the request. |
| `description` | `string` | Yes | Description of the request. |
| `resourceType` | `string` | No | Type of the resource related to the request. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.request.approved",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "roles": [
      "consumer"
    ],
    "spaceId": "00000000-0000-0000-0000-000000001",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "resourceId": "00000000-0000-0000-0000-000000000001",
    "description": "Request for accessing the resource",
    "resourceType": "app"
  }
}
```


### com.qlik.core.space.request.created

**Title:** Space request created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space access request is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.request.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created request. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the request. |
| `type` | `string` | Yes | Type of request. Allowed values: assignment \| share. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space related to the request. |
| `tenantId` | `string` | Yes | Identifier of the tenant the request belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the request was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the access request. |
| `resourceId` | `string` | No | Identifier of the resource related to the request. |
| `description` | `string` | Yes | Description of the request. |
| `overWritten` | `boolean` | No | Indicates if the request was over-written by another request. |
| `resourceName` | `string` | No | Name of the resource related to the request. |
| `resourceType` | `string` | No | Type of the resource related to the request. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.request.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "assignment",
    "roles": [
      "consumer"
    ],
    "spaceId": "12345678-abcd-abcd-abcd-abcd12345678",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000001",
    "resourceId": "12345678-abcd-abcd-abcd-abcd12345678",
    "description": "Request for accessing the resource 123",
    "overWritten": false,
    "resourceName": "My App",
    "resourceType": "app"
  }
}
```


### com.qlik.core.space.request.deleted

**Title:** Space request deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space access request is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.request.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted request. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the request. |
| `type` | `string` | Yes | Type of request. Allowed values: assignment \| share. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space related to the request. |
| `tenantId` | `string` | Yes | Identifier of the tenant the request belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the request was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who deleted the access request. |
| `resourceId` | `string` | No | Identifier of the resource related to the request. |
| `description` | `string` | Yes | Description of the request. |
| `resourceType` | `string` | No | Type of the resource related to the request. |
| `requestedUserId` | `string` | Yes | Identifier of the user for whom access was requested. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.request.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "assignment",
    "roles": [
      "consumer"
    ],
    "spaceId": "00000000-0000-0000-0000-000000001234",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "resourceId": "12345678-abcd-abcd-abcd-abcd12345678",
    "description": "Request for accessing the resource 123",
    "resourceType": "app",
    "requestedUserId": "00000000-0000-0000-0000-000000000001"
  }
}
```


### com.qlik.core.space.settings.updated

**Title:** Space settings updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the space settings are updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.settings.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated space settings. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant. |
| `updatedAt` | `string` | No | Timestamp when the settings were updated. Metadata: format = "date-time". |
| `allowShares` | `boolean` | Yes | Whether app sharing is allowed in the tenant. |
| `allowOffline` | `boolean` | Yes | Whether offline usage is allowed from shared or managed spaces. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.settings.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "updatedAt": "2025-03-07T23:47:53Z",
    "allowShares": true,
    "allowOffline": true
  }
}
```


### com.qlik.core.space.share.created

**Title:** Space share created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new space share is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.share.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created share. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `spaceId` | `string` | Yes | Identifier of the space the share belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant. |
| `createdAt` | `string` | Yes | Timestamp when the share was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the share. |
| `spaceType` | `string` | Yes | The type of the space. Allowed values: managed \| shared \| data. |
| `assigneeId` | `string` | Yes | Unique identifier for the user or group assigned the share. |
| `resourceId` | `string` | Yes | Identifier for the resource being shared. |
| `resourceName` | `string` | Yes | Name of the resource being shared. |
| `resourceType` | `string` | Yes | All supported resource types for sharing. Allowed values: app \| note. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.share.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
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
    "resourceId": "00000000-0000-0000-0000-000000000000",
    "resourceName": "SomeApp",
    "resourceType": "app"
  }
}
```


### com.qlik.core.space.share.deleted

**Title:** Space share deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space share is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.share.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
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
| `resourceId` | `string` | Yes | Identifier for the resource being shared. |
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
  "type": "com.qlik.core.space.share.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "user",
    "spaceId": "00000000-0000-0000-0000-000000000000",
    "spaceName": "Accounting",
    "assigneeId": "00000000-0000-0000-0000-000000000000",
    "resourceId": "00000000-0000-0000-0000-000000000000",
    "description": "Shared app for science",
    "spaceDelete": true,
    "resourceName": "SomeApp",
    "resourceType": "app"
  }
}
```


### com.qlik.core.space.share.updated

**Title:** Space share updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space share is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.share.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated share. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the share. |
| `type` | `string` | Yes | Type of assignee for a space assignment. Allowed values: user \| group. |
| `roles` | `spaceRoles[]` | Yes | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |
| `linkId` | `string` | Yes | Identifier of the share link. |
| `spaceId` | `string` | Yes | Identifier of the space the share belongs to. |
| `tenantId` | `string` | Yes | Identifier of the tenant related to the event. |
| `createdAt` | `string` | Yes | Timestamp when the share was created. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | Identifier of the user who created the share. |
| `spaceType` | `string` | Yes | The type of the space. Allowed values: managed \| shared \| data. |
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
  "type": "com.qlik.core.space.share.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
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


### com.qlik.core.space.updated

**Title:** Space updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a space is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.space.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated space. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the space. |
| `name` | `string` | No | Name of the space. |
| `type` | `string` | No | The type of the space. Allowed values: managed \| shared \| data. |
| `ownerId` | `string` | Yes | Identifier of the space owner. |
| `createdAt` | `string` | No | Timestamp when the space was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the space was updated. Metadata: format = "date-time". |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the space. |
| `environment` | `object` | No | Environment details if the space belongs to an environment. |
| `previousName` | `string` | No | Previous name of the space before the update. |
| `restrictions` | `object[]` | No | Restrictions applied to the space. |
| `environmentId` | `string` | No | Identifier of the environment the space belongs to. |
| `previousOwnerId` | `string` | No | Identifier of the previous space owner before the update. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |

</details>

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
| `spaceCount` | `integer` | No | Number of spaces in the environment. |
| `description` | `string` | No | Description of the environment. |
| `permissions` | `string[]` | No | Permissions the requesting user has on the environment. |
| `defaultDesignEnvironment` | `boolean` | No | Whether this is the default design environment. |
| `environmentConfiguration` | `string` | No | Configuration of the environment. |

<details>
<summary>Properties of `variables`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `restrictions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Identifier of the restriction. |
| `code` | `string` | No | Code of the restriction. |
| `action` | `string` | No | Action associated with the restriction. |
| `description` | `string` | No | Description of the restriction. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.space.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Public space",
    "type": "managed",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "updatedAt": "2025-03-07T23:47:53Z",
    "variables": [
      {
        "key": "string",
        "value": "string",
        "updatedAt": "2025-03-07T23:47:53Z"
      }
    ],
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
          "value": "string",
          "updatedAt": "2025-03-07T23:47:53Z"
        }
      ],
      "spaceCount": 5,
      "description": "Production environment",
      "permissions": [
        "read",
        "update"
      ],
      "defaultDesignEnvironment": false,
      "environmentConfiguration": "{\"key\":\"value\"}"
    },
    "previousName": "Old space name",
    "restrictions": [
      {
        "id": "00000000-0000-0000-0000-000000000000",
        "code": "SPACE_LIMIT_REACHED",
        "action": "block",
        "description": "The space has reached its resource limit."
      }
    ],
    "environmentId": "00000000-0000-0000-0000-000000000000",
    "previousOwnerId": "00000000-0000-0000-0000-000000000000"
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
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### requestTypes

Type of request.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requestTypes` | `string` | No | Type of request. Allowed values: assignment \| share. |



### restriction

Restriction applied to the space.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Identifier of the restriction. |
| `code` | `string` | No | Code of the restriction. |
| `action` | `string` | No | Action associated with the restriction. |
| `description` | `string` | No | Description of the restriction. |



### shareResourceTypes

All supported resource types for sharing.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shareResourceTypes` | `string` | No | All supported resource types for sharing. Allowed values: app \| note. |



### spaceRoles

The roles a user or group can be assigned within a space.

**Type:** `string[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceRoles` | `string[]` | No | The roles a user or group can be assigned within a space. Allowed values: facilitator \| producer \| consumer \| dataconsumer \| contributor \| operator \| publisher \| basicconsumer \| codeveloper. |



### spaceTypes

The type of the space.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceTypes` | `string` | No | The type of the space. Allowed values: managed \| shared \| data. |



### variable

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |


