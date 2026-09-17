---
source: https://qlik.dev/apis/event/user-sessions/
last_updated: 2026-04-10T12:07:03Z
---

# User sessions

Events emitted when user sessions begin or end in a Qlik Cloud tenant.

## Table of Contents

### system-events.user-session

- [com.qlik.user-session.begin](#comqlikuser-sessionbegin)
- [com.qlik.user-session.end](#comqlikuser-sessionend)

## Events published on the `system-events.user-session` channel

### com.qlik.user-session.begin

**Title:** Session begin

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user session is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.user-session.begin". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `data` | `object` | Yes | Data specific to the user session begin event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `idpId` | `string` | No | Identifier of the identity provider through which the session was initiated. `null` if user logged in using Qlik Account. |
| `source` | `string` | No | The source of the event. Allowed values: com.qlik/edge-auth. |
| `subject` | `string` | No | User's subject in our DB. |
| `recovery` | `boolean` | No | Whether the session is part of a recovery login. |
| `userType` | `string` | No | The user's type, only specified for anonymous users. Allowed values: anonymous. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.user-session.begin",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "authtype": "service_account",
  "originip": "0.0.0.0",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\\\"iss\\\":\\\"qlik.api.internal/service\\\",\\\"sub\\\":\\\"service\\\",\\\"subType\\\":\\\"service\\\"}",
  "data": {
    "idpId": "661d627cef218789bbd67cc9",
    "source": "com.qlik/edge-auth",
    "subject": "auth0\\foo",
    "recovery": false
  }
}
```


### com.qlik.user-session.end

**Title:** Session end

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user session ends.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.user-session.end". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `data` | `object` | Yes | Data specific to the user session end event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `subject` | `string` | No | User's subject in our DB. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.user-session.end",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "605a18af2ab08cdbfad09259",
  "authtype": "service_account",
  "originip": "0.0.0.0",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\\\"iss\\\":\\\"qlik.api.internal/service\\\",\\\"sub\\\":\\\"service\\\",\\\"subType\\\":\\\"service\\\"}",
  "data": {
    "subject": "auth0\\foo"
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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |


