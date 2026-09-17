# CSRF token

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

A CSRF token is a secure random token (e.g., synchronizer token or challenge token) that is used to prevent CSRF attacks. This API retrieves the token for the current user session.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/csrf-token`](#get-apiv1csrf-token) | Returns CSRF token via the qlik-csrf-token header. |

## API Reference

### GET /api/v1/csrf-token

Returns CSRF token via the qlik-csrf-token header.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 204

Successfully returned token in qlik-csrf-token header

##### 400

Token is not supported for the auth mechanism being used.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message |
| `status` | string | No | The http status code. |

</details>

##### 404

Token not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Non-standard information about the error |
| `title` | string | Yes | The error title. |
| `detail` | string | No | The detailed error message |
| `status` | string | No | The http status code. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/csrf-token` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csrf-token',
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
# qlik-cli has not implemented support for GET /api/v1/csrf-token yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csrf-token" \
-H "Authorization: Bearer <access_token>"
```

---
