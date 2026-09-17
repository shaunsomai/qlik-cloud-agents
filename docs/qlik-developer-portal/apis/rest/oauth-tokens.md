# OAuth tokens

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

List and revoke active OAuth tokens issued for your tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/oauth-tokens`](#get-apiv1oauth-tokens) | Retrieve list of OAuth tokens that the user has access to. Users assigned with a `TenantAdmin` role can list OAuth tokens generated for all users in the tenant. |
| `DELETE` | [`/api/v1/oauth-tokens/{tokenId}`](#delete-apiv1oauth-tokenstokenid) | Revokes a specific OAuth token by ID. Requesting user must have `TenantAdmin` role assigned to delete tokens owned by other users. |

## API Reference

### GET /api/v1/oauth-tokens

Retrieve list of OAuth tokens that the user has access to. Users assigned with a `TenantAdmin` role can list OAuth tokens generated for all users in the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | number | No | The maximum number of tokens to return. |
| `page` | string | No | The target page. |
| `sort` | string | No | The field to sort by. Enum: "userId" |
| `userId` | string | No | The ID of the user to limit results to. |

#### Responses

##### 200

The page result.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The token ID. |
| `userId` | string | Yes | The ID of the owning user. |
| `lastUsed` | string | No | The last time the token was used. |
| `tenantId` | string | Yes | The ID of the owning tenant. |
| `deviceType` | string | No | The type of the user device the authorization token is generated for (Tablet, Phone etc.). |
| `description` | string | No | The description of the token. |

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

Invalid request parameter for querying tokens.

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

Authentication failed.

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
// qlik-api has not implemented support for `GET /api/v1/oauth-tokens` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-tokens',
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
# qlik-cli has not implemented support for GET /api/v1/oauth-tokens yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-tokens" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "userId": "string",
      "lastUsed": "2018-10-30T07:06:22Z",
      "tenantId": "string",
      "deviceType": "string",
      "description": "string"
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

### DELETE /api/v1/oauth-tokens/{tokenId}

Revokes a specific OAuth token by ID. Requesting user must have `TenantAdmin` role assigned to delete tokens owned by other users.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tokenId` | string | Yes | The ID of the token to revoke. |

#### Responses

##### 204

Token deleted successfully.

##### 401

Authentication failed.

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
| `meta` | object | No | Non-standard information about the error. |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message. |
| `status` | string | No | The http status code. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/oauth-tokens/{tokenId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/oauth-tokens/{tokenId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/oauth-tokens/{tokenId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-tokens/{tokenId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
