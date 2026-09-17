---
source: https://qlik.dev/apis/event/core/tenants/
last_updated: 2026-08-31T15:18:51+02:00
---

# Tenants

Events emitted when tenants are created, updated, deleted, deactivated, or reactivated in Qlik Cloud.

## Table of Contents

### system-events.tenants

- [com.qlik.core.tenant.allowed-deactivate](#comqlikcoretenantallowed-deactivate)
- [com.qlik.core.tenant.created](#comqlikcoretenantcreated)
- [com.qlik.core.tenant.deactivated](#comqlikcoretenantdeactivated)
- [com.qlik.core.tenant.deleted](#comqlikcoretenantdeleted)
- [com.qlik.core.tenant.disallowed-deactivate](#comqlikcoretenantdisallowed-deactivate)
- [com.qlik.core.tenant.reactivated](#comqlikcoretenantreactivated)
- [com.qlik.core.tenant.updated](#comqlikcoretenantupdated)

## Events published on the `system-events.tenants` channel

### com.qlik.core.tenant.allowed-deactivate

**Title:** Tenant deactivation allowed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when deactivation is allowed for a tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.allowed-deactivate". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the tenant. Contains the full tenant object. |

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
  "type": "com.qlik.core.tenant.allowed-deactivate",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.created

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
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the created tenant. Contains the full tenant object. |

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
  "type": "com.qlik.core.tenant.created",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.deactivated

**Title:** Tenant deactivated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the tenant is deactivated, either when its status changes from active to disabled or when its disallowed statuses are updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.deactivated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
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
  "type": "com.qlik.core.tenant.deactivated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.deleted

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
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the deleted tenant. Contains the full tenant object. |

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
  "type": "com.qlik.core.tenant.deleted",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.disallowed-deactivate

**Title:** Tenant deactivation disallowed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when deactivation is disallowed for a tenant.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.disallowed-deactivate". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the tenant. Contains the full tenant object. |

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
  "type": "com.qlik.core.tenant.disallowed-deactivate",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.reactivated

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
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.reactivated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the reactivated tenant. Contains the full tenant object. |

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
  "type": "com.qlik.core.tenant.reactivated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
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


### com.qlik.core.tenant.updated

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
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.tenant.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |
| `data` | `coreTenantData` | No | Details of the updated tenant. Contains the full tenant object plus the list of applied updates. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | Yes | Tenant name. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |
| `_updates` | `object[]` | Yes | Collection of updates performed on the resource, in JSON Pointer form. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | JSON Pointer path of the property that has changed. |
| `newValue` | `` | No | Value of the field after the update. The JSON value type depends on the field identified by path. |
| `oldValue` | `` | No | Value of the field before the update. The JSON value type depends on the field identified by path. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.core.tenant.updated",
  "source": "com.qlik/tenants",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f1f77bcf86cd799439011",
  "authtype": "tenants",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "authclaims": "{\"sub\":\"507f1f77bcf86cd799439011\"}",
  "toplevelresourceid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "Example Tenant",
    "hostnames": [
      "example-tenant.us.qlikcloud.com",
      "example-tenant.eu.qlikcloud.com"
    ],
    "_updates": [
      {
        "path": "/name",
        "newValue": "Example Tenant Updated",
        "oldValue": "Example Tenant"
      }
    ]
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
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/tenants". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Type of authentication context for the actor that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | Serialized authentication claims for the actor that triggered the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource related to the event. Only present on the Talend metadata updated event. |



### coreTenantData

The full tenant record. Core events publish the complete tenant object, so consumers may receive additional fields beyond those they rely on. Only id, name and hostnames are guaranteed; the remaining fields are present when set on the tenant.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier of the tenant. |
| `name` | `string` | Yes | Tenant name. |
| `hostnames` | `string[]` | Yes | List of hostname(s) associated with the tenant. |


