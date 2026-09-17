# Groups

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Groups is the resource representing a group in the system, to which space and tenant roles can be assigned to simplify access control management.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/groups`](#get-apiv1groups) | Returns a list of groups with cursor-based pagination. |
| `POST` | [`/api/v1/groups`](#post-apiv1groups) | Creates a new group. The maximum number of groups a tenant can have is 10,000. Group names are case-sensitive, and must be unique. |
| `GET` | [`/api/v1/groups/{groupId}`](#get-apiv1groupsgroupid) | Returns the requested group. |
| `PATCH` | [`/api/v1/groups/{groupId}`](#patch-apiv1groupsgroupid) | Updates the requested group. |
| `DELETE` | [`/api/v1/groups/{groupId}`](#delete-apiv1groupsgroupid) | Deletes the requested group. |
| `POST` | [`/api/v1/groups/actions/filter`](#post-apiv1groupsactionsfilter) | Retrieves a list of groups matching the filter using advanced query string. |
| `GET` | [`/api/v1/groups/settings`](#get-apiv1groupssettings) | Returns the tenant's group settings, such as whether automatic group creation and IdP group synchronization are enabled or disabled, and roles assigned to system groups. |
| `PATCH` | [`/api/v1/groups/settings`](#patch-apiv1groupssettings) | Updates the tenant's group settings, such as whether automatic group creation and IdP group synchronization are enabled or disabled, and roles assigned to system groups. |

## API Reference

### GET /api/v1/groups

Returns a list of groups with cursor-based pagination.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive. |
| `limit` | number | No | The number of groups to retrieve. |
| `next` | string | No | The next page cursor. |
| `prev` | string | No | The previous page cursor. |
| `sort` | string | No | Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending. |
| `systemGroups` | boolean | No | Return system groups (e.g. Everyone) instead of regular groups. Cannot be combined with any other query parameters. |
| `totalResults` | boolean | No | Whether to return a total match count in the result. Defaults to false. |

#### Responses

##### 200

An array of groups, and pagination links.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | An array of groups. |
| `links` | object | No |  |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the group |
| `name` | string | Yes | The name of the group. |
| `links` | object | Yes | Contains Links for current document |
| `status` | string | Yes | The state of the group. Enum: "active", "disabled" |
| `tenantId` | string | Yes | The tenant identifier associated with the given group |
| `createdAt` | string | Yes | The timestamp for when the group record was created. |
| `createdBy` | string | No | Id of user that created role. |
| `updatedBy` | string | No | Id of user that last updated this role. |
| `description` | string | No | A description of a custom group. |
| `providerType` | string | No | The type of provider for the group. Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the group record was last updated. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |
| `name` | string | Yes | The role name |
| `type` | string | Yes | The type of role Enum: "default", "custom" |
| `level` | string | Yes | The role level Enum: "admin", "user" |

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
| `href` | string | Yes | Link to the next page of items |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the previous page of items |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the current page of items |

</details>

</details>

##### 400

Invalid request parameters for querying groups.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized, JWT is invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

All operations failed due to insufficient permissions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/groups` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/groups', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/groups yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "Development",
      "links": {
        "self": {
          "href": "http://mytenant.us.qlikcloud.com/api/v1/groups/507f191e810c19729de860ea"
        }
      },
      "status": "active",
      "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
      "createdAt": "2021-03-21T17:32:28Z",
      "createdBy": "string",
      "updatedBy": "string",
      "description": "string",
      "providerType": "idp",
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "A Custom Role",
          "type": "custom",
          "level": "user"
        }
      ],
      "lastUpdatedAt": "2021-03-22T10:01:02Z"
    }
  ],
  "links": {
    "next": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups?next=FgAAAAdfaWQAYF33ydumcVj1cawoAA"
    },
    "prev": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups?prev=FgAACAdfaWQAYF33ydumcVj1cawoAA"
    },
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups"
    }
  },
  "totalResults": 42
}
```

---

### POST /api/v1/groups

Creates a new group. The maximum number of groups a tenant can have is 10,000. Group names are case-sensitive, and must be unique.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the group (maximum length of 256 characters). |
| `status` | string | No | The status of the created group within the tenant. Defaults to active if empty. Enum: "active" |
| `description` | string | No | The description of the group. |
| `providerType` | string | No | The type of group provider. Must be "idp" or "custom". Defaults to "idp" if not provided. Enum: "idp", "custom" |
| `assignedRoles` | array | No | The roles to assign to the group (limit of 100 roles per group). |

<details>
<summary>Properties of `assignedRoles`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefIDs` | object[] | No | An array of role reference identifiers. |

<details>
<summary>Properties of `AssignedRolesRefIDs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefNames` | object[] | No | An array of role reference names. |

<details>
<summary>Properties of `AssignedRolesRefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the role |

</details>

</details>

#### Responses

##### 201

Group was successfully created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the group |
| `name` | string | Yes | The name of the group. |
| `links` | object | Yes | Contains Links for current document |
| `status` | string | Yes | The state of the group. Enum: "active", "disabled" |
| `tenantId` | string | Yes | The tenant identifier associated with the given group |
| `createdAt` | string | Yes | The timestamp for when the group record was created. |
| `createdBy` | string | No | Id of user that created role. |
| `updatedBy` | string | No | Id of user that last updated this role. |
| `description` | string | No | A description of a custom group. |
| `providerType` | string | No | The type of provider for the group. Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the group record was last updated. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the current group document |

</details>

</details>

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |
| `name` | string | Yes | The role name |
| `type` | string | Yes | The type of role Enum: "default", "custom" |
| `level` | string | Yes | The role level Enum: "admin", "user" |

</details>

##### 400

Invalid request was made.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to create a group.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from creating a group.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 409

Name conflict when attempting to create a new group.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 413

Payload was too large.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `POST /api/v1/groups` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/groups', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'Development',
    status: 'active',
    assignedRoles: [{ name: 'A Custom Role' }],
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/groups yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Development","status":"active","assignedRoles":[{"name":"A Custom Role"}]}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Development",
  "links": {
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups/507f191e810c19729de860ea"
    }
  },
  "status": "active",
  "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "string",
  "updatedBy": "string",
  "description": "string",
  "providerType": "idp",
  "assignedRoles": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "A Custom Role",
      "type": "custom",
      "level": "user"
    }
  ],
  "lastUpdatedAt": "2021-03-22T10:01:02Z"
}
```

---

### GET /api/v1/groups/{groupId}

Returns the requested group.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `groupId` | string | Yes | The group's unique identifier |

#### Responses

##### 200

Request successfully completed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the group |
| `name` | string | Yes | The name of the group. |
| `links` | object | Yes | Contains Links for current document |
| `status` | string | Yes | The state of the group. Enum: "active", "disabled" |
| `tenantId` | string | Yes | The tenant identifier associated with the given group |
| `createdAt` | string | Yes | The timestamp for when the group record was created. |
| `createdBy` | string | No | Id of user that created role. |
| `updatedBy` | string | No | Id of user that last updated this role. |
| `description` | string | No | A description of a custom group. |
| `providerType` | string | No | The type of provider for the group. Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the group record was last updated. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the current group document |

</details>

</details>

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |
| `name` | string | Yes | The role name |
| `type` | string | Yes | The type of role Enum: "default", "custom" |
| `level` | string | Yes | The role level Enum: "admin", "user" |

</details>

##### 403

The operation failed due to insufficient permissions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Group ID not found or Invalid format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/groups/{groupId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/{groupId}',
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
# qlik-cli has not implemented support for GET /api/v1/groups/{groupId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/{groupId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "Development",
  "links": {
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups/507f191e810c19729de860ea"
    }
  },
  "status": "active",
  "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "string",
  "updatedBy": "string",
  "description": "string",
  "providerType": "idp",
  "assignedRoles": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "A Custom Role",
      "type": "custom",
      "level": "user"
    }
  ],
  "lastUpdatedAt": "2021-03-22T10:01:02Z"
}
```

---

### PATCH /api/v1/groups/{groupId}

Updates the requested group.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `groupId` | string | Yes | The ID of the group to update. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Currently "replace" is the only supported operation. Enum: "replace" |
| `path` | string | Yes | Attribute name of a field of the Groups entity. "Name" and "description" is only available for custom groups. Enum: "assignedRoles", "name", "description" |
| `value` | array \| string | Yes | The roles to assign to the group (limit of 100 roles per group) or the new custom group name or description. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefIDs` | object[] | No | An array of role reference identifiers. |

<details>
<summary>Properties of `AssignedRolesRefIDs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefNames` | object[] | No | An array of role reference names. |

<details>
<summary>Properties of `AssignedRolesRefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the role |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

</details>

#### Responses

##### 204

Group updated successfully.

##### 400

Invalid request for patching a user.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to patch a group.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from patching a group.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Group was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `PATCH /api/v1/groups/{groupId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/{groupId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/assignedRoles',
        value: [
          { name: 'TenantAdmin' },
          { name: 'AnalyticsAdmin' },
        ],
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/groups/{groupId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/{groupId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/assignedRoles","value":[{"name":"TenantAdmin"},{"name":"AnalyticsAdmin"}]}]'
```

---

### DELETE /api/v1/groups/{groupId}

Deletes the requested group.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `groupId` | string | Yes | The ID of the group to delete. |

#### Responses

##### 204

Group deleted successfully.

##### 401

Unauthorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Group ID not found or Invalid format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `DELETE /api/v1/groups/{groupId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/{groupId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/groups/{groupId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/{groupId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/groups/actions/filter

Retrieves a list of groups matching the filter using advanced query string.

- **Rate Limit:** Special (200 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | number | No | The number of user entries to retrieve. |
| `next` | string | No | Get users with IDs that are higher than the target user ID. Cannot be used in conjunction with prev. |
| `prev` | string | No | Get users with IDs that are lower than the target user ID. Cannot be used in conjunction with next. |
| `sort` | string | No | The field to sort by, with +/- prefix indicating sort order Enum: "name", "+name", "-name" |

#### Request Body

Will contain the query filter to apply. It shall not contain more than 100 ids.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The advanced filtering to be applied the query. All conditional statements within this query parameter are case insensitive. |

#### Responses

##### 200

Groups retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | An array of groups. |
| `links` | object | No |  |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the group |
| `name` | string | Yes | The name of the group. |
| `links` | object | Yes | Contains Links for current document |
| `status` | string | Yes | The state of the group. Enum: "active", "disabled" |
| `tenantId` | string | Yes | The tenant identifier associated with the given group |
| `createdAt` | string | Yes | The timestamp for when the group record was created. |
| `createdBy` | string | No | Id of user that created role. |
| `updatedBy` | string | No | Id of user that last updated this role. |
| `description` | string | No | A description of a custom group. |
| `providerType` | string | No | The type of provider for the group. Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the group record was last updated. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |
| `name` | string | Yes | The role name |
| `type` | string | Yes | The type of role Enum: "default", "custom" |
| `level` | string | Yes | The role level Enum: "admin", "user" |

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
| `href` | string | Yes | Link to the next page of items |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the previous page of items |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the current page of items |

</details>

</details>

##### 400

Advanced query filter syntax error or query params format error or filter too complex.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The operation failed due to insufficient permissions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `POST /api/v1/groups/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      filter:
        '(id eq "626949b9017b657805080bbd" or id eq "626949bf017b657805080bbe") and (status eq "active" or status eq "deleted")',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/groups/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"filter":"(id eq \"626949b9017b657805080bbd\" or id eq \"626949bf017b657805080bbe\") and (status eq \"active\" or status eq \"deleted\")"}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "Development",
      "links": {
        "self": {
          "href": "http://mytenant.us.qlikcloud.com/api/v1/groups/507f191e810c19729de860ea"
        }
      },
      "status": "active",
      "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
      "createdAt": "2021-03-21T17:32:28Z",
      "createdBy": "string",
      "updatedBy": "string",
      "description": "string",
      "providerType": "idp",
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "A Custom Role",
          "type": "custom",
          "level": "user"
        }
      ],
      "lastUpdatedAt": "2021-03-22T10:01:02Z"
    }
  ],
  "links": {
    "next": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups?next=FgAAAAdfaWQAYF33ydumcVj1cawoAA"
    },
    "prev": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups?prev=FgAACAdfaWQAYF33ydumcVj1cawoAA"
    },
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups"
    }
  },
  "totalResults": 42
}
```

---

### GET /api/v1/groups/settings

Returns the tenant's group settings, such as whether automatic group creation and IdP group synchronization are enabled or disabled, and roles assigned to system groups.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The requested tenant's group settings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `links` | object | Yes | Contains Links for current document |
| `tenantId` | string | Yes | The unique tenant identifier. |
| `systemGroups` | object | No |  |
| `syncIdpGroups` | boolean | No | _(deprecated)_ Determines if groups should be created on login. |
| `autoCreateGroups` | boolean | Yes | Determines if groups should be created on login. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the current group settings document |

</details>

</details>

<details>
<summary>Properties of `systemGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `000000000000000000000001` | object | No |  |

<details>
<summary>Properties of `000000000000000000000001`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The ID of the Everyone group. This value will not change and is immutable. Enum: "000000000000000000000001" |
| `name` | string | No | The name of the Everyone group. This value will not change and is immutable. Enum: "com.qlik.Everyone" |
| `enabled` | boolean | No | For Everyone, this is always `true` and can't be patched. |
| `createdAt` | string | No | The timestamp for when the Everyone group was created. |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | No | The timestamp for when the Everyone group was last updated. |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Not authorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The operation failed due to insufficient permissions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/groups/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/settings',
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
# qlik-cli has not implemented support for GET /api/v1/groups/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "links": {
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/groups/settings"
    }
  },
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "systemGroups": {
    "000000000000000000000001": {
      "id": "000000000000000000000001",
      "name": "com.qlik.Everyone",
      "enabled": true,
      "createdAt": "2021-03-22T10:01:02Z",
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "A Custom Role",
          "type": "custom",
          "level": "user"
        }
      ],
      "lastUpdatedAt": "2021-03-22T10:01:02Z"
    }
  },
  "syncIdpGroups": false,
  "autoCreateGroups": false
}
```

---

### PATCH /api/v1/groups/settings

Updates the tenant's group settings, such as whether automatic group creation and IdP group synchronization are enabled or disabled, and roles assigned to system groups.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | A JSON Pointer. Enum: "/autoCreateGroups", "/syncIdpGroups", "/systemGroups/{id}/assignedRoles" |
| `value` | boolean \| array | Yes | The value to be used for this operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefIDs` | object[] | No | An array of role reference identifiers. |

<details>
<summary>Properties of `AssignedRolesRefIDs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique role identitier |

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedRolesRefNames` | object[] | No | An array of role reference names. |

<details>
<summary>Properties of `AssignedRolesRefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the role |

</details>

</details>

#### Responses

##### 204

Config updated successfully.

##### 400

Bad request. Payload could not be parsed to a JSON Patch or Patch operations are invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Not authorized.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The operation failed due to insufficient permissions.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 429

Request has been rate limited.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An array of errors related to the operation. |
| `traceId` | string | No | A unique identifier for tracing the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional properties relating to the error. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `source` | object | No | References to the source of the error. |
| `status` | integer | No | The HTTP status code. |

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
// qlik-api has not implemented support for `PATCH /api/v1/groups/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/groups/settings',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/syncIdpGroups',
        value: true,
      },
      {
        op: 'replace',
        path: '/autoCreateGroups',
        value: true,
      },
      {
        op: 'replace',
        path: '/systemGroups/000000000000000000000001/assignedRoles',
        value: [{ name: 'Steward' }],
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/groups/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/groups/settings" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/syncIdpGroups","value":true},{"op":"replace","path":"/autoCreateGroups","value":true},{"op":"replace","path":"/systemGroups/000000000000000000000001/assignedRoles","value":[{"name":"Steward"}]}]'
```

---
