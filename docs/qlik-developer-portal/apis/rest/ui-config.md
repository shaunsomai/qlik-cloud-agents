# Pinned links

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Pinned links are administrator-defined URLs which appear for all users under the More button in the global navigation menu.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/ui-config/pinned-links`](#get-apiv1ui-configpinned-links) | Retrieves a list of all pinned links. All users can list pinned links. This endpoint does not support pagination as a tenant can have a maximum of 50 pinned links at one time. |
| `POST` | [`/api/v1/ui-config/pinned-links`](#post-apiv1ui-configpinned-links) | Creates a pinned link, which will appear below any existing pinned links in the tenant. Requires calling user to be assigned the `TenantAdmin` role. A tenant can have a maximum of 50 pinned links. |
| `GET` | [`/api/v1/ui-config/pinned-links/{id}`](#get-apiv1ui-configpinned-linksid) | Retrieves a specific pinned link. |
| `PATCH` | [`/api/v1/ui-config/pinned-links/{id}`](#patch-apiv1ui-configpinned-linksid) | Updates a specific pinned link with an array of JSON patches. Requires calling user to be assigned the `TenantAdmin` role. |
| `DELETE` | [`/api/v1/ui-config/pinned-links/{id}`](#delete-apiv1ui-configpinned-linksid) | Deletes a specific pinned link. Requires calling user to be assigned the `TenantAdmin` role. |
| `POST` | [`/api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links`](#post-apiv1ui-configpinned-linksactionsbulk-create-pinned-links) | Creates one or more pinned links for navigation, an alternative method to multiple calls to `/ui-config/pinned-links`. Links are displayed below any existing pinned links, and will be added in the order sent in the request. Requires calling user to be assigned the `TenantAdmin` role. A tenant can have a maximum of 50 pinned links. |
| `POST` | [`/api/v1/ui-config/pinned-links/actions/delete-all-pinned-links`](#post-apiv1ui-configpinned-linksactionsdelete-all-pinned-links) | Deletes all pinned links in the tenant. Requires calling user to be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/v1/ui-config/pinned-links

Retrieves a list of all pinned links. All users can list pinned links. This endpoint does not support pagination as a tenant can have a maximum of 50 pinned links at one time.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Pinned links retrieval was successful.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `link` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "custom-link" |
| `scope` | string | Yes | Enum: "user", "tenant" |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes | Date string |
| `createdBy` | string | Yes |  |
| `updatedAt` | string | No | Date string |
| `updatedBy` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/ui-config/pinned-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links',
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
# qlik-cli has not implemented support for GET /api/v1/ui-config/pinned-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "link": "string",
      "name": "string",
      "type": "custom-link",
      "scope": "user",
      "tenantId": "string",
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "updatedBy": "string"
    }
  ]
}
```

---

### POST /api/v1/ui-config/pinned-links

Creates a pinned link, which will appear below any existing pinned links in the tenant. Requires calling user to be assigned the `TenantAdmin` role. A tenant can have a maximum of 50 pinned links.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link` | string | Yes | The URL the user will be taken to when they click on the custom link. Must be https. |
| `name` | string | Yes | The title of the link, which will be shown in the navigation bar. Max length 50 characters. |
| `type` | string | Yes | Specifies the type of the link. Only supports `custom-link`. Enum: "custom-link" |
| `scope` | string | Yes | Specifies the scope of the link. Only supports `tenant`. Enum: "tenant" |

#### Responses

##### 201

Successfully created pinned link

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `link` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "custom-link" |
| `scope` | string | Yes | Enum: "user", "tenant" |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes | Date string |
| `createdBy` | string | Yes |  |
| `updatedAt` | string | No | Date string |
| `updatedBy` | string | No |  |

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/ui-config/pinned-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      link: 'string',
      name: 'string',
      type: 'custom-link',
      scope: 'tenant',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ui-config/pinned-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"link":"string","name":"string","type":"custom-link","scope":"tenant"}'
```

**Example Response:**

```json
{
  "id": "string",
  "link": "string",
  "name": "string",
  "type": "custom-link",
  "scope": "user",
  "tenantId": "string",
  "createdAt": "string",
  "createdBy": "string",
  "updatedAt": "string",
  "updatedBy": "string"
}
```

---

### GET /api/v1/ui-config/pinned-links/{id}

Retrieves a specific pinned link.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The pinned link identifier. |

#### Responses

##### 200

Pinned link retrieval was successful.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `link` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "custom-link" |
| `scope` | string | Yes | Enum: "user", "tenant" |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes | Date string |
| `createdBy` | string | Yes |  |
| `updatedAt` | string | No | Date string |
| `updatedBy` | string | No |  |

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/ui-config/pinned-links/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/ui-config/pinned-links/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "link": "string",
  "name": "string",
  "type": "custom-link",
  "scope": "user",
  "tenantId": "string",
  "createdAt": "string",
  "createdBy": "string",
  "updatedAt": "string",
  "updatedBy": "string"
}
```

---

### PATCH /api/v1/ui-config/pinned-links/{id}

Updates a specific pinned link with an array of JSON patches. Requires calling user to be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The pinned link identifier. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "replace" |
| `path` | string | Yes | Enum: "/name", "/link" |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 200

Successfully updated pinned link

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `link` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "custom-link" |
| `scope` | string | Yes | Enum: "user", "tenant" |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes | Date string |
| `createdBy` | string | Yes |  |
| `updatedAt` | string | No | Date string |
| `updatedBy` | string | No |  |

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/ui-config/pinned-links/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'https://updatedlink.com',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/ui-config/pinned-links/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"https://updatedlink.com"}]'
```

**Example Response:**

```json
{
  "id": "string",
  "link": "string",
  "name": "string",
  "type": "custom-link",
  "scope": "user",
  "tenantId": "string",
  "createdAt": "string",
  "createdBy": "string",
  "updatedAt": "string",
  "updatedBy": "string"
}
```

---

### DELETE /api/v1/ui-config/pinned-links/{id}

Deletes a specific pinned link. Requires calling user to be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The pinned link identifier. |

#### Responses

##### 204

Successfully deleted pinned links

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 404

Pinned link not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/ui-config/pinned-links/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/ui-config/pinned-links/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links

Creates one or more pinned links for navigation, an alternative method to multiple calls to `/ui-config/pinned-links`. Links are displayed below any existing pinned links, and will be added in the order sent in the request. Requires calling user to be assigned the `TenantAdmin` role. A tenant can have a maximum of 50 pinned links.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Specifies the type of the link. Only supports `custom-link`. Enum: "custom-link" |
| `scope` | string | Yes | Specifies the scope of the link. Only supports `tenant`. Enum: "tenant" |
| `links` | object[] | Yes |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link` | string | Yes | The URL the user will be taken to when they click on the custom link. Must be https. |
| `name` | string | Yes | The title of the link, which will be shown in the navigation bar. Max length 50 characters. |

</details>

#### Responses

##### 200

Successfully created pinned links

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `link` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | string | Yes | Enum: "custom-link" |
| `scope` | string | Yes | Enum: "user", "tenant" |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes | Date string |
| `createdBy` | string | Yes |  |
| `updatedAt` | string | No | Date string |
| `updatedBy` | string | No |  |

</details>

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'custom-link',
      scope: 'tenant',
      links: [{ link: 'string', name: 'string' }],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"custom-link","scope":"tenant","links":[{"link":"string","name":"string"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "link": "string",
      "name": "string",
      "type": "custom-link",
      "scope": "user",
      "tenantId": "string",
      "createdAt": "string",
      "createdBy": "string",
      "updatedAt": "string",
      "updatedBy": "string"
    }
  ]
}
```

---

### POST /api/v1/ui-config/pinned-links/actions/delete-all-pinned-links

Deletes all pinned links in the tenant. Requires calling user to be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 204

Successfully deleted all pinned links

##### 403

Forbidden error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `message` | string | No | Error cause. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/ui-config/pinned-links/actions/delete-all-pinned-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/ui-config/pinned-links/actions/delete-all-pinned-links',
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
# qlik-cli has not implemented support for POST /api/v1/ui-config/pinned-links/actions/delete-all-pinned-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links/actions/delete-all-pinned-links" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---
