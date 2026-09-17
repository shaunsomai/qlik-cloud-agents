# API keys

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

API keys can be used by developers to gain programmatic access to the Qlik platform, acting as their own user.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/api-keys`](#get-apiv1api-keys) | Lists API keys for the tenant. To list API keys owned by other users, requesting user must be assigned the `TenantAdmin` role. |
| `POST` | [`/api/v1/api-keys`](#post-apiv1api-keys) | Creates an API key, either for a user, or for configuring SCIM for a compatible Identity Provider. |
| `GET` | [`/api/v1/api-keys/{id}`](#get-apiv1api-keysid) | Returns the API key for a given API key ID. |
| `PATCH` | [`/api/v1/api-keys/{id}`](#patch-apiv1api-keysid) | Updates an API key description for a given API key ID. |
| `DELETE` | [`/api/v1/api-keys/{id}`](#delete-apiv1api-keysid) | Deletes or revokes an API key for a given API key ID. When the owner of the API key sends the request, the key will be deleted and removed from the tenant. When a user assigned the `TenantAdmin` role sends the request, the key will be disabled and marked as revoked. |
| `GET` | [`/api/v1/api-keys/configs/{tenantId}`](#get-apiv1api-keysconfigstenantid) | Retrieves the API key configuration for a tenant. |
| `PATCH` | [`/api/v1/api-keys/configs/{tenantId}`](#patch-apiv1api-keysconfigstenantid) | Updates the API keys configuration for a given tenant ID. |

## API Reference

### GET /api/v1/api-keys

Lists API keys for the tenant. To list API keys owned by other users, requesting user must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `createdByUser` | string | No | The user ID that created the API key. |
| `endingBefore` | string | No | Get resources with IDs that are lower than the target resource ID. Cannot be used in conjunction with startingAfter. |
| `limit` | number | No | Maximum number of API keys to retrieve. |
| `sort` | string | No | The field to sort by, with +/- prefix indicating sort order Enum: "createdByUser", "+createdByUser", "-createdByUser", "sub", "+sub", "-sub", "status", "+status", "-status", "description", "+description", "-description", "created", "+created", "-created" |
| `startingAfter` | string | No | Get resources with IDs that are higher than the target resource ID. Cannot be used in conjunction with endingBefore. |
| `status` | string | No | The status of the API key. Enum: "active", "expired", "revoked" |
| `sub` | string | No | The ID of the subject. For SCIM the format is `SCIM\\{{IDP-ID}}`, where `{{IDP-ID}}` is the ID of the IDP in Qlik. For users, use their user ID, e.g. `64ef645a3b7009d55dee5a2b`. |

#### Responses

##### 200

The list API keys result.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Properties of API keys in a given tenant. |
| `links` | object | Yes | Navigation links to page results. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique ID for the resource. |
| `sub` | string | Yes | The ID of the subject for the API key. For SCIM the format is `SCIM\\{{IDP-ID}}`, where `{{IDP-ID}}` is the ID of the IDP in Qlik. For users, use their user ID, e.g. `64ef645a3b7009d55dee5a2b`. |
| `expiry` | string | Yes | When the API key will expire and no longer be a valid authentication token. |
| `status` | string | Yes | The status of the API key. Enum: "active", "expired", "revoked" |
| `created` | string | No | When the API key was created. |
| `subType` | string | Yes | Type of the subject. For SCIM, it should be `externalClient`. Enum: "user", "externalClient" |
| `tenantId` | string | Yes | The tenant ID. |
| `description` | string | Yes | A description for the API key. |
| `lastUpdated` | string | No | When the API key was last updated. |
| `createdByUser` | string | Yes | The ID of the user who created the key. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the link. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the link. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | The URL for the link. |

</details>

</details>

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Requestor not allowed to list API keys.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/api-keys` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/api-keys', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/api-keys yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "sub": "SCIM\\\\215g5595380d646163cadbb9",
      "expiry": "2018-10-30T07:06:22Z",
      "status": "active",
      "created": "2018-10-30T07:06:22Z",
      "subType": "user",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "description": "string",
      "lastUpdated": "2018-10-30T07:06:22Z",
      "createdByUser": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
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

### POST /api/v1/api-keys

Creates an API key, either for a user, or for configuring SCIM for a compatible Identity Provider.
Sending `sub` and `subType` is required only for creating SCIM keys.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Properties that the user wants to set for the API key.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sub` | string | No | The ID of the subject for the API key. For SCIM the format is `SCIM\\{{IDP-ID}}`, where `{{IDP-ID}}` is the ID of the IDP in Qlik. When creating an API key for a user, this is their user ID, e.g. `64ef645a3b7009d55dee5a2b`, and will default to the requesting user if not provided. User must be assigned the `Developer` role. |
| `expiry` | string | No | The expiry of the API key, in ISO8601 duration format. For example, `P7D` sets expiry after 7 days. If not provided, defaults to the maximum API key or SCIM key expiry configured in the tenant. |
| `subType` | string | No | Type of the subject. For SCIM, it should be `externalClient`. If not specified, defaults to `user`. Enum: "user", "externalClient" |
| `description` | string | Yes | Text that describes the API key. |

#### Responses

##### 201

Created the API key successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique ID for the resource. |
| `sub` | string | Yes | The ID of the subject for the API key. |
| `token` | string | Yes | The generated signed JWT. |
| `expiry` | string | Yes | When the API key will expire and no longer be a valid authentication token. |
| `status` | string | Yes | The status of the API key. Enum: "active", "expired", "revoked" |
| `created` | string | No | When the API key was created. |
| `subType` | string | Yes | Type of the subject. Enum: "user" |
| `tenantId` | string | Yes | The tenant ID. |
| `description` | string | Yes | A description for the API key. |
| `lastUpdated` | string | No | When the API key was last updated. |
| `createdByUser` | string | Yes | The id of the user who created the key. |

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Requestor not allowed to create an API key

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `POST /api/v1/api-keys` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/api-keys', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    sub: 'SCIM\\\\215g5595380d646163cadbb9',
    expiry: 'P7D',
    subType: 'user',
    description: 'string',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/api-keys yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"sub":"SCIM\\\\215g5595380d646163cadbb9","expiry":"P7D","subType":"user","description":"string"}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sub": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "token": "string",
  "expiry": "2018-10-30T07:06:22Z",
  "status": "active",
  "created": "2018-10-30T07:06:22Z",
  "subType": "user",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "description": "string",
  "lastUpdated": "2018-10-30T07:06:22Z",
  "createdByUser": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
}
```

---

### GET /api/v1/api-keys/{id}

Returns the API key for a given API key ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the API key to be retrieved. |

#### Responses

##### 200

Returns an API key resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique ID for the resource. |
| `sub` | string | Yes | The ID of the subject for the API key. For SCIM the format is `SCIM\\{{IDP-ID}}`, where `{{IDP-ID}}` is the ID of the IDP in Qlik. For users, use their user ID, e.g. `64ef645a3b7009d55dee5a2b`. |
| `expiry` | string | Yes | When the API key will expire and no longer be a valid authentication token. |
| `status` | string | Yes | The status of the API key. Enum: "active", "expired", "revoked" |
| `created` | string | No | When the API key was created. |
| `subType` | string | Yes | Type of the subject. For SCIM, it should be `externalClient`. Enum: "user", "externalClient" |
| `tenantId` | string | Yes | The tenant ID. |
| `description` | string | Yes | A description for the API key. |
| `lastUpdated` | string | No | When the API key was last updated. |
| `createdByUser` | string | Yes | The ID of the user who created the key. |

##### 403

Requestor not allowed to query this API key.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

API key was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/api-keys/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/api-keys/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/api-keys/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "sub": "SCIM\\\\215g5595380d646163cadbb9",
  "expiry": "2018-10-30T07:06:22Z",
  "status": "active",
  "created": "2018-10-30T07:06:22Z",
  "subType": "user",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "description": "string",
  "lastUpdated": "2018-10-30T07:06:22Z",
  "createdByUser": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
}
```

---

### PATCH /api/v1/api-keys/{id}

Updates an API key description for a given API key ID.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the API key resource to be updated. |

#### Request Body

**Required**

Properties that the user wants to update for the API key.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/description" |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 204

API key updated successfully.

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Requestor not allowed to update this API key.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

API key was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `PATCH /api/v1/api-keys/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/api-keys/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/description',
        value: 'my new description',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/api-keys/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/description","value":"my new description"}]'
```

---

### DELETE /api/v1/api-keys/{id}

Deletes or revokes an API key for a given API key ID. When the owner of the API key sends the request, the key will be deleted and removed from the tenant. When a user assigned the `TenantAdmin` role sends the request, the key will be disabled and marked as revoked.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the API key to be retrieved. |

#### Responses

##### 204

Deleted or revoked an API key resource.

##### 403

Requestor not allowed to delete or revoke this API key.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

API key was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `DELETE /api/v1/api-keys/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/api-keys/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/api-keys/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/api-keys/configs/{tenantId}

Retrieves the API key configuration for a tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The tenant ID from which you wish to retrieve the API key configuration. |

#### Responses

##### 200

API keys configuration.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `max_keys_per_user` | number | No | The maximum number of active API keys that any user can create for the specified tenant. |
| `max_api_key_expiry` | string | No | The maximum lifetime, in ISO8601 duration format, for which an API key can be issued for the specified tenant, e.g. `P7D` for 7 days. |
| `scim_externalClient_expiry` | string | No | The expiry of the scim `externalClient` token in ISO8601 duration format, e.g. `P365D` for 365 days. Used during the creation of an `externalClient` API key for configuring a SCIM compatible Identity Provider. |

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/api-keys/configs/{tenantId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/api-keys/configs/{tenantId}',
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
# qlik-cli has not implemented support for GET /api/v1/api-keys/configs/{tenantId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys/configs/{tenantId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "max_keys_per_user": 5,
  "max_api_key_expiry": "PT24H",
  "scim_externalClient_expiry": "P365D"
}
```

---

### PATCH /api/v1/api-keys/configs/{tenantId}

Updates the API keys configuration for a given tenant ID.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | Yes | The tenant ID of the API keys configuration to be retrieved. |

#### Request Body

**Required**

Configurations that the user wants to update for API keys.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/max_api_key_expiry", "/max_keys_per_user", "/scim_externalClient_expiry" |
| `value` | any | Yes | The value to be used for this operation. |

#### Responses

##### 204

API keys configuration updated successfully.

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Requestor not allowed to update the API keys configuration.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Failed to update the API keys configuration.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
| `errors` | object[] | No | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `PATCH /api/v1/api-keys/configs/{tenantId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/api-keys/configs/{tenantId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/max_keys_per_user',
        value: 10,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/api-keys/configs/{tenantId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys/configs/{tenantId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/max_keys_per_user","value":10}]'
```

---
