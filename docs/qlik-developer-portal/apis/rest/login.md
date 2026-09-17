# Login

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

This API is used to initiate interactive logins, or to process JWT login requests.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/login`](#get-login) | Initiates login using the active interactive identity provider associated with the tenant. Uses default Qlik identity provider if no customer-configured interactive identity provider is active. |
| `POST` | [`/login/jwt-session`](#post-loginjwt-session) | Exchanges a token in the form of a user JWT for a session cookie. |

## API Reference

### GET /login

Initiates login using the active interactive identity provider associated with the tenant. Uses default Qlik identity provider if no customer-configured interactive identity provider is active.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `login_hint` | string | No | Hint to the Authorization Server about the login identifier the End-User might use to log in. |
| `max_age` | number | No | Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OpenID Provider. If time is greater than max_age, force user to re-authorize. |
| `prompt` | string | No | Specifies whether the Authorization Server prompts the End-User for re-authentication and consent. Enum: "none", "login" |
| `returnto` | string | No | Relative or full URL on the tenant to redirect to after successful login. |
| `scope` | array | No | Specifies the scope of access for login. Only supports offline_access to request a refresh token from the identity provider. Enum: "offline_access" |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Qlik-Web-Integration-ID` | string | No | Web Integration ID associated with origin whitelist used to validate returnto value. |

#### Responses

##### 302

Redirect to the identity provider.

**Content-Type:** `text/html`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/html` | string | No |  |

##### 401

Invalid login.

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
// qlik-api has not implemented support for `GET /login` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/login', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /login yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/login"
```

---

### POST /login/jwt-session

Exchanges a token in the form of a user JWT for a session cookie.
The JWT should be securely signed with an algorithm other than HS, and it should contain the following claims:
1. iss: identifies the principal that issued the JWT; it must match the issuer in the IDP definition.
2. aud: identifies the recipients of the JWT, which in this case is "qlik.api/login/jwt-session".
3. sub: identifies the subject of the JWT.
4. subType: the type of identifier the sub represents, which in this case is "user".
5. name: the name of the user.
6. email: the email address of the user.
7. email_verified: a claim indicating to Qlik that the JWT source has verified that the email address belongs to the subject.
9. jti: JWT ID; it should be unique for each consumed JWT token.
10. iat: identifies the time at which the JWT was issued.
11. nbf: identifies the starting time on which the JWT is accepted. The current unix time must be passed this value.
12. exp: identifies the expiration time after which the JWT is not accepted.
13. keyid: identifies the KeyID used to sign the JWT; it must match the KeyID in the IDP definition.

And the time window between exp and nbf should not exceed 1 hour.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 200

Successfully exchanged JWT for session.

**Content-Type:** `application/json`


##### 401

Unauthorized.

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
// qlik-api has not implemented support for `POST /login/jwt-session` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/login/jwt-session',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /login/jwt-session yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/login/jwt-session" \
-X POST \
-H "Authorization: Bearer <Signed JWT>"
```

**Example Response:**

```json
{}
```

---
