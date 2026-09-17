# OAuth clients

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Create and manage the configuration of OAuth clients in your tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/oauth-clients`](#get-apiv1oauth-clients) | Retrieve all OAuth clients. |
| `POST` | [`/api/v1/oauth-clients`](#post-apiv1oauth-clients) | Create a new OAuth client. Requires `TenantAdmin` role when created in-tenant. `appType` cannot be changed after creation. Consent method and published state can be changed after creation. For supported `appType`, use `PATCH /oauth-clients/{id}/connection-configs/me` to change consent method, and `POST /oauth-clients/{id}/actions/publish` to change the client to published after creation. |
| `GET` | [`/api/v1/oauth-clients/{id}`](#get-apiv1oauth-clientsid) | Retrieves the specified OAuth client. |
| `PATCH` | [`/api/v1/oauth-clients/{id}`](#patch-apiv1oauth-clientsid) | Updates the specified OAuth client. Returns 202 Accepted with a client secret in the response body if a client secret is generated during the update (e.g., when adding client_secret to allowedAuthMethods). Otherwise returns 204 No Content. |
| `DELETE` | [`/api/v1/oauth-clients/{id}`](#delete-apiv1oauth-clientsid) | Delete the specified OAuth client. |
| `POST` | [`/api/v1/oauth-clients/{id}/actions/publish`](#post-apiv1oauth-clientsidactionspublish) | Publishes the specified OAuth client. By default, OAuth clients are bound to the tenant that created it. Publishing shares the client and makes it available to all other tenants within a region. Third-party applications connecting to Qlik Cloud can then have the same client ID for all Qlik Cloud tenants. |
| `POST` | [`/api/v1/oauth-clients/{id}/client-secrets`](#post-apiv1oauth-clientsidclient-secrets) | Create a new client secret for the specified OAuth client. An OAuth client can have a maximum of 5 client secrets at one time. |
| `DELETE` | [`/api/v1/oauth-clients/{id}/client-secrets/{hint}`](#delete-apiv1oauth-clientsidclient-secretshint) | Deletes a specific client secret for an OAuth client. |
| `GET` | [`/api/v1/oauth-clients/{id}/connection-configs/me`](#get-apiv1oauth-clientsidconnection-configsme) | Get configuration for consent method and status. |
| `PATCH` | [`/api/v1/oauth-clients/{id}/connection-configs/me`](#patch-apiv1oauth-clientsidconnection-configsme) | Updates the consent method for the specified OAuth client. |
| `DELETE` | [`/api/v1/oauth-clients/{id}/connection-configs/me`](#delete-apiv1oauth-clientsidconnection-configsme) | Deletes the connection config for the calling tenant, related to the supplied client id. |

## API Reference

### GET /api/v1/oauth-clients

Retrieve all OAuth clients.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The filter query that should be used to filter the list of oauth clients.  The filter syntax is defined in RFC 7644. Valid attributes for filtering are `clientId`, `clientName`, `appType`, `tenantId`, and `createdByType`. |
| `limit` | number | No | The number of OAuth client entries to retrieve. |
| `next` | string | No | The next page cursor |
| `prev` | string | No | The previous page cursor |
| `sort` | string | No | The attribute to sort by, beginning with + for ascending and - for descending. Valid attributes for sorting are clientId, clientName, appType, tenantId, createdAt, updatedAt. Enum: "+clientId", "-clientId", "+clientName", "-clientName", "+appType", "-appType", "+tenantId", "-tenantId", "+createdAt", "-createdAt", "+updatedAt", "-updatedAt" |
| `totalResults` | boolean | No | Boolean query parameter that determines if the total count of results should be included in the response. If true, the response includes the total number of results in the `totalResults` field. If false or not included in the query, `totalResults` will be excluded from the response. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `OAuthClientAdminListResponse` | object | No | Response schema for listing OAuth clients as an admin user |

<details>
<summary>Properties of `OAuthClientAdminListResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Schema for a OAuth client when listing as an admin user |
| `links` | object | Yes |  |
| `totalResults` | integer | No | Total number of oauth clients, included only if `totalResults` query parameter is set to true. |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `OAuthClientListResponse` | object | No | Response schema for listing OAuth clients |

<details>
<summary>Properties of `OAuthClientListResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Response schema for reading an OAuth client |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/oauth-clients` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients',
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
# qlik-cli has not implemented support for GET /api/v1/oauth-clients yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "appType": "web",
      "jwksUri": "https://example.com/.well-known/jwks.json",
      "logoUri": "string",
      "clientUri": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "deletedAt": "2018-10-30T07:06:22Z",
      "updatedAt": "2018-10-30T07:06:22Z",
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
      "publishedAt": "2018-10-30T07:06:22Z",
      "allowedScopes": [
        "string"
      ],
      "clientSecrets": [
        {
          "hint": "string",
          "createdAt": "2018-10-30T07:06:22Z",
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

### POST /api/v1/oauth-clients

Create a new OAuth client. Requires `TenantAdmin` role when created in-tenant. `appType` cannot be changed after creation. Consent method and published state can be changed after creation. For supported `appType`, use `PATCH /oauth-clients/{id}/connection-configs/me` to change consent method, and `POST /oauth-clients/{id}/actions/publish` to change the client to published after creation.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | string | Yes | Application type Enum: "web", "native", "spa", "anonymous-embed" |
| `jwksUri` | string | No | URI of the JSON Web Key Set (JWKS) for the client |
| `logoUri` | string | No | URI for logo of client |
| `clientUri` | string | No | URI for homepage of client |
| `clientName` | string | Yes | Client application name |
| `publicKeys` | object[] | No | List of public keys for JWT authentication (required when using private_key_jwt) |
| `description` | string | No | Client description |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. For a full list of scopes see [qlik.dev/authenticate/oauth/scopes/](https://qlik.dev/authenticate/oauth/scopes/). |
| `allowedOrigins` | string[] | No | List of allowed origins for this client, only available with SPA application type |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types, only for use with appType: 'web' Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client Enum: "client_secret", "private_key_jwt" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | Exponent for RSA keys |
| `n` | string | No | Modulus for RSA keys |
| `x` | string | No | X coordinate for EC keys |
| `y` | string | No | Y coordinate for EC keys |
| `alg` | string | Yes | Algorithm intended for use with the key Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | Curve for EC keys |
| `kid` | string | Yes | Key ID |
| `kty` | string | Yes | Key type (e.g., RSA, EC) Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key (typically "sig" for signature) Enum: "sig" |

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `consentMethod` | string | No | Specifies the consent method for the connection. The only allowed value is "trusted." Enum: "trusted" |

</details>

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | Yes | Client application id |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `clientSecret` | string | Yes | Client application secret |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login |
| `allowedOrigins` | string[] | No | List of allowed redirect URIs for login |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client Enum: "client_secret", "private_key_jwt" |
| `appType` | string | Yes | Application type Enum: "web", "native", "spa", "anonymous-embed" |
| `jwksUri` | string | No | URI of the JSON Web Key Set (JWKS) for the client |
| `logoUri` | string | No | URI for logo of client |
| `clientUri` | string | No | URI for homepage of client |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | Client application name |
| `disableTag` | string | No | Is set if client disabled |
| `description` | string | No | Client description |
| `publishedAt` | string | No | The timestamp which is set, if the client is published. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. For a full list of scopes see [qlik.dev/authenticate/oauth/scopes/](https://qlik.dev/authenticate/oauth/scopes/). |
| `clientSecrets` | object[] | No | Hints of any client application secrets |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types, only for use with appType: 'web' Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |

<details>
<summary>Properties of `publicKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `e` | string | No | Exponent for RSA keys |
| `n` | string | No | Modulus for RSA keys |
| `x` | string | No | X coordinate for EC keys |
| `y` | string | No | Y coordinate for EC keys |
| `alg` | string | Yes | Algorithm intended for use with the key Enum: "RS256", "RS512", "ES384" |
| `crv` | string | No | Curve for EC keys |
| `kid` | string | Yes | Key ID |
| `kty` | string | Yes | Key type (e.g., RSA, EC) Enum: "RSA", "EC" |
| `use` | string | Yes | Intended use of the key (typically "sig" for signature) Enum: "sig" |

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

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/oauth-clients` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      appType: 'web',
      jwksUri:
        'https://example.com/.well-known/jwks.json',
      logoUri: 'string',
      clientUri: 'string',
      clientName: 'string',
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
      description: 'string',
      redirectUris: ['string'],
      allowedScopes: ['string'],
      allowedOrigins: ['string'],
      connectionConfig: {
        consentMethod: 'trusted',
      },
      allowedGrantTypes: ['client_credentials'],
      allowedAuthMethods: ['client_secret'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/oauth-clients yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"appType":"web","jwksUri":"https://example.com/.well-known/jwks.json","logoUri":"string","clientUri":"string","clientName":"string","publicKeys":[{"e":"AQAB","n":"0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx","x":"WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis","y":"y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE","alg":"RS256","crv":"P-384","kid":"key-1","kty":"RSA","use":"sig"}],"description":"string","redirectUris":["string"],"allowedScopes":["string"],"allowedOrigins":["string"],"connectionConfig":{"consentMethod":"trusted"},"allowedGrantTypes":["client_credentials"],"allowedAuthMethods":["client_secret"]}'
```

**Example Response:**

```json
{
  "appType": "web",
  "jwksUri": "https://example.com/.well-known/jwks.json",
  "logoUri": "string",
  "clientUri": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "deletedAt": "2018-10-30T07:06:22Z",
  "updatedAt": "2018-10-30T07:06:22Z",
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
  "publishedAt": "2018-10-30T07:06:22Z",
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

### GET /api/v1/oauth-clients/{id}

Retrieves the specified OAuth client.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `OAuthClientAdminReadResponse` | object | No | Response schema for reading an OAuth client as an admin user |

<details>
<summary>Properties of `OAuthClientAdminReadResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jwksUri` | string | No | URI of the JSON Web Key Set (JWKS) for the client |
| `clientId` | string | Yes | Client application id |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `redirectUris` | string[] | No | List of allowed redirect URIs for login |
| `clientSecrets` | object[] | No | Hints of any client application secrets |
| `allowedOrigins` | string[] | No | List of allowed origins for client |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client Enum: "client_secret", "private_key_jwt" |
| `appType` | string | Yes | Application type Enum: "web", "native", "spa", "anonymous-embed" |
| `logoUri` | string | No | URI for logo of client |
| `clientUri` | string | No | URI for homepage of client |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | Client application name |
| `disableTag` | string | No | Is set if client disabled |
| `description` | string | No | Client description |
| `publishedAt` | string | No | The timestamp which is set, if the client is published. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. For a full list of scopes see [qlik.dev/authenticate/oauth/scopes/](https://qlik.dev/authenticate/oauth/scopes/). |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types, only for use with appType: 'web' Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |

<details>
<summary>Properties of `publicKeys`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `clientSecrets`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `OAuthClientReadResponse` | object | No | Response schema for reading an OAuth client |

<details>
<summary>Properties of `OAuthClientReadResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | Yes | Client application id |
| `appType` | string | Yes | Application type Enum: "web", "native", "spa", "anonymous-embed" |
| `jwksUri` | string | No | URI of the JSON Web Key Set (JWKS) for the client |
| `logoUri` | string | No | URI for logo of client |
| `clientUri` | string | No | URI for homepage of client |
| `createdAt` | string | Yes | The timestamp for when the oauth-clients record was created. |
| `deletedAt` | string | No | The timestamp for when the oauth-clients record was deleted. |
| `updatedAt` | string | No | The timestamp for when the oauth-clients record was updated. |
| `clientName` | string | Yes | Client application name |
| `disableTag` | string | No | Is set if client disabled |
| `publicKeys` | object[] | No | List of public keys for JWT authentication |
| `description` | string | No | Client description |
| `publishedAt` | string | No | The timestamp which is set, if the client is published. |
| `allowedScopes` | string[] | No | List of allowed scopes for this client. For a full list of scopes see [qlik.dev/authenticate/oauth/scopes/](https://qlik.dev/authenticate/oauth/scopes/). |
| `clientSecrets` | object[] | No | Hints of any client application secrets |
| `createdByType` | string | No | The type of caller that created this client. Possible values are `user`, `service`, and `dcr` for Dynamic Client Registration. |
| `connectionConfig` | object | No | Optional settings for configuring the client connection. |
| `allowedGrantTypes` | string[] | No | Allowed grant types, only for use with appType: 'web' Enum: "client_credentials", "urn:qlik:oauth:user-impersonation" |
| `allowedAuthMethods` | string[] | No | List of allowed authentication methods for the client Enum: "client_secret", "private_key_jwt" |

<details>
<summary>Properties of `publicKeys`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `clientSecrets`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `connectionConfig`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/oauth-clients/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/oauth-clients/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "appType": "web",
  "jwksUri": "https://example.com/.well-known/jwks.json",
  "logoUri": "string",
  "clientUri": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "deletedAt": "2018-10-30T07:06:22Z",
  "updatedAt": "2018-10-30T07:06:22Z",
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
  "publishedAt": "2018-10-30T07:06:22Z",
  "allowedScopes": [
    "string"
  ],
  "clientSecrets": [
    {
      "hint": "string",
      "createdAt": "2018-10-30T07:06:22Z",
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

### PATCH /api/v1/oauth-clients/{id}

Updates the specified OAuth client. Returns 202 Accepted with a client secret in the response body if a client secret is generated during the update (e.g., when adding client_secret to allowedAuthMethods). Otherwise returns 204 No Content.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed Enum: "add", "remove", "replace" |
| `path` | string | Yes | The path for the given resource field to patch Enum: "/allowedOrigins", "/clientName", "/clientUri", "/description", "/logoUri", "/redirectUris", "/allowedScopes", "/allowedGrantTypes", "/publicKeys", "/allowedAuthMethods", "/jwksUri" |
| `value` | string \| array | No | The value to be used for this operation. |

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

Accepted - Client secret was generated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientSecret` | string | Yes | The generated client application secret |

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/oauth-clients/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: '/allowedOrigins',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/oauth-clients/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/allowedOrigins","value":"string"}]'
```

**Example Response:**

```json
{
  "clientSecret": "string"
}
```

---

### DELETE /api/v1/oauth-clients/{id}

Delete the specified OAuth client.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-confirm-delete` | string | Yes | A confirmation string that should match the id of the oauth-client resource to be deleted |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/oauth-clients/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/oauth-clients/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}" \
-X DELETE \
-H "qlik-confirm-delete: string" \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/oauth-clients/{id}/actions/publish

Publishes the specified OAuth client. By default, OAuth clients are bound to the tenant that created it. Publishing shares the client and makes it available to all other tenants within a region. Third-party applications connecting to Qlik Cloud can then have the same client ID for all Qlik Cloud tenants.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `publishedAt` | string | Yes | The timestamp which is set, if the client is published. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/oauth-clients/{id}/actions/publish` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/actions/publish',
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
# qlik-cli has not implemented support for POST /api/v1/oauth-clients/{id}/actions/publish yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/actions/publish" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "publishedAt": "2018-10-30T07:06:22Z"
}
```

---

### POST /api/v1/oauth-clients/{id}/client-secrets

Create a new client secret for the specified OAuth client. An OAuth client can have a maximum of 5 client secrets at one time.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | Client application hint |
| `clientId` | string | Yes | Client application id |
| `createdAt` | string | No | The timestamp for when the client-secret record was created. |
| `createdBy` | string | No | The identifier for the user that created the client-secret record. |
| `clientSecret` | string | Yes | Client application secret |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 409

The max number of client secrets is 5

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/oauth-clients/{id}/client-secrets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/client-secrets',
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
# qlik-cli has not implemented support for POST /api/v1/oauth-clients/{id}/client-secrets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/client-secrets" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "hint": "string",
  "clientId": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "string",
  "clientSecret": "string"
}
```

---

### DELETE /api/v1/oauth-clients/{id}/client-secrets/{hint}

Deletes a specific client secret for an OAuth client.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | string | Yes | The unique identifier for the OAuth secret |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/oauth-clients/{id}/client-secrets/{hint}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/client-secrets/{hint}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/oauth-clients/{id}/client-secrets/{hint} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/client-secrets/{hint}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/oauth-clients/{id}/connection-configs/me

Get configuration for consent method and status.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for an OAuth client |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Status |
| `consentMethod` | string | Yes | Consent method |
| `deletedByOwner` | boolean | No | OAuth client has been deleted by owning tenant, only applies for published clients. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/oauth-clients/{id}/connection-configs/me` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/connection-configs/me',
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
# qlik-cli has not implemented support for GET /api/v1/oauth-clients/{id}/connection-configs/me yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/connection-configs/me" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "string",
  "consentMethod": "string",
  "deletedByOwner": true
}
```

---

### PATCH /api/v1/oauth-clients/{id}/connection-configs/me

Updates the consent method for the specified OAuth client.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object[] | No | A JSON Patch document as defined in http://tools.ietf.org/html/rfc6902 |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No | Patch the consent method. Only `replace` is supported. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "replace" |
| `path` | string | Yes | Enum: "/consentMethod" |
| `value` | string | Yes | Enum: "required", "trusted" |

</details>

</details>

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/oauth-clients/{id}/connection-configs/me` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/connection-configs/me',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/consentMethod',
        value: 'required',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/oauth-clients/{id}/connection-configs/me yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/connection-configs/me" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/consentMethod","value":"required"}]'
```

---

### DELETE /api/v1/oauth-clients/{id}/connection-configs/me

Deletes the connection config for the calling tenant, related to the supplied client id.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the OAuth client |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of the error |
| `detail` | string | No | Additional details about the error |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/oauth-clients/{id}/connection-configs/me` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-clients/{id}/connection-configs/me',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/oauth-clients/{id}/connection-configs/me yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients/{id}/connection-configs/me" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
