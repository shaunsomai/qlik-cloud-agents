# Data alerts

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Supports chart sharing, chart monitoring and alerting features. The legacy sharing APIs refer to chart sharing and chart monitoring, which is a feature that allows the user to send an e-mail with an embedded chart either manually (chart sharing) or in a recurring manner (chart monitoring). It also stores the history related to these actions. The alerting/ data-alerts APIs support the alerting feature, where a user is able to create alerts that trigger notifications in case a condition in the dataset of an app is fulfilled.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-alerts`](#get-apiv1data-alerts) | Retrieves all data alert tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks. |
| `POST` | [`/api/v1/data-alerts`](#post-apiv1data-alerts) | Creates a new data alerting task. |
| `GET` | [`/api/v1/data-alerts/{alertId}`](#get-apiv1data-alertsalertid) | Returns the details of a specific data alert task. |
| `PATCH` | [`/api/v1/data-alerts/{alertId}`](#patch-apiv1data-alertsalertid) | Updates one or more properties of a specific data alerting task. |
| `DELETE` | [`/api/v1/data-alerts/{alertId}`](#delete-apiv1data-alertsalertid) | Deletes a specific data alerting task. |
| `GET` | [`/api/v1/data-alerts/{alertId}/condition`](#get-apiv1data-alertsalertidcondition) | Retrieves the condition associated with a data alerting task. |
| `GET` | [`/api/v1/data-alerts/{alertId}/executions/{executionId}`](#get-apiv1data-alertsalertidexecutionsexecutionid) | Retrieves a specific execution for the specified data alerting task. |
| `DELETE` | [`/api/v1/data-alerts/{alertId}/executions/{executionId}`](#delete-apiv1data-alertsalertidexecutionsexecutionid) | Deletes a specific data alerting task execution. |
| `GET` | [`/api/v1/data-alerts/{alertId}/recipient-stats`](#get-apiv1data-alertsalertidrecipient-stats) | Retrieve the recipient stats for a data alerting task. |
| `GET` | [`/api/v1/data-alerts/{taskId}/executions`](#get-apiv1data-alertstaskidexecutions) | Lists executions for the specified data alerting task. |
| `GET` | [`/api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations`](#get-apiv1data-alertstaskidexecutionsexecutionidevaluations) | Retrieves the content of an evaluation for a specified data alerting task execution. |
| `GET` | [`/api/v1/data-alerts/{taskId}/executions/stats`](#get-apiv1data-alertstaskidexecutionsstats) | Retrieves stats for overall data alerting task executions. |
| `POST` | [`/api/v1/data-alerts/actions/trigger`](#post-apiv1data-alertsactionstrigger) | Creates a new data alerting task trigger action. |
| `POST` | [`/api/v1/data-alerts/actions/validate`](#post-apiv1data-alertsactionsvalidate) | Validates a new data alerting task. Current support includes validation for recipients only. |
| `GET` | [`/api/v1/data-alerts/settings`](#get-apiv1data-alertssettings) | Retrieves the current settings for data alerts. |
| `PUT` | [`/api/v1/data-alerts/settings`](#put-apiv1data-alertssettings) | Updates the settings for data alerts. User must be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/v1/data-alerts

Retrieves all data alert tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appID` | string | No | The app ID you would like to filter by |
| `conditionId` | string | No | The conditionId you would like to filter by |
| `limit` | integer | No | Limit the returned result set |
| `next` | string | No | The cursor to the next page of data. Only one of next or previous may be specified. |
| `offset` | integer | No | Offset for finding a list of entities - used for pagination |
| `ownerId` | string | No | The id of the owner you would like to filter by |
| `ownerName` | string | No | The name of the owner you would like to filter by |
| `prev` | string | No | The cursor to the previous page of data. Only one of next or previous may be specified. |
| `role` | string[] | No | The role you would like to filter by Enum: "owner", "recipient", "notowner" |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "-datecreated", "datecreated", "+datecreated", "-ownername", "ownername", "+ownername", "lasttrigger", "-lasttrigger", "+lasttrigger", "lastscan", "-lastscan", "+lastscan", "name", "-name", "+name", "enabled", "-enabled", "+enabled", "status", "-status", "+status", "nextexecutiontime", "-nextexecutiontime", "+nextexecutiontime" |
| `status` | string[] | No | The status you would like to filter by Enum: "INVALID_RECIPIENT", "INVALID_OWNER", "DISABLED", "VALID" |

#### Responses

##### 200

The alerting tasks list has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `links` | object | No |  |
| `tasks` | object[] | No | Gets a list of alerting tasks. |

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

<details>
<summary>Properties of `tasks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | data alerting identifier (this is the alertID) |
| `name` | string | No | name associated to alerting task |
| `appId` | string | No | appId associated to this alert definition |
| `links` | object | No |  |
| `status` | string | No | particular status of the alerting task Enum: "creating", "deleting" |
| `enabled` | boolean | No | true if the alerting task is enabled |
| `ownerId` | string | No | the owner of this alert |
| `sheetId` | string | No | sheetId associated to this alert definition |
| `lastScan` | string | No | last time a trigger was detected, but not sure if executed for requesting user |
| `tenantId` | string | No | the tenant of this alert |
| `ownerName` | string | No | the owner name of this alert |
| `accessMode` | string | No | Enum: "SOURCE_ACCESS", "TARGET_ACCESS" |
| `bookmarkId` | string | No | bookmarkId associated to this alert definition |
| `recipients` | object | No | List of recipients. An internal recipient is represented by either their user id or group id. |
| `throttling` | object | No | The rules and setup for throttling |
| `conditionId` | string | No | the id of the condition that determines if this data alert should be triggered |
| `dateCreated` | string | No | Timestamp for the creation of the task (rfc3339 format) |
| `description` | string | No | description associated to alerting task |
| `errorStatus` | string | No | error labels from the latest workflow that happened within the task Enum: "OK", "FATAL-ERROR", "PARTIAL-TRIGGER" |
| `lastTrigger` | string | No | last time an execution had been created for requesting user |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `triggerType` | string | No | Type of job that triggered the task Enum: "RELOAD", "SCHEDULED", "MANUAL" |
| `triggerStats` | object | Yes |  |
| `hideSelections` | boolean | No | Whether the selection needs to be hidden. |
| `evaluationCount` | integer | No | the number of actual evaluations with engine this task has consumed in the current month |
| `scheduleOptions` | object | No |  |
| `subscriptionIds` | string[] | No | list of subscriptions related to this alerting task |
| `absoluteLastScan` | string | No | last time a trigger was detected, but not sure if executed |
| `conditionResponse` | object | No | Should reference ConditionResponse type in condition-manager api docs |
| `alertingTaskErrors` | object[] | No |  |
| `absoluteLastTrigger` | string | No | last time an execution had been created |
| `hasHistoryCondition` | boolean | No | true if the alert has history condition enabled |
| `lastExecutionStatus` | string | No | Enum: "OK", "FAILED" |
| `recipientsChangeHistory` | object[] | No | Change in a recipient for an alerting task |
| `lastEvaluationCountUpdate` | string | No | the date when the evaluation count was updated |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | Yes | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `DLListId` | string | No | Identifier of the distribution list the recipients belong to. |
| `groupIds` | object[] | No | an internal recipient based on its group id. |

<details>
<summary>Properties of `userIds`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `groupIds`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `throttling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | integer | No | the maximum number of tokens that the bucket can contain |
| `timezone` | string | No | the timezone for time calculations in this throttlingresource, for current time and time reference. |
| `replenishRate` | integer | No | the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded) |
| `recurrenceRule` | string | No | A string that supports a subset of RFC5545 recurrence rule directives. |
| `initialTokenCount` | integer | No | the initial amount of tokens in the bucket upon creation. cannot exceed capacity. |
| `referenceTimestamp` | string | No | a date and time reference specified in RFC3339 format |

</details>

<details>
<summary>Properties of `triggerStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalScans` | integer | Yes | The number of scans for the current condition. |
| `last10Scans` | integer | Yes | The number of triggers out of the last 10 scans for the current condition. |
| `last100Scans` | integer | Yes | The number of triggers out of the last 100 scans for the current condition. |

</details>

<details>
<summary>Properties of `scheduleOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | No | The timezone for time calculations in SCHEDULED triggers, optional. |
| `recurrence` | string[] | No | List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed. |
| `endDateTime` | string | No | EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending. |
| `chronosJobID` | string | No | The chronos job identifier. It is set once the related chronos job is created. |
| `startDateTime` | string | No | StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time. |
| `lastExecutionTime` | string | No | lastExecutionTime is the time of the chronos job last execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if job has not run yet. |
| `nextExecutionTime` | string | No | nextExecutionTime is the time of the chronos job next execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if the job is completed. |

</details>

<details>
<summary>Properties of `alertingTaskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `added` | string | No | Timestamp for the creation of the error |
| `value` | string | No | Identifier for type of error occurring on alerting task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "EVAL_ERROR", "ORPHAN", "CONVERSION_DENIED", "EXPIRED", "PARTIAL_SENT", "QUOTA_REACHED", "OWNER_HAS_NO_VALID_USER_ENTITLEMENT" |

</details>

<details>
<summary>Properties of `recipientsChangeHistory`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dateTime` | string | No | time of recipient state change |
| `patchAction` | object[] | No | A custom custom JSON Patch document, as an array of objects with operation, recipient type and value. Original defined in https://datatracker.ietf.org/doc/html/rfc6902. |

<details>
<summary>Properties of `patchAction`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 42,
  "currentPageCount": 42,
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
  "tasks": [
    {
      "id": "5da5825325dc9a0dd0260af9",
      "name": "string",
      "appId": "string",
      "links": {
        "self": {
          "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
        }
      },
      "status": "creating",
      "enabled": true,
      "ownerId": "string",
      "sheetId": "string",
      "lastScan": "string",
      "tenantId": "string",
      "ownerName": "string",
      "accessMode": "SOURCE_ACCESS",
      "bookmarkId": "string",
      "recipients": {
        "DLUsers": [],
        "userIds": [
          {
            "value": "1b263bs8m0mm_s21s3f",
            "groups": [
              "addedIndividually",
              "group1",
              "group2"
            ],
            "enabled": true,
            "subscribed": true,
            "taskRecipientErrors": [
              {
                "value": "NO_ACCESS_TO_APP",
                "timestamp": "2019-10-15T16:07:01.492Z"
              }
            ],
            "alertingTaskRecipientErrors": [
              {
                "added": "2019-10-15T16:07:01.492Z",
                "value": "NO_ACCESS_TO_APP"
              }
            ]
          }
        ],
        "DLGroups": [],
        "DLListId": "dl-12345",
        "groupIds": [
          {
            "value": "group1",
            "enabled": true,
            "taskGroupRecipientErrors": [
              {
                "value": "GROUP_WITH_NO_APP_ACCESS",
                "timestamp": "2019-10-15T16:07:01.492Z"
              }
            ],
            "alertingTaskGroupRecipientErrors": [
              {
                "added": "2019-10-15T16:07:01.492Z",
                "value": "GROUP_WITH_NO_APP_ACCESS"
              }
            ]
          }
        ]
      },
      "throttling": {
        "capacity": 10,
        "timezone": "Etc/UTC",
        "replenishRate": 1,
        "recurrenceRule": "RRULE:FREQ=DAILY",
        "initialTokenCount": 10,
        "referenceTimestamp": "2021-07-14T10:00:00Z"
      },
      "conditionId": "string",
      "dateCreated": "2019-10-15T16:07:01.492Z",
      "description": "string",
      "errorStatus": "OK",
      "lastTrigger": "string",
      "lastUpdated": "2019-10-15T16:07:01.492Z",
      "triggerType": "RELOAD",
      "triggerStats": {
        "totalScans": 100,
        "last10Scans": 10,
        "last100Scans": 100
      },
      "hideSelections": true,
      "evaluationCount": 42,
      "scheduleOptions": {
        "timezone": "Canada/Pacific",
        "recurrence": [
          "RRULE:FREQ=HOURLY;INTERVAL=2"
        ],
        "endDateTime": "",
        "chronosJobID": "chronos-job-123",
        "startDateTime": "2006-01-02T16:04:05",
        "lastExecutionTime": "2020-11-20T12:00:55.000Z",
        "nextExecutionTime": "2020-11-20T12:00:55.000Z"
      },
      "subscriptionIds": [
        "string"
      ],
      "absoluteLastScan": "string",
      "conditionResponse": {},
      "alertingTaskErrors": [
        {
          "added": "2019-10-15T16:07:01.492Z",
          "value": "OWNER_DISABLED"
        }
      ],
      "absoluteLastTrigger": "string",
      "hasHistoryCondition": true,
      "lastExecutionStatus": "OK",
      "recipientsChangeHistory": [
        {
          "dateTime": "string",
          "patchAction": [
            {
              "op": "add",
              "value": {
                "value": "recipient-1",
                "enabled": true
              },
              "recipientType": "userid"
            },
            {
              "op": "remove",
              "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
              "recipientType": "userid"
            },
            {
              "op": "enable",
              "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
              "recipientType": "userid"
            },
            {
              "op": "disable",
              "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
              "recipientType": "userid"
            },
            {
              "op": "replace",
              "value": [
                {
                  "value": "recipient-1",
                  "enabled": true
                },
                {
                  "value": "recipient-2",
                  "enabled": false
                }
              ],
              "recipientType": "userid"
            }
          ]
        }
      ],
      "lastEvaluationCountUpdate": "string"
    }
  ]
}
```

---

### POST /api/v1/data-alerts

Creates a new data alerting task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The alerting task create request definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | name associated to alerting task |
| `appId` | string | Yes | appId associated to this alert definition |
| `enabled` | boolean | No | if the alerting task is enabled |
| `sheetId` | string | No | sheetId associated to this alert definition |
| `bookmarkId` | string | No | bookmarkId associated to this alert definition |
| `recipients` | object | Yes | List of recipients. An internal recipient is represented by either their user id or group id. |
| `throttling` | object | No | The rules and setup for throttling |
| `conditionId` | string | Yes | the id of the condition that determines if this data alert should be triggered |
| `description` | string | No | description associated to alerting task |
| `triggerType` | string | Yes | Type of job that triggered the task Enum: "RELOAD", "SCHEDULED" |
| `scheduleOptions` | object | No |  |

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | Yes | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `DLListId` | string | No | Identifier of the distribution list the recipients belong to. |
| `groupIds` | object[] | No | an internal recipient based on its group id. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `subscribed` | boolean | No | Whether this recipient is subscribed to alerts of a task |
| `taskRecipientErrors` | object[] | No |  |
| `alertingTaskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `groupIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Group ID of recipient. |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskGroupRecipientErrors` | object[] | No |  |
| `alertingTaskGroupRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `throttling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | integer | No | the maximum number of tokens that the bucket can contain |
| `timezone` | string | No | the timezone for time calculations in this throttlingresource, for current time and time reference. |
| `replenishRate` | integer | No | the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded) |
| `recurrenceRule` | string | No | A string that supports a subset of RFC5545 recurrence rule directives. |
| `initialTokenCount` | integer | No | the initial amount of tokens in the bucket upon creation. cannot exceed capacity. |
| `referenceTimestamp` | string | No | a date and time reference specified in RFC3339 format |

</details>

<details>
<summary>Properties of `scheduleOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | No | The timezone for time calculations in SCHEDULED triggers, optional. |
| `recurrence` | string[] | No | List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed. |
| `endDateTime` | string | No | EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending. |
| `startDateTime` | string | No | StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time. |

</details>

#### Responses

##### 202

Alert creation has been accepted. The alerting task will have status creating, until status is set to either valid or invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | data alerting identifier (this is the alertID) |
| `name` | string | No | name associated to alerting task |
| `appId` | string | No | appId associated to this alert definition |
| `links` | object | No |  |
| `status` | string | No | particular status of the alerting task Enum: "creating", "deleting" |
| `enabled` | boolean | No | true if the alerting task is enabled |
| `ownerId` | string | No | the owner of this alert |
| `sheetId` | string | No | sheetId associated to this alert definition |
| `lastScan` | string | No | last time a trigger was detected, but not sure if executed for requesting user |
| `tenantId` | string | No | the tenant of this alert |
| `ownerName` | string | No | the owner name of this alert |
| `accessMode` | string | No | Enum: "SOURCE_ACCESS", "TARGET_ACCESS" |
| `bookmarkId` | string | No | bookmarkId associated to this alert definition |
| `recipients` | object | No | List of recipients. An internal recipient is represented by either their user id or group id. |
| `throttling` | object | No | The rules and setup for throttling |
| `conditionId` | string | No | the id of the condition that determines if this data alert should be triggered |
| `dateCreated` | string | No | Timestamp for the creation of the task (rfc3339 format) |
| `description` | string | No | description associated to alerting task |
| `errorStatus` | string | No | error labels from the latest workflow that happened within the task Enum: "OK", "FATAL-ERROR", "PARTIAL-TRIGGER" |
| `lastTrigger` | string | No | last time an execution had been created for requesting user |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `triggerType` | string | No | Type of job that triggered the task Enum: "RELOAD", "SCHEDULED", "MANUAL" |
| `triggerStats` | object | Yes |  |
| `hideSelections` | boolean | No | Whether the selection needs to be hidden. |
| `evaluationCount` | integer | No | the number of actual evaluations with engine this task has consumed in the current month |
| `scheduleOptions` | object | No |  |
| `subscriptionIds` | string[] | No | list of subscriptions related to this alerting task |
| `absoluteLastScan` | string | No | last time a trigger was detected, but not sure if executed |
| `conditionResponse` | object | No | Should reference ConditionResponse type in condition-manager api docs |
| `alertingTaskErrors` | object[] | No |  |
| `absoluteLastTrigger` | string | No | last time an execution had been created |
| `hasHistoryCondition` | boolean | No | true if the alert has history condition enabled |
| `lastExecutionStatus` | string | No | Enum: "OK", "FAILED" |
| `recipientsChangeHistory` | object[] | No | Change in a recipient for an alerting task |
| `lastEvaluationCountUpdate` | string | No | the date when the evaluation count was updated |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | Yes | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `DLListId` | string | No | Identifier of the distribution list the recipients belong to. |
| `groupIds` | object[] | No | an internal recipient based on its group id. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `subscribed` | boolean | No | Whether this recipient is subscribed to alerts of a task |
| `taskRecipientErrors` | object[] | No |  |
| `alertingTaskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `groupIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Group ID of recipient. |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskGroupRecipientErrors` | object[] | No |  |
| `alertingTaskGroupRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `throttling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | integer | No | the maximum number of tokens that the bucket can contain |
| `timezone` | string | No | the timezone for time calculations in this throttlingresource, for current time and time reference. |
| `replenishRate` | integer | No | the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded) |
| `recurrenceRule` | string | No | A string that supports a subset of RFC5545 recurrence rule directives. |
| `initialTokenCount` | integer | No | the initial amount of tokens in the bucket upon creation. cannot exceed capacity. |
| `referenceTimestamp` | string | No | a date and time reference specified in RFC3339 format |

</details>

<details>
<summary>Properties of `triggerStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalScans` | integer | Yes | The number of scans for the current condition. |
| `last10Scans` | integer | Yes | The number of triggers out of the last 10 scans for the current condition. |
| `last100Scans` | integer | Yes | The number of triggers out of the last 100 scans for the current condition. |

</details>

<details>
<summary>Properties of `scheduleOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | No | The timezone for time calculations in SCHEDULED triggers, optional. |
| `recurrence` | string[] | No | List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed. |
| `endDateTime` | string | No | EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending. |
| `chronosJobID` | string | No | The chronos job identifier. It is set once the related chronos job is created. |
| `startDateTime` | string | No | StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time. |
| `lastExecutionTime` | string | No | lastExecutionTime is the time of the chronos job last execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if job has not run yet. |
| `nextExecutionTime` | string | No | nextExecutionTime is the time of the chronos job next execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if the job is completed. |

</details>

<details>
<summary>Properties of `alertingTaskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `added` | string | No | Timestamp for the creation of the error |
| `value` | string | No | Identifier for type of error occurring on alerting task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "EVAL_ERROR", "ORPHAN", "CONVERSION_DENIED", "EXPIRED", "PARTIAL_SENT", "QUOTA_REACHED", "OWNER_HAS_NO_VALID_USER_ENTITLEMENT" |

</details>

<details>
<summary>Properties of `recipientsChangeHistory`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dateTime` | string | No | time of recipient state change |
| `patchAction` | object[] | No | A custom custom JSON Patch document, as an array of objects with operation, recipient type and value. Original defined in https://datatracker.ietf.org/doc/html/rfc6902. |

<details>
<summary>Properties of `patchAction`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "remove", "add", "replace", "enable", "disable", "subscribe", "unsubscribe" |
| `value` | object | Yes | The value to be used for this operation. |
| `recipientType` | string | Yes | Defines the path for the given resource field to patch. Enum: "userid", "groupid" |

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-alerts` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Sales threshold alert',
      appId:
        'e0e3187e-4f8c-4c1f-9d2a-1234567890ab',
      enabled: true,
      sheetId: 'abcABC1',
      bookmarkId: 'def-456',
      recipients: {
        DLUsers: [],
        userIds: [
          {
            value: '1b263bs8m0mm_s21s3f',
            groups: [
              'addedIndividually',
              'group1',
              'group2',
            ],
            enabled: true,
            subscribed: true,
            taskRecipientErrors: [
              {
                value: 'NO_ACCESS_TO_APP',
                timestamp:
                  '2019-10-15T16:07:01.492Z',
              },
            ],
            alertingTaskRecipientErrors: [
              {
                added: '2019-10-15T16:07:01.492Z',
                value: 'NO_ACCESS_TO_APP',
              },
            ],
          },
        ],
        DLGroups: [],
        DLListId: 'dl-12345',
        groupIds: [
          {
            value: 'group1',
            enabled: true,
            taskGroupRecipientErrors: [
              {
                value: 'GROUP_WITH_NO_APP_ACCESS',
                timestamp:
                  '2019-10-15T16:07:01.492Z',
              },
            ],
            alertingTaskGroupRecipientErrors: [
              {
                added: '2019-10-15T16:07:01.492Z',
                value: 'GROUP_WITH_NO_APP_ACCESS',
              },
            ],
          },
        ],
      },
      throttling: {
        capacity: 10,
        timezone: 'Etc/UTC',
        replenishRate: 1,
        recurrenceRule: 'RRULE:FREQ=DAILY',
        initialTokenCount: 10,
        referenceTimestamp:
          '2021-07-14T10:00:00Z',
      },
      conditionId: 'cond-789',
      description:
        'Notifies when sales drop below target.',
      triggerType: 'SCHEDULED',
      scheduleOptions: {
        timezone: 'Canada/Pacific',
        recurrence: [
          'RRULE:FREQ=HOURLY;INTERVAL=2',
        ],
        endDateTime: '',
        startDateTime: '2006-01-02T16:04:05',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-alerts yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Sales threshold alert","appId":"e0e3187e-4f8c-4c1f-9d2a-1234567890ab","enabled":true,"sheetId":"abcABC1","bookmarkId":"def-456","recipients":{"DLUsers":[],"userIds":[{"value":"1b263bs8m0mm_s21s3f","groups":["addedIndividually","group1","group2"],"enabled":true,"subscribed":true,"taskRecipientErrors":[{"value":"NO_ACCESS_TO_APP","timestamp":"2019-10-15T16:07:01.492Z"}],"alertingTaskRecipientErrors":[{"added":"2019-10-15T16:07:01.492Z","value":"NO_ACCESS_TO_APP"}]}],"DLGroups":[],"DLListId":"dl-12345","groupIds":[{"value":"group1","enabled":true,"taskGroupRecipientErrors":[{"value":"GROUP_WITH_NO_APP_ACCESS","timestamp":"2019-10-15T16:07:01.492Z"}],"alertingTaskGroupRecipientErrors":[{"added":"2019-10-15T16:07:01.492Z","value":"GROUP_WITH_NO_APP_ACCESS"}]}]},"throttling":{"capacity":10,"timezone":"Etc/UTC","replenishRate":1,"recurrenceRule":"RRULE:FREQ=DAILY","initialTokenCount":10,"referenceTimestamp":"2021-07-14T10:00:00Z"},"conditionId":"cond-789","description":"Notifies when sales drop below target.","triggerType":"SCHEDULED","scheduleOptions":{"timezone":"Canada/Pacific","recurrence":["RRULE:FREQ=HOURLY;INTERVAL=2"],"endDateTime":"","startDateTime":"2006-01-02T16:04:05"}}'
```

**Example Response:**

```json
{
  "id": "5da5825325dc9a0dd0260af9",
  "name": "string",
  "appId": "string",
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "status": "creating",
  "enabled": true,
  "ownerId": "string",
  "sheetId": "string",
  "lastScan": "string",
  "tenantId": "string",
  "ownerName": "string",
  "accessMode": "SOURCE_ACCESS",
  "bookmarkId": "string",
  "recipients": {
    "DLUsers": [],
    "userIds": [
      {
        "value": "1b263bs8m0mm_s21s3f",
        "groups": [
          "addedIndividually",
          "group1",
          "group2"
        ],
        "enabled": true,
        "subscribed": true,
        "taskRecipientErrors": [
          {
            "value": "NO_ACCESS_TO_APP",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ],
        "alertingTaskRecipientErrors": [
          {
            "added": "2019-10-15T16:07:01.492Z",
            "value": "NO_ACCESS_TO_APP"
          }
        ]
      }
    ],
    "DLGroups": [],
    "DLListId": "dl-12345",
    "groupIds": [
      {
        "value": "group1",
        "enabled": true,
        "taskGroupRecipientErrors": [
          {
            "value": "GROUP_WITH_NO_APP_ACCESS",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ],
        "alertingTaskGroupRecipientErrors": [
          {
            "added": "2019-10-15T16:07:01.492Z",
            "value": "GROUP_WITH_NO_APP_ACCESS"
          }
        ]
      }
    ]
  },
  "throttling": {
    "capacity": 10,
    "timezone": "Etc/UTC",
    "replenishRate": 1,
    "recurrenceRule": "RRULE:FREQ=DAILY",
    "initialTokenCount": 10,
    "referenceTimestamp": "2021-07-14T10:00:00Z"
  },
  "conditionId": "string",
  "dateCreated": "2019-10-15T16:07:01.492Z",
  "description": "string",
  "errorStatus": "OK",
  "lastTrigger": "string",
  "lastUpdated": "2019-10-15T16:07:01.492Z",
  "triggerType": "RELOAD",
  "triggerStats": {
    "totalScans": 100,
    "last10Scans": 10,
    "last100Scans": 100
  },
  "hideSelections": true,
  "evaluationCount": 42,
  "scheduleOptions": {
    "timezone": "Canada/Pacific",
    "recurrence": [
      "RRULE:FREQ=HOURLY;INTERVAL=2"
    ],
    "endDateTime": "",
    "chronosJobID": "chronos-job-123",
    "startDateTime": "2006-01-02T16:04:05",
    "lastExecutionTime": "2020-11-20T12:00:55.000Z",
    "nextExecutionTime": "2020-11-20T12:00:55.000Z"
  },
  "subscriptionIds": [
    "string"
  ],
  "absoluteLastScan": "string",
  "conditionResponse": {},
  "alertingTaskErrors": [
    {
      "added": "2019-10-15T16:07:01.492Z",
      "value": "OWNER_DISABLED"
    }
  ],
  "absoluteLastTrigger": "string",
  "hasHistoryCondition": true,
  "lastExecutionStatus": "OK",
  "recipientsChangeHistory": [
    {
      "dateTime": "string",
      "patchAction": [
        {
          "op": "add",
          "value": {
            "value": "recipient-1",
            "enabled": true
          },
          "recipientType": "userid"
        },
        {
          "op": "remove",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "enable",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "disable",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "replace",
          "value": [
            {
              "value": "recipient-1",
              "enabled": true
            },
            {
              "value": "recipient-2",
              "enabled": false
            }
          ],
          "recipientType": "userid"
        }
      ]
    }
  ],
  "lastEvaluationCountUpdate": "string"
}
```

---

### GET /api/v1/data-alerts/{alertId}

Returns the details of a specific data alert task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |

#### Responses

##### 200

Alert has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | data alerting identifier (this is the alertID) |
| `name` | string | No | name associated to alerting task |
| `appId` | string | No | appId associated to this alert definition |
| `links` | object | No |  |
| `status` | string | No | particular status of the alerting task Enum: "creating", "deleting" |
| `enabled` | boolean | No | true if the alerting task is enabled |
| `ownerId` | string | No | the owner of this alert |
| `sheetId` | string | No | sheetId associated to this alert definition |
| `lastScan` | string | No | last time a trigger was detected, but not sure if executed for requesting user |
| `tenantId` | string | No | the tenant of this alert |
| `ownerName` | string | No | the owner name of this alert |
| `accessMode` | string | No | Enum: "SOURCE_ACCESS", "TARGET_ACCESS" |
| `bookmarkId` | string | No | bookmarkId associated to this alert definition |
| `recipients` | object | No | List of recipients. An internal recipient is represented by either their user id or group id. |
| `throttling` | object | No | The rules and setup for throttling |
| `conditionId` | string | No | the id of the condition that determines if this data alert should be triggered |
| `dateCreated` | string | No | Timestamp for the creation of the task (rfc3339 format) |
| `description` | string | No | description associated to alerting task |
| `errorStatus` | string | No | error labels from the latest workflow that happened within the task Enum: "OK", "FATAL-ERROR", "PARTIAL-TRIGGER" |
| `lastTrigger` | string | No | last time an execution had been created for requesting user |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `triggerType` | string | No | Type of job that triggered the task Enum: "RELOAD", "SCHEDULED", "MANUAL" |
| `triggerStats` | object | Yes |  |
| `hideSelections` | boolean | No | Whether the selection needs to be hidden. |
| `evaluationCount` | integer | No | the number of actual evaluations with engine this task has consumed in the current month |
| `scheduleOptions` | object | No |  |
| `subscriptionIds` | string[] | No | list of subscriptions related to this alerting task |
| `absoluteLastScan` | string | No | last time a trigger was detected, but not sure if executed |
| `conditionResponse` | object | No | Should reference ConditionResponse type in condition-manager api docs |
| `alertingTaskErrors` | object[] | No |  |
| `absoluteLastTrigger` | string | No | last time an execution had been created |
| `hasHistoryCondition` | boolean | No | true if the alert has history condition enabled |
| `lastExecutionStatus` | string | No | Enum: "OK", "FAILED" |
| `recipientsChangeHistory` | object[] | No | Change in a recipient for an alerting task |
| `lastEvaluationCountUpdate` | string | No | the date when the evaluation count was updated |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | Yes | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `DLListId` | string | No | Identifier of the distribution list the recipients belong to. |
| `groupIds` | object[] | No | an internal recipient based on its group id. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `subscribed` | boolean | No | Whether this recipient is subscribed to alerts of a task |
| `taskRecipientErrors` | object[] | No |  |
| `alertingTaskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `groupIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Group ID of recipient. |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskGroupRecipientErrors` | object[] | No |  |
| `alertingTaskGroupRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `throttling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | integer | No | the maximum number of tokens that the bucket can contain |
| `timezone` | string | No | the timezone for time calculations in this throttlingresource, for current time and time reference. |
| `replenishRate` | integer | No | the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded) |
| `recurrenceRule` | string | No | A string that supports a subset of RFC5545 recurrence rule directives. |
| `initialTokenCount` | integer | No | the initial amount of tokens in the bucket upon creation. cannot exceed capacity. |
| `referenceTimestamp` | string | No | a date and time reference specified in RFC3339 format |

</details>

<details>
<summary>Properties of `triggerStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalScans` | integer | Yes | The number of scans for the current condition. |
| `last10Scans` | integer | Yes | The number of triggers out of the last 10 scans for the current condition. |
| `last100Scans` | integer | Yes | The number of triggers out of the last 100 scans for the current condition. |

</details>

<details>
<summary>Properties of `scheduleOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | No | The timezone for time calculations in SCHEDULED triggers, optional. |
| `recurrence` | string[] | No | List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed. |
| `endDateTime` | string | No | EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending. |
| `chronosJobID` | string | No | The chronos job identifier. It is set once the related chronos job is created. |
| `startDateTime` | string | No | StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time. |
| `lastExecutionTime` | string | No | lastExecutionTime is the time of the chronos job last execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if job has not run yet. |
| `nextExecutionTime` | string | No | nextExecutionTime is the time of the chronos job next execution in RFC3339 format (a time with a fixed UTC offset). Could be empty if the job is completed. |

</details>

<details>
<summary>Properties of `alertingTaskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `added` | string | No | Timestamp for the creation of the error |
| `value` | string | No | Identifier for type of error occurring on alerting task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "EVAL_ERROR", "ORPHAN", "CONVERSION_DENIED", "EXPIRED", "PARTIAL_SENT", "QUOTA_REACHED", "OWNER_HAS_NO_VALID_USER_ENTITLEMENT" |

</details>

<details>
<summary>Properties of `recipientsChangeHistory`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dateTime` | string | No | time of recipient state change |
| `patchAction` | object[] | No | A custom custom JSON Patch document, as an array of objects with operation, recipient type and value. Original defined in https://datatracker.ietf.org/doc/html/rfc6902. |

<details>
<summary>Properties of `patchAction`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "remove", "add", "replace", "enable", "disable", "subscribe", "unsubscribe" |
| `value` | object | Yes | The value to be used for this operation. |
| `recipientType` | string | Yes | Defines the path for the given resource field to patch. Enum: "userid", "groupid" |

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or execution not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{alertId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{alertId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "5da5825325dc9a0dd0260af9",
  "name": "string",
  "appId": "string",
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "status": "creating",
  "enabled": true,
  "ownerId": "string",
  "sheetId": "string",
  "lastScan": "string",
  "tenantId": "string",
  "ownerName": "string",
  "accessMode": "SOURCE_ACCESS",
  "bookmarkId": "string",
  "recipients": {
    "DLUsers": [],
    "userIds": [
      {
        "value": "1b263bs8m0mm_s21s3f",
        "groups": [
          "addedIndividually",
          "group1",
          "group2"
        ],
        "enabled": true,
        "subscribed": true,
        "taskRecipientErrors": [
          {
            "value": "NO_ACCESS_TO_APP",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ],
        "alertingTaskRecipientErrors": [
          {
            "added": "2019-10-15T16:07:01.492Z",
            "value": "NO_ACCESS_TO_APP"
          }
        ]
      }
    ],
    "DLGroups": [],
    "DLListId": "dl-12345",
    "groupIds": [
      {
        "value": "group1",
        "enabled": true,
        "taskGroupRecipientErrors": [
          {
            "value": "GROUP_WITH_NO_APP_ACCESS",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ],
        "alertingTaskGroupRecipientErrors": [
          {
            "added": "2019-10-15T16:07:01.492Z",
            "value": "GROUP_WITH_NO_APP_ACCESS"
          }
        ]
      }
    ]
  },
  "throttling": {
    "capacity": 10,
    "timezone": "Etc/UTC",
    "replenishRate": 1,
    "recurrenceRule": "RRULE:FREQ=DAILY",
    "initialTokenCount": 10,
    "referenceTimestamp": "2021-07-14T10:00:00Z"
  },
  "conditionId": "string",
  "dateCreated": "2019-10-15T16:07:01.492Z",
  "description": "string",
  "errorStatus": "OK",
  "lastTrigger": "string",
  "lastUpdated": "2019-10-15T16:07:01.492Z",
  "triggerType": "RELOAD",
  "triggerStats": {
    "totalScans": 100,
    "last10Scans": 10,
    "last100Scans": 100
  },
  "hideSelections": true,
  "evaluationCount": 42,
  "scheduleOptions": {
    "timezone": "Canada/Pacific",
    "recurrence": [
      "RRULE:FREQ=HOURLY;INTERVAL=2"
    ],
    "endDateTime": "",
    "chronosJobID": "chronos-job-123",
    "startDateTime": "2006-01-02T16:04:05",
    "lastExecutionTime": "2020-11-20T12:00:55.000Z",
    "nextExecutionTime": "2020-11-20T12:00:55.000Z"
  },
  "subscriptionIds": [
    "string"
  ],
  "absoluteLastScan": "string",
  "conditionResponse": {},
  "alertingTaskErrors": [
    {
      "added": "2019-10-15T16:07:01.492Z",
      "value": "OWNER_DISABLED"
    }
  ],
  "absoluteLastTrigger": "string",
  "hasHistoryCondition": true,
  "lastExecutionStatus": "OK",
  "recipientsChangeHistory": [
    {
      "dateTime": "string",
      "patchAction": [
        {
          "op": "add",
          "value": {
            "value": "recipient-1",
            "enabled": true
          },
          "recipientType": "userid"
        },
        {
          "op": "remove",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "enable",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "disable",
          "value": "I6mWVd60wRWIbOXZr1ZKV8QTnxhnitb",
          "recipientType": "userid"
        },
        {
          "op": "replace",
          "value": [
            {
              "value": "recipient-1",
              "enabled": true
            },
            {
              "value": "recipient-2",
              "enabled": false
            }
          ],
          "recipientType": "userid"
        }
      ]
    }
  ],
  "lastEvaluationCountUpdate": "string"
}
```

---

### PATCH /api/v1/data-alerts/{alertId}

Updates one or more properties of a specific data alerting task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |

#### Request Body

**Required**

Patch request definition for an alerting task.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed Enum: "replace" |
| `path` | string | Yes | A JSON Patch document as defined in https://datatracker.ietf.org/doc/html/rfc6902 Enum: "/ownerName", "/ownerId", "/conditionId", "/enabledAction", "/bookmarkId", "/name", "/description", "/throttling", "/triggerType", "/scheduleOptions" |
| `value` | object | No | The value to be used for this operation. |

#### Responses

##### 204

The alerting task has been successfully updated.

##### 400

The specified alerting task ID or body is invalid (e.g. not a number).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

An alerting task with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/data-alerts/{alertId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/ownerName',
        value: {},
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/data-alerts/{alertId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/ownerName","value":{}}]'
```

---

### DELETE /api/v1/data-alerts/{alertId}

Deletes a specific data alerting task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |

#### Responses

##### 204

The alerting task has been successfully deleted.

##### 400

The specified alerting task ID is invalid (e.g. not a number).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

An alerting task with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-alerts/{alertId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-alerts/{alertId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/data-alerts/{alertId}/condition

Retrieves the condition associated with a data alerting task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |

#### Responses

##### 200

Condition associated with the alerting task has been successfully returned. See ConditionResponse in condition-manager api docs

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hideSelections` | boolean | No |  |
| `conditionResponse` | object | No | Should reference ConditionResponse type in condition-manager api docs |

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or condition not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{alertId}/condition` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}/condition',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{alertId}/condition yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}/condition" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "hideSelections": true,
  "conditionResponse": {}
}
```

---

### GET /api/v1/data-alerts/{alertId}/executions/{executionId}

Retrieves a specific execution for the specified data alerting task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |
| `executionId` | string | Yes | The execution identifier. If value is "latest", the latest execution will be returned |

#### Responses

##### 200

The execution has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the execution identifier. |
| `errors` | object[] | No |  |
| `result` | object | No |  |
| `alertId` | string | No | ID for the alerting task that this execution references |
| `ownerId` | string | No | The owner that this execution belongs to |
| `measures` | string[] | No | Measures applied in the condition |
| `tenantId` | string | No | The tenant that this execution belongs to |
| `accessMode` | string | No | Enum: "SOURCE_ACCESS", "TARGET_ACCESS" |
| `bookmarkId` | string | No | Id of the bookmark associated with an alert |
| `dimensions` | string[] | No | Dimensions applied in the condition |
| `workflowId` | string | No | ID for the workflow, coming from eventing service |
| `conditionId` | string | No | Id of the condition the alert is associated with |
| `triggerTime` | string | No | Timestamp of execution start |
| `evaluationId` | string | No | Id of the evaluation for the condition |
| `executionType` | string | No | Enum: "INDIVIDUAL", "SHARED" |
| `conditionStatus` | string | No | Enum: "FINISHED", "FAILED" |
| `executionEvaluationStatus` | string | No | Enum: "CONDITION_MET", "CONDITION_NOT_MET", "FAILED" |
| `links` | object | No |  |
| `evaluation` | object | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertTriggerStatus` | string | No |  |
| `throttlerTokensLeft` | integer | No |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `evaluation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `result` | string | No | The final result of the evalution Enum: "success", "failure", "error" |
| `status` | string | No | The status of the evaluation execution Enum: "RUNNING", "FAILED", "FINISHED" |
| `endTime` | string | No | The time the evaluation ended |
| `ownerId` | string | No | userId of user being impersonated to evaluate the condition |
| `tenantId` | string | No | The tenant id |
| `contextId` | string | No | Extra context information to carry through to the result if one was included on when the evaluation was triggered |
| `startTime` | string | No | The time the evaluation started |
| `resultData` | object | No | Condition type specific result, one of dataResult or compoundResult |
| `causalEvent` | object | No | Representation of the event that caused the condition to be evaluated if one was included on when the evaluation was triggered |
| `conditionId` | string | No | The unique id of the associated condition |
| `dataConditionEvaluatorId` | string | No | The unique id for the resource given from Data Condition Evaluator |

</details>

##### 400

The specified task or execution ID is invalid (e.g. not a number).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or execution not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{alertId}/executions/{executionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}/executions/{executionId}',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{alertId}/executions/{executionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}/executions/{executionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "errors": [
    {
      "code": "string",
      "title": "string",
      "detail": "string"
    }
  ],
  "result": {
    "alertTriggerStatus": "alertSent",
    "throttlerTokensLeft": 5
  },
  "alertId": "string",
  "ownerId": "string",
  "measures": [
    "string"
  ],
  "tenantId": "string",
  "accessMode": "SOURCE_ACCESS",
  "bookmarkId": "string",
  "dimensions": [
    "string"
  ],
  "workflowId": "string",
  "conditionId": "string",
  "triggerTime": "string",
  "evaluationId": "string",
  "executionType": "INDIVIDUAL",
  "conditionStatus": "FINISHED",
  "executionEvaluationStatus": "CONDITION_MET",
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "evaluation": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "result": "success",
    "status": "RUNNING",
    "endTime": "string",
    "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "contextId": "string",
    "startTime": "string",
    "resultData": {},
    "causalEvent": {},
    "conditionId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "dataConditionEvaluatorId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
  }
}
```

---

### DELETE /api/v1/data-alerts/{alertId}/executions/{executionId}

Deletes a specific data alerting task execution.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |
| `executionId` | string | Yes | The execution identifier. |

#### Responses

##### 204

The execution has been successfully deleted.

##### 400

The specified task or execution ID is invalid (e.g. not a number).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or execution not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-alerts/{alertId}/executions/{executionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}/executions/{executionId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-alerts/{alertId}/executions/{executionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}/executions/{executionId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/data-alerts/{alertId}/recipient-stats

Retrieve the recipient stats for a data alerting task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | string | Yes | The alerting task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `groups` | string[] | No | The name of the groups you would like to filter by |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "+userID", "-userID", "subscribed", "+subscribed" |
| `subscribed` | boolean | No | Subscribed property you would like to filter by |
| `userID` | string | No | The recipients ID you would like to filter by |

#### Responses

##### 200

Alert recipient stats have been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recipientStats` | object[] | No |  |

<details>
<summary>Properties of `recipientStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "userid" |
| `value` | string | No |  |
| `errors` | object[] | No |  |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `enabled` | boolean | Yes | Whether the recipient is enabled. |
| `lastScan` | string | No | last time a trigger was detected, but not sure if executed |
| `subscribed` | boolean | No | Whether the recipient is subscribed. |
| `lastTrigger` | string | No | last time an execution had been created |
| `conditionStatus` | string | No | Enum: "OK", "FAILED" |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or execution not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{alertId}/recipient-stats` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{alertId}/recipient-stats',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{alertId}/recipient-stats yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{alertId}/recipient-stats" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "recipientStats": [
    {
      "type": "userid",
      "value": "string",
      "errors": [
        {
          "code": "string",
          "title": "string",
          "detail": "string"
        }
      ],
      "groups": [
        "addedIndividually",
        "group1",
        "group2"
      ],
      "enabled": true,
      "lastScan": "string",
      "subscribed": true,
      "lastTrigger": "string",
      "conditionStatus": "OK"
    }
  ]
}
```

---

### GET /api/v1/data-alerts/{taskId}/executions

Lists executions for the specified data alerting task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The alerting task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `conditionId` | string | No | Filter by condition id related to the executions. |
| `conditionStatus` | string | No | Filter by whether the alerting task execution status is FINISHED or FAILED. Enum: "FINISHED", "FAILED", "ALL" |
| `daysOfMonth` | integer[] | No | Specifies required days of the month that the execution was created in |
| `daysOfWeek` | string[] | No | Specifies a filter for custom handled periods of time in which the executions were handled Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY" |
| `fields` | string[] | No | Specifies specific properties to be populated Enum: "evaluationId", "triggerTime", "conditionStatus", "executionEvaluationStatus", "evaluation", "evaluation.endTime", "evaluation.resultData", "evaluation.resultData.count", "evaluation.resultData.headers", "evaluation.resultData.positive", "evaluation.resultData.negative", "evaluation.resultData.dimensions", "evaluation.resultData.measures" |
| `includeEvaluation` | boolean | No | Specifies whether to include evaluation details |
| `lastEachDay` | boolean | No | Specifies whether to only show the last execution in each day |
| `limit` | integer | No | Limit the returned result set |
| `minimumGapDays` | integer | No | Specifies the number of days required between each entry. This should require a sort by triggertime |
| `next` | string | No | The cursor to the next page of data. Only one of next or previous may be specified. |
| `offset` | integer | No | Offset for pagination - how many elements to skip |
| `prev` | string | No | The cursor to the previous page of data. Only one of next or previous may be specified. |
| `searchResultsLimit` | integer | No | Specifies a limit number for the search query, affects total count and is not related to pagination |
| `since` | string | No | Specifies a date that executions should have been created after. Date in RFC3339Nano format, such as 2020-01-01T00:00:00.000Z |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "triggertime", "-triggertime", "+triggertime" |
| `timezone` | string | No | Specifies a timezone the other time-based filters in this query should consider. Expecting a momentjs format, such as America/Los_Angeles |
| `triggered` | boolean | No | Filter by whether the alerting task is triggered. |
| `until` | string | No | Specifies a date that executions should have been created before. Date in RFC3339Nano format, such as 2020-01-01T00:00:00.000Z |

#### Responses

##### 200

The alerting-executions list has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `links` | object | No |  |
| `executions` | object[] | No | Gets a list of alerting-executions. |

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

<details>
<summary>Properties of `executions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the execution identifier. |
| `errors` | object[] | No |  |
| `result` | object | No |  |
| `alertId` | string | No | ID for the alerting task that this execution references |
| `ownerId` | string | No | The owner that this execution belongs to |
| `measures` | string[] | No | Measures applied in the condition |
| `tenantId` | string | No | The tenant that this execution belongs to |
| `accessMode` | string | No | Enum: "SOURCE_ACCESS", "TARGET_ACCESS" |
| `bookmarkId` | string | No | Id of the bookmark associated with an alert |
| `dimensions` | string[] | No | Dimensions applied in the condition |
| `workflowId` | string | No | ID for the workflow, coming from eventing service |
| `conditionId` | string | No | Id of the condition the alert is associated with |
| `triggerTime` | string | No | Timestamp of execution start |
| `evaluationId` | string | No | Id of the evaluation for the condition |
| `executionType` | string | No | Enum: "INDIVIDUAL", "SHARED" |
| `conditionStatus` | string | No | Enum: "FINISHED", "FAILED" |
| `executionEvaluationStatus` | string | No | Enum: "CONDITION_MET", "CONDITION_NOT_MET", "FAILED" |
| `links` | object | No |  |
| `evaluation` | object | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertTriggerStatus` | string | No |  |
| `throttlerTokensLeft` | integer | No |  |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `evaluation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `result` | string | No | The final result of the evalution Enum: "success", "failure", "error" |
| `status` | string | No | The status of the evaluation execution Enum: "RUNNING", "FAILED", "FINISHED" |
| `endTime` | string | No | The time the evaluation ended |
| `ownerId` | string | No | userId of user being impersonated to evaluate the condition |
| `tenantId` | string | No | The tenant id |
| `contextId` | string | No | Extra context information to carry through to the result if one was included on when the evaluation was triggered |
| `startTime` | string | No | The time the evaluation started |
| `resultData` | object | No | Condition type specific result, one of dataResult or compoundResult |
| `causalEvent` | object | No | Representation of the event that caused the condition to be evaluated if one was included on when the evaluation was triggered |
| `conditionId` | string | No | The unique id of the associated condition |
| `dataConditionEvaluatorId` | string | No | The unique id for the resource given from Data Condition Evaluator |

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Task or execution not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{taskId}/executions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{taskId}/executions',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{taskId}/executions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{taskId}/executions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 42,
  "currentPageCount": 42,
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
  "executions": [
    {
      "id": "string",
      "errors": [
        {
          "code": "string",
          "title": "string",
          "detail": "string"
        }
      ],
      "result": {
        "alertTriggerStatus": "alertSent",
        "throttlerTokensLeft": 5
      },
      "alertId": "string",
      "ownerId": "string",
      "measures": [
        "string"
      ],
      "tenantId": "string",
      "accessMode": "SOURCE_ACCESS",
      "bookmarkId": "string",
      "dimensions": [
        "string"
      ],
      "workflowId": "string",
      "conditionId": "string",
      "triggerTime": "string",
      "evaluationId": "string",
      "executionType": "INDIVIDUAL",
      "conditionStatus": "FINISHED",
      "executionEvaluationStatus": "CONDITION_MET",
      "links": {
        "self": {
          "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
        }
      },
      "evaluation": {
        "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
        "result": "success",
        "status": "RUNNING",
        "endTime": "string",
        "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
        "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
        "contextId": "string",
        "startTime": "string",
        "resultData": {},
        "causalEvent": {},
        "conditionId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
        "dataConditionEvaluatorId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
      }
    }
  ]
}
```

---

### GET /api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations

Retrieves the content of an evaluation for a specified data alerting task execution.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `executionId` | string | Yes | The execution identifier. |
| `taskId` | string | Yes | The alerting task identifier. |

#### Responses

##### 200

Evaluation successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `condition` | object | No |  |
| `evaluation` | object | No |  |
| `hideSelections` | boolean | No |  |

<details>
<summary>Properties of `evaluation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The unique id for the resource |
| `result` | string | No | The final result of the evalution Enum: "success", "failure", "error" |
| `status` | string | No | The status of the evaluation execution Enum: "RUNNING", "FAILED", "FINISHED" |
| `endTime` | string | No | The time the evaluation ended |
| `ownerId` | string | No | userId of user being impersonated to evaluate the condition |
| `tenantId` | string | No | The tenant id |
| `contextId` | string | No | Extra context information to carry through to the result if one was included on when the evaluation was triggered |
| `startTime` | string | No | The time the evaluation started |
| `resultData` | object | No | Condition type specific result, one of dataResult or compoundResult |
| `causalEvent` | object | No | Representation of the event that caused the condition to be evaluated if one was included on when the evaluation was triggered |
| `conditionId` | string | No | The unique id of the associated condition |
| `dataConditionEvaluatorId` | string | No | The unique id for the resource given from Data Condition Evaluator |

</details>

##### 404

A task or execution with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{taskId}/executions/{executionId}/evaluations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "condition": {},
  "evaluation": {
    "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "result": "success",
    "status": "RUNNING",
    "endTime": "string",
    "ownerId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "contextId": "string",
    "startTime": "string",
    "resultData": {},
    "causalEvent": {},
    "conditionId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
    "dataConditionEvaluatorId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69"
  },
  "hideSelections": true
}
```

---

### GET /api/v1/data-alerts/{taskId}/executions/stats _(deprecated)_

Retrieves stats for overall data alerting task executions.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The alerting task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `period` | string | Yes | The period by which the stats aggregation needs to be performed. Enum: "month" |

#### Responses

##### 200

Evaluation successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `links` | object | No |  |
| `executionsStats` | object[] | No |  |

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

<details>
<summary>Properties of `executionsStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | string | No |  |
| `periodKey` | string | No |  |
| `startTime` | string | No |  |
| `totalExecutions` | string | No |  |
| `triggeredExecutions` | string | No |  |

</details>

##### 404

A task or execution with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/{taskId}/executions/stats` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/{taskId}/executions/stats',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/{taskId}/executions/stats yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/{taskId}/executions/stats" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 42,
  "currentPageCount": 42,
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
  "executionsStats": [
    {
      "endTime": "string",
      "periodKey": "string",
      "startTime": "string",
      "totalExecutions": "string",
      "triggeredExecutions": "string"
    }
  ]
}
```

---

### POST /api/v1/data-alerts/actions/trigger

Creates a new data alerting task trigger action.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The alerting trigger action create request definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertingTaskID` | string | Yes | Identifier of the alerting task to trigger. |

#### Responses

##### 202

Action has been successfully done. Request to eventing was successfully triggered.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `workflowID` | string | No | the workflow id created for the manual triggering of alert |

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-alerts/actions/trigger` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/actions/trigger',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      alertingTaskID: 'a1b2c3d4f5',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-alerts/actions/trigger yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/actions/trigger" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"alertingTaskID":"a1b2c3d4f5"}'
```

**Example Response:**

```json
{
  "workflowID": "a1b2c3d4f5"
}
```

---

### POST /api/v1/data-alerts/actions/validate

Validates a new data alerting task. Current support includes validation for recipients only.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The alerting validate action validates a new alerting task.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | name associated to alerting task |
| `appId` | string | Yes | appId associated to this alert definition |
| `enabled` | boolean | No | if the alerting task is enabled |
| `sheetId` | string | No | sheetId associated to this alert definition |
| `bookmarkId` | string | No | bookmarkId associated to this alert definition |
| `recipients` | object | Yes | List of recipients. An internal recipient is represented by either their user id or group id. |
| `throttling` | object | No | The rules and setup for throttling |
| `conditionId` | string | Yes | the id of the condition that determines if this data alert should be triggered |
| `description` | string | No | description associated to alerting task |
| `triggerType` | string | Yes | Type of job that triggered the task Enum: "RELOAD", "SCHEDULED" |
| `scheduleOptions` | object | No |  |

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | Yes | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `DLListId` | string | No | Identifier of the distribution list the recipients belong to. |
| `groupIds` | object[] | No | an internal recipient based on its group id. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `subscribed` | boolean | No | Whether this recipient is subscribed to alerts of a task |
| `taskRecipientErrors` | object[] | No |  |
| `alertingTaskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `groupIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Group ID of recipient. |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskGroupRecipientErrors` | object[] | No |  |
| `alertingTaskGroupRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskGroupRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `throttling`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | integer | No | the maximum number of tokens that the bucket can contain |
| `timezone` | string | No | the timezone for time calculations in this throttlingresource, for current time and time reference. |
| `replenishRate` | integer | No | the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded) |
| `recurrenceRule` | string | No | A string that supports a subset of RFC5545 recurrence rule directives. |
| `initialTokenCount` | integer | No | the initial amount of tokens in the bucket upon creation. cannot exceed capacity. |
| `referenceTimestamp` | string | No | a date and time reference specified in RFC3339 format |

</details>

<details>
<summary>Properties of `scheduleOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `timezone` | string | No | The timezone for time calculations in SCHEDULED triggers, optional. |
| `recurrence` | string[] | No | List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed. |
| `endDateTime` | string | No | EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending. |
| `startDateTime` | string | No | StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time. |

</details>

#### Responses

##### 200

Alerting task has been validated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Enum: "FAILURE", "SUCCESS" |
| `validations` | object[] | No |  |

<details>
<summary>Properties of `validations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Identifies for user id or condition id |
| `type` | string | No | Identifier for type of a validation error occurring on alerting task Enum: "RECIPIENT", "CONDITION", "RECIPIENT_GROUP" |
| `error` | string | No | _(deprecated)_ Identifier for a validation error occurring on alerting task Enum: "NO_ACCESS", "USER_IS_DISABLED", "INVALID_CONDITION", "GROUP_IS_DISABLED", "GROUP_SIZE_EXCEEDED" |
| `description` | string | No | Description of the error |
| `validationErrors` | string[] | No | Enum: "NO_ACCESS", "USER_IS_DISABLED", "INVALID_CONDITION", "MAX_ALERTS_LIMIT_REACHED", "MAX_ALERT_RECIPIENTS_LIMIT_REACHED", "GROUP_IS_DISABLED", "GROUP_SIZE_EXCEEDED" |

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-alerts/actions/validate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/actions/validate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Sales threshold alert',
      appId:
        'e0e3187e-4f8c-4c1f-9d2a-1234567890ab',
      enabled: true,
      sheetId: 'abcABC1',
      bookmarkId: 'def-456',
      recipients: {
        DLUsers: [],
        userIds: [
          {
            value: '1b263bs8m0mm_s21s3f',
            groups: [
              'addedIndividually',
              'group1',
              'group2',
            ],
            enabled: true,
            subscribed: true,
            taskRecipientErrors: [
              {
                value: 'NO_ACCESS_TO_APP',
                timestamp:
                  '2019-10-15T16:07:01.492Z',
              },
            ],
            alertingTaskRecipientErrors: [
              {
                added: '2019-10-15T16:07:01.492Z',
                value: 'NO_ACCESS_TO_APP',
              },
            ],
          },
        ],
        DLGroups: [],
        DLListId: 'dl-12345',
        groupIds: [
          {
            value: 'group1',
            enabled: true,
            taskGroupRecipientErrors: [
              {
                value: 'GROUP_WITH_NO_APP_ACCESS',
                timestamp:
                  '2019-10-15T16:07:01.492Z',
              },
            ],
            alertingTaskGroupRecipientErrors: [
              {
                added: '2019-10-15T16:07:01.492Z',
                value: 'GROUP_WITH_NO_APP_ACCESS',
              },
            ],
          },
        ],
      },
      throttling: {
        capacity: 10,
        timezone: 'Etc/UTC',
        replenishRate: 1,
        recurrenceRule: 'RRULE:FREQ=DAILY',
        initialTokenCount: 10,
        referenceTimestamp:
          '2021-07-14T10:00:00Z',
      },
      conditionId: 'cond-789',
      description:
        'Notifies when sales drop below target.',
      triggerType: 'SCHEDULED',
      scheduleOptions: {
        timezone: 'Canada/Pacific',
        recurrence: [
          'RRULE:FREQ=HOURLY;INTERVAL=2',
        ],
        endDateTime: '',
        startDateTime: '2006-01-02T16:04:05',
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-alerts/actions/validate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/actions/validate" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Sales threshold alert","appId":"e0e3187e-4f8c-4c1f-9d2a-1234567890ab","enabled":true,"sheetId":"abcABC1","bookmarkId":"def-456","recipients":{"DLUsers":[],"userIds":[{"value":"1b263bs8m0mm_s21s3f","groups":["addedIndividually","group1","group2"],"enabled":true,"subscribed":true,"taskRecipientErrors":[{"value":"NO_ACCESS_TO_APP","timestamp":"2019-10-15T16:07:01.492Z"}],"alertingTaskRecipientErrors":[{"added":"2019-10-15T16:07:01.492Z","value":"NO_ACCESS_TO_APP"}]}],"DLGroups":[],"DLListId":"dl-12345","groupIds":[{"value":"group1","enabled":true,"taskGroupRecipientErrors":[{"value":"GROUP_WITH_NO_APP_ACCESS","timestamp":"2019-10-15T16:07:01.492Z"}],"alertingTaskGroupRecipientErrors":[{"added":"2019-10-15T16:07:01.492Z","value":"GROUP_WITH_NO_APP_ACCESS"}]}]},"throttling":{"capacity":10,"timezone":"Etc/UTC","replenishRate":1,"recurrenceRule":"RRULE:FREQ=DAILY","initialTokenCount":10,"referenceTimestamp":"2021-07-14T10:00:00Z"},"conditionId":"cond-789","description":"Notifies when sales drop below target.","triggerType":"SCHEDULED","scheduleOptions":{"timezone":"Canada/Pacific","recurrence":["RRULE:FREQ=HOURLY;INTERVAL=2"],"endDateTime":"","startDateTime":"2006-01-02T16:04:05"}}'
```

**Example Response:**

```json
{
  "status": "FAILURE",
  "validations": [
    {
      "id": "string",
      "type": "RECIPIENT",
      "error": "NO_ACCESS",
      "description": "string",
      "validationErrors": [
        "NO_ACCESS"
      ]
    }
  ]
}
```

---

### GET /api/v1/data-alerts/settings

Retrieves the current settings for data alerts.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The alerting settings have been successfully returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | No | These persisted alerting settings are only available for this tenant. Extracted from request JWT. |
| `dataAlertsLimits` | number | No | Represents the number of data alerts limit to be consumed by the user either as an owner or recipient |
| `dataAlertsConsumed` | number | No | Represents the number of data alerts consumed by the user either as an owner or recipient |
| `enable-data-alerting` | boolean | Yes | true if data-alerting feature is enabled for this tenant. Enabling this feature also requires that the license has this feature enabled. |
| `data-alerting-license-status` | string | No | Whether the license for the tenant has the data alerting feature enabled. Enum: "enabled", "disabled" |
| `max-recipients-in-target-access` | integer | No | The maximum number of recipients that can be present in an alerting task in TARGET_ACCESS mode. New recipients cannot be added when this limit is exceeded |
| `data-alerting-feature-operation-status` | string | No | This indicates that there is an ongoing operation to either disable or enable the data alerting feature. none means that no such operation is ongoing. enabling/disabling means that system is currently enabling/disabling the feature Enum: "none", "enabling", "disabling" |
| `data-alerting-feature-operation-status-change` | string | No | UTC timestamp of the most recent change of data-alerting-feature-operation-status. If there has not been any such change, this is the timestamp of the initial creation of the record. |

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-alerts/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/settings',
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
# qlik-cli has not implemented support for GET /api/v1/data-alerts/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "tenantId": "cgdsAumGmQ6l0Bi7CUKt9V8P_Y9GL0sC",
  "dataAlertsLimits": 50,
  "dataAlertsConsumed": 40,
  "enable-data-alerting": true,
  "data-alerting-license-status": "enabled",
  "max-recipients-in-target-access": 100,
  "data-alerting-feature-operation-status": "disabling",
  "data-alerting-feature-operation-status-change": "2020-09-02T13:44:33Z"
}
```

---

### PUT /api/v1/data-alerts/settings

Updates the settings for data alerts. User must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Request for updating the alerting settings

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enable-data-alerting` | boolean | Yes | true if data-alerting feature is enabled. A status change could potentially result in a considerable amount of API operations to enable/disable triggers. Enabling this feature also requires that the license has this feature enabled. |

#### Responses

##### 204

Alerting settings have been successfully updated.

##### 400

Bad request body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 409

Request was denied at this time. This could happen when requesting to disable/enable the feature while there is an ongoing operation to enable/disable the feature

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

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
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/data-alerts/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-alerts/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'enable-data-alerting': true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-alerts/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"enable-data-alerting":true}'
```

---
