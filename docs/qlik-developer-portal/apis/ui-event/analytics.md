---
source: https://qlik.dev/apis/ui-event/analytics/
last_updated: 2026-09-11T16:13:57Z
---

# Analytics

Qlik Sense events

## Table of Contents

### ui-events

- [com.qlik.v1.analytics.analytics-app-client.deprecated-charts.opened](#comqlikv1analyticsanalytics-app-clientdeprecated-chartsopened)
- [com.qlik.v1.analytics.analytics-app-client.sheet-view.opened](#comqlikv1analyticsanalytics-app-clientsheet-viewopened)

## Events published on the `ui-events` channel

### com.qlik.v1.analytics.analytics-app-client.deprecated-charts.opened

**Title:** Deprecated charts opened in sheet

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Emitted when a client (browser) detects one or more deprecated chart types as a user opens or navigates to a sheet in the native experience or via qlik-embed with the classic/app UI. It is not emitted when switching sheet modes (for example, View to Edit) or from non-sheet UIs such as Stories or Reporting.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the event. Metadata: format = "uuid". |
| `time` | `string` | Yes | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The type of the event. |
| `source` | `string` | Yes | Metadata: default = "com.qlik/analytics". |
| `specversion` | `string` | Yes | The event is compatible with the CloudEvents specification v1.0.2. Allowed values: 1.0. |
| `data` | `object` | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Identifier of the app related to this event. Metadata: format = "uuid". |
| `charts` | `object[]` | No | List of charts |
| `ownerId` | `string` | No | ID of the user currently owning the related resource. Metadata: format = "uuid". |
| `sheetId` | `string` | No | Identifier of the sheet related to this event. Metadata: format = "uuid". |
| `sheetTitle` | `string` | No | If set, the evaluated sheet title expression, else the sheet title. |
| `sheetApproved` | `boolean` | No | Indicates whether the sheet has been approved or not. |
| `sheetPublished` | `boolean` | No | Indicates whether the sheet has been published or not. |

<details>
<summary>Properties of `charts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `chartId` | `string` | No | Identifier of the chart. Metadata: format = "uuid". |
| `chartType` | `string` | No | Type of the chart. |
| `chartTitle` | `string` | No | Title of the chart. |
| `inContainer` | `boolean` | No | Indicates whether the chart is inside a container or not. |

</details>

</details>


**Example**

```json
{
  "id": "60143626-36a8-4661-9afe-8080a01d89e7",
  "time": "2018-10-30T07:06:22Z",
  "type": "string",
  "source": "com.qlik/analytics",
  "specversion": "1.0",
  "data": {
    "appId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "charts": [
      {
        "chartId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "chartType": "bar",
        "chartTitle": "string",
        "inContainer": true
      }
    ],
    "ownerId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetTitle": "My Sheet",
    "sheetApproved": true,
    "sheetPublished": true
  }
}
```


### com.qlik.v1.analytics.analytics-app-client.sheet-view.opened

**Title:** Sense Sheet View Opened

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Triggered by a client (browser) each time a sheet change event is recorded, when in the native experience or when using qlik-embed with the `classic/app` UI. Will not be emitted when changing between sheet modes (for example, going from View to Edit), or in non-sheet UIs (such as Stories, Reporting, etc).

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the event. Metadata: format = "uuid". |
| `time` | `string` | Yes | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The type of the event. |
| `source` | `string` | Yes | Metadata: default = "com.qlik/analytics". |
| `specversion` | `string` | Yes | The event is compatible with the CloudEvents specification v1.0.2. Allowed values: 1.0. |
| `data` | `object` | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Identifier of the app related to this event. Metadata: format = "uuid". |
| `sheetId` | `string` | No | Identifier of the sheet related to this event. Metadata: format = "uuid". |
| `sheetState` | `string` | No | The mode in which the sheet was opened, either `analysis` (view mode), `edit` (advanced edit mode), or `simpleEdit` (simplified edit mode). Allowed values: analysis \| edit \| simpleEdit. |
| `sheetTitle` | `string` | No | If set, the evaluated sheet title expression, else the sheet title. |

</details>


**Example**

```json
{
  "id": "60143626-36a8-4661-9afe-8080a01d89e7",
  "time": "2018-10-30T07:06:22Z",
  "type": "string",
  "source": "com.qlik/analytics",
  "specversion": "1.0",
  "data": {
    "appId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetState": "analysis",
    "sheetTitle": "My Sheet"
  }
}
```


## Schemas

### eventBase

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the event. Metadata: format = "uuid". |
| `time` | `string` | Yes | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The type of the event. |
| `source` | `string` | Yes | The source of the event. See the `source` field on each message's payload for the value emitted for that event. |
| `specversion` | `string` | Yes | The event is compatible with the CloudEvents specification v1.0.2. Allowed values: 1.0. |


