# OAuth

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Authorize OAuth client flows, and create and revoke OAuth tokens.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/oauth/authorize`](#get-oauthauthorize) | Allows a client application to use an OAuth flow to request user authorization. |
| `POST` | [`/oauth/revoke`](#post-oauthrevoke) | Allows a client to revoke their token. |
| `POST` | [`/oauth/token`](#post-oauthtoken) | Allows a client to perform an OAuth flow to obtain a token set. |

## API Reference

### GET /oauth/authorize

Allows a client application to use an OAuth flow to request user authorization.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | string | Yes | The client identifier. |
| `code_challenge_method` | string | Yes | The algorithm that client used for generating code_challenge, only S256 is supported for now. Enum: "S256" |
| `redirect_uri` | string | Yes | Relative or full URL to redirect to after successful login. |
| `response_type` | string | Yes | Describes the grant flow to use. |
| `scope` | array | Yes | The scope of access that is being requested. |
| `state` | string | Yes | State parameter to roundtrip to client in final redirect. |
| `code_challenge` | string | No | The code challenge created by the client. |
| `login_hint` | string | No | Hint to the Authorization Server about the login identifier the End-User might use to log in. |
| `max_age` | number | No | Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OpenID Provider. If time is greater than max_age, force user to re-authorize. |
| `prompt` | string | No | Specifies whether the Authorization Server prompts the End-User for re-authentication or requires a non-interactive authentication. Enum: "none", "login", "consent" |

#### Responses

##### 302

Redirect to the identity provider or back to the redirect_uri if an error occurs. On error the redirect will follow the OAuth2 RFC section 4.1.2.1 (https://tools.ietf.org/html/rfc6749#section-4.1.2.1) with an additional error_code parameter with the internal error code. When a detail is known for the error it will be included as error_detail.

**Content-Type:** `text/html`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/html` | string | No |  |

##### 400

Invalid client_id or redirect_uri.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /oauth/authorize` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/oauth/authorize', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /oauth/authorize yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/oauth/authorize"
```

---

### POST /oauth/revoke

Allows a client to revoke their token.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Properties of the token that the client wants to revoke.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `token` | string | Yes | The token to revoke. |
| `token_type_hint` | string | No | Type of the provided token. Enum: "access_token", "refresh_token" |

**Content-Type:** `application/x-www-form-urlencoded`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `token` | string | Yes | The token to revoke. |
| `token_type_hint` | string | No | Type of the provided token. Enum: "access_token", "refresh_token" |

#### Responses

##### 200

Token was revoked.

##### 400

Invalid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /oauth/revoke` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/oauth/revoke', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    token: 'string',
    token_type_hint: 'access_token',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /oauth/revoke yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/oauth/revoke" \
-X POST \
-H "Content-type: application/json" \
-d '{"token":"string","token_type_hint":"access_token"}'
```

---

### POST /oauth/token

Allows a client to perform an OAuth flow to obtain a token set.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | any | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-client-credentials-request` | object | No |  |

<details>
<summary>Properties of `oauth-client-credentials-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | string | No | The scope of access that is being requested. The scope should already be assigned to the OAuth client. For a list of available scopes, visit: https://qlik.dev/authenticate/oauth/scopes/#available-scopes |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | The grant type used to obtain an access token outside of the context of a user. Enum: "client_credentials" |
| `client_secret` | string | Yes | The client secret. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-refresh-request` | object | No |  |

<details>
<summary>Properties of `oauth-refresh-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `grant_type` | string | Yes | The grant type used to exchange a refresh token for an access token. Enum: "refresh_token" |
| `client_secret` | string | No | The client secret. |
| `refresh_token` | string | Yes | The refresh token to use. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-authorization-code-request` | object | No |  |

<details>
<summary>Properties of `oauth-authorization-code-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The authorization code created by the server. |
| `client_id` | string | Yes | The client identifier. |
| `deviceType` | string | No | The type of the user device the authorization token is generated for (Tablet, Phone etc.). |
| `grant_type` | string | Yes | The grant type used to exchange an authorization code for an access token. Enum: "authorization_code" |
| `description` | string | No | A user-friendly description to distinguish between multiple tokens. |
| `redirect_uri` | string | Yes | The original redirect URI provided during authorization. For verification purposes only. |
| `client_secret` | string | No | The client secret. |
| `code_verifier` | string | Yes | Required when grant_type is "authorization_code". The code verifier to verify original code challenge created by the client. It must be between 43 and 128 characters long and consists of [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~" |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-token-exchange` | object | No | Exchanges one token for another. Implementation is based on this spec: https://datatracker.ietf.org/doc/html/rfc8693. |

<details>
<summary>Properties of `oauth-token-exchange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `purpose` | string | Yes | The intended use for the requested token. Enum: "websocket", "webresource" |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | Specifies the method in which the token will be granted. Enum: "urn:ietf:params:oauth:grant-type:token-exchange" |
| `subject_token` | string | Yes | The token that represents the identity of the party on behalf of whom the request is being made. |
| `subject_token_type` | string | Yes | The type of the subject token. Enum: "urn:ietf:params:oauth:token-type:access_token" |

</details>

**Option 5:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-user-impersonation-request` | object | No |  |

<details>
<summary>Properties of `oauth-user-impersonation-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | string | No | The scope of access that is being requested. The scope should already be assigned to the OAuth client. For a list of available scopes, visit: https://qlik.dev/authenticate/oauth/scopes/#available-scopes |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | The grant type used to obtain an access token on behalf of an existing user. Enum: "urn:qlik:oauth:user-impersonation" |
| `user_lookup` | object | Yes |  |
| `client_secret` | string | Yes | The client secret. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

<details>
<summary>Properties of `user_lookup`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

**Content-Type:** `application/x-www-form-urlencoded`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/x-www-form-urlencoded` | any | No |  |

<details>
<summary>Properties of `application/x-www-form-urlencoded`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-client-credentials-request` | object | No |  |

<details>
<summary>Properties of `oauth-client-credentials-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | string | No | The scope of access that is being requested. The scope should already be assigned to the OAuth client. For a list of available scopes, visit: https://qlik.dev/authenticate/oauth/scopes/#available-scopes |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | The grant type used to obtain an access token outside of the context of a user. Enum: "client_credentials" |
| `client_secret` | string | Yes | The client secret. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-refresh-request` | object | No |  |

<details>
<summary>Properties of `oauth-refresh-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `grant_type` | string | Yes | The grant type used to exchange a refresh token for an access token. Enum: "refresh_token" |
| `client_secret` | string | No | The client secret. |
| `refresh_token` | string | Yes | The refresh token to use. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-authorization-code-request` | object | No |  |

<details>
<summary>Properties of `oauth-authorization-code-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The authorization code created by the server. |
| `client_id` | string | Yes | The client identifier. |
| `deviceType` | string | No | The type of the user device the authorization token is generated for (Tablet, Phone etc.). |
| `grant_type` | string | Yes | The grant type used to exchange an authorization code for an access token. Enum: "authorization_code" |
| `description` | string | No | A user-friendly description to distinguish between multiple tokens. |
| `redirect_uri` | string | Yes | The original redirect URI provided during authorization. For verification purposes only. |
| `client_secret` | string | No | The client secret. |
| `code_verifier` | string | Yes | Required when grant_type is "authorization_code". The code verifier to verify original code challenge created by the client. It must be between 43 and 128 characters long and consists of [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~" |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-token-exchange` | object | No | Exchanges one token for another. Implementation is based on this spec: https://datatracker.ietf.org/doc/html/rfc8693. |

<details>
<summary>Properties of `oauth-token-exchange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `purpose` | string | Yes | The intended use for the requested token. Enum: "websocket", "webresource" |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | Specifies the method in which the token will be granted. Enum: "urn:ietf:params:oauth:grant-type:token-exchange" |
| `subject_token` | string | Yes | The token that represents the identity of the party on behalf of whom the request is being made. |
| `subject_token_type` | string | Yes | The type of the subject token. Enum: "urn:ietf:params:oauth:token-type:access_token" |

</details>

**Option 5:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `oauth-user-impersonation-request` | object | No |  |

<details>
<summary>Properties of `oauth-user-impersonation-request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | string | No | The scope of access that is being requested. The scope should already be assigned to the OAuth client. For a list of available scopes, visit: https://qlik.dev/authenticate/oauth/scopes/#available-scopes |
| `client_id` | string | Yes | The client identifier. |
| `grant_type` | string | Yes | The grant type used to obtain an access token on behalf of an existing user. Enum: "urn:qlik:oauth:user-impersonation" |
| `user_lookup` | object | Yes |  |
| `client_secret` | string | Yes | The client secret. |
| `client_assertion` | string | No | JWT used for client authentication instead of client_secret. |
| `client_assertion_type` | string | No | Assertion type for JWT client assertion. |

<details>
<summary>Properties of `user_lookup`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 200

Token set created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | string | No | The scope of access that is being granted, delimited by space. |
| `auth_time` | number | No | Unix time of when the last authentication occurred. |
| `expires_at` | string | No | The date and time in ISO format for when the access token will expire. |
| `token_type` | string | Yes | The type of the token issued. Enum: "bearer" |
| `access_token` | string | Yes | The access token granted. |
| `refresh_token` | string | No | Refresh token to be used to obtain a new access token without user intervention. |
| `issued_token_type` | string | No | The type of the token issued for a token exchange. See https://datatracker.ietf.org/doc/html/rfc8693#section-2.2.1 for more details. Enum: "urn:ietf:params:oauth:token-type:access_token" |

##### 400

Invalid request parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

##### 401

Invalid login or tokens, indicates that code or token used can be deleted by the client. Also could be invalid client credentials provided in Authorization header.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

##### 403

Forbidden because user is disabled or has reached the maximum number of tokens.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /oauth/token` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/oauth/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    scope: 'user_default offline_access',
    client_id: 'string',
    grant_type: 'client_credentials',
    client_secret: 'string',
    client_assertion:
      'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1jbGllbnQtaWQiLCJzdWIiOiJteS1jbGllbnQtaWQiLCJhdWQiOiJodHRwczovL215LXRlbmFudC51cy5xbGlrY2xvdWQuY29tL29hdXRoL3Rva2VuIiwiZXhwIjoxNzM3MTIwMDAwLCJpYXQiOjE3MzcxMTk0MDAsImp0aSI6ImU1Zjg0ZGE3LWI0YzMtNGE5Yi04ZjFlLTNhMmIxYzRkNWU2ZiJ9.kR7Y5tz9Xm3KpwF8jH2vQ4nL9sA6bC1dE8fG0hI3jK5mN7oP9qR2sT4uV6wX8yZ0aB2cD4eF6gH8iJ0kL2mN4oP6qR8sT0uV2wX4yZ6aB8cD0eF2gH4iJ6kL8mN0oP2qR4sT6uV8wX0yZ2aB4cD6eF8gH0iJ2kL4mN6oP8qR0sT2uV4wX6yZ8aB0cD2eF4gH6iJ8kL0mN2oP4qR6sT8uV0wX2yZ4aB6cD8eF0gH2iJ4kL6mN8oP0qR2sT4uV6wX8yZ0aB2cD4eF6gH8iJ0kL2mN4oP6qR8',
    client_assertion_type:
      'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /oauth/token yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/oauth/token" \
-X POST \
-H "Content-type: application/json" \
-d '{"scope":"user_default offline_access","client_id":"string","grant_type":"client_credentials","client_secret":"string","client_assertion":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1jbGllbnQtaWQiLCJzdWIiOiJteS1jbGllbnQtaWQiLCJhdWQiOiJodHRwczovL215LXRlbmFudC51cy5xbGlrY2xvdWQuY29tL29hdXRoL3Rva2VuIiwiZXhwIjoxNzM3MTIwMDAwLCJpYXQiOjE3MzcxMTk0MDAsImp0aSI6ImU1Zjg0ZGE3LWI0YzMtNGE5Yi04ZjFlLTNhMmIxYzRkNWU2ZiJ9.kR7Y5tz9Xm3KpwF8jH2vQ4nL9sA6bC1dE8fG0hI3jK5mN7oP9qR2sT4uV6wX8yZ0aB2cD4eF6gH8iJ0kL2mN4oP6qR8sT0uV2wX4yZ6aB8cD0eF2gH4iJ6kL8mN0oP2qR4sT6uV8wX0yZ2aB4cD6eF8gH0iJ2kL4mN6oP8qR0sT2uV4wX6yZ8aB0cD2eF4gH6iJ8kL0mN2oP4qR6sT8uV0wX2yZ4aB6cD8eF0gH2iJ4kL6mN8oP0qR2sT4uV6wX8yZ0aB2cD4eF6gH8iJ0kL2mN4oP6qR8","client_assertion_type":"urn:ietf:params:oauth:client-assertion-type:jwt-bearer"}'
```

**Example Response:**

```json
{
  "scope": "offline_access user_default",
  "auth_time": 1628524367,
  "expires_at": "1970-01-18T13:17:10.931Z",
  "token_type": "bearer",
  "access_token": "string",
  "refresh_token": "string",
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
}
```

---
