---
source: https://qlik.dev/apis/event/users/
last_updated: 2026-04-10T12:07:03Z
---

# Users

Events emitted when users are created or deleted in a Qlik Cloud tenant.

## Table of Contents

### system-events.users

- [com.qlik.v1.user.created](#comqlikv1usercreated)
- [com.qlik.v1.user.deleted](#comqlikv1userdeleted)

## Events published on the `system-events.users` channel

### com.qlik.v1.user.created

**Title:** User created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new user is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.user.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `oneOf(user \| botUser)` | No | The event data payload containing created user details. |

<details>
<summary>Properties of `data`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `user` | `user` | No |  |

<details>
<summary>Properties of `user`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `groups` | `string[]` | No | Users assigned idp group references. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |
| `preferredLocale` | `string` | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | `string` | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `botUser` | `botUser` | No |  |

<details>
<summary>Properties of `botUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique bot user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the bot user. |
| `groups` | `string[]` | No | Group names associated to the bot user. |
| `status` | `string` | No | The status of the bot user within the tenant. Allowed values: active \| disabled \| deleted. |
| `subject` | `string` | Yes | The unique bot user identifier which incorporates the client ID. |
| `clientId` | `string` | Yes | The OAuth client ID that the bot user belongs to. |
| `tenantId` | `string` | Yes | The tenant that the bot user belongs to. Metadata: format = "uid". |
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date". |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.user.created",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f191e810c19729de860ea",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "string",
    "email": "string",
    "groups": [
      "group1",
      "group2"
    ],
    "locale": "string",
    "status": "active",
    "picture": "http://example.com",
    "subject": "string",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "zoneinfo": "string",
    "createdAt": "string",
    "inviteExpiry": 42,
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "string",
    "assignedGroups": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "Finance",
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
    "preferredLocale": "string",
    "preferredZoneinfo": "string"
  }
}
```


### com.qlik.v1.user.deleted

**Title:** User deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.user.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `oneOf(user \| botUser)` | No | The event data payload containing deleted user details. |

<details>
<summary>Properties of `data`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `user` | `user` | No |  |

<details>
<summary>Properties of `user`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `groups` | `string[]` | No | Users assigned idp group references. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |
| `preferredLocale` | `string` | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | `string` | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `botUser` | `botUser` | No |  |

<details>
<summary>Properties of `botUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique bot user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the bot user. |
| `groups` | `string[]` | No | Group names associated to the bot user. |
| `status` | `string` | No | The status of the bot user within the tenant. Allowed values: active \| disabled \| deleted. |
| `subject` | `string` | Yes | The unique bot user identifier which incorporates the client ID. |
| `clientId` | `string` | Yes | The OAuth client ID that the bot user belongs to. |
| `tenantId` | `string` | Yes | The tenant that the bot user belongs to. Metadata: format = "uid". |
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date". |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.v1.user.deleted",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "507f191e810c19729de860ea",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "name": "string",
    "email": "string",
    "groups": [
      "group1",
      "group2"
    ],
    "locale": "string",
    "status": "active",
    "picture": "http://example.com",
    "subject": "string",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "zoneinfo": "string",
    "createdAt": "string",
    "inviteExpiry": 42,
    "assignedRoles": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "My Custom Role",
        "type": "custom",
        "level": "user"
      }
    ],
    "lastUpdatedAt": "string",
    "assignedGroups": [
      {
        "id": "507f191e810c19729de860ea",
        "name": "Finance",
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
    "preferredLocale": "string",
    "preferredZoneinfo": "string"
  }
}
```


## Schemas

### assignedGroups

**Type:** `object[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique group identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The group name |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |

</details>



### assignedRoles

**Type:** `object[]`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |



### botUser

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique bot user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the bot user. |
| `groups` | `string[]` | No | Group names associated to the bot user. |
| `status` | `string` | No | The status of the bot user within the tenant. Allowed values: active \| disabled \| deleted. |
| `subject` | `string` | Yes | The unique bot user identifier which incorporates the client ID. |
| `clientId` | `string` | Yes | The OAuth client ID that the bot user belongs to. |
| `tenantId` | `string` | Yes | The tenant that the bot user belongs to. Metadata: format = "uid". |
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date". |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique group identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The group name |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |

</details>

</details>



### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### user

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `groups` | `string[]` | No | Users assigned idp group references. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date". |
| `assignedGroups` | `assignedGroups[]` | No | represents a group entity stored in the database |
| `preferredLocale` | `string` | No | Represents the end-user's preferred language tag. |
| `preferredZoneinfo` | `string` | No | Represents the end-user's preferred time zone. |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |

</details>

<details>
<summary>Properties of `assignedGroups`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique group identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The group name |
| `assignedRoles` | `assignedRoles[]` | No | represents a role entity stored in the database |

<details>
<summary>Properties of `assignedRoles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique role identifier Metadata: format = "uid". |
| `name` | `string` | Yes | The role name |
| `type` | `string` | Yes | The type of role Allowed values: default \| custom. |
| `level` | `string` | Yes | The role level Allowed values: admin \| user. |

</details>

</details>


