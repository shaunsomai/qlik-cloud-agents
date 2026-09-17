# Roles

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Tenant roles are assigned to users or groups in the tenant, and define what permissions they have.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/roles`](#get-apiv1roles) | Returns a list of roles using cursor-based pagination. |
| `POST` | [`/api/v1/roles`](#post-apiv1roles) | Creates a custom role. Role names must be unique, and there is a maximum of 500 custom roles per tenant. Requestor must be assigned the `TenantAdmin` role. |
| `GET` | [`/api/v1/roles/{id}`](#get-apiv1rolesid) | Returns the requested role. |
| `PATCH` | [`/api/v1/roles/{id}`](#patch-apiv1rolesid) | Updates the requested role. Only applicable to roles of type `custom`. Requestor must be assigned the `TenantAdmin` role. |
| `DELETE` | [`/api/v1/roles/{id}`](#delete-apiv1rolesid) | Deletes the requested role. Role can only be deleted if it has been unassigned from all users and groups. Only applicable to roles of type `custom`. Requestor must be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/v1/roles

Returns a list of roles using cursor-based pagination.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. All conditional statements within this query parameter are case insensitive. |
| `limit` | number | No | The number of roles to retrieve. |
| `next` | string | No | The next page cursor. |
| `prev` | string | No | The previous page cursor. |
| `sort` | string | No | Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending. |
| `totalResults` | boolean | No | Determines wether to return a count of the total records matched in the query. Defaults to false. |

#### Responses

##### 200

An array of roles, and pagination links.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | An array of roles. |
| `links` | object | Yes | Contains pagination links |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |
| `name` | string | Yes | The name of the role. |
| `type` | string | Yes | The type of role. Enum: "default", "custom" |
| `level` | string | No | The level of access associated to the role. Enum: "admin", "user" |
| `links` | object | Yes | Contains links for the role. |
| `canEdit` | boolean | No | Indicate if role can be edited by tenant (Shown as Profile in MC) |
| `fullUser` | boolean | No | _(deprecated)_ DEPRECATED. Use userEntitlementType instead for impact of roles on user entitlements with a capacity-based subscription. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the given Role. |
| `canDelete` | boolean | No | Indicate if role can be deleted |
| `createdAt` | string | Yes | The timestamp for when the role was created. |
| `createdBy` | string | No | Id of user that created role |
| `updatedBy` | string | No | Id of user that last updated this role |
| `description` | string | Yes | Descriptive text for the role. |
| `permissions` | string[] | No | An array of permissions associated with the role. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the role was last updated. |
| `assignedScopes` | string[] | No | Selection of scopes added to this Role |
| `userEntitlementType` | string | No | Indicate whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. Returns fullUser if it will trigger promotion. |

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

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | Link to the next page of items |
| `prev` | object | No | Link to the previous page of items |
| `self` | object | Yes | Link to the current page of items |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Invalid request parameters for querying roles.

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
// qlik-api has not implemented support for `GET /api/v1/roles` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/roles', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/roles yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/roles" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "My Custom Role",
      "type": "custom",
      "level": "user",
      "links": {
        "self": {
          "href": "http://mytenant.us.qlikcloud.com/api/v1/roles/507f191e810c19729de860ea"
        }
      },
      "canEdit": false,
      "fullUser": true,
      "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
      "canDelete": false,
      "createdAt": "2021-03-21T17:32:28Z",
      "createdBy": "string",
      "updatedBy": "string",
      "description": "Grants permission to edit resource 'foo'",
      "permissions": [
        "edit_foo"
      ],
      "lastUpdatedAt": "2021-03-22T10:01:02Z",
      "assignedScopes": [
        "string"
      ],
      "userEntitlementType": "fullUser"
    }
  ],
  "links": {
    "next": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/roles?next=QaFdFYW6pImZvRgFaDyB1UffNgfs4mRd"
    },
    "prev": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/roles?prev=QaFdFYW6pImZvRgFaDyB1UffNgfs4mRd"
    },
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/roles"
    }
  },
  "totalResults": 42
}
```

---

### POST /api/v1/roles

Creates a custom role. Role names must be unique, and there is a maximum of 500 custom roles per tenant. Requestor must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Role name, needs to be unique |
| `description` | string | No | Role description |
| `assignedScopes` | string[] | No | Selection of scopes to assign to role |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |
| `name` | string | Yes | The name of the role. |
| `type` | string | Yes | The type of role. Enum: "default", "custom" |
| `level` | string | No | The level of access associated to the role. Enum: "admin", "user" |
| `links` | object | Yes | Contains links for the role. |
| `canEdit` | boolean | No | Indicate if role can be edited by tenant (Shown as Profile in MC) |
| `fullUser` | boolean | No | _(deprecated)_ DEPRECATED. Use userEntitlementType instead for impact of roles on user entitlements with a capacity-based subscription. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the given Role. |
| `canDelete` | boolean | No | Indicate if role can be deleted |
| `createdAt` | string | Yes | The timestamp for when the role was created. |
| `createdBy` | string | No | Id of user that created role |
| `updatedBy` | string | No | Id of user that last updated this role |
| `description` | string | Yes | Descriptive text for the role. |
| `permissions` | string[] | No | An array of permissions associated with the role. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the role was last updated. |
| `assignedScopes` | string[] | No | Selection of scopes added to this Role |
| `userEntitlementType` | string | No | Indicate whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. Returns fullUser if it will trigger promotion. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the role. |

</details>

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to create role.

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from creating role.

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
// qlik-api has not implemented support for `POST /api/v1/roles` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/roles', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'string',
    description: 'string',
    assignedScopes: ['string'],
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/roles yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/roles" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","description":"string","assignedScopes":["string"]}'
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "My Custom Role",
  "type": "custom",
  "level": "user",
  "links": {
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/roles/507f191e810c19729de860ea"
    }
  },
  "canEdit": false,
  "fullUser": true,
  "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
  "canDelete": false,
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "string",
  "updatedBy": "string",
  "description": "Grants permission to edit resource 'foo'",
  "permissions": [
    "edit_foo"
  ],
  "lastUpdatedAt": "2021-03-22T10:01:02Z",
  "assignedScopes": [
    "string"
  ],
  "userEntitlementType": "fullUser"
}
```

---

### GET /api/v1/roles/{id}

Returns the requested role.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |

#### Responses

##### 200

Request successfully completed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |
| `name` | string | Yes | The name of the role. |
| `type` | string | Yes | The type of role. Enum: "default", "custom" |
| `level` | string | No | The level of access associated to the role. Enum: "admin", "user" |
| `links` | object | Yes | Contains links for the role. |
| `canEdit` | boolean | No | Indicate if role can be edited by tenant (Shown as Profile in MC) |
| `fullUser` | boolean | No | _(deprecated)_ DEPRECATED. Use userEntitlementType instead for impact of roles on user entitlements with a capacity-based subscription. |
| `tenantId` | string | Yes | The tenant unique identifier associated with the given Role. |
| `canDelete` | boolean | No | Indicate if role can be deleted |
| `createdAt` | string | Yes | The timestamp for when the role was created. |
| `createdBy` | string | No | Id of user that created role |
| `updatedBy` | string | No | Id of user that last updated this role |
| `description` | string | Yes | Descriptive text for the role. |
| `permissions` | string[] | No | An array of permissions associated with the role. |
| `lastUpdatedAt` | string | Yes | The timestamp for when the role was last updated. |
| `assignedScopes` | string[] | No | Selection of scopes added to this Role |
| `userEntitlementType` | string | No | Indicate whether this role will trigger promotion of a user from a basic to a full user on tenants with a capacity-based subscription. Does not apply to tenants with a user-based subscription. Returns fullUser if it will trigger promotion. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | Link to the role. |

</details>

</details>

##### 404

Role ID not found or Invalid format.

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
// qlik-api has not implemented support for `GET /api/v1/roles/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/roles/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/roles/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/roles/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "507f191e810c19729de860ea",
  "name": "My Custom Role",
  "type": "custom",
  "level": "user",
  "links": {
    "self": {
      "href": "http://mytenant.us.qlikcloud.com/api/v1/roles/507f191e810c19729de860ea"
    }
  },
  "canEdit": false,
  "fullUser": true,
  "tenantId": "q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f",
  "canDelete": false,
  "createdAt": "2021-03-21T17:32:28Z",
  "createdBy": "string",
  "updatedBy": "string",
  "description": "Grants permission to edit resource 'foo'",
  "permissions": [
    "edit_foo"
  ],
  "lastUpdatedAt": "2021-03-22T10:01:02Z",
  "assignedScopes": [
    "string"
  ],
  "userEntitlementType": "fullUser"
}
```

---

### PATCH /api/v1/roles/{id}

Updates the requested role. Only applicable to roles of type `custom`. Requestor must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "replace", "add", "remove-value" |
| `path` | string | Yes | Enum: "/name", "/description", "/assignedScopes", "/assignedScopes/-" |
| `value` | string \| array | Yes |  |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string[] | No |  |

</details>

#### Responses

##### 204

Updated

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to update role.

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from updating role.

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Role ID not found or Invalid format.

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
// qlik-api has not implemented support for `PATCH /api/v1/roles/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/roles/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'Role1',
      },
      {
        op: 'replace',
        path: '/assignedScopes',
        value: ['knowledgebase'],
      },
      {
        op: 'add',
        path: '/assignedScopes/-',
        value: 'knowledgebase',
      },
      {
        op: 'remove-value',
        path: '/assignedScopes',
        value: 'knowledgebase',
      },
      {
        op: 'replace',
        path: '/description',
        value: 'My custom role description',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/roles/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/roles/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"Role1"},{"op":"replace","path":"/assignedScopes","value":["knowledgebase"]},{"op":"add","path":"/assignedScopes/-","value":"knowledgebase"},{"op":"remove-value","path":"/assignedScopes","value":"knowledgebase"},{"op":"replace","path":"/description","value":"My custom role description"}]'
```

---

### DELETE /api/v1/roles/{id}

Deletes the requested role. Role can only be deleted if it has been unassigned from all users and groups. Only applicable to roles of type `custom`. Requestor must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the role. |

#### Responses

##### 204

Deleted successfully.

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to delete role.

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

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from deleting role.

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
// qlik-api has not implemented support for `DELETE /api/v1/roles/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/roles/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/roles/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/roles/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
