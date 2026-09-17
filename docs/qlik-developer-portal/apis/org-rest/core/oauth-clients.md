# Oauth clients

**Base URL:** `https://console.qlikcloud.com`

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/core/oauth-clients`](#get-apicoreoauth-clients) | Retrieves all OAuth clients registered. |
| `POST` | [`/api/core/oauth-clients`](#post-apicoreoauth-clients) | Registers a new OAuth client in the tenant. The `appType` field determines the |
| `GET` | [`/api/core/oauth-clients/{id}`](#get-apicoreoauth-clientsid) | Retrieves a single OAuth client by its unique identifier. The response includes |
| `PATCH` | [`/api/core/oauth-clients/{id}`](#patch-apicoreoauth-clientsid) | Updates one or more properties of an OAuth client using JSON Patch (RFC 6902). |
| `DELETE` | [`/api/core/oauth-clients/{id}`](#delete-apicoreoauth-clientsid) | Deletes an OAuth client. After deletion, no new tokens can be issued for the client. |
| `POST` | [`/api/core/oauth-clients/{id}/client-secrets`](#post-apicoreoauth-clientsidclient-secrets) | Generates a new client secret for the specified OAuth client. Client secrets are |
| `DELETE` | [`/api/core/oauth-clients/{id}/client-secrets/{hint}`](#delete-apicoreoauth-clientsidclient-secretshint) | Deletes a specific client secret for an OAuth client. After deletion, the secret |

## API Reference

### GET /api/core/oauth-clients

Retrieves all OAuth clients registered.
Results are paginated using cursor-based pagination; use the `next` and `prev`
parameters to navigate between pages. Use the `filter` and `sort` parameters to
narrow or order the results.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | A filter expression used to narrow the list of OAuth clients. The filter syntax follows RFC 7644. Valid filter attributes are `clientId`, `clientName`, `appType`, and `createdByType`. |
| `limit` | number | No | The maximum number of OAuth clients to return per page. |
| `next` | string | No | The cursor for the next page of results. |
| `prev` | string | No | The cursor for the previous page of results. |
| `sort` | string | No | The field to sort by, prefixed with `+` for ascending or `-` for descending order. Valid fields for sorting are `clientId`, `clientName`, `appType`, `createdAt`, `updatedAt`. Enum: "+clientId", "-clientId", "+clientName", "-clientName", "+appType", "-appType", "+createdAt", "-createdAt", "+updatedAt", "-updatedAt" |
| `totalResults` | boolean | No | When `true`, the response includes the total number of matching OAuth clients in the `totalResults` field. When `false` or omitted, `totalResults` is excluded from the response. |

#### Responses

##### 200

OAuth clients retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An OAuth client entry returned in a list response. |
| `links` | object | Yes | Pagination links for navigating between pages of results. |
| `totalResults` | integer | No | Total number of OAuth clients. Included only when the `totalResults` query parameter is set to `true`. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | Yes | The unique identifier of the OAuth client application. |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login. |
| `allowedOrigins` | string[] | No | List of allowed origins for the client. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client. Enum: "client_secret", "private_key_jwt" |
| `appType` | string | Yes | The type of application the OAuth client represents. Enum: "web", "native", "spa", "anonymous-embed" |
| `logoUri` | string | No | The URI for the client application's logo image. |
| `clientUri` | string | No | The URI for the client application's homepage. |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | The display name of the OAuth client application. |
| `disableTag` | string | No | Indicates the reason the client is disabled. Present only when the client has been disabled. |
| `description` | string | No | A text description of the OAuth client. |
| `publishedAt` | string | No | The timestamp when the client was published. Present only for published clients. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. |
| `clientSecrets` | object[] | No | Partial identifiers (hints) for the client secrets associated with this OAuth client. |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `allowedGrantTypes` | string[] | No | Allowed grant types. Only applicable when `appType` is `web`. Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | The RSA key public exponent, Base64URL-encoded. |
| `n` | string | No | The RSA key modulus, Base64URL-encoded. |
| `x` | string | No | The X coordinate of the EC public key, Base64URL-encoded. |
| `y` | string | No | The Y coordinate of the EC public key, Base64URL-encoded. |
| `alg` | string | Yes | The algorithm intended for use with the key. Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | The elliptic curve used with this key. |
| `kid` | string | Yes | A unique identifier for this key. |
| `kty` | string | Yes | The cryptographic key type. Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key. The only accepted value is `sig` (signature verification). Enum: "sig" |

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The current status of the client connection configuration. |
| `consentMethod` | string | Yes | Specifies the consent method for the connection. Enum: "required", "trusted" |
| `deletedByOwner` | boolean | No | OAuth client has been deleted by owner, only applies for published clients. |

</details>

<details>
<summary>Properties of `clientSecrets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | Hint of a client application secret |
| `createdAt` | string | No | The timestamp for when the client-secret record was created. |
| `createdBy` | string | No | The identifier for the user that created the client-secret record. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | A navigational link containing an absolute URL. |
| `prev` | object | No | A navigational link containing an absolute URL. |
| `self` | object | No | A navigational link containing an absolute URL. |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The absolute URL of the linked resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The absolute URL of the linked resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The absolute URL of the linked resource. |

</details>

</details>

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients',
  method: 'GET',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "data": [
    {
      "appType": "web",
      "logoUri": "string",
      "clientUri": "string",
      "createdAt": "2025-11-06T14:30:00.123456Z",
      "deletedAt": "2025-11-06T15:45:30.789012Z",
      "updatedAt": "2025-11-06T16:20:15.456789Z",
      "clientName": "string",
      "disableTag": "string",
      "publicKeys": [
        {
          "e": "AQAB",
          "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx",
          "x": "WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis",
          "y": "y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE",
          "alg": "RS256",
          "crv": "P-384",
          "kid": "key-1",
          "kty": "RSA",
          "use": "sig"
        }
      ],
      "description": "string",
      "publishedAt": "2025-11-06T17:00:00.321654Z",
      "allowedScopes": [
        "string"
      ],
      "clientSecrets": [
        {
          "hint": "string",
          "createdAt": "2025-12-03T14:59:46.331Z",
          "createdBy": "string"
        }
      ],
      "createdByType": "string",
      "connectionConfig": {
        "status": "string",
        "consentMethod": "string",
        "deletedByOwner": true
      },
      "allowedGrantTypes": [
        "client_credentials"
      ],
      "allowedAuthMethods": [
        "client_secret"
      ],
      "clientId": "string",
      "redirectUris": [
        "string"
      ],
      "allowedOrigins": [
        "string"
      ]
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  },
  "totalResults": 42
}
```

---

### POST /api/core/oauth-clients

Registers a new OAuth client in the tenant. The `appType` field determines the
client type and cannot be changed after creation. The consent method and published
state can be updated after creation using the PATCH operation.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | string | Yes | The type of application the OAuth client represents. Enum: "web", "native", "spa", "anonymous-embed" |
| `logoUri` | string | No | The URI for the client application's logo image. |
| `clientUri` | string | No | The URI for the client application's homepage. |
| `clientName` | string | Yes | The display name of the OAuth client application. |
| `publicKeys` | object[] | No | List of public keys for JWT authentication. Required when `private_key_jwt` is listed in `allowedAuthMethods`. |
| `description` | string | No | A text description of the OAuth client. |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. |
| `allowedOrigins` | string[] | No | List of allowed origins for this client. Only applicable when `appType` is `spa`. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types. Only applicable when `appType` is `web`. Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client. Enum: "client_secret", "private_key_jwt" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | The RSA key public exponent, Base64URL-encoded. |
| `n` | string | No | The RSA key modulus, Base64URL-encoded. |
| `x` | string | No | The X coordinate of the EC public key, Base64URL-encoded. |
| `y` | string | No | The Y coordinate of the EC public key, Base64URL-encoded. |
| `alg` | string | Yes | The algorithm intended for use with the key. Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | The elliptic curve used with this key. |
| `kid` | string | Yes | A unique identifier for this key. |
| `kty` | string | Yes | The cryptographic key type. Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key. The only accepted value is `sig` (signature verification). Enum: "sig" |

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `consentMethod` | string | No | Specifies the consent method for the connection. The only allowed value is `trusted`. Enum: "trusted" |

</details>

#### Responses

##### 201

OAuth client created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | Yes | The unique identifier of the OAuth client application. |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `clientSecret` | string | Yes | The initial client secret. Returned only at creation time; store it securely. |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login. |
| `allowedOrigins` | string[] | No | List of allowed origins for the client. |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client. Enum: "client_secret", "private_key_jwt" |
| `appType` | string | Yes | The type of application the OAuth client represents. Enum: "web", "native", "spa", "anonymous-embed" |
| `logoUri` | string | No | The URI for the client application's logo image. |
| `clientUri` | string | No | The URI for the client application's homepage. |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | The display name of the OAuth client application. |
| `disableTag` | string | No | Indicates the reason the client is disabled. Present only when the client has been disabled. |
| `description` | string | No | A text description of the OAuth client. |
| `publishedAt` | string | No | The timestamp when the client was published. Present only for published clients. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. |
| `clientSecrets` | object[] | No | Partial identifiers (hints) for the client secrets associated with this OAuth client. |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types. Only applicable when `appType` is `web`. Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | The RSA key public exponent, Base64URL-encoded. |
| `n` | string | No | The RSA key modulus, Base64URL-encoded. |
| `x` | string | No | The X coordinate of the EC public key, Base64URL-encoded. |
| `y` | string | No | The Y coordinate of the EC public key, Base64URL-encoded. |
| `alg` | string | Yes | The algorithm intended for use with the key. Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | The elliptic curve used with this key. |
| `kid` | string | Yes | A unique identifier for this key. |
| `kty` | string | Yes | The cryptographic key type. Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key. The only accepted value is `sig` (signature verification). Enum: "sig" |

</details>

<details>
<summary>Properties of `clientSecrets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | Hint of a client application secret |
| `createdAt` | string | No | The timestamp for when the client-secret record was created. |
| `createdBy` | string | No | The identifier for the user that created the client-secret record. |

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `consentMethod` | string | No | Specifies the consent method for the connection. Enum: "required", "trusted" |

</details>

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"appType":"web","logoUri":"https://org.us.qlik.com/logo.png","clientUri":"https://org.us.qlik.com/","clientName":"My_test_application","publicKeys":[{"e":"AQAB","n":"0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx","x":"WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis","y":"y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE","alg":"RS256","crv":"P-384","kid":"key-1","kty":"RSA","use":"sig"}],"description":"A test application client","redirectUris":["https://org.us.qlik.com/home"],"allowedScopes":["automations"],"allowedOrigins":["https://qlik.com"],"connectionConfig":{"consentMethod":"trusted"},"allowedGrantTypes":["client_credentials"],"allowedAuthMethods":["client_secret"]}'
```

**Node.js:**

```javascript
const https = require('https')

const data = JSON.stringify({
  appType: 'web',
  logoUri: 'https://org.us.qlik.com/logo.png',
  clientUri: 'https://org.us.qlik.com/',
  clientName: 'My_test_application',
  publicKeys: [
    {
      e: 'AQAB',
      n: '0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx',
      x: 'WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis',
      y: 'y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE',
      alg: 'RS256',
      crv: 'P-384',
      kid: 'key-1',
      kty: 'RSA',
      use: 'sig',
    },
  ],
  description: 'A test application client',
  redirectUris: ['https://org.us.qlik.com/home'],
  allowedScopes: ['automations'],
  allowedOrigins: ['https://qlik.com'],
  connectionConfig: { consentMethod: 'trusted' },
  allowedGrantTypes: ['client_credentials'],
  allowedAuthMethods: ['client_secret'],
})
const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients',
  method: 'POST',
  headers: {
    'Content-type': 'application/json',
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)
req.write(data)

```

**Example Response:**

```json
{
  "appType": "web",
  "logoUri": "string",
  "clientUri": "string",
  "createdAt": "2025-11-06T14:30:00.123456Z",
  "deletedAt": "2025-11-06T15:45:30.789012Z",
  "updatedAt": "2025-11-06T16:20:15.456789Z",
  "clientName": "string",
  "disableTag": "string",
  "publicKeys": [
    {
      "e": "AQAB",
      "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx",
      "x": "WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis",
      "y": "y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE",
      "alg": "RS256",
      "crv": "P-384",
      "kid": "key-1",
      "kty": "RSA",
      "use": "sig"
    }
  ],
  "description": "string",
  "publishedAt": "2025-11-06T17:00:00.321654Z",
  "allowedScopes": [
    "string"
  ],
  "clientSecrets": [
    {
      "hint": "string",
      "createdAt": "2025-12-03T14:59:46.331Z",
      "createdBy": "string"
    }
  ],
  "createdByType": "string",
  "connectionConfig": {
    "consentMethod": "required"
  },
  "allowedGrantTypes": [
    "client_credentials"
  ],
  "allowedAuthMethods": [
    "client_secret"
  ],
  "clientId": "string",
  "clientSecret": "string",
  "redirectUris": [
    "string"
  ],
  "allowedOrigins": [
    "string"
  ]
}
```

---

### GET /api/core/oauth-clients/{id}

Retrieves a single OAuth client by its unique identifier. The response includes
the client's configuration, allowed scopes, authentication methods, and public keys.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client. |

#### Responses

##### 200

OAuth client retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | Yes | The unique identifier of the OAuth client application. |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login |
| `clientSecrets` | object[] | No | Partial identifiers (hints) for the client secrets associated with this OAuth client. |
| `allowedOrigins` | string[] | No | List of allowed origins for the client. |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client. Enum: "client_secret", "private_key_jwt" |
| `appType` | string | Yes | The type of application the OAuth client represents. Enum: "web", "native", "spa", "anonymous-embed" |
| `logoUri` | string | No | The URI for the client application's logo image. |
| `clientUri` | string | No | The URI for the client application's homepage. |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | The display name of the OAuth client application. |
| `disableTag` | string | No | Indicates the reason the client is disabled. Present only when the client has been disabled. |
| `description` | string | No | A text description of the OAuth client. |
| `publishedAt` | string | No | The timestamp when the client was published. Present only for published clients. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types. Only applicable when `appType` is `web`. Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | The RSA key public exponent, Base64URL-encoded. |
| `n` | string | No | The RSA key modulus, Base64URL-encoded. |
| `x` | string | No | The X coordinate of the EC public key, Base64URL-encoded. |
| `y` | string | No | The Y coordinate of the EC public key, Base64URL-encoded. |
| `alg` | string | Yes | The algorithm intended for use with the key. Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | The elliptic curve used with this key. |
| `kid` | string | Yes | A unique identifier for this key. |
| `kty` | string | Yes | The cryptographic key type. Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key. The only accepted value is `sig` (signature verification). Enum: "sig" |

</details>

<details>
<summary>Properties of `clientSecrets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | Hint of a client application secret |
| `createdAt` | string | No | The timestamp for when the client-secret record was created. |
| `createdBy` | string | No | The identifier for the user that created the client-secret record. |

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `consentMethod` | string | No | Specifies the consent method for the connection. Enum: "required", "trusted" |

</details>

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 404

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients/{id}',
  method: 'GET',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "appType": "web",
  "logoUri": "string",
  "clientUri": "string",
  "createdAt": "2025-11-06T14:30:00.123456Z",
  "deletedAt": "2025-11-06T15:45:30.789012Z",
  "updatedAt": "2025-11-06T16:20:15.456789Z",
  "clientName": "string",
  "disableTag": "string",
  "publicKeys": [
    {
      "e": "AQAB",
      "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx",
      "x": "WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis",
      "y": "y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE",
      "alg": "RS256",
      "crv": "P-384",
      "kid": "key-1",
      "kty": "RSA",
      "use": "sig"
    }
  ],
  "description": "string",
  "publishedAt": "2025-11-06T17:00:00.321654Z",
  "allowedScopes": [
    "string"
  ],
  "clientSecrets": [
    {
      "hint": "string",
      "createdAt": "2025-11-06T14:30:00.123456Z",
      "createdBy": "string"
    }
  ],
  "createdByType": "string",
  "connectionConfig": {
    "consentMethod": "required"
  },
  "allowedGrantTypes": [
    "client_credentials"
  ],
  "allowedAuthMethods": [
    "client_secret"
  ],
  "clientId": "string",
  "redirectUris": [
    "string"
  ],
  "allowedOrigins": [
    "string"
  ]
}
```

---

### PATCH /api/core/oauth-clients/{id}

Updates one or more properties of an OAuth client using JSON Patch (RFC 6902).
Supply an array of patch operations targeting the fields you want to change. If
the update results in a new client secret being generated, the response returns
`202 Accepted` with the new secret in the body; otherwise it returns `204 No Content`.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The patch operation to perform. Use `add` or `replace` to set a value, and `remove` to clear it. Enum: "add", "remove", "replace" |
| `path` | string | Yes | The JSON pointer path of the field to patch. Enum: "/clientName", "/description", "/allowedScopes" |
| `value` | string \| array | No | The value to set for the targeted field. Required for `add` and `replace` operations. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string[] | No |  |

</details>

#### Responses

##### 202

A new client secret was generated. The response body contains the new secret value.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientSecret` | string | Yes | The generated client application secret. |

##### 204

The OAuth client was updated successfully.

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 404

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/clientName","value":"string"}]'
```

**Node.js:**

```javascript
const https = require('https')

const data = JSON.stringify([
  {
    op: 'add',
    path: '/clientName',
    value: 'string',
  },
])
const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients/{id}',
  method: 'PATCH',
  headers: {
    'Content-type': 'application/json',
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)
req.write(data)

```

**Example Response:**

```json
{
  "clientSecret": "a1b2c3d4e5f6..."
}
```

---

### DELETE /api/core/oauth-clients/{id}

Deletes an OAuth client. After deletion, no new tokens can be issued for the client.
Existing tokens may remain valid until they expire unless invalidated by a downstream revocation mechanism.
Supply the `qlik-confirm-delete` header to confirm the deletion.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-confirm-delete` | string | Yes | A confirmation string that must equal the `id` of the OAuth client to delete. |

#### Responses

##### 204

The OAuth client was deleted successfully.

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 404

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients/{id}" \
-X DELETE \
-H "qlik-confirm-delete: string" \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients/{id}',
  method: 'DELETE',
  headers: {
    'qlik-confirm-delete': 'string',
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

---

### POST /api/core/oauth-clients/{id}/client-secrets

Generates a new client secret for the specified OAuth client. Client secrets are
supported only for clients with `appType` set to `web` and `client_secret` listed
in `allowedAuthMethods`. An OAuth client can have a maximum of 5 client secrets at
one time. The secret value is returned only in the response and cannot be retrieved again.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client. |

#### Responses

##### 201

Client secret created successfully. The secret value is returned only once and cannot be retrieved again.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | A short identifier for this client secret, used to distinguish it from other secrets. |
| `clientId` | string | Yes | The unique identifier of the OAuth client. |
| `createdAt` | string | No | The timestamp for when the client-secret record was created. |
| `createdBy` | string | No | The identifier for the user that created the client-secret record. |
| `clientSecret` | string | Yes | The client secret value. Store this securely; it cannot be retrieved again. |

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 404

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 409

The maximum number of client secrets is 5.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients/{id}/client-secrets" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients/{id}/client-secrets',
  method: 'POST',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

**Example Response:**

```json
{
  "hint": "string",
  "clientId": "string",
  "createdAt": "2025-11-06T14:30:00.123456Z",
  "createdBy": "string",
  "clientSecret": "string"
}
```

---

### DELETE /api/core/oauth-clients/{id}/client-secrets/{hint}

Deletes a specific client secret for an OAuth client. After deletion, the secret
can no longer be used for future client authentication or token requests that
require that secret.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | The hint identifying the client secret to delete. |
| `id` | string | Yes | The unique identifier for the OAuth client. |

#### Responses

##### 204

The client secret was deleted successfully.

##### 400

The request is invalid. Check the request body or parameters for errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 403

Access denied. You lack the required permissions to perform this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 404

The requested resource was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 500

An unexpected error occurred on the server. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

##### 503

The service is temporarily unavailable. Try again later.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error object describing what went wrong with the request. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | A machine-readable error code. |
| `title` | string | Yes | A summary of the error. |
| `detail` | string | No | Additional context about the error to help with debugging. |

</details>

#### Examples

**Qlik CLI:**

```bash
This API is not included yet in qlik-cli
```

**cURL:**

```bash
curl "https://console.qlikcloud.com/api/core/oauth-clients/{id}/client-secrets/{hint}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

**Node.js:**

```javascript
const https = require('https')

const options = {
  hostname: 'console.qlikcloud.com',
  port: 443,
  path: '/api/core/oauth-clients/{id}/client-secrets/{hint}',
  method: 'DELETE',
  headers: {
    Authorization: 'Bearer <access_token>',
  },
}

const req = https.request(options)

```

---
