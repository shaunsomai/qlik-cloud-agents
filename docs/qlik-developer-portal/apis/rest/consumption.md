# Entitlement consumption

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Tracks usage of entitled features in a tenant, used for the consumption metrics in the admin console in a tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/consumption/executions`](#get-apiv1consumptionexecutions) | Lists of execution records by tenant. |

## API Reference

### GET /api/v1/consumption/executions

Lists of execution records by tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `actionToBlock` | string | No |  |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax.  example `taskName eq "automation_run_ended" or taskName eq "report_triggered" or or taskName eq "dataVolumeAggregated"`  The following fields are supported: `scope`, `resourcetype`, `resourceaction`, `resourceid`, `capacitylimit`, `localusage`, `globalusage`, `overage`, `blocked`, `periodstart`, `periodend`, `consumptionreportid`, `blockedeventtime`, `overageeventtime`, `taskname`, `taskdescription`, `userid`, `tenantid`, `customerfacing`, `actiontoblock` |
| `limit` | integer | No | Limit the returned result set |
| `offset` | integer | No | Offset for pagination - how many elements to skip |
| `page` | string | No | The cursor to the page of data. |
| `periodsToInclude` | string[] | No | Specifies which periods to include regardless of the period type, start and end specified Enum: "current", "previous" |
| `sort` | string[] | No | Enum: "periodstart", "-periodstart", "+periodstart", "periodend", "-periodend", "+periodend" |

#### Responses

##### 200

The executions list has been successfully returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `data` | object[] | No |  |
| `links` | object | No |  |
| `overage` | boolean | No |  |
| `closeToOverage` | boolean | No |  |
| `globalUsageAvailable` | boolean | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | string | No | Unit of measurement for the resource consumption |
| `scope` | string[] | No | Enum: "user", "tenant", "resourceId", "resourceType", "resourceAction" |
| `userId` | string | No | The user id. |
| `blocked` | boolean | No |  |
| `overage` | boolean | No |  |
| `segments` | object[] | No |  |
| `taskName` | string | No | The resource task name. |
| `tenantId` | string | No | The tenant id. |
| `periodEnd` | string | No | The end of the associated period. |
| `localUsage` | number | No | The local usage. |
| `periodType` | string | No | Enum: "day", "month", "year", "", "fixed", "minute" |
| `resourceId` | string | No | The resource id. |
| `updateTime` | string | No | The RFC3339 timestamp when the resource was updated. |
| `enforcement` | object[] | No | Contains a list of resources that are blocked when quota for this is reached. |
| `globalUsage` | number | No | The global usage. |
| `periodStart` | string | No | The start of the associated period. |
| `resourceType` | string | No | The resource type. Enum: "app", "automations", "space", "data.volume.consumption" |
| `scopeMapping` | string | No | The map to the resource scope. |
| `capacityLimit` | number | No | The capacity limit. |
| `closeToOverage` | boolean | No |  |
| `customerFacing` | boolean | No | The field to determine if a resource should be visible on the client. |
| `guardrailLimit` | number | No | The guardrail limit. |
| `resourceAction` | string | No | The resource action. Enum: "report.generated", "reload", "scheduledReload", "executed", "aggregation", "import", "updated", "deployed", "3rd_party_executed", "standard_executed" |
| `taskDescription` | string | No | The resource task description. |
| `blockedEventTime` | string | No | RFC3339 timestamp when a block event was last emitted for this execution. |
| `overageEventTime` | string | No | RFC3339 timestamp when a overage event was last emitted for this execution. |
| `consumptionReportId` | string | No | The id of the consumption report |

<details>
<summary>Properties of `enforcement`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resourceType` | string | No | Resource type to be blocked |
| `actionToBlock` | string | No | Resource action type to be blocked |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | URL to particular set of elements |
| `type` | string | No | Page type, can be next or prev Enum: "prev", "next" |
| `token` | string | No | Page unique token |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | URL to particular set of elements |
| `type` | string | No | Page type, can be next or prev Enum: "prev", "next" |
| `token` | string | No | Page unique token |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to usage-tracker. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to usage-tracker. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to usage-tracker. |
| `meta` | object | No | meta properties for an error. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/consumption/executions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/consumption/executions',
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
# qlik-cli has not implemented support for GET /api/v1/consumption/executions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/consumption/executions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 1,
  "currentPageCount": 1,
  "data": [
    {
      "unit": "string",
      "scope": [
        "tenant",
        "resourceType"
      ],
      "userId": "string",
      "blocked": false,
      "overage": false,
      "segments": [
        {
          "QDI": 10
        },
        {
          "APP": 10
        }
      ],
      "taskName": "task_name",
      "tenantId": "string",
      "periodEnd": "2022-01-31",
      "localUsage": 20,
      "periodType": "month",
      "resourceId": "228ac375-086e-4652-b9c0-fa8689bac75f",
      "updateTime": "string",
      "enforcement": [
        {
          "resourceType": "string",
          "actionToBlock": "string"
        }
      ],
      "globalUsage": 29,
      "periodStart": "2022-01-01",
      "resourceType": "app",
      "scopeMapping": "string",
      "capacityLimit": 50,
      "closeToOverage": false,
      "customerFacing": true,
      "guardrailLimit": 20,
      "resourceAction": "reload",
      "taskDescription": "some description",
      "blockedEventTime": "string",
      "overageEventTime": "string",
      "consumptionReportId": "01xQ1chLoHkOikyzUGcHJquteNrAfketW"
    }
  ],
  "links": {
    "next": {
      "href": "http://localhost:8787/v1/items?limit=12",
      "type": "next",
      "token": "JwAAAAJfaWQAGQAAADVjZjUwM2NjMjVkYzlhMTM1MzYwZTVjZAAA"
    },
    "prev": {
      "href": "http://localhost:8787/v1/items?limit=12",
      "type": "next",
      "token": "JwAAAAJfaWQAGQAAADVjZjUwM2NjMjVkYzlhMTM1MzYwZTVjZAAA"
    },
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "overage": false,
  "closeToOverage": false,
  "globalUsageAvailable": true
}
```

---
