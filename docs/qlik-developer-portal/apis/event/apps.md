---
source: https://qlik.dev/apis/event/apps/
last_updated: 2026-06-17T14:10:50+01:00
---

# Apps

Events emitted when apps are created, deleted, updated, exported, published, or reloaded in a Qlik Cloud tenant.

## Table of Contents

### system-events.app

- [com.qlik.v1.app.opened](#comqlikv1appopened)
- [com.qlik.v1.app.reload.finished](#comqlikv1appreloadfinished)

### system-events.engine.app

- [com.qlik.app.created](#comqlikappcreated)
- [com.qlik.app.data.updated](#comqlikappdataupdated)
- [com.qlik.app.deleted](#comqlikappdeleted)
- [com.qlik.app.exported](#comqlikappexported)
- [com.qlik.app.harddeleted](#comqlikappharddeleted)
- [com.qlik.app.published](#comqlikapppublished)
- [com.qlik.app.softdeleted](#comqlikappsoftdeleted)

## Events published on the `system-events.app` channel

### com.qlik.v1.app.opened

**Title:** AppOpened

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was opened.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppOpened` | No | An app was opened. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.v1.app.opened". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `workloadType` | `string` | No | Workload type. |
| `_resourcetype` | `string` | No | App resource type. |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "resourceType": "string",
    "workloadType": "string",
    "_resourcetype": "string"
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.v1.app.opened",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.v1.app.reload.finished

**Title:** AppReloadFinished

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

A reload of an app was finished v1

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppReloadFinished` | No | A reload of an app was finished v1 |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.v1.app.reload.finished". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | App name. |
| `size` | `AppDataSizeV1` | No |  |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `errors` | `undefined[]` | No | Reload errors. Max items 5. |
| `status` | `string` | No | Reload status - error or ok. |
| `endTime` | `string` | No | Time when reload ended. Metadata: format = "date-time". |
| `duration` | `integer` | No | Duration of reload (ms). Metadata: format = int64. |
| `reloadId` | `string` | No | Reload identifier. Metadata: format = "uuid". |
| `rowLimit` | `integer` | No | If greater than or equal 0, defines max number of rows loaded from a data source. Metadata: default = -1, format = int64, default = -1. |
| `warnings` | `undefined[]` | No | Reload warnings. Max items 5. |
| `statements` | `undefined[]` | No | An empty list intended to hold script statements and their metadata. Use the Apps API to fetch reload metadata. |
| `isSkipStore` | `boolean` | No | True if store statements are blocked from executing. |
| `isSessionApp` | `boolean` | No | App is a Session app. |
| `isPartialReload` | `boolean` | No | True if the reload is a partial reload. |
| `peakMemoryBytes` | `integer` | No | Maximum number of bytes used during reload of the app. Metadata: format = int64. |
| `isDirectQueryMode` | `boolean` | No | App is a Direct Query app |
| `endedWithMemoryConstraint` | `boolean` | No | true if memory limits were exhausted during reload. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "name": "string",
    "size": {
      "memory": 42
    },
    "errors": [],
    "status": "string",
    "endTime": "2018-10-30T07:06:22Z",
    "duration": 42,
    "reloadId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "rowLimit": -1,
    "warnings": [],
    "statements": [],
    "isSkipStore": true,
    "isSessionApp": true,
    "isPartialReload": true,
    "peakMemoryBytes": 42,
    "isDirectQueryMode": true,
    "endedWithMemoryConstraint": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.v1.app.reload.finished",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


## Events published on the `system-events.engine.app` channel

### com.qlik.app.created

**Title:** AppCreated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppCreated` | No | An app was created. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.created". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `size` | `AppDataSize` | No |  |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | `string` | No | App owner identifier. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `published` | `boolean` | No | When true, the app was distributed. |
| `thumbnail` | `string` | No | App thumbnail. |
| `createdDate` | `string` | No | Time when app was created. Metadata: format = "date-time". |
| `description` | `string` | No | App description. |
| `originAppId` | `string` | No | Origin app identifier. Metadata: format = "uuid". |
| `publishTime` | `string` | No | Time when app was published. Metadata: format = "date-time". |
| `dynamicColor` | `string` | No | App dynamic color. |
| `modifiedDate` | `string` | No | Time when app was last modified. Metadata: format = "date-time". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `lastReloadTime` | `string` | No | Time of last successful reload. Metadata: format = "date-time". |
| `createdByAction` | `string` | No | Allowed values: create \| copy \| publish \| import \| restore. |
| `hasSectionAccess` | `boolean` | No | When true, the app has section access. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `integer` | No | Data model size on file (bytes). Metadata: format = int64. |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "size": {
      "file": 42,
      "memory": 42
    },
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "published": true,
    "thumbnail": "string",
    "createdDate": "2018-10-30T07:06:22Z",
    "description": "string",
    "originAppId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "publishTime": "2018-10-30T07:06:22Z",
    "dynamicColor": "string",
    "modifiedDate": "2018-10-30T07:06:22Z",
    "resourceType": "string",
    "_resourcetype": "string",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "hasSectionAccess": true,
    "isDirectQueryMode": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.created",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.data.updated

**Title:** AppDataUpdated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

The data of an app was updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppDataUpdated` | No | The data of an app was updated. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.data.updated". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `size` | `AppDataSize` | No |  |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `_updates` | `object[]` | No |  |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `lastReloadTime` | `string` | No | Time of last successful reload. Metadata: format = "date-time". |
| `lineageChanged` | `boolean` | No | When true, there is new lineage information saved. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `integer` | No | Data model size on file (bytes). Metadata: format = int64. |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to the updated value. |
| `newValue` | `string` | No | Value after update. |
| `oldValue` | `string` | No | Value before update. |

</details>

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "size": {
      "file": 42,
      "memory": 42
    },
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "_updates": [
      {
        "path": "string",
        "newValue": "string",
        "oldValue": "string"
      }
    ],
    "resourceType": "string",
    "_resourcetype": "string",
    "lastReloadTime": "2018-10-30T07:06:22Z",
    "lineageChanged": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.data.updated",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.deleted

**Title:** AppDeleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppDeleted` | No | An app was deleted. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.deleted". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `deleteType` | `string` | No | Allowed values: SOFT \| HARD. |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "resourceType": "string",
    "_resourcetype": "string",
    "isDirectQueryMode": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.deleted",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.exported

**Title:** AppExported

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was exported.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppExported` | No | An app was exported. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.exported". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | `string` | No | App owner. |
| `spaceId` | `string` | No | Space identifier. Metadata: format = "uuid". |
| `dataReduced` | `boolean` | No | When true, data was reduced for smaller file size. |
| `dataExported` | `boolean` | No | When true, data was exported. |
| `exportedDate` | `string` | No | Time when app was exported. Metadata: format = "date-time". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "owner": "string",
    "custom": {},
    "ownerId": "string",
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "dataReduced": true,
    "dataExported": true,
    "exportedDate": "2018-10-30T07:06:22Z",
    "resourceType": "string",
    "_resourcetype": "string"
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.exported",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.harddeleted

**Title:** AppHardDeleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was hard deleted and can no longer be restored.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppHardDeleted` | No | An app was hard deleted and can no longer be restored. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.harddeleted". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "resourceType": "string",
    "isDirectQueryMode": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.harddeleted",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.published

**Title:** AppPublished

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was published.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppPublished` | No | An app was published. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.published". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `spaceId` | `string` | No | Space identifier. Metadata: format = "uuid". |
| `originAppId` | `string` | No | Origin app identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `dataPublished` | `boolean` | No | When true, data was published. |
| `originSpaceId` | `string` | No | Origin space identifier. Metadata: format = "uuid". |
| `publishedDate` | `string` | No | Time when app was published. Metadata: format = "date-time". |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "owner": "string",
    "custom": {},
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "originAppId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "resourceType": "string",
    "_resourcetype": "string",
    "dataPublished": true,
    "originSpaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "publishedDate": "2018-10-30T07:06:22Z"
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.published",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


### com.qlik.app.softdeleted

**Title:** AppSoftDeleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

An app was soft deleted and can still be restored.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | CloudEvent Identifier. Metadata: format = "uuid". |
| `data` | `AppSoftDeleted` | No | An app was soft deleted and can still be restored. |
| `host` | `string` | No | Unique identifier for event producer. |
| `time` | `string` | No | Time when event was sent. Metadata: format = "date". |
| `type` | `string` | No | Event message name. Metadata: default = "com.qlik.app.softdeleted". |
| `reason` | `string` | No | Reason for event. |
| `source` | `string` | No | CloudEvent source Identifier. Metadata: default = "com.qlik/engine". |
| `userid` | `string` | No | User Identifier. |
| `ownerid` | `string` | No | Owner Identifier. |
| `spaceid` | `string` | No | Space Identifier if resource is in a space. |
| `authtype` | `string` | No | A string representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | OAuth-Client Identifier of the Event for OAuth token requests. |
| `tenantid` | `string` | No | Tenant Identifier. |
| `sessionid` | `string` | No | Session Identifier. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `specversion` | `string` | No | CloudEvents version. Metadata: default = "1.0". |
| `datacontenttype` | `string` | No | CloudEvent content type. Metadata: default = "application/json". |
| `toplevelresourceid` | `string` | No | Identifier of the top level resource |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `purgeAt` | `string` | No | Earliest date the soft deleted app may be hard deleted (permanently purged). Once this date is reached, purge can happen at any time and is not under user control. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |

</details>


**Example**

```json
{
  "id": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "data": {
    "id": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "name": "string",
    "purgeAt": "string",
    "spaceId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "resourceType": "string",
    "isDirectQueryMode": true
  },
  "host": "id",
  "time": "2022-10-30T07:06:22Z",
  "type": "com.qlik.app.softdeleted",
  "reason": "publishreplace",
  "source": "com.qlik/engine",
  "userid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "ownerid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "spaceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authtype": "service_account",
  "clientid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "tenantid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "sessionid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76",
  "authclaims": "{\"iss\":\"02_Open_App_V1\", \"sub\":\"7eddf8df-ce4f-4b94-9388-8d9e21b9ed75\", \"subType\":\"api-key\"}",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "toplevelresourceid": "ccb149fb-e2dd-420b-8d9f-e6aacb95eb76"
}
```


## Schemas

### AppCreated

An app was created.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `size` | `AppDataSize` | No |  |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | `string` | No | App owner identifier. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `published` | `boolean` | No | When true, the app was distributed. |
| `thumbnail` | `string` | No | App thumbnail. |
| `createdDate` | `string` | No | Time when app was created. Metadata: format = "date-time". |
| `description` | `string` | No | App description. |
| `originAppId` | `string` | No | Origin app identifier. Metadata: format = "uuid". |
| `publishTime` | `string` | No | Time when app was published. Metadata: format = "date-time". |
| `dynamicColor` | `string` | No | App dynamic color. |
| `modifiedDate` | `string` | No | Time when app was last modified. Metadata: format = "date-time". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `lastReloadTime` | `string` | No | Time of last successful reload. Metadata: format = "date-time". |
| `createdByAction` | `string` | No | Allowed values: create \| copy \| publish \| import \| restore. |
| `hasSectionAccess` | `boolean` | No | When true, the app has section access. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `integer` | No | Data model size on file (bytes). Metadata: format = int64. |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>



### AppCreatedByAction

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `AppCreatedByAction` | `string` | No | Allowed values: create \| copy \| publish \| import \| restore. |



### AppDataSize

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `integer` | No | Data model size on file (bytes). Metadata: format = int64. |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |



### AppDataSizeV1

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |



### AppDataUpdated

The data of an app was updated.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `size` | `AppDataSize` | No |  |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `_updates` | `object[]` | No |  |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `lastReloadTime` | `string` | No | Time of last successful reload. Metadata: format = "date-time". |
| `lineageChanged` | `boolean` | No | When true, there is new lineage information saved. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `integer` | No | Data model size on file (bytes). Metadata: format = int64. |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to the updated value. |
| `newValue` | `string` | No | Value after update. |
| `oldValue` | `string` | No | Value before update. |

</details>



### AppDeleted

An app was deleted.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `deleteType` | `string` | No | Allowed values: SOFT \| HARD. |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |



### AppExported

An app was exported.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `ownerId` | `string` | No | App owner. |
| `spaceId` | `string` | No | Space identifier. Metadata: format = "uuid". |
| `dataReduced` | `boolean` | No | When true, data was reduced for smaller file size. |
| `dataExported` | `boolean` | No | When true, data was exported. |
| `exportedDate` | `string` | No | Time when app was exported. Metadata: format = "date-time". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |



### AppHardDeleted

An app was hard deleted and can no longer be restored.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |



### AppOpened

An app was opened.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `workloadType` | `string` | No | Workload type. |
| `_resourcetype` | `string` | No | App resource type. |



### AppPublished

An app was published.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `owner` | `string` | No | App owner. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `custom` | `JsonObject` | No | Contains dynamic JSON data specified by the client. |
| `spaceId` | `string` | No | Space identifier. Metadata: format = "uuid". |
| `originAppId` | `string` | No | Origin app identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `_resourcetype` | `string` | No | App resource type. |
| `dataPublished` | `boolean` | No | When true, data was published. |
| `originSpaceId` | `string` | No | Origin space identifier. Metadata: format = "uuid". |
| `publishedDate` | `string` | No | Time when app was published. Metadata: format = "date-time". |



### AppReloadFinished

A reload of an app was finished v1

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | App name. |
| `size` | `AppDataSizeV1` | No |  |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `errors` | `undefined[]` | No | Reload errors. Max items 5. |
| `status` | `string` | No | Reload status - error or ok. |
| `endTime` | `string` | No | Time when reload ended. Metadata: format = "date-time". |
| `duration` | `integer` | No | Duration of reload (ms). Metadata: format = int64. |
| `reloadId` | `string` | No | Reload identifier. Metadata: format = "uuid". |
| `rowLimit` | `integer` | No | If greater than or equal 0, defines max number of rows loaded from a data source. Metadata: default = -1, format = int64, default = -1. |
| `warnings` | `undefined[]` | No | Reload warnings. Max items 5. |
| `statements` | `undefined[]` | No | An empty list intended to hold script statements and their metadata. Use the Apps API to fetch reload metadata. |
| `isSkipStore` | `boolean` | No | True if store statements are blocked from executing. |
| `isSessionApp` | `boolean` | No | App is a Session app. |
| `isPartialReload` | `boolean` | No | True if the reload is a partial reload. |
| `peakMemoryBytes` | `integer` | No | Maximum number of bytes used during reload of the app. Metadata: format = int64. |
| `isDirectQueryMode` | `boolean` | No | App is a Direct Query app |
| `endedWithMemoryConstraint` | `boolean` | No | true if memory limits were exhausted during reload. |

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `memory` | `integer` | No | Data model size in memory (bytes). Metadata: format = int64. |

</details>



### AppSoftDeleted

An app was soft deleted and can still be restored.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | App identifier. Metadata: format = "uuid". |
| `name` | `string` | No | App name. |
| `usage` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |
| `purgeAt` | `string` | No | Earliest date the soft deleted app may be hard deleted (permanently purged). Once this date is reached, purge can happen at any time and is not under user control. |
| `spaceId` | `string` | No | App space identifier. Metadata: format = "uuid". |
| `resourceType` | `string` | No | App resource type. |
| `isDirectQueryMode` | `boolean` | No | When true, the app is a Direct Query app. |



### CloudEventsObjectUpdate

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | Path to the updated value. |
| `newValue` | `string` | No | Value after update. |
| `oldValue` | `string` | No | Value before update. |



### DeleteTypeEnum

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DeleteTypeEnum` | `string` | No | Allowed values: SOFT \| HARD. |



### JsonObject

Contains dynamic JSON data specified by the client.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `JsonObject` | `object` | No | Contains dynamic JSON data specified by the client. |



### NxLocalizedErrorCode

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `NxLocalizedErrorCode` | `string` | No | Allowed values: LOCERR_INTERNAL_ERROR \| LOCERR_GENERIC_UNKNOWN \| LOCERR_GENERIC_OK \| LOCERR_GENERIC_NOT_SET \| LOCERR_GENERIC_NOT_FOUND \| LOCERR_GENERIC_ALREADY_EXISTS \| LOCERR_GENERIC_INVALID_PATH \| LOCERR_GENERIC_ACCESS_DENIED \| LOCERR_GENERIC_OUT_OF_MEMORY \| LOCERR_GENERIC_NOT_INITIALIZED \| LOCERR_GENERIC_INVALID_PARAMETERS \| LOCERR_GENERIC_EMPTY_PARAMETERS \| LOCERR_GENERIC_INTERNAL_ERROR \| LOCERR_GENERIC_CORRUPT_DATA \| LOCERR_GENERIC_MEMORY_INCONSISTENCY \| LOCERR_GENERIC_INVISIBLE_OWNER_ABORT \| LOCERR_GENERIC_PROHIBIT_VALIDATE \| LOCERR_GENERIC_ABORTED \| LOCERR_GENERIC_CONNECTION_LOST \| LOCERR_GENERIC_UNSUPPORTED_IN_PRODUCT_VERSION \| LOCERR_GENERIC_REST_CONNECTION_FAILURE \| LOCERR_GENERIC_MEMORY_LIMIT_REACHED \| LOCERR_GENERIC_NOT_IMPLEMENTED \| LOCERR_GENERIC_ENGINE_TERMINATED \| LOCERR_GENERIC_WRITE_OPERATIONS_LIMIT_REACHED \| LOCERR_HTTP_400 \| LOCERR_HTTP_401 \| LOCERR_HTTP_402 \| LOCERR_HTTP_403 \| LOCERR_HTTP_404 \| LOCERR_HTTP_405 \| LOCERR_HTTP_406 \| LOCERR_HTTP_407 \| LOCERR_HTTP_408 \| LOCERR_HTTP_409 \| LOCERR_HTTP_410 \| LOCERR_HTTP_411 \| LOCERR_HTTP_412 \| LOCERR_HTTP_413 \| LOCERR_HTTP_414 \| LOCERR_HTTP_415 \| LOCERR_HTTP_416 \| LOCERR_HTTP_417 \| LOCERR_HTTP_422 \| LOCERR_HTTP_423 \| LOCERR_HTTP_429 \| LOCERR_HTTP_500 \| LOCERR_HTTP_501 \| LOCERR_HTTP_502 \| LOCERR_HTTP_503 \| LOCERR_HTTP_504 \| LOCERR_HTTP_505 \| LOCERR_HTTP_509 \| LOCERR_HTTP_COULD_NOT_RESOLVE_HOST \| LOCERR_APP_ALREADY_EXISTS \| LOCERR_APP_INVALID_NAME \| LOCERR_APP_ALREADY_OPEN \| LOCERR_APP_NOT_FOUND \| LOCERR_APP_IMPORT_FAILED \| LOCERR_APP_SAVE_FAILED \| LOCERR_APP_CREATE_FAILED \| LOCERR_APP_INVALID \| LOCERR_APP_CONNECT_FAILED \| LOCERR_APP_ALREADY_OPEN_IN_DIFFERENT_MODE \| LOCERR_APP_MIGRATION_COULD_NOT_CONTACT_MIGRATION_SERVICE \| LOCERR_APP_MIGRATION_COULD_NOT_START_MIGRATION \| LOCERR_APP_MIGRATION_FAILURE \| LOCERR_APP_SCRIPT_MISSING \| LOCERR_APP_EXPORT_FAILED \| LOCERR_APP_SIZE_EXCEEDED \| LOCERR_APP_DIRECT_QUERY_WORKLOAD_NOT_SUPPORTED \| LOCERR_APP_NOT_OPEN \| LOCERR_APP_EVENT_SOURCE_TIMEOUT \| LOCERR_APP_SOFT_DELETED \| LOCERR_CONNECTION_ALREADY_EXISTS \| LOCERR_CONNECTION_NOT_FOUND \| LOCERR_CONNECTION_FAILED_TO_LOAD \| LOCERR_CONNECTION_FAILED_TO_IMPORT \| LOCERR_CONNECTION_NAME_IS_INVALID \| LOCERR_CONNECTION_MISSING_CREDENTIALS \| LOCERR_CONNECTOR_NO_FILE_STREAMING_SUPPORT \| LOCERR_CONNECTOR_FILESIZE_EXCEEDED_BUFFER_SIZE \| LOCERR_FILE_ACCESS_DENIED \| LOCERR_FILE_NAME_INVALID \| LOCERR_FILE_CORRUPT \| LOCERR_FILE_NOT_FOUND \| LOCERR_FILE_FORMAT_UNSUPPORTED \| LOCERR_FILE_OPENED_IN_UNSUPPORTED_MODE \| LOCERR_FILE_TABLE_NOT_FOUND \| LOCERR_USER_ACCESS_DENIED \| LOCERR_USER_IMPERSONATION_FAILED \| LOCERR_SERVER_OUT_OF_SESSION_AND_USER_CALS \| LOCERR_SERVER_OUT_OF_SESSION_CALS \| LOCERR_SERVER_OUT_OF_USAGE_CALS \| LOCERR_SERVER_OUT_OF_CALS \| LOCERR_SERVER_OUT_OF_NAMED_CALS \| LOCERR_SERVER_OFF_DUTY \| LOCERR_SERVER_BUSY \| LOCERR_SERVER_LICENSE_EXPIRED \| LOCERR_SERVER_AJAX_DISABLED \| LOCERR_SERVER_NO_TOKEN \| LOCERR_HC_INVALID_OBJECT \| LOCERR_HC_RESULT_TOO_LARGE \| LOCERR_HC_INVALID_OBJECT_STATE \| LOCERR_HC_MODAL_OBJECT_ERROR \| LOCERR_CALC_INVALID_DEF \| LOCERR_CALC_NOT_IN_LIB \| LOCERR_CALC_HEAP_ERROR \| LOCERR_CALC_TOO_LARGE \| LOCERR_CALC_TIMEOUT \| LOCERR_CALC_EVAL_CONDITION_FAILED \| LOCERR_CALC_MIXED_LINKED_AGGREGATION \| LOCERR_CALC_MISSING_LINKED \| LOCERR_CALC_INVALID_COL_SORT \| LOCERR_CALC_PAGES_TOO_LARGE \| LOCERR_CALC_SEMANTIC_FIELD_NOT_ALLOWED \| LOCERR_CALC_VALIDATION_STATE_INVALID \| LOCERR_CALC_PIVOT_DIMENSIONS_ALREADY_EXISTS \| LOCERR_CALC_MISSING_LINKED_FIELD \| LOCERR_CALC_NOT_CALCULATED \| LOCERR_LAYOUT_EXTENDS_INVALID_ID \| LOCERR_LAYOUT_LINKED_OBJECT_NOT_FOUND \| LOCERR_LAYOUT_LINKED_OBJECT_INVALID \| LOCERR_PERSISTENCE_WRITE_FAILED \| LOCERR_PERSISTENCE_READ_FAILED \| LOCERR_PERSISTENCE_DELETE_FAILED \| LOCERR_PERSISTENCE_NOT_FOUND \| LOCERR_PERSISTENCE_UNSUPPORTED_VERSION \| LOCERR_PERSISTENCE_MIGRATION_FAILED_READ_ONLY \| LOCERR_PERSISTENCE_MIGRATION_CANCELLED \| LOCERR_PERSISTENCE_MIGRATION_BACKUP_FAILED \| LOCERR_PERSISTENCE_DISK_FULL \| LOCERR_PERSISTENCE_NOT_SUPPORTED_FOR_SESSION_APP \| LOCERR_PERSISTENCE_MOVE_FAILED \| LOCERR_PERSISTENCE_OBJECT_LOCKED \| LOCERR_PERSISTENCE_ENCRYPTION_KEY_MIGRATION_ONGOING \| LOCERR_PERSISTENCE_SYNC_SET_CHUNK_INVALID_PARAMETERS \| LOCERR_PERSISTENCE_SYNC_GET_CHUNK_INVALID_PARAMETERS \| LOCERR_SCRIPT_DATASOURCE_ACCESS_DENIED \| LOCERR_RELOAD_IN_PROGRESS \| LOCERR_RELOAD_TABLE_X_NOT_FOUND \| LOCERR_RELOAD_UNKNOWN_STATEMENT \| LOCERR_RELOAD_EXPECTED_SOMETHING_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_NOTHING_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_1_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_2_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_3_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_4_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_5_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_6_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_7_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_EXPECTED_ONE_OF_8_OR_MORE_TOKENS_FOUND_UNKNOWN \| LOCERR_RELOAD_FIELD_X_NOT_FOUND \| LOCERR_RELOAD_MAPPING_TABLE_X_NOT_FOUND \| LOCERR_RELOAD_LIB_CONNECTION_X_NOT_FOUND \| LOCERR_RELOAD_NAME_ALREADY_TAKEN \| LOCERR_RELOAD_WRONG_FILE_FORMAT_DIF \| LOCERR_RELOAD_WRONG_FILE_FORMAT_BIFF \| LOCERR_RELOAD_WRONG_FILE_FORMAT_ENCRYPTED \| LOCERR_RELOAD_OPEN_FILE_ERROR \| LOCERR_RELOAD_AUTO_GENERATE_COUNT \| LOCERR_RELOAD_PE_ILLEGAL_PREFIX_COMB \| LOCERR_RELOAD_MATCHING_CONTROL_STATEMENT_ERROR \| LOCERR_RELOAD_MATCHING_LIBPATH_X_NOT_FOUND \| LOCERR_RELOAD_MATCHING_LIBPATH_X_INVALID \| LOCERR_RELOAD_MATCHING_LIBPATH_X_OUTSIDE \| LOCERR_RELOAD_NO_QUALIFIED_PATH_FOR_FILE \| LOCERR_RELOAD_MODE_STATEMENT_ONLY_FOR_LIB_PATHS \| LOCERR_RELOAD_INCONSISTENT_USE_OF_SEMANTIC_FIELDS \| LOCERR_RELOAD_NO_OPEN_DATABASE \| LOCERR_RELOAD_AGGREGATION_REQUIRED_BY_GROUP_BY \| LOCERR_RELOAD_CONNECT_MUST_USE_LIB_PREFIX_IN_THIS_MODE \| LOCERR_RELOAD_ODBC_CONNECT_FAILED \| LOCERR_RELOAD_OLEDB_CONNECT_FAILED \| LOCERR_RELOAD_CUSTOM_CONNECT_FAILED \| LOCERR_RELOAD_ODBC_READ_FAILED \| LOCERR_RELOAD_OLEDB_READ_FAILED \| LOCERR_RELOAD_CUSTOM_READ_FAILED \| LOCERR_RELOAD_BINARY_LOAD_PROHIBITED \| LOCERR_RELOAD_CONNECTOR_START_FAILED \| LOCERR_RELOAD_CONNECTOR_NOT_RESPONDING \| LOCERR_RELOAD_CONNECTOR_REPLY_ERROR \| LOCERR_RELOAD_CONNECTOR_CONNECT_ERROR \| LOCERR_RELOAD_CONNECTOR_NOT_FOUND_ERROR \| LOCERR_RELOAD_INPUT_FIELD_WITH_DUPLICATE_KEYS \| LOCERR_RELOAD_CONCATENATE_LOAD_NO_PREVIOUS_TABLE \| LOCERR_RELOAD_WRONG_FILE_FORMAT_QVD \| LOCERR_RELOAD_ACTION_BLOCKED_ENTITLEMENT \| LOCERR_RELOAD_EXIT_ERROR \| LOCERR_PERSONAL_NEW_VERSION_AVAILABLE \| LOCERR_PERSONAL_VERSION_EXPIRED \| LOCERR_PERSONAL_SECTION_ACCESS_DETECTED \| LOCERR_PERSONAL_APP_DELETION_FAILED \| LOCERR_USER_AUTHENTICATION_FAILURE \| LOCERR_EXPORT_OUT_OF_MEMORY \| LOCERR_EXPORT_NO_DATA \| LOCERR_SYNC_INVALID_OFFSET \| LOCERR_SEARCH_TIMEOUT \| LOCERR_DIRECT_DISCOVERY_LINKED_EXPRESSION_FAIL \| LOCERR_DIRECT_DISCOVERY_ROWCOUNT_OVERFLOW \| LOCERR_DIRECT_DISCOVERY_EMPTY_RESULT \| LOCERR_DIRECT_DISCOVERY_DB_CONNECTION_FAILED \| LOCERR_DIRECT_DISCOVERY_MEASURE_NOT_ALLOWED \| LOCERR_DIRECT_DISCOVERY_DETAIL_NOT_ALLOWED \| LOCERR_DIRECT_DISCOVERY_NOT_SYNTH_CIRCULAR_ALLOWED \| LOCERR_DIRECT_DISCOVERY_ONLY_ONE_DD_TABLE_ALLOWED \| LOCERR_DIRECT_DISCOVERY_DB_AUTHORIZATION_FAILED \| LOCERR_SMART_LOAD_TABLE_NOT_FOUND \| LOCERR_SMART_LOAD_TABLE_DUPLICATED \| LOCERR_VARIABLE_NO_NAME \| LOCERR_VARIABLE_DUPLICATE_NAME \| LOCERR_VARIABLE_INCONSISTENCY \| LOCERR_VARIABLE_CONSTRAINT_INCONSISTENCY \| LOCERR_VARIABLE_CONSTRAINT_FAILED \| LOCERR_MEDIA_LIBRARY_LIST_FAILED \| LOCERR_MEDIA_LIBRARY_CONTENT_FAILED \| LOCERR_MEDIA_BUNDLING_FAILED \| LOCERR_MEDIA_UNBUNDLING_FAILED \| LOCERR_MEDIA_LIBRARY_NOT_FOUND \| LOCERR_FEATURE_DISABLED \| LOCERR_LOAD_TOO_MANY_FIELDS \| LOCERR_LOAD_TOO_MANY_TABLES \| LOCERR_JSON_RPC_INVALID_REQUEST \| LOCERR_JSON_RPC_METHOD_NOT_FOUND \| LOCERR_JSON_RPC_INVALID_PARAMETERS \| LOCERR_JSON_RPC_INTERNAL_ERROR \| LOCERR_JSON_RPC_RESPONSE_TOO_LARGE \| LOCERR_JSON_RPC_PARSE_ERROR \| LOCERR_MQ_SOCKET_CONNECT_FAILURE \| LOCERR_MQ_SOCKET_OPEN_FAILURE \| LOCERR_MQ_PROTOCOL_NO_RESPONE \| LOCERR_MQ_PROTOCOL_LIBRARY_EXCEPTION \| LOCERR_MQ_PROTOCOL_CONNECTION_CLOSED \| LOCERR_MQ_PROTOCOL_CHANNEL_CLOSED \| LOCERR_MQ_PROTOCOL_UNKNOWN_ERROR \| LOCERR_MQ_PROTOCOL_INVALID_STATUS \| LOCERR_EXTENGINE_GRPC_STATUS_OK \| LOCERR_EXTENGINE_GRPC_STATUS_CANCELLED \| LOCERR_EXTENGINE_GRPC_STATUS_UNKNOWN \| LOCERR_EXTENGINE_GRPC_STATUS_INVALID_ARGUMENT \| LOCERR_EXTENGINE_GRPC_STATUS_DEADLINE_EXCEEDED \| LOCERR_EXTENGINE_GRPC_STATUS_NOT_FOUND \| LOCERR_EXTENGINE_GRPC_STATUS_ALREADY_EXISTS \| LOCERR_EXTENGINE_GRPC_STATUS_PERMISSION_DENIED \| LOCERR_EXTENGINE_GRPC_STATUS_RESOURCE_EXHAUSTED \| LOCERR_EXTENGINE_GRPC_STATUS_FAILED_PRECONDITION \| LOCERR_EXTENGINE_GRPC_STATUS_ABORTED \| LOCERR_EXTENGINE_GRPC_STATUS_OUT_OF_RANGE \| LOCERR_EXTENGINE_GRPC_STATUS_UNIMPLEMENTED \| LOCERR_EXTENGINE_GRPC_STATUS_INTERNAL \| LOCERR_EXTENGINE_GRPC_STATUS_UNAVAILABLE \| LOCERR_EXTENGINE_GRPC_STATUS_DATA_LOSS \| LOCERR_EXTENGINE_GRPC_STATUS_UNAUTHENTICATED \| LOCERR_LXW_INVALID_OBJ \| LOCERR_LXW_INVALID_FILE \| LOCERR_LXW_INVALID_SHEET \| LOCERR_LXW_INVALID_EXPORT_RANGE \| LOCERR_LXW_ERROR \| LOCERR_LXW_ERROR_MEMORY_MALLOC_FAILED \| LOCERR_LXW_ERROR_CREATING_XLSX_FILE \| LOCERR_LXW_ERROR_CREATING_TMPFILE \| LOCERR_LXW_ERROR_ZIP_FILE_OPERATION \| LOCERR_LXW_ERROR_ZIP_FILE_ADD \| LOCERR_LXW_ERROR_ZIP_CLOSE \| LOCERR_LXW_ERROR_NULL_PARAMETER_IGNORED \| LOCERR_LXW_ERROR_MAX_STRING_LENGTH_EXCEEDED \| LOCERR_LXW_ERROR_255_STRING_LENGTH_EXCEEDED \| LOCERR_LXW_ERROR_SHARED_STRING_INDEX_NOT_FOUND \| LOCERR_LXW_ERROR_WORKSHEET_INDEX_OUT_OF_RANGE \| LOCERR_LXW_ERROR_WORKSHEET_MAX_NUMBER_URLS_EXCEEDED \| LOCERR_BDI_STATUS_OK \| LOCERR_BDI_GENERIC_ERROR_NOT_TRANSLATED \| LOCERR_TRENDLINE_INVALID_DEF \| LOCERR_TRENDLINE_INVALID_MATH_ERROR \| LOCERR_CURL_UNSUPPORTED_PROTOCOL \| LOCERR_CURL_COULDNT_RESOLVE_PROXY \| LOCERR_CURL_COULDNT_CONNECT \| LOCERR_CURL_REMOTE_ACCESS_DENIED \| LOCERR_CURL_FTP_ACCEPT_FAILED \| LOCERR_CURL_FTP_ACCEPT_TIMEOUT \| LOCERR_CURL_FTP_CANT_GET_HOST \| LOCERR_CURL_PARTIAL_FILE \| LOCERR_CURL_QUOTE_ERROR \| LOCERR_CURL_WRITE_ERROR \| LOCERR_CURL_UPLOAD_FAILED \| LOCERR_CURL_OUT_OF_MEMORY \| LOCERR_CURL_OPERATION_TIMEDOUT \| LOCERR_CURL_FTP_COULDNT_USE_REST \| LOCERR_CURL_HTTP_POST_ERROR \| LOCERR_CURL_SSL_CONNECT_ERROR \| LOCERR_CURL_FILE_COULDNT_READ_FILE \| LOCERR_CURL_LDAP_CANNOT_BIND \| LOCERR_CURL_LDAP_SEARCH_FAILED \| LOCERR_CURL_TOO_MANY_REDIRECTS \| LOCERR_CURL_PEER_FAILED_VERIFICATION \| LOCERR_CURL_GOT_NOTHING \| LOCERR_CURL_SSL_ENGINE_NOTFOUND \| LOCERR_CURL_SSL_ENGINE_SETFAILED \| LOCERR_CURL_SSL_CERTPROBLEM \| LOCERR_CURL_SSL_CIPHER \| LOCERR_CURL_SSL_CACERT \| LOCERR_CURL_BAD_CONTENT_ENCODING \| LOCERR_CURL_LDAP_INVALID_URL \| LOCERR_CURL_USE_SSL_FAILED \| LOCERR_CURL_SSL_ENGINE_INITFAILED \| LOCERR_CURL_LOGIN_DENIED \| LOCERR_CURL_TFTP_NOTFOUND \| LOCERR_CURL_TFTP_ILLEGAL \| LOCERR_CURL_SSH \| LOCERR_SETEXPRESSION_TOO_LARGE \| LOCERR_RELOAD_MERGE_LOAD_ERROR \| LOCERR_WIN_FTP_DROPPED \| LOCERR_WIN_FTP_NO_PASSIVE_MODE \| LOCERR_WIN_HTTP_DOWNLEVEL_SERVER \| LOCERR_WIN_HTTP_INVALID_SERVER_RESPONSE \| LOCERR_WIN_HTTP_REDIRECT_NEEDS_CONFIRMATION \| LOCERR_WIN_INTERNET_FORCE_RETRY \| LOCERR_WIN_INTERNET_CANNOT_CONNECT \| LOCERR_WIN_INTERNET_CONNECTION_ABORTED \| LOCERR_WIN_INTERNET_CONNECTION_RESET \| LOCERR_WIN_INTERNET_DISCONNECTED \| LOCERR_WIN_INTERNET_INCORRECT_FORMAT \| LOCERR_WIN_INTERNET_INVALID_CA \| LOCERR_WIN_INTERNET_INVALID_OPERATION \| LOCERR_WIN_INTERNET_INVALID_URL \| LOCERR_WIN_INTERNET_ITEM_NOT_FOUND \| LOCERR_WIN_INTERNET_LOGIN_FAILURE \| LOCERR_WIN_INTERNET_NAME_NOT_RESOLVED \| LOCERR_WIN_INTERNET_NEED_UI \| LOCERR_WIN_INTERNET_SEC_CERT_CN_INVALID \| LOCERR_WIN_INTERNET_SEC_CERT_DATE_INVALID \| LOCERR_WIN_INTERNET_SEC_CERT_ERRORS \| LOCERR_WIN_INTERNET_SEC_INVALID_CERT \| LOCERR_WIN_INTERNET_SERVER_UNREACHABLE \| LOCERR_BM_RESULT_TOO_LARGE. |



### UsageEnum

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `UsageEnum` | `string` | No | Allowed values: ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP \| DIRECT_QUERY_MODE. |


