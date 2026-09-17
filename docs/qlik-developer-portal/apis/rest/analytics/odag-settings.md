# ODAG settings

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Read and configure tenant-level on-demand analytics generation settings.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/analytics/odag-settings`](#get-apianalyticsodag-settings) | Retrieves ODAG settings, including feature enablement status. Available only to administrators. |
| `PUT` | [`/api/analytics/odag-settings`](#put-apianalyticsodag-settings) | Modifies ODAG settings such as feature enablement. Available only to administrators. Changes apply immediately to all ODAG operations. |
| `GET` | [`/api/analytics/odag-settings/canupdate`](#get-apianalyticsodag-settingscanupdate) | Checks whether the current user has permission to modify ODAG settings. |

## API Reference

### GET /api/analytics/odag-settings

Retrieves ODAG settings, including feature enablement status. Available only to administrators.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

ODAG settings retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `odagEnabled` | boolean | No | Whether the ODAG feature is enabled. |
| `dynamicViewEnabled` | boolean | No | Whether the dynamic view feature is enabled. |

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 500

Internal system error accessing ODAG settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-settings',
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
# qlik-cli has not implemented support for GET /api/analytics/odag-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "odagEnabled": true,
  "dynamicViewEnabled": true
}
```

---

### PUT /api/analytics/odag-settings

Modifies ODAG settings such as feature enablement. Available only to administrators. Changes apply immediately to all ODAG operations.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

A JSON payload containing the content for the new settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `odagEnabled` | boolean | No |  |
| `dynamicViewEnabled` | boolean | No |  |

#### Responses

##### 200

ODAG settings updated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `odagEnabled` | boolean | No | Whether the ODAG feature is enabled. |
| `dynamicViewEnabled` | boolean | No | Whether the dynamic view feature is enabled. |

##### 403

Access denied. You lack permission to modify ODAG settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 500

Internal system error accessing ODAG settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/analytics/odag-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      odagEnabled: true,
      dynamicViewEnabled: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/analytics/odag-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"odagEnabled":true,"dynamicViewEnabled":true}'
```

**Example Response:**

```json
{
  "odagEnabled": true,
  "dynamicViewEnabled": true
}
```

---

### GET /api/analytics/odag-settings/canupdate

Checks whether the current user has permission to modify ODAG settings.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Permission check completed successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `canUpdateSettings` | boolean | No |  |

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-settings/canupdate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-settings/canupdate',
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
# qlik-cli has not implemented support for GET /api/analytics/odag-settings/canupdate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-settings/canupdate" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "canUpdateSettings": true
}
```

---
