# CSP origins

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

CSP origins allow you to configure domains, or origins, that Qlik Sense client visualizations/extensions are allowed to communicate with.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/csp-origins`](#get-apiv1csp-origins) | Retrieves all content security policies for a tenant. |
| `POST` | [`/api/v1/csp-origins`](#post-apiv1csp-origins) | Creates a new content security policy for an origin. |
| `GET` | [`/api/v1/csp-origins/{id}`](#get-apiv1csp-originsid) | Returns details for a specific content security policy. |
| `PUT` | [`/api/v1/csp-origins/{id}`](#put-apiv1csp-originsid) | Updates a content security policy. |
| `DELETE` | [`/api/v1/csp-origins/{id}`](#delete-apiv1csp-originsid) | Deletes a specific content security policy. |
| `GET` | [`/api/v1/csp-origins/actions/generate-header`](#get-apiv1csp-originsactionsgenerate-header) | Retrieves the full content security policy header (including all configured policies and origins) for the tenant. |

## API Reference

### GET /api/v1/csp-origins

Retrieves all content security policies for a tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `childSrc` | boolean | No | Filter resources by directive 'childSrc', true/false. |
| `connectSrc` | boolean | No | Filter resources by directive 'connectSrc', true/false. |
| `connectSrcWSS` | boolean | No | Filter resources by directive 'connectSrcWSS', true/false. |
| `fontSrc` | boolean | No | Filter resources by directive 'fontSrc', true/false. |
| `formAction` | boolean | No | Filter resources by directive 'formAction', true/false. |
| `frameAncestors` | boolean | No | Filter resources by directive 'frameAncestors', true/false. |
| `frameSrc` | boolean | No | Filter resources by directive 'frameSrc', true/false. |
| `imgSrc` | boolean | No | Filter resources by directive 'imgSrc', true/false. |
| `limit` | number | No | Maximum number of CSP-Origins to retrieve. |
| `mediaSrc` | boolean | No | Filter resources by directive 'mediaSrc', true/false. |
| `name` | string | No | Filter resources by name (wildcard and case insensitive). |
| `next` | string | No | Cursor to the next page. |
| `objectSrc` | boolean | No | Filter resources by directive 'objectSrc', true/false. |
| `origin` | string | No | Filter resources by origin (wildcard and case insensitive). |
| `prev` | string | No | Cursor to previous next page. |
| `scriptSrc` | boolean | No | Filter resources by directive 'scriptSrc', true/false. |
| `sort` | string | No | Field to sort by, prefix with -/+ to indicate order. Enum: "name", "-name", "origin", "-origin", "createdDate", "-createdDate", "modifiedDate", "-modifiedDate" |
| `styleSrc` | boolean | No | Filter resources by directive 'styleSrc', true/false. |
| `workerSrc` | boolean | No | Filter resources by directive 'workerSrc', true/false. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The CSP entry's unique identifier. |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `createdDate` | string | No | The UTC timestamp when the CSP entry was created. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `modifiedDate` | string | No | The UTC timestamp when the CSP entry was last modified. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

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
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/csp-origins` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins',
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
# qlik-cli has not implemented support for GET /api/v1/csp-origins yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "name": "string",
      "imgSrc": true,
      "origin": "string",
      "fontSrc": true,
      "childSrc": true,
      "frameSrc": true,
      "mediaSrc": true,
      "styleSrc": true,
      "objectSrc": true,
      "scriptSrc": true,
      "workerSrc": true,
      "connectSrc": true,
      "formAction": true,
      "createdDate": "2018-10-30T07:06:22Z",
      "description": "string",
      "modifiedDate": "2018-10-30T07:06:22Z",
      "connectSrcWSS": true,
      "frameAncestors": true,
      "id": "string"
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

### POST /api/v1/csp-origins

Creates a new content security policy for an origin.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

#### Responses

##### 201

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The CSP entry's unique identifier. |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `createdDate` | string | No | The UTC timestamp when the CSP entry was created. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `modifiedDate` | string | No | The UTC timestamp when the CSP entry was last modified. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/csp-origins` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      imgSrc: true,
      origin: 'string',
      fontSrc: true,
      childSrc: true,
      frameSrc: true,
      mediaSrc: true,
      styleSrc: true,
      objectSrc: true,
      scriptSrc: true,
      workerSrc: true,
      connectSrc: true,
      formAction: true,
      description: 'string',
      connectSrcWSS: true,
      frameAncestors: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/csp-origins yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","imgSrc":true,"origin":"string","fontSrc":true,"childSrc":true,"frameSrc":true,"mediaSrc":true,"styleSrc":true,"objectSrc":true,"scriptSrc":true,"workerSrc":true,"connectSrc":true,"formAction":true,"description":"string","connectSrcWSS":true,"frameAncestors":true}'
```

**Example Response:**

```json
{
  "name": "string",
  "imgSrc": true,
  "origin": "string",
  "fontSrc": true,
  "childSrc": true,
  "frameSrc": true,
  "mediaSrc": true,
  "styleSrc": true,
  "objectSrc": true,
  "scriptSrc": true,
  "workerSrc": true,
  "connectSrc": true,
  "formAction": true,
  "createdDate": "2018-10-30T07:06:22Z",
  "description": "string",
  "modifiedDate": "2018-10-30T07:06:22Z",
  "connectSrcWSS": true,
  "frameAncestors": true,
  "id": "string"
}
```

---

### GET /api/v1/csp-origins/{id}

Returns details for a specific content security policy.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The CSP entry's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The CSP entry's unique identifier. |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `createdDate` | string | No | The UTC timestamp when the CSP entry was created. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `modifiedDate` | string | No | The UTC timestamp when the CSP entry was last modified. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/csp-origins/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/csp-origins/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "name": "string",
  "imgSrc": true,
  "origin": "string",
  "fontSrc": true,
  "childSrc": true,
  "frameSrc": true,
  "mediaSrc": true,
  "styleSrc": true,
  "objectSrc": true,
  "scriptSrc": true,
  "workerSrc": true,
  "connectSrc": true,
  "formAction": true,
  "createdDate": "2018-10-30T07:06:22Z",
  "description": "string",
  "modifiedDate": "2018-10-30T07:06:22Z",
  "connectSrcWSS": true,
  "frameAncestors": true,
  "id": "string"
}
```

---

### PUT /api/v1/csp-origins/{id}

Updates a content security policy.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The CSP entry's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The CSP entry's unique identifier. |
| `name` | string | No | The name for this entry. |
| `imgSrc` | boolean | No | Specifies valid sources of images and favicons. |
| `origin` | string | Yes | The origin that the CSP directives should be applied to. |
| `fontSrc` | boolean | No | Specifies valid sources for loading fonts. |
| `childSrc` | boolean | No | Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame. |
| `frameSrc` | boolean | No | Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame. |
| `mediaSrc` | boolean | No | Specifies valid sources for loading media using the audio and video elements. |
| `styleSrc` | boolean | No | Specifies valid sources for stylesheets. |
| `objectSrc` | boolean | No | Specifies valid sources for the object, embed, and applet elements. |
| `scriptSrc` | boolean | No | Specifies valid sources for JavaScript. |
| `workerSrc` | boolean | No | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |
| `connectSrc` | boolean | No | Restricts the URLs that can be loaded using script interfaces. |
| `formAction` | boolean | No | Allow forms to be submitted to the origin. |
| `createdDate` | string | No | The UTC timestamp when the CSP entry was created. |
| `description` | string | No | The reason for adding this origin to the Content Security Policy. |
| `modifiedDate` | string | No | The UTC timestamp when the CSP entry was last modified. |
| `connectSrcWSS` | boolean | No | Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://'). |
| `frameAncestors` | boolean | No | Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/csp-origins/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      imgSrc: true,
      origin: 'string',
      fontSrc: true,
      childSrc: true,
      frameSrc: true,
      mediaSrc: true,
      styleSrc: true,
      objectSrc: true,
      scriptSrc: true,
      workerSrc: true,
      connectSrc: true,
      formAction: true,
      description: 'string',
      connectSrcWSS: true,
      frameAncestors: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/csp-origins/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","imgSrc":true,"origin":"string","fontSrc":true,"childSrc":true,"frameSrc":true,"mediaSrc":true,"styleSrc":true,"objectSrc":true,"scriptSrc":true,"workerSrc":true,"connectSrc":true,"formAction":true,"description":"string","connectSrcWSS":true,"frameAncestors":true}'
```

**Example Response:**

```json
{
  "name": "string",
  "imgSrc": true,
  "origin": "string",
  "fontSrc": true,
  "childSrc": true,
  "frameSrc": true,
  "mediaSrc": true,
  "styleSrc": true,
  "objectSrc": true,
  "scriptSrc": true,
  "workerSrc": true,
  "connectSrc": true,
  "formAction": true,
  "createdDate": "2018-10-30T07:06:22Z",
  "description": "string",
  "modifiedDate": "2018-10-30T07:06:22Z",
  "connectSrcWSS": true,
  "frameAncestors": true,
  "id": "string"
}
```

---

### DELETE /api/v1/csp-origins/{id}

Deletes a specific content security policy.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The CSP entry's unique identifier. |

#### Responses

##### 204

No Content response.

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/csp-origins/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/csp-origins/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/csp-origins/actions/generate-header

Retrieves the full content security policy header (including all configured policies and origins) for the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Accept` | string | No | The Accept request HTTP header indicates which content types, expressed as MIME types, the client is able to understand Enum: "application/json", "text/plain" |

#### Responses

##### 200

OK Response

**Content-Type:** `text/plain`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/plain` | string | No |  |

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Content-Security-Policy` | string | No | The compiled CSP header. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

##### 406

Not Acceptable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

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
| `code` | string | Yes | The unique code for the error. |
| `title` | string | Yes | A summary of what went wrong. |
| `detail` | string | No | May be used to provide additional details. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/csp-origins/actions/generate-header` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/csp-origins/actions/generate-header',
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
# qlik-cli has not implemented support for GET /api/v1/csp-origins/actions/generate-header yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins/actions/generate-header" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```text
string
```

---
