# Temporary contents

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Services such as app and data-files which may import or export larger files can opt to leverage the temporary contents service to handle these requests. Acts as a temporary file store.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/temp-contents`](#post-apiv1temp-contents) | Upload a file as a temporary content resource. It returns a `201 Created` with a location header that contains the location of the created resource. If filename or TTL is not properly set, a `400 Bad request` is returned. For internal issues, a `500 Internal Server Error` is returned. |
| `GET` | [`/api/v1/temp-contents/{id}`](#get-apiv1temp-contentsid) | This endpoint is used to retrieve a temporary content file. It returns a valid (`200 OK`) in case the file exists and the user is authorized to view the contents. It returns a `410 Gone` if the file has expired and `404 Not Found` if the criteria is not met. |
| `GET` | [`/api/v1/temp-contents/{id}/details`](#get-apiv1temp-contentsiddetails) | Retrieve a summary of the metadata associated with a temporary content resource. It returns a `200 OK` with a model if the temporary resource is valid. It returns a `410 Gone` if the file has expired and `404 Not Found` if the criteria is not met. |
| `POST` | [`/api/v1/temp-contents/files`](#post-apiv1temp-contentsfiles) | Create a new upload resource (tus protocol `creation` extension POST request). See [tus.io](http://tus.io) for details. |
| `PATCH` | [`/api/v1/temp-contents/files/{id}`](#patch-apiv1temp-contentsfilesid) | Apply bytes contained in the message at a given offset (tus protocol PATCH request). Note that the tus server only |

## API Reference

### POST /api/v1/temp-contents

Upload a file as a temporary content resource. It returns a `201 Created` with a location header that contains the location of the created resource. If filename or TTL is not properly set, a `400 Bad request` is returned. For internal issues, a `500 Internal Server Error` is returned.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filename` | string | No | The name of the file to upload. |
| `ttl` | integer | No | The TTL parameter is used to define the time-to-live for the content resource in seconds. It defaults to one hour (3600) if no input is provided. Max TTL is 259200 (3 days).' |

#### Request Body

**Required**

The file content (binary) to upload.

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

#### Responses

##### 201

Created

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/temp-contents` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/temp-contents',
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
# qlik-cli has not implemented support for POST /api/v1/temp-contents yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents" \
-X POST \
-H "Content-type: application/octet-stream" \
-H "Authorization: Bearer <access_token>" \
--data-binary' \
          '"@/path/to/file"
```

---

### GET /api/v1/temp-contents/{id}

This endpoint is used to retrieve a temporary content file. It returns a valid (`200 OK`) in case the file exists and the user is authorized to view the contents. It returns a `410 Gone` if the file has expired and `404 Not Found` if the criteria is not met.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The temporary contents ID. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `inline` | string | No | Set to "1" to download the file in inline mode. Useful for displaying a preview of the file in a browser. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Range` | string | No | Set to `unit=start-end` (for example, `bytes=0-100`) where `unit` = `bytes` (only supported unit), and start/end is a positive integer, where start <= end. Will also handle `start-` and `-end` as described in https://tools.ietf.org/html/rfc7233. |

#### Responses

##### 200

Success

**Content-Type:** `*/*`


##### 204

No Content, resource is incomplete.

##### 206

Success

**Content-Type:** `*/*`


##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 410

Gone

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 416

Range Not Satisfiable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/temp-contents/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/temp-contents/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/temp-contents/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{}
```

---

### GET /api/v1/temp-contents/{id}/details

Retrieve a summary of the metadata associated with a temporary content resource. It returns a `200 OK` with a model if the temporary resource is valid. It returns a `410 Gone` if the file has expired and `404 Not Found` if the criteria is not met.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The temporary contents ID. |

#### Responses

##### 200

Success

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ID` | string | No | Identifier |
| `Name` | string | No | File name of the file uploaded by the user. |
| `Size` | string | No | Size of resource (in bytes). |
| `Expires` | string | No | Datetime-stamp when the resource expired (in UTC). |
| `CreatedAt` | string | No | Datetime-stamp when the resource was created (in UTC). |
| `CreatorID` | string | No | Identifier for the subject / resource creator. |
| `UpdatedAt` | string | No | Datetime-stamp when the resource was updated (in UTC). |
| `TTLSeconds` | integer | No | Time-to-live in seconds. |

##### 204

No Content, resource is incomplete.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 410

Gone

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/temp-contents/{id}/details` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/temp-contents/{id}/details',
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
# qlik-cli has not implemented support for GET /api/v1/temp-contents/{id}/details yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents/{id}/details" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "ID": "string",
  "Name": "string",
  "Size": "string",
  "Expires": "string",
  "CreatedAt": "string",
  "CreatorID": "string",
  "UpdatedAt": "string",
  "TTLSeconds": 42
}
```

---

### POST /api/v1/temp-contents/files

Create a new upload resource (tus protocol `creation` extension POST request). See [tus.io](http://tus.io) for details.

- **Rate Limit:** Special (800 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Tus-Resumable` | string | Yes | The version of the tus protocol used. |
| `Upload-Length` | integer | Yes | The size of the entire upload in bytes. |
| `Upload-Metadata` | string | No | One or more comma-separated key-value pairs. The key and value must be separated by a space. The key should be ASCII encoded, and the value must be Base64 encoded. All keys must be unique. See [tus.io](http://tus.io) for details.  The following keys are used; any other keys are ignored. - `filename` - the name of the file. - `ttl` - the time-to-live for the uploaded file in seconds. Note that the time is counted from the _start_ of   the upload creation, not when the upload has finished. The server will keep the file available for access for   this period of time. The server may then delete it. The time defaults to one hour (3600) if not provided.   The maximum value is 259200 (3 days).' |

#### Responses

##### 201

Created

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 412

Precondition Failed. tus protocol version not supported by the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 413

Request Entity Too Large

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/temp-contents/files` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/temp-contents/files',
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
# qlik-cli has not implemented support for POST /api/v1/temp-contents/files yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents/files" \
-X POST \
-H "Tus-Resumable: string" \
-H "Upload-Length: 0" \
-H "Authorization: Bearer <access_token>"
```

---

### PATCH /api/v1/temp-contents/files/{id}

Apply bytes contained in the message at a given offset (tus protocol PATCH request). Note that the tus server only
accepts that the Content-Type response header is set to `application/offset+octet-stream`.
See [tus.io](http://tus.io) for details.

Note that the server may return `423 Locked` on this request. This happens if the client attempts to perform
concurrent access to the resource, for example, if attempting to do a `HEAD` request during an ongoing `PATCH` request.
It can also occur in situations where the connection is unexpectedly dropped between the client and the server
and the client attempts to make a new request when the server is still busy processing the upload. When this
happens, the client shall, after some period of time, try to resume the upload again.


- **Rate Limit:** Special (800 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID used to uniquely identify the upload. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Content-Type` | string | Yes | Standard HTTP `Content-Type` header. |
| `Tus-Resumable` | string | Yes | The version of the tus protocol used. |
| `Upload-Offset` | integer | Yes | The byte offset within the upload. |
| `Content-Length` | integer | No | Standard HTTP `Content-Length` header. |

#### Request Body

**Required**

The patch content (binary, either a complete or a partial file) to upload.

**Content-Type:** `application/offset+octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/offset+octet-stream` | string | No |  |

#### Responses

##### 204

No Content. Patch successfully applied to upload.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 404

Not Found. Non-existent upload resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 409

Conflict. Upload offsets do not match.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 410

Gone. The upload resource no longer exists (could have expired).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 412

Precondition Failed. tus protocol version not supported by the server.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 415

Unsupported Media Type

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

##### 423

Locked. Concurrent access is not allowed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An Error object. |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The API error code. |
| `meta` | object | No | Additional properties and information regarding the issue. |
| `title` | string | Yes | Title of the type of API Error. |
| `detail` | string | No | A human-readable problem description of the issue. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | Locale |
| `errorType` | string | No | The error type. |
| `sourceErrors` | string | No | The source errors (stack trace). |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/temp-contents/files/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/temp-contents/files/{id}',
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
# qlik-cli has not implemented support for PATCH /api/v1/temp-contents/files/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents/files/{id}" \
-X PATCH \
-H "Content-Type: string" \
-H "Tus-Resumable: string" \
-H "Upload-Offset: 0" \
-H "Content-type: application/offset+octet-stream" \
-H "Authorization: Bearer <access_token>" \
-d '"string"'
```

---
