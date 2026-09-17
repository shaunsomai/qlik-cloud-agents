---
source: https://qlik.dev/apis/event/core/api-keys/
last_updated: 2026-08-31T15:18:51+02:00
---

# API keys

Events emitted when API keys are created, updated, deleted, or when validation failed in a Qlik Cloud tenant.

## Table of Contents

### system-events.api-keys

- [com.qlik.core.api-key.created](#comqlikcoreapi-keycreated)
- [com.qlik.core.api-key.deleted](#comqlikcoreapi-keydeleted)
- [com.qlik.core.api-key.updated](#comqlikcoreapi-keyupdated)
- [com.qlik.core.api-key.validation.failed](#comqlikcoreapi-keyvalidationfailed)

## Events published on the `system-events.api-keys` channel

### com.qlik.core.api-key.created

**Title:** API key created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an API key is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Identifies the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.api-key.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `data` | `dataPayload` | No | Details of the created API key. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |
| `expiry` | `string` | Yes | API key expiry date. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00Z",
  "type": "com.qlik.core.api-key.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "api-keys",
  "originip": "0.0.0.0",
  "tenantid": "Rn8kQvY2wZ4pL7mX1jB6tC3dS5fH0gJ9",
  "sessionid": "9fBc2dE4gH6jK8mN0pQ2rS4tV6wX8yZ0",
  "authclaims": "{\"sub\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\"tenantId\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\"}",
  "data": {
    "id": "1fc531f9-1964-46d6-9267-256e707fac45",
    "sub": "62eadf5a01f72ccd31f37041",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z"
  }
}
```


### com.qlik.core.api-key.deleted

**Title:** API key deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an API key is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Identifies the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.api-key.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `data` | `dataPayload` | No | Details of the deleted API key. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |
| `expiry` | `string` | Yes | API key expiry date. |
| `status` | `string` | Yes | Status of the API key. Set to `deleted` when triggered by the owner, or `revoked` when triggered by a tenant admin. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00Z",
  "type": "com.qlik.core.api-key.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "api-keys",
  "originip": "0.0.0.0",
  "tenantid": "Rn8kQvY2wZ4pL7mX1jB6tC3dS5fH0gJ9",
  "sessionid": "9fBc2dE4gH6jK8mN0pQ2rS4tV6wX8yZ0",
  "authclaims": "{\"sub\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\"tenantId\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\"}",
  "data": {
    "id": "1fc531f9-1964-46d6-9267-256e707fac45",
    "sub": "62eadf5a01f72ccd31f37041",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z",
    "status": "deleted"
  }
}
```


### com.qlik.core.api-key.updated

**Title:** API key updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an API key is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Identifies the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.api-key.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `data` | `dataPayload` | No | Details of the updated API key. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |
| `expiry` | `string` | Yes | API key expiry date. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00Z",
  "type": "com.qlik.core.api-key.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "api-keys",
  "originip": "0.0.0.0",
  "tenantid": "Rn8kQvY2wZ4pL7mX1jB6tC3dS5fH0gJ9",
  "sessionid": "9fBc2dE4gH6jK8mN0pQ2rS4tV6wX8yZ0",
  "authclaims": "{\"sub\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\"tenantId\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\"}",
  "data": {
    "id": "1fc531f9-1964-46d6-9267-256e707fac45",
    "sub": "62eadf5a01f72ccd31f37041",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z"
  }
}
```


### com.qlik.core.api-key.validation.failed

**Title:** API key validation failed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when API key validation fails. Only published for externalClient API keys.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Identifies the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.api-key.validation.failed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `data` | `object` | No | Details of the failed API key validation. |
| `toplevelresourceid` | `string` | No | API key identifier. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jti` | `string` | Yes | API key identifier (MongoDB ObjectId). |
| `code` | `string` | Yes | Error code. |
| `idpId` | `string` | No | Identity provider identifier tied to the externalClient. |
| `subType` | `string` | Yes | API key subType. |
| `description` | `string` | Yes | Error description. |
| `createdByUser` | `string` | No | Identifier of the user who created the key. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00Z",
  "type": "com.qlik.core.api-key.validation.failed",
  "source": "com.qlik/my-service",
  "specversion": "1.0.2",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "api-keys",
  "originip": "0.0.0.0",
  "tenantid": "Rn8kQvY2wZ4pL7mX1jB6tC3dS5fH0gJ9",
  "sessionid": "9fBc2dE4gH6jK8mN0pQ2rS4tV6wX8yZ0",
  "authclaims": "{\"sub\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\"tenantId\":\"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\"}",
  "data": {
    "jti": "62eadf5a01f72ccd31f37041",
    "code": "APIKEYS-18",
    "idpId": "62eaddcce5ff30cabc6f67e8",
    "subType": "externalClient",
    "description": "The api key is either expired or revoked",
    "createdByUser": "62eadf5a01f72ccd31f37041"
  },
  "toplevelresourceid": "1fc531f9-1964-46d6-9267-256e707fac45"
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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |



### dataPayload

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |


