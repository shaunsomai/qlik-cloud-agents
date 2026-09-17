---
source: https://qlik.dev/apis/event/api-keys-configs/
last_updated: 2026-04-10T12:07:03Z
---

# API key configs

Events emitted when API key configuration settings are updated in a Qlik Cloud tenant.

## Table of Contents

### system-events.api-keys

- [com.qlik.api-keys-config.updated](#comqlikapi-keys-configupdated)

## Events published on the `system-events.api-keys` channel

### com.qlik.api-keys-config.updated

**Title:** API key config updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the API key configuration is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.api-keys-config.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `object` | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apiKeysEnabled` | `boolean` | Yes | Determines if API keys functionality is enabled. |
| `maxKeysPerUser` | `string` | Yes | Maximum number of active API keys per user. |
| `maxApiKeyExpiry` | `string` | Yes | Maximum expiry for an API key, in ISO 8601 format. |
| `scimExternalClientExpiry` | `string` | Yes | Expiry of the SCIM `externalClient` token in ISO 8601 duration format, for example `P365D` for 365 days. Set when creating an `externalClient` API key for a SCIM-compatible identity provider. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.api-keys-config.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "apiKeysEnabled": true,
    "maxKeysPerUser": 5,
    "maxApiKeyExpiry": "PT24H",
    "scimExternalClientExpiry": "P365D"
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
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |


