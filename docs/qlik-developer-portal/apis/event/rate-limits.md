---
source: https://qlik.dev/apis/event/rate-limits/
last_updated: 2026-07-17T09:30:31+02:00
---

# Rate limits

Events emitted when API rate limits are exceeded for a tenant or user in a Qlik Cloud environment.

## Table of Contents

### system-events.rate-limit

- [com.qlik.v1.rate-limit.exceeded](#comqlikv1rate-limitexceeded)

## Events published on the `system-events.rate-limit` channel

### com.qlik.v1.rate-limit.exceeded

**Title:** Rate limit exceeded

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a rate limit has been reached or exceeded. The rate limit decision is in the `data` property and includes whether the limit is enforced (`enforce`), what entity is affected (`appliesTo` - TENANT or USER), validity period (`validUntil`), top contributing users (`users`), and affected endpoints (`includes`/`excludes`).

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.rate-limit.exceeded". |
| `source` | `string` | Yes | The source of the event. Allowed values: com.qlik/rate-limiter. Metadata: default = "com.qlik/rate-limiter". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `host` | `string` | No | Unique identifier for the event producer. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `authtype` | `string` | No | Type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Rate limit decision containing the affected entity (tenant or user), top contributing users, and matched endpoint configurations. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the decision. |
| `type` | `string` | Yes | Type of traffic the decision applies to. Allowed values: rest. |
| `users` | `object[]` | No | Users contributing most to the rate limit decision. |
| `tierId` | `string` | No | Identifier of the tier where the limit has been reached. |
| `enforce` | `boolean` | Yes | Whether the rate limit decision should be enforced. |
| `excludes` | `object[]` | No | Request matching configurations that are excluded from the exceeded tier. |
| `includes` | `object[]` | No | Request matching configurations that are included in the exceeded tier. |
| `appliesTo` | `string` | Yes | Entity type the decision applies to. Allowed values: TENANT \| USER. |
| `validUntil` | `string` | Yes | Timestamp until which the decision remains valid. Metadata: format = "date-time". |

<details>
<summary>Properties of `users`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | No | Identifier of the user contributing to the rate limiting decision. |
| `requests` | `integer` | No | Number of requests in the last sliding window. |

</details>

<details>
<summary>Properties of `excludes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to be matched. |
| `query` | `object[]` | No | Query parameters to be matched. |
| `method` | `string` | No | Method to be matched. Allowed values: GET \| HEAD \| POST \| PUT \| DELETE \| CONNECT \| OPTIONS \| TRACE \| PATCH. |
| `pathType` | `string` | No | How to match the path against incoming API requests. EXACT matches only the exact path, such as `/v1/themes` matching only `/v1/themes`. PREFIX matches any path starting with this value, such as `/v1/themes` matching `/v1/themes`, `/v1/themes/123`, or `/v1/themes/123/file`. Allowed values: PREFIX \| EXACT. |

<details>
<summary>Properties of `query`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `includes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to be matched. |
| `query` | `object[]` | No | Query parameters to be matched. |
| `method` | `string` | No | Method to be matched. Allowed values: GET \| HEAD \| POST \| PUT \| DELETE \| CONNECT \| OPTIONS \| TRACE \| PATCH. |
| `pathType` | `string` | No | How to match the path against incoming API requests. EXACT matches only the exact path, such as `/v1/themes` matching only `/v1/themes`. PREFIX matches any path starting with this value, such as `/v1/themes` matching `/v1/themes`, `/v1/themes/123`, or `/v1/themes/123/file`. Allowed values: PREFIX \| EXACT. |

<details>
<summary>Properties of `query`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2021-11-10T08:50:00Z",
  "type": "com.qlik.v1.rate-limit.exceeded",
  "source": "com.qlik/rate-limiter",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "host": "rate-limiter-pod-12345",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "service_account",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\\\"iss\\\":\\\"qlik.api.internal/service\\\",\\\"sub\\\":\\\"service\\\",\\\"subType\\\":\\\"service\\\"}",
  "tracestate": "b3=05ec17ed8adb7726ecceac3ef58f466f-c05c51826dbc3307-1",
  "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
  "data": {
    "id": "id123",
    "type": "rest",
    "tierId": "1",
    "enforce": true,
    "appliesTo": "TENANT",
    "validUntil": "2021-11-10T08:50:00+01:00"
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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `host` | `string` | No | Unique identifier for the event producer. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `authtype` | `string` | No | Type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |



### queryParameter

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `param` | `string` | No | Name of the query parameter. |



### requestMatcher

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to be matched. |
| `query` | `object[]` | No | Query parameters to be matched. |
| `method` | `string` | No | Method to be matched. Allowed values: GET \| HEAD \| POST \| PUT \| DELETE \| CONNECT \| OPTIONS \| TRACE \| PATCH. |
| `pathType` | `string` | No | How to match the path against incoming API requests. EXACT matches only the exact path, such as `/v1/themes` matching only `/v1/themes`. PREFIX matches any path starting with this value, such as `/v1/themes` matching `/v1/themes`, `/v1/themes/123`, or `/v1/themes/123/file`. Allowed values: PREFIX \| EXACT. |

<details>
<summary>Properties of `query`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `param` | `string` | No | Name of the query parameter. |

</details>



### userRequestData

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | No | Identifier of the user contributing to the rate limiting decision. |
| `requests` | `integer` | No | Number of requests in the last sliding window. |


