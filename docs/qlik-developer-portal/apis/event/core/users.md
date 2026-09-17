---
source: https://qlik.dev/apis/event/core/users/
last_updated: 2026-08-31T15:18:51+02:00
---

# Users

Events emitted when users are created or deleted in a Qlik Cloud tenant.

## Table of Contents

### system-events.users

- [com.qlik.core.user.created](#comqlikcoreusercreated)
- [com.qlik.core.user.deleted](#comqlikcoreuserdeleted)
- [com.qlik.core.user.provisioned](#comqlikcoreuserprovisioned)
- [com.qlik.core.user.updated](#comqlikcoreuserupdated)

## Events published on the `system-events.users` channel

### com.qlik.core.user.created

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
| `type` | `string` | Yes | The type of the event. Metadata: default = "com.qlik.core.user.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `oneOf(user \| botUser)` | No | The event data payload containing created user details. The payload conforms to the `user` schema for human users, or the `botUser` schema for bot (service) accounts. |

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
| `groups` | `string[]` | No | References to IdP groups assigned to the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date-time". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |
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
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date-time". |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |

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
  "type": "com.qlik.core.user.created",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
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
        "id": "507f191e810c19729de860ea",
        "name": "Finance",
        "providerType": "custom",
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


### com.qlik.core.user.deleted

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
| `type` | `string` | Yes | The type of the event. Metadata: default = "com.qlik.core.user.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `oneOf(user \| botUser)` | No | The event data payload containing deleted user details. The payload conforms to the `user` schema for human users, or the `botUser` schema for bot (service) accounts. |

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
| `groups` | `string[]` | No | References to IdP groups assigned to the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date-time". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |
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
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date-time". |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |

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
  "type": "com.qlik.core.user.deleted",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
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
        "id": "507f191e810c19729de860ea",
        "name": "Finance",
        "providerType": "custom",
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


### com.qlik.core.user.provisioned

**Title:** User provisioned

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new user is provisioned by an IdP.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of the event. Metadata: default = "com.qlik.core.user.provisioned". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `provisionedUser` | No | The event data payload containing provisioned user details. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | No | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the provisioned user within the tenant. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | No | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was provisioned. Metadata: format = "date-time". |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-04-21T13:45:30Z",
  "type": "com.qlik.core.user.provisioned",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "507f191e810c19729de860ea",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "locale": "en-US",
    "status": "provisioned",
    "subject": "auth0\\user123",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "zoneinfo": "America/New_York",
    "createdAt": "2025-11-25T10:30:00Z",
    "lastUpdatedAt": "2025-11-25T10:30:00Z"
  }
}
```


### com.qlik.core.user.updated

**Title:** User updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a user is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The type of the event. Metadata: default = "com.qlik.core.user.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference", default = "com.qlik/identities". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `oneOf(user \| botUser)` | No | The event data payload containing updated user details. It combines the `_updates` change set (see the `updateObject` schema) with the updated user record, which conforms to the `user` schema for human users, or the `botUser` schema for bot (service) accounts. |

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
| `groups` | `string[]` | No | References to IdP groups assigned to the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date-time". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |
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
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date-time". |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |

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
  "type": "com.qlik.core.user.updated",
  "source": "com.qlik/identities",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "_updates": [
      {
        "path": "/name",
        "newValue": "Dan",
        "oldValue": "Dylan"
      },
      {
        "path": "/email",
        "newValue": "dan@example.com",
        "oldValue": "dylan@example.com"
      }
    ]
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
| `providerType` | `string` | No | The provider type of the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |

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
| `createdAt` | `string` | No | The timestamp for when the bot user record was created. Metadata: format = "date-time". |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the bot user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |

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
| `providerType` | `string` | No | The provider type of the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |

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



### provisionedUser

The event data payload containing provisioned user details.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | No | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the provisioned user within the tenant. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | No | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was provisioned. Metadata: format = "date-time". |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |



### updateObject

Object representing the updates performed on a resource.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `_updates` | `object[]` | No | Collection of updates performed on the resource. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Field that was updated. |
| `newValue` | `` | No | JSON value of the field after the update. The value can be a scalar, array, object, or null, depending on the field. |
| `oldValue` | `` | No | JSON value of the field before the update. The value can be a scalar, array, object, or null, depending on the field. |

</details>



### user

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique user identifier. Metadata: format = "uid". |
| `name` | `string` | Yes | The name of the user. |
| `email` | `string` | No | The email address for the user. |
| `groups` | `string[]` | No | References to IdP groups assigned to the user. |
| `locale` | `string` | No | Represents the end-user's language tag. |
| `status` | `string` | No | The status of the user within the tenant. Allowed values: active \| invited \| disabled \| deleted. |
| `picture` | `string` | No | A static url linking to the avatar of the user. Metadata: format = "url". |
| `subject` | `string` | Yes | The unique user identifier from an identity provider. |
| `tenantId` | `string` | Yes | The tenant that the user belongs to. Metadata: format = "uid". |
| `zoneinfo` | `string` | No | Represents the end-user's time zone. |
| `createdAt` | `string` | No | The timestamp for when the user record was created. Metadata: format = "date-time". |
| `inviteExpiry` | `number` | No | The number of seconds until the user invitation will expire. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |
| `lastUpdatedAt` | `string` | No | The timestamp for when the user record was last updated. Metadata: format = "date-time". |
| `assignedGroups` | `assignedGroups[]` | No | A group assigned to the user. |
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
| `providerType` | `string` | No | The provider type of the group. Allowed values: idp \| custom. |
| `assignedRoles` | `assignedRoles[]` | No | A role assigned to the user. |

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


