# Spaces

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Spaces are logical containers within your tenant and control access for users and groups through space roles to what content users can access.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/spaces`](#get-apiv1spaces) | Retrieves spaces that the current user has access to and match the query. |
| `POST` | [`/api/v1/spaces`](#post-apiv1spaces) | Creates a space. Spaces names must be unique. Spaces of type `data` should only be used for Qlik Talend Data Integration projects. |
| `GET` | [`/api/v1/spaces/{spaceId}`](#get-apiv1spacesspaceid) | Retrieves a single space by ID. |
| `PATCH` | [`/api/v1/spaces/{spaceId}`](#patch-apiv1spacesspaceid) | Updates one or more properties of a space. To update all properties at once, use `PUT /spaces/{spaceId}`. |
| `PUT` | [`/api/v1/spaces/{spaceId}`](#put-apiv1spacesspaceid) | Updates a space. To update specific properties, use `PATCH /spaces/{spaceId}`. |
| `DELETE` | [`/api/v1/spaces/{spaceId}`](#delete-apiv1spacesspaceid) | Deletes a space. Ensure that you first delete all resources from the space to avoid orphaning content. |
| `GET` | [`/api/v1/spaces/{spaceId}/assignments`](#get-apiv1spacesspaceidassignments) | Retrieves the assignments of the space matching the query. Each assignment represents one user or group and their corresponding roles in the space. Assignments are not shown for the owner of a space, who receive all `assignableRoles` by default. |
| `POST` | [`/api/v1/spaces/{spaceId}/assignments`](#post-apiv1spacesspaceidassignments) | Creates an assignment for a user or group (assignee) to a space with the specified roles. Assignments are not required for space owners, who receive all `assignableRoles` by default. Only one assignment can exist per space, per user or group. |
| `GET` | [`/api/v1/spaces/{spaceId}/assignments/{assignmentId}`](#get-apiv1spacesspaceidassignmentsassignmentid) | Retrieves a single assignment by assignment ID. Use `GET /spaces/{spaceId}/assignments` to list all users and groups assigned to the space and their assignment ID. |
| `PUT` | [`/api/v1/spaces/{spaceId}/assignments/{assignmentId}`](#put-apiv1spacesspaceidassignmentsassignmentid) | Updates a single assignment by assignment ID. Use `GET /spaces/{spaceId}/assignments` to list all users and groups assigned to the space and their assignment ID. The complete list of roles must be provided. |
| `DELETE` | [`/api/v1/spaces/{spaceId}/assignments/{assignmentId}`](#delete-apiv1spacesspaceidassignmentsassignmentid) | Deletes an assignment. |
| `GET` | [`/api/v1/spaces/{spaceId}/shares`](#get-apiv1spacesspaceidshares) | Retrieves the shares of the space matching the query. |
| `POST` | [`/api/v1/spaces/{spaceId}/shares`](#post-apiv1spacesspaceidshares) | Creates a share. |
| `GET` | [`/api/v1/spaces/{spaceId}/shares/{shareId}`](#get-apiv1spacesspaceidsharesshareid) | Retrieves a single space share by ID. |
| `PATCH` | [`/api/v1/spaces/{spaceId}/shares/{shareId}`](#patch-apiv1spacesspaceidsharesshareid) | Updates properties of a space share (roles, and disabled state for link shares). |
| `DELETE` | [`/api/v1/spaces/{spaceId}/shares/{shareId}`](#delete-apiv1spacesspaceidsharesshareid) | Deletes a space share. |
| `GET` | [`/api/v1/spaces/types`](#get-apiv1spacestypes) | Gets a list of distinct space types available for use in the tenant. |

## API Reference

### GET /api/v1/spaces

Retrieves spaces that the current user has access to and match the query.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | string | No | Action on space. Supports only "?action=publish". |
| `environment.name` | string | No | Environment name to filter by. For example, "?environment.name=Development". Use an empty value to return spaces with no environment. |
| `environmentId` | string | No | Environment ID to filter by. For example, "?environmentId=67f4fba37f7cbb2f04ce727a". Use an empty value to return spaces with no environment. |
| `limit` | integer | No | Maximum number of spaces to return. |
| `name` | string | No | Space name to search and filter for. Case-insensitive open search with wildcards both as prefix and suffix. For example, "?name=fin" will get "finance", "Final" and "Griffin". |
| `next` | string | No | The next page cursor. Next links make use of this. |
| `ownerId` | string | No | Space ownerId to filter by. For example, "?ownerId=123". |
| `prev` | string | No | The previous page cursor. Previous links make use of this. |
| `roles` | string[] | No | Comma-separated list of roles to filter spaces by the caller's assignment role. For example, "?roles=publisher,facilitator" returns spaces where the caller has the publisher or facilitator role. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `sort` | string | No | Field to sort by. Prefix with +/- to indicate asc/desc. For example, "?sort=+name" to sort ascending on Name. Supported fields are "type", "name" and "createdAt". |
| `type` | string | No | Type(s) of space to filter. For example, "?type=managed,shared". |

#### Responses

##### 200

Spaces retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | A space is a security context simplifying the management of access control by allowing users to control it on the containers instead of on the resources themselves. |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | A unique identifier for the space, for example, 62716f4b39b865ece543cd45. |
| `meta` | object | No | Information about the space settings. |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | No | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `links` | object | Yes |  |
| `ownerId` | string | No | The ID for the space owner. |
| `tenantId` | string | Yes | The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the space. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | Yes | The list of roles assigned to the current user in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `assignableRoles` | string[] | Yes | The list of roles that could be assigned in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `assignments` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `assignments`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | The total number of spaces matching the current filter. |
| `personalSpace` | object | No | The meta related to personal space when applicable. |

<details>
<summary>Properties of `personalSpace`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `resourceType` | string | Yes | resource type |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 400

Bad request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/spaces', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/spaces yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "meta": {
        "roles": [
          "consumer"
        ],
        "actions": [
          "change_owner"
        ],
        "assignableRoles": [
          "consumer"
        ]
      },
      "name": "string",
      "type": "shared",
      "links": {
        "self": {
          "href": "string"
        },
        "assignments": {
          "href": "string"
        }
      },
      "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "updatedAt": "2018-10-30T07:06:22Z",
      "description": "string"
    }
  ],
  "meta": {
    "count": 42,
    "personalSpace": {
      "actions": [
        "change_owner"
      ],
      "resourceType": "string"
    }
  },
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

### POST /api/v1/spaces

Creates a space. Spaces names must be unique. Spaces of type `data` should only be used for Qlik Talend Data Integration projects.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Attributes that the user wants to set for a new space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | Yes | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

#### Responses

##### 201

Space created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | A unique identifier for the space, for example, 62716f4b39b865ece543cd45. |
| `meta` | object | No | Information about the space settings. |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | No | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `links` | object | Yes |  |
| `ownerId` | string | No | The ID for the space owner. |
| `tenantId` | string | Yes | The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the space. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | Yes | The list of roles assigned to the current user in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `assignableRoles` | string[] | Yes | The list of roles that could be assigned in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `assignments` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `assignments`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Space create operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 409

Space already exists. `name` must be unique.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/spaces` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/spaces', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'Finance (dev)',
    type: 'shared',
    description:
      'Development space for users building apps for the Finance team.',
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/spaces yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Finance (dev)","type":"shared","description":"Development space for users building apps for the Finance team."}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "meta": {
    "roles": [
      "consumer"
    ],
    "actions": [
      "change_owner"
    ],
    "assignableRoles": [
      "consumer"
    ]
  },
  "name": "string",
  "type": "shared",
  "links": {
    "self": {
      "href": "string"
    },
    "assignments": {
      "href": "string"
    }
  },
  "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "description": "string"
}
```

---

### GET /api/v1/spaces/{spaceId}

Retrieves a single space by ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space to retrieve. |

#### Responses

##### 200

Space retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | A unique identifier for the space, for example, 62716f4b39b865ece543cd45. |
| `meta` | object | No | Information about the space settings. |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | No | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `links` | object | Yes |  |
| `ownerId` | string | No | The ID for the space owner. |
| `tenantId` | string | Yes | The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the space. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | Yes | The list of roles assigned to the current user in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `assignableRoles` | string[] | Yes | The list of roles that could be assigned in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `assignments` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `assignments`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 429

Too many repetetive requests.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/{spaceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/{spaceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "meta": {
    "roles": [
      "consumer"
    ],
    "actions": [
      "change_owner"
    ],
    "assignableRoles": [
      "consumer"
    ]
  },
  "name": "string",
  "type": "shared",
  "links": {
    "self": {
      "href": "string"
    },
    "assignments": {
      "href": "string"
    }
  },
  "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "description": "string"
}
```

---

### PATCH /api/v1/spaces/{spaceId}

Updates one or more properties of a space. To update all properties at once, use `PUT /spaces/{spaceId}`.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space to update. |

#### Request Body

**Required**

Attribute that the user wants to patch (update) for the specified space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | Field of space to be patched (updated). Enum: "/name", "/ownerId", "/description" |
| `value` | string | Yes | The value to be used within the operations. - name: The name (string) of space of maxLength 256 of pattern: ^[^\"\*\?\<\>\/\\|\\\:]+$ - description: The description (string) of the space. Personal spaces do not have a description. - ownerId: The user ID in uid format (string) of the space owner. |

#### Responses

##### 200

Space patched (updated).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | A unique identifier for the space, for example, 62716f4b39b865ece543cd45. |
| `meta` | object | No | Information about the space settings. |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | No | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `links` | object | Yes |  |
| `ownerId` | string | No | The ID for the space owner. |
| `tenantId` | string | Yes | The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the space. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | Yes | The list of roles assigned to the current user in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `assignableRoles` | string[] | Yes | The list of roles that could be assigned in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `assignments` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `assignments`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Space patch (update) operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/spaces/{spaceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/spaces/{spaceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"string"}]'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "meta": {
    "roles": [
      "consumer"
    ],
    "actions": [
      "change_owner"
    ],
    "assignableRoles": [
      "consumer"
    ]
  },
  "name": "string",
  "type": "shared",
  "links": {
    "self": {
      "href": "string"
    },
    "assignments": {
      "href": "string"
    }
  },
  "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "description": "string"
}
```

---

### PUT /api/v1/spaces/{spaceId}

Updates a space. To update specific properties, use `PATCH /spaces/{spaceId}`.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space to update. |

#### Request Body

**Required**

Attributes that the user wants to update for the specified space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of the space. |
| `ownerId` | string | No | The user ID of the space owner. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

#### Responses

##### 200

Space updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | A unique identifier for the space, for example, 62716f4b39b865ece543cd45. |
| `meta` | object | No | Information about the space settings. |
| `name` | string | Yes | The name of the space. Personal spaces do not have a name. |
| `type` | string | No | The type of space such as shared, managed, and so on. Enum: "shared", "managed", "data" |
| `links` | object | Yes |  |
| `ownerId` | string | No | The ID for the space owner. |
| `tenantId` | string | Yes | The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the space. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `description` | string | No | The description of the space. Personal spaces do not have a description. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | Yes | The list of roles assigned to the current user in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `actions` | string[] | Yes | The list of actions allowed by the current user in this space. Enum: "change_owner", "create", "read", "update", "delete", "publish", "link_environment", "restrict" |
| `assignableRoles` | string[] | Yes | The list of roles that could be assigned in this space. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `assignments` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `assignments`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Space update operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/spaces/{spaceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      ownerId: 'TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69',
      description: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/spaces/{spaceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","ownerId":"TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69","description":"string"}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "meta": {
    "roles": [
      "consumer"
    ],
    "actions": [
      "change_owner"
    ],
    "assignableRoles": [
      "consumer"
    ]
  },
  "name": "string",
  "type": "shared",
  "links": {
    "self": {
      "href": "string"
    },
    "assignments": {
      "href": "string"
    }
  },
  "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "description": "string"
}
```

---

### DELETE /api/v1/spaces/{spaceId}

Deletes a space. Ensure that you first delete all resources from the space to avoid orphaning content.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space to delete. |

#### Responses

##### 204

Space deleted.

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Space delete operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 412

Space delete precondition (space not empty) failed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/spaces/{spaceId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/spaces/{spaceId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/spaces/{spaceId}/assignments

Retrieves the assignments of the space matching the query. Each assignment represents one user or group and their corresponding roles in the space. Assignments are not shown for the owner of a space, who receive all `assignableRoles` by default.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space of the assignment. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assigneeId` | string | No | Filters assignment for a specific assigneeid. |
| `limit` | integer | No | Maximum number of assignments to return. |
| `next` | string | No | The next page cursor. Next links make use of this. |
| `prev` | string | No | The previous page cursor. Previous links make use of this. |
| `type` | string | No | The type of assignment. Supported values are user or group. Enum: "user", "group", "bot" |

#### Responses

##### 200

Assignments retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | The type of assignment such as user or group Enum: "user", "group", "bot" |
| `links` | object | Yes |  |
| `roles` | string[] | Yes | The roles assigned to a user or group. Must not be empty. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `spaceId` | string | Yes | The unique identifier for the space. |
| `tenantId` | string | Yes | The unique identifier for the tenant. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the assignment. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `updatedBy` | string | No | The ID of the user who updated the assignment. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `space`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | The total number of assignments matching the current filter. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Assignments retrieve operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/{spaceId}/assignments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/assignments',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/{spaceId}/assignments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/assignments" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "type": "user",
      "links": {
        "self": {
          "href": "string"
        },
        "space": {
          "href": "string"
        }
      },
      "roles": [
        "consumer"
      ],
      "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "updatedAt": "2018-10-30T07:06:22Z",
      "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
    }
  ],
  "meta": {
    "count": 42
  },
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

### POST /api/v1/spaces/{spaceId}/assignments

Creates an assignment for a user or group (assignee) to a space with the specified roles. Assignments are not required for space owners, who receive all `assignableRoles` by default. Only one assignment can exist per space, per user or group.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space of the assignment. |

#### Request Body

**Required**

Attributes that the user wants to set for the assignment for the space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The type of assignment such as user or group Enum: "user", "group", "bot" |
| `roles` | string[] | Yes | The roles assigned to the assigneeId. For the full list of roles assignable in this space type, call `GET /spaces/{spaceId}` and inspect the `meta.assignableRoles` object. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |

#### Responses

##### 201

Assignment created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | The type of assignment such as user or group Enum: "user", "group", "bot" |
| `links` | object | Yes |  |
| `roles` | string[] | Yes | The roles assigned to a user or group. Must not be empty. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `spaceId` | string | Yes | The unique identifier for the space. |
| `tenantId` | string | Yes | The unique identifier for the tenant. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the assignment. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `updatedBy` | string | No | The ID of the user who updated the assignment. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Assignment create operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 409

Assignment already exists. `assigneeId` must be unique.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/spaces/{spaceId}/assignments` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/assignments',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'user',
      roles: ['consumer'],
      assigneeId:
        'TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/spaces/{spaceId}/assignments yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/assignments" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"user","roles":["consumer"],"assigneeId":"TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
}
```

---

### GET /api/v1/spaces/{spaceId}/assignments/{assignmentId}

Retrieves a single assignment by assignment ID. Use `GET /spaces/{spaceId}/assignments` to list all users and groups assigned to the space and their assignment ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assignmentId` | string | Yes | The ID of the assignment to retrieve. |
| `spaceId` | string | Yes | The ID of the space of the assignment. |

#### Responses

##### 200

Assignment retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | The type of assignment such as user or group Enum: "user", "group", "bot" |
| `links` | object | Yes |  |
| `roles` | string[] | Yes | The roles assigned to a user or group. Must not be empty. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `spaceId` | string | Yes | The unique identifier for the space. |
| `tenantId` | string | Yes | The unique identifier for the tenant. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the assignment. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `updatedBy` | string | No | The ID of the user who updated the assignment. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Assignment retrieve operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied or assignment not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/{spaceId}/assignments/{assignmentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/assignments/{assignmentId}',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/{spaceId}/assignments/{assignmentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/assignments/{assignmentId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
}
```

---

### PUT /api/v1/spaces/{spaceId}/assignments/{assignmentId}

Updates a single assignment by assignment ID. Use `GET /spaces/{spaceId}/assignments` to list all users and groups assigned to the space and their assignment ID. The complete list of roles must be provided.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assignmentId` | string | Yes | The ID of the assignment to update. |
| `spaceId` | string | Yes | The ID of the space of the assignment. |

#### Request Body

**Required**

Attributes that the user wants to update for the specified assignment.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `roles` | string[] | No | The roles assigned to the assigneeId. For the full list of roles assignable in this space type, call `GET /spaces/{spaceId}` and inspect the `meta.assignableRoles` object. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |

#### Responses

##### 200

Assignment updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | The type of assignment such as user or group Enum: "user", "group", "bot" |
| `links` | object | Yes |  |
| `roles` | string[] | Yes | The roles assigned to a user or group. Must not be empty. Enum: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper" |
| `spaceId` | string | Yes | The unique identifier for the space. |
| `tenantId` | string | Yes | The unique identifier for the tenant. |
| `createdAt` | string | No | The date and time when the space was created. |
| `createdBy` | string | No | The ID of the user who created the assignment. |
| `updatedAt` | string | No | The date and time when the space was updated. |
| `updatedBy` | string | No | The ID of the user who updated the assignment. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Assignment update operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/spaces/{spaceId}/assignments/{assignmentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/assignments/{assignmentId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ roles: ['consumer'] }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/spaces/{spaceId}/assignments/{assignmentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/assignments/{assignmentId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"roles":["consumer"]}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
}
```

---

### DELETE /api/v1/spaces/{spaceId}/assignments/{assignmentId}

Deletes an assignment.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `assignmentId` | string | Yes | The ID of the assignment to delete. |
| `spaceId` | string | Yes | The ID of the space of the assignment. |

#### Responses

##### 204

Assignment deleted.

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Assignment delete operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied or assignment not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/spaces/{spaceId}/assignments/{assignmentId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/assignments/{assignmentId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/spaces/{spaceId}/assignments/{assignmentId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/assignments/{assignmentId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/spaces/{spaceId}/shares

Retrieves the shares of the space matching the query.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space containing the shares. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `groupId` | string | No | The ID of the group to which the resource is shared. |
| `limit` | integer | No | Maximum number of shares to return. |
| `name` | string | No | The name of the shared resource. |
| `next` | string | No | The next page cursor. Next links make use of this. |
| `prev` | string | No | The previous page cursor. Previous links make use of this. |
| `resourceId` | string | No | The ID of the shared resource. |
| `resourceType` | string | No | The type of the shared resource. |
| `type` | string | No | The type of share. `user` shares assign to a specific user, `group` shares assign to a specific group, and `link` shares provide anonymous access to a resource. Enum: "user", "group", "link" |
| `userId` | string | No | The ID of the user to which the resource is shared. |

#### Responses

##### 200

Shares retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `meta` | object | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "user", "group", "link" |
| `links` | object | No |  |
| `roles` | string[] | No | The roles assigned to the assigneeId. Enum: "consumer", "contributor", "basicconsumer" |
| `spaceId` | string | Yes |  |
| `disabled` | boolean | No | If the share is disabled (effective ONLY for link shares). |
| `tenantId` | string | Yes |  |
| `createdAt` | string | No |  |
| `createdBy` | string | No | The ID of the user who created the share. |
| `updatedAt` | string | No |  |
| `updatedBy` | string | No | The ID of the user who updated the share. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |
| `resourceId` | string | Yes | The ID of the shared resource. |
| `resourceName` | string | No | The name of the shared resource. |
| `resourceType` | string | Yes | The type of the shared resource. Enum: "app" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `space`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | The total number of Shares matching the current filter. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Shares retrieve operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/{spaceId}/shares` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/shares',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/{spaceId}/shares yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/shares" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "type": "user",
      "links": {
        "self": {
          "href": "string"
        },
        "space": {
          "href": "string"
        }
      },
      "roles": [
        "consumer"
      ],
      "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "disabled": true,
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "updatedAt": "2018-10-30T07:06:22Z",
      "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "resourceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "resourceName": "string",
      "resourceType": "app"
    }
  ],
  "meta": {
    "count": 42
  },
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

### POST /api/v1/spaces/{spaceId}/shares

Creates a share.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The ID of the space of the share. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "user", "group", "link" |
| `roles` | string[] | Yes | The roles assigned to the assigneeId. Enum: "consumer", "contributor", "basicconsumer" |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |
| `resourceId` | string | Yes | The resource id for the shared item. |
| `resourceType` | string | Yes | The resource type for the shared item. |

#### Responses

##### 201

Share created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "user", "group", "link" |
| `links` | object | No |  |
| `roles` | string[] | No | The roles assigned to the assigneeId. Enum: "consumer", "contributor", "basicconsumer" |
| `spaceId` | string | Yes |  |
| `disabled` | boolean | No | If the share is disabled (effective ONLY for link shares). |
| `tenantId` | string | Yes |  |
| `createdAt` | string | No |  |
| `createdBy` | string | No | The ID of the user who created the share. |
| `updatedAt` | string | No |  |
| `updatedBy` | string | No | The ID of the user who updated the share. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |
| `resourceId` | string | Yes | The ID of the shared resource. |
| `resourceName` | string | No | The name of the shared resource. |
| `resourceType` | string | Yes | The type of the shared resource. Enum: "app" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Share create operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 409

Share already exists. `assigneeId` must be unique.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/spaces/{spaceId}/shares` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/shares',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      type: 'user',
      roles: ['consumer'],
      assigneeId:
        'TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69',
      resourceId:
        'TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69',
      resourceType:
        'TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/spaces/{spaceId}/shares yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/shares" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"user","roles":["consumer"],"assigneeId":"TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69","resourceId":"TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69","resourceType":"TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "disabled": true,
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceName": "string",
  "resourceType": "app"
}
```

---

### GET /api/v1/spaces/{spaceId}/shares/{shareId}

Retrieves a single space share by ID.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shareId` | string | Yes | The ID of the share to retrieve. |
| `spaceId` | string | Yes | The ID of the space to which the share belongs. |

#### Responses

##### 200

Share retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "user", "group", "link" |
| `links` | object | No |  |
| `roles` | string[] | No | The roles assigned to the assigneeId. Enum: "consumer", "contributor", "basicconsumer" |
| `spaceId` | string | Yes |  |
| `disabled` | boolean | No | If the share is disabled (effective ONLY for link shares). |
| `tenantId` | string | Yes |  |
| `createdAt` | string | No |  |
| `createdBy` | string | No | The ID of the user who created the share. |
| `updatedAt` | string | No |  |
| `updatedBy` | string | No | The ID of the user who updated the share. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |
| `resourceId` | string | Yes | The ID of the shared resource. |
| `resourceName` | string | No | The name of the shared resource. |
| `resourceType` | string | Yes | The type of the shared resource. Enum: "app" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Share retrieve operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied or share not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/{spaceId}/shares/{shareId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/shares/{shareId}',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/{spaceId}/shares/{shareId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/shares/{shareId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "disabled": true,
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceName": "string",
  "resourceType": "app"
}
```

---

### PATCH /api/v1/spaces/{spaceId}/shares/{shareId}

Updates properties of a space share (roles, and disabled state for link shares).

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shareId` | string | Yes | The ID of the share to update. |
| `spaceId` | string | Yes | The ID of the space to which the share belongs. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | Field of Share to be patched (updated). Enum: "/roles", "/disabled" |
| `value` | string | Yes | The value to be used within the operations. - roles: The roles assigned to the assigneeId. - disabled: To disable the share (effective ONLY for link shares). |

#### Responses

##### 200

Share patched (updated).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `type` | string | Yes | Enum: "user", "group", "link" |
| `links` | object | No |  |
| `roles` | string[] | No | The roles assigned to the assigneeId. Enum: "consumer", "contributor", "basicconsumer" |
| `spaceId` | string | Yes |  |
| `disabled` | boolean | No | If the share is disabled (effective ONLY for link shares). |
| `tenantId` | string | Yes |  |
| `createdAt` | string | No |  |
| `createdBy` | string | No | The ID of the user who created the share. |
| `updatedAt` | string | No |  |
| `updatedBy` | string | No | The ID of the user who updated the share. |
| `assigneeId` | string | Yes | The userId or groupId based on the type. |
| `resourceId` | string | Yes | The ID of the shared resource. |
| `resourceName` | string | No | The name of the shared resource. |
| `resourceType` | string | Yes | The type of the shared resource. Enum: "app" |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `space` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

<details>
<summary>Properties of `space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

Share patch (update) operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Share not found or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/spaces/{spaceId}/shares/{shareId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/shares/{shareId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/roles',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/spaces/{spaceId}/shares/{shareId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/shares/{shareId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/roles","value":"string"}]'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "type": "user",
  "links": {
    "self": {
      "href": "string"
    },
    "space": {
      "href": "string"
    }
  },
  "roles": [
    "consumer"
  ],
  "spaceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "disabled": true,
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "createdAt": "2018-10-30T07:06:22Z",
  "createdBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "updatedAt": "2018-10-30T07:06:22Z",
  "updatedBy": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "assigneeId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "resourceName": "string",
  "resourceType": "app"
}
```

---

### DELETE /api/v1/spaces/{spaceId}/shares/{shareId}

Deletes a space share.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `shareId` | string | Yes | The ID of the share to delete. |
| `spaceId` | string | Yes | The ID of the space to which the share belongs. |

#### Responses

##### 204

Share deleted.

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 403

share delete operation denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 404

Space not found or access denied or share not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/spaces/{spaceId}/shares/{shareId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/{spaceId}/shares/{shareId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/spaces/{spaceId}/shares/{shareId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/{spaceId}/shares/{shareId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/spaces/types

Gets a list of distinct space types available for use in the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Space types retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | string[] | No | The name of the type. Enum: "shared", "managed", "data" |

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | _(deprecated)_ The error code. |
| `meta` | object | No | _(deprecated)_ Additional properties relating to the error. |
| `title` | string | No | _(deprecated)_ Summary of the problem. |
| `detail` | string | No | _(deprecated)_ A human-readable explanation specific to the occurrence of this problem. |
| `errors` | object[] | No | An error object. |
| `source` | object | No | _(deprecated)_ References to the source of the error. |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to the occurrence of this problem. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | object | No | References to the source of the error. |

<details>
<summary>Properties of `source`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/spaces/types` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/spaces/types',
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
# qlik-cli has not implemented support for GET /api/v1/spaces/types yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/spaces/types" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    "data",
    "shared",
    "managed"
  ]
}
```

---
