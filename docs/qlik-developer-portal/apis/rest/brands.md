# Brands

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Brands allow you to apply tenant level branding across most user interfaces.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/brands`](#get-apiv1brands) | Lists all brand entries for a tenant. |
| `POST` | [`/api/v1/brands`](#post-apiv1brands) | Creates a new brand. |
| `GET` | [`/api/v1/brands/{brand-id}`](#get-apiv1brandsbrand-id) | Returns a specific brand. |
| `PATCH` | [`/api/v1/brands/{brand-id}`](#patch-apiv1brandsbrand-id) | Patches a brand. |
| `DELETE` | [`/api/v1/brands/{brand-id}`](#delete-apiv1brandsbrand-id) | Deletes a specific brand. If the active brand is deleted, the tenant will return to the Qlik default. |
| `POST` | [`/api/v1/brands/{brand-id}/actions/activate`](#post-apiv1brandsbrand-idactionsactivate) | Sets the brand active and de-activates any other active brand. If the brand is already active, no action is taken. |
| `POST` | [`/api/v1/brands/{brand-id}/actions/deactivate`](#post-apiv1brandsbrand-idactionsdeactivate) | Sets the brand so it is no longer active, returning the tenant the Qlik default brand. If the brand is already inactive, no action is taken. |
| `GET` | [`/api/v1/brands/{brand-id}/files/{brand-file-id}`](#get-apiv1brandsbrand-idfilesbrand-file-id) | Downloads the specified brand file. |
| `POST` | [`/api/v1/brands/{brand-id}/files/{brand-file-id}`](#post-apiv1brandsbrand-idfilesbrand-file-id) | Creates a brand file for the specified identifier. |
| `PUT` | [`/api/v1/brands/{brand-id}/files/{brand-file-id}`](#put-apiv1brandsbrand-idfilesbrand-file-id) | Updates the specified brand file. |
| `DELETE` | [`/api/v1/brands/{brand-id}/files/{brand-file-id}`](#delete-apiv1brandsbrand-idfilesbrand-file-id) | Deletes the specified brand file. |
| `GET` | [`/api/v1/brands/active`](#get-apiv1brandsactive) | Returns the current active brand. If using the Qlik default brand, no value is returned. |

## API Reference

### GET /api/v1/brands

Lists all brand entries for a tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endingBefore` | string | No | Cursor to previous. |
| `limit` | integer | No | Maximum number of brands to retrieve. |
| `sort` | string | No | Field to sort by, prefixed with -/+ to indicate the order. Enum: "id", "+id", "-id", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt" |
| `startingAfter` | string | No | Cursor to the next page. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | A brand is a collection of assets for applying custom branding. Only a single brand can be active in a tenant. |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `files` | object[] | Yes | Collection of resources that make up the brand. |
| `active` | boolean | No |  |
| `createdAt` | string | No | The UTC timestamp when the brand was created. |
| `createdBy` | string | No | ID of a user that created the brand. |
| `updatedAt` | string | No | The UTC timestamp when the brand was last updated. |
| `updatedBy` | string | No | ID of a user that last updated the brand. |
| `description` | string | Yes |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

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
| `href` | string | Yes | URL of a resource request. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL of a resource request. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL of a resource request. |

</details>

</details>

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/brands` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/brands', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/brands yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "name": "string",
      "files": [
        {
          "id": "logo",
          "eTag": "string",
          "path": "string",
          "contentType": "string"
        }
      ],
      "active": true,
      "createdAt": "2024-01-01T00:00:00.000Z",
      "createdBy": "string",
      "updatedAt": "2024-01-01T00:00:00.000Z",
      "updatedBy": "string",
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

### POST /api/v1/brands

Creates a new brand.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `logo` | string | No | The path and name of a JPG or PNG file that will be adjusted to fit in a 'box' measuring 109px in width and 62 px in height while maintaining aspect ratio. Maximum size of 300 KB, but smaller is recommended. |
| `name` | string | Yes | Name of the brand. |
| `styles` | string | No | The path and name of a JSON file to define brand style settings. Maximum size is 100 KB. This property is not currently operational. |
| `favIcon` | string | No | The path and name of a properly formatted ICO file. Maximum size is 100 KB. |
| `description` | string | No | Description of the brand. |

#### Responses

##### 201

Created Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `files` | object[] | Yes | Collection of resources that make up the brand. |
| `active` | boolean | No |  |
| `createdAt` | string | No | The UTC timestamp when the brand was created. |
| `createdBy` | string | No | ID of a user that created the brand. |
| `updatedAt` | string | No | The UTC timestamp when the brand was last updated. |
| `updatedBy` | string | No | ID of a user that last updated the brand. |
| `description` | string | Yes |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

</details>

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/brands` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/brands', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/brands yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "logo=@/path/to/file" \
-F "name=\"string\"" \
-F "styles=@/path/to/file" \
-F "favIcon=@/path/to/file" \
-F "description=\"string\""
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "files": [
    {
      "id": "logo",
      "eTag": "string",
      "path": "string",
      "contentType": "string"
    }
  ],
  "active": true,
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "description": "string"
}
```

---

### GET /api/v1/brands/{brand-id}

Returns a specific brand.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `files` | object[] | Yes | Collection of resources that make up the brand. |
| `active` | boolean | No |  |
| `createdAt` | string | No | The UTC timestamp when the brand was created. |
| `createdBy` | string | No | ID of a user that created the brand. |
| `updatedAt` | string | No | The UTC timestamp when the brand was last updated. |
| `updatedBy` | string | No | ID of a user that last updated the brand. |
| `description` | string | Yes |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

</details>

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/brands/{brand-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}',
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
# qlik-cli has not implemented support for GET /api/v1/brands/{brand-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "files": [
    {
      "id": "logo",
      "eTag": "string",
      "path": "string",
      "contentType": "string"
    }
  ],
  "active": true,
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "description": "string"
}
```

---

### PATCH /api/v1/brands/{brand-id}

Patches a brand.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "add", "remove", "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/name", "/description" |
| `value` | string | No | The value to be used for this operation. |

#### Responses

##### 204

No Content Response.

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/brands/{brand-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: '/description',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/brands/{brand-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/description","value":"string"}]'
```

---

### DELETE /api/v1/brands/{brand-id}

Deletes a specific brand. If the active brand is deleted, the tenant will return to the Qlik default.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |

#### Responses

##### 204

No Content Response.

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/brands/{brand-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/brands/{brand-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/brands/{brand-id}/actions/activate

Sets the brand active and de-activates any other active brand. If the brand is already active, no action is taken.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |

#### Request Body

#### Responses

##### 200

Responds with the brand that was activated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `files` | object[] | Yes | Collection of resources that make up the brand. |
| `active` | boolean | No |  |
| `createdAt` | string | No | The UTC timestamp when the brand was created. |
| `createdBy` | string | No | ID of a user that created the brand. |
| `updatedAt` | string | No | The UTC timestamp when the brand was last updated. |
| `updatedBy` | string | No | ID of a user that last updated the brand. |
| `description` | string | Yes |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

</details>

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/brands/{brand-id}/actions/activate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/actions/activate',
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
# qlik-cli has not implemented support for POST /api/v1/brands/{brand-id}/actions/activate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/actions/activate" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "files": [
    {
      "id": "logo",
      "eTag": "string",
      "path": "string",
      "contentType": "string"
    }
  ],
  "active": true,
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "description": "string"
}
```

---

### POST /api/v1/brands/{brand-id}/actions/deactivate

Sets the brand so it is no longer active, returning the tenant the Qlik default brand. If the brand is already inactive, no action is taken.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |

#### Request Body

#### Responses

##### 200

Responds with the brand that was deactivated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `files` | object[] | Yes | Collection of resources that make up the brand. |
| `active` | boolean | No |  |
| `createdAt` | string | No | The UTC timestamp when the brand was created. |
| `createdBy` | string | No | ID of a user that created the brand. |
| `updatedAt` | string | No | The UTC timestamp when the brand was last updated. |
| `updatedBy` | string | No | ID of a user that last updated the brand. |
| `description` | string | Yes |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

</details>

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/brands/{brand-id}/actions/deactivate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/actions/deactivate',
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
# qlik-cli has not implemented support for POST /api/v1/brands/{brand-id}/actions/deactivate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/actions/deactivate" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "files": [
    {
      "id": "logo",
      "eTag": "string",
      "path": "string",
      "contentType": "string"
    }
  ],
  "active": true,
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "description": "string"
}
```

---

### GET /api/v1/brands/{brand-id}/files/{brand-file-id}

Downloads the specified brand file.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |
| `brand-file-id` | string | Yes | The unique identifier of a file within a brand. Enum: "logo", "favIcon", "styles" |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | Media type accepted for the downloaded brand file. |

#### Responses

##### 200

OK Response

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `*/*` | string | No |  |

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/brands/{brand-id}/files/{brand-file-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/files/{brand-file-id}',
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
# qlik-cli has not implemented support for GET /api/v1/brands/{brand-id}/files/{brand-file-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/files/{brand-file-id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
"string"
```

---

### POST /api/v1/brands/{brand-id}/files/{brand-file-id}

Creates a brand file for the specified identifier.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |
| `brand-file-id` | string | Yes | The unique identifier of a file within a brand. Enum: "logo", "favIcon", "styles" |

#### Request Body

**Required**

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | string | No | The path and name of a file to upload. |

#### Responses

##### 201

Created Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/brands/{brand-id}/files/{brand-file-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/files/{brand-file-id}',
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
# qlik-cli has not implemented support for POST /api/v1/brands/{brand-id}/files/{brand-file-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/files/{brand-file-id}" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "file=@/path/to/file"
```

**Example Response:**

```json
{
  "id": "logo",
  "eTag": "string",
  "path": "string",
  "contentType": "string"
}
```

---

### PUT /api/v1/brands/{brand-id}/files/{brand-file-id}

Updates the specified brand file.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |
| `brand-file-id` | string | Yes | The unique identifier of a file within a brand. Enum: "logo", "favIcon", "styles" |

#### Request Body

**Required**

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | string | No | A file to upload. |

#### Responses

##### 200

OK Response - file updated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Enum: "logo", "favIcon", "styles" |
| `eTag` | string | No |  |
| `path` | string | No |  |
| `contentType` | string | No |  |

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/brands/{brand-id}/files/{brand-file-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/files/{brand-file-id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/brands/{brand-id}/files/{brand-file-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/files/{brand-file-id}" \
-X PUT \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "file=@/path/to/file"
```

**Example Response:**

```json
{
  "id": "logo",
  "eTag": "string",
  "path": "string",
  "contentType": "string"
}
```

---

### DELETE /api/v1/brands/{brand-id}/files/{brand-file-id}

Deletes the specified brand file.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brand-id` | string | Yes | The brand's unique identifier. |
| `brand-file-id` | string | Yes | The unique identifier of a file within a brand. Enum: "logo", "favIcon", "styles" |

#### Responses

##### 204

No content response.

##### 400

Bad Request

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

##### 401

Unauthorized

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

##### 403

Forbidden

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

Not found

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

##### 500

Internal Server Error

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

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/brands/{brand-id}/files/{brand-file-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/{brand-id}/files/{brand-file-id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/brands/{brand-id}/files/{brand-file-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/{brand-id}/files/{brand-file-id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/brands/active

Returns the current active brand. If using the Qlik default brand, no value is returned.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

No active brand, returns an empty response.

**Content-Type:** `application/json`


##### 301

Successful redirect.

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/brands/active` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/brands/active',
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
# qlik-cli has not implemented support for GET /api/v1/brands/active yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/brands/active" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{}
```

---
