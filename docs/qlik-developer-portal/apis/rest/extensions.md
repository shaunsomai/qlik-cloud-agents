# Extensions

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Visualization extensions is a capability in Qlik Sense which allows third-party visualizations and other presentation objects to be used in the Qlik Sense client.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/extensions`](#get-apiv1extensions) | Lists all imported extensions in the tenant. |
| `POST` | [`/api/v1/extensions`](#post-apiv1extensions) | Creates a new extension. Accepts either provided file or data object. The name of the new extension must be different to any existing extensions. |
| `GET` | [`/api/v1/extensions/{id}`](#get-apiv1extensionsid) | Returns a specific extension matching either extension ID or extension name. |
| `PATCH` | [`/api/v1/extensions/{id}`](#patch-apiv1extensionsid) | Updates a specific extension matching either extension ID or extension name. Accepts either provided file or data object. |
| `DELETE` | [`/api/v1/extensions/{id}`](#delete-apiv1extensionsid) | Deletes a specific extension matching either extension ID or extension name. |
| `GET` | [`/api/v1/extensions/{id}/file`](#get-apiv1extensionsidfile) | Downloads all files in the extension matching either extension ID or extension name as a `.zip` archive. |
| `GET` | [`/api/v1/extensions/{id}/file/{filepath}`](#get-apiv1extensionsidfilefilepath) | Downloads a specific file from the extension matching either extension ID or extension name, identified by the file path within the imported extension. |

## API Reference

### GET /api/v1/extensions

Lists all imported extensions in the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

OK. Lists all extensions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | The extension model. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `userId` | string | No |  |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `tenantId` | string | No |  |
| `updateAt` | string | No |  |
| `createdAt` | string | No |  |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |
| `migrationState` | string | No | The migration state of the extension. It can be either "READY_TO_MOVE", "IN_PROGRESS" or "COMPLETED". |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/extensions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions',
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
# qlik-cli has not implemented support for GET /api/v1/extensions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "file": {},
      "icon": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "type": "string",
      "author": "string",
      "bundle": {
        "id": "string",
        "name": "string",
        "description": "string"
      },
      "userId": "string",
      "bundled": true,
      "license": "string",
      "preview": "string",
      "version": "string",
      "checksum": "string",
      "homepage": "string",
      "keywords": "string",
      "loadpath": "string",
      "supplier": "string",
      "tenantId": "string",
      "updateAt": "string",
      "createdAt": "string",
      "supernova": true,
      "deprecated": "string",
      "repository": "string",
      "description": "string",
      "qextVersion": "string",
      "dependencies": {},
      "qextFilename": "string",
      "migrationState": "string"
    }
  ]
}
```

---

### POST /api/v1/extensions

Creates a new extension. Accepts either provided file or data object. The name of the new extension must be different to any existing extensions.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | The extension model. |
| `file` | string | No | Extension archive. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

</details>

#### Responses

##### 201

Created. Creates a new extension and returns it.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `userId` | string | No |  |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `tenantId` | string | No |  |
| `updateAt` | string | No |  |
| `createdAt` | string | No |  |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |
| `migrationState` | string | No | The migration state of the extension. It can be either "READY_TO_MOVE", "IN_PROGRESS" or "COMPLETED". |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

##### 409

Conflict. Resource with same unique identity already exists.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 415

Unsupported media type. Body of the payload is not a valid JSON object.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 422

Unprocessable entity. Validation error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/extensions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions',
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
# qlik-cli has not implemented support for POST /api/v1/extensions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "data={\"id\":\"string\",\"file\":{},\"icon\":\"string\",\"name\":\"string\",\"tags\":[\"string\"],\"type\":\"string\",\"author\":\"string\",\"bundle\":{\"id\":\"string\",\"name\":\"string\",\"description\":\"string\"},\"userId\":\"string\",\"bundled\":true,\"license\":\"string\",\"preview\":\"string\",\"version\":\"string\",\"checksum\":\"string\",\"homepage\":\"string\",\"keywords\":\"string\",\"loadpath\":\"string\",\"supplier\":\"string\",\"tenantId\":\"string\",\"updateAt\":\"string\",\"createdAt\":\"string\",\"supernova\":true,\"deprecated\":\"string\",\"repository\":\"string\",\"description\":\"string\",\"qextVersion\":\"string\",\"dependencies\":{},\"qextFilename\":\"string\",\"migrationState\":\"string\"}" \
-F "file=@/path/to/file"
```

**Example Response:**

```json
{
  "id": "string",
  "file": {},
  "icon": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "author": "string",
  "bundle": {
    "id": "string",
    "name": "string",
    "description": "string"
  },
  "userId": "string",
  "bundled": true,
  "license": "string",
  "preview": "string",
  "version": "string",
  "checksum": "string",
  "homepage": "string",
  "keywords": "string",
  "loadpath": "string",
  "supplier": "string",
  "tenantId": "string",
  "updateAt": "string",
  "createdAt": "string",
  "supernova": true,
  "deprecated": "string",
  "repository": "string",
  "description": "string",
  "qextVersion": "string",
  "dependencies": {},
  "qextFilename": "string",
  "migrationState": "string"
}
```

---

### GET /api/v1/extensions/{id}

Returns a specific extension matching either extension ID or extension name.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Extension identifier or its qextFilename. |

#### Responses

##### 200

OK. Returns extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `userId` | string | No |  |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `tenantId` | string | No |  |
| `updateAt` | string | No |  |
| `createdAt` | string | No |  |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |
| `migrationState` | string | No | The migration state of the extension. It can be either "READY_TO_MOVE", "IN_PROGRESS" or "COMPLETED". |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

##### 403

Forbidden. User is not authorized to read extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 404

Not found. Could not find the extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 410

Gone. Extension with {id} has been deleted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/extensions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/extensions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "file": {},
  "icon": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "author": "string",
  "bundle": {
    "id": "string",
    "name": "string",
    "description": "string"
  },
  "userId": "string",
  "bundled": true,
  "license": "string",
  "preview": "string",
  "version": "string",
  "checksum": "string",
  "homepage": "string",
  "keywords": "string",
  "loadpath": "string",
  "supplier": "string",
  "tenantId": "string",
  "updateAt": "string",
  "createdAt": "string",
  "supernova": true,
  "deprecated": "string",
  "repository": "string",
  "description": "string",
  "qextVersion": "string",
  "dependencies": {},
  "qextFilename": "string",
  "migrationState": "string"
}
```

---

### PATCH /api/v1/extensions/{id}

Updates a specific extension matching either extension ID or extension name. Accepts either provided file or data object.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Extension identifier or its qextFilename. |

#### Request Body

**Required**

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object | No | The extension model. |
| `file` | string | No | Extension archive. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

</details>

#### Responses

##### 200

OK. Extension has been updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `file` | object | No | The file that was uploaded with the extension. |
| `icon` | string | No | Icon to show in the client. |
| `name` | string | No | The display name of this extension. |
| `tags` | string[] | No | List of tags. |
| `type` | string | No | The type of this extension (visualization, etc.). |
| `author` | string | No | Author of the extension. |
| `bundle` | object | No | Object containing meta data regarding the bundle the extension belongs to. If it does not belong to a bundle, this object is not defined. |
| `userId` | string | No |  |
| `bundled` | boolean | No | If the extension is part of an extension bundle. |
| `license` | string | No | Under which license this extension is published. |
| `preview` | string | No | Path to an image that enables users to preview the extension. |
| `version` | string | No | Version of the extension. |
| `checksum` | string | No | Checksum of the extension contents. |
| `homepage` | string | No | Home page of the extension. |
| `keywords` | string | No | Keywords for the extension. |
| `loadpath` | string | No | Relative path to the extension's entry file, defaults to `filename` from the qext file. |
| `supplier` | string | No | Supplier of the extension. |
| `tenantId` | string | No |  |
| `updateAt` | string | No |  |
| `createdAt` | string | No |  |
| `supernova` | boolean | No | If the extension is a supernova extension or not. |
| `deprecated` | string | No | A date noting when the extension was deprecated. |
| `repository` | string | No | Link to the extension source code. |
| `description` | string | No | Description of the extension. |
| `qextVersion` | string | No | The version from the qext file that was uploaded with this extension. |
| `dependencies` | object | No | Map of dependencies describing version of the component it requires. |
| `qextFilename` | string | No | The name of the qext file that was uploaded with this extension. |
| `migrationState` | string | No | The migration state of the extension. It can be either "READY_TO_MOVE", "IN_PROGRESS" or "COMPLETED". |

<details>
<summary>Properties of `bundle`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique identifier of the bundle. |
| `name` | string | No | Name of the bundle. |
| `description` | string | No | Description of the bundle. |

</details>

##### 403

Forbidden. User is not authorized to update extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 404

Not found. Could not find the extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 409

Conflict. Resource with same unique identity already exists.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 415

Unsupported media type. Body of the payload is not a valid JSON object.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 422

Unprocessable entity. Validation error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/extensions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/extensions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions/{id}" \
-X PATCH \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "data={\"id\":\"string\",\"file\":{},\"icon\":\"string\",\"name\":\"string\",\"tags\":[\"string\"],\"type\":\"string\",\"author\":\"string\",\"bundle\":{\"id\":\"string\",\"name\":\"string\",\"description\":\"string\"},\"userId\":\"string\",\"bundled\":true,\"license\":\"string\",\"preview\":\"string\",\"version\":\"string\",\"checksum\":\"string\",\"homepage\":\"string\",\"keywords\":\"string\",\"loadpath\":\"string\",\"supplier\":\"string\",\"tenantId\":\"string\",\"updateAt\":\"string\",\"createdAt\":\"string\",\"supernova\":true,\"deprecated\":\"string\",\"repository\":\"string\",\"description\":\"string\",\"qextVersion\":\"string\",\"dependencies\":{},\"qextFilename\":\"string\",\"migrationState\":\"string\"}" \
-F "file=@/path/to/file"
```

**Example Response:**

```json
{
  "id": "string",
  "file": {},
  "icon": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "string",
  "author": "string",
  "bundle": {
    "id": "string",
    "name": "string",
    "description": "string"
  },
  "userId": "string",
  "bundled": true,
  "license": "string",
  "preview": "string",
  "version": "string",
  "checksum": "string",
  "homepage": "string",
  "keywords": "string",
  "loadpath": "string",
  "supplier": "string",
  "tenantId": "string",
  "updateAt": "string",
  "createdAt": "string",
  "supernova": true,
  "deprecated": "string",
  "repository": "string",
  "description": "string",
  "qextVersion": "string",
  "dependencies": {},
  "qextFilename": "string",
  "migrationState": "string"
}
```

---

### DELETE /api/v1/extensions/{id}

Deletes a specific extension matching either extension ID or extension name.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Extension identifier or its qextFilename. |

#### Responses

##### 204

No content. Soft deletes the extension.

##### 403

Forbidden. User is not authorized to delete extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 404

Not found. Could not find the extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 410

Gone. Extension with {id} has been deleted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/extensions/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/extensions/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/extensions/{id}/file

Downloads all files in the extension matching either extension ID or extension name as a `.zip` archive.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Extension identifier or its qextFilename. |

#### Responses

##### 200

OK. Extension exists. Returns the extension archive.

**Content-Type:** `application/zip`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/zip` | string | No |  |

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

##### 403

Forbidden. User is not authorized to read extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 404

Not found. Could not find the extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 410

Gone. Extension with {id} has been deleted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/extensions/{id}/file` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions/{id}/file',
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
# qlik-cli has not implemented support for GET /api/v1/extensions/{id}/file yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions/{id}/file" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
"string"
```

---

### GET /api/v1/extensions/{id}/file/{filepath}

Downloads a specific file from the extension matching either extension ID or extension name, identified by the file path within the imported extension.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filepath` | string | Yes | Path to the file location within the specified extension archive. Folders separated with forward slashes. |
| `id` | string | Yes | Extension identifier or its qextFilename. |

#### Responses

##### 200

OK. Extension exists and the file specified exists. Returns the specific file.

##### 403

Forbidden. User is not authorized to read extension with {id}.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 404

Not found. Could not find the extension with {id} or the file does not exist in the archive.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

##### 410

Gone. Extension with {id} has been deleted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Object containing meta data regarding an error. It does not necessarily contain all the properties. |
| `title` | string | Yes | Title of the HTTP status code. |
| `source` | object | No | Optional JSON patch object pointing to an invalid property. |
| `status` | number | No | The HTTP status code. |
| `traceId` | string | No | The active traceId. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stack` | string | No | Full stack trace of the error that was raised. |
| `message` | string | No | A more detailed message explaining the error. |
| `resourceName` | string | No | Name of the resource related to the error. If there is a conflict, it is the name of the model attempting to be created. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/extensions/{id}/file/{filepath}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/extensions/{id}/file/{filepath}',
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
# qlik-cli has not implemented support for GET /api/v1/extensions/{id}/file/{filepath} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/extensions/{id}/file/{filepath}" \
-H "Authorization: Bearer <access_token>"
```

---
