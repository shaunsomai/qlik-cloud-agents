---
source: https://qlik.dev/apis/event/oauth-clients/
last_updated: 2026-04-10T12:07:03Z
---

# OAuth clients

Events emitted when OAuth clients are created, updated, deleted, published, or when their secrets and connection configurations are modified.

## Table of Contents

### system-events.oauth-clients

- [com.qlik.v1.oauth-client.connection-config.approved](#comqlikv1oauth-clientconnection-configapproved)
- [com.qlik.v1.oauth-client.connection-config.deleted](#comqlikv1oauth-clientconnection-configdeleted)
- [com.qlik.v1.oauth-client.connection-config.updated](#comqlikv1oauth-clientconnection-configupdated)
- [com.qlik.v1.oauth-client.created](#comqlikv1oauth-clientcreated)
- [com.qlik.v1.oauth-client.deleted](#comqlikv1oauth-clientdeleted)
- [com.qlik.v1.oauth-client.published](#comqlikv1oauth-clientpublished)
- [com.qlik.v1.oauth-client.secret.created](#comqlikv1oauth-clientsecretcreated)
- [com.qlik.v1.oauth-client.secret.deleted](#comqlikv1oauth-clientsecretdeleted)
- [com.qlik.v1.oauth-client.updated](#comqlikv1oauth-clientupdated)

## Events published on the `system-events.oauth-clients` channel

### com.qlik.v1.oauth-client.connection-config.approved

**Title:** OAuth client connection config approved

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a tenant admin approves an OAuth client.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.connection-config.approved". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthConnectionConfigEntry` | No | Full client connection config resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | No | Status of the connection-config for the tenant. Allowed values: approved. |
| `tenantId` | `string` | Yes | Identifier of the tenant the connection-config relates to. |
| `createdAt` | `string` | Yes | Timestamp when the connection-config was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the connection-config was updated. Metadata: format = "date-time". |
| `consentMethod` | `string` | Yes | Consent method for the connection-config. Allowed values: required \| trusted. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.connection-config.approved",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "status": "approved",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "updatedAt": "2026-10-30T07:06:22Z",
    "consentMethod": "trusted"
  }
}
```


### com.qlik.v1.oauth-client.connection-config.deleted

**Title:** OAuth client connection config deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a tenant admin revokes their access to another tenant's OAuth client by deleting the connection config.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.connection-config.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthConnectionConfigEntry` | No | Full client connection config resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | No | Status of the connection-config for the tenant. Allowed values: approved. |
| `tenantId` | `string` | Yes | Identifier of the tenant the connection-config relates to. |
| `createdAt` | `string` | Yes | Timestamp when the connection-config was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the connection-config was updated. Metadata: format = "date-time". |
| `consentMethod` | `string` | Yes | Consent method for the connection-config. Allowed values: required \| trusted. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.connection-config.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "status": "approved",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "updatedAt": "2026-10-30T07:06:22Z",
    "consentMethod": "trusted"
  }
}
```


### com.qlik.v1.oauth-client.connection-config.updated

**Title:** OAuth client connection config updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a connection config is updated by a tenant admin.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.connection-config.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthConnectionConfigEntry` | No | Full client connection config resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | No | Status of the connection-config for the tenant. Allowed values: approved. |
| `tenantId` | `string` | Yes | Identifier of the tenant the connection-config relates to. |
| `createdAt` | `string` | Yes | Timestamp when the connection-config was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the connection-config was updated. Metadata: format = "date-time". |
| `consentMethod` | `string` | Yes | Consent method for the connection-config. Allowed values: required \| trusted. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.connection-config.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "status": "approved",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "updatedAt": "2026-10-30T07:06:22Z",
    "consentMethod": "trusted"
  }
}
```


### com.qlik.v1.oauth-client.created

**Title:** OAuth client created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientEntry` | No | Full oauth-client resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | `string` | Yes | Application type for the client. Allowed values: web \| native \| spa \| anonymous-embed. |
| `logoUri` | `string` | No | URI for the logo of the client. Metadata: format = "uri". |
| `ownerId` | `string` | Yes | Identifier of the owner that created the client. |
| `clientId` | `string` | Yes | Identifier of the client. |
| `tenantId` | `string` | Yes | Identifier of the tenant where the client was created. |
| `clientUri` | `string` | No | URI for the homepage of the client. Metadata: format = "uri". |
| `createdAt` | `string` | Yes | Timestamp when the client was created. Metadata: format = "date-time". |
| `deletedAt` | `string` | No | Timestamp when the client was deleted. Metadata: format = "date-time". |
| `ownerType` | `string` | Yes | Type of owner that created the client. |
| `clientName` | `string` | Yes | Name of the client. |
| `disableTag` | `string` | No | Indicates whether the client is disabled. |
| `createdById` | `string` | Yes | Identifier of the resource that created the client. |
| `publishedAt` | `string` | No | Timestamp when the client was published. Metadata: format = "date-time". |
| `redirectUris` | `string[]` | No | List of allowed redirect URIs for logins with the client. |
| `allowedScopes` | `string[]` | No | List of allowed scopes for the client. |
| `createdByType` | `string` | Yes | Type of the resource that created the client. |
| `allowedOrigins` | `string[]` | No | List of allowed origins for the client. |
| `connectionPolicy` | `object[]` | No | Connection policies for the client. |

<details>
<summary>Properties of `connectionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "appType": "web",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "clientId": "000000000000000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "ownerType": "tenant",
    "clientName": "New oauth client",
    "createdById": "00000000-0000-0000-0000-000000000000",
    "createdByType": "user"
  }
}
```


### com.qlik.v1.oauth-client.deleted

**Title:** OAuth client deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientEntry` | No | Full oauth-client resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | `string` | Yes | Application type for the client. Allowed values: web \| native \| spa \| anonymous-embed. |
| `logoUri` | `string` | No | URI for the logo of the client. Metadata: format = "uri". |
| `ownerId` | `string` | Yes | Identifier of the owner that created the client. |
| `clientId` | `string` | Yes | Identifier of the client. |
| `tenantId` | `string` | Yes | Identifier of the tenant where the client was created. |
| `clientUri` | `string` | No | URI for the homepage of the client. Metadata: format = "uri". |
| `createdAt` | `string` | Yes | Timestamp when the client was created. Metadata: format = "date-time". |
| `deletedAt` | `string` | No | Timestamp when the client was deleted. Metadata: format = "date-time". |
| `ownerType` | `string` | Yes | Type of owner that created the client. |
| `clientName` | `string` | Yes | Name of the client. |
| `disableTag` | `string` | No | Indicates whether the client is disabled. |
| `createdById` | `string` | Yes | Identifier of the resource that created the client. |
| `publishedAt` | `string` | No | Timestamp when the client was published. Metadata: format = "date-time". |
| `redirectUris` | `string[]` | No | List of allowed redirect URIs for logins with the client. |
| `allowedScopes` | `string[]` | No | List of allowed scopes for the client. |
| `createdByType` | `string` | Yes | Type of the resource that created the client. |
| `allowedOrigins` | `string[]` | No | List of allowed origins for the client. |
| `connectionPolicy` | `object[]` | No | Connection policies for the client. |

<details>
<summary>Properties of `connectionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "appType": "web",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "clientId": "000000000000000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "ownerType": "tenant",
    "clientName": "New oauth client",
    "createdById": "00000000-0000-0000-0000-000000000000",
    "createdByType": "user"
  }
}
```


### com.qlik.v1.oauth-client.published

**Title:** OAuth client published

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client is published.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.published". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientEntry` | No | Full oauth-client resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | `string` | Yes | Application type for the client. Allowed values: web \| native \| spa \| anonymous-embed. |
| `logoUri` | `string` | No | URI for the logo of the client. Metadata: format = "uri". |
| `ownerId` | `string` | Yes | Identifier of the owner that created the client. |
| `clientId` | `string` | Yes | Identifier of the client. |
| `tenantId` | `string` | Yes | Identifier of the tenant where the client was created. |
| `clientUri` | `string` | No | URI for the homepage of the client. Metadata: format = "uri". |
| `createdAt` | `string` | Yes | Timestamp when the client was created. Metadata: format = "date-time". |
| `deletedAt` | `string` | No | Timestamp when the client was deleted. Metadata: format = "date-time". |
| `ownerType` | `string` | Yes | Type of owner that created the client. |
| `clientName` | `string` | Yes | Name of the client. |
| `disableTag` | `string` | No | Indicates whether the client is disabled. |
| `createdById` | `string` | Yes | Identifier of the resource that created the client. |
| `publishedAt` | `string` | No | Timestamp when the client was published. Metadata: format = "date-time". |
| `redirectUris` | `string[]` | No | List of allowed redirect URIs for logins with the client. |
| `allowedScopes` | `string[]` | No | List of allowed scopes for the client. |
| `createdByType` | `string` | Yes | Type of the resource that created the client. |
| `allowedOrigins` | `string[]` | No | List of allowed origins for the client. |
| `connectionPolicy` | `object[]` | No | Connection policies for the client. |

<details>
<summary>Properties of `connectionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.published",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "appType": "web",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "clientId": "000000000000000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "ownerType": "tenant",
    "clientName": "New oauth client",
    "createdById": "00000000-0000-0000-0000-000000000000",
    "createdByType": "user"
  }
}
```


### com.qlik.v1.oauth-client.secret.created

**Title:** OAuth client secret created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client secret is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.secret.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientSecretData` | No | OAuth client identifier and hint for the secret the event is related to. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | `string` | Yes | Hint for the client secret. |
| `clientId` | `string` | Yes | Identifier of the client. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.secret.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "hint": "00000",
    "clientId": "000000000000000000000000"
  }
}
```


### com.qlik.v1.oauth-client.secret.deleted

**Title:** OAuth client secret deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client secret is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.secret.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientSecretData` | No | OAuth client identifier and hint for the secret the event is related to. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | `string` | Yes | Hint for the client secret. |
| `clientId` | `string` | Yes | Identifier of the client. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.secret.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "hint": "00000",
    "clientId": "000000000000000000000000"
  }
}
```


### com.qlik.v1.oauth-client.updated

**Title:** OAuth client updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an OAuth client is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.v1.oauth-client.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `OAuthClientEntry` | No | Full oauth-client resource after the event was published. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | `string` | Yes | Application type for the client. Allowed values: web \| native \| spa \| anonymous-embed. |
| `logoUri` | `string` | No | URI for the logo of the client. Metadata: format = "uri". |
| `ownerId` | `string` | Yes | Identifier of the owner that created the client. |
| `clientId` | `string` | Yes | Identifier of the client. |
| `tenantId` | `string` | Yes | Identifier of the tenant where the client was created. |
| `clientUri` | `string` | No | URI for the homepage of the client. Metadata: format = "uri". |
| `createdAt` | `string` | Yes | Timestamp when the client was created. Metadata: format = "date-time". |
| `deletedAt` | `string` | No | Timestamp when the client was deleted. Metadata: format = "date-time". |
| `ownerType` | `string` | Yes | Type of owner that created the client. |
| `clientName` | `string` | Yes | Name of the client. |
| `disableTag` | `string` | No | Indicates whether the client is disabled. |
| `createdById` | `string` | Yes | Identifier of the resource that created the client. |
| `publishedAt` | `string` | No | Timestamp when the client was published. Metadata: format = "date-time". |
| `redirectUris` | `string[]` | No | List of allowed redirect URIs for logins with the client. |
| `allowedScopes` | `string[]` | No | List of allowed scopes for the client. |
| `createdByType` | `string` | Yes | Type of the resource that created the client. |
| `allowedOrigins` | `string[]` | No | List of allowed origins for the client. |
| `connectionPolicy` | `object[]` | No | Connection policies for the client. |

<details>
<summary>Properties of `connectionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.v1.oauth-client.updated",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "tenantid": "id123",
  "data": {
    "appType": "web",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "clientId": "000000000000000000000000",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "createdAt": "2026-10-30T07:06:22Z",
    "ownerType": "tenant",
    "clientName": "New oauth client",
    "createdById": "00000000-0000-0000-0000-000000000000",
    "createdByType": "user"
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### OAuthClientEntry

Full oauth-client resource after the event was published.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appType` | `string` | Yes | Application type for the client. Allowed values: web \| native \| spa \| anonymous-embed. |
| `logoUri` | `string` | No | URI for the logo of the client. Metadata: format = "uri". |
| `ownerId` | `string` | Yes | Identifier of the owner that created the client. |
| `clientId` | `string` | Yes | Identifier of the client. |
| `tenantId` | `string` | Yes | Identifier of the tenant where the client was created. |
| `clientUri` | `string` | No | URI for the homepage of the client. Metadata: format = "uri". |
| `createdAt` | `string` | Yes | Timestamp when the client was created. Metadata: format = "date-time". |
| `deletedAt` | `string` | No | Timestamp when the client was deleted. Metadata: format = "date-time". |
| `ownerType` | `string` | Yes | Type of owner that created the client. |
| `clientName` | `string` | Yes | Name of the client. |
| `disableTag` | `string` | No | Indicates whether the client is disabled. |
| `createdById` | `string` | Yes | Identifier of the resource that created the client. |
| `publishedAt` | `string` | No | Timestamp when the client was published. Metadata: format = "date-time". |
| `redirectUris` | `string[]` | No | List of allowed redirect URIs for logins with the client. |
| `allowedScopes` | `string[]` | No | List of allowed scopes for the client. |
| `createdByType` | `string` | Yes | Type of the resource that created the client. |
| `allowedOrigins` | `string[]` | No | List of allowed origins for the client. |
| `connectionPolicy` | `object[]` | No | Connection policies for the client. |

<details>
<summary>Properties of `connectionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |

</details>



### OAuthClientSecretData

OAuth client identifier and hint for the secret the event is related to.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hint` | `string` | Yes | Hint for the client secret. |
| `clientId` | `string` | Yes | Identifier of the client. |



### OAuthConnectionConfigEntry

Full client connection config resource after the event was published.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | No | Status of the connection-config for the tenant. Allowed values: approved. |
| `tenantId` | `string` | Yes | Identifier of the tenant the connection-config relates to. |
| `createdAt` | `string` | Yes | Timestamp when the connection-config was created. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the connection-config was updated. Metadata: format = "date-time". |
| `consentMethod` | `string` | Yes | Consent method for the connection-config. Allowed values: required \| trusted. |



### OAuthConnectionPolicy

Oauth-client connection policy

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | `string` | Yes | Identifier of the tenant allowed to use this OAuth client. |


