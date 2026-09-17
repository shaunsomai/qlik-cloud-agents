---
source: https://qlik.dev/apis/event/api-keys/
last_updated: 2026-04-10T12:07:03Z
---

# API keys

Events emitted when API keys are created, updated, deleted, or validated in a Qlik Cloud tenant.

## Table of Contents

### system-events.api-keys

- [com.qlik.api-key.created](#comqlikapi-keycreated)
- [com.qlik.api-key.deleted](#comqlikapi-keydeleted)
- [com.qlik.api-key.updated](#comqlikapi-keyupdated)
- [com.qlik.api-key.validated](#comqlikapi-keyvalidated)
- [com.qlik.v1.api-key.validation.failed](#comqlikv1api-keyvalidationfailed)

## Events published on the `system-events.api-keys` channel

### com.qlik.api-key.created

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.api-key.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `dataPayload` | No |  |

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
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.api-key.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "id123",
    "sub": "id123",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z"
  }
}
```


### com.qlik.api-key.deleted

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.api-key.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `dataPayload` | No |  |

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
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.api-key.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "id123",
    "sub": "id123",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z",
    "status": "deleted"
  }
}
```


### com.qlik.api-key.updated

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.api-key.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `dataPayload` | No |  |

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
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.api-key.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "id123",
    "sub": "id123",
    "subType": "user",
    "description": "description text for the key",
    "expiry": "2025-11-08T20:43:24.130Z"
  }
}
```


### com.qlik.api-key.validated

**Title:** API key validated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an API key is validated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.api-key.validated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `dataPayload` | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |
| `tenantId` | `string` | Yes | API key tenant identifier. |
| `createdByUser` | `string` | Yes | Identifier of the user who created the key. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.api-key.validated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "id123",
    "sub": "id123",
    "subType": "user",
    "description": "description text for the key",
    "tenantId": "id123",
    "createdByUser": "id123"
  }
}
```


### com.qlik.v1.api-key.validation.failed

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
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.api-key.validation.failed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `dataPayload` | No |  |
| `toplevelresourceid` | `string` | No | API key identifier. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | API key subType. |
| `description` | `string` | Yes | Error description. |
| `jti` | `string` | Yes | API key identifier. |
| `code` | `string` | Yes | Error code. |
| `idpId` | `string` | No | Identity provider identifier tied to the externalClient. |
| `createdByUser` | `string` | No | Identifier of the user who created the key. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.api-key.validation.failed",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "string",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "originip": "0.0.0.0",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "id123",
    "sub": "id123",
    "subType": "externalClient",
    "description": "The api key is either expired or revoked",
    "jti": "1fc531f9-1964-46d6-9267-256e707fac45",
    "code": "APIKEYS-18",
    "idpId": "62eaddcce5ff30cabc6f67e8",
    "createdByUser": "62eadf5a01f72ccd31f37041"
  },
  "toplevelresourceid": "1fc531f9-1964-46d6-9267-256e707fac45"
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



### dataPayload

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | API key identifier. |
| `sub` | `string` | Yes | Subject identifier. |
| `subType` | `string` | Yes | Subject type. |
| `description` | `string` | Yes | API key description. |


