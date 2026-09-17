---
source: https://qlik.dev/apis/event/user-identities/
last_updated: 2026-04-10T12:07:03Z
---

# User identities

Events emitted when user identities experience conflicts or are reassigned in a Qlik Cloud tenant.

## Table of Contents

### system-events.user-identity

- [com.qlik.user-identity.conflict](#comqlikuser-identityconflict)
- [com.qlik.user-identity.reassigned](#comqlikuser-identityreassigned)

## Events published on the `system-events.user-identity` channel

### com.qlik.user-identity.conflict

**Title:** Identity conflict

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when attempting to create a user with an existing identity.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.user-identity.conflict". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `data` | `object` | Yes | Data specific to the user identity conflict event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `matchedUsers` | `object[]` | Yes | Array of matched user objects. |

<details>
<summary>Properties of `matchedUsers`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes |  |
| `email` | `string` | Yes |  |
| `status` | `string` | Yes |  |
| `subject` | `string` | Yes |  |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.user-identity.conflict",
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
    "matchedUsers": [
      {
        "id": "LCkX6XCql7Owoea9HFfmxsMLxbnwd3pE",
        "email": "foo@bar.example",
        "status": "active",
        "subject": "auth0\\foo"
      },
      {
        "id": "FAkX2XCql4Owoea5HafmxsMLxbnwd3pE",
        "email": "foo@bar.example",
        "status": "active",
        "subject": "auth0\\bar"
      }
    ]
  }
}
```


### com.qlik.user-identity.reassigned

**Title:** Identity reassigned

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user is assigned a new identity.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.user-identity.reassigned". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `data` | `object` | Yes | Data specific to the user identity reassigned event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | Yes | User's email used to reassign. |
| `newSubject` | `string` | Yes | User's new subject in our DB. |
| `oldSubject` | `string` | Yes | User's old subject in our DB. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.user-identity.reassigned",
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
    "email": "foo@corp.example",
    "newSubject": "okta\\bar",
    "oldSubject": "auth0\\foo"
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



### userObject

Object containing user information.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes |  |
| `email` | `string` | Yes |  |
| `status` | `string` | Yes |  |
| `subject` | `string` | Yes |  |


