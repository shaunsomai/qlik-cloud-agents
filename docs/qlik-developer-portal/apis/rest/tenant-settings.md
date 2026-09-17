# Tenant settings

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Configure tenant-wide settings for security, appearance, and operational preferences.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/tenant-settings`](#get-apiv1tenant-settings) | Retrieves tenant settings associated with the tenant ID specified in JWT. This is access controlled by the permission admin.tenant-settings:read. |
| `POST` | [`/api/v1/tenant-settings`](#post-apiv1tenant-settings) | Creates a new tenant settings entry for the tenant ID specified in the JWT. This is access controlled by the permission admin.tenant-settings:create. |
| `PATCH` | [`/api/v1/tenant-settings`](#patch-apiv1tenant-settings) | Updates existing tenant settings. This is access controlled by the permission admin.tenant-settings:update. |
| `DELETE` | [`/api/v1/tenant-settings`](#delete-apiv1tenant-settings) | Deletes the tenant settings associated with the tenant ID specified in JWT. This is access controlled by the permission admin.tenant-settings:delete. |
| `POST` | [`/api/v1/tenant-settings/actions/toggle-cross-region-data-processing`](#post-apiv1tenant-settingsactionstoggle-cross-region-data-processing) | Sets the cross region inference setting for the tenant. Creates tenant settings if none exist, or updates existing settings. This is access controlled by the permission `admin.tenant-settings:update`. |
| `POST` | [`/api/v1/tenant-settings/actions/toggle-cross-region-inference`](#post-apiv1tenant-settingsactionstoggle-cross-region-inference) | Sets the cross-region inference setting for the tenant. Creates tenant settings if none exist, or updates existing settings. This is access controlled by the permission `admin.tenant-settings:update`. |
| `GET` | [`/api/v1/tenant-settings/start-pages`](#get-apiv1tenant-settingsstart-pages) | Retrieves start pages for the tenant settings. |

## API Reference

### GET /api/v1/tenant-settings

Retrieves tenant settings associated with the tenant ID specified in JWT. This is access controlled by the permission admin.tenant-settings:read.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Tenant settings retrieval was successful.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the settings |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | No | userId of the user who last modified the settings |
| `releaseCadence` | string | No | Set the release cadence Enum: "monthly", "continuous" |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | object | No |  |
| `sessionReplayOptOut` | boolean | No | Tenant-wide preference for opting out of session replay. When set, this value overrides individual user preferences. EU regions default to true (opted out) if this is not explicitly configured. |
| `crossRegionDataProcessing` | boolean | No | Set to true to enable cross-region inference, false to disable. |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `preferredStartPage`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigConsole` | object | No |  |

<details>
<summary>Properties of `StartPageConfigConsole`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/console" |
| `value` | string | No | Enum: "management-console" |

</details>

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tenant-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings',
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
# qlik-cli has not implemented support for GET /api/v1/tenant-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "releaseCadence": "monthly",
  "customizeNoAccess": {
    "linkUrl": "string",
    "message": "string",
    "linkLabel": "string",
    "linkEnabled": true
  },
  "preferredStartPage": {
    "route": "/insights",
    "value": "analytics-hub"
  },
  "sessionReplayOptOut": true,
  "crossRegionDataProcessing": true
}
```

---

### POST /api/v1/tenant-settings

Creates a new tenant settings entry for the tenant ID specified in the JWT. This is access controlled by the permission admin.tenant-settings:create.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | string | No | Enum: "analytics-hub", "data-integration-hub", "management-console", "analytics-creation-hub" |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

#### Responses

##### 201

The tenant settings have been successfully created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the settings |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | No | userId of the user who last modified the settings |
| `releaseCadence` | string | No | Set the release cadence Enum: "monthly", "continuous" |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | object | No |  |
| `sessionReplayOptOut` | boolean | No | Tenant-wide preference for opting out of session replay. When set, this value overrides individual user preferences. EU regions default to true (opted out) if this is not explicitly configured. |
| `crossRegionDataProcessing` | boolean | No | Set to true to enable cross-region inference, false to disable. |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `preferredStartPage`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigConsole` | object | No |  |

<details>
<summary>Properties of `StartPageConfigConsole`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/console" |
| `value` | string | No | Enum: "management-console" |

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
| `status` | integer | No |  |

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
| `status` | integer | No |  |

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
| `status` | integer | No |  |

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
| `status` | integer | No |  |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenant-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      customizeNoAccess: {
        linkUrl: 'string',
        message: 'string',
        linkLabel: 'string',
        linkEnabled: true,
      },
      preferredStartPage: 'analytics-hub',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenant-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"customizeNoAccess":{"linkUrl":"string","message":"string","linkLabel":"string","linkEnabled":true},"preferredStartPage":"analytics-hub"}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "releaseCadence": "monthly",
  "customizeNoAccess": {
    "linkUrl": "string",
    "message": "string",
    "linkLabel": "string",
    "linkEnabled": true
  },
  "preferredStartPage": {
    "route": "/insights",
    "value": "analytics-hub"
  },
  "sessionReplayOptOut": true,
  "crossRegionDataProcessing": true
}
```

---

### PATCH /api/v1/tenant-settings

Updates existing tenant settings. This is access controlled by the permission admin.tenant-settings:update.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object[] | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `JSONPatchRequestAddReplaceTest` | object | No |  |

<details>
<summary>Properties of `JSONPatchRequestAddReplaceTest`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to perform. Enum: "add", "replace", "test" |
| `path` | string | Yes | A JSON Pointer path. |
| `value` | any | Yes | The value to add, replace or test. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `JSONPatchRequestRemove` | object | No |  |

<details>
<summary>Properties of `JSONPatchRequestRemove`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to perform. Enum: "remove" |
| `path` | string | Yes | A JSON Pointer path. |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `JSONPatchRequestMoveCopy` | object | No |  |

<details>
<summary>Properties of `JSONPatchRequestMoveCopy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to perform. Enum: "move", "copy" |
| `from` | string | Yes | A JSON Pointer path. |
| `path` | string | Yes | A JSON Pointer path. |

</details>

</details>

#### Responses

##### 200

The tenant settings have been successfully updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the settings |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | No | userId of the user who last modified the settings |
| `releaseCadence` | string | No | Set the release cadence Enum: "monthly", "continuous" |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | object | No |  |
| `sessionReplayOptOut` | boolean | No | Tenant-wide preference for opting out of session replay. When set, this value overrides individual user preferences. EU regions default to true (opted out) if this is not explicitly configured. |
| `crossRegionDataProcessing` | boolean | No | Set to true to enable cross-region inference, false to disable. |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `preferredStartPage`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigConsole` | object | No |  |

<details>
<summary>Properties of `StartPageConfigConsole`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/console" |
| `value` | string | No | Enum: "management-console" |

</details>

</details>

##### 404

Tenant settings for this tenant do not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/tenant-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      { op: 'add', path: 'string' },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/tenant-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"string"}]'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "releaseCadence": "monthly",
  "customizeNoAccess": {
    "linkUrl": "string",
    "message": "string",
    "linkLabel": "string",
    "linkEnabled": true
  },
  "preferredStartPage": {
    "route": "/insights",
    "value": "analytics-hub"
  },
  "sessionReplayOptOut": true,
  "crossRegionDataProcessing": true
}
```

---

### DELETE /api/v1/tenant-settings

Deletes the tenant settings associated with the tenant ID specified in JWT. This is access controlled by the permission admin.tenant-settings:delete.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 204

The tenant settings have been successfully deleted.

##### 404

Tenant settings for tenant ID do not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/tenant-settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings',
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
# qlik-cli has not implemented support for DELETE /api/v1/tenant-settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/tenant-settings/actions/toggle-cross-region-data-processing _(deprecated)_

Sets the cross region inference setting for the tenant. Creates tenant settings if none exist, or updates existing settings. This is access controlled by the permission `admin.tenant-settings:update`.
When cross-region processing is required, you must include an additional header `x-qlik-consent-verified: true` in your API requests to confirm that you have the authority to enable this feature and accept the associated terms.


- **Replaced by:** "POST:/v1/tenant-settings/actions/toggle-cross-region-inference"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-05. Use `/tenant-settings/actions/toggle-cross-region-inference` instead. This endpoint uses outdated terminology.

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | boolean | Yes | Set to true to enable cross-region inference, false to disable. |

#### Responses

##### 200

The cross region inference setting has been successfully updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the settings |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | No | userId of the user who last modified the settings |
| `releaseCadence` | string | No | Set the release cadence Enum: "monthly", "continuous" |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | object | No |  |
| `sessionReplayOptOut` | boolean | No | Tenant-wide preference for opting out of session replay. When set, this value overrides individual user preferences. EU regions default to true (opted out) if this is not explicitly configured. |
| `crossRegionDataProcessing` | boolean | No | Set to true to enable cross-region inference, false to disable. |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `preferredStartPage`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigConsole` | object | No |  |

<details>
<summary>Properties of `StartPageConfigConsole`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/console" |
| `value` | string | No | Enum: "management-console" |

</details>

</details>

##### 400

Bad Request. The request is incorrect.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### 401

Unauthorized. The user is not authorized to access the service.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### 403

Forbidden. You don't have sufficient permissions to access this resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenant-settings/actions/toggle-cross-region-data-processing` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings/actions/toggle-cross-region-data-processing',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ value: true }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenant-settings/actions/toggle-cross-region-data-processing yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings/actions/toggle-cross-region-data-processing" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"value":true}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "releaseCadence": "monthly",
  "customizeNoAccess": {
    "linkUrl": "string",
    "message": "string",
    "linkLabel": "string",
    "linkEnabled": true
  },
  "preferredStartPage": {
    "route": "/insights",
    "value": "analytics-hub"
  },
  "sessionReplayOptOut": true,
  "crossRegionDataProcessing": true
}
```

---

### POST /api/v1/tenant-settings/actions/toggle-cross-region-inference

Sets the cross-region inference setting for the tenant. Creates tenant settings if none exist, or updates existing settings. This is access controlled by the permission `admin.tenant-settings:update`.
When cross-region inference is required, you must include an additional header `x-qlik-consent-verified: true` in your API requests to confirm that you have the authority to enable this feature and accept the associated terms.


- **Replaces:** "POST:/v1/tenant-settings/actions/toggle-cross-region-data-processing"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | boolean | Yes | Set to true to enable cross-region inference, false to disable. |

#### Responses

##### 200

The cross region inference setting has been successfully updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `tenantId` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `createdBy` | string | Yes | userId of the user who created the settings |
| `updatedAt` | string | Yes |  |
| `updatedBy` | string | No | userId of the user who last modified the settings |
| `releaseCadence` | string | No | Set the release cadence Enum: "monthly", "continuous" |
| `customizeNoAccess` | object | No |  |
| `preferredStartPage` | object | No |  |
| `sessionReplayOptOut` | boolean | No | Tenant-wide preference for opting out of session replay. When set, this value overrides individual user preferences. EU regions default to true (opted out) if this is not explicitly configured. |
| `crossRegionDataProcessing` | boolean | No | Set to true to enable cross-region inference, false to disable. |

<details>
<summary>Properties of `customizeNoAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkUrl` | string | No |  |
| `message` | string | No |  |
| `linkLabel` | string | No |  |
| `linkEnabled` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `preferredStartPage`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigConsole` | object | No |  |

<details>
<summary>Properties of `StartPageConfigConsole`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/console" |
| `value` | string | No | Enum: "management-console" |

</details>

</details>

##### 400

Bad Request. The request is incorrect.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### 401

Unauthorized. The user is not authorized to access the service.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### 403

Forbidden. You don't have sufficient permissions to access this resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/tenant-settings/actions/toggle-cross-region-inference` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings/actions/toggle-cross-region-inference',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ value: true }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/tenant-settings/actions/toggle-cross-region-inference yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings/actions/toggle-cross-region-inference" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"value":true}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "updatedBy": "string",
  "releaseCadence": "monthly",
  "customizeNoAccess": {
    "linkUrl": "string",
    "message": "string",
    "linkLabel": "string",
    "linkEnabled": true
  },
  "preferredStartPage": {
    "route": "/insights",
    "value": "analytics-hub"
  },
  "sessionReplayOptOut": true,
  "crossRegionDataProcessing": true
}
```

---

### GET /api/v1/tenant-settings/start-pages

Retrieves start pages for the tenant settings.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Tenant settings start pages retrieval was successful.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes |  |
| `defaultValue` | string | Yes | Enum: "analytics-hub" |

<details>
<summary>Properties of `values`</summary>

**Any of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/insights" |
| `value` | string | No | Enum: "analytics-hub" |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigCreationHub` | object | No |  |

<details>
<summary>Properties of `StartPageConfigCreationHub`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/analytics" |
| `value` | string | No | Enum: "analytics-creation-hub" |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartPageConfigQdi` | object | No |  |

<details>
<summary>Properties of `StartPageConfigQdi`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `route` | string | No | Enum: "/qdi" |
| `value` | string | No | Enum: "data-integration-hub" |

</details>

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | No | Error code. |
| `title` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/tenant-settings/start-pages` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/tenant-settings/start-pages',
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
# qlik-cli has not implemented support for GET /api/v1/tenant-settings/start-pages yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings/start-pages" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "values": [
    {
      "route": "/insights",
      "value": "analytics-hub"
    }
  ],
  "defaultValue": "analytics-hub"
}
```

---
