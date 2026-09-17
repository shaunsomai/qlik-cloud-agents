---
source: https://qlik.dev/apis/event/tenants/
last_updated: 2026-04-10T12:07:03Z
---

# Tenants

Events emitted when tenants are created, updated, deleted, deactivated, or reactivated in Qlik Cloud.

## Table of Contents

### system-events.tenants

- [com.qlik.v1.tenant.allowed-deactivate](#comqlikv1tenantallowed-deactivate)
- [com.qlik.tenant.created](#comqliktenantcreated)
- [com.qlik.v1.tenant.deactivated](#comqlikv1tenantdeactivated)
- [com.qlik.tenant.deleted](#comqliktenantdeleted)
- [com.qlik.v1.tenant.disallowed-deactivate](#comqlikv1tenantdisallowed-deactivate)
- [com.qlik.v1.tenant.reactivated](#comqlikv1tenantreactivated)
- [com.qlik.tenant.updated](#comqliktenantupdated)

## Events published on the `system-events.tenants` channel

### com.qlik.v1.tenant.allowed-deactivate

**Title:** Tenant allowed deactivate

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when deactivation is allowed for a tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.tenant.allowed-deactivate". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | No | Tenant name. |
| `hostnames` | `string[]` | No | List of hostname(s) associated with the tenant. |
| `allowDeactivateUntil` | `string` | No | Timestamp until which the tenant can be deactivated. Metadata: format = "date-time". |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.tenant.allowed-deactivate",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "allowDeactivateUntil": "2026-06-24T18:28:31.301Z"
  }
}
```


### com.qlik.tenant.created

**Title:** Tenant created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new tenant is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.tenant.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the created tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | Yes | Tenant name. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |
| `licenseId` | `string` | No | License identifier associated with the tenant. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.tenant.created",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "licenseId": "9999000000003063"
  }
}
```


### com.qlik.v1.tenant.deactivated

**Title:** Tenant deactivated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the tenant status changes from active to disabled.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.tenant.deactivated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deactivated tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | Yes | Tenant name. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |
| `purgeDate` | `string` | No | Scheduled purge date when a user or OEM deactivates the tenant. Metadata: format = "date-time". |
| `statusesDisallowed` | `string[]` | No | List of statuses that are disallowed for the tenant. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.tenant.deactivated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "purgeDate": "2026-06-24T18:28:31.301Z",
    "statusesDisallowed": [
      "active"
    ]
  }
}
```


### com.qlik.tenant.deleted

**Title:** Tenant deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a tenant is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.tenant.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the deleted tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | Yes | Tenant name. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.tenant.deleted",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ]
  }
}
```


### com.qlik.v1.tenant.disallowed-deactivate

**Title:** Tenant disallowed deactivate

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when deactivation is disallowed for a tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.tenant.disallowed-deactivate". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | No | Tenant name. |
| `hostnames` | `string[]` | No | List of hostname(s) associated with the tenant. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.tenant.disallowed-deactivate",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ]
  }
}
```


### com.qlik.v1.tenant.reactivated

**Title:** Tenant reactivated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the tenant status changes from disabled to active.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.tenant.reactivated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the reactivated tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | No | Tenant name. |
| `hostnames` | `string[]` | No | List of hostname(s) associated with the tenant. |
| `statusesDisallowed` | `string[]` | No | List of statuses that are disallowed for the tenant. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.tenant.reactivated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "statusesDisallowed": [
      "active"
    ]
  }
}
```


### com.qlik.tenant.updated

**Title:** Tenant updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a tenant is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.tenant.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `object` | No | Details of the updated tenant. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `updates` | `object[]` | Yes | Collection of updates performed on the resource. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |
| `licenseId` | `string` | Yes | License identifier associated with the tenant. |
| `parentTenantId` | `string` | No | Parent license identifier associated with the tenant. |
| `capabilityBankId` | `string` | No | Capability bank identifier associated with the license. |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `newValue` | `string` | No | Value of the field after the update. |
| `oldValue` | `string` | No | Value of the field before the update. |
| `property` | `string` | No | Property that has changed. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.tenant.updated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "updates": [
      {
        "newValue": "Example Tenant Updated",
        "oldValue": "Example Tenant",
        "property": "name"
      }
    ],
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "licenseId": "9999000000003063"
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |


