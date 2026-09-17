---
source: https://qlik.dev/apis/event/core/user-identities/
last_updated: 2026-08-31T15:18:51+02:00
---

# User identities

Events emitted when user identities experience conflicts or are reassigned in a Qlik Cloud tenant.

## Table of Contents

### system-events.user-identity

- [com.qlik.core.user-identity.conflicted](#comqlikcoreuser-identityconflicted)
- [com.qlik.core.user-identity.reassigned](#comqlikcoreuser-identityreassigned)

## Events published on the `system-events.user-identity` channel

### com.qlik.core.user-identity.conflicted

**Title:** Identity conflicted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when attempting to create a user with an existing identity.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.core.user-identity.conflicted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `meta` | `object` | No | Additional request metadata carried as a CloudEvents extension. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | W3C Trace Context tracestate header propagated with the event. |
| `traceparent` | `string` | No | W3C Trace Context traceparent header propagated with the event. |
| `data` | `object` | Yes | Data specific to the user identity conflicted event. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userAgent` | `string` | No | The User-Agent header of the request that triggered the event. |

</details>

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
  "type": "com.qlik.core.user-identity.conflicted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "meta": {
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
  },
  "userid": "605a18af2ab08cdbfad09259",
  "authtype": "service_account",
  "originip": "0.0.0.0",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\\\"iss\\\":\\\"qlik.api.internal/service\\\",\\\"sub\\\":\\\"service\\\",\\\"subType\\\":\\\"service\\\"}",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
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


### com.qlik.core.user-identity.reassigned

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
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.core.user-identity.reassigned". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `meta` | `object` | No | Additional request metadata carried as a CloudEvents extension. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | W3C Trace Context tracestate header propagated with the event. |
| `traceparent` | `string` | No | W3C Trace Context traceparent header propagated with the event. |
| `data` | `object` | Yes | Data specific to the user identity reassigned event. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userAgent` | `string` | No | The User-Agent header of the request that triggered the event. |

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | No | User's email used to reassign. |
| `newSubject` | `string` | Yes | User's new subject identifier in the identity database. |
| `oldSubject` | `string` | Yes | User's old subject identifier in the identity database. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.user-identity.reassigned",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "meta": {
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
  },
  "userid": "605a18af2ab08cdbfad09259",
  "authtype": "service_account",
  "originip": "0.0.0.0",
  "tenantid": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sessionid": "WZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\\\"iss\\\":\\\"qlik.api.internal/service\\\",\\\"sub\\\":\\\"service\\\",\\\"subType\\\":\\\"service\\\"}",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
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
| `meta` | `object` | No | Additional request metadata carried as a CloudEvents extension. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `originip` | `string` | No | Origin IP address. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | W3C Trace Context tracestate header propagated with the event. |
| `traceparent` | `string` | No | W3C Trace Context traceparent header propagated with the event. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userAgent` | `string` | No | The User-Agent header of the request that triggered the event. |

</details>



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


