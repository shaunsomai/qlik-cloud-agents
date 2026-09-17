# Automations

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Automations in Qlik Automate are no-code workflows which connect applications together.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/automations`](#get-apiv1automations) | Retrieves a list of the automations that the requesting user has access to. |
| `POST` | [`/api/v1/automations`](#post-apiv1automations) | Creates a new automation. The requesting user must be assigned the `AutomationCreator` role or have at least one of the following scopes: `automations`, `admin.automations`, `automations.private` or `automations.shared`. |
| `GET` | [`/api/v1/automations/{id}`](#get-apiv1automationsid) | Retrieves the full definition of an automation. The requesting user must be the owner of the automation and either be assigned one of the roles: `AutomationsCreator`, `TenantAdmin` or have at least one of the following scopes (depending on whether the automation is in a private or shared space): `automations`, `automations.private` or `automations.shared`. |
| `PUT` | [`/api/v1/automations/{id}`](#put-apiv1automationsid) | Updates the full definition of an automation. The requesting user must be the owner of the automation and either be assigned the `AutomationCreator` role or have at least one of the following scopes: `automations`, `admin.automations`, `automations.private` or `automations.shared`. |
| `DELETE` | [`/api/v1/automations/{id}`](#delete-apiv1automationsid) | Deletes an automation. The requesting user must meet at least one of the following conditions: |
| `POST` | [`/api/v1/automations/{id}/actions/change-owner`](#post-apiv1automationsidactionschange-owner) | Changes the owner of an automation to another user. This action removes the history and change logs of this automation. All linked connections used in the automation are detached and not moved to the new owner. The requesting user must be assigned `TenantAdmin` role or have at least one of the following scopes: `admin.automations`, `admin.automations:strict`. |
| `POST` | [`/api/v1/automations/{id}/actions/change-space`](#post-apiv1automationsidactionschange-space) | Changes the space of an automation by specifying a new space. |
| `POST` | [`/api/v1/automations/{id}/actions/copy`](#post-apiv1automationsidactionscopy) | Duplicates an existing automation. |
| `POST` | [`/api/v1/automations/{id}/actions/disable`](#post-apiv1automationsidactionsdisable) | Disables an automation so that it cannot be run. To disable an automation, the requesting user must meet at least one of the following conditions: |
| `POST` | [`/api/v1/automations/{id}/actions/enable`](#post-apiv1automationsidactionsenable) | Enables an automation so that it can be run. To enable an automation, the requesting user must meet at least one of the following conditions: |
| `POST` | [`/api/v1/automations/{id}/actions/move`](#post-apiv1automationsidactionsmove) | Changes the owner of an automation to another user. This action removes the history and change logs of this automation. All linked connections used in the automation are detached and not moved to the new owner. The requesting user must be assigned `TenantAdmin` role or have at least one of the following scopes: `admin.automations`, `admin.automations:strict`. |
| `GET` | [`/api/v1/automations/{id}/runs`](#get-apiv1automationsidruns) | Retrieves a list of runs for a specific automation. The requesting user must be the owner of the automation, or be assigned the one of roles: `TenantAdmin`, `AnalyticsAdmin`. Alternatively, the user must have at least one of the following scopes: `admin.automation-runs`, `automation-runs.private`, or `automation-runs.shared`. |
| `POST` | [`/api/v1/automations/{id}/runs`](#post-apiv1automationsidruns) | Creates a run for a specific automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement: |
| `GET` | [`/api/v1/automations/{id}/runs/{runId}`](#get-apiv1automationsidrunsrunid) | Retrieves a specific run for an automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement: |
| `POST` | [`/api/v1/automations/{id}/runs/{runId}/actions/export`](#post-apiv1automationsidrunsrunidactionsexport) | Retrieves the URL for the debug log of a specific automation run. Depending on the space the automation belongs to, the requesting user must meet the following requirement: |
| `POST` | [`/api/v1/automations/{id}/runs/{runId}/actions/retry`](#post-apiv1automationsidrunsrunidactionsretry) | Retries a specific run by creating a new run using the same inputs. Depending on the space the automation belongs to, the requesting user must meet the following requirement: |
| `POST` | [`/api/v1/automations/{id}/runs/{runId}/actions/stop`](#post-apiv1automationsidrunsrunidactionsstop) | Forcefully stops an automation run immediately. Depending on the space the automation belongs to, the requesting user must meet the following requirement: |
| `GET` | [`/api/v1/automations/usage`](#get-apiv1automationsusage) | Retrieves paginated usage metrics for automations. The requesting user must be assigned the `TenantAdmin` or `AnalyticsAdmin` role. |

## API Reference

### GET /api/v1/automations

Retrieves a list of the automations that the requesting user has access to.

- **Replaced by:** "GET:/workflows/automations"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | string | No | Pagination cursor returned from a previous request. |
| `filter` | string | No | Allowed filters: `name`, `runMode`, `lastRunStatus`, `ownerId`, `spaceId`. |
| `limit` | integer | No | The number of automations to retrieve. |
| `listAll` | boolean | No | When true, list all automations. Restricted to tenant admins and analytics admins. |
| `sort` | string | No | The field to sort by, with +- prefix indicating sort order. (`?sort=-name` => sort on the `name` field using descending order). Enum: "id", "name", "runMode", "state", "createdAt", "updatedAt", "lastRunAt", "lastRunStatus", "+id", "+name", "+runMode", "+state", "+createdAt", "+updatedAt", "+lastRunAt", "+lastRunStatus", "-id", "-name", "-runMode", "-state", "-createdAt", "-updatedAt", "-lastRunAt", "-lastRunStatus", "maxConcurrentRuns", "+maxConcurrentRuns", "-maxConcurrentRuns" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the automation. |
| `name` | string | No | The name of the automation. |
| `state` | string | No | The state of the automation. Enum: "available", "unavailable", "disabled" |
| `lastRun` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation. |
| `runMode` | string | No | Defines how the automation run is started. Enum: "manual", "scheduled", "triggered", "webhook" |
| `spaceId` | string | No | The unique identifier of the space that contains the automation. |
| `duration` | integer | No | Duration of the last run, indicated in seconds. Calculated from start and stop times. |
| `createdAt` | string | No |  |
| `lastRunAt` | string | No | The date and time when the last automation run was finished. |
| `updatedAt` | string | No |  |
| `workspace` | object | No | The workspace contains the JSON representation of the used blocks |
| `snippetIds` | string[] | No | A list of snippets that were detected in the workspace. This includes snippet blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `description` | string | No | The description of the automation. |
| `endpointIds` | string[] | No | A list of endpoints that were detected in the workspace. This includes endpoints present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `connectorIds` | string[] | No | A list of connectors that were detected in the workspace. This includes connectors present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `lastRunStatus` | string | No | The status of the last run of the automation. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "paused", "running", "starting", "stopped", "exceeded limit" |
| `executionToken` | string | No |  |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for automation. |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations',
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
# qlik-cli has not implemented support for GET /api/v1/automations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
      "name": "string",
      "state": "available",
      "lastRun": {
        "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
        "error": [
          {}
        ],
        "title": "string",
        "status": "failed",
        "context": "test_run",
        "metrics": {
          "blocks": [
            {
              "type": "endpointBlock",
              "rxBytes": 18329921,
              "txBytes": 18329921,
              "apiCalls": 40,
              "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
              "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
              "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
            }
          ],
          "network": {
            "rxBytes": 0,
            "txBytes": 0
          },
          "totalApiCalls": 0
        },
        "ownerId": "string",
        "spaceId": "string",
        "testRun": true,
        "archived": true,
        "stopTime": "2021-12-23T12:28:21.000000Z",
        "createdAt": "2021-12-23T12:28:21.000000Z",
        "isTestRun": true,
        "startTime": "2021-12-23T12:28:21.000000Z",
        "updatedAt": "2021-12-23T12:28:21.000000Z",
        "isArchived": true,
        "executedById": "string",
        "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
      },
      "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
      "runMode": "triggered",
      "spaceId": "5f0f78b239ff4f0001234567",
      "duration": "9001",
      "createdAt": "2021-12-23T12:28:21.000000Z",
      "lastRunAt": "2021-12-23T12:28:21.000000Z",
      "updatedAt": "2021-12-23T12:28:21.000000Z",
      "workspace": {},
      "snippetIds": [
        "e0e720d0-4947-11ec-a1d2-9559fa35801d"
      ],
      "description": "string",
      "endpointIds": [
        "9d94bef0-b28c-11eb-8dba-01593c457362",
        "53a6fb70-b28f-11eb-b601-b545a40867e0"
      ],
      "connectorIds": [
        "0d87808f-27c0-11ea-921c-022e6b5ea1e2",
        "0d86ee8a-27c0-11ea-921c-022e6b5ea1e2"
      ],
      "lastRunStatus": "finished",
      "executionToken": "aZXuEogT9X3le0k0WXMBnzuYKq4xRlkDnurjs8NVhEAAW1BYx8C1PpIl3ielgRb1",
      "maxConcurrentRuns": 10
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/automations

Creates a new automation. The requesting user must be assigned the `AutomationCreator` role or have at least one of the following scopes: `automations`, `admin.automations`, `automations.private` or `automations.shared`.

- **Replaced by:** "POST:/workflows/automations"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Automation object to create

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `spaceId` | string | No |  |
| `schedules` | object[] | No |  |
| `workspace` | object | No | The workspace generated by the Qlik Automate editor. |
| `description` | string | No |  |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for this automation. The maximum value is defined in automations settings. |

<details>
<summary>Properties of `schedules`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stopAt` | string | No |  |
| `startAt` | string | No |  |
| `interval` | integer | No | Interval in seconds; must be a multiple of 60. Values are rounded to the nearest minute (≥30 seconds rounded up, otherwise down). |
| `timezone` | string | No |  |
| `recurrence` | string | No | The RRULE that defines when the automation runs. When provided, it takes precedence over interval. |

</details>

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No | The name of the automation. |
| `state` | string | No | The state of the automation. Enum: "available", "unavailable", "disabled" |
| `lastRun` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation. |
| `runMode` | string | No | Defines how the automation run is started. Enum: "manual", "scheduled", "triggered", "webhook" |
| `spaceId` | string | No | The unique identifier of the space that contains the automation. |
| `createdAt` | string | No |  |
| `lastRunAt` | string | No | The date and time when the last automation run was finished. |
| `schedules` | object[] | No |  |
| `updatedAt` | string | No |  |
| `workspace` | object | No | The workspace generated by the Qlik Automate editor. |
| `snippetIds` | string[] | No | A list of snippets that were detected in the workspace. This includes snippet blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `description` | string | No | The description of the automation. |
| `endpointIds` | string[] | No | A list of endpoints that were detected in the workspace. This includes endpoints present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `connectorIds` | string[] | No | A list of connectors that were detected in the workspace. This includes connectors present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `lastRunStatus` | string | No | The status of the last run of the automation. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "paused", "running", "starting", "stopped", "exceeded limit" |
| `executionToken` | string | No | Execution token required to authorize the execution of the automation. |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for this automation. |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | object[] | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | object | No |  |
| `totalApiCalls` | integer | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `network`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `schedules`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `stopAt` | string | No |  |
| `startAt` | string | No |  |
| `interval` | integer | No | Interval in seconds. |
| `timezone` | string | No |  |
| `nextRunAt` | string | No |  |
| `recurrence` | string | No | The RRULE that defines when the automation runs. |
| `lastStartedAt` | string | No |  |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      spaceId: 'string',
      schedules: [
        {
          stopAt: '2022-12-01 00:00:00',
          startAt: '2022-01-01 00:00:00',
          interval: 60,
          timezone: 'Europe/Stockholm',
          recurrence:
            'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0',
        },
      ],
      workspace: {},
      description: 'string',
      maxConcurrentRuns: 1,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","spaceId":"string","schedules":[{"stopAt":"2022-12-01 00:00:00","startAt":"2022-01-01 00:00:00","interval":60,"timezone":"Europe/Stockholm","recurrence":"RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0"}],"workspace":{},"description":"string","maxConcurrentRuns":1}'
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "string",
  "state": "available",
  "lastRun": {
    "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
    "error": [
      {}
    ],
    "title": "string",
    "status": "failed",
    "context": "test_run",
    "metrics": {
      "blocks": [
        {
          "type": "endpointBlock",
          "rxBytes": 18329921,
          "txBytes": 18329921,
          "apiCalls": 40,
          "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "network": {
        "rxBytes": 0,
        "txBytes": 0
      },
      "totalApiCalls": 0
    },
    "ownerId": "string",
    "spaceId": "string",
    "testRun": true,
    "archived": true,
    "stopTime": "2021-12-23T12:28:21.000000Z",
    "createdAt": "2021-12-23T12:28:21.000000Z",
    "isTestRun": true,
    "startTime": "2021-12-23T12:28:21.000000Z",
    "updatedAt": "2021-12-23T12:28:21.000000Z",
    "isArchived": true,
    "executedById": "string",
    "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
  },
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "runMode": "triggered",
  "spaceId": "5f0f78b239ff4f0001234567",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "lastRunAt": "2021-12-23T12:28:21.000000Z",
  "schedules": [
    {
      "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
      "stopAt": "2022-12-01 00:00:00",
      "startAt": "2021-12-01 00:00:00",
      "interval": 60,
      "timezone": "Europe/Stockholm",
      "nextRunAt": "2021-12-01 00:00:00",
      "recurrence": "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0",
      "lastStartedAt": "2022-01-01T12:28:21.000000Z"
    }
  ],
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "workspace": {},
  "snippetIds": [
    "e0e720d0-4947-11ec-a1d2-9559fa35801d"
  ],
  "description": "string",
  "endpointIds": [
    "9d94bef0-b28c-11eb-8dba-01593c457362",
    "53a6fb70-b28f-11eb-b601-b545a40867e0"
  ],
  "connectorIds": [
    "0d87808f-27c0-11ea-921c-022e6b5ea1e2",
    "0d86ee8a-27c0-11ea-921c-022e6b5ea1e2"
  ],
  "lastRunStatus": "finished",
  "executionToken": "aZXuEogT9X3le0k0WXMBnzuYKq4xRlkDnurjs8NVhEAAW1BYx8C1PpIl3ielgRb1",
  "maxConcurrentRuns": 10
}
```

---

### GET /api/v1/automations/{id}

Retrieves the full definition of an automation. The requesting user must be the owner of the automation and either be assigned one of the roles: `AutomationsCreator`, `TenantAdmin` or have at least one of the following scopes (depending on whether the automation is in a private or shared space): `automations`, `automations.private` or `automations.shared`.

- **Replaced by:** "GET:/workflows/automations/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No | The name of the automation. |
| `state` | string | No | The state of the automation. Enum: "available", "unavailable", "disabled" |
| `lastRun` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation. |
| `runMode` | string | No | Defines how the automation run is started. Enum: "manual", "scheduled", "triggered", "webhook" |
| `spaceId` | string | No | The unique identifier of the space that contains the automation. |
| `createdAt` | string | No |  |
| `lastRunAt` | string | No | The date and time when the last automation run was finished. |
| `schedules` | object[] | No |  |
| `updatedAt` | string | No |  |
| `workspace` | object | No | The workspace generated by the Qlik Automate editor. |
| `snippetIds` | string[] | No | A list of snippets that were detected in the workspace. This includes snippet blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `description` | string | No | The description of the automation. |
| `endpointIds` | string[] | No | A list of endpoints that were detected in the workspace. This includes endpoints present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `connectorIds` | string[] | No | A list of connectors that were detected in the workspace. This includes connectors present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `lastRunStatus` | string | No | The status of the last run of the automation. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "paused", "running", "starting", "stopped", "exceeded limit" |
| `executionToken` | string | No | Execution token required to authorize the execution of the automation. |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for this automation. |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | object[] | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | object | No |  |
| `totalApiCalls` | integer | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `network`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `schedules`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `stopAt` | string | No |  |
| `startAt` | string | No |  |
| `interval` | integer | No | Interval in seconds. |
| `timezone` | string | No |  |
| `nextRunAt` | string | No |  |
| `recurrence` | string | No | The RRULE that defines when the automation runs. |
| `lastStartedAt` | string | No |  |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/automations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "string",
  "state": "available",
  "lastRun": {
    "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
    "error": [
      {}
    ],
    "title": "string",
    "status": "failed",
    "context": "test_run",
    "metrics": {
      "blocks": [
        {
          "type": "endpointBlock",
          "rxBytes": 18329921,
          "txBytes": 18329921,
          "apiCalls": 40,
          "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "network": {
        "rxBytes": 0,
        "txBytes": 0
      },
      "totalApiCalls": 0
    },
    "ownerId": "string",
    "spaceId": "string",
    "testRun": true,
    "archived": true,
    "stopTime": "2021-12-23T12:28:21.000000Z",
    "createdAt": "2021-12-23T12:28:21.000000Z",
    "isTestRun": true,
    "startTime": "2021-12-23T12:28:21.000000Z",
    "updatedAt": "2021-12-23T12:28:21.000000Z",
    "isArchived": true,
    "executedById": "string",
    "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
  },
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "runMode": "triggered",
  "spaceId": "5f0f78b239ff4f0001234567",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "lastRunAt": "2021-12-23T12:28:21.000000Z",
  "schedules": [
    {
      "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
      "stopAt": "2022-12-01 00:00:00",
      "startAt": "2021-12-01 00:00:00",
      "interval": 60,
      "timezone": "Europe/Stockholm",
      "nextRunAt": "2021-12-01 00:00:00",
      "recurrence": "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0",
      "lastStartedAt": "2022-01-01T12:28:21.000000Z"
    }
  ],
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "workspace": {},
  "snippetIds": [
    "e0e720d0-4947-11ec-a1d2-9559fa35801d"
  ],
  "description": "string",
  "endpointIds": [
    "9d94bef0-b28c-11eb-8dba-01593c457362",
    "53a6fb70-b28f-11eb-b601-b545a40867e0"
  ],
  "connectorIds": [
    "0d87808f-27c0-11ea-921c-022e6b5ea1e2",
    "0d86ee8a-27c0-11ea-921c-022e6b5ea1e2"
  ],
  "lastRunStatus": "finished",
  "executionToken": "aZXuEogT9X3le0k0WXMBnzuYKq4xRlkDnurjs8NVhEAAW1BYx8C1PpIl3ielgRb1",
  "maxConcurrentRuns": 10
}
```

---

### PUT /api/v1/automations/{id}

Updates the full definition of an automation. The requesting user must be the owner of the automation and either be assigned the `AutomationCreator` role or have at least one of the following scopes: `automations`, `admin.automations`, `automations.private` or `automations.shared`.

- **Replaced by:** "PUT:/workflows/automations/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Required**

Automation object to update

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `schedules` | object[] | No |  |
| `workspace` | object | No | The workspace generated by the Qlik Automate editor. |
| `description` | string | No |  |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for this automation. The maximum value is defined in automations settings. |

<details>
<summary>Properties of `schedules`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stopAt` | string | No |  |
| `startAt` | string | No |  |
| `interval` | integer | No | Interval in seconds; must be a multiple of 60. Values are rounded to the nearest minute (≥30 seconds rounded up, otherwise down). |
| `timezone` | string | No |  |
| `recurrence` | string | No | The RRULE that defines when the automation runs. When provided, it takes precedence over interval. |

</details>

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `name` | string | No | The name of the automation. |
| `state` | string | No | The state of the automation. Enum: "available", "unavailable", "disabled" |
| `lastRun` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation. |
| `runMode` | string | No | Defines how the automation run is started. Enum: "manual", "scheduled", "triggered", "webhook" |
| `spaceId` | string | No | The unique identifier of the space that contains the automation. |
| `createdAt` | string | No |  |
| `lastRunAt` | string | No | The date and time when the last automation run was finished. |
| `schedules` | object[] | No |  |
| `updatedAt` | string | No |  |
| `workspace` | object | No | The workspace generated by the Qlik Automate editor. |
| `snippetIds` | string[] | No | A list of snippets that were detected in the workspace. This includes snippet blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `description` | string | No | The description of the automation. |
| `endpointIds` | string[] | No | A list of endpoints that were detected in the workspace. This includes endpoints present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `connectorIds` | string[] | No | A list of connectors that were detected in the workspace. This includes connectors present in blocks that are not connected to other blocks. Order of GUIDs is not guaranteed. |
| `lastRunStatus` | string | No | The status of the last run of the automation. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "paused", "running", "starting", "stopped", "exceeded limit" |
| `executionToken` | string | No | Execution token required to authorize the execution of the automation. |
| `maxConcurrentRuns` | integer | No | Maximum number of concurrent runs allowed for this automation. |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | object[] | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | object | No |  |
| `totalApiCalls` | integer | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `network`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `schedules`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `stopAt` | string | No |  |
| `startAt` | string | No |  |
| `interval` | integer | No | Interval in seconds. |
| `timezone` | string | No |  |
| `nextRunAt` | string | No |  |
| `recurrence` | string | No | The RRULE that defines when the automation runs. |
| `lastStartedAt` | string | No |  |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/automations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'string',
      schedules: [
        {
          stopAt: '2022-12-01 00:00:00',
          startAt: '2022-01-01 00:00:00',
          interval: 60,
          timezone: 'Europe/Stockholm',
          recurrence:
            'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0',
        },
      ],
      workspace: {},
      description: 'string',
      maxConcurrentRuns: 1,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/automations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string","schedules":[{"stopAt":"2022-12-01 00:00:00","startAt":"2022-01-01 00:00:00","interval":60,"timezone":"Europe/Stockholm","recurrence":"RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0"}],"workspace":{},"description":"string","maxConcurrentRuns":1}'
```

**Example Response:**

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "string",
  "state": "available",
  "lastRun": {
    "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
    "error": [
      {}
    ],
    "title": "string",
    "status": "failed",
    "context": "test_run",
    "metrics": {
      "blocks": [
        {
          "type": "endpointBlock",
          "rxBytes": 18329921,
          "txBytes": 18329921,
          "apiCalls": 40,
          "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
        }
      ],
      "network": {
        "rxBytes": 0,
        "txBytes": 0
      },
      "totalApiCalls": 0
    },
    "ownerId": "string",
    "spaceId": "string",
    "testRun": true,
    "archived": true,
    "stopTime": "2021-12-23T12:28:21.000000Z",
    "createdAt": "2021-12-23T12:28:21.000000Z",
    "isTestRun": true,
    "startTime": "2021-12-23T12:28:21.000000Z",
    "updatedAt": "2021-12-23T12:28:21.000000Z",
    "isArchived": true,
    "executedById": "string",
    "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
  },
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "runMode": "triggered",
  "spaceId": "5f0f78b239ff4f0001234567",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "lastRunAt": "2021-12-23T12:28:21.000000Z",
  "schedules": [
    {
      "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
      "stopAt": "2022-12-01 00:00:00",
      "startAt": "2021-12-01 00:00:00",
      "interval": 60,
      "timezone": "Europe/Stockholm",
      "nextRunAt": "2021-12-01 00:00:00",
      "recurrence": "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0",
      "lastStartedAt": "2022-01-01T12:28:21.000000Z"
    }
  ],
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "workspace": {},
  "snippetIds": [
    "e0e720d0-4947-11ec-a1d2-9559fa35801d"
  ],
  "description": "string",
  "endpointIds": [
    "9d94bef0-b28c-11eb-8dba-01593c457362",
    "53a6fb70-b28f-11eb-b601-b545a40867e0"
  ],
  "connectorIds": [
    "0d87808f-27c0-11ea-921c-022e6b5ea1e2",
    "0d86ee8a-27c0-11ea-921c-022e6b5ea1e2"
  ],
  "lastRunStatus": "finished",
  "executionToken": "aZXuEogT9X3le0k0WXMBnzuYKq4xRlkDnurjs8NVhEAAW1BYx8C1PpIl3ielgRb1",
  "maxConcurrentRuns": 10
}
```

---

### DELETE /api/v1/automations/{id}

Deletes an automation. The requesting user must meet at least one of the following conditions:
- be the owner of the automation
- be assigned one of the following roles: `AnalyticsAdmin`, `TenantAdmin`
- have at least one of the following scopes: `admin.automations`, `admin.automations:strict`, `automations.private`, or `automations.shared`

- **Replaced by:** "DELETE:/workflows/automations/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Responses

##### 204

No Content

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/automations/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}',
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
# qlik-cli has not implemented support for DELETE /api/v1/automations/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automations/{id}/actions/change-owner

Changes the owner of an automation to another user. This action removes the history and change logs of this automation. All linked connections used in the automation are detached and not moved to the new owner. The requesting user must be assigned `TenantAdmin` role or have at least one of the following scopes: `admin.automations`, `admin.automations:strict`.

- **Replaced by:** "POST:/workflows/automations/{id}/actions/change-owner"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | Yes | The unique identifier of the new owner. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/change-owner` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/change-owner',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      userId: 'sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/change-owner yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/change-owner" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"userId":"sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy"}'
```

---

### POST /api/v1/automations/{id}/actions/change-space

Changes the space of an automation by specifying a new space.

- **Replaced by:** "POST:/workflows/automations/{id}/actions/change-space"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | The unique identifier of the new space. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/change-space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/change-space',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      spaceId: '5f0f78b239ff4f0001234567',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/change-space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/change-space" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"spaceId":"5f0f78b239ff4f0001234567"}'
```

---

### POST /api/v1/automations/{id}/actions/copy

Duplicates an existing automation.

- **Replaced by:** "POST:/workflows/automations/{id}/actions/copy"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the new automation. |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier for the automation. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/copy` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/copy',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: 'string' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/copy yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/copy" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"string"}'
```

**Example Response:**

```json
{
  "id": "00000000-0000-0000-0000-000000000000"
}
```

---

### POST /api/v1/automations/{id}/actions/disable

Disables an automation so that it cannot be run. To disable an automation, the requesting user must meet at least one of the following conditions:
- be the owner of the automation
- be assigned one of the following roles: `TenantAdmin`, `AnalyticsAdmin`
- have at least one of the following scopes: `admin.automations`, `admin.automations:strict`, `automations.private`, or `automations.shared`

- **Replaced by:** "POST:/workflows/automations/{id}/actions/disable"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/disable` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/disable',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/disable yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/disable" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automations/{id}/actions/enable

Enables an automation so that it can be run. To enable an automation, the requesting user must meet at least one of the following conditions:
- be the owner of the automation
- be assigned one of the following roles: `AnalyticsAdmin`, `TenantAdmin`
- have at least one of the following scopes: `admin.automations`, `admin.automations:strict`, `automations.private`, or `automations.shared`

- **Replaced by:** "POST:/workflows/automations/{id}/actions/enable"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/enable` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/enable',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/enable yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/enable" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automations/{id}/actions/move

Changes the owner of an automation to another user. This action removes the history and change logs of this automation. All linked connections used in the automation are detached and not moved to the new owner. The requesting user must be assigned `TenantAdmin` role or have at least one of the following scopes: `admin.automations`, `admin.automations:strict`.

- **Replaced by:** "POST:/workflows/automations/{id}/actions/move"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | Yes |  |

#### Responses

##### 204

No Content

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/actions/move` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/actions/move',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      userId: 'sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/actions/move yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/actions/move" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"userId":"sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy"}'
```

---

### GET /api/v1/automations/{id}/runs

Retrieves a list of runs for a specific automation. The requesting user must be the owner of the automation, or be assigned the one of roles: `TenantAdmin`, `AnalyticsAdmin`. Alternatively, the user must have at least one of the following scopes: `admin.automation-runs`, `automation-runs.private`, or `automation-runs.shared`.

- **Replaced by:** "GET:/workflows/automations/{id}/runs"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | string | No | Pagination cursor returned from a previous request. |
| `filter` | string | No | Allowed filters: `status`, `context`, `startTime`, `title`, `spaceId`, `ownerId`, `executedById`, `billable`. |
| `limit` | integer | No | The number of runs to retrieve. |
| `sort` | string | No | The field to sort by, with +- prefix indicating sort order. (`?query=-startTime` => sort on the `startTime` field using descending order). Enum: "id", "status", "startTime", "-id", "-status", "-startTime", "+id", "+status", "+startTime" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The context set by the source that triggers the automation. Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `duration` | integer | No | Duration of the run, indicated in seconds. Calculated from start and stop times |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automations/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs',
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
# qlik-cli has not implemented support for GET /api/v1/automations/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
      "error": [
        {}
      ],
      "title": "string",
      "status": "failed",
      "context": "test_run",
      "ownerId": "string",
      "spaceId": "string",
      "testRun": true,
      "archived": true,
      "duration": "9001",
      "stopTime": "2021-12-23T12:28:21.000000Z",
      "createdAt": "2021-12-23T12:28:21.000000Z",
      "isTestRun": true,
      "startTime": "2021-12-23T12:28:21.000000Z",
      "updatedAt": "2021-12-23T12:28:21.000000Z",
      "isArchived": true,
      "executedById": "string",
      "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/automations/{id}/runs

Creates a run for a specific automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement:
- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

- **Replaced by:** "POST:/workflows/automations/{id}/runs"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |

#### Request Body

**Required**

Run object to create

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | The source that triggers the automation will set the context. Enum: "api" |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | object[] | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | object | No |  |
| `totalApiCalls` | integer | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Type of the block. Enum: "snippetBlock", "endpointBlock" |
| `rxBytes` | integer | Yes | Total amount of received bytes sent by the current block. |
| `txBytes` | integer | Yes | Total amount of sent bytes sent by the current block. |
| `apiCalls` | integer | No | API calls to external resources made by the current block. |
| `snippetId` | string | No | Unique identifier for the snippet block used within the execution. |
| `endpointId` | string | No | Unique identifier for the endpoint block used within the execution. |
| `connectorId` | string | No | Unique identifier for the connector used within the block of the execution. |

</details>

<details>
<summary>Properties of `network`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rxBytes` | integer | No | The number of received bytes. |
| `txBytes` | integer | No | The number of sent bytes. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/runs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ context: 'api' }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/runs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"context":"api"}'
```

**Example Response:**

```json
{
  "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
  "error": [
    {}
  ],
  "title": "string",
  "status": "failed",
  "context": "test_run",
  "metrics": {
    "blocks": [
      {
        "type": "endpointBlock",
        "rxBytes": 18329921,
        "txBytes": 18329921,
        "apiCalls": 40,
        "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      }
    ],
    "network": {
      "rxBytes": 0,
      "txBytes": 0
    },
    "totalApiCalls": 0
  },
  "ownerId": "string",
  "spaceId": "string",
  "testRun": true,
  "archived": true,
  "stopTime": "2021-12-23T12:28:21.000000Z",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "isTestRun": true,
  "startTime": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "isArchived": true,
  "executedById": "string",
  "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
}
```

---

### GET /api/v1/automations/{id}/runs/{runId}

Retrieves a specific run for an automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement:
- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

- **Replaced by:** "GET:/workflows/automations/{id}/runs/{runId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |
| `runId` | string | Yes | The unique identifier for the run. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique identifier of the run. |
| `error` | object[] | No | List of errors that occurred during the automation run. |
| `title` | string | No | The title of the automation run. |
| `status` | string | No | The current status of the automation run. Enum: "failed", "finished", "finished with warnings", "must stop", "not started", "running", "starting", "stopped", "exceeded limit", "queued" |
| `context` | string | No | The source that triggers the automation will set the context. Certain contexts impact the execution of an automation (for example, The "test_run" context will not process all results when listing items). Enum: "test_run", "editor", "detail", "api_sync", "api_async", "webhook", "lookup" |
| `metrics` | object | No |  |
| `ownerId` | string | No | The unique identifier of the owner of the automation run. |
| `spaceId` | string | No | The unique identifier of the space in which the automation run is created. |
| `testRun` | boolean | No | Indicates if this automation run is a test run. |
| `archived` | boolean | No | Indicates if this automation run is archived. |
| `stopTime` | string | No | The date and time at which the automation run stopped. |
| `createdAt` | string | No |  |
| `isTestRun` | boolean | No | Indicates if this automation run is a test run. |
| `startTime` | string | No | The date and time at which the automation run started. |
| `updatedAt` | string | No |  |
| `isArchived` | boolean | No | Indicates if this automation run is archived. |
| `executedById` | string | No | The unique identifier of the user who executed the automation run. |
| `scheduledStartTime` | string | No | The date and time at which the automation run is scheduled to start. |

<details>
<summary>Properties of `metrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `blocks` | object[] | No | List of blocks used during execution. Note: this list currently only contains endpointBlocks and snippetBlocks |
| `network` | object | No |  |
| `totalApiCalls` | integer | No | The number of API calls made. |

<details>
<summary>Properties of `blocks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Type of the block. Enum: "snippetBlock", "endpointBlock" |
| `rxBytes` | integer | Yes | Total amount of received bytes sent by the current block. |
| `txBytes` | integer | Yes | Total amount of sent bytes sent by the current block. |
| `apiCalls` | integer | No | API calls to external resources made by the current block. |
| `snippetId` | string | No | Unique identifier for the snippet block used within the execution. |
| `endpointId` | string | No | Unique identifier for the endpoint block used within the execution. |
| `connectorId` | string | No | Unique identifier for the connector used within the block of the execution. |

</details>

<details>
<summary>Properties of `network`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rxBytes` | integer | No | The number of received bytes. |
| `txBytes` | integer | No | The number of sent bytes. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automations/{id}/runs/{runId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs/{runId}',
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
# qlik-cli has not implemented support for GET /api/v1/automations/{id}/runs/{runId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs/{runId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "d452d100-9b0b-11ec-b199-8323e1031c3e",
  "error": [
    {}
  ],
  "title": "string",
  "status": "failed",
  "context": "test_run",
  "metrics": {
    "blocks": [
      {
        "type": "endpointBlock",
        "rxBytes": 18329921,
        "txBytes": 18329921,
        "apiCalls": 40,
        "snippetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "endpointId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
        "connectorId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4"
      }
    ],
    "network": {
      "rxBytes": 0,
      "txBytes": 0
    },
    "totalApiCalls": 0
  },
  "ownerId": "string",
  "spaceId": "string",
  "testRun": true,
  "archived": true,
  "stopTime": "2021-12-23T12:28:21.000000Z",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "isTestRun": true,
  "startTime": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "isArchived": true,
  "executedById": "string",
  "scheduledStartTime": "2021-12-23T12:28:21.000000Z"
}
```

---

### POST /api/v1/automations/{id}/runs/{runId}/actions/export

Retrieves the URL for the debug log of a specific automation run. Depending on the space the automation belongs to, the requesting user must meet the following requirement:
- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

- **Replaced by:** "POST:/workflows/automations/{id}/runs/{runId}/actions/export"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |
| `runId` | string | Yes | The unique identifier for the run. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No |  |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/runs/{runId}/actions/export` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs/{runId}/actions/export',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/runs/{runId}/actions/export yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs/{runId}/actions/export" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "url": "https://{tenantname}.{region}.qlikcloud.com/api/v1/automations/{id}/runs/{runId}/debug"
}
```

---

### POST /api/v1/automations/{id}/runs/{runId}/actions/retry

Retries a specific run by creating a new run using the same inputs. Depending on the space the automation belongs to, the requesting user must meet the following requirement:
- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

- **Replaced by:** "POST:/workflows/automations/{id}/runs/{runId}/actions/retry"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |
| `runId` | string | Yes | The unique identifier for the run. |

#### Responses

##### 204

OK Response

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/runs/{runId}/actions/retry` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs/{runId}/actions/retry',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/runs/{runId}/actions/retry yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs/{runId}/actions/retry" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/automations/{id}/runs/{runId}/actions/stop

Forcefully stops an automation run immediately. Depending on the space the automation belongs to, the requesting user must meet the following requirement:
- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

- **Replaced by:** "POST:/workflows/automations/{id}/runs/{runId}/actions/stop"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier for the automation. |
| `runId` | string | Yes | The unique identifier for the run. |

#### Responses

##### 204

OK Response

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/automations/{id}/runs/{runId}/actions/stop` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/{id}/runs/{runId}/actions/stop',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/automations/{id}/runs/{runId}/actions/stop yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/{id}/runs/{runId}/actions/stop" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/automations/usage

Retrieves paginated usage metrics for automations. The requesting user must be assigned the `TenantAdmin` or `AnalyticsAdmin` role.

- **Replaced by:** "GET:/workflows/automations/usage"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | Yes | Indicates how the metrics should be filtered using a SCIM-style expression. Available parameters: - name (specify one or more enums to return specific metrics. Supported enum values: `runs`, `scheduledRuns`, `triggeredRuns`, `webhookRuns`, `duration`, `bandwidthIn`, `bandwidthOut`) - date (return a metric for a specific date or range of dates, e.g. "2025-08-01") |
| `breakdownBy` | string | No | If specified, result will be broken apart for each automation |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `date` | string | Yes | The date for the metric |
| `name` | string | Yes | The name for the metric Enum: "runs", "scheduledRun", "triggeredRun", "webhookRuns", "duration", "bandwidthIn", "bandwidthOut" |
| `value` | integer | Yes | The value count of the metric |
| `automation` | object | No |  |

<details>
<summary>Properties of `automation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | string | No | The unique identifier for the automation. |
| `name` | string | No | The name for the automation. |
| `ownerId` | string | No | The unique identifier for the user who owns the automation |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/automations/usage` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/automations/usage',
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
# qlik-cli has not implemented support for GET /api/v1/automations/usage yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/automations/usage" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "date": "2021-12-15",
      "name": "bandwidthIn",
      "value": 310179713,
      "automation": {
        "guid": "00000000-0000-0000-0000-000000000000",
        "name": "My Automation.",
        "ownerId": "KP1zJiPDn0gsla236GmETadFcxBW-J8F"
      }
    }
  ]
}
```

---
