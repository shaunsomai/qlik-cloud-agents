---
source: https://qlik.dev/apis/event/core/oauth-tokens/
last_updated: 2026-08-31T15:18:51+02:00
---

# OAuth tokens

Events emitted when OAuth tokens are issued or revoked in a Qlik Cloud tenant.

## Table of Contents

### system-events.oauth-tokens

- [com.qlik.core.oauth-token.issued](#comqlikcoreoauth-tokenissued)
- [com.qlik.core.oauth-token.revoked](#comqlikcoreoauth-tokenrevoked)

## Events published on the `system-events.oauth-tokens` channel

### com.qlik.core.oauth-token.issued

**Title:** OAuth token issued

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth token is issued.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.core.oauth-token.issued". |
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
| `data` | `object` | Yes | Data specific to the oauth token issued event. |

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
| `id` | `string` | No | Identifier of the newly issued token. |
| `scopes` | `string[]` | No | The list of scopes granted to the token. |
| `appType` | `string` | No | The app type of the client that the token was issued to. |
| `ownerId` | `string` | No | Identifier of the OAuth client. |
| `issuedAt` | `string` | No | Timestamp when the token was issued. Metadata: format = "date-time". |
| `tenantId` | `string` | No | Identifier of the tenant the token belongs to. |
| `userType` | `string` | No | The type of user the token was issued for (for example, `bot` or `anonymous`). Absent for regular interactive users. |
| `createdBy` | `string` | No | Identifier of the OAuth client who created the token. |
| `grantType` | `string` | No | The grant type that was used to generate the token Allowed values: authorization_code \| refresh_token \| client_credentials \| urn:ietf:params:oauth:grant-type:token-exchange \| urn:qlik:oauth:user-impersonation \| urn:qlik:oauth:anonymous-embed. |
| `deviceType` | `string` | No | The device manufacturer and model. |
| `description` | `string` | No | A description of the token. |
| `resourceOwner` | `string` | No | Identifier of the user the token was issued for. |
| `issuedToClientId` | `string` | No | Identifier of the client the token was issued to. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.oauth-token.issued",
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
    "id": "601abc3fe95f07dbb73ce50f",
    "scopes": [
      "user_default"
    ],
    "appType": "web",
    "ownerId": "LkedCLXCtzdMdZJayyw8LzASxcL9jLTB",
    "issuedAt": "2025-10-30T07:06:22Z",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "createdBy": "sEkC_KKE4RYwBzoeqQ4-TEp982A0gNnA",
    "grantType": "authorization_code",
    "deviceType": "Dell XPS 15",
    "description": "John's PC",
    "resourceOwner": "LkedCLXCtzdMdZJayyw8LzASxcL9jLTB",
    "issuedToClientId": "3e7651d5-98d9-467c-be0b-09623e6aa551"
  }
}
```


### com.qlik.core.oauth-token.revoked

**Title:** OAuth token revoked

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when OAuth tokens are revoked.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of event. Metadata: default = "com.qlik.core.oauth-token.revoked". |
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
| `data` | `object` | Yes | Data specific to the oauth token revoked event. |

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
| `revokedAt` | `string` | Yes | Timestamp when the token(s) were revoked. Metadata: format = "date-time". |
| `revokedBy` | `string` | No | Identifier of the user who revoked the token(s). |
| `revokedContext` | `object` | Yes | Context indicating the scope of the tokens that have been revoked (individual token or many tokens). The revoked tokens are the intersection of the context properties. For example, if both `userId` and `clientId` are provided, only tokens belonging to that user issued from that client are revoked (and not tokens from other users or from other clients). Metadata: minProperties = 1. |
| `revokedByBearer` | `boolean` | Yes | Whether the token was revoked by the bearer using the access or refresh token (`true`), or revoked via the REST API (`false`). |

<details>
<summary>Properties of `revokedContext`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | No | If provided, revoked tokens are limited to this user. |
| `grantId` | `string` | No | Unique identifier of the token. If provided, only this specific token has been revoked. |
| `clientId` | `string` | No | If provided, revoked tokens are limited to this OAuth client. |
| `tenantId` | `string` | No | If provided, revoked tokens are limited to this tenant. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-01-01T12:00:00Z",
  "type": "com.qlik.core.oauth-token.revoked",
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
    "revokedAt": "2025-10-30T07:06:22Z",
    "revokedBy": "sEkC_KKE4RYwBzoeqQ4-TEp982A0gNnA",
    "revokedContext": {
      "userId": "605a18af2ab08cdbfad09259",
      "grantId": "601abc3fe95f07dbb73ce50f",
      "clientId": "630201422597f43c47128aa651af2172",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
    },
    "revokedByBearer": true
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


