---
source: https://qlik.dev/apis/event/core/environments/
last_updated: 2026-08-31T15:18:51+02:00
---

# Environments

## Table of Contents

### system-events.spaces

- [com.qlik.core.environment.created](#comqlikcoreenvironmentcreated)
- [com.qlik.core.environment.deleted](#comqlikcoreenvironmentdeleted)
- [com.qlik.core.environment.updated](#comqlikcoreenvironmentupdated)

## Events published on the `system-events.spaces` channel

### com.qlik.core.environment.created

**Title:** Environment created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is created in the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.environment.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created environment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the environment. |
| `name` | `string` | No | Name of the environment. |
| `tenantId` | `string` | Yes | Identifier of the tenant the environment belongs to. |
| `createdAt` | `string` | Yes | Timestamp when the environment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the environment. |
| `updatedAt` | `string` | No | Timestamp when the environment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | Identifier of the user who updated the environment. |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the environment. |
| `permissions` | `string[]` | No | Permissions the requesting user has on the environment. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.environment.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Default environment",
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
    "description": "Default environment for the tenant.",
    "permissions": [
      "read",
      "update"
    ]
  }
}
```


### com.qlik.core.environment.deleted

**Title:** Environment deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is deleted from the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.environment.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted environment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the deleted environment. |
| `name` | `string` | No | Name of the deleted environment. |
| `tenantId` | `string` | No | Identifier of the tenant the environment belongs to. |
| `description` | `string` | No | Description of the environment. |
| `environmentDelete` | `boolean` | No | Indicates whether the environment itself was deleted. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.environment.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "string",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "description": "Default environment",
    "environmentDelete": false
  }
}
```


### com.qlik.core.environment.updated

**Title:** Environment updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.environment.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated environment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the environment. |
| `name` | `string` | No | Name of the environment. |
| `tenantId` | `string` | No | Identifier of the tenant the environment belongs to. |
| `createdAt` | `string` | No | Timestamp when the environment was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | Identifier of the user who created the environment. |
| `updatedAt` | `string` | Yes | Timestamp when the environment was updated. Metadata: format = "date-time". |
| `updatedBy` | `string` | No | Identifier of the user who updated the environment. |
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the environment. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.environment.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Default environment",
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
    "description": "Default environment for the tenant."
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

Additional metadata and custom fields

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### variable

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |
| `updatedAt` | `string` | No | Timestamp when the variable was last updated. Metadata: format = "date-time". |


