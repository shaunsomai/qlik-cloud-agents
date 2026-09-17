# Report templates

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Create and manage report templates for consistent report generation and distribution.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/report-templates`](#get-apiv1report-templates) |  |
| `POST` | [`/api/v1/report-templates`](#post-apiv1report-templates) |  |
| `GET` | [`/api/v1/report-templates/{id}`](#get-apiv1report-templatesid) |  |
| `PATCH` | [`/api/v1/report-templates/{id}`](#patch-apiv1report-templatesid) |  |
| `PUT` | [`/api/v1/report-templates/{id}`](#put-apiv1report-templatesid) |  |
| `DELETE` | [`/api/v1/report-templates/{id}`](#delete-apiv1report-templatesid) |  |
| `POST` | [`/api/v1/report-templates/{id}/actions/download`](#post-apiv1report-templatesidactionsdownload) |  |

## API Reference

### GET /api/v1/report-templates

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | If present, restrict the number of returned items to this value. |
| `name` | string | No | Template name to search and filter for. Case-insensitive open search with wildcards both as prefix and suffix. |
| `ownerId` | string | No | Return the templates for the specified owner. |
| `skip` | integer | No | If present, skip this number of the returned values in the result set (facilitates paging). |
| `sort` | string[] | No | Field to sort by. Prefix with +/- to indicate ascending/descending. By default, the sort order is ascending. Enum: "name", "+name", "-name", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt", "type", "+type", "-type" |
| `sourceAppId` | string | No | Return the templates that are using the specified app as data source. |

#### Responses

##### 200

The templates list was retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | The current page data. |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The template ID |
| `name` | string | No | Template name |
| `type` | string | No | Template type Enum: "excel", "pixelPerfect", "html", "powerPoint", "word" |
| `ownerId` | string | No | The user that this template is scoped to. |
| `createdAt` | string | No | The date and time when the template was created. |
| `createdBy` | string | No | The id of the user who created the template. |
| `updatedAt` | string | No | The date and time when the template was last updated. |
| `updatedBy` | string | No | The id of the user who last updated the template. |
| `description` | string | No | Template description |
| `sourceAppId` | string | No | The id of the app that this template is using as data source. |
| `sourceAppName` | string | No | The name of the app that this template is using as data source. |
| `metadataVersion` | integer | No | The template metadata version |

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
| `href` | string | No | The URL for the pagination link. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the pagination link. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the pagination link. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/report-templates` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates',
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
# qlik-cli has not implemented support for GET /api/v1/report-templates yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "name": "Sales by category",
      "type": "excel",
      "ownerId": "0rTsxGg_rtsZAs19Zib_421n6haydjIh",
      "createdAt": "2026-01-01T12:00:00.000Z",
      "createdBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
      "updatedAt": "2026-01-01T12:00:00.000Z",
      "updatedBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
      "description": "Sales grouped by product category",
      "sourceAppId": "c4c70012-29c7-47c2-820d-4ff74cb164a9",
      "sourceAppName": "Qlik app",
      "metadataVersion": 1
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

### POST /api/v1/report-templates

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

The upload request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Template name |
| `description` | string | No | Template description |
| `sourceAppId` | string | No | The ID of the app that this template is using as data source. The id stored in the template file metadata is used if no value is specified. |
| `sourceAppAction` | string | No | Specifies the action to perform with the given source app id. Use "validate" to verify that the template source app matches the provided value. Use "replace" to migrate the template to a different app by replacing the source app id. Enum: "validate", "replace" |
| `temporaryContentId` | string | Yes | The ID of a previously uploaded temporary content file |

#### Responses

##### 201

New template was created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The template ID |
| `name` | string | No | Template name |
| `type` | string | No | Template type Enum: "excel", "pixelPerfect", "html", "powerPoint", "word" |
| `ownerId` | string | No | The user that this template is scoped to. |
| `createdAt` | string | No | The date and time when the template was created. |
| `createdBy` | string | No | The id of the user who created the template. |
| `updatedAt` | string | No | The date and time when the template was last updated. |
| `updatedBy` | string | No | The id of the user who last updated the template. |
| `description` | string | No | Template description |
| `sourceAppId` | string | No | The id of the app that this template is using as data source. |
| `sourceAppName` | string | No | The name of the app that this template is using as data source. |
| `metadataVersion` | integer | No | The template metadata version |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 413

The template file exceeds the user's quota for maximum file to upload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/report-templates` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Sales by category',
      description:
        'Sales grouped by product category',
      sourceAppId:
        '78fb8e8d-bc83-4da1-b0d1-b0dc0a5c3e5b',
      sourceAppAction: 'validate',
      temporaryContentId:
        '69b14f2bb93332c3ff8c64b8',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/report-templates yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Sales by category","description":"Sales grouped by product category","sourceAppId":"78fb8e8d-bc83-4da1-b0d1-b0dc0a5c3e5b","sourceAppAction":"validate","temporaryContentId":"69b14f2bb93332c3ff8c64b8"}'
```

**Example Response:**

```json
{
  "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
  "name": "Sales by category",
  "type": "excel",
  "ownerId": "0rTsxGg_rtsZAs19Zib_421n6haydjIh",
  "createdAt": "2026-01-01T12:00:00.000Z",
  "createdBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "updatedAt": "2026-01-01T12:00:00.000Z",
  "updatedBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "description": "Sales grouped by product category",
  "sourceAppId": "c4c70012-29c7-47c2-820d-4ff74cb164a9",
  "sourceAppName": "Qlik app",
  "metadataVersion": 1
}
```

---

### GET /api/v1/report-templates/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the report template. |

#### Responses

##### 200

The template was located.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The template ID |
| `name` | string | No | Template name |
| `type` | string | No | Template type Enum: "excel", "pixelPerfect", "html", "powerPoint", "word" |
| `ownerId` | string | No | The user that this template is scoped to. |
| `createdAt` | string | No | The date and time when the template was created. |
| `createdBy` | string | No | The id of the user who created the template. |
| `updatedAt` | string | No | The date and time when the template was last updated. |
| `updatedBy` | string | No | The id of the user who last updated the template. |
| `description` | string | No | Template description |
| `sourceAppId` | string | No | The id of the app that this template is using as data source. |
| `sourceAppName` | string | No | The name of the app that this template is using as data source. |
| `metadataVersion` | integer | No | The template metadata version |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A template with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/report-templates/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/report-templates/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
  "name": "Sales by category",
  "type": "excel",
  "ownerId": "0rTsxGg_rtsZAs19Zib_421n6haydjIh",
  "createdAt": "2026-01-01T12:00:00.000Z",
  "createdBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "updatedAt": "2026-01-01T12:00:00.000Z",
  "updatedBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "description": "Sales grouped by product category",
  "sourceAppId": "c4c70012-29c7-47c2-820d-4ff74cb164a9",
  "sourceAppName": "Qlik app",
  "metadataVersion": 1
}
```

---

### PATCH /api/v1/report-templates/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the report template to patch. |

#### Request Body

A JSON patch request as defined by RFC 6902.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | No |  |
| `from` | string | No |  |
| `path` | string | No |  |
| `value` | object | No |  |

**Content-Type:** `application/json-patch+json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | No |  |
| `from` | string | No |  |
| `path` | string | No |  |
| `value` | object | No |  |

#### Responses

##### 204

Patch successfully applied to template.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A template with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 413

The template file exceeds the user's quota for maximum file to upload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/report-templates/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'string',
        from: 'string',
        path: 'string',
        value: {},
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/report-templates/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"string","from":"string","path":"string","value":{}}]'
```

---

### PUT /api/v1/report-templates/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the report template to update. |

#### Request Body

The upload request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Template name |
| `description` | string | No | Template description |
| `sourceAppAction` | string | No | Specifies the action to perform with the new source app. Use "validate" to verify that the source app of the uploaded template matches the target app. Use "replace" to migrate the uploaded template to the target app by replacing the source app id. Enum: "validate", "replace" |
| `temporaryContentId` | string | Yes | The ID of a previously uploaded temporary content file |

#### Responses

##### 201

The template was updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The template ID |
| `name` | string | No | Template name |
| `type` | string | No | Template type Enum: "excel", "pixelPerfect", "html", "powerPoint", "word" |
| `ownerId` | string | No | The user that this template is scoped to. |
| `createdAt` | string | No | The date and time when the template was created. |
| `createdBy` | string | No | The id of the user who created the template. |
| `updatedAt` | string | No | The date and time when the template was last updated. |
| `updatedBy` | string | No | The id of the user who last updated the template. |
| `description` | string | No | Template description |
| `sourceAppId` | string | No | The id of the app that this template is using as data source. |
| `sourceAppName` | string | No | The name of the app that this template is using as data source. |
| `metadataVersion` | integer | No | The template metadata version |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A template with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 413

The template file exceeds the user's quota for maximum file to upload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/report-templates/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Sales by category',
      description:
        'Sales grouped by product category',
      sourceAppAction: 'validate',
      temporaryContentId:
        '69b14f2bb93332c3ff8c64b8',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/report-templates/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Sales by category","description":"Sales grouped by product category","sourceAppAction":"validate","temporaryContentId":"69b14f2bb93332c3ff8c64b8"}'
```

**Example Response:**

```json
{
  "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
  "name": "Sales by category",
  "type": "excel",
  "ownerId": "0rTsxGg_rtsZAs19Zib_421n6haydjIh",
  "createdAt": "2026-01-01T12:00:00.000Z",
  "createdBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "updatedAt": "2026-01-01T12:00:00.000Z",
  "updatedBy": "0rTsxGg_rtsZAs19Zib_421n6htydjIh",
  "description": "Sales grouped by product category",
  "sourceAppId": "c4c70012-29c7-47c2-820d-4ff74cb164a9",
  "sourceAppName": "Qlik app",
  "metadataVersion": 1
}
```

---

### DELETE /api/v1/report-templates/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the report template to delete. |

#### Responses

##### 204

The template was deleted.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/report-templates/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/report-templates/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/report-templates/{id}/actions/download

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the report template. |

#### Responses

##### 200

The template file.

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | List of errors and their properties. |
| `statusCode` | integer | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `meta` | object | No | Additional error metadata. |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/report-templates/{id}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/report-templates/{id}/actions/download',
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
# qlik-cli has not implemented support for POST /api/v1/report-templates/{id}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates/{id}/actions/download" \
-X POST \
-H "Authorization: Bearer <access_token>" \
-o "output-file"
```

---
