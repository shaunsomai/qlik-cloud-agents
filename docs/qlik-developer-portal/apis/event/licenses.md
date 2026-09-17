---
source: https://qlik.dev/apis/event/licenses/
last_updated: 2026-08-25T10:14:37+01:00
---

# Licenses

Track license usage and entitlement events for your Qlik Cloud tenant.

## Table of Contents

### system-events.licenses

- [com.qlik.license.assignment.deleted](#comqliklicenseassignmentdeleted)
- [com.qlik.license.assignment.rejected](#comqliklicenseassignmentrejected)
- [com.qlik.license.assignment.updated](#comqliklicenseassignmentupdated)
- [com.qlik.license.data.volume.consumption.aggregated](#comqliklicensedatavolumeconsumptionaggregated)
- [com.qlik.license.definition.updated](#comqliklicensedefinitionupdated)
- [com.qlik.v1.license.lease.created](#comqlikv1licenseleasecreated)
- [com.qlik.v1.license.lease.deleted](#comqlikv1licenseleasedeleted)
- [com.qlik.v1.license.lease.updated](#comqlikv1licenseleaseupdated)
- [com.qlik.v1.license.tenant.associated](#comqlikv1licensetenantassociated)

## Events published on the `system-events.licenses` channel

### com.qlik.license.assignment.deleted

**Title:** Assignment deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a license assignment is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.license.assignment.deleted". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type. May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.license.assignment.deleted",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "type": "professional",
    "origin": "internal",
    "license": "1234123412341234",
    "subject": "qtsel\\lhr"
  },
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.license.assignment.rejected

**Title:** Assignment rejected

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a license assignment is rejected.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.license.assignment.rejected". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type. May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `message` | `string` | No | Message about why the assignment was rejected. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.license.assignment.rejected",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "type": "professional",
    "origin": "internal",
    "license": "1234123412341234",
    "message": "string",
    "subject": "qtsel\\lhr"
  },
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.license.assignment.updated

**Title:** Assignment updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a license assignment is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.license.assignment.updated". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type (e.g. 'analyzer_time', 'professional', etc.). May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.license.assignment.updated",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "type": "professional",
    "origin": "internal",
    "license": "1234123412341234",
    "subject": "qtsel\\lhr"
  },
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.license.data.volume.consumption.aggregated  _(deprecated)_

**Title:** Data volume consumption aggregated

**Action:** `send`

**Deprecated:** `true`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when data volume consumption is reported.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.license.data.volume.consumption.aggregated". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer` | No | Total data volume consumption across all consumption types. Metadata: format = int64. |
| `dataVolume` | `dataVolume` | Yes |  |
| `globalConsumption` | `integer` | No | Total data volume consumed globally by the tenant. Metadata: format = int64. |
| `globalConsumptionUnit` | `string` | No | Unit the global consumption value is expressed in. |
| `totalLocalConsumption` | `integer` | Yes | Total data volume consumed locally by the tenant. Metadata: format = int64. |
| `licenseHighWatermarkWithinMonth` | `integer` | No | Highest recorded data volume consumption for the tenant within the current month. Metadata: format = int64. |
| `licenseHighWatermarkWithinMonthUnit` | `string` | No | Unit the monthly high-watermark value is expressed in. |

<details>
<summary>Properties of `dataVolume`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | Unit the reported volumes are expressed in (e.g. 'byte'). |
| `volume` | `integer` | No | Consumed data volume for the tenant, mirroring localVolume for backward compatibility. Always emitted even though it is not part of required. Metadata: format = int64. |
| `localVolume` | `integer` | Yes | Data volume consumed locally by the tenant. Metadata: format = int64. |
| `externalVolume` | `integer` | Yes | Data volume consumed externally by the tenant. Metadata: format = int64. |
| `consumptionType` | `string` | Yes | Type of data consumption the volume is reported for. |

</details>

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.license.data.volume.consumption.aggregated",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "total": 42,
    "dataVolume": {
      "unit": "string",
      "volume": 42,
      "localVolume": 42,
      "externalVolume": 42,
      "consumptionType": "string"
    },
    "globalConsumption": 42,
    "globalConsumptionUnit": "byte",
    "totalLocalConsumption": 42,
    "licenseHighWatermarkWithinMonth": 42,
    "licenseHighWatermarkWithinMonthUnit": "byte"
  },
  "tenantid": "string"
}
```


### com.qlik.license.definition.updated

**Title:** Definition updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a license definition is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.license.definition.updated". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `valid` | `object` | No | The interval during which the definition is valid. |
| `license` | `string` | Yes | License number. |
| `changeTime` | `string` | No | Timestamp of when the definition change was recorded. Metadata: format = "date-time". |
| `updateTime` | `string` | No | Timestamp of when the definition was updated. Metadata: format = "date-time". |
| `licenseType` | `string` | No | The type of the license. |
| `parentLicense` | `string` | No | Parent license number. |
| `latestValidTime` | `string` | No | The latest time the definition is valid. Emitted as null when not set. Metadata: format = "date-time". |
| `capabilityBankId` | `string` | No | Capability bank id. |

<details>
<summary>Properties of `valid`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Stop` | `string` | No | End of the valid interval. |
| `Start` | `string` | No | Start of the valid interval. |

</details>

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.license.definition.updated",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "valid": {
      "Stop": "string",
      "Start": "string"
    },
    "license": "string",
    "changeTime": "2018-10-30T07:06:22Z",
    "updateTime": "2018-10-30T07:06:22Z",
    "licenseType": "string",
    "parentLicense": "string",
    "latestValidTime": "2018-10-30T07:06:22Z",
    "capabilityBankId": "string"
  },
  "userid": "string",
  "tenantid": "string"
}
```


### com.qlik.v1.license.lease.created

**Title:** Lease created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a lease is created.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.v1.license.lease.created". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.license.lease.created",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "name": "amlDepModel1",
    "size": 4,
    "excess": true,
    "license": "1234123412341234",
    "resource": "amlDepModel",
    "createdAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "excessQuantity": 42,
    "leasedQuantity": 42,
    "licenseQuantity": 42,
    "licenseUnlimited": true
  },
  "userid": "string",
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.v1.license.lease.deleted

**Title:** Lease deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a lease is deleted.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.v1.license.lease.deleted". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.license.lease.deleted",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "name": "amlDepModel1",
    "size": 4,
    "excess": true,
    "license": "1234123412341234",
    "resource": "amlDepModel",
    "createdAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "excessQuantity": 42,
    "leasedQuantity": 42,
    "licenseQuantity": 42,
    "licenseUnlimited": true
  },
  "userid": "string",
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.v1.license.lease.updated

**Title:** Lease updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a lease is updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.v1.license.lease.updated". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `_updates` | `object[]` | No | List of changes applied to the lease during the update. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | JSON path of the field that changed. |
| `newValue` | `` | Yes | Value of the field after the update. |
| `oldValue` | `` | Yes | Value of the field before the update. |

</details>

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.license.lease.updated",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "name": "amlDepModel1",
    "size": 4,
    "excess": true,
    "license": "1234123412341234",
    "_updates": [
      {
        "path": "string"
      }
    ],
    "resource": "amlDepModel",
    "createdAt": "2018-10-30T07:06:22Z",
    "updatedAt": "2018-10-30T07:06:22Z",
    "excessQuantity": 42,
    "leasedQuantity": 42,
    "licenseQuantity": 42,
    "licenseUnlimited": true
  },
  "userid": "string",
  "tenantid": "string",
  "sessionid": "string"
}
```


### com.qlik.v1.license.tenant.associated

**Title:** Tenant associated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event triggered when a tenant gets associated to a license.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | Yes | The event type identifier. Metadata: default = "com.qlik.v1.license.tenant.associated". |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `license` | `string` | Yes | License number. |
| `updateTime` | `string` | No | Timestamp of when the tenant association was updated. Metadata: format = "date-time". |
| `parentLicense` | `string` | Yes | Parent license number. |
| `previousLicense` | `string` | No | License number prior to the association. |
| `capabilityBankId` | `string` | No | Identifier of the capability bank associated with the license. |
| `previousParentLicense` | `string` | No | Parent license number prior to the association. |

</details>


**Example**

```json
{
  "id": "string",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.license.tenant.associated",
  "source": "string",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "authtype": "string",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "data": {
    "license": "string",
    "updateTime": "2018-10-30T07:06:22Z",
    "parentLicense": "string",
    "previousLicense": "string",
    "capabilityBankId": "string",
    "previousParentLicense": "string"
  },
  "userid": "string",
  "tenantid": "string"
}
```


## Schemas

### assignmentDeleted

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type. May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>



### assignmentRejected

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type. May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `message` | `string` | No | Message about why the assignment was rejected. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>



### assignmentUpdated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | Assignment type (e.g. 'analyzer_time', 'professional', etc.). May be an empty string when the assignment has no allotment name. |
| `origin` | `string` | Yes | event origin:   * `internal` - API triggered   * `external` - triggered by a sync operation  Allowed values: internal \| external. |
| `license` | `string` | Yes | License number. |
| `subject` | `string` | Yes | Subject of the user assigned access. |

</details>



### cloudEventsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier of the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | No | Type of the event. |
| `source` | `string` | No | The source of the event. |
| `specversion` | `string` | No | CloudEvents spec version. Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |



### cloudEventsQlikCommonAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authtype` | `string` | No | The type of principal that triggered the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |



### dataVolume

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | Unit the reported volumes are expressed in (e.g. 'byte'). |
| `volume` | `integer` | No | Consumed data volume for the tenant, mirroring localVolume for backward compatibility. Always emitted even though it is not part of required. Metadata: format = int64. |
| `localVolume` | `integer` | Yes | Data volume consumed locally by the tenant. Metadata: format = int64. |
| `externalVolume` | `integer` | Yes | Data volume consumed externally by the tenant. Metadata: format = int64. |
| `consumptionType` | `string` | Yes | Type of data consumption the volume is reported for. |



### dataVolumeConsumptionAggregated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer` | No | Total data volume consumption across all consumption types. Metadata: format = int64. |
| `dataVolume` | `dataVolume` | Yes |  |
| `globalConsumption` | `integer` | No | Total data volume consumed globally by the tenant. Metadata: format = int64. |
| `globalConsumptionUnit` | `string` | No | Unit the global consumption value is expressed in. |
| `totalLocalConsumption` | `integer` | Yes | Total data volume consumed locally by the tenant. Metadata: format = int64. |
| `licenseHighWatermarkWithinMonth` | `integer` | No | Highest recorded data volume consumption for the tenant within the current month. Metadata: format = int64. |
| `licenseHighWatermarkWithinMonthUnit` | `string` | No | Unit the monthly high-watermark value is expressed in. |

<details>
<summary>Properties of `dataVolume`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | `string` | Yes | Unit the reported volumes are expressed in (e.g. 'byte'). |
| `volume` | `integer` | No | Consumed data volume for the tenant, mirroring localVolume for backward compatibility. Always emitted even though it is not part of required. Metadata: format = int64. |
| `localVolume` | `integer` | Yes | Data volume consumed locally by the tenant. Metadata: format = int64. |
| `externalVolume` | `integer` | Yes | Data volume consumed externally by the tenant. Metadata: format = int64. |
| `consumptionType` | `string` | Yes | Type of data consumption the volume is reported for. |

</details>

</details>



### definitionUpdated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `valid` | `object` | No | The interval during which the definition is valid. |
| `license` | `string` | Yes | License number. |
| `changeTime` | `string` | No | Timestamp of when the definition change was recorded. Metadata: format = "date-time". |
| `updateTime` | `string` | No | Timestamp of when the definition was updated. Metadata: format = "date-time". |
| `licenseType` | `string` | No | The type of the license. |
| `parentLicense` | `string` | No | Parent license number. |
| `latestValidTime` | `string` | No | The latest time the definition is valid. Emitted as null when not set. Metadata: format = "date-time". |
| `capabilityBankId` | `string` | No | Capability bank id. |

<details>
<summary>Properties of `valid`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Stop` | `string` | No | End of the valid interval. |
| `Start` | `string` | No | Start of the valid interval. |

</details>

</details>



### leaseCreated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

</details>



### leaseDeleted

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

</details>



### leaseUpdated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier of the session related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Name of the leased resource. |
| `size` | `integer` | Yes | Size of the lease. |
| `excess` | `boolean` | Yes | Whether the lease exceeds the licensed quantity. |
| `license` | `string` | Yes | License number. |
| `_updates` | `object[]` | No | List of changes applied to the lease during the update. |
| `resource` | `string` | Yes | Identifier of the leased resource. |
| `createdAt` | `string` | Yes | Timestamp when the lease was created. Emitted as null when the lease has no recorded creation time. Metadata: format = "date-time". |
| `updatedAt` | `string` | Yes | Timestamp when the lease was last updated. Metadata: format = "date-time". |
| `excessQuantity` | `integer` | Yes | Quantity leased in excess of the licensed quantity. Metadata: format = int64. |
| `leasedQuantity` | `integer` | Yes | Quantity currently leased. Metadata: format = int64. |
| `licenseQuantity` | `integer` | Yes | Total quantity granted by the license. Metadata: format = int64. |
| `licenseUnlimited` | `boolean` | Yes | Whether the license grants an unlimited quantity. |

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | JSON path of the field that changed. |
| `newValue` | `` | Yes | Value of the field after the update. |
| `oldValue` | `` | Yes | Value of the field before the update. |

</details>

</details>



### tenantAssociated

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | Yes |  |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `license` | `string` | Yes | License number. |
| `updateTime` | `string` | No | Timestamp of when the tenant association was updated. Metadata: format = "date-time". |
| `parentLicense` | `string` | Yes | Parent license number. |
| `previousLicense` | `string` | No | License number prior to the association. |
| `capabilityBankId` | `string` | No | Identifier of the capability bank associated with the license. |
| `previousParentLicense` | `string` | No | Parent license number prior to the association. |

</details>


