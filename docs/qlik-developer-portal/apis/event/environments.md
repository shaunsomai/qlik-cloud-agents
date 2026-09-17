---
source: https://qlik.dev/apis/event/environments/
last_updated: 2026-06-02T09:50:42Z
---

# Environments

Events emitted for environment creation, deletion, and configuration changes.

## Table of Contents

### system-events.spaces

- [com.qlik.v1.environment.created](#comqlikv1environmentcreated)
- [com.qlik.v1.environment.deleted](#comqlikv1environmentdeleted)
- [com.qlik.v1.environment.updated](#comqlikv1environmentupdated)

## Events published on the `system-events.spaces` channel

### com.qlik.v1.environment.created  _(deprecated)_

**Title:** Environment created

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is created in the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.environment.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
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
| `variables` | `object[]` | No | Key-value pairs. |
| `description` | `string` | No | Description of the environment. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.environment.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Default environment",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2025-03-07T23:47:53Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "variables": [
      {
        "key": "string",
        "value": "string"
      }
    ],
    "description": "Default environment"
  }
}
```


### com.qlik.v1.environment.deleted  _(deprecated)_

**Title:** Environment deleted

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is deleted from the tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.environment.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted environment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the deleted environment. |
| `name` | `string` | No |  |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.environment.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "string"
  }
}
```


### com.qlik.v1.environment.updated  _(deprecated)_

**Title:** Environment updated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Published when an environment is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.environment.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated environment. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the environment. |
| `name` | `string` | No | Name of the environment. |
| `createdAt` | `string` | No | Timestamp when the environment was created. Metadata: format = "date-time". |
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

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.environment.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Default environment",
    "createdAt": "2025-03-07T23:47:53Z",
    "updatedAt": "2025-03-07T23:47:53Z",
    "updatedBy": "00000000-0000-0000-0000-000000000000",
    "variables": [
      {
        "key": "string",
        "value": "string"
      }
    ],
    "description": "Default environment"
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
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### variable

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `key` | `string` | No | Variable key. |
| `value` | `string` | No | Variable value. |


