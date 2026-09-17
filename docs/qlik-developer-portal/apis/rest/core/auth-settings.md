# Auth settings

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Configure and retrieve authentication settings for your Qlik Cloud tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/core/auth-settings`](#get-apicoreauth-settings) | Returns the authentication settings for the tenant, including the session inactivity timeout and maximum session lifespan. If no custom values have been saved, the response reflects tenant-wide defaults with `isDefault` set to `true`. The user must be assigned the `TenantAdmin` role. |
| `PATCH` | [`/api/core/auth-settings`](#patch-apicoreauth-settings) | Updates one or more authentication settings for the tenant using JSON Patch (RFC 6902). Supports `replace` operations on `/userSessionInactivityTimeoutMinutes`, `/maxUserSessionLifespanMinutes`, and `/dynamicClientRegistrationEnabled`. The value for `maxUserSessionLifespanMinutes` must be a whole number of hours (divisible by 60). The user must be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/core/auth-settings

Returns the authentication settings for the tenant, including the session inactivity timeout and maximum session lifespan. If no custom values have been saved, the response reflects tenant-wide defaults with `isDefault` set to `true`. The user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Authentication settings retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the authentication settings. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the authentication settings. |
| `isDefault` | boolean | No | `true` if the authentication settings are using tenant-wide defaults. No custom values have been saved for this tenant. |
| `maxUserSessionLifespanMinutes` | integer | Yes | Maximum total lifespan for a user session, in minutes. Sessions are invalidated after this duration regardless of activity. |
| `dcrAllowedAuthenticationMethods` | string[] | No | The allowed authentication methods for dynamic client registration. Only present when dynamic client registration is enabled. Enum: "none", "client_secret" |
| `dynamicClientRegistrationEnabled` | boolean | No | Indicates whether dynamic client registration is enabled for this tenant. |
| `userSessionInactivityTimeoutMinutes` | integer | Yes | Maximum inactivity period for a user session, in minutes. Sessions that have been idle for longer than this value are invalidated. |

##### 401

Not authorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The authenticated user does not have the `TenantAdmin` role required to read authentication settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Authentication settings not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/auth-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/auth-settings',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/core/auth-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/auth-settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "tenantId": "644fd58b846d649c82eba436",
  "isDefault": false,
  "maxUserSessionLifespanMinutes": 1440,
  "dcrAllowedAuthenticationMethods": [
    "client_secret"
  ],
  "dynamicClientRegistrationEnabled": false,
  "userSessionInactivityTimeoutMinutes": 60
}
```

---

### PATCH /api/core/auth-settings

Updates one or more authentication settings for the tenant using JSON Patch (RFC 6902). Supports `replace` operations on `/userSessionInactivityTimeoutMinutes`, `/maxUserSessionLifespanMinutes`, and `/dynamicClientRegistrationEnabled`. The value for `maxUserSessionLifespanMinutes` must be a whole number of hours (divisible by 60). The user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

An array of JSON Patch operations to apply to the authentication settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | A JSON Pointer to the authentication settings field. Use `/dynamicClientRegistrationEnabled` only with a boolean `value`. Field `/dcrAllowedAuthenticationMethods` is only available when dynamic client registration is enabled. Enum: "/userSessionInactivityTimeoutMinutes", "/maxUserSessionLifespanMinutes", "/dynamicClientRegistrationEnabled", "/dcrAllowedAuthenticationMethods" |
| `value` | integer \| boolean \| string \| array | Yes | Value to set for the targeted authentication settings field. Timeout fields accept only integer values, `/dynamicClientRegistrationEnabled` accepts only boolean values, and `/dcrAllowedAuthenticationMethods` accepts an array of strings. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | integer | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string[] | No |  |

</details>

#### Responses

##### 200

Authentication settings updated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the authentication settings. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the authentication settings. |
| `isDefault` | boolean | No | `true` if the authentication settings are using tenant-wide defaults. No custom values have been saved for this tenant. |
| `maxUserSessionLifespanMinutes` | integer | Yes | Maximum total lifespan for a user session, in minutes. Sessions are invalidated after this duration regardless of activity. |
| `dcrAllowedAuthenticationMethods` | string[] | No | The allowed authentication methods for dynamic client registration. Only present when dynamic client registration is enabled. Enum: "none", "client_secret" |
| `dynamicClientRegistrationEnabled` | boolean | No | Indicates whether dynamic client registration is enabled for this tenant. |
| `userSessionInactivityTimeoutMinutes` | integer | Yes | Maximum inactivity period for a user session, in minutes. Sessions that have been idle for longer than this value are invalidated. |

##### 400

Invalid request body.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Not authorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The authenticated user does not have the `TenantAdmin` role required to update authentication settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Authentication settings not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/core/auth-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/auth-settings',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/userSessionInactivityTimeoutMinutes',
        value: 60,
      },
      {
        op: 'replace',
        path: '/maxUserSessionLifespanMinutes',
        value: 1440,
      },
      {
        op: 'replace',
        path: '/dynamicClientRegistrationEnabled',
        value: true,
      },
      {
        op: 'replace',
        path: '/dcrAllowedAuthenticationMethods',
        value: ['client_secret'],
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/core/auth-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/auth-settings" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/userSessionInactivityTimeoutMinutes","value":60},{"op":"replace","path":"/maxUserSessionLifespanMinutes","value":1440},{"op":"replace","path":"/dynamicClientRegistrationEnabled","value":true},{"op":"replace","path":"/dcrAllowedAuthenticationMethods","value":["client_secret"]}]'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "tenantId": "644fd58b846d649c82eba436",
  "isDefault": false,
  "maxUserSessionLifespanMinutes": 1440,
  "dcrAllowedAuthenticationMethods": [
    "client_secret"
  ],
  "dynamicClientRegistrationEnabled": false,
  "userSessionInactivityTimeoutMinutes": 60
}
```

---
