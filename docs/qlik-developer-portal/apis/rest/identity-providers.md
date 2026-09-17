# Identity providers

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Identity providers define how your users authenticate to your tenant when attempting to access content.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/identity-providers`](#get-apiv1identity-providers) | This endpoint retrieves any IdPs registered on the tenant. |
| `POST` | [`/api/v1/identity-providers`](#post-apiv1identity-providers) | Creates a new IdP on a tenant. Requesting user must be assigned the `TenantAdmin` role. For non-interactive IdPs (e.g. JWT), IdP must be created by sending `options` payload. For interactive IdPs (e.g. SAML or OIDC), send `pendingOptions` payload to require the interactive verification step; or send `options` payload with `skipVerify` set to `true` to skip validation step and make IdP immediately available. |
| `GET` | [`/api/v1/identity-providers/.well-known/metadata.json`](#get-apiv1identity-providerswell-knownmetadatajson) | Returns IdP configuration metadata supported on the tenant. Clients can use this information to programmatically configure their interactions with Qlik Cloud. |
| `GET` | [`/api/v1/identity-providers/{id}`](#get-apiv1identity-providersid) | Retrieves a specific IdP. Requesting user must be assigned the `TenantAdmin` role. |
| `PATCH` | [`/api/v1/identity-providers/{id}`](#patch-apiv1identity-providersid) | Updates the configuration of an IdP. Requesting user must be assigned the `TenantAdmin` role. Partial failure is treated as complete failure and returns an error. |
| `DELETE` | [`/api/v1/identity-providers/{id}`](#delete-apiv1identity-providersid) | Deletes an identity provider. Requesting user must be assigned the `TenantAdmin` role. |
| `GET` | [`/api/v1/identity-providers/me/meta`](#get-apiv1identity-providersmemeta) | Retrieves default IdP metadata when no interactive IdP is enabled. |
| `GET` | [`/api/v1/identity-providers/status`](#get-apiv1identity-providersstatus) | Retrieves the status of all IdP configurations. Requires `TenantAdmin` role. |

## API Reference

### GET /api/v1/identity-providers

This endpoint retrieves any IdPs registered on the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `active` | boolean | No | If provided, filters the results by the active field. |
| `limit` | number | No | The number of IdP entries to retrieve. |
| `next` | string | No | The next page cursor. |
| `prev` | string | No | The previous page cursor. |

#### Responses

##### 200

Success

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | undefined[] | No | An array of IdPs. |
| `links` | object | No | Contains pagination links. |

<details>
<summary>Properties of `data`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPOIDC` | object | No | An OIDC-compliant identity provider. |

<details>
<summary>Properties of `IDPOIDC`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPSAML` | object | No | A SAML-compliant identity provider. |

<details>
<summary>Properties of `IDPSAML`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPJWTAuth` | object | No | An identity provider for JWT authentication. |

<details>
<summary>Properties of `IDPJWTAuth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the next page of items. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the previous page of items. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | Link to the current page of items. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/identity-providers` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers',
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
# qlik-cli has not implemented support for GET /api/v1/identity-providers yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "meta": {},
      "active": true,
      "created": "2018-10-30T07:06:22Z",
      "protocol": "OIDC",
      "provider": "auth0",
      "tenantIds": [
        "string"
      ],
      "description": "string",
      "interactive": true,
      "lastUpdated": "2018-10-30T07:06:22Z",
      "clockToleranceSec": 42,
      "createNewUsersOnLogin": true,
      "postLogoutRedirectUri": "string",
      "options": {
        "realm": "string",
        "scope": "string",
        "issuer": "string",
        "clientId": "string",
        "clientSecret": "string",
        "discoveryUrl": "string",
        "claimsMapping": {
          "sub": [
            "string"
          ],
          "name": [
            "string"
          ],
          "email": [
            "string"
          ],
          "groups": [
            "string"
          ],
          "locale": [
            "string"
          ],
          "picture": [
            "string"
          ],
          "zoneinfo": [
            "string"
          ],
          "client_id": [
            "string"
          ],
          "email_verified": [
            "string"
          ]
        },
        "decryptingKey": {
          "jwks": "string",
          "keyId": "string",
          "keySize": 42,
          "keyType": "string",
          "createdAt": "2018-10-30T07:06:22Z",
          "createdBy": "string",
          "publicKey": "string",
          "certificate": "string"
        },
        "openid_configuration": {
          "issuer": "string",
          "jwks_uri": "string",
          "token_endpoint": "string",
          "userinfo_endpoint": "string",
          "end_session_endpoint": "string",
          "authorization_endpoint": "string",
          "introspection_endpoint": "string"
        },
        "blockOfflineAccessScope": true,
        "emailVerifiedAlwaysTrue": true
      },
      "pendingState": "verified",
      "pendingResult": {
        "error": "string",
        "status": "success",
        "started": "2018-10-30T07:06:22Z",
        "protocol": "OIDC",
        "idpClaims": {},
        "oauth2Error": {
          "error": "string",
          "errorURI": "string",
          "errorDescription": "string"
        },
        "resultantClaims": {}
      },
      "pendingOptions": {
        "realm": "string",
        "scope": "string",
        "issuer": "string",
        "clientId": "string",
        "clientSecret": "string",
        "discoveryUrl": "string",
        "claimsMapping": {
          "sub": [
            "string"
          ],
          "name": [
            "string"
          ],
          "email": [
            "string"
          ],
          "groups": [
            "string"
          ],
          "locale": [
            "string"
          ],
          "picture": [
            "string"
          ],
          "zoneinfo": [
            "string"
          ],
          "client_id": [
            "string"
          ],
          "email_verified": [
            "string"
          ]
        },
        "decryptingKey": {
          "jwks": "string",
          "keyId": "string",
          "keySize": 42,
          "keyType": "string",
          "createdAt": "2018-10-30T07:06:22Z",
          "createdBy": "string",
          "publicKey": "string",
          "certificate": "string"
        },
        "openid_configuration": {
          "issuer": "string",
          "jwks_uri": "string",
          "token_endpoint": "string",
          "userinfo_endpoint": "string",
          "end_session_endpoint": "string",
          "authorization_endpoint": "string",
          "introspection_endpoint": "string"
        },
        "blockOfflineAccessScope": true,
        "emailVerifiedAlwaysTrue": true
      }
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
  }
}
```

---

### POST /api/v1/identity-providers

Creates a new IdP on a tenant. Requesting user must be assigned the `TenantAdmin` role. For non-interactive IdPs (e.g. JWT), IdP must be created by sending `options` payload. For interactive IdPs (e.g. SAML or OIDC), send `pendingOptions` payload to require the interactive verification step; or send `options` payload with `skipVerify` set to `true` to skip validation step and make IdP immediately available.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

Attributes that the user wants to set for a new identity provider resource.

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
| `CreateOIDCPayload` | object | No | Payload for creating an OIDC-compatible identity provider. |

<details>
<summary>Properties of `CreateOIDCPayload`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `options` | object | No | Required OIDC configurations for non-interactive IdPs and interactive IdPs with `skipVerify` flag enabled. |
| `protocol` | string | Yes | The protocol to be used for communicating with the identity provider. Enum: "OIDC" |
| `provider` | string | Yes | The identity provider to be used. Enum: "auth0", "okta", "generic", "salesforce", "keycloak", "adfs", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers that map to the given IdP. |
| `skipVerify` | boolean | No | If set to `true`, skips IdP verification process and assumes the IdP is verified. |
| `description` | string | No |  |
| `interactive` | boolean | Yes | Indicates whether the IdP is meant for interactive login. |
| `pendingOptions` | object | No | Required OIDC configurations for interactive IdPs that require verification. |
| `clockToleranceSec` | integer | No | There can be clock skew between the IdP and Qlik's login server. In these cases, a tolerance can be set. |
| `createNewUsersOnLogin` | boolean | No | Tells the consumer of the IdP that new users should be created on login if they don't exist. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `CreateJWTAuthPayload` | object | No | Payload for creating an identity provider using JWT authentication. |

<details>
<summary>Properties of `CreateJWTAuthPayload`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `options` | object | Yes | Required IdP configurations. |
| `protocol` | string | Yes | The protocol to be used for communicating with the identity provider. Enum: "jwtAuth" |
| `provider` | string | Yes | The identity provider to be used. Enum: "external" |
| `tenantIds` | string[] | No | The tenant identifiers that map to the given IdP. |
| `description` | string | No |  |
| `clockToleranceSec` | integer | No | There can be clock skew between the IdP and Qlik's login server. In these cases, a tolerance can be set. |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `CreateSAMLPayload` | object | No | Payload for creating a SAML compatible identity provider. |

<details>
<summary>Properties of `CreateSAMLPayload`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `options` | object | No | Required SAML configurations for IdPs with `skipVerify` flag enabled. |
| `protocol` | string | Yes | The protocol to be used for communicating with the identity provider. Enum: "SAML" |
| `provider` | string | Yes | The identity provider to be used. Enum: "okta", "generic", "adfs", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers that map to the given IdP. |
| `skipVerify` | boolean | No | If set to `true`, skips IdP verification process and assumes the IdP is verified. |
| `description` | string | No |  |
| `interactive` | boolean | Yes | Indicates whether the IdP is meant for interactive login. Must be true for SAML IdPs. |
| `pendingOptions` | object | No | Required configurations for SAML IdPs that require verification. |
| `clockToleranceSec` | integer | No | There can be clock skew between the IdP and Qlik's login server. In these cases, a tolerance can be set. |
| `createNewUsersOnLogin` | boolean | No | Tells the consumer of the IdP that new users should be created on login if they don't exist. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

Created

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
| `IDPOIDC` | object | No | An OIDC-compliant identity provider. |

<details>
<summary>Properties of `IDPOIDC`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPSAML` | object | No | A SAML-compliant identity provider. |

<details>
<summary>Properties of `IDPSAML`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPJWTAuth` | object | No | An identity provider for JWT authentication. |

<details>
<summary>Properties of `IDPJWTAuth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden. User missing `TenantAdmin` role, or the tenantID in the JWT does not match any of the tenantIDs in the payload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/identity-providers` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      options: {
        realm: 'string',
        audience: 'string',
        discoveryUrl: 'string',
        claimsMapping: {
          sub: ['string'],
          client_id: ['string'],
        },
        allowedClientIds: ['string'],
        openid_configuration: {
          issuer: 'string',
          jwks_uri: 'string',
          token_endpoint: 'string',
          userinfo_endpoint: 'string',
          end_session_endpoint: 'string',
          authorization_endpoint: 'string',
          introspection_endpoint: 'string',
        },
      },
      protocol: 'OIDC',
      provider: 'auth0',
      tenantIds: ['string'],
      skipVerify: false,
      description: 'string',
      interactive: false,
      pendingOptions: {
        realm: 'string',
        scope: 'string',
        clientId: 'string',
        clientSecret: 'string',
        discoveryUrl: 'string',
        claimsMapping: {
          sub: ['string'],
          name: ['string'],
          email: ['string'],
          groups: ['string'],
          locale: ['string'],
          picture: ['string'],
          zoneinfo: ['string'],
          client_id: ['string'],
          email_verified: ['string'],
        },
        decryptingKey: {
          jwks: 'string',
          keyId: 'string',
          keySize: 42,
          keyType: 'string',
          createdAt: '2018-10-30T07:06:22Z',
          createdBy: 'string',
          publicKey: 'string',
          certificate: 'string',
        },
        idTokenSignatureAlg: 'RS256',
        openid_configuration: {
          issuer: 'string',
          jwks_uri: 'string',
          token_endpoint: 'string',
          userinfo_endpoint: 'string',
          end_session_endpoint: 'string',
          authorization_endpoint: 'string',
          introspection_endpoint: 'string',
        },
        useClaimsFromIdToken: true,
        blockOfflineAccessScope: true,
        emailVerifiedAlwaysTrue: true,
      },
      clockToleranceSec: 5,
      createNewUsersOnLogin: true,
      postLogoutRedirectUri: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/identity-providers yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"options":{"realm":"string","audience":"string","discoveryUrl":"string","claimsMapping":{"sub":["string"],"client_id":["string"]},"allowedClientIds":["string"],"openid_configuration":{"issuer":"string","jwks_uri":"string","token_endpoint":"string","userinfo_endpoint":"string","end_session_endpoint":"string","authorization_endpoint":"string","introspection_endpoint":"string"}},"protocol":"OIDC","provider":"auth0","tenantIds":["string"],"skipVerify":false,"description":"string","interactive":false,"pendingOptions":{"realm":"string","scope":"string","clientId":"string","clientSecret":"string","discoveryUrl":"string","claimsMapping":{"sub":["string"],"name":["string"],"email":["string"],"groups":["string"],"locale":["string"],"picture":["string"],"zoneinfo":["string"],"client_id":["string"],"email_verified":["string"]},"decryptingKey":{"jwks":"string","keyId":"string","keySize":42,"keyType":"string","createdAt":"2018-10-30T07:06:22Z","createdBy":"string","publicKey":"string","certificate":"string"},"idTokenSignatureAlg":"RS256","openid_configuration":{"issuer":"string","jwks_uri":"string","token_endpoint":"string","userinfo_endpoint":"string","end_session_endpoint":"string","authorization_endpoint":"string","introspection_endpoint":"string"},"useClaimsFromIdToken":true,"blockOfflineAccessScope":true,"emailVerifiedAlwaysTrue":true},"clockToleranceSec":5,"createNewUsersOnLogin":true,"postLogoutRedirectUri":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "meta": {},
  "active": true,
  "created": "2018-10-30T07:06:22Z",
  "protocol": "OIDC",
  "provider": "auth0",
  "tenantIds": [
    "string"
  ],
  "description": "string",
  "interactive": true,
  "lastUpdated": "2018-10-30T07:06:22Z",
  "clockToleranceSec": 42,
  "createNewUsersOnLogin": true,
  "postLogoutRedirectUri": "string",
  "options": {
    "realm": "string",
    "scope": "string",
    "issuer": "string",
    "clientId": "string",
    "clientSecret": "string",
    "discoveryUrl": "string",
    "claimsMapping": {
      "sub": [
        "string"
      ],
      "name": [
        "string"
      ],
      "email": [
        "string"
      ],
      "groups": [
        "string"
      ],
      "locale": [
        "string"
      ],
      "picture": [
        "string"
      ],
      "zoneinfo": [
        "string"
      ],
      "client_id": [
        "string"
      ],
      "email_verified": [
        "string"
      ]
    },
    "decryptingKey": {
      "jwks": "string",
      "keyId": "string",
      "keySize": 42,
      "keyType": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "publicKey": "string",
      "certificate": "string"
    },
    "openid_configuration": {
      "issuer": "string",
      "jwks_uri": "string",
      "token_endpoint": "string",
      "userinfo_endpoint": "string",
      "end_session_endpoint": "string",
      "authorization_endpoint": "string",
      "introspection_endpoint": "string"
    },
    "blockOfflineAccessScope": true,
    "emailVerifiedAlwaysTrue": true
  },
  "pendingState": "verified",
  "pendingResult": {
    "error": "string",
    "status": "success",
    "started": "2018-10-30T07:06:22Z",
    "protocol": "OIDC",
    "idpClaims": {},
    "oauth2Error": {
      "error": "string",
      "errorURI": "string",
      "errorDescription": "string"
    },
    "resultantClaims": {}
  },
  "pendingOptions": {
    "realm": "string",
    "scope": "string",
    "issuer": "string",
    "clientId": "string",
    "clientSecret": "string",
    "discoveryUrl": "string",
    "claimsMapping": {
      "sub": [
        "string"
      ],
      "name": [
        "string"
      ],
      "email": [
        "string"
      ],
      "groups": [
        "string"
      ],
      "locale": [
        "string"
      ],
      "picture": [
        "string"
      ],
      "zoneinfo": [
        "string"
      ],
      "client_id": [
        "string"
      ],
      "email_verified": [
        "string"
      ]
    },
    "decryptingKey": {
      "jwks": "string",
      "keyId": "string",
      "keySize": 42,
      "keyType": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "publicKey": "string",
      "certificate": "string"
    },
    "openid_configuration": {
      "issuer": "string",
      "jwks_uri": "string",
      "token_endpoint": "string",
      "userinfo_endpoint": "string",
      "end_session_endpoint": "string",
      "authorization_endpoint": "string",
      "introspection_endpoint": "string"
    },
    "blockOfflineAccessScope": true,
    "emailVerifiedAlwaysTrue": true
  }
}
```

---

### GET /api/v1/identity-providers/.well-known/metadata.json

Returns IdP configuration metadata supported on the tenant. Clients can use this information to programmatically configure their interactions with Qlik Cloud.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Success

**Content-Type:** `application/json`


#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/identity-providers/.well-known/metadata.json` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/.well-known/metadata.json',
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
# qlik-cli has not implemented support for GET /api/v1/identity-providers/.well-known/metadata.json yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/.well-known/metadata.json" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{}
```

---

### GET /api/v1/identity-providers/{id}

Retrieves a specific IdP. Requesting user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The identity provider ID. |

#### Responses

##### 200

Success

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
| `IDPOIDC` | object | No | An OIDC-compliant identity provider. |

<details>
<summary>Properties of `IDPOIDC`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPSAML` | object | No | A SAML-compliant identity provider. |

<details>
<summary>Properties of `IDPSAML`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |
| `pendingState` | string | No | The state of pendingOptions. This represents the latest IdP test result. Enum: "verified", "pending", "error" |
| `pendingResult` | object | No |  |
| `pendingOptions` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingResult`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `pendingOptions`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `IDPJWTAuth` | object | No | An identity provider for JWT authentication. |

<details>
<summary>Properties of `IDPJWTAuth`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the IdP. |
| `meta` | object | No |  |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `created` | string | No | The timestamp for when the IdP was created. |
| `protocol` | string | No | The protocol to be used for communicating with the identity provider. Valid values are `OIDC`, `SAML`, `jwtAuth`, and `qsefw-local-bearer-token`. Enum: "OIDC", "SAML", "jwtAuth", "qsefw-local-bearer-token" |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `tenantIds` | string[] | No | The tenant identifiers associated with the given IdP. |
| `description` | string | No |  |
| `interactive` | boolean | No | Indicates the type of connection with the IdP, either interactive login or a machine to machine connection. |
| `lastUpdated` | string | No | The timestamp for when the IdP was last updated. |
| `clockToleranceSec` | integer | No |  |
| `createNewUsersOnLogin` | boolean | No | When the flag is true, new users should be created when logging in for the first time. |
| `postLogoutRedirectUri` | string | No | Direct the user on logout to a specific URI. |
| `options` | object | No |  |

<details>
<summary>Properties of `options`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/identity-providers/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/identity-providers/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "meta": {},
  "active": true,
  "created": "2018-10-30T07:06:22Z",
  "protocol": "OIDC",
  "provider": "auth0",
  "tenantIds": [
    "string"
  ],
  "description": "string",
  "interactive": true,
  "lastUpdated": "2018-10-30T07:06:22Z",
  "clockToleranceSec": 42,
  "createNewUsersOnLogin": true,
  "postLogoutRedirectUri": "string",
  "options": {
    "realm": "string",
    "scope": "string",
    "issuer": "string",
    "clientId": "string",
    "clientSecret": "string",
    "discoveryUrl": "string",
    "claimsMapping": {
      "sub": [
        "string"
      ],
      "name": [
        "string"
      ],
      "email": [
        "string"
      ],
      "groups": [
        "string"
      ],
      "locale": [
        "string"
      ],
      "picture": [
        "string"
      ],
      "zoneinfo": [
        "string"
      ],
      "client_id": [
        "string"
      ],
      "email_verified": [
        "string"
      ]
    },
    "decryptingKey": {
      "jwks": "string",
      "keyId": "string",
      "keySize": 42,
      "keyType": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "publicKey": "string",
      "certificate": "string"
    },
    "openid_configuration": {
      "issuer": "string",
      "jwks_uri": "string",
      "token_endpoint": "string",
      "userinfo_endpoint": "string",
      "end_session_endpoint": "string",
      "authorization_endpoint": "string",
      "introspection_endpoint": "string"
    },
    "blockOfflineAccessScope": true,
    "emailVerifiedAlwaysTrue": true
  },
  "pendingState": "verified",
  "pendingResult": {
    "error": "string",
    "status": "success",
    "started": "2018-10-30T07:06:22Z",
    "protocol": "OIDC",
    "idpClaims": {},
    "oauth2Error": {
      "error": "string",
      "errorURI": "string",
      "errorDescription": "string"
    },
    "resultantClaims": {}
  },
  "pendingOptions": {
    "realm": "string",
    "scope": "string",
    "issuer": "string",
    "clientId": "string",
    "clientSecret": "string",
    "discoveryUrl": "string",
    "claimsMapping": {
      "sub": [
        "string"
      ],
      "name": [
        "string"
      ],
      "email": [
        "string"
      ],
      "groups": [
        "string"
      ],
      "locale": [
        "string"
      ],
      "picture": [
        "string"
      ],
      "zoneinfo": [
        "string"
      ],
      "client_id": [
        "string"
      ],
      "email_verified": [
        "string"
      ]
    },
    "decryptingKey": {
      "jwks": "string",
      "keyId": "string",
      "keySize": 42,
      "keyType": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "publicKey": "string",
      "certificate": "string"
    },
    "openid_configuration": {
      "issuer": "string",
      "jwks_uri": "string",
      "token_endpoint": "string",
      "userinfo_endpoint": "string",
      "end_session_endpoint": "string",
      "authorization_endpoint": "string",
      "introspection_endpoint": "string"
    },
    "blockOfflineAccessScope": true,
    "emailVerifiedAlwaysTrue": true
  }
}
```

---

### PATCH /api/v1/identity-providers/{id}

Updates the configuration of an IdP. Requesting user must be assigned the `TenantAdmin` role. Partial failure is treated as complete failure and returns an error.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The identity provider ID. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `QLIK-IDP-POPTS-MATCH` | string | No | A unique string representing a hash that should map to an IdP's hash representation of the current configuration being tested. |

#### Request Body

Attributes that the user wants to patially update for an identity provider resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | array | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object[] | No | A patch request for an identity provider using the `OIDC` protocol. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The "operation" to be performed on a given IdP. Currently supports a custom operation value called "promote-options" that allows the test configuration to be promoted to the current configuration used for login. Enum: "replace", "promote-options" |
| `path` | string | No | The "path" to the part of the IdP document. Enum: "/active", "/description", "/meta", "/options", "/options/realm", "/options/discoveryUrl", "/options/claimsMapping", "/pendingOptions", "/pendingOptions/realm", "/pendingOptions/discoveryUrl", "/pendingOptions/clientId", "/pendingOptions/clientSecret", "/pendingOptions/emailVerifiedAlwaysTrue", "/pendingOptions/claimsMapping", "/postLogoutRedirectUri", "/clockToleranceSec", "/pendingOptions/idTokenSignatureAlg", "/pendingOptions/decryptingKey" |
| `value` | any | No | The "value" data type is dependent on the path value being used. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object[] | No | A patch request for an identity provider using the `SAML` protocol. Supports a custom operation value called `promote-options` that allows the test configuration (`pendingOptions`) to be promoted to the live configuration (`options`) used for login.' |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The "operation" to be performed on a given IdP. Enum: "replace", "promote-options" |
| `path` | string | No | The "path" to the part of the IdP document. Enum: "/active", "/description", "/pendingOptions", "/pendingOptions/nameIdFormat", "/pendingOptions/allowIdpInitiatedLogin", "/pendingOptions/entityId", "/pendingOptions/signOnUrl", "/pendingOptions/metadata", "/pendingOptions/certificates", "/pendingOptions/claimsMapping", "/postLogoutRedirectUri", "/clockToleranceSec" |
| `value` | any | No | The "value" data type is dependent on the path value being used. |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object[] | No | A patch request for an identity provider using the `jwtAuth` protocol. |

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The "operation" to be performed on a given IdP. Enum: "replace" |
| `path` | string | No | The "path" to the part of the IdP document. Enum: "/description" |
| `value` | any | No | The "value" data type is dependent on the path value being used. |

</details>

</details>

#### Responses

##### 204

Success

##### 400

Bad request. Invalid request body, URL, or state transition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Access Denied. Only the edge-auth service or TenantAdmin user request can patch an IdP.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 412

Precondition Failed. Missing QLIK-IDP-OPTS-MATCH header, or value doesn't match against IdP test configuration value.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error, the operation failed unexpectedly

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/identity-providers/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      { op: 'replace', path: '/active' },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/identity-providers/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/active"}]'
```

---

### DELETE /api/v1/identity-providers/{id}

Deletes an identity provider. Requesting user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The identity provider ID. |

#### Responses

##### 204

Success

##### 400

Bad request. The interactive IdP for the tenant can't be deleted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/identity-providers/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/identity-providers/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/identity-providers/me/meta

Retrieves default IdP metadata when no interactive IdP is enabled.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Success

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userPortalLink` | string | No | A link to direct you to where you can manage your Qlik account. Only available if the default identity provider is used (no custom interactive identity providers are active). |
| `upgradeSubscriptionLink` | string | No | A link to direct you to where you can upgrade your trial or manage your subscriptions. Only available if the default identity provider is used (no custom interactive identity providers are active). |

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/identity-providers/me/meta` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/me/meta',
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
# qlik-cli has not implemented support for GET /api/v1/identity-providers/me/meta yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/me/meta" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "userPortalLink": "string",
  "upgradeSubscriptionLink": "string"
}
```

---

### GET /api/v1/identity-providers/status

Retrieves the status of all IdP configurations. Requires `TenantAdmin` role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Success

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `idps_metadata` | object[] | No | A list of IdP metadata. |
| `active_interactive_idps_count` | number | No | The number of active interactive IdPs. |

<details>
<summary>Properties of `idps_metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `active` | boolean | No | Indicates whether the IdP is available for use. |
| `provider` | string | No | The identity provider to be used. If protocol is `OIDC`, the valid values are `auth0`, `okta`, `generic`, `salesforce`, `keycloak`, `adfs`, and `azureAD`. If protocol is `jwtAuth`, the valid value is `external`. Enum: "auth0", "okta", "qlik", "generic", "salesforce", "keycloak", "adfs", "external", "azureAD" |
| `interactive` | boolean | No | Indicates whether the IdP is meant for interactive login. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/identity-providers/status` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/identity-providers/status',
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
# qlik-cli has not implemented support for GET /api/v1/identity-providers/status yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers/status" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "idps_metadata": [
    {
      "active": true,
      "provider": "auth0",
      "interactive": true
    }
  ],
  "active_interactive_idps_count": 42
}
```

---
