# Apps

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Create, manage, and retrieve analytics applications in Qlik Cloud.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/apps`](#post-apiv1apps) | Creates a new app. |
| `GET` | [`/api/v1/apps/{appId}`](#get-apiv1appsappid) | Retrieves information for a specific app. |
| `PUT` | [`/api/v1/apps/{appId}`](#put-apiv1appsappid) | Updates the information for a specific app. |
| `DELETE` | [`/api/v1/apps/{appId}`](#delete-apiv1appsappid) | Deletes a specific app. |
| `POST` | [`/api/v1/apps/{appId}/copy`](#post-apiv1appsappidcopy) | Copies a specific app. |
| `GET` | [`/api/v1/apps/{appId}/data/lineage`](#get-apiv1appsappiddatalineage) | Retrieves the lineage for an app. |
| `GET` | [`/api/v1/apps/{appId}/data/metadata`](#get-apiv1appsappiddatametadata) | Retrieves the data model and reload statistics metadata of an app. |
| `POST` | [`/api/v1/apps/{appId}/export`](#post-apiv1appsappidexport) | Exports a specific app. |
| `GET` | [`/api/v1/apps/{appId}/insight-analyses`](#get-apiv1appsappidinsight-analyses) |  |
| `POST` | [`/api/v1/apps/{appId}/insight-analyses/actions/recommend`](#post-apiv1appsappidinsight-analysesactionsrecommend) |  |
| `GET` | [`/api/v1/apps/{appId}/insight-analyses/model`](#get-apiv1appsappidinsight-analysesmodel) |  |
| `GET` | [`/api/v1/apps/{appId}/media/files/{path}`](#get-apiv1appsappidmediafilespath) | Gets media content from file. |
| `PUT` | [`/api/v1/apps/{appId}/media/files/{path}`](#put-apiv1appsappidmediafilespath) | Stores the media content file. |
| `DELETE` | [`/api/v1/apps/{appId}/media/files/{path}`](#delete-apiv1appsappidmediafilespath) | Deletes a media content file or complete directory. |
| `GET` | [`/api/v1/apps/{appId}/media/list/{path}`](#get-apiv1appsappidmedialistpath) | Lists media content. |
| `GET` | [`/api/v1/apps/{appId}/media/thumbnail`](#get-apiv1appsappidmediathumbnail) | Gets media content from file currently used as application thumbnail. |
| `POST` | [`/api/v1/apps/{appId}/objects/{objectId}/actions/change-owner`](#post-apiv1appsappidobjectsobjectidactionschange-owner) | Sets owner on an app object. |
| `PUT` | [`/api/v1/apps/{appId}/owner`](#put-apiv1appsappidowner) | Changes owner of the app. |
| `GET` | [`/api/v1/apps/{appId}/placement`](#get-apiv1appsappidplacement) | Retrieves the app size override for an app. |
| `PUT` | [`/api/v1/apps/{appId}/placement`](#put-apiv1appsappidplacement) | Sets the app size override for an app. |
| `DELETE` | [`/api/v1/apps/{appId}/placement`](#delete-apiv1appsappidplacement) | Removes the app size override for an app. |
| `POST` | [`/api/v1/apps/{appId}/publish`](#post-apiv1appsappidpublish) | Publishes a specific app to a managed space. |
| `PUT` | [`/api/v1/apps/{appId}/publish`](#put-apiv1appsappidpublish) | Republishes a published app to a managed space. |
| `GET` | [`/api/v1/apps/{appId}/reloads/logs`](#get-apiv1appsappidreloadslogs) | Retrieves the metadata about all script logs stored for an app. |
| `GET` | [`/api/v1/apps/{appId}/reloads/logs/{reloadId}`](#get-apiv1appsappidreloadslogsreloadid) | Retrieves the log of a specific reload. |
| `GET` | [`/api/v1/apps/{appId}/reloads/metadata/{reloadId}`](#get-apiv1appsappidreloadsmetadatareloadid) | Retrieves the app reload metadata list. |
| `GET` | [`/api/v1/apps/{appId}/report-filters`](#get-apiv1appsappidreport-filters) | List all filters that are present in the given app. Filters allow to reduce the app data visible in a report output. Each filter can contain definitions on one or multiple fields. |
| `POST` | [`/api/v1/apps/{appId}/report-filters`](#post-apiv1appsappidreport-filters) | Creates a new report filter which is used to re-apply selections, variables, patches to an engine session. |
| `GET` | [`/api/v1/apps/{appId}/report-filters/{id}`](#get-apiv1appsappidreport-filtersid) |  |
| `PATCH` | [`/api/v1/apps/{appId}/report-filters/{id}`](#patch-apiv1appsappidreport-filtersid) |  |
| `DELETE` | [`/api/v1/apps/{appId}/report-filters/{id}`](#delete-apiv1appsappidreport-filtersid) |  |
| `GET` | [`/api/v1/apps/{appId}/report-filters/actions/count`](#get-apiv1appsappidreport-filtersactionscount) |  |
| `GET` | [`/api/v1/apps/{appId}/scripts`](#get-apiv1appsappidscripts) | Retrieves the script history for an app. |
| `POST` | [`/api/v1/apps/{appId}/scripts`](#post-apiv1appsappidscripts) | Sets script for an app. |
| `GET` | [`/api/v1/apps/{appId}/scripts/{id}`](#get-apiv1appsappidscriptsid) | Retrieves a version of the script for an app. |
| `PATCH` | [`/api/v1/apps/{appId}/scripts/{id}`](#patch-apiv1appsappidscriptsid) | Updates a specific version of the script for an app. |
| `DELETE` | [`/api/v1/apps/{appId}/scripts/{id}`](#delete-apiv1appsappidscriptsid) | Deletes a specific version of the script for an app. |
| `PUT` | [`/api/v1/apps/{appId}/space`](#put-apiv1appsappidspace) | Sets space on a specific app. |
| `DELETE` | [`/api/v1/apps/{appId}/space`](#delete-apiv1appsappidspace) | Removes space from a specific app. |
| `GET` | [`/api/v1/apps/{guid}/evaluations`](#get-apiv1appsguidevaluations) | Find all evaluations for an app GUID. |
| `POST` | [`/api/v1/apps/{guid}/evaluations`](#post-apiv1appsguidevaluations) | Queue an app evaluation by its app guid. |
| `GET` | [`/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}`](#get-apiv1appsevaluationsbaseidactionscomparecomparisonid) | Accepts two evaluation ids and returns a comparison denoting the differences between the two. |
| `GET` | [`/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download`](#get-apiv1appsevaluationsbaseidactionscomparecomparisonidactionsdownload) | Accepts two evaluation ids and downloads a log, in XML format, denoting the differences between the two. |
| `GET` | [`/api/v1/apps/evaluations/{id}`](#get-apiv1appsevaluationsid) | Find an evaluation by a specific id. |
| `GET` | [`/api/v1/apps/evaluations/{id}/actions/download`](#get-apiv1appsevaluationsidactionsdownload) | Find and download an evaluation log by a specific evaluation id. |
| `POST` | [`/api/v1/apps/import`](#post-apiv1appsimport) | Imports an app into the system. |
| `GET` | [`/api/v1/apps/privileges`](#get-apiv1appsprivileges) | Gets the app privileges for the current user, such as create app and import app. Empty means that the current user has no app privileges. |
| `POST` | [`/api/v1/apps/validatescript`](#post-apiv1appsvalidatescript) | Validates the script. |

## API Reference

### POST /api/v1/apps

Creates a new app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Request Body

**Required**

Attributes that the user wants to set in new app.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name (title) of the application |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `locale` | string | No | Set custom locale instead of the system default |
| `spaceId` | string | No | The space ID of the application |
| `description` | string | No | The description of the application |

</details>

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/apps', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/apps yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"attributes":{"name":"string","locale":"string","spaceId":"string","description":"string"}}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/{appId}

Retrieves information for a specific app.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### PUT /api/v1/apps/{appId}

Updates the information for a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

Attributes that user wants to set.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name (title) of the application. |
| `description` | string | No | The description of the application. |

</details>

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}" \
-X PUT \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"attributes":{"name":"string","description":"string"}}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### DELETE /api/v1/apps/{appId}

Deletes a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/apps/{appId}/copy

Copies a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

Attributes that should be set in the copy.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attributes` | object | No |  |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name (title) of the application |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `locale` | string | No | Set custom locale instead of the system default |
| `spaceId` | string | No | The space ID of the application |
| `description` | string | No | The description of the application |

</details>

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/copy` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/copy',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/copy yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/copy" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"attributes":{"name":"string","locale":"string","spaceId":"string","description":"string"}}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/{appId}/data/lineage

Retrieves the lineage for an app.
Returns a JSON-formatted array of strings describing the lineage of the app.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statement` | string | No | The LOAD and SELECT script statements from the data load script. |
| `discriminator` | string | No | A string indicating the origin of the data: * [filename]: the data comes from a local file. * INLINE: the data is entered inline in the load script. * RESIDENT: the data comes from a resident table. The table name is listed. * AUTOGENERATE: the data is generated from the load script (no external table of data source). * Provider: the data comes from a data connection. The connector source name is listed. * [webfile]: the data comes from a web-based file. * STORE: path to QVD or TXT file where data is stored. * EXTENSION: the data comes from a Server Side Extension (SSE). |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/data/lineage` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/data/lineage',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/data/lineage yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/data/lineage" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "statement": "string",
    "discriminator": "string"
  }
]
```

---

### GET /api/v1/apps/{appId}/data/metadata

Retrieves the data model and reload statistics metadata of an app.
An empty metadata structure is returned if the metadata is not available in the app.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `fields` | object[] | No | List of field descriptions. |
| `tables` | object[] | No | List of table descriptions. |
| `reload_meta` | object | No |  |
| `static_byte_size` | integer | No | Static memory usage for the app. |
| `has_section_access` | boolean | No | If set to true, the app has section access configured. |
| `is_direct_query_mode` | boolean | No |  |
| `tables_profiling_data` | object[] | No | Profiling data of the tables in the app. |

<details>
<summary>Properties of `fields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hash` | string | No | Hash of the data in the field. If the data in a reload is the same, the hash will be consistent. |
| `name` | string | No | Name of the field. |
| `tags` | string[] | No | Gives information on a field. For example, it can return the type of the field. Examples: key, text, ASCII. |
| `comment` | string | No | Field comment. |
| `cardinal` | integer | No | Number of distinct field values. |
| `byte_size` | integer | No | Static RAM memory used in bytes. |
| `is_hidden` | boolean | No | If set to true, the field is hidden. The default value is false. |
| `is_locked` | boolean | No | If set to true, the field is locked. The default value is false. |
| `is_system` | boolean | No | If set to true, the field is a system field. The default value is false. |
| `is_numeric` | boolean | No | Is set to true if the value is a numeric. The default value is false. |
| `src_tables` | string[] | No | List of table names. |
| `is_semantic` | boolean | No | If set to true, the field is semantic. The default value is false. |
| `total_count` | integer | No | Total number of field values. |
| `distinct_only` | boolean | No | If set to true, only distinct field values are shown. The default value is false. |
| `always_one_selected` | boolean | No | If set to true, the field has one and only one selection (not 0 and not more than 1). If this property is set to true, the field cannot be cleared anymore and no more selections can be performed in that field. The default value is false. |

</details>

<details>
<summary>Properties of `tables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the table. |
| `comment` | string | No | Table comment. |
| `is_loose` | boolean | No | If set to true, the table is loose due to circular connection. The default value is false. |
| `byte_size` | integer | No | Static RAM memory used in bytes. |
| `is_system` | boolean | No | If set to true, the table is a system table. The default value is false. |
| `no_of_rows` | integer | No | Number of rows. |
| `is_semantic` | boolean | No | If set to true, the table is semantic. The default value is false. |
| `no_of_fields` | integer | No | Number of fields. |
| `no_of_key_fields` | integer | No | Number of key fields. |

</details>

<details>
<summary>Properties of `reload_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hardware` | object | No |  |
| `cpu_time_spent_ms` | integer | No | Number of CPU milliseconds it took to reload the app. |
| `peak_memory_bytes` | integer | No | Maximum number of bytes used during reload of the app. |
| `fullReloadPeakMemoryBytes` | integer | No | Maximum number of bytes used during full reload of the app. |
| `partialReloadPeakMemoryBytes` | integer | No | Maximum number of bytes used during partial reload of the app. |

<details>
<summary>Properties of `hardware`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total_memory` | integer | No | RAM available. |
| `logical_cores` | integer | No | Number of logical cores available. |

</details>

</details>

<details>
<summary>Properties of `tables_profiling_data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `NoOfRows` | integer | No | Number of rows in the table. |
| `FieldProfiling` | object[] | No | Field values profiling info |

<details>
<summary>Properties of `FieldProfiling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Max` | number | No | Maximum value of numerical values. NaN otherwise. |
| `Min` | number | No | Minimum value of numerical values. NaN otherwise. |
| `Std` | number | No | Standard deviation of numerical values. NaN otherwise. |
| `Sum` | number | No | Sum of all numerical values. NaN otherwise. |
| `Name` | string | No | Name of the field. |
| `Sum2` | number | No | Squared sum of all numerical values. NaN otherwise. |
| `Median` | number | No | Median of all numerical values. NaN otherwise. |
| `Average` | number | No | Average of all numerical values. NaN otherwise. |
| `Kurtosis` | number | No | Kurtosis of the numerical values. NaN otherwise. |
| `Skewness` | number | No | Skewness of the numerical values. NaN otherwise. |
| `FieldTags` | string[] | No | List of tags related to the field. |
| `Fractiles` | number[] | No | The .01, .05, .1, .25, .5, .75, .9, .95, .99 fractiles. Array of NaN otherwise. |
| `NegValues` | integer | No | Number of negative values |
| `PosValues` | integer | No | Number of positive values |
| `LastSorted` | string | No | For textual values the last sorted string. |
| `NullValues` | integer | No | Number of null values |
| `TextValues` | integer | No | Number of textual values |
| `ZeroValues` | integer | No | Number of zero values for numerical values |
| `FirstSorted` | string | No | For textual values the first sorted string. |
| `AvgStringLen` | number | No | Average string length of textual values. 0 otherwise. |
| `DataEvenness` | number | No | Data evenness aka Shannon's entropy normalized to [0,1] |
| `EmptyStrings` | integer | No | Number of empty strings |
| `MaxStringLen` | integer | No | Maximum string length of textual values. 0 otherwise. |
| `MinStringLen` | integer | No | Minimum string length of textual values. 0 otherwise. |
| `MostFrequent` | object[] | No | Three most frequent values and their frequencies |
| `NumberFormat` | object | No | Sets the formatting of a field. The properties of _qFieldAttributes_ and the formatting mechanism are described below.  ### Formatting mechanism The formatting mechanism depends on the type set in _qType,_ as shown below: <div class=note>In case of inconsistencies between the type and the format pattern, the format pattern takes precedence over the type.</div>  ### Type is DATE, TIME, TIMESTAMP or INTERVAL The following applies: * If a format pattern is defined in _qFmt_ , the formatting is as defined in _qFmt_ . * If _qFmt_ is empty, the formatting is defined by the number interpretation variables included at the top of the script ( _TimeFormat_ , _DateFormat_ , _TimeStampFormat_ ). * The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used.  ### Type is INTEGER The following applies: * If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the formatting mechanism uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). * If no format pattern is defined in _qFmt_ , no formatting is applied. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ and the number interpretation variables defined in the script are not used .  ### Type is REAL The following applies: * If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). * If no format pattern is defined in _qFmt_ , and if the value is almost an integer value (for example, 14,000012), the value is formatted as an integer. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used. * If no format pattern is defined in _qFmt_ , and if _qnDec_ is defined and not 0, the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used. * If no format pattern is defined in _qFmt_ , and if _qnDec_ is 0, the number of decimals is 14 and the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  ### Type is FIX The following applies: * If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). * If no format pattern is defined in _qFmt_ , the properties _qDec_ and _qnDec_ are used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  ### Type is MONEY The following applies: * If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of any script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ). * If no format pattern is defined in _qFmt_ , the engine uses the number interpretation variables included at the top of the script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ).  ### Type is ASCII No formatting, _qFmt_ is ignored. |
| `SumStringLen` | integer | No | Sum of all characters in strings in the field |
| `NumericValues` | integer | No | Number of numeric values |
| `DistinctValues` | integer | No | Number of distinct values |
| `DistinctTextValues` | integer | No | Number of distinct text values |
| `DistinctNumericValues` | integer | No | Number of distinct numeric values |
| `FrequencyDistribution` | object | No |  |

<details>
<summary>Properties of `MostFrequent`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `NumberFormat`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `FrequencyDistribution`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/data/metadata` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/data/metadata',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/data/metadata yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/data/metadata" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "fields": [
    {
      "hash": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "comment": "string",
      "cardinal": 42,
      "byte_size": 42,
      "is_hidden": true,
      "is_locked": true,
      "is_system": true,
      "is_numeric": true,
      "src_tables": [
        "string"
      ],
      "is_semantic": true,
      "total_count": 42,
      "distinct_only": true,
      "always_one_selected": true
    }
  ],
  "tables": [
    {
      "name": "string",
      "comment": "string",
      "is_loose": true,
      "byte_size": 42,
      "is_system": true,
      "no_of_rows": 42,
      "is_semantic": true,
      "no_of_fields": 42,
      "no_of_key_fields": 42
    }
  ],
  "reload_meta": {
    "hardware": {
      "total_memory": 42,
      "logical_cores": 42
    },
    "cpu_time_spent_ms": 42,
    "peak_memory_bytes": 42,
    "fullReloadPeakMemoryBytes": 42,
    "partialReloadPeakMemoryBytes": 42
  },
  "static_byte_size": 42,
  "has_section_access": true,
  "is_direct_query_mode": true,
  "tables_profiling_data": [
    {
      "NoOfRows": 42,
      "FieldProfiling": [
        {
          "Max": 42,
          "Min": 42,
          "Std": 42,
          "Sum": 42,
          "Name": "string",
          "Sum2": 42,
          "Median": 42,
          "Average": 42,
          "Kurtosis": 42,
          "Skewness": 42,
          "FieldTags": [
            "string"
          ],
          "Fractiles": [
            42
          ],
          "NegValues": 42,
          "PosValues": 42,
          "LastSorted": "string",
          "NullValues": 42,
          "TextValues": 42,
          "ZeroValues": 42,
          "FirstSorted": "string",
          "AvgStringLen": 42,
          "DataEvenness": 42,
          "EmptyStrings": 42,
          "MaxStringLen": 42,
          "MinStringLen": 42,
          "MostFrequent": [
            {
              "Symbol": {
                "Text": "string",
                "Number": 42
              },
              "Frequency": 42
            }
          ],
          "NumberFormat": {
            "Dec": "string",
            "Fmt": "string",
            "Thou": "string",
            "nDec": 10,
            "UseThou": 0
          },
          "SumStringLen": 42,
          "NumericValues": 42,
          "DistinctValues": 42,
          "DistinctTextValues": 42,
          "DistinctNumericValues": 42,
          "FrequencyDistribution": {
            "BinsEdges": [
              42
            ],
            "Frequencies": [
              42
            ],
            "NumberOfBins": 42
          }
        }
      ]
    }
  ]
}
```

---

### POST /api/v1/apps/{appId}/export

Exports a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `NoData` | boolean | No | The flag indicating if only object contents should be exported. |

#### Responses

##### 201

Created

##### 400

Bad request

##### 401

Unauthorized

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/export` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/export',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/export yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/export" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/apps/{appId}/insight-analyses

- **Rate Limit:** Special (500 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `accept-language` | string | No | language specified as an ISO-639-1 code. Defaults to 'en' (English). |

#### Responses

##### 200

The request is successfully processed and information about supported analyses is returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `compositions` | object[] | No |  |
| `supportsMasterItems` | boolean | No | If analysis can work with master items (default is true) |
| `requiresAutoCalendarPeriod` | boolean | No | Used for period-specific analyses to indicate the defined or available calendar period must be of type autoCalendar |
| `requiresDefinedAnalysisPeriod` | boolean | No | Used for period-specific analyses to indicate the measure must be associated with one or more analysis periods |
| `requiresAvailableAnalysisPeriod` | boolean | No | Used for period-specific analyses to indicate the temporal dimension must be associated with one or more analysis periods |

<details>
<summary>Properties of `compositions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dims` | object | No | Upper and lower bounds for items of specific classification types |
| `geos` | object | No | Upper and lower bounds for items of specific classification types |
| `msrs` | object | No | Upper and lower bounds for items of specific classification types |
| `items` | object | No | Upper and lower bounds for items of specific classification types |
| `temporals` | object | No | Upper and lower bounds for items of specific classification types |
| `description` | object | No |  |

<details>
<summary>Properties of `dims`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `geos`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `msrs`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporals`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `description`</summary>

_Properties truncated due to depth limit._

</details>

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
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request. The payload is not formed correctly.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

User is not authorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 422

Unprocessable entity. The payload contains fields
that are invalid, such as too long of a query.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/insight-analyses` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/insight-analyses',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/insight-analyses yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/insight-analyses" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "compositions": [
        {
          "dims": {
            "max": 42,
            "min": 42
          },
          "geos": {
            "max": 42,
            "min": 42
          },
          "msrs": {
            "max": 42,
            "min": 42
          },
          "items": {
            "max": 42,
            "min": 42
          },
          "temporals": {
            "max": 42,
            "min": 42
          },
          "description": {
            "long": "string",
            "short": "string"
          }
        }
      ],
      "supportsMasterItems": true,
      "requiresAutoCalendarPeriod": true,
      "requiresDefinedAnalysisPeriod": true,
      "requiresAvailableAnalysisPeriod": true
    }
  ],
  "links": {
    "next": {
      "href": "http://example.com"
    },
    "prev": {
      "href": "http://example.com"
    },
    "self": {
      "href": "http://example.com"
    }
  }
}
```

---

### POST /api/v1/apps/{appId}/insight-analyses/actions/recommend

- **Rate Limit:** Special (500 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `accept-language` | string | No | language specified as an ISO-639-1 code. Defaults to 'en' (English). |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object | No | Request payload can be of two types, using natural language query or consist of fields or master items and optional target analysis. In below examples, consider sales as a master item and product as field, so to get recommendations using sales and product, you can utilize below three approaches, also you can set language parameter in headers as part of accept-language. Examples: ``` {   'text': 'show me sales by product' } ``` ``` {   'fields': [     {       'name': 'product'     }   ],   'libItems': [     {       libId: 'NwQfJ'     }   ] } ``` ``` {   'fields': [     {       'name': 'product'     }   ],   'libItems': [     {       'libId': 'NwQfJ'     }   ],   'targetAnalysis': {     'id': 'rank-rank'   } } ``` |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RecommendNaturalLangQuery` | object | No |  |

<details>
<summary>Properties of `RecommendNaturalLangQuery`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | string | Yes | The NL query. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RecommendItems` | object | No |  |

<details>
<summary>Properties of `RecommendItems`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No | structure for providing fields in recommendation request, user can retrieve the fields using insight-analyses/model endpoint |
| `libItems` | object[] | No | structure for providing master items in recommendation request, user can retrieve the libId of master item using insight-analyses/model endpoint |
| `targetAnalysis` | object | No |  |

<details>
<summary>Properties of `fields`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `libItems`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `targetAnalysis`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 200

The request is successfully processed and recommendations are returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `nluInfo` | object[] | No | Contains break down of the asked question in the form of tokens with their classification. |
| `recAnalyses` | object[] | Yes |  |

<details>
<summary>Properties of `nluInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the token or phrase from query Enum: "dimension", "measure", "date" |
| `text` | string | No | Matching token or phrase from query |
| `type` | string | No | Type of token from query Enum: "field", "filter", "master_dimension", "master_measure", "custom_analysis" |
| `fieldName` | string | No | Qlik sense application field selected for given token or phrase |
| `fieldValue` | string | No | Filter value found from query |

</details>

<details>
<summary>Properties of `recAnalyses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `options` | object | No | (chart options + hypercube definition) |
| `analysis` | object | No |  |
| `chartType` | string | No | Chart type given to current recommendation Enum: "barchart", "combochart", "distributionplot", "kpi", "linechart", "map", "scatterplot", "table" |
| `relevance` | number | No | percentage of selected items in the analysis to the overall items passed to the endpoint |
| `parts` | object[] | No | part analyses (only for macro analyses) |

<details>
<summary>Properties of `analysis`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `parts`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad request. The payload is not formed correctly.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

User is not authorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 409

Invalid Business Logic

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 422

Unprocessable entity. The payload contains fields
that are invalid, such as too long of a query.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/insight-analyses/actions/recommend` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/insight-analyses/actions/recommend',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: 'string' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/insight-analyses/actions/recommend yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/insight-analyses/actions/recommend" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"text":"string"}'
```

**Example Response:**

```json
{
  "data": [
    {
      "nluInfo": [
        {
          "role": "dimension",
          "text": "string",
          "type": "field",
          "fieldName": "string",
          "fieldValue": "string"
        }
      ],
      "recAnalyses": [
        {
          "options": {},
          "analysis": {
            "title": "string",
            "analysis": "breakdown",
            "analysisGroup": "anomaly"
          },
          "chartType": "barchart",
          "relevance": 42,
          "parts": [
            {
              "options": {},
              "analysis": {
                "title": "string",
                "analysis": "breakdown",
                "analysisGroup": "anomaly"
              },
              "chartType": "barchart",
              "relevance": 42
            }
          ]
        }
      ]
    }
  ]
}
```

---

### GET /api/v1/apps/{appId}/insight-analyses/model

- **Rate Limit:** Special (500 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Responses

##### 200

The request is successfully processed and information about model is returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No |  |
| `masterItems` | object[] | No |  |
| `isLogicalModelEnabled` | boolean | No | if the analysis model is constructed based on a user-defined business-logic (as opposed to a default one) |
| `isDefinedLogicalModelValid` | boolean | No | set only if previous property is true, to indicate if the business logic passes validation |

<details>
<summary>Properties of `fields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | populated only for fields |
| `isHidden` | boolean | No | whether the field is hidden in business logic |
| `classifications` | string[] | No | classification defines the default role that attribute can play in an analysis Enum: "dimension", "measure", "temporal", "city", "address", "boolean", "country", "date", "email", "geographical", "geoPoint", "geoPolygon", "hour", "latitude", "monetary", "ordinal", "percentage", "postalCode", "quarter", "stateProvince", "timestamp", "week", "weekDay", "year", "yearDay" |
| `simplifiedClassifications` | string[] | No | Enum: "dimension", "measure", "temporal", "geographical" |

</details>

<details>
<summary>Properties of `masterItems`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `libId` | string | No | only available for master items |
| `caption` | string | No |  |
| `isHidden` | boolean | No | whether the master item is hidden in business logic |
| `classifications` | string[] | No | classification defines the default role that attribute can play in an analysis Enum: "dimension", "measure", "temporal", "city", "address", "boolean", "country", "date", "email", "geographical", "geoPoint", "geoPolygon", "hour", "latitude", "monetary", "ordinal", "percentage", "postalCode", "quarter", "stateProvince", "timestamp", "week", "weekDay", "year", "yearDay" |
| `simplifiedClassifications` | string[] | No | Enum: "dimension", "measure", "temporal", "geographical" |

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
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request. The payload is not formed correctly.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

User is not authorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 409

Invalid Business Logic

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 422

Unprocessable entity. The payload contains fields
that are invalid, such as too long of a query.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/insight-analyses/model` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/insight-analyses/model',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/insight-analyses/model yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/insight-analyses/model" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "fields": [
        {
          "name": "string",
          "isHidden": false,
          "classifications": [
            "dimension"
          ],
          "simplifiedClassifications": [
            "dimension"
          ]
        }
      ],
      "masterItems": [
        {
          "libId": "string",
          "caption": "string",
          "isHidden": false,
          "classifications": [
            "dimension"
          ],
          "simplifiedClassifications": [
            "dimension"
          ]
        }
      ],
      "isLogicalModelEnabled": true,
      "isDefinedLogicalModelValid": true
    }
  ],
  "links": {
    "next": {
      "href": "http://example.com"
    },
    "prev": {
      "href": "http://example.com"
    },
    "self": {
      "href": "http://example.com"
    }
  }
}
```

---

### GET /api/v1/apps/{appId}/media/files/{path}

Gets media content from file.
Returns a stream of bytes containing the media file content on success, or error if file is not found.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Unique application identifier. |
| `path` | string | Yes | Path to file content. |

#### Responses

##### 200

OK

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/media/files/{path}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/media/files/{path}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/media/files/{path} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/media/files/{path}" \
-H "Authorization: Bearer <access_token>" \
-o "output-file"
```

---

### PUT /api/v1/apps/{appId}/media/files/{path}

Stores the media content file.
Returns OK if the bytes containing the media file content were successfully stored, or error in case of failure, lack of permission or file already exists on the supplied path.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Unique application identifier. |
| `path` | string | Yes | Path to file content. |

#### Request Body

**Required**

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

#### Responses

##### 200

OK

##### 403

Forbidden

##### 404

Not Found

##### 409

Conflict

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}/media/files/{path}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/media/files/{path}',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId}/media/files/{path} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/media/files/{path}" \
-X PUT \
-H "Content-type: application/octet-stream" \
-H "Authorization: Bearer <access_token>" \
--data-binary' \
          '"@/path/to/file"
```

---

### DELETE /api/v1/apps/{appId}/media/files/{path}

Deletes a media content file or complete directory.
Returns OK if the bytes containing the media file (or the complete content of a directory) were successfully deleted, or error in case of failure or lack of permission.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Unique application identifier. |
| `path` | string | Yes | Path to file content. |

#### Responses

##### 200

OK

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}/media/files/{path}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/media/files/{path}',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId}/media/files/{path} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/media/files/{path}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/apps/{appId}/media/list/{path}

Lists media content.
Returns a JSON formatted array of strings describing the available media content or error if the optional path supplied is not found.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Unique application identifier. |
| `path` | string | Yes | The path to sub folder with static content relative to the root folder. Use empty path to access the root folder. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `show` | string | No | Optional. List output can include files and folders in different ways: * Not recursive, default if show option is not supplied or incorrectly specified, results in output with files and empty directories for the path specified only. * Recursive(r), use ?show=r or ?show=recursive, results in a recursive output with files, all empty folders are excluded. * All(a), use ?show=a or ?show=all, results in a recursive output with files and empty directories. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Content list items. |
| `library` | string | No | Content library name. |
| `subpath` | string | No | Content library relative listing path. Empty in case of root listed or representing actual subpath listed. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Unique content identifier. |
| `link` | string | No | Unique content link. |
| `name` | string | No | Content name. |
| `type` | string | No | Content type. |

</details>

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/media/list/{path}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/media/list/{path}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/media/list/{path} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/media/list/{path}" \
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
      "type": "string"
    }
  ],
  "library": "string",
  "subpath": "string"
}
```

---

### GET /api/v1/apps/{appId}/media/thumbnail

Gets media content from file currently used as application thumbnail.
Returns a stream of bytes containing the media file content on success, or error if file is not found.
The image selected as thumbnail is only updated when application is saved.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Unique application identifier. |

#### Responses

##### 200

OK

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/media/thumbnail` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/media/thumbnail',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/media/thumbnail yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/media/thumbnail" \
-H "Authorization: Bearer <access_token>" \
-o "output-file"
```

---

### POST /api/v1/apps/{appId}/objects/{objectId}/actions/change-owner

Sets owner on an app object.
The user must be the owner of the object.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |
| `objectId` | string | Yes | Identifier of the object. |

#### Request Body

**Required**

New owner.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `attributes` | object | No | App object attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application object privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * publish * exportdata * change_owner |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The object Id. |
| `name` | string | No | Object name. |
| `ownerId` | string | No | The object owner's Id. |
| `approved` | boolean | No | True if the object is approved. |
| `createdAt` | string | No | The date and time when the object was created. |
| `updatedAt` | string | No | The date and time when the object was modified. |
| `objectType` | string | No | The type of the object. |
| `description` | string | No | Object description. |
| `genericType` | string | No | Enum: "genericObject", "genericBookmark", "genericMeasure", "genericDimension", "genericVariable" |
| `publishedAt` | string | No | The date and time when the object was published, empty if unpublished. |

</details>

##### 400

Bad request

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/objects/{objectId}/actions/change-owner` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/objects/{objectId}/actions/change-owner',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/objects/{objectId}/actions/change-owner yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/objects/{objectId}/actions/change-owner" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"ownerId":"string"}'
```

**Example Response:**

```json
{
  "attributes": {
    "id": "string",
    "name": "string",
    "ownerId": "string",
    "approved": true,
    "createdAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "objectType": "string",
    "description": "string",
    "publishedAt": "2018-10-30T07:06:22Z"
  },
  "privileges": [
    "string"
  ]
}
```

---

### PUT /api/v1/apps/{appId}/owner

Changes owner of the app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

New owner.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}/owner` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/owner',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId}/owner yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/owner" \
-X PUT \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"ownerId":"string"}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/{appId}/placement

Retrieves the app size override for an app.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `createdAt` | string | No | The iso timestamp for when the override was configured. |
| `minEngineSize` | string | No | Enum: "0", "40", "60", "80", "120", "160", "200" |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/placement` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/placement',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/placement yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/placement" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "createdAt": "2018-10-30T07:06:22Z"
}
```

---

### PUT /api/v1/apps/{appId}/placement

Sets the app size override for an app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app |

#### Request Body

**Required**

The override information to be used for app placement.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `minEngineSize` | string | No | Enum: "0", "40", "60", "80", "120", "160", "200" |

#### Responses

##### 200

OK

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}/placement` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/placement',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId}/placement yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/placement" \
-X PUT \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{}'
```

---

### DELETE /api/v1/apps/{appId}/placement

Removes the app size override for an app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app |

#### Responses

##### 200

OK

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}/placement` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/placement',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId}/placement yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/placement" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/apps/{appId}/publish

Publishes a specific app to a managed space.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

Publish information for the app.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | string | No | Enum: "source", "target" |
| `moveApp` | boolean | No | The original is moved instead of copied. The current published state of all objects is kept. |
| `spaceId` | string | No | The managed space ID where the app will be published. |
| `attributes` | object | No |  |
| `originAppId` | string | No | If app is moved, originAppId needs to be provided. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name (title) of the application. |
| `description` | string | No | The description of the application. |

</details>

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/publish` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/publish',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/publish yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/publish" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"moveApp":false,"spaceId":"string","attributes":{"name":"string","description":"string"},"originAppId":"string"}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### PUT /api/v1/apps/{appId}/publish

Republishes a published app to a managed space.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

Republish information for the app.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | string | No | Enum: "source", "target" |
| `targetId` | string | No | The target ID to be republished. |
| `attributes` | object | No |  |
| `checkOriginAppId` | boolean | No | Validate that source app is same as originally published. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name (title) of the application. |
| `description` | string | No | The description of the application. |

</details>

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}/publish` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/publish',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId}/publish yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/publish" \
-X PUT \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"targetId":"string","attributes":{"name":"string","description":"string"},"checkOriginAppId":true}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/{appId}/reloads/logs

Retrieves the metadata about all script logs stored for an app.
Returns an array of ScriptLogMeta objects.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Array of scriptLogMeta. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `links` | object | No |  |
| `endTime` | string | No | Time when reload ended. |
| `success` | boolean | No | True if the reload was successful. |
| `duration` | integer | No | Duration of reload (ms). |
| `reloadId` | string | No | Reload identifier. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `log` | string | No | Provides a link to download the log file. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/reloads/logs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/reloads/logs',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/reloads/logs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/reloads/logs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "links": {
        "log": "string"
      },
      "endTime": "2018-10-30T07:06:22Z",
      "success": true,
      "duration": 42,
      "reloadId": "string"
    }
  ]
}
```

---

### GET /api/v1/apps/{appId}/reloads/logs/{reloadId}

Retrieves the log of a specific reload.
Returns the log as "text/plain; charset=UTF-8".

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |
| `reloadId` | string | Yes | Identifier of the reload. |

#### Responses

##### 200

OK

**Content-Type:** `text/plain`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/plain` | string | No |  |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/reloads/logs/{reloadId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/reloads/logs/{reloadId}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/reloads/logs/{reloadId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/reloads/logs/{reloadId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```text
string
```

---

### GET /api/v1/apps/{appId}/reloads/metadata/{reloadId}

Retrieves the app reload metadata list.
Reload metadata contains reload information, including reload id, duration, endtime and lineage load info. Data is available for the last 10 reloads of an application.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeSkipStoreReloads` | boolean | No | Include metadata for reloads ran with SkipStore flag set to true. Default: false |
| `limit` | string | No | Maximum number of records to return from this request. Default: 100 |
| `reloadId` | string | No | Identifier of the reload. Use empty reloadId to get all reloads. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Array of ReloadMeta. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | string | No | Time when reload ended. |
| `success` | boolean | No | true if the reload was successful. |
| `duration` | integer | No | Duration of reload (ms). |
| `reloadId` | string | No | Reload identifier. |
| `rowLimit` | integer | No | If greater than or equal 0, defines max number of rows loaded from a data source. |
| `appDbHash` | string | No | A Base64-encoded hash value of the new app database. |
| `skipStore` | boolean | No | Set to true to skip Store statements. The default value is false. |
| `storeHash` | string | No | A Base64-encoded hash value of all fields stored via the store statements. |
| `statements` | object[] | No | List of external loaded or stored statements. |
| `accessDbHash` | string | No | A Base64-encoded hash value of the new section access database. |
| `includeFiles` | object[] | No | Files brought into the script via include/mustInclude macros. |
| `loadFilesBytes` | integer | No |  |
| `isPartialReload` | boolean | No | True if the reload is a partial reload. |
| `storeFilesBytes` | integer | No |  |
| `loadExternalBytes` | integer | No |  |
| `loadDataFilesBytes` | integer | No |  |
| `storeDataFilesBytes` | integer | No |  |

<details>
<summary>Properties of `statements`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qri` | string | No | Resource Identifier. |
| `type` | string | No | Type of statement, e.g. Store/Load. |
| `label` | string | No | Label of the resource level node in lineage. |
| `dataSize` | integer | No | Data loaded from the network (bytes). |
| `duration` | integer | No | Duration of data generation (ms). |
| `nbrOfRows` | integer | No | Number of rows loaded. |
| `tableName` | string | No | Name of the source table in lineage. |
| `connection` | string | No | The connection name. |
| `nbrOfFields` | integer | No | Number of fields loaded. |
| `connectionId` | string | No | Connection ID. |
| `partialReloadOperation` | string | No | Partial load operation. e.g. add/replace/update/merge. n/a when not in partial load mode. |

</details>

<details>
<summary>Properties of `includeFiles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qri` | string | No | File QRI resource identifier. |
| `path` | string | No | File location within the connection. |
| `connection` | string | No | The connection name. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/reloads/metadata/{reloadId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/reloads/metadata/{reloadId}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/reloads/metadata/{reloadId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/reloads/metadata/{reloadId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "endTime": "2018-10-30T07:06:22Z",
      "success": true,
      "duration": 42,
      "reloadId": "string",
      "rowLimit": -1,
      "appDbHash": "string",
      "skipStore": false,
      "storeHash": "string",
      "statements": [
        {
          "qri": "string",
          "type": "string",
          "label": "string",
          "dataSize": 42,
          "duration": 42,
          "nbrOfRows": 42,
          "tableName": "string",
          "connection": "string",
          "nbrOfFields": 42,
          "connectionId": "string",
          "partialReloadOperation": "string"
        }
      ],
      "accessDbHash": "string",
      "includeFiles": [
        {
          "qri": "string",
          "path": "string",
          "connection": "string"
        }
      ],
      "loadFilesBytes": 42,
      "isPartialReload": true,
      "storeFilesBytes": 42,
      "loadExternalBytes": 42,
      "loadDataFilesBytes": 42,
      "storeDataFilesBytes": 42
    }
  ]
}
```

---

### GET /api/v1/apps/{appId}/report-filters

List all filters that are present in the given app. Filters allow to reduce the app data visible in a report output. Each filter can contain definitions on one or multiple fields.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filterTypes` | string[] | Yes | The filter type (REP, SUB). REP stands for report bookmark, SUB for subscription bookmark. Enum: "REP", "SUB" |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive. The following fields support the `co` (contains) operator: `name`, `description` The following fields support the `eq` (equals) operator: `id`, `ownerId` Example: (name co "query1" or description co "query2") and ownerId eq "123" |
| `limit` | integer | No | Limit the returned result set |
| `loadType` | string | No | Load type expressing the kind of request, eg. interactive for report requests from the Web UI, batch for scheduled report generation. Enum: "interactive", "batch" |
| `page` | string | No | If present, the cursor that starts the page of data that is returned. |
| `sort` | string[] | No | Sorting parameters. Enum: "+ownerId", "-ownerId", "-name", "+name", "+description", "-description", "+createdAt", "-createdAt", "+updatedAt", "-updatedAt" |

#### Responses

##### 200

The filters have been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | a list of filters containing all the filters properties (like name,description...) except the filter definition (like FilterV1_0) |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The filter ID (bookmarkId) |
| `name` | string | No | The filter name. |
| `ownerId` | string | No | The user that owns the filter, if missing the same as the request user. |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `filterType` | string | No | Enum: "REP", "SUB" |
| `filterV1_0` | object | No |  |
| `description` | string | No | The filter description. |
| `filterVersion` | string | No | Enum: "filter-1.0", "filter-2.0" |

<details>
<summary>Properties of `filterV1_0`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object[] | No | The filter variables. |
| `fieldsByState` | object | No | Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |

<details>
<summary>Properties of `variables`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/report-filters` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/report-filters yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "c61841ac-7b35-4434-aa74-4421f10fc68e",
      "name": "Filter 1",
      "ownerId": "649173fbc8ffcfde27412b99",
      "createdAt": "2023-08-09T08:19:37.577Z",
      "updatedAt": "2023-08-09T08:19:37.577Z",
      "filterType": "REP",
      "filterV1_0": {
        "fieldsByState": {
          "$": [
            {
              "name": "Country",
              "values": [
                {
                  "valueType": "string",
                  "valueAsText": "1-Argentina"
                },
                {
                  "valueType": "string",
                  "valueAsText": "4-Brazil"
                }
              ],
              "overrideValues": false,
              "selectExcluded": false
            },
            {
              "name": "Order number",
              "values": [
                {
                  "valueType": "number",
                  "valueAsText": "61300",
                  "valueAsNumber": 61300
                }
              ],
              "overrideValues": false,
              "selectExcluded": false
            }
          ]
        }
      },
      "description": "This is the filter description",
      "filterVersion": "filter-1.0"
    }
  ],
  "links": {
    "next": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    },
    "prev": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    },
    "self": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    }
  }
}
```

---

### POST /api/v1/apps/{appId}/report-filters

Creates a new report filter which is used to re-apply selections, variables, patches to an engine session.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Request Body

**Required**

The filter definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The filter name. |
| `appId` | string | No | The App ID. |
| `ownerId` | string | No | The user that owns the filter, if missing the same as the request user. |
| `filterType` | string | Yes | Enum: "REP", "SUB" |
| `filterV1_0` | object | No |  |
| `description` | string | No | The filter description. |
| `filterVersion` | string | Yes | Enum: "filter-1.0", "filter-2.0" |

<details>
<summary>Properties of `filterV1_0`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object[] | No | The filter variables. |
| `fieldsByState` | object | No | Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `value` | string | No |  |
| `evaluate` | boolean | No |  |

</details>

</details>

#### Responses

##### 201

The filter has been successfully created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The filter ID (bookmarkId). |
| `name` | string | No | The filter name. |
| `ownerId` | string | No | The user that owns the filter, if missing the same as the request user. |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `filterType` | string | No | Enum: "REP", "SUB" |
| `filterV1_0` | object | No |  |
| `description` | string | No | The filter description. |
| `filterVersion` | string | No | Enum: "filter-1.0", "filter-2.0" |

<details>
<summary>Properties of `filterV1_0`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object[] | No | The filter variables. |
| `fieldsByState` | object | No | Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `value` | string | No |  |
| `evaluate` | boolean | No |  |

</details>

</details>

##### 400

Bad request, malformed syntax, errors in params or the report request is not valid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 409

Filter name conflict.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/report-filters` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Filter sample',
      filterType: 'REP',
      filterV1_0: {
        fieldsByState: {
          $: [
            {
              name: 'Country',
              values: [
                {
                  valueType: 'string',
                  valueAsText: '1-Argentina',
                },
                {
                  valueType: 'string',
                  valueAsText: '4-Brazil',
                },
              ],
              overrideValues: false,
              selectExcluded: false,
            },
            {
              name: 'Order number',
              values: [
                {
                  valueType: 'number',
                  valueAsText: '61300',
                  valueAsNumber: 61300,
                },
              ],
              overrideValues: false,
              selectExcluded: false,
            },
          ],
        },
      },
      description: 'this is a filter sample',
      filterVersion: 'filter-1.0',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/report-filters yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Filter sample","filterType":"REP","filterV1_0":{"fieldsByState":{"$":[{"name":"Country","values":[{"valueType":"string","valueAsText":"1-Argentina"},{"valueType":"string","valueAsText":"4-Brazil"}],"overrideValues":false,"selectExcluded":false},{"name":"Order number","values":[{"valueType":"number","valueAsText":"61300","valueAsNumber":61300}],"overrideValues":false,"selectExcluded":false}]}},"description":"this is a filter sample","filterVersion":"filter-1.0"}'
```

**Example Response:**

```json
{
  "id": "c61841ac-7b35-4434-aa74-4421f10fc68e",
  "name": "Filter 1",
  "ownerId": "649173fbc8ffcfde27412b99",
  "createdAt": "2023-08-09T08:19:37.577Z",
  "updatedAt": "2023-08-09T08:19:37.577Z",
  "filterType": "REP",
  "filterV1_0": {
    "fieldsByState": {
      "$": [
        {
          "name": "Country",
          "values": [
            {
              "valueType": "string",
              "valueAsText": "1-Argentina"
            },
            {
              "valueType": "string",
              "valueAsText": "4-Brazil"
            }
          ],
          "overrideValues": false,
          "selectExcluded": false
        },
        {
          "name": "Order number",
          "values": [
            {
              "valueType": "number",
              "valueAsText": "61300",
              "valueAsNumber": 61300
            }
          ],
          "overrideValues": false,
          "selectExcluded": false
        }
      ]
    }
  },
  "description": "This is the filter description",
  "filterVersion": "filter-1.0"
}
```

---

### GET /api/v1/apps/{appId}/report-filters/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |
| `id` | string | Yes | The filter id identifier (bookmarkId). |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `loadType` | string | No | Load type expressing the kind of request, eg. interactive for report requests from the Web UI, batch for scheduled report generation. Enum: "interactive", "batch" |

#### Responses

##### 200

The filter has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The filter ID (bookmarkId). |
| `name` | string | No | The filter name. |
| `ownerId` | string | No | The user that owns the filter, if missing the same as the request user. |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `filterType` | string | No | Enum: "REP", "SUB" |
| `filterV1_0` | object | No |  |
| `description` | string | No | The filter description. |
| `filterVersion` | string | No | Enum: "filter-1.0", "filter-2.0" |

<details>
<summary>Properties of `filterV1_0`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `variables` | object[] | No | The filter variables. |
| `fieldsByState` | object | No | Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |

<details>
<summary>Properties of `variables`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `value` | string | No |  |
| `evaluate` | boolean | No |  |

</details>

</details>

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/report-filters/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/report-filters/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "c61841ac-7b35-4434-aa74-4421f10fc68e",
  "name": "Filter 1",
  "ownerId": "649173fbc8ffcfde27412b99",
  "createdAt": "2023-08-09T08:19:37.577Z",
  "updatedAt": "2023-08-09T08:19:37.577Z",
  "filterType": "REP",
  "filterV1_0": {
    "fieldsByState": {
      "$": [
        {
          "name": "Country",
          "values": [
            {
              "valueType": "string",
              "valueAsText": "1-Argentina"
            },
            {
              "valueType": "string",
              "valueAsText": "4-Brazil"
            }
          ],
          "overrideValues": false,
          "selectExcluded": false
        },
        {
          "name": "Order number",
          "values": [
            {
              "valueType": "number",
              "valueAsText": "61300",
              "valueAsNumber": 61300
            }
          ],
          "overrideValues": false,
          "selectExcluded": false
        }
      ]
    }
  },
  "description": "This is the filter description",
  "filterVersion": "filter-1.0"
}
```

---

### PATCH /api/v1/apps/{appId}/report-filters/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |
| `id` | string | Yes | The filter id identifier (bookmarkId). |

#### Request Body

**Required**

The filter definition that will replace the existing one.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | operation (replace). Enum: "replace" |
| `path` | string | Yes | A JSON Pointer path (/). Enum: "/filter" |
| `value` | object | Yes | The value to be used for this operation. The properties that cannot be patched include id, filterType, appId |

<details>
<summary>Properties of `value`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Filter` | object | No |  |

<details>
<summary>Properties of `Filter`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The filter name. |
| `ownerId` | string | No | The user that owns the filter, if missing the same as the request user. |
| `filterV1_0` | object | No |  |
| `description` | string | No | The filter description. |
| `filterVersion` | string | No | Enum: "filter-1.0", "filter-2.0" |

<details>
<summary>Properties of `filterV1_0`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 204

The filter has been successfully patched.

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 409

Filter name conflict. A filter with the same name already exists.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/apps/{appId}/report-filters/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/filter',
        value: {
          Filter: {
            name: 'Filter 1',
            ownerId: '649173fbc8ffcfde27412b99',
            filterV1_0: {
              fieldsByState: {
                $: [
                  {
                    name: 'Country',
                    values: [
                      {
                        valueType: 'string',
                        valueAsText:
                          '1-Argentina',
                      },
                      {
                        valueType: 'string',
                        valueAsText: '4-Brazil',
                      },
                    ],
                    overrideValues: false,
                    selectExcluded: false,
                  },
                  {
                    name: 'Order number',
                    values: [
                      {
                        valueType: 'number',
                        valueAsText: '61300',
                        valueAsNumber: 61300,
                      },
                    ],
                    overrideValues: false,
                    selectExcluded: false,
                  },
                ],
              },
            },
            description:
              'This is the filter description',
            filterVersion: 'filter-1.0',
          },
        },
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/apps/{appId}/report-filters/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/filter","value":{"Filter":{"name":"Filter 1","ownerId":"649173fbc8ffcfde27412b99","filterV1_0":{"fieldsByState":{"$":[{"name":"Country","values":[{"valueType":"string","valueAsText":"1-Argentina"},{"valueType":"string","valueAsText":"4-Brazil"}],"overrideValues":false,"selectExcluded":false},{"name":"Order number","values":[{"valueType":"number","valueAsText":"61300","valueAsNumber":61300}],"overrideValues":false,"selectExcluded":false}]}},"description":"This is the filter description","filterVersion":"filter-1.0"}}}]'
```

---

### DELETE /api/v1/apps/{appId}/report-filters/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |
| `id` | string | Yes | The filter id identifier (bookmarkId). |

#### Responses

##### 204

The filter has been successfully deleted.

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}/report-filters/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId}/report-filters/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/apps/{appId}/report-filters/actions/count

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Qlik Sense app identifier |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filterTypes` | string[] | Yes | The filter type (REP, SUB). REP stands for report bookmark, SUB for subscription bookmark. Enum: "REP", "SUB" |

#### Responses

##### 200

The count of filters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | number | No | The total number of filters. |

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 403

Forbidden, user lacks sufficient permissions to access the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error occured during the Filter creation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-404000" Not found. The server can not find the requested resource. - "REP-409043" Filter name conflict. The filter name must be unique. - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429016" Exceeded max session tenant quota per day. - "REP-500000" Fail to resolve resource. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-504042" Context deadline exceeded applying selections of the Filter. - "REP-500031" Error creating bookmark. - "REP-404032" Bookmark not found after creating the bookmark. - "REP-500033" Error destroying bookmark. - "REP-404033" Bookmark not found destroying the bookmark. - "REP-409043" Dupliacate bookmark name. - "REP-429034" Filters quota exceeded. - "REP-400044" Missing or renamed field. - "REP-403049" Report filter access not allowed. |
| `title` | string | Yes | A summary in english explaining what went wrong. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/report-filters/actions/count` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/report-filters/actions/count',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/report-filters/actions/count yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/report-filters/actions/count" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "total": 20
}
```

---

### GET /api/v1/apps/{appId}/scripts

Retrieves the script history for an app.
Returns information about the saved versions of the script in a list sorted with latest first.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | A scim filter expression defining which script versions should be retrieved. Filterable fields are: * ScriptId * ModifiedTime * ModifierId |
| `limit` | string | No | Maximum number of records to return from this request. |
| `page` | string | No | Opaque definition of which page of the result set to return. Returned from a previous call using the same filter. Not yet supported. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `links` | object | No |  |
| `scripts` | object[] | No | Script versions metadata. |
| `privileges` | string[] | No |  |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `scripts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No | Script size. |
| `scriptId` | string | No | Script id. |
| `modifierId` | string | No | User last modifying script version. |
| `modifiedTime` | string | No | Script version last modification time. |
| `versionMessage` | string | No | Description of this script version |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/scripts` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/scripts',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/scripts yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/scripts" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    }
  },
  "scripts": [
    {
      "size": 42,
      "scriptId": "string",
      "modifierId": "string",
      "modifiedTime": "string",
      "versionMessage": "string"
    }
  ],
  "privileges": [
    "string"
  ]
}
```

---

### POST /api/v1/apps/{appId}/scripts

Sets script for an app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

The script to set.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `script` | string | No | Script text. |
| `versionMessage` | string | No | Description of this script version |

#### Responses

##### 200

OK

##### 403

Forbidden

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{appId}/scripts` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/scripts',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{appId}/scripts yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/scripts" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"script":"string","versionMessage":"string"}'
```

---

### GET /api/v1/apps/{appId}/scripts/{id}

Retrieves a version of the script for an app.
Returns the script text.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |
| `id` | string | Yes | Identifier of the script version, or 'current' for retrieving the current version. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `script` | string | No | Script text. |
| `versionMessage` | string | No | Description of this script version |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{appId}/scripts/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/scripts/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{appId}/scripts/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/scripts/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "script": "string",
  "versionMessage": "string"
}
```

---

### PATCH /api/v1/apps/{appId}/scripts/{id}

Updates a specific version of the script for an app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |
| `id` | string | Yes | Identifier of the script version. |

#### Request Body

**Required**

Array of patches for the object ScriptVersion.
<div class=note>Patches have limited functionality for this object. Only /versionMessage can be modified using operations add, remove and replace.</div>

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Op` | string | No | Enum: "add", "remove", "replace" |
| `Path` | string | No | Path to the property to add, remove or replace. |
| `Value` | string | No | This parameter is not used in a remove operation. Corresponds to the value of the property to add or to the new value of the property to update. Examples: "false", "2", "\"New title\"" |

#### Responses

##### 200

OK

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/apps/{appId}/scripts/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/scripts/{id}',
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
# qlik-cli has not implemented support for PATCH /api/v1/apps/{appId}/scripts/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/scripts/{id}" \
-X PATCH \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '[{"Path":"string","Value":"string"}]'
```

---

### DELETE /api/v1/apps/{appId}/scripts/{id}

Deletes a specific version of the script for an app.
Fails if the supplied id is the current version.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |
| `id` | string | Yes | Identifier of the script version |

#### Responses

##### 200

OK

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}/scripts/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/scripts/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId}/scripts/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/scripts/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### PUT /api/v1/apps/{appId}/space

Sets space on a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Request Body

**Required**

New space.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/apps/{appId}/space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/space',
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
# qlik-cli has not implemented support for PUT /api/v1/apps/{appId}/space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/space" \
-X PUT \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"spaceId":"string"}'
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### DELETE /api/v1/apps/{appId}/space

Removes space from a specific app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | Identifier of the app. |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/apps/{appId}/space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{appId}/space',
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
# qlik-cli has not implemented support for DELETE /api/v1/apps/{appId}/space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{appId}/space" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/{guid}/evaluations _(deprecated)_

Find all evaluations for an app GUID.
Supports paging via next, prev which are sent in the response body


- **Replaced by:** "GET:/analytics/apps/{guid}/evaluations"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | string | Yes | The app guid. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | Get the full data of the evaluation |
| `fileMode` | boolean | No | Add file transfer headers to response |
| `format` | string | No | Specify output format, currently supported are 'json' and 'xml' |
| `limit` | integer | No | Number of results to return per page. |
| `next` | string | No | The app evaluation id to get next page from |
| `prev` | string | No | The app evaluation id to get previous page from |
| `sort` | string | No | Property to sort list on |

#### Responses

##### 200

Evaluation(s) retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `sheetId` | string | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `metadata` | object | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `sheetTitle` | string | No |  |

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheets` | object[] | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `sheets`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objNoCache`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `dedicated` | boolean | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/{guid}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{guid}/evaluations',
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
# qlik-cli has not implemented support for GET /api/v1/apps/{guid}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{guid}/evaluations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "5ecb5e65028d1f0001a98071",
      "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
      "ended": "2022-02-09T06:58:40.575Z",
      "events": [
        {
          "details": "An object failed",
          "sheetId": "gregFG",
          "objectId": "adfRFr",
          "severity": "warning",
          "errorCode": "ERR-GOPHERCISER",
          "objectType": "linechart",
          "sheetTitle": "mysheet",
          "objectTitle": "profit",
          "objectVisualization": "linechart"
        }
      ],
      "result": {
        "sheets": [
          {
            "sheet": {
              "id": "fjETFn",
              "title": "my chart",
              "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
              "objectType": "table",
              "timeoutStatusCode": "CALC-TIMEOUT",
              "responseTimeSeconds": 12.3
            },
            "objectCount": 1,
            "sheetObjects": [
              {
                "id": "fjETFn",
                "title": "my chart",
                "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
                "objectType": "table",
                "timeoutStatusCode": "CALC-TIMEOUT",
                "responseTimeSeconds": 12.3
              }
            ]
          }
        ],
        "rowCount": 20000,
        "objNoCache": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "sheetCount": 5,
        "objectCount": 33,
        "objSlowCached": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "objMemoryLimit": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "memoryLimitStatusCode": "OUT-OF-MEMORY"
          }
        ],
        "documentSizeMiB": 12.3,
        "objSlowUncached": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ],
        "hasSectionAccess": false,
        "topFieldsByBytes": [
          {
            "name": "a",
            "byte_size": 1234,
            "is_system": false
          }
        ],
        "topTablesByBytes": [
          {
            "name": "a",
            "byte_size": 1234,
            "is_system": false
          }
        ],
        "objSingleThreaded": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "cpuQuotient1": 12.3
          }
        ]
      },
      "status": "finished",
      "appName": "my app",
      "details": {
        "errors": [
          "this is an error"
        ],
        "warnings": [
          "this is a warning"
        ],
        "dedicated": false,
        "objectMetrics": {},
        "engineHasCache": false,
        "concurrentReload": false
      },
      "sheetId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
      "started": "2022-02-09T06:58:40.575Z",
      "version": 1,
      "metadata": {
        "reloadmeta": {
          "cpuspent": "123983",
          "peakmemorybytes": 112
        },
        "amountofrows": 1423423234,
        "amountoffields": 12,
        "amountoftables": 7,
        "staticbytesize": 1444234,
        "hassectionaccess": false,
        "amountoffieldvalues": 144423433,
        "amountofcardinalfieldvalues": 14442
      },
      "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
      "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
      "timestamp": "2022-02-09T06:58:40.575Z",
      "sheetTitle": "my sheet"
    }
  ],
  "links": {
    "next": {
      "href": "/api/v1/evaluations/appId=a84c22cf-31e5-41fe-9e8f-544b85513484&prev=5f5201908b3fc5fc132dbd35"
    },
    "prev": {
      "href": "/api/v1/evaluations/appId=a84c22cf-31e5-41fe-9e8f-544b85513484&prev=5f5201908b3fc5fc132dbd35"
    }
  }
}
```

---

### POST /api/v1/apps/{guid}/evaluations _(deprecated)_

Queue an app evaluation by its app guid.


- **Replaced by:** "POST:/analytics/apps/{guid}/evaluations"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | string | Yes | Guid of the app. |

#### Responses

##### 201

App evaluation queued.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `sheetId` | string | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `metadata` | object | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `sheetTitle` | string | No |  |

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheets` | object[] | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `sheets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuQuotient1` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `dedicated` | boolean | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 400

Bad request, incorrect body.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 403

User lacks permissions to evaluate app.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 404

App does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/{guid}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/{guid}/evaluations',
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
# qlik-cli has not implemented support for POST /api/v1/apps/{guid}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/{guid}/evaluations" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "events": [
    {
      "details": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "sheets": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuQuotient1": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "dedicated": false,
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "sheetId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "metadata": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  },
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "sheetTitle": "my sheet"
}
```

---

### GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid} _(deprecated)_

Accepts two evaluation ids and returns a comparison denoting the differences between the two.


- **Replaced by:** "GET:/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `baseid` | string | Yes | Id of the baseline evaluation |
| `comparisonid` | string | Yes | Id of the comparison evaluation |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | Get the full list of comparisons including non-significant diffs |
| `format` | string | No | Specify output format, currently supported are 'json' and 'xml' |

#### Responses

##### 200

Comparison executed successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `objHeavy` | object | No |  |
| `rowCount` | object | No |  |
| `objNoCache` | object | No |  |
| `sheetCount` | object | No |  |
| `fileSizeMib` | object | No |  |
| `objectCount` | object | No |  |
| `maxMemoryMib` | object | No |  |
| `sheetsCached` | object | No |  |
| `objSlowCached` | object | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object | No |  |
| `documentSizeMib` | object | No |  |
| `objSlowUncached` | object | No |  |
| `dataModelSizeMib` | object | No |  |
| `hasSectionAccess` | object | No |  |
| `topFieldsByBytes` | object | No |  |
| `topTablesByBytes` | object | No |  |
| `objSingleThreaded` | object | No |  |
| `appOpenTimeSeconds` | object | No |  |

<details>
<summary>Properties of `objHeavy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `rowCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `sheetCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `fileSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objectCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `maxMemoryMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `baselineMemoryLimitStatusCode` | string | No |  |
| `comparisonMemoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `documentSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `dataModelSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `hasSectionAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | boolean | No |  |
| `comparison` | boolean | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `appOpenTimeSeconds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "objHeavy": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "rowCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objNoCache": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "sheetCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "fileSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objectCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "maxMemoryMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "sheetsCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objSlowCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objMemoryLimit": [
    {
      "id": "fjETFn",
      "title": "my chart",
      "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
      "objectType": "table",
      "dataSourceStatus": "full",
      "baselineMemoryLimitStatusCode": "OUT-OF-MEMORY",
      "comparisonMemoryLimitStatusCode": "OUT-OF-MEMORY"
    }
  ],
  "sheetsUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "documentSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objSlowUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "dataModelSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "hasSectionAccess": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": false,
    "comparison": true
  },
  "topFieldsByBytes": {
    "list": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "topTablesByBytes": {
    "list": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "objSingleThreaded": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "appOpenTimeSeconds": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  }
}
```

---

### GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download _(deprecated)_

Accepts two evaluation ids and downloads a log, in XML format, denoting the differences between the two.


- **Replaced by:** "GET:/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `baseid` | string | Yes | Id of the baseline evaluation |
| `comparisonid` | string | Yes | Id of the comparison evaluation |

#### Responses

##### 200

Comparison executed successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `objHeavy` | object | No |  |
| `rowCount` | object | No |  |
| `objNoCache` | object | No |  |
| `sheetCount` | object | No |  |
| `fileSizeMib` | object | No |  |
| `objectCount` | object | No |  |
| `maxMemoryMib` | object | No |  |
| `sheetsCached` | object | No |  |
| `objSlowCached` | object | No |  |
| `objMemoryLimit` | object[] | No |  |
| `sheetsUncached` | object | No |  |
| `documentSizeMib` | object | No |  |
| `objSlowUncached` | object | No |  |
| `dataModelSizeMib` | object | No |  |
| `hasSectionAccess` | object | No |  |
| `topFieldsByBytes` | object | No |  |
| `topTablesByBytes` | object | No |  |
| `objSingleThreaded` | object | No |  |
| `appOpenTimeSeconds` | object | No |  |

<details>
<summary>Properties of `objHeavy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuSeconds1` | object | No |  |
| `cpuSeconds2` | object | No |  |
| `cpuQuotient1` | object | No |  |
| `cpuQuotient2` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `cpuSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cpuQuotient2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `rowCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `sheetCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `fileSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objectCount`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `maxMemoryMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `sheetsCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `baselineMemoryLimitStatusCode` | string | No |  |
| `comparisonMemoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `sheetsUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `documentSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `dataModelSizeMib`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

<details>
<summary>Properties of `hasSectionAccess`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | boolean | No |  |
| `comparison` | boolean | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `cardinal` | object | No |  |
| `total_count` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `cardinal`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `total_count`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | object | No |  |
| `is_system` | object | No |  |
| `no_of_rows` | object | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |

<details>
<summary>Properties of `byte_size`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `is_system`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `no_of_rows`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `list` | object[] | No |  |
| `absoluteDiffAsc` | object[] | No |  |
| `relativeDiffAsc` | object[] | No |  |
| `absoluteDiffDesc` | object[] | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `relativeDiffDesc` | object[] | No |  |

<details>
<summary>Properties of `list`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffAsc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `absoluteDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `relativeDiffDesc`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `dataSourceStatus` | string | No | Enum: "full", "none", "baselinemissing", "comparisonmissing" |
| `responseTimeSeconds1` | object | No |  |
| `responseTimeSeconds2` | object | No |  |

<details>
<summary>Properties of `responseTimeSeconds1`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `responseTimeSeconds2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `appOpenTimeSeconds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | number | No |  |
| `trend` | string | No |  |
| `absoluteDiff` | number | No |  |
| `baseline` | number | No |  |
| `comparison` | number | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download',
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
# qlik-cli has not implemented support for GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "objHeavy": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "cpuQuotient2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "rowCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "objNoCache": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "sheetCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "fileSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objectCount": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1,
    "comparison": 2
  },
  "maxMemoryMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "sheetsCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objSlowCached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "objMemoryLimit": [
    {
      "id": "fjETFn",
      "title": "my chart",
      "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
      "objectType": "table",
      "dataSourceStatus": "full",
      "baselineMemoryLimitStatusCode": "OUT-OF-MEMORY",
      "comparisonMemoryLimitStatusCode": "OUT-OF-MEMORY"
    }
  ],
  "sheetsUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "documentSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "objSlowUncached": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "dataModelSizeMib": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  },
  "hasSectionAccess": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": false,
    "comparison": true
  },
  "topFieldsByBytes": {
    "list": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "cardinal": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "total_count": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "topTablesByBytes": {
    "list": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "relativeDiffAsc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "absoluteDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "name": "a",
        "byte_size": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "is_system": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": false,
          "comparison": true
        },
        "no_of_rows": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1,
          "comparison": 2
        },
        "dataSourceStatus": "full"
      }
    ]
  },
  "objSingleThreaded": {
    "list": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "relativeDiffAsc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "absoluteDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ],
    "dataSourceStatus": "full",
    "relativeDiffDesc": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "dataSourceStatus": "full",
        "responseTimeSeconds1": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        },
        "responseTimeSeconds2": {
          "diff": 0.5,
          "trend": "up",
          "absoluteDiff": 2.5,
          "baseline": 1.1,
          "comparison": 2.2,
          "baselineTimeoutStatusCode": "CALC-TIMEOUT",
          "comparisonTimeoutStatusCode": "CALC-TIMEOUT"
        }
      }
    ]
  },
  "appOpenTimeSeconds": {
    "diff": 0.5,
    "trend": "up",
    "absoluteDiff": 2.5,
    "baseline": 1.1,
    "comparison": 2.2
  }
}
```

---

### GET /api/v1/apps/evaluations/{id} _(deprecated)_

Find an evaluation by a specific id.


- **Replaced by:** "GET:/analytics/apps/evaluations/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Id of the desired evaluation. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `all` | boolean | No | Get the full data of the evaluation |
| `format` | string | No | Specify output format, currently supported are 'json' and 'xml' |

#### Responses

##### 200

Evaluation(s) retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `sheetId` | string | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `metadata` | object | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `sheetTitle` | string | No |  |

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheets` | object[] | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `sheets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuQuotient1` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `dedicated` | boolean | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/evaluations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/evaluations/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/apps/evaluations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/evaluations/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "events": [
    {
      "details": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "sheets": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuQuotient1": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "dedicated": false,
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "sheetId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "metadata": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  },
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "sheetTitle": "my sheet"
}
```

---

### GET /api/v1/apps/evaluations/{id}/actions/download _(deprecated)_

Find and download an evaluation log by a specific evaluation id.


- **Replaced by:** "GET:/analytics/apps/evaluations/{id}/actions/download"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. Replaced by namespaced API

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Id of the desired evaluation. |

#### Responses

##### 200

Evaluation(s) retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `appId` | string | No |  |
| `ended` | string | No |  |
| `events` | object[] | No |  |
| `result` | object | No |  |
| `status` | string | No |  |
| `appName` | string | No |  |
| `details` | object | No |  |
| `sheetId` | string | No |  |
| `started` | string | No |  |
| `version` | number | No |  |
| `metadata` | object | No |  |
| `tenantId` | string | No |  |
| `appItemId` | string | No |  |
| `timestamp` | string | No |  |
| `sheetTitle` | string | No |  |

<details>
<summary>Properties of `events`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | string | No |  |
| `sheetId` | string | No |  |
| `objectId` | string | No |  |
| `severity` | string | No |  |
| `errorCode` | string | No |  |
| `objectType` | string | No |  |
| `sheetTitle` | string | No |  |
| `objectTitle` | string | No |  |
| `objectVisualization` | string | No |  |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheets` | object[] | No |  |
| `rowCount` | number | No |  |
| `objNoCache` | object[] | No |  |
| `sheetCount` | number | No |  |
| `objectCount` | number | No |  |
| `objSlowCached` | object[] | No |  |
| `objMemoryLimit` | object[] | No |  |
| `documentSizeMiB` | number | No |  |
| `objSlowUncached` | object[] | No |  |
| `hasSectionAccess` | boolean | No |  |
| `topFieldsByBytes` | object[] | No |  |
| `topTablesByBytes` | object[] | No |  |
| `objSingleThreaded` | object[] | No |  |

<details>
<summary>Properties of `sheets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheet` | object | No |  |
| `objectCount` | number | No |  |
| `sheetObjects` | object[] | No |  |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetObjects`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `objNoCache`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objSlowCached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `objMemoryLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `memoryLimitStatusCode` | string | No |  |

</details>

<details>
<summary>Properties of `objSlowUncached`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `timeoutStatusCode` | string | No |  |
| `responseTimeSeconds` | number | No |  |

</details>

<details>
<summary>Properties of `topFieldsByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `topTablesByBytes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `byte_size` | number | No |  |
| `is_system` | boolean | No |  |

</details>

<details>
<summary>Properties of `objSingleThreaded`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `title` | string | No |  |
| `sheetId` | string | No |  |
| `objectType` | string | No |  |
| `cpuQuotient1` | number | No |  |

</details>

</details>

<details>
<summary>Properties of `details`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | string[] | No |  |
| `warnings` | string[] | No |  |
| `dedicated` | boolean | No |  |
| `objectMetrics` | object | No |  |
| `engineHasCache` | boolean | No |  |
| `concurrentReload` | boolean | No |  |

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reloadmeta` | object | No |  |
| `amountofrows` | number | No |  |
| `amountoffields` | number | No |  |
| `amountoftables` | number | No |  |
| `staticbytesize` | number | No |  |
| `hassectionaccess` | boolean | No |  |
| `amountoffieldvalues` | number | No |  |
| `amountofcardinalfieldvalues` | number | No |  |

<details>
<summary>Properties of `reloadmeta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cpuspent` | number | No |  |
| `peakmemorybytes` | number | No |  |

</details>

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/evaluations/{id}/actions/download` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/evaluations/{id}/actions/download',
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
# qlik-cli has not implemented support for GET /api/v1/apps/evaluations/{id}/actions/download yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/evaluations/{id}/actions/download" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5ecb5e65028d1f0001a98071",
  "appId": "7c2ce11d-4d10-4414-a9b0-620e57298038",
  "ended": "2022-02-09T06:58:40.575Z",
  "events": [
    {
      "details": "An object failed",
      "sheetId": "gregFG",
      "objectId": "adfRFr",
      "severity": "warning",
      "errorCode": "ERR-GOPHERCISER",
      "objectType": "linechart",
      "sheetTitle": "mysheet",
      "objectTitle": "profit",
      "objectVisualization": "linechart"
    }
  ],
  "result": {
    "sheets": [
      {
        "sheet": {
          "id": "fjETFn",
          "title": "my chart",
          "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
          "objectType": "table",
          "timeoutStatusCode": "CALC-TIMEOUT",
          "responseTimeSeconds": 12.3
        },
        "objectCount": 1,
        "sheetObjects": [
          {
            "id": "fjETFn",
            "title": "my chart",
            "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
            "objectType": "table",
            "timeoutStatusCode": "CALC-TIMEOUT",
            "responseTimeSeconds": 12.3
          }
        ]
      }
    ],
    "rowCount": 20000,
    "objNoCache": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "sheetCount": 5,
    "objectCount": 33,
    "objSlowCached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "objMemoryLimit": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "memoryLimitStatusCode": "OUT-OF-MEMORY"
      }
    ],
    "documentSizeMiB": 12.3,
    "objSlowUncached": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "timeoutStatusCode": "CALC-TIMEOUT",
        "responseTimeSeconds": 12.3
      }
    ],
    "hasSectionAccess": false,
    "topFieldsByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "topTablesByBytes": [
      {
        "name": "a",
        "byte_size": 1234,
        "is_system": false
      }
    ],
    "objSingleThreaded": [
      {
        "id": "fjETFn",
        "title": "my chart",
        "sheetId": "41dbb01c-d1bd-4528-be05-910ee565988b",
        "objectType": "table",
        "cpuQuotient1": 12.3
      }
    ]
  },
  "status": "finished",
  "appName": "my app",
  "details": {
    "errors": [
      "this is an error"
    ],
    "warnings": [
      "this is a warning"
    ],
    "dedicated": false,
    "objectMetrics": {},
    "engineHasCache": false,
    "concurrentReload": false
  },
  "sheetId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "started": "2022-02-09T06:58:40.575Z",
  "version": 1,
  "metadata": {
    "reloadmeta": {
      "cpuspent": "123983",
      "peakmemorybytes": 112
    },
    "amountofrows": 1423423234,
    "amountoffields": 12,
    "amountoftables": 7,
    "staticbytesize": 1444234,
    "hassectionaccess": false,
    "amountoffieldvalues": 144423433,
    "amountofcardinalfieldvalues": 14442
  },
  "tenantId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "appItemId": "zyb2bQTeFmPVt9TXZOS0I5GZCFn",
  "timestamp": "2022-02-09T06:58:40.575Z",
  "sheetTitle": "my sheet"
}
```

---

### POST /api/v1/apps/import

Imports an app into the system.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | The app ID of the target app when source is qvw file. |
| `fallbackName` | string | No | The name of the target app when source does not have a specified name, applicable if source is qvw file. |
| `fileId` | string | No | The file ID to be downloaded from Temporary Content Service (TCS) and used during import. |
| `mode` | string | No | The import mode. In `new` mode (default), the source app will be imported as a new app.<div class=note>The `autoreplace` mode is an internal mode only and is not permitted for external use.</div>  One of: * NEW * AUTOREPLACE |
| `name` | string | No | The name of the target app. |
| `NoData` | boolean | No | If NoData is true, the data of the existing app will be kept as is, otherwise it will be replaced by the new incoming data. |
| `spaceId` | string | No | The space ID of the target app. |

#### Request Body

Path of the source app.

**Content-Type:** `application/octet-stream`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/octet-stream` | string | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `create` | object[] | No | Object create privileges. Hints to the client what type of objects the user is allowed to create. |
| `attributes` | object | No | App attributes. This structure can also contain extra user-defined attributes. |
| `privileges` | string[] | No | Application privileges. Hints to the client what actions the user is allowed to perform. Could be any of: * read * create * update * delete * reload * import * publish * duplicate * export * exportdata * change_owner * change_space |

<details>
<summary>Properties of `create`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource` | string | No | Type of resource. For example, sheet, story, bookmark, etc. |
| `canCreate` | boolean | No | Is set to true if the user has privileges to create the resource. |

</details>

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The App ID. |
| `name` | string | No | App name. |
| `owner` | string | No | _(deprecated)_ Deprecated. Use the Users API to fetch user metadata. |
| `usage` | string | No | Enum: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP", "DIRECT_QUERY_MODE" |
| `custom` | object | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | string | No | Identifier of the app owner. |
| `encrypted` | boolean | No | If set to true, the app is encrypted. |
| `published` | boolean | No | For Qlik Cloud, indicates whether the app has been distributed from client-managed, not whether it has been published. To determine if the app is published in Qlik Cloud, check for a non-empty value in the publishTime field. For client-managed, determines if the app is published. |
| `thumbnail` | string | No | App thumbnail. |
| `createdDate` | string | No | The date and time when the app was created. |
| `description` | string | No | App description. |
| `originAppId` | string | No | The Origin App ID for published apps. |
| `publishTime` | string | No | The date and time when the app was published, empty if unpublished. Use to determine if an app is published in Qlik Cloud. |
| `dynamicColor` | string | No | The dynamic color of the app. |
| `modifiedDate` | string | No | The date and time when the app was modified. |
| `lastReloadTime` | string | No | Date and time of the last reload of the app. |
| `hasSectionAccess` | boolean | No | If set to true, the app has section access configured, |
| `isDirectQueryMode` | boolean | No | True if the app is a Direct Query app, false if not |

</details>

##### 404

Not Found

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/import` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/import',
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
# qlik-cli has not implemented support for POST /api/v1/apps/import yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/import" \
-X POST \
-H "Content-type: application/octet-stream" \
-H "Authorization: Bearer <access_token>" \
--data-binary' \
          '"@/path/to/file"
```

**Example Response:**

```json
{
  "create": [
    {
      "resource": "string",
      "canCreate": true
    }
  ],
  "attributes": {
    "id": "string",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "encrypted": true,
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "string",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "privileges": [
    "string"
  ]
}
```

---

### GET /api/v1/apps/privileges

Gets the app privileges for the current user, such as create app and import app. Empty means that the current user has no app privileges.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Stability:** locked

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | string[] | No | Enum: "can_create_app", "can_import_app", "can_create_session_app" |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/apps/privileges` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/privileges',
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
# qlik-cli has not implemented support for GET /api/v1/apps/privileges yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/privileges" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[]
```

---

### POST /api/v1/apps/validatescript

Validates the script.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Stability:** locked

#### Request Body

**Required**

Script to validate.

**Content-Type:** `*/*`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `script` | string | No |  |

#### Responses

##### 200

OK

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Errors` | object[] | No |  |
| `Warnings` | object[] | No |  |

<details>
<summary>Properties of `Errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Msg` | string | No | Error or warning string. What is the problem. |
| `Tab` | integer | No | The index of the tab for the issue. |
| `Info` | string | No | Additional information like workarounds or clarifications. |
| `Line` | integer | No | Line in the tab of the issue. |
| `Column` | integer | No | UTF-8 byte column of the issue. |

</details>

<details>
<summary>Properties of `Warnings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Msg` | string | No | Error or warning string. What is the problem. |
| `Tab` | integer | No | The index of the tab for the issue. |
| `Info` | string | No | Additional information like workarounds or clarifications. |
| `Line` | integer | No | Line in the tab of the issue. |
| `Column` | integer | No | UTF-8 byte column of the issue. |

</details>

##### 403

Forbidden

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/apps/validatescript` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/apps/validatescript',
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
# qlik-cli has not implemented support for POST /api/v1/apps/validatescript yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/apps/validatescript" \
-X POST \
-H "Content-type: */*" \
-H "Authorization: Bearer <access_token>" \
-d '{"script":"string"}'
```

**Example Response:**

```json
{
  "Errors": [
    {
      "Msg": "string",
      "Tab": 42,
      "Info": "string",
      "Line": 42,
      "Column": 42
    }
  ],
  "Warnings": [
    {
      "Msg": "string",
      "Tab": 42,
      "Info": "string",
      "Line": 42,
      "Column": 42
    }
  ]
}
```

---
