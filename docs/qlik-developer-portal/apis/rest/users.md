# Users

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Users represent clients accessing the Qlik Cloud tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/users`](#get-apiv1users) | Returns a list of users using cursor-based pagination. |
| `POST` | [`/api/v1/users`](#post-apiv1users) | Creates an invited user. |
| `GET` | [`/api/v1/users/{userId}`](#get-apiv1usersuserid) | Returns the requested user. |
| `PATCH` | [`/api/v1/users/{userId}`](#patch-apiv1usersuserid) | Updates fields for a user resource |
| `DELETE` | [`/api/v1/users/{userId}`](#delete-apiv1usersuserid) | Deletes the requested user. |
| `GET` | [`/api/v1/users/actions/count`](#get-apiv1usersactionscount) | Returns the number of users in a given tenant |
| `POST` | [`/api/v1/users/actions/filter`](#post-apiv1usersactionsfilter) | Retrieves a list of users matching the filter using an advanced query string. |
| `POST` | [`/api/v1/users/actions/invite`](#post-apiv1usersactionsinvite) |  |
| `GET` | [`/api/v1/users/me`](#get-apiv1usersme) | Redirects to retrieve the user resource associated with the JWT claims. |

## API Reference

### GET /api/v1/users

Returns a list of users using cursor-based pagination.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | string | No | A comma-delimited string of the requested fields per entity. If the 'links' value is omitted, then the entity HATEOAS link will also be omitted. |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive.  The following fields support the `eq` operator: `id`, `subject`, `name`, `email`, `status`, `clientId`, `assignedRoles.id`, `assignedRoles.name`, `assignedGroups.id`, `assignedGroupsAssignedRoles.name`, `assignedScopes`  Additionally, the following fields support the `co` operator: `name`, `email`, `subject`  Queries may be rate limited if they differ greatly from these examples:  ``` (id eq "62716ab404a7bd8626af9bd6" or id eq "62716ac4c7e500e13ff5fa22") and (status eq "active" or status eq "disabled") ```  ``` name co "query" or email co "query" or subject co "query" or id eq "query" or assignedRoles.name eq "query" ```  Any filters for status must be grouped together and applied to the whole query.  Valid:  ``` (name eq "Bob" or name eq "Alice") and (status eq "active" or status eq "disabled") ```  Invalid:  ``` name eq "Bob" or name eq "Alice" and (status eq "active" or status eq "disabled") ``` |
| `limit` | number | No | The number of user entries to retrieve. |
| `next` | string | No | Get users that come after this cursor value when sorted. Cannot be used in conjunction with `prev`. |
| `prev` | string | No | Get users that come before this cursor value when sorted. Cannot be used in conjunction with `next`. |
| `sort` | string | No | The field to sort by, with +/- prefix indicating sort order Enum: "name", "+name", "-name", "_id", "+_id", "-_id", "id", "+id", "-id", "tenantId", "+tenantId", "-tenantId", "clientId", "+clientId", "-clientId", "status", "+status", "-status", "subject", "+subject", "-subject", "email", "+email", "-email", "inviteExpiry", "+inviteExpiry", "-inviteExpiry", "createdAt", "+createdAt", "-createdAt" |
| `totalResults` | boolean | No | Whether to return a total match count in the result. Defaults to false. It will trigger an extra DB query to count, reducing the efficiency of the endpoint. |

#### Responses

##### 200

Successful query, returns an array of users

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | List of users. |
| `links` | object | No | Pagination links |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique user identifier. |
| `name` | string | Yes | The name of the user. |
| `email` | string | No | The email address for the user. |
| `links` | object | No | Pagination links to the user. |
| `locale` | string | No | Represents the end-user's language tag. |
| `status` | string | No | The status of the user within the tenant. Enum: "active", "invited", "disabled", "deleted", "provisioned" |
| `picture` | string | No | A static url linking to the avatar of the user. |
| `subject` | string | Yes | The unique user identitier from an identity provider. |
| `tenantId` | string | Yes | The tenant that the user belongs too. |
| `zoneinfo` | string | No | Represents the end-user's time zone. |
| `createdAt` | string | No | The timestamp for when the user record was created. |
| `inviteExpiry` | number | No | The Unix timestamp indicating when the invite will expire. |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | No | The timestamp for when the user record was last updated. |
| `assignedGroups` | object[] | No | An array of group references. |
| `assignedScopes` | string[] | No | An array of scopes assigned to a user |
| `preferredLocale` | string | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | string | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this user. |

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

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique group identitier |
| `name` | string | Yes | The group name |
| `providerType` | string | No | The provider type of the group Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | Link information for next page |
| `prev` | object | No | Link information for previous page |
| `self` | object | Yes | Link information for current page |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the next page of records |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the previous page of records |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the current page of records |

</details>

</details>

##### 400

Invalid request parameters for querying users.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/users` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/users', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/users yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "string",
      "email": "string",
      "links": {
        "self": {
          "href": "http://mytenant.elastic.example/api/v1/users/DKNmFJCNo8SGURUdh2ll--------USER"
        }
      },
      "locale": "string",
      "status": "active",
      "picture": "http://example.com",
      "subject": "string",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "zoneinfo": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "inviteExpiry": 42,
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "My Custom Role",
          "type": "custom",
          "level": "user"
        }
      ],
      "lastUpdatedAt": "2018-10-30T07:06:22Z",
      "assignedGroups": [
        {
          "id": "507f191e810c19729de860eb",
          "name": "Finance",
          "providerType": "idp",
          "assignedRoles": [
            {
              "id": "507f191e810c19729de860ea",
              "name": "My Custom Role",
              "type": "custom",
              "level": "user"
            }
          ]
        }
      ],
      "assignedScopes": [
        "string"
      ],
      "preferredLocale": "string",
      "preferredZoneinfo": "string"
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
  },
  "totalResults": 42
}
```

---

### POST /api/v1/users

Creates an invited user.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The name of the user. |
| `email` | string | No | The email address for the user. This is a required field when inviting a user. |
| `status` | string | No | The status of the created user within the tenant. Enum: "invited" |
| `picture` | string | No | A static url linking to the avatar of the user. |
| `subject` | string | Yes | The unique user identitier from an identity provider. |
| `tenantId` | string | No | The tenant that the user will belong too. |
| `assignedRoles` | array | No | The roles to assign to the user. |

<details>
<summary>Properties of `assignedRoles`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RefIDs` | object[] | No | An array of entity reference identifiers (e.g. roles, groups). |

<details>
<summary>Properties of `RefIDs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identitier |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RefNames` | object[] | No | An array of reference names (e.g. roles). |

<details>
<summary>Properties of `RefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the entity |

</details>

</details>

#### Responses

##### 201

User created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique user identifier. |
| `name` | string | Yes | The name of the user. |
| `email` | string | No | The email address for the user. |
| `links` | object | No | Pagination links to the user. |
| `locale` | string | No | Represents the end-user's language tag. |
| `status` | string | No | The status of the user within the tenant. Enum: "active", "invited", "disabled", "deleted", "provisioned" |
| `picture` | string | No | A static url linking to the avatar of the user. |
| `subject` | string | Yes | The unique user identitier from an identity provider. |
| `tenantId` | string | Yes | The tenant that the user belongs too. |
| `zoneinfo` | string | No | Represents the end-user's time zone. |
| `createdAt` | string | No | The timestamp for when the user record was created. |
| `inviteExpiry` | number | No | The Unix timestamp indicating when the invite will expire. |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | No | The timestamp for when the user record was last updated. |
| `assignedGroups` | object[] | No | An array of group references. |
| `assignedScopes` | string[] | No | An array of scopes assigned to a user |
| `preferredLocale` | string | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | string | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this user. |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

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

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique group identitier |
| `name` | string | Yes | The group name |
| `providerType` | string | No | The provider type of the group Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 401

Unauthorized to create a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from creating a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 409

User conflict when attempting to create a new user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 413

Payload was too large (limit of 500kB)

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `POST /api/v1/users` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'John Smith',
    email: 'john.smith@corp.example',
    status: 'invited',
    picture:
      'https://corp.example/docs/jsmith.png',
    subject: '1234asdasa6789',
    tenantId: 'q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f',
    assignedRoles: [{ name: 'My Custom Role' }],
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/users yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"John Smith","email":"john.smith@corp.example","status":"invited","picture":"https://corp.example/docs/jsmith.png","subject":"1234asdasa6789","tenantId":"q3VRZ4YMixRaLKEPhkZWM-XMIDN7cO8f","assignedRoles":[{"name":"My Custom Role"}]}'
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "string",
  "email": "string",
  "links": {
    "self": {
      "href": "http://mytenant.elastic.example/api/v1/users/DKNmFJCNo8SGURUdh2ll--------USER"
    }
  },
  "locale": "string",
  "status": "active",
  "picture": "http://example.com",
  "subject": "string",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "zoneinfo": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "inviteExpiry": 42,
  "assignedRoles": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "My Custom Role",
      "type": "custom",
      "level": "user"
    }
  ],
  "lastUpdatedAt": "2018-10-30T07:06:22Z",
  "assignedGroups": [
    {
      "id": "507f191e810c19729de860eb",
      "name": "Finance",
      "providerType": "idp",
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "My Custom Role",
          "type": "custom",
          "level": "user"
        }
      ]
    }
  ],
  "assignedScopes": [
    "string"
  ],
  "preferredLocale": "string",
  "preferredZoneinfo": "string"
}
```

---

### GET /api/v1/users/{userId}

Returns the requested user.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | Yes | The user's unique identifier |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | string | No | A comma-delimited string of the requested fields per entity. If the 'links' value is omitted, then the entity HATEOAS link will also be omitted. |

#### Responses

##### 200

User resource

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique user identifier. |
| `name` | string | Yes | The name of the user. |
| `email` | string | No | The email address for the user. |
| `links` | object | No | Pagination links to the user. |
| `locale` | string | No | Represents the end-user's language tag. |
| `status` | string | No | The status of the user within the tenant. Enum: "active", "invited", "disabled", "deleted", "provisioned" |
| `picture` | string | No | A static url linking to the avatar of the user. |
| `subject` | string | Yes | The unique user identitier from an identity provider. |
| `tenantId` | string | Yes | The tenant that the user belongs too. |
| `zoneinfo` | string | No | Represents the end-user's time zone. |
| `createdAt` | string | No | The timestamp for when the user record was created. |
| `inviteExpiry` | number | No | The Unix timestamp indicating when the invite will expire. |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | No | The timestamp for when the user record was last updated. |
| `assignedGroups` | object[] | No | An array of group references. |
| `assignedScopes` | string[] | No | An array of scopes assigned to a user |
| `preferredLocale` | string | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | string | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this user. |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL that defines the resource. |

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

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique group identitier |
| `name` | string | Yes | The group name |
| `providerType` | string | No | The provider type of the group Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |

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

##### 403

Forbidden from getting a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

User was not found.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/users/{userId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/{userId}',
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
# qlik-cli has not implemented support for GET /api/v1/users/{userId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/{userId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "string",
  "email": "string",
  "links": {
    "self": {
      "href": "http://mytenant.elastic.example/api/v1/users/DKNmFJCNo8SGURUdh2ll--------USER"
    }
  },
  "locale": "string",
  "status": "active",
  "picture": "http://example.com",
  "subject": "string",
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "zoneinfo": "string",
  "createdAt": "2018-10-30T07:06:22Z",
  "inviteExpiry": 42,
  "assignedRoles": [
    {
      "id": "507f191e810c19729de860ea",
      "name": "My Custom Role",
      "type": "custom",
      "level": "user"
    }
  ],
  "lastUpdatedAt": "2018-10-30T07:06:22Z",
  "assignedGroups": [
    {
      "id": "507f191e810c19729de860eb",
      "name": "Finance",
      "providerType": "idp",
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "My Custom Role",
          "type": "custom",
          "level": "user"
        }
      ]
    }
  ],
  "assignedScopes": [
    "string"
  ],
  "preferredLocale": "string",
  "preferredZoneinfo": "string"
}
```

---

### PATCH /api/v1/users/{userId}

Updates fields for a user resource

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | Yes | The ID of the user to update. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. The fields `set` and `unset` are deprecated. Enum: "replace", "set", "unset", "add", "renew", "remove-value" |
| `path` | string | Yes | A JSON Pointer. The field `roles` is deprecated. Enum: "/name", "/roles", "/assignedRoles", "/inviteExpiry", "/preferredZoneinfo", "/preferredLocale", "/status", "/assignedGroups" |
| `value` | string \| boolean \| array | Yes | The value to be used for this operation. |

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
| `` | boolean | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | array | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RefIDs` | object[] | No | An array of entity reference identifiers (e.g. roles, groups). |

<details>
<summary>Properties of `RefIDs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identitier |

</details>

**Option 5:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `RefNames` | object[] | No | An array of reference names (e.g. roles). |

<details>
<summary>Properties of `RefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the entity |

</details>

**Option 6:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AssignedGroupsRefNames` | object[] | No | An array of group reference names and provider type. |

<details>
<summary>Properties of `AssignedGroupsRefNames`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the group |
| `providerType` | string | Yes | The type of provider for the group. Enum: "idp", "custom" |

</details>

</details>

#### Responses

##### 204

User updated successfully.

##### 207

User update was partially successful with non-critical failures.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from patching a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

User was not found.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `PATCH /api/v1/users/{userId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/{userId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'John',
      },
      {
        op: 'replace',
        path: '/assignedRoles',
        value: [{ name: 'My Custom Role' }],
      },
      {
        op: 'replace',
        path: '/email',
        value: 'unicorn@corp.example',
      },
      {
        op: 'replace',
        path: '/preferredZoneInfo',
        value: 'America/Halifax',
      },
      {
        op: 'replace',
        path: '/preferredLocale',
        value: 'en_US_POSIX',
      },
      {
        op: 'replace',
        path: '/status',
        value: 'active',
      },
      {
        op: 'add',
        path: '/assignedRoles/-',
        value: { name: 'TenantAdmin' },
      },
      {
        op: 'remove-value',
        path: '/assignedRoles',
        value: { id: '67ac386d2bab6dd4925008e8' },
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/users/{userId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/{userId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"John"},{"op":"replace","path":"/assignedRoles","value":[{"name":"My Custom Role"}]},{"op":"replace","path":"/email","value":"unicorn@corp.example"},{"op":"replace","path":"/preferredZoneInfo","value":"America/Halifax"},{"op":"replace","path":"/preferredLocale","value":"en_US_POSIX"},{"op":"replace","path":"/status","value":"active"},{"op":"add","path":"/assignedRoles/-","value":{"name":"TenantAdmin"}},{"op":"remove-value","path":"/assignedRoles","value":{"id":"67ac386d2bab6dd4925008e8"}}]'
```

**Example Response:**

```json
{
  "errors": [
    {
      "code": "USERS-7",
      "title": "Not found",
      "status": 404
    }
  ],
  "traceId": "000000000000000079cf1ebeae103de1"
}
```

---

### DELETE /api/v1/users/{userId}

Deletes the requested user.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | Yes | The ID of the user to delete. |

#### Responses

##### 204

User deleted successfully.

##### 400

Invalid request for deleting a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

Forbidden from deleting a user.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

User was not found.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `DELETE /api/v1/users/{userId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/{userId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/users/{userId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/{userId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/users/actions/count

Returns the number of users in a given tenant

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The count of users.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | number | Yes | The total number of users in the tenant. |

##### 403

Forbidden from reading the count.

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 404

Not found.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/users/actions/count` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/actions/count',
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
# qlik-cli has not implemented support for GET /api/v1/users/actions/count yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/actions/count" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "total": 42
}
```

---

### POST /api/v1/users/actions/filter

Retrieves a list of users matching the filter using an advanced query string.

- **Rate Limit:** Special (200 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | string | No | A comma-delimited string of the requested fields per entity. If the 'links' value is omitted, then the entity HATEOAS link will also be omitted. |
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

Users retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | List of users. |
| `links` | object | No | Pagination links |
| `totalResults` | integer | No | Indicates the total number of matching documents. Will only be returned if the query parameter "totalResults" is true. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique user identifier. |
| `name` | string | Yes | The name of the user. |
| `email` | string | No | The email address for the user. |
| `links` | object | No | Pagination links to the user. |
| `locale` | string | No | Represents the end-user's language tag. |
| `status` | string | No | The status of the user within the tenant. Enum: "active", "invited", "disabled", "deleted", "provisioned" |
| `picture` | string | No | A static url linking to the avatar of the user. |
| `subject` | string | Yes | The unique user identitier from an identity provider. |
| `tenantId` | string | Yes | The tenant that the user belongs too. |
| `zoneinfo` | string | No | Represents the end-user's time zone. |
| `createdAt` | string | No | The timestamp for when the user record was created. |
| `inviteExpiry` | number | No | The Unix timestamp indicating when the invite will expire. |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |
| `lastUpdatedAt` | string | No | The timestamp for when the user record was last updated. |
| `assignedGroups` | object[] | No | An array of group references. |
| `assignedScopes` | string[] | No | An array of scopes assigned to a user |
| `preferredLocale` | string | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | string | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | A link to this user. |

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

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique group identitier |
| `name` | string | Yes | The group name |
| `providerType` | string | No | The provider type of the group Enum: "idp", "custom" |
| `assignedRoles` | object[] | No | An array of role references. Visibility dependant on access level. Must have access to roles to view other users' assigned roles. |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | Link information for next page |
| `prev` | object | No | Link information for previous page |
| `self` | object | Yes | Link information for current page |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the next page of records |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the previous page of records |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to the current page of records |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pointer` | string | No | A JSON Pointer to the property that caused the error. |
| `parameter` | string | No | The URI query parameter that caused the error. |

</details>

</details>

##### 403

The operation failed due to unsufficient permissions.

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `POST /api/v1/users/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/actions/filter',
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
# qlik-cli has not implemented support for POST /api/v1/users/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/actions/filter" \
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
      "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "name": "string",
      "email": "string",
      "links": {
        "self": {
          "href": "http://mytenant.elastic.example/api/v1/users/DKNmFJCNo8SGURUdh2ll--------USER"
        }
      },
      "locale": "string",
      "status": "active",
      "picture": "http://example.com",
      "subject": "string",
      "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "zoneinfo": "string",
      "createdAt": "2018-10-30T07:06:22Z",
      "inviteExpiry": 42,
      "assignedRoles": [
        {
          "id": "507f191e810c19729de860ea",
          "name": "My Custom Role",
          "type": "custom",
          "level": "user"
        }
      ],
      "lastUpdatedAt": "2018-10-30T07:06:22Z",
      "assignedGroups": [
        {
          "id": "507f191e810c19729de860eb",
          "name": "Finance",
          "providerType": "idp",
          "assignedRoles": [
            {
              "id": "507f191e810c19729de860ea",
              "name": "My Custom Role",
              "type": "custom",
              "level": "user"
            }
          ]
        }
      ],
      "assignedScopes": [
        "string"
      ],
      "preferredLocale": "string",
      "preferredZoneinfo": "string"
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
  },
  "totalResults": 42
}
```

---

### POST /api/v1/users/actions/invite

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `invitees` | object[] | No | List of invitees who should receive an invite email. |

<details>
<summary>Properties of `invitees`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Optional display name for this invitee. Example - "Elvis Presley". |
| `email` | string | Yes | Email address for this invitee. Example - "foo@qlik.com". |
| `resend` | boolean | No | Flag - when true invite message is sent to inactive or invited users. Typically used to force email resend to users who are not yet active. |
| `language` | string | No | Optional ISO 639-1 2 letter code for invite language. Defaults to 'en' when missing or not found. |

</details>

#### Responses

##### 207

Request completed successfully. See Results for ResultDetail on each invite.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ResultItem` | object | No | Invitee result item |

<details>
<summary>Properties of `ResultItem`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | string | Yes | Email specified for this invitee |
| `status` | string | Yes | Result status = {"ok" (new user; email sent) \| "exists" (existing user; no email sent)} Enum: "ok", "exists" |
| `userId` | string | Yes | UserId for this invitee |
| `subject` | string | Yes | IdP generated UUID for this invitee |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `InviteErrorItem` | object | No | Error object. |

<details>
<summary>Properties of `InviteErrorItem`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Error code - \| HTTP Status code \| 1001 - Active User \| 1002 - Disabled User \| 1003 - Default External Dependency Error \| |
| `title` | string | Yes | Summary of the problem |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem (if applicable) |
| `email` | string | Yes | Invitee email |
| `status` | string | Yes | Result status = "error" Enum: "error" |

</details>

</details>

##### 403

Request denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | Yes | Error code |
| `title` | string | Yes | Summary of the problem |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem (if applicable) |

</details>

##### default

Request error. See Errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | integer | Yes | Error code |
| `title` | string | Yes | Summary of the problem |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem (if applicable) |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/users/actions/invite` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/users/actions/invite',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      invitees: [
        {
          name: 'string',
          email: 'string',
          resend: true,
          language: 'string',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/users/actions/invite yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/actions/invite" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"invitees":[{"name":"string","email":"string","resend":true,"language":"string"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "email": "string",
      "status": "ok",
      "userId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
      "subject": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
    }
  ]
}
```

---

### GET /api/v1/users/me

Redirects to retrieve the user resource associated with the JWT claims.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 301

Successful redirect.

**Content-Type:** `text/html`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/html` | string | No |  |

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
| `status` | number | No | The HTTP status code. |

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
// qlik-api has not implemented support for `GET /api/v1/users/me` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/users/me', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/users/me yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/users/me" \
-H "Authorization: Bearer <access_token>"
```

---
