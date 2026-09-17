# Sharing tasks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

For scheduled capabilities such as reports, data alerts, subscriptions, and more, sharing tasks defines when these tasks execute, and tie together the resource definition with any conditions on execution.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/sharing-tasks`](#get-apiv1sharing-tasks) | Retrieves all sharing tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks. |
| `POST` | [`/api/v1/sharing-tasks`](#post-apiv1sharing-tasks) | Creates a new recurring sharing task. |
| `GET` | [`/api/v1/sharing-tasks/{taskId}`](#get-apiv1sharing-taskstaskid) | Returns the details of a specific sharing task. |
| `PATCH` | [`/api/v1/sharing-tasks/{taskId}`](#patch-apiv1sharing-taskstaskid) | Updates one or more properties of a specific sharing task. |
| `DELETE` | [`/api/v1/sharing-tasks/{taskId}`](#delete-apiv1sharing-taskstaskid) | Deletes a specific sharing task. |
| `POST` | [`/api/v1/sharing-tasks/{taskId}/actions/cancel`](#post-apiv1sharing-taskstaskidactionscancel) | Requests cancellation of an execution of the specified recurring sharing task. |
| `GET` | [`/api/v1/sharing-tasks/{taskId}/executions`](#get-apiv1sharing-taskstaskidexecutions) | Lists executions for the specified sharing task. |
| `GET` | [`/api/v1/sharing-tasks/{taskId}/executions/{executionId}`](#get-apiv1sharing-taskstaskidexecutionsexecutionid) | Retrieves a specific sharing task execution. |
| `GET` | [`/api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}`](#get-apiv1sharing-taskstaskidexecutionsexecutionidfilesfilealias) | Retrieves the file content for the requested execution and file type. |
| `POST` | [`/api/v1/sharing-tasks/actions/execute`](#post-apiv1sharing-tasksactionsexecute) | Requests execution of the specified recurring sharing task. |
| `GET` | [`/api/v1/sharing-tasks/settings`](#get-apiv1sharing-taskssettings) | Retrieves the current settings for sharing tasks, reports, and other related configuration. |
| `PATCH` | [`/api/v1/sharing-tasks/settings`](#patch-apiv1sharing-taskssettings) | Patches the toggle settings for sharing tasks, reports, and other related configuration in the tenant. User must be assigned the `TenantAdmin` role. |
| `PUT` | [`/api/v1/sharing-tasks/settings`](#put-apiv1sharing-taskssettings) | Updates the settings for sharing tasks, reports, and other related configuration in the tenant. User must be assigned the `TenantAdmin` role. |

## API Reference

### GET /api/v1/sharing-tasks

Retrieves all sharing tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appid` | string | No | the filter by sharing task resource app id. TenantAdmin users may omit this parameter to list all sharing-tasks in the tenant. |
| `excludeDeleting` | boolean | No | Indicates if task with the status DELETING should be excluded from the list |
| `limit` | integer | No | Limit the returned result set |
| `offset` | integer | No | Offset for finding a list of entities - used for pagination |
| `owner` | string | No | the filter by sharing task resource owner id. |
| `ownername` | string | No | the filter by sharing task resource owner name. |
| `page` | string | No | The cursor to the page of data. |
| `role` | string[] | No | the filter by sharing task resource role. Enum: "owner", "recipient" |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "-datecreated", "datecreated", "+datecreated", "-name", "name", "+name", "-ownername", "ownername", "+ownername", "-enabled", "enabled", "+enabled", "-status", "status", "+status", "-type", "type", "+type", "-sent", "sent", "+sent", "-scheduled", "scheduled", "+scheduled", "-appname", "appname", "+appname", "-appid", "appid", "+appid" |
| `templateId` | string[] | No | array of template ids to filter by |
| `type` | string[] | No | the filter by sharing task resource type. If type is template-sharing only and user is not tenant admin, appid is also required. Enum: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing" |
| `next` | string | No | _(deprecated)_ The cursor to the next page of data. Only one of next or previous may be specified. |
| `prev` | string | No | _(deprecated)_ The cursor to the previous page of data. Only one of next or previous may be specified. |

#### Responses

##### 200

The sharing task list has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `links` | object | No |  |
| `recipients` | object | No | List of recipients. An internal recipient is represented by their user id. |
| `sharingTasks` | object[] | No | Gets a list of recurring sharing tasks. |

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
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | No | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `emailAddresses` | string[] | No | Email of recipient (external user). |

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

</details>

<details>
<summary>Properties of `sharingTasks`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the sharing task resource identifier. |
| `name` | string | No | Name of this sharing task |
| `tags` | string[] | No |  |
| `type` | string | No | The sharing task resource type Enum: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing" |
| `appId` | string | No | ID of the app associated (through the templates) with this sharing task |
| `owner` | string | No | User id of owner of the sharing task |
| `state` | object | No | State of the selections and jsOpts |
| `tenant` | string | No | Tenant of the sharing task |
| `appName` | string | No | Name of the app associated (through the templates) with this sharing task |
| `lastRun` | string | No | The last execution start date time timestamp of the task |
| `message` | string | No | Message along with sharing task |
| `spaceId` | string | No | spaceId of the app associated to this task definition |
| `subType` | string | No | _(deprecated)_ Mashup subType of sharing task Enum: "pdf", "pptx", "xlsx", "html", "docx" |
| `trigger` | object | No |  |
| `createdBy` | string | No | ID of creator |
| `insightID` | string | No | The identifier for the insight URLs in this sharing task. Needed to remove the permanent insight upon task deletion. (currently not used in multi-sheet scenarios) |
| `ownerName` | string | No | User name of owner of the sharing task |
| `startTime` | string | No | Time to start capturing the history |
| `templates` | object[] | No | Depending on the value of type, sharing service will internally validate a specific property regarding its data. Type "file" validates property "fileData", type "chart" validates property "chartData", type "story" validates property "storyData". Check description of each of the models for their required properties. |
| `thumbnail` | string | No |  |
| `updatedBy` | string | No | ID of a user that updated this task last |
| `expiration` | string | No | Time for the termination of the task |
| `lastViewed` | string | No | Timestamp of the most recent view by the user. |
| `recipients` | object | No | List of persisted recipients. |
| `statusCode` | string | No | the status of this recurring sharing task Enum: "CHART_NOT_FOUND", "APP_NOT_FOUND", "STORY_NOT_FOUND", "SHEET_NOT_FOUND", "ENGINE_POD_NOT_AVAILABLE", "APP_FORBIDDEN", "CHART_TYPE_NOT_ALLOWED", "FAILED", "DELETING", "IN_PROGRESS", "VALID", "MAX_FAILURES_REACHED", "BOOKMARK_NOT_FOUND", "CANCELLING", "CANCELLED", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "REPORTING_DAILY_QUOTA_EXCEEDED" |
| `taskErrors` | object[] | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `dateCreated` | string | No | Timestamp for the creation of the task |
| `description` | string | No | A description of this sharing task |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `statusLabel` | string | No | error message indicating the underlying failure |
| `emailContent` | object | No |  |
| `enabledByUser` | boolean | No | Toggle for enabling sharing task (user level). Example: user chooses to enable/ disable task. |
| `encryptedState` | object | No | Encrypted property in DB |
| `byokMigrationId` | string | No | internal identifier used when migrating keys |
| `enabledBySystem` | boolean | No | Toggle for enabling sharing task (system level). Example: when task owner gets enabled/ disabled. |
| `retentionPolicy` | object | No |  |
| `scheduleOptions` | object | No |  |
| `selectionErrors` | object | No | reporting service returns rendering errors for missing selections |
| `dataConnectionID` | string | No | the id of the data connection |
| `hasSectionAccess` | boolean | No | true if the associated app has section access enabled |
| `insightDirectURL` | string | No | The direct insights URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `multiInsightURLs` | object[] | No | Contains one or more insight links. Currently only used in multi sheet scenarios. Sharing will ensure that the persisted sort order is aligned to the order of sheets provided. |
| `nextScheduledRun` | string | No | Time for the next scheduled run |
| `reportProperties` | object | No |  |
| `sharePointFolder` | string | No | the SharePoint folder to upload the report to |
| `executeOnCreation` | boolean | No | making this true will execute the sharing task upon creation regardless of next trigger |
| `lastExecutionDate` | string | No | The last execution end date time timestamp of the task |
| `transportChannels` | string[] | No | the transport type for the report Enum: "email", "sharepoint" |
| `distributionListId` | string | No | the id of the distribution list associated to the app |
| `encryptedTemplates` | object | No | Encrypted property in DB |
| `insightFallbackURL` | string | No | The insights fallback URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `encryptedEmailContent` | object | No | the subject and body content for the email to send on report subscriptions |
| `failedExecutionsCount` | integer | No | the number of consecutive failed executions for all recipeints. This is reset on a successful execution for at least one recipient |
| `failedVerificationsCount` | integer | No | the number of failed verifications. This is reset on a successful verification |
| `isCandidateForVerification` | boolean | No | true if the sharing task is a candidate for verification |
| `persistentBookmarkIncludeVariables` | boolean | No | _(deprecated)_ Flag to configure the persistent bookmark to use variables. it is valid for subscriptions with type chart-sharing or sheet-sharing. Deprecated: please use the same field defined in the template instead. |
| `links` | object | No |  |
| `enabled` | boolean | No | true if the sharing task is enabled |
| `latestExecutionURL` | string | No | URL to querying the latest execution tied to this sharing task |
| `latestExecutionFilesURL` | string[] | No | URL to querying the files of the latest execution tied to this sharing task |

<details>
<summary>Properties of `state`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No | Selected fields that led to discovery of monitored Insight Advisor chart |
| `queryItems` | object[] | No | Query that led to discovery of monitored Insight Advisor chart |
| `selections` | object[] | No |  |

<details>
<summary>Properties of `selections`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recurrence` | string[] | Yes | List of RRULE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; event start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. This field is omitted for single events. |
| `chronosJobID` | string | No | The chronosJobId which triggers the sharing task |
| `executeOnAppReload` | boolean | No | Toggle for executing sharing task on app reload. |
| `executionHistoryInterval` | string | No | To prevent overflow in the history, setting this to daily store the chart of a previous day in the history and maintain the live version with the tag latest. Enum: "minutely", "hourly", "daily", "weekly", "monthly", "quarterly", "yearly" |

</details>

<details>
<summary>Properties of `templates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The type of template used to generate the report output. Enum: "file", "chart", "story", "sheet", "multi-sheet", "excel", "pixel-perfect", "html", "powerpoint", "word" |
| `subType` | string | No | The output sub-type produced for the template. Enum: "image", "snapshot", "pdf", "pptx", "xlsx", "qpxp", "qhtml", "docx" |
| `fileName` | string | No | fileName to be used when generating the report |
| `chartData` | object | No | If the template type is not "chart", this can be null. Otherwise, the following properties are required: appId, sheetId, objectId, widthPx, heightPx, language. The following properties are optional: outZoom, outDpi |
| `fileAlias` | string | No | fileAlias provide an opaqueId for the client which can be used to filter and select the report generated |
| `sheetData` | object | No | _(deprecated)_ |
| `storyData` | object | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `fileTimeStamp` | string | No | file name timestamp to be used when generating the report Enum: "yyyy-MM-dd", "yyyy-MM-dd_HH-mm", "yyyyMMdd", "yyyyMMdd_HH-mm" |
| `multiSheetData` | object[] | No | array of sheet data for multi-sheet type template |

<details>
<summary>Properties of `chartData`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sheetData`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `storyData`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `multiSheetData`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `DLGroups` | array | No |  |
| `groupIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `emailAddresses` | object[] | No | recipient object model that is directly persisted in the DB |
| `netRecipientCount` | integer | No | Net count of recipients in DLGroups and DLUsers. |

<details>
<summary>Properties of `userIds`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `groupIds`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `emailAddresses`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `taskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Identifier for type of error occurring on sharing task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "ORPHAN", "PARTIAL_SENT", "FATAL_SENT_ERROR", "SECTION_ACCESS_MODIFIED", "INVALID_DISTRIBUTION_LIST", "MAX_DL_RECIPIENTS_LIMIT_REACHED", "TEMPLATE_NOT_FOUND", "REPORTING_BOOKMARK_NOT_FOUND", "DATA_CONNECTION_NOT_FOUND", "INVALID_SHAREPOINT_DIRECTORY", "GENERIC_FILE_UPLOAD_ERROR", "DISABLED_DUE_TO_OWNERSHIP_CHANGE", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "EXECUTION_TIME_OUT", "OWNER_INSUFFICIENT_PERMISSIONS", "MAX_UNIQUE_REPORTS_LIMIT_REACHED", "MISSING_DISTRIBUTION_LIST", "SECTION_ACCESS_NOT_SUPPORTED", "REPORTING_DAILY_QUOTA_EXCEEDED", "EMAIL_DELIVERY_FAILURE" |
| `timestamp` | string | No | Timestamp for the creation of the error |

</details>

<details>
<summary>Properties of `emailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | Body content of the email sent to recipients. |
| `subject` | string | No | Subject line of the email sent to recipients. |

</details>

<details>
<summary>Properties of `encryptedState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `retentionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `historySize` | integer | No | Number indicating the size of the window which stores the history. For Chart monitoring, the size should be 10. |
| `overrideInterval` | string | No | Using RFC-5545 provide the time interval in which the previous generated can be overridden with the newly generated report. For Chart monitoring, interval should be FREQ=DAILY;INTERVAL=1 |

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
<summary>Properties of `multiInsightURLs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | the status of the creation for this insight URL Enum: "successful", "failed" |
| `directURL` | string | No |  |
| `insightID` | string | No |  |
| `resourceID` | string | No | an identifier for the object within the template that this insight link points to |
| `templateID` | string | No | _(deprecated)_ an identifier for the template that this insight link points to |
| `fallbackURL` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedTemplates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedEmailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | object | No | Encrypted property in DB |
| `subject` | object | No | Encrypted property in DB |

<details>
<summary>Properties of `body`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `subject`</summary>

_Properties truncated due to depth limit._

</details>

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks" \
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
    "emailAddresses": [
      "abc@xyz.com"
    ]
  },
  "sharingTasks": [
    {
      "id": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "type": "chart-monitoring",
      "appId": "string",
      "owner": "pXVNKqotgEMwbKwhz2agPE4yFelnPcWO",
      "state": {
        "fields": [
          {}
        ],
        "queryItems": [
          {}
        ],
        "selections": [
          {
            "name": "Country",
            "values": [
              "Germany"
            ],
            "isNumeric": false,
            "stateName": "$",
            "displayName": "Country",
            "displayValues": [
              "Germany"
            ]
          }
        ]
      },
      "tenant": "_mpoXaH22_vLR1pStfI7oUdGya1nKK24",
      "appName": "string",
      "lastRun": "2019-10-15T16:07:01.492Z",
      "message": "Look at the presentation.",
      "spaceId": "string",
      "subType": "pdf",
      "trigger": {
        "recurrence": [
          "RRULE:FREQ=WEEKLY;INTERVAL=1"
        ],
        "chronosJobID": "chronos-job-123",
        "executeOnAppReload": true,
        "executionHistoryInterval": "daily"
      },
      "createdBy": "string",
      "insightID": "string",
      "ownerName": "Harley Kiffe",
      "startTime": "2019-10-15T16:07:01.492Z",
      "templates": [
        {
          "type": "file",
          "subType": "image",
          "fileName": "sales-report",
          "chartData": {
            "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
            "jsOpts": {},
            "outDpi": 96,
            "outZoom": 1,
            "patches": [
              {}
            ],
            "sheetId": "bdf2efee-815e-4eb7-9e1e-asdfasdfasdf",
            "widthPx": 1584,
            "heightPx": 587,
            "objectId": "167f3e67-ff3b-4ead-a09e-e8cc81d8ad78",
            "objectDef": {},
            "persistentBookmarkIncludeVariables": true
          },
          "fileAlias": "file1",
          "sheetData": {
            "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
            "jsOpts": {},
            "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
            "widthPx": 1584,
            "heightPx": 587,
            "isPrivate": false,
            "sheetName": "My new sheet",
            "jsOptsById": {},
            "patchesById": {}
          },
          "storyData": {
            "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
            "storyId": "39a671a-5f58-468c-bb49-dff933294774"
          },
          "templateId": "da5825325dc9a0dd0260af9",
          "fileTimeStamp": "yyyy-MM-dd",
          "multiSheetData": [
            {
              "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
              "jsOpts": {},
              "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
              "widthPx": 1584,
              "heightPx": 587,
              "isPrivate": false,
              "sheetName": "My new sheet",
              "jsOptsById": {},
              "resizeType": "none",
              "patchesById": {},
              "persistentBookmarkIncludeVariables": true
            }
          ]
        }
      ],
      "thumbnail": "string",
      "updatedBy": "string",
      "expiration": "2019-10-15T16:07:01.492Z",
      "lastViewed": "2019-10-15T16:07:01.492Z",
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
            "subscribed": true,
            "enabledByUser": true,
            "enabledBySystem": true,
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
        "groupIds": [
          {
            "value": "group1",
            "enabledByUser": true,
            "enabledBySystem": true,
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
        ],
        "emailAddresses": [
          {
            "value": "abc@xyz.com",
            "enabled": true,
            "taskRecipientErrors": [
              {
                "value": "NO_ACCESS_TO_APP",
                "timestamp": "2019-10-15T16:07:01.492Z"
              }
            ]
          }
        ],
        "netRecipientCount": 10
      },
      "statusCode": "CHART_NOT_FOUND",
      "taskErrors": [
        {
          "value": "OWNER_DISABLED",
          "timestamp": "2019-10-15T16:07:01.492Z"
        }
      ],
      "templateId": "da5825325dc9a0dd0260af9",
      "dateCreated": "2019-10-15T16:07:01.492Z",
      "description": "string",
      "lastUpdated": "2019-10-15T16:07:01.492Z",
      "statusLabel": "string",
      "emailContent": {
        "body": "report body string",
        "subject": "report subject"
      },
      "enabledByUser": true,
      "encryptedState": {
        "cipher": "string"
      },
      "byokMigrationId": "string",
      "enabledBySystem": true,
      "retentionPolicy": {
        "historySize": 10,
        "overrideInterval": "FREQ=DAILY;INTERVAL=1"
      },
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
      "selectionErrors": {},
      "dataConnectionID": "string",
      "hasSectionAccess": true,
      "insightDirectURL": "string",
      "multiInsightURLs": [
        {
          "status": "successful",
          "directURL": "string",
          "insightID": "string",
          "resourceID": "string",
          "templateID": "string",
          "fallbackURL": "string"
        }
      ],
      "nextScheduledRun": "2019-10-15T16:07:01.492Z",
      "reportProperties": {},
      "sharePointFolder": "string",
      "executeOnCreation": true,
      "lastExecutionDate": "2019-10-15T16:09:01.492Z",
      "transportChannels": [
        "email"
      ],
      "distributionListId": "vXVNKqotgEMwbKwhz2agPE4yFelnPcWX",
      "encryptedTemplates": {
        "cipher": "string"
      },
      "insightFallbackURL": "string",
      "encryptedEmailContent": {
        "body": {
          "cipher": "string"
        },
        "subject": {
          "cipher": "string"
        }
      },
      "failedExecutionsCount": 42,
      "failedVerificationsCount": 42,
      "isCandidateForVerification": true,
      "persistentBookmarkIncludeVariables": true,
      "links": {
        "self": {
          "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
        }
      },
      "enabled": true,
      "latestExecutionURL": "string",
      "latestExecutionFilesURL": [
        "string"
      ]
    }
  ]
}
```

---

### POST /api/v1/sharing-tasks

Creates a new recurring sharing task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The sharing task create request definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of this sharing task |
| `tags` | string[] | No | used to assign sharing task to a collection bucket (tags) |
| `type` | string | Yes | the sharing task resource type. Enum: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing" |
| `state` | object | Yes | State of the selections and jsOpts |
| `appName` | string | No | _(deprecated)_ Name of the app associated (through the templates) with this sharing task |
| `enabled` | boolean | No | Toggle for enabling sharing task. |
| `message` | string | No | Message along with sharing task |
| `spaceId` | string | No | Space ID of the sharing task |
| `subType` | string | No | _(deprecated)_ the sharing task resource mashup sub type. Enum: "pdf", "pptx", "xlsx", "html", "docx" |
| `trigger` | object | No |  |
| `startTime` | string | No | Time to start capturing the history |
| `templates` | object[] | Yes | Templates associated with the sharing task |
| `expiration` | string | No | Timestamp for the termination of the task |
| `recipients` | object | No | List of recipients. An internal recipient is represented by their user id. |
| `description` | string | No | Description of the sharing task |
| `emailContent` | object | No |  |
| `cleanupStrategy` | string | No | A bookmark is considered old if its modification date is older than the app creation date. Enum: "noCleanup", "removeOldBookmarks" |
| `retentionPolicy` | object | No |  |
| `scheduleOptions` | object | No |  |
| `dataConnectionID` | string | No | the id of the data connection |
| `sharePointFolder` | string | No | the SharePoint folder to upload the report to |
| `executeOnCreation` | boolean | No | making this true will execute the sharing task upon creation regardless of next trigger |
| `transportChannels` | string[] | No | the transport type for the report Enum: "email", "sharepoint" |
| `distributionListId` | string | No | the id of the distribution list associated to the app |

<details>
<summary>Properties of `state`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No | Selected fields that led to discovery of monitored Insight Advisor chart |
| `queryItems` | object[] | No | Query that led to discovery of monitored Insight Advisor chart |
| `selections` | object[] | No |  |

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the field the selection applies to. |
| `values` | string[] | Yes | A selected value for the field. |
| `isNumeric` | boolean | Yes | Whether the selected values are numeric. |
| `stateName` | string | Yes | Name of the selection state the values belong to. |
| `displayName` | string | No | Human-readable name of the field the selection applies to. |
| `displayValues` | string[] | No | A human-readable selected value for the field. |

</details>

</details>

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recurrence` | string[] | Yes | List of RRULE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; event start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. This field is omitted for single events. |
| `executeOnAppReload` | boolean | No | Toggle for executing sharing task on app reload. |
| `executionHistoryInterval` | string | No | To prevent overflow in the history, setting this to daily store the chart of a previous day in the history and maintain the live version with the tag latest. Enum: "minutely", "hourly", "daily", "weekly", "monthly", "quarterly", "yearly" |

</details>

<details>
<summary>Properties of `templates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The type of template used to generate the report output. Enum: "file", "chart", "story", "sheet", "multi-sheet", "excel", "pixel-perfect", "html", "powerpoint", "word" |
| `subType` | string | No | The output sub-type produced for the template. Enum: "image", "snapshot", "pdf", "pptx", "xlsx", "qpxp", "qhtml", "docx" |
| `fileName` | string | No | fileName to be used when generating the report |
| `chartData` | object | No | If the template type is not "chart", this can be null. Otherwise, the following properties are required: appId, sheetId, objectId, widthPx, heightPx, language. The following properties are optional: outZoom, outDpi |
| `fileAlias` | string | No | fileAlias provide an opaqueId for the client which can be used to filter and select the report generated |
| `sheetData` | object | No | _(deprecated)_ |
| `storyData` | object | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `fileTimeStamp` | string | No | file name timestamp to be used when generating the report Enum: "yyyy-MM-dd", "yyyy-MM-dd_HH-mm", "yyyyMMdd", "yyyyMMdd_HH-mm" |
| `multiSheetData` | object[] | No | array of sheet data for multi-sheet type template |

<details>
<summary>Properties of `chartData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Visualization state from client as a string json value. Can include language, theme, viewState etc. |
| `outDpi` | integer | No | outDpi of chart |
| `outZoom` | number | No | outZoom of chart |
| `patches` | object[] | No | Soft property changes on chart |
| `sheetId` | string | No | sheetId of app |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `objectId` | string | No | ID of object |
| `objectDef` | object | No | Session chart object definition |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables. |

</details>

<details>
<summary>Properties of `sheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `isPrivate` | boolean | No | _(deprecated)_ optional value to indicate that this sheet is private (used in multi-sheet sharing) |
| `sheetName` | string | No | _(deprecated)_ an optional name for the sheet (used in multi-sheet sharing) |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |

</details>

<details>
<summary>Properties of `storyData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `storyId` | string | No | ID of story |

</details>

<details>
<summary>Properties of `multiSheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart, must be 0 or omitted for autofit. |
| `heightPx` | integer | No | heightPx of chart, must be 0 or omitted for autofit. |
| `isPrivate` | boolean | No | optional value to indicate that this sheet is private |
| `sheetName` | string | No | an optional name for the sheet |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `resizeType` | string | No | Currently only autofit is supported. If omitted, autofit is the default. The type of resize to be performed:   - none is used to export a visualization, sheet as is (e.g. normal size), regardless its size. This may result in cropping.   - autofit automatically fits the visualization, sheet into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.   - fit fits the visualization, sheet into the area specified in resizeData. The content will be rescaled to fit in that area.  Enum: "none", "fit", "autofit" |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables |

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | No | an internal recipient based on its user id. |
| `DLGroups` | array | No |  |
| `emailAddresses` | string[] | No | Email of recipient (external user). |

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

</details>

<details>
<summary>Properties of `emailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | Body content of the email sent to recipients. |
| `subject` | string | No | Subject line of the email sent to recipients. |

</details>

<details>
<summary>Properties of `retentionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `historySize` | integer | No | Number indicating the size of the window which stores the history. For Chart monitoring, the size should be 10. |
| `overrideInterval` | string | No | Using RFC-5545 provide the time interval in which the previous generated can be overridden with the newly generated report. For Chart monitoring, interval should be FREQ=DAILY;INTERVAL=1 |

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

##### 201

The sharing task has been successfully created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the sharing task resource identifier. |
| `name` | string | No | Name of this sharing task |
| `tags` | string[] | No |  |
| `type` | string | No | The sharing task resource type Enum: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing" |
| `appId` | string | No | ID of the app associated (through the templates) with this sharing task |
| `owner` | string | No | User id of owner of the sharing task |
| `state` | object | No | State of the selections and jsOpts |
| `tenant` | string | No | Tenant of the sharing task |
| `appName` | string | No | Name of the app associated (through the templates) with this sharing task |
| `lastRun` | string | No | The last execution start date time timestamp of the task |
| `message` | string | No | Message along with sharing task |
| `spaceId` | string | No | spaceId of the app associated to this task definition |
| `subType` | string | No | _(deprecated)_ Mashup subType of sharing task Enum: "pdf", "pptx", "xlsx", "html", "docx" |
| `trigger` | object | No |  |
| `createdBy` | string | No | ID of creator |
| `insightID` | string | No | The identifier for the insight URLs in this sharing task. Needed to remove the permanent insight upon task deletion. (currently not used in multi-sheet scenarios) |
| `ownerName` | string | No | User name of owner of the sharing task |
| `startTime` | string | No | Time to start capturing the history |
| `templates` | object[] | No | Depending on the value of type, sharing service will internally validate a specific property regarding its data. Type "file" validates property "fileData", type "chart" validates property "chartData", type "story" validates property "storyData". Check description of each of the models for their required properties. |
| `thumbnail` | string | No |  |
| `updatedBy` | string | No | ID of a user that updated this task last |
| `expiration` | string | No | Time for the termination of the task |
| `lastViewed` | string | No | Timestamp of the most recent view by the user. |
| `recipients` | object | No | List of persisted recipients. |
| `statusCode` | string | No | the status of this recurring sharing task Enum: "CHART_NOT_FOUND", "APP_NOT_FOUND", "STORY_NOT_FOUND", "SHEET_NOT_FOUND", "ENGINE_POD_NOT_AVAILABLE", "APP_FORBIDDEN", "CHART_TYPE_NOT_ALLOWED", "FAILED", "DELETING", "IN_PROGRESS", "VALID", "MAX_FAILURES_REACHED", "BOOKMARK_NOT_FOUND", "CANCELLING", "CANCELLED", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "REPORTING_DAILY_QUOTA_EXCEEDED" |
| `taskErrors` | object[] | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `dateCreated` | string | No | Timestamp for the creation of the task |
| `description` | string | No | A description of this sharing task |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `statusLabel` | string | No | error message indicating the underlying failure |
| `emailContent` | object | No |  |
| `enabledByUser` | boolean | No | Toggle for enabling sharing task (user level). Example: user chooses to enable/ disable task. |
| `encryptedState` | object | No | Encrypted property in DB |
| `byokMigrationId` | string | No | internal identifier used when migrating keys |
| `enabledBySystem` | boolean | No | Toggle for enabling sharing task (system level). Example: when task owner gets enabled/ disabled. |
| `retentionPolicy` | object | No |  |
| `scheduleOptions` | object | No |  |
| `selectionErrors` | object | No | reporting service returns rendering errors for missing selections |
| `dataConnectionID` | string | No | the id of the data connection |
| `hasSectionAccess` | boolean | No | true if the associated app has section access enabled |
| `insightDirectURL` | string | No | The direct insights URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `multiInsightURLs` | object[] | No | Contains one or more insight links. Currently only used in multi sheet scenarios. Sharing will ensure that the persisted sort order is aligned to the order of sheets provided. |
| `nextScheduledRun` | string | No | Time for the next scheduled run |
| `reportProperties` | object | No |  |
| `sharePointFolder` | string | No | the SharePoint folder to upload the report to |
| `executeOnCreation` | boolean | No | making this true will execute the sharing task upon creation regardless of next trigger |
| `lastExecutionDate` | string | No | The last execution end date time timestamp of the task |
| `transportChannels` | string[] | No | the transport type for the report Enum: "email", "sharepoint" |
| `distributionListId` | string | No | the id of the distribution list associated to the app |
| `encryptedTemplates` | object | No | Encrypted property in DB |
| `insightFallbackURL` | string | No | The insights fallback URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `encryptedEmailContent` | object | No | the subject and body content for the email to send on report subscriptions |
| `failedExecutionsCount` | integer | No | the number of consecutive failed executions for all recipeints. This is reset on a successful execution for at least one recipient |
| `failedVerificationsCount` | integer | No | the number of failed verifications. This is reset on a successful verification |
| `isCandidateForVerification` | boolean | No | true if the sharing task is a candidate for verification |
| `persistentBookmarkIncludeVariables` | boolean | No | _(deprecated)_ Flag to configure the persistent bookmark to use variables. it is valid for subscriptions with type chart-sharing or sheet-sharing. Deprecated: please use the same field defined in the template instead. |
| `links` | object | No |  |
| `enabled` | boolean | No | true if the sharing task is enabled |
| `latestExecutionURL` | string | No | URL to querying the latest execution tied to this sharing task |
| `latestExecutionFilesURL` | string[] | No | URL to querying the files of the latest execution tied to this sharing task |

<details>
<summary>Properties of `state`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No | Selected fields that led to discovery of monitored Insight Advisor chart |
| `queryItems` | object[] | No | Query that led to discovery of monitored Insight Advisor chart |
| `selections` | object[] | No |  |

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the field the selection applies to. |
| `values` | string[] | Yes | A selected value for the field. |
| `isNumeric` | boolean | Yes | Whether the selected values are numeric. |
| `stateName` | string | Yes | Name of the selection state the values belong to. |
| `displayName` | string | No | Human-readable name of the field the selection applies to. |
| `displayValues` | string[] | No | A human-readable selected value for the field. |

</details>

</details>

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recurrence` | string[] | Yes | List of RRULE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; event start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. This field is omitted for single events. |
| `chronosJobID` | string | No | The chronosJobId which triggers the sharing task |
| `executeOnAppReload` | boolean | No | Toggle for executing sharing task on app reload. |
| `executionHistoryInterval` | string | No | To prevent overflow in the history, setting this to daily store the chart of a previous day in the history and maintain the live version with the tag latest. Enum: "minutely", "hourly", "daily", "weekly", "monthly", "quarterly", "yearly" |

</details>

<details>
<summary>Properties of `templates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The type of template used to generate the report output. Enum: "file", "chart", "story", "sheet", "multi-sheet", "excel", "pixel-perfect", "html", "powerpoint", "word" |
| `subType` | string | No | The output sub-type produced for the template. Enum: "image", "snapshot", "pdf", "pptx", "xlsx", "qpxp", "qhtml", "docx" |
| `fileName` | string | No | fileName to be used when generating the report |
| `chartData` | object | No | If the template type is not "chart", this can be null. Otherwise, the following properties are required: appId, sheetId, objectId, widthPx, heightPx, language. The following properties are optional: outZoom, outDpi |
| `fileAlias` | string | No | fileAlias provide an opaqueId for the client which can be used to filter and select the report generated |
| `sheetData` | object | No | _(deprecated)_ |
| `storyData` | object | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `fileTimeStamp` | string | No | file name timestamp to be used when generating the report Enum: "yyyy-MM-dd", "yyyy-MM-dd_HH-mm", "yyyyMMdd", "yyyyMMdd_HH-mm" |
| `multiSheetData` | object[] | No | array of sheet data for multi-sheet type template |

<details>
<summary>Properties of `chartData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Visualization state from client as a string json value. Can include language, theme, viewState etc. |
| `outDpi` | integer | No | outDpi of chart |
| `outZoom` | number | No | outZoom of chart |
| `patches` | object[] | No | Soft property changes on chart |
| `sheetId` | string | No | sheetId of app |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `objectId` | string | No | ID of object |
| `objectDef` | object | No | Session chart object definition |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables. |

</details>

<details>
<summary>Properties of `sheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `isPrivate` | boolean | No | _(deprecated)_ optional value to indicate that this sheet is private (used in multi-sheet sharing) |
| `sheetName` | string | No | _(deprecated)_ an optional name for the sheet (used in multi-sheet sharing) |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |

</details>

<details>
<summary>Properties of `storyData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `storyId` | string | No | ID of story |

</details>

<details>
<summary>Properties of `multiSheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart, must be 0 or omitted for autofit. |
| `heightPx` | integer | No | heightPx of chart, must be 0 or omitted for autofit. |
| `isPrivate` | boolean | No | optional value to indicate that this sheet is private |
| `sheetName` | string | No | an optional name for the sheet |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `resizeType` | string | No | Currently only autofit is supported. If omitted, autofit is the default. The type of resize to be performed:   - none is used to export a visualization, sheet as is (e.g. normal size), regardless its size. This may result in cropping.   - autofit automatically fits the visualization, sheet into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.   - fit fits the visualization, sheet into the area specified in resizeData. The content will be rescaled to fit in that area.  Enum: "none", "fit", "autofit" |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables |

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `DLGroups` | array | No |  |
| `groupIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `emailAddresses` | object[] | No | recipient object model that is directly persisted in the DB |
| `netRecipientCount` | integer | No | Net count of recipients in DLGroups and DLUsers. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `subscribed` | boolean | No | Whether this user is subscribed to alerts in this task |
| `enabledByUser` | boolean | No | Whether this recipient can receive alerts, set by api calls. |
| `enabledBySystem` | boolean | No | Whether this recipient can receive alerts, set by external settings. |
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
| `enabledByUser` | boolean | No | Whether this recipient can receive alerts, set by api calls. |
| `enabledBySystem` | boolean | No | Whether this recipient can receive alerts, set by external settings. |
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

<details>
<summary>Properties of `emailAddresses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Email of recipient (external user). |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `taskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Identifier for type of error occurring on sharing task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "ORPHAN", "PARTIAL_SENT", "FATAL_SENT_ERROR", "SECTION_ACCESS_MODIFIED", "INVALID_DISTRIBUTION_LIST", "MAX_DL_RECIPIENTS_LIMIT_REACHED", "TEMPLATE_NOT_FOUND", "REPORTING_BOOKMARK_NOT_FOUND", "DATA_CONNECTION_NOT_FOUND", "INVALID_SHAREPOINT_DIRECTORY", "GENERIC_FILE_UPLOAD_ERROR", "DISABLED_DUE_TO_OWNERSHIP_CHANGE", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "EXECUTION_TIME_OUT", "OWNER_INSUFFICIENT_PERMISSIONS", "MAX_UNIQUE_REPORTS_LIMIT_REACHED", "MISSING_DISTRIBUTION_LIST", "SECTION_ACCESS_NOT_SUPPORTED", "REPORTING_DAILY_QUOTA_EXCEEDED", "EMAIL_DELIVERY_FAILURE" |
| `timestamp` | string | No | Timestamp for the creation of the error |

</details>

<details>
<summary>Properties of `emailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | Body content of the email sent to recipients. |
| `subject` | string | No | Subject line of the email sent to recipients. |

</details>

<details>
<summary>Properties of `encryptedState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `retentionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `historySize` | integer | No | Number indicating the size of the window which stores the history. For Chart monitoring, the size should be 10. |
| `overrideInterval` | string | No | Using RFC-5545 provide the time interval in which the previous generated can be overridden with the newly generated report. For Chart monitoring, interval should be FREQ=DAILY;INTERVAL=1 |

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
<summary>Properties of `multiInsightURLs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | the status of the creation for this insight URL Enum: "successful", "failed" |
| `directURL` | string | No |  |
| `insightID` | string | No |  |
| `resourceID` | string | No | an identifier for the object within the template that this insight link points to |
| `templateID` | string | No | _(deprecated)_ an identifier for the template that this insight link points to |
| `fallbackURL` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedTemplates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedEmailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | object | No | Encrypted property in DB |
| `subject` | object | No | Encrypted property in DB |

<details>
<summary>Properties of `body`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `subject`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

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
// qlik-api has not implemented support for `POST /api/v1/sharing-tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'Example Sharing Task',
      tags: ['finance'],
      type: 'chart-monitoring',
      state: {
        fields: [{}],
        queryItems: [{}],
        selections: [
          {
            name: 'Country',
            values: ['Germany'],
            isNumeric: false,
            stateName: '$',
            displayName: 'Country',
            displayValues: ['Germany'],
          },
        ],
      },
      appName: 'Sales Dashboard',
      enabled: true,
      message: 'Look at the presentation.',
      spaceId: '5f7b1a2c3d4e5f6a7b8c9d0e',
      subType: 'pdf',
      trigger: {
        recurrence: [
          'RRULE:FREQ=WEEKLY;INTERVAL=1',
        ],
        executeOnAppReload: true,
        executionHistoryInterval: 'daily',
      },
      startTime: '2019-10-15T16:07:01.492Z',
      templates: [
        {
          type: 'file',
          subType: 'image',
          fileName: 'sales-report',
          chartData: {
            appId:
              'bdf2efee-815e-4eb7-9e1e-c42d516baf29',
            jsOpts: {},
            outDpi: 96,
            outZoom: 1,
            patches: [{}],
            sheetId:
              'bdf2efee-815e-4eb7-9e1e-asdfasdfasdf',
            widthPx: 1584,
            heightPx: 587,
            objectId:
              '167f3e67-ff3b-4ead-a09e-e8cc81d8ad78',
            objectDef: {},
            persistentBookmarkIncludeVariables: true,
          },
          fileAlias: 'file1',
          sheetData: {
            appId:
              'bdf2efee-815e-4eb7-9e1e-c42d516baf29',
            jsOpts: {},
            sheetId:
              '39a671a-5f58-468c-bb49-dff933294774',
            widthPx: 1584,
            heightPx: 587,
            isPrivate: false,
            sheetName: 'My new sheet',
            jsOptsById: {},
            patchesById: {},
          },
          storyData: {
            appId:
              'bdf2efee-815e-4eb7-9e1e-c42d516baf29',
            storyId:
              '39a671a-5f58-468c-bb49-dff933294774',
          },
          fileTimeStamp: 'yyyy-MM-dd',
          multiSheetData: [
            {
              appId:
                'bdf2efee-815e-4eb7-9e1e-c42d516baf29',
              jsOpts: {},
              sheetId:
                '39a671a-5f58-468c-bb49-dff933294774',
              widthPx: 1584,
              heightPx: 587,
              isPrivate: false,
              sheetName: 'My new sheet',
              jsOptsById: {},
              resizeType: 'none',
              patchesById: {},
              persistentBookmarkIncludeVariables: true,
            },
          ],
        },
      ],
      expiration: '2019-10-15T16:07:01.492Z',
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
        emailAddresses: ['abc@xyz.com'],
      },
      description:
        'Weekly sales report subscription.',
      emailContent: {
        body: 'report body string',
        subject: 'report subject',
      },
      cleanupStrategy: 'noCleanup',
      retentionPolicy: {
        historySize: 10,
        overrideInterval: 'FREQ=DAILY;INTERVAL=1',
      },
      scheduleOptions: {
        timezone: 'Canada/Pacific',
        recurrence: [
          'RRULE:FREQ=HOURLY;INTERVAL=2',
        ],
        endDateTime: '',
        startDateTime: '2006-01-02T16:04:05',
      },
      dataConnectionID: 'data-connection-123',
      sharePointFolder:
        'Shared Documents/Reports',
      executeOnCreation: true,
      transportChannels: ['email'],
      distributionListId:
        'mpoXaH22_vLR1pStfI7oUdGya1nKK24',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/sharing-tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"Example Sharing Task","tags":["finance"],"type":"chart-monitoring","state":{"fields":[{}],"queryItems":[{}],"selections":[{"name":"Country","values":["Germany"],"isNumeric":false,"stateName":"$","displayName":"Country","displayValues":["Germany"]}]},"appName":"Sales Dashboard","enabled":true,"message":"Look at the presentation.","spaceId":"5f7b1a2c3d4e5f6a7b8c9d0e","subType":"pdf","trigger":{"recurrence":["RRULE:FREQ=WEEKLY;INTERVAL=1"],"executeOnAppReload":true,"executionHistoryInterval":"daily"},"startTime":"2019-10-15T16:07:01.492Z","templates":[{"type":"file","subType":"image","fileName":"sales-report","chartData":{"appId":"bdf2efee-815e-4eb7-9e1e-c42d516baf29","jsOpts":{},"outDpi":96,"outZoom":1,"patches":[{}],"sheetId":"bdf2efee-815e-4eb7-9e1e-asdfasdfasdf","widthPx":1584,"heightPx":587,"objectId":"167f3e67-ff3b-4ead-a09e-e8cc81d8ad78","objectDef":{},"persistentBookmarkIncludeVariables":true},"fileAlias":"file1","sheetData":{"appId":"bdf2efee-815e-4eb7-9e1e-c42d516baf29","jsOpts":{},"sheetId":"39a671a-5f58-468c-bb49-dff933294774","widthPx":1584,"heightPx":587,"isPrivate":false,"sheetName":"My new sheet","jsOptsById":{},"patchesById":{}},"storyData":{"appId":"bdf2efee-815e-4eb7-9e1e-c42d516baf29","storyId":"39a671a-5f58-468c-bb49-dff933294774"},"fileTimeStamp":"yyyy-MM-dd","multiSheetData":[{"appId":"bdf2efee-815e-4eb7-9e1e-c42d516baf29","jsOpts":{},"sheetId":"39a671a-5f58-468c-bb49-dff933294774","widthPx":1584,"heightPx":587,"isPrivate":false,"sheetName":"My new sheet","jsOptsById":{},"resizeType":"none","patchesById":{},"persistentBookmarkIncludeVariables":true}]}],"expiration":"2019-10-15T16:07:01.492Z","recipients":{"DLUsers":[],"userIds":[{"value":"1b263bs8m0mm_s21s3f","groups":["addedIndividually","group1","group2"],"enabled":true,"subscribed":true,"taskRecipientErrors":[{"value":"NO_ACCESS_TO_APP","timestamp":"2019-10-15T16:07:01.492Z"}],"alertingTaskRecipientErrors":[{"added":"2019-10-15T16:07:01.492Z","value":"NO_ACCESS_TO_APP"}]}],"DLGroups":[],"emailAddresses":["abc@xyz.com"]},"description":"Weekly sales report subscription.","emailContent":{"body":"report body string","subject":"report subject"},"cleanupStrategy":"noCleanup","retentionPolicy":{"historySize":10,"overrideInterval":"FREQ=DAILY;INTERVAL=1"},"scheduleOptions":{"timezone":"Canada/Pacific","recurrence":["RRULE:FREQ=HOURLY;INTERVAL=2"],"endDateTime":"","startDateTime":"2006-01-02T16:04:05"},"dataConnectionID":"data-connection-123","sharePointFolder":"Shared Documents/Reports","executeOnCreation":true,"transportChannels":["email"],"distributionListId":"mpoXaH22_vLR1pStfI7oUdGya1nKK24"}'
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "chart-monitoring",
  "appId": "string",
  "owner": "pXVNKqotgEMwbKwhz2agPE4yFelnPcWO",
  "state": {
    "fields": [
      {}
    ],
    "queryItems": [
      {}
    ],
    "selections": [
      {
        "name": "Country",
        "values": [
          "Germany"
        ],
        "isNumeric": false,
        "stateName": "$",
        "displayName": "Country",
        "displayValues": [
          "Germany"
        ]
      }
    ]
  },
  "tenant": "_mpoXaH22_vLR1pStfI7oUdGya1nKK24",
  "appName": "string",
  "lastRun": "2019-10-15T16:07:01.492Z",
  "message": "Look at the presentation.",
  "spaceId": "string",
  "subType": "pdf",
  "trigger": {
    "recurrence": [
      "RRULE:FREQ=WEEKLY;INTERVAL=1"
    ],
    "chronosJobID": "chronos-job-123",
    "executeOnAppReload": true,
    "executionHistoryInterval": "daily"
  },
  "createdBy": "string",
  "insightID": "string",
  "ownerName": "Harley Kiffe",
  "startTime": "2019-10-15T16:07:01.492Z",
  "templates": [
    {
      "type": "file",
      "subType": "image",
      "fileName": "sales-report",
      "chartData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "jsOpts": {},
        "outDpi": 96,
        "outZoom": 1,
        "patches": [
          {}
        ],
        "sheetId": "bdf2efee-815e-4eb7-9e1e-asdfasdfasdf",
        "widthPx": 1584,
        "heightPx": 587,
        "objectId": "167f3e67-ff3b-4ead-a09e-e8cc81d8ad78",
        "objectDef": {},
        "persistentBookmarkIncludeVariables": true
      },
      "fileAlias": "file1",
      "sheetData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "jsOpts": {},
        "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
        "widthPx": 1584,
        "heightPx": 587,
        "isPrivate": false,
        "sheetName": "My new sheet",
        "jsOptsById": {},
        "patchesById": {}
      },
      "storyData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "storyId": "39a671a-5f58-468c-bb49-dff933294774"
      },
      "templateId": "da5825325dc9a0dd0260af9",
      "fileTimeStamp": "yyyy-MM-dd",
      "multiSheetData": [
        {
          "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
          "jsOpts": {},
          "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
          "widthPx": 1584,
          "heightPx": 587,
          "isPrivate": false,
          "sheetName": "My new sheet",
          "jsOptsById": {},
          "resizeType": "none",
          "patchesById": {},
          "persistentBookmarkIncludeVariables": true
        }
      ]
    }
  ],
  "thumbnail": "string",
  "updatedBy": "string",
  "expiration": "2019-10-15T16:07:01.492Z",
  "lastViewed": "2019-10-15T16:07:01.492Z",
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
        "subscribed": true,
        "enabledByUser": true,
        "enabledBySystem": true,
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
    "groupIds": [
      {
        "value": "group1",
        "enabledByUser": true,
        "enabledBySystem": true,
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
    ],
    "emailAddresses": [
      {
        "value": "abc@xyz.com",
        "enabled": true,
        "taskRecipientErrors": [
          {
            "value": "NO_ACCESS_TO_APP",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ]
      }
    ],
    "netRecipientCount": 10
  },
  "statusCode": "CHART_NOT_FOUND",
  "taskErrors": [
    {
      "value": "OWNER_DISABLED",
      "timestamp": "2019-10-15T16:07:01.492Z"
    }
  ],
  "templateId": "da5825325dc9a0dd0260af9",
  "dateCreated": "2019-10-15T16:07:01.492Z",
  "description": "string",
  "lastUpdated": "2019-10-15T16:07:01.492Z",
  "statusLabel": "string",
  "emailContent": {
    "body": "report body string",
    "subject": "report subject"
  },
  "enabledByUser": true,
  "encryptedState": {
    "cipher": "string"
  },
  "byokMigrationId": "string",
  "enabledBySystem": true,
  "retentionPolicy": {
    "historySize": 10,
    "overrideInterval": "FREQ=DAILY;INTERVAL=1"
  },
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
  "selectionErrors": {},
  "dataConnectionID": "string",
  "hasSectionAccess": true,
  "insightDirectURL": "string",
  "multiInsightURLs": [
    {
      "status": "successful",
      "directURL": "string",
      "insightID": "string",
      "resourceID": "string",
      "templateID": "string",
      "fallbackURL": "string"
    }
  ],
  "nextScheduledRun": "2019-10-15T16:07:01.492Z",
  "reportProperties": {},
  "sharePointFolder": "string",
  "executeOnCreation": true,
  "lastExecutionDate": "2019-10-15T16:09:01.492Z",
  "transportChannels": [
    "email"
  ],
  "distributionListId": "vXVNKqotgEMwbKwhz2agPE4yFelnPcWX",
  "encryptedTemplates": {
    "cipher": "string"
  },
  "insightFallbackURL": "string",
  "encryptedEmailContent": {
    "body": {
      "cipher": "string"
    },
    "subject": {
      "cipher": "string"
    }
  },
  "failedExecutionsCount": 42,
  "failedVerificationsCount": 42,
  "isCandidateForVerification": true,
  "persistentBookmarkIncludeVariables": true,
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "enabled": true,
  "latestExecutionURL": "string",
  "latestExecutionFilesURL": [
    "string"
  ]
}
```

---

### GET /api/v1/sharing-tasks/{taskId}

Returns the details of a specific sharing task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isViewChart` | boolean | No | Determines whether to update the `lastViewed` property for the sharing task, which is used to determine whether the sharing task is still in use. If set to `true`, this will be updated to current time. |

#### Responses

##### 200

Sharing task has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the sharing task resource identifier. |
| `name` | string | No | Name of this sharing task |
| `tags` | string[] | No |  |
| `type` | string | No | The sharing task resource type Enum: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing" |
| `appId` | string | No | ID of the app associated (through the templates) with this sharing task |
| `owner` | string | No | User id of owner of the sharing task |
| `state` | object | No | State of the selections and jsOpts |
| `tenant` | string | No | Tenant of the sharing task |
| `appName` | string | No | Name of the app associated (through the templates) with this sharing task |
| `lastRun` | string | No | The last execution start date time timestamp of the task |
| `message` | string | No | Message along with sharing task |
| `spaceId` | string | No | spaceId of the app associated to this task definition |
| `subType` | string | No | _(deprecated)_ Mashup subType of sharing task Enum: "pdf", "pptx", "xlsx", "html", "docx" |
| `trigger` | object | No |  |
| `createdBy` | string | No | ID of creator |
| `insightID` | string | No | The identifier for the insight URLs in this sharing task. Needed to remove the permanent insight upon task deletion. (currently not used in multi-sheet scenarios) |
| `ownerName` | string | No | User name of owner of the sharing task |
| `startTime` | string | No | Time to start capturing the history |
| `templates` | object[] | No | Depending on the value of type, sharing service will internally validate a specific property regarding its data. Type "file" validates property "fileData", type "chart" validates property "chartData", type "story" validates property "storyData". Check description of each of the models for their required properties. |
| `thumbnail` | string | No |  |
| `updatedBy` | string | No | ID of a user that updated this task last |
| `expiration` | string | No | Time for the termination of the task |
| `lastViewed` | string | No | Timestamp of the most recent view by the user. |
| `recipients` | object | No | List of persisted recipients. |
| `statusCode` | string | No | the status of this recurring sharing task Enum: "CHART_NOT_FOUND", "APP_NOT_FOUND", "STORY_NOT_FOUND", "SHEET_NOT_FOUND", "ENGINE_POD_NOT_AVAILABLE", "APP_FORBIDDEN", "CHART_TYPE_NOT_ALLOWED", "FAILED", "DELETING", "IN_PROGRESS", "VALID", "MAX_FAILURES_REACHED", "BOOKMARK_NOT_FOUND", "CANCELLING", "CANCELLED", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "REPORTING_DAILY_QUOTA_EXCEEDED" |
| `taskErrors` | object[] | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `dateCreated` | string | No | Timestamp for the creation of the task |
| `description` | string | No | A description of this sharing task |
| `lastUpdated` | string | No | Timestamp of the most recent update. |
| `statusLabel` | string | No | error message indicating the underlying failure |
| `emailContent` | object | No |  |
| `enabledByUser` | boolean | No | Toggle for enabling sharing task (user level). Example: user chooses to enable/ disable task. |
| `encryptedState` | object | No | Encrypted property in DB |
| `byokMigrationId` | string | No | internal identifier used when migrating keys |
| `enabledBySystem` | boolean | No | Toggle for enabling sharing task (system level). Example: when task owner gets enabled/ disabled. |
| `retentionPolicy` | object | No |  |
| `scheduleOptions` | object | No |  |
| `selectionErrors` | object | No | reporting service returns rendering errors for missing selections |
| `dataConnectionID` | string | No | the id of the data connection |
| `hasSectionAccess` | boolean | No | true if the associated app has section access enabled |
| `insightDirectURL` | string | No | The direct insights URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `multiInsightURLs` | object[] | No | Contains one or more insight links. Currently only used in multi sheet scenarios. Sharing will ensure that the persisted sort order is aligned to the order of sheets provided. |
| `nextScheduledRun` | string | No | Time for the next scheduled run |
| `reportProperties` | object | No |  |
| `sharePointFolder` | string | No | the SharePoint folder to upload the report to |
| `executeOnCreation` | boolean | No | making this true will execute the sharing task upon creation regardless of next trigger |
| `lastExecutionDate` | string | No | The last execution end date time timestamp of the task |
| `transportChannels` | string[] | No | the transport type for the report Enum: "email", "sharepoint" |
| `distributionListId` | string | No | the id of the distribution list associated to the app |
| `encryptedTemplates` | object | No | Encrypted property in DB |
| `insightFallbackURL` | string | No | The insights fallback URL for the first template of this sharing task. (currently not used in multi-sheet scenarios) |
| `encryptedEmailContent` | object | No | the subject and body content for the email to send on report subscriptions |
| `failedExecutionsCount` | integer | No | the number of consecutive failed executions for all recipeints. This is reset on a successful execution for at least one recipient |
| `failedVerificationsCount` | integer | No | the number of failed verifications. This is reset on a successful verification |
| `isCandidateForVerification` | boolean | No | true if the sharing task is a candidate for verification |
| `persistentBookmarkIncludeVariables` | boolean | No | _(deprecated)_ Flag to configure the persistent bookmark to use variables. it is valid for subscriptions with type chart-sharing or sheet-sharing. Deprecated: please use the same field defined in the template instead. |
| `links` | object | No |  |
| `enabled` | boolean | No | true if the sharing task is enabled |
| `latestExecutionURL` | string | No | URL to querying the latest execution tied to this sharing task |
| `latestExecutionFilesURL` | string[] | No | URL to querying the files of the latest execution tied to this sharing task |

<details>
<summary>Properties of `state`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | No | Selected fields that led to discovery of monitored Insight Advisor chart |
| `queryItems` | object[] | No | Query that led to discovery of monitored Insight Advisor chart |
| `selections` | object[] | No |  |

<details>
<summary>Properties of `selections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the field the selection applies to. |
| `values` | string[] | Yes | A selected value for the field. |
| `isNumeric` | boolean | Yes | Whether the selected values are numeric. |
| `stateName` | string | Yes | Name of the selection state the values belong to. |
| `displayName` | string | No | Human-readable name of the field the selection applies to. |
| `displayValues` | string[] | No | A human-readable selected value for the field. |

</details>

</details>

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recurrence` | string[] | Yes | List of RRULE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; event start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. This field is omitted for single events. |
| `chronosJobID` | string | No | The chronosJobId which triggers the sharing task |
| `executeOnAppReload` | boolean | No | Toggle for executing sharing task on app reload. |
| `executionHistoryInterval` | string | No | To prevent overflow in the history, setting this to daily store the chart of a previous day in the history and maintain the live version with the tag latest. Enum: "minutely", "hourly", "daily", "weekly", "monthly", "quarterly", "yearly" |

</details>

<details>
<summary>Properties of `templates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The type of template used to generate the report output. Enum: "file", "chart", "story", "sheet", "multi-sheet", "excel", "pixel-perfect", "html", "powerpoint", "word" |
| `subType` | string | No | The output sub-type produced for the template. Enum: "image", "snapshot", "pdf", "pptx", "xlsx", "qpxp", "qhtml", "docx" |
| `fileName` | string | No | fileName to be used when generating the report |
| `chartData` | object | No | If the template type is not "chart", this can be null. Otherwise, the following properties are required: appId, sheetId, objectId, widthPx, heightPx, language. The following properties are optional: outZoom, outDpi |
| `fileAlias` | string | No | fileAlias provide an opaqueId for the client which can be used to filter and select the report generated |
| `sheetData` | object | No | _(deprecated)_ |
| `storyData` | object | No |  |
| `templateId` | string | No | _(deprecated)_ ID of unique template |
| `fileTimeStamp` | string | No | file name timestamp to be used when generating the report Enum: "yyyy-MM-dd", "yyyy-MM-dd_HH-mm", "yyyyMMdd", "yyyyMMdd_HH-mm" |
| `multiSheetData` | object[] | No | array of sheet data for multi-sheet type template |

<details>
<summary>Properties of `chartData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Visualization state from client as a string json value. Can include language, theme, viewState etc. |
| `outDpi` | integer | No | outDpi of chart |
| `outZoom` | number | No | outZoom of chart |
| `patches` | object[] | No | Soft property changes on chart |
| `sheetId` | string | No | sheetId of app |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `objectId` | string | No | ID of object |
| `objectDef` | object | No | Session chart object definition |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables. |

</details>

<details>
<summary>Properties of `sheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart |
| `heightPx` | integer | No | heightPx of chart |
| `isPrivate` | boolean | No | _(deprecated)_ optional value to indicate that this sheet is private (used in multi-sheet sharing) |
| `sheetName` | string | No | _(deprecated)_ an optional name for the sheet (used in multi-sheet sharing) |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |

</details>

<details>
<summary>Properties of `storyData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `storyId` | string | No | ID of story |

</details>

<details>
<summary>Properties of `multiSheetData`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | ID of app |
| `jsOpts` | object | No | Sheet state from client as a string json value. Can include language, theme, viewState etc. |
| `sheetId` | string | No | ID of sheet |
| `widthPx` | integer | No | widthPx of chart, must be 0 or omitted for autofit. |
| `heightPx` | integer | No | heightPx of chart, must be 0 or omitted for autofit. |
| `isPrivate` | boolean | No | optional value to indicate that this sheet is private |
| `sheetName` | string | No | an optional name for the sheet |
| `jsOptsById` | object | No | Map of Qlik Sense object id to rendering options applied when generating the report. |
| `resizeType` | string | No | Currently only autofit is supported. If omitted, autofit is the default. The type of resize to be performed:   - none is used to export a visualization, sheet as is (e.g. normal size), regardless its size. This may result in cropping.   - autofit automatically fits the visualization, sheet into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.   - fit fits the visualization, sheet into the area specified in resizeData. The content will be rescaled to fit in that area.  Enum: "none", "fit", "autofit" |
| `patchesById` | object | No | Map of Qlik Sense object id to patches applied when generating the report. |
| `persistentBookmarkIncludeVariables` | boolean | No | Flag to configure the persistent bookmark to use variables |

</details>

</details>

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DLUsers` | array | No |  |
| `userIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `DLGroups` | array | No |  |
| `groupIds` | object[] | No | recipient object model that is directly persisted in the DB |
| `emailAddresses` | object[] | No | recipient object model that is directly persisted in the DB |
| `netRecipientCount` | integer | No | Net count of recipients in DLGroups and DLUsers. |

<details>
<summary>Properties of `userIds`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | User ID of recipient (internal user). |
| `groups` | string[] | No | A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included |
| `subscribed` | boolean | No | Whether this user is subscribed to alerts in this task |
| `enabledByUser` | boolean | No | Whether this recipient can receive alerts, set by api calls. |
| `enabledBySystem` | boolean | No | Whether this recipient can receive alerts, set by external settings. |
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
| `enabledByUser` | boolean | No | Whether this recipient can receive alerts, set by api calls. |
| `enabledBySystem` | boolean | No | Whether this recipient can receive alerts, set by external settings. |
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

<details>
<summary>Properties of `emailAddresses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Email of recipient (external user). |
| `enabled` | boolean | No | Whether this recipient can receive alerts. |
| `taskRecipientErrors` | object[] | No |  |

<details>
<summary>Properties of `taskRecipientErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `taskErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | string | No | Identifier for type of error occurring on sharing task Enum: "OWNER_DISABLED", "OWNER_ACCESS", "OWNER_LICENSE", "APP_DELETED", "NO_RECIPIENTS", "PARTIAL_ACCESS", "ORPHAN", "PARTIAL_SENT", "FATAL_SENT_ERROR", "SECTION_ACCESS_MODIFIED", "INVALID_DISTRIBUTION_LIST", "MAX_DL_RECIPIENTS_LIMIT_REACHED", "TEMPLATE_NOT_FOUND", "REPORTING_BOOKMARK_NOT_FOUND", "DATA_CONNECTION_NOT_FOUND", "INVALID_SHAREPOINT_DIRECTORY", "GENERIC_FILE_UPLOAD_ERROR", "DISABLED_DUE_TO_OWNERSHIP_CHANGE", "REPORTING_CONSUMPTION_EXCEEDED", "REPORTING_CAPABILITY_NOT_FOUND", "EXECUTION_TIME_OUT", "OWNER_INSUFFICIENT_PERMISSIONS", "MAX_UNIQUE_REPORTS_LIMIT_REACHED", "MISSING_DISTRIBUTION_LIST", "SECTION_ACCESS_NOT_SUPPORTED", "REPORTING_DAILY_QUOTA_EXCEEDED", "EMAIL_DELIVERY_FAILURE" |
| `timestamp` | string | No | Timestamp for the creation of the error |

</details>

<details>
<summary>Properties of `emailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | Body content of the email sent to recipients. |
| `subject` | string | No | Subject line of the email sent to recipients. |

</details>

<details>
<summary>Properties of `encryptedState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `retentionPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `historySize` | integer | No | Number indicating the size of the window which stores the history. For Chart monitoring, the size should be 10. |
| `overrideInterval` | string | No | Using RFC-5545 provide the time interval in which the previous generated can be overridden with the newly generated report. For Chart monitoring, interval should be FREQ=DAILY;INTERVAL=1 |

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
<summary>Properties of `multiInsightURLs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | the status of the creation for this insight URL Enum: "successful", "failed" |
| `directURL` | string | No |  |
| `insightID` | string | No |  |
| `resourceID` | string | No | an identifier for the object within the template that this insight link points to |
| `templateID` | string | No | _(deprecated)_ an identifier for the template that this insight link points to |
| `fallbackURL` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedTemplates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `encryptedEmailContent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | object | No | Encrypted property in DB |
| `subject` | object | No | Encrypted property in DB |

<details>
<summary>Properties of `body`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

<details>
<summary>Properties of `subject`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | any | No |  |
| `cipher` | string | No |  |

</details>

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "type": "chart-monitoring",
  "appId": "string",
  "owner": "pXVNKqotgEMwbKwhz2agPE4yFelnPcWO",
  "state": {
    "fields": [
      {}
    ],
    "queryItems": [
      {}
    ],
    "selections": [
      {
        "name": "Country",
        "values": [
          "Germany"
        ],
        "isNumeric": false,
        "stateName": "$",
        "displayName": "Country",
        "displayValues": [
          "Germany"
        ]
      }
    ]
  },
  "tenant": "_mpoXaH22_vLR1pStfI7oUdGya1nKK24",
  "appName": "string",
  "lastRun": "2019-10-15T16:07:01.492Z",
  "message": "Look at the presentation.",
  "spaceId": "string",
  "subType": "pdf",
  "trigger": {
    "recurrence": [
      "RRULE:FREQ=WEEKLY;INTERVAL=1"
    ],
    "chronosJobID": "chronos-job-123",
    "executeOnAppReload": true,
    "executionHistoryInterval": "daily"
  },
  "createdBy": "string",
  "insightID": "string",
  "ownerName": "Harley Kiffe",
  "startTime": "2019-10-15T16:07:01.492Z",
  "templates": [
    {
      "type": "file",
      "subType": "image",
      "fileName": "sales-report",
      "chartData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "jsOpts": {},
        "outDpi": 96,
        "outZoom": 1,
        "patches": [
          {}
        ],
        "sheetId": "bdf2efee-815e-4eb7-9e1e-asdfasdfasdf",
        "widthPx": 1584,
        "heightPx": 587,
        "objectId": "167f3e67-ff3b-4ead-a09e-e8cc81d8ad78",
        "objectDef": {},
        "persistentBookmarkIncludeVariables": true
      },
      "fileAlias": "file1",
      "sheetData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "jsOpts": {},
        "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
        "widthPx": 1584,
        "heightPx": 587,
        "isPrivate": false,
        "sheetName": "My new sheet",
        "jsOptsById": {},
        "patchesById": {}
      },
      "storyData": {
        "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
        "storyId": "39a671a-5f58-468c-bb49-dff933294774"
      },
      "templateId": "da5825325dc9a0dd0260af9",
      "fileTimeStamp": "yyyy-MM-dd",
      "multiSheetData": [
        {
          "appId": "bdf2efee-815e-4eb7-9e1e-c42d516baf29",
          "jsOpts": {},
          "sheetId": "39a671a-5f58-468c-bb49-dff933294774",
          "widthPx": 1584,
          "heightPx": 587,
          "isPrivate": false,
          "sheetName": "My new sheet",
          "jsOptsById": {},
          "resizeType": "none",
          "patchesById": {},
          "persistentBookmarkIncludeVariables": true
        }
      ]
    }
  ],
  "thumbnail": "string",
  "updatedBy": "string",
  "expiration": "2019-10-15T16:07:01.492Z",
  "lastViewed": "2019-10-15T16:07:01.492Z",
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
        "subscribed": true,
        "enabledByUser": true,
        "enabledBySystem": true,
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
    "groupIds": [
      {
        "value": "group1",
        "enabledByUser": true,
        "enabledBySystem": true,
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
    ],
    "emailAddresses": [
      {
        "value": "abc@xyz.com",
        "enabled": true,
        "taskRecipientErrors": [
          {
            "value": "NO_ACCESS_TO_APP",
            "timestamp": "2019-10-15T16:07:01.492Z"
          }
        ]
      }
    ],
    "netRecipientCount": 10
  },
  "statusCode": "CHART_NOT_FOUND",
  "taskErrors": [
    {
      "value": "OWNER_DISABLED",
      "timestamp": "2019-10-15T16:07:01.492Z"
    }
  ],
  "templateId": "da5825325dc9a0dd0260af9",
  "dateCreated": "2019-10-15T16:07:01.492Z",
  "description": "string",
  "lastUpdated": "2019-10-15T16:07:01.492Z",
  "statusLabel": "string",
  "emailContent": {
    "body": "report body string",
    "subject": "report subject"
  },
  "enabledByUser": true,
  "encryptedState": {
    "cipher": "string"
  },
  "byokMigrationId": "string",
  "enabledBySystem": true,
  "retentionPolicy": {
    "historySize": 10,
    "overrideInterval": "FREQ=DAILY;INTERVAL=1"
  },
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
  "selectionErrors": {},
  "dataConnectionID": "string",
  "hasSectionAccess": true,
  "insightDirectURL": "string",
  "multiInsightURLs": [
    {
      "status": "successful",
      "directURL": "string",
      "insightID": "string",
      "resourceID": "string",
      "templateID": "string",
      "fallbackURL": "string"
    }
  ],
  "nextScheduledRun": "2019-10-15T16:07:01.492Z",
  "reportProperties": {},
  "sharePointFolder": "string",
  "executeOnCreation": true,
  "lastExecutionDate": "2019-10-15T16:09:01.492Z",
  "transportChannels": [
    "email"
  ],
  "distributionListId": "vXVNKqotgEMwbKwhz2agPE4yFelnPcWX",
  "encryptedTemplates": {
    "cipher": "string"
  },
  "insightFallbackURL": "string",
  "encryptedEmailContent": {
    "body": {
      "cipher": "string"
    },
    "subject": {
      "cipher": "string"
    }
  },
  "failedExecutionsCount": 42,
  "failedVerificationsCount": 42,
  "isCandidateForVerification": true,
  "persistentBookmarkIncludeVariables": true,
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "enabled": true,
  "latestExecutionURL": "string",
  "latestExecutionFilesURL": [
    "string"
  ]
}
```

---

### PATCH /api/v1/sharing-tasks/{taskId}

Updates one or more properties of a specific sharing task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Request Body

**Required**

The sharing task definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed Enum: "replace", "remove" |
| `path` | string | Yes | A JSON Patch document as defined in http://tools.ietf.org/html/rfc6902 Enum: "/name", "/tags", "/ownerId", "/enabled", "/description", "/scheduleOptions", "/templates", "/recipients", "/recipient", "/sharePointFolder", "/dataConnectionID", "/transportChannels", "/bookmarkId" |
| `value` | object | No | The value to be used for this operation. |

#### Responses

##### 204

The sharing task has been successfully updated.

##### 400

The specified task ID or body is invalid (e.g. not a number).

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

A task with the specified ID was not found.

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
// qlik-api has not implemented support for `PATCH /api/v1/sharing-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'new name',
      },
      {
        op: 'replace',
        path: '/tags',
        value: ['tag1', 'tag2'],
      },
      {
        op: 'replace',
        path: '/tags',
        value: 'new-tag',
      },
      {
        op: 'replace',
        path: '/tags',
        value: 'deleted-tag',
      },
      {
        op: 'replace',
        path: '/ownerId',
        value: 'new-owner',
      },
      {
        op: 'replace',
        path: '/enabled',
        value: true,
      },
      {
        op: 'replace',
        path: '/description',
        value: 'new-description',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/sharing-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"new name"},{"op":"replace","path":"/tags","value":["tag1","tag2"]},{"op":"replace","path":"/tags","value":"new-tag"},{"op":"replace","path":"/tags","value":"deleted-tag"},{"op":"replace","path":"/ownerId","value":"new-owner"},{"op":"replace","path":"/enabled","value":true},{"op":"replace","path":"/description","value":"new-description"}]'
```

---

### DELETE /api/v1/sharing-tasks/{taskId}

Deletes a specific sharing task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Responses

##### 204

The sharing task has been successfully deleted.

##### 400

The specified task ID is invalid (e.g. not a number).

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

A task with the specified ID was not found.

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
// qlik-api has not implemented support for `DELETE /api/v1/sharing-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/sharing-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/sharing-tasks/{taskId}/actions/cancel

Requests cancellation of an execution of the specified recurring sharing task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Responses

##### 204

The sharing task has been successfully cancelled.

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

Task not found, if the provided sharing task cannot be found or otherwise unable to be cancelled

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
// qlik-api has not implemented support for `POST /api/v1/sharing-tasks/{taskId}/actions/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}/actions/cancel',
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
# qlik-cli has not implemented support for POST /api/v1/sharing-tasks/{taskId}/actions/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}/actions/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/v1/sharing-tasks/{taskId}/executions

Lists executions for the specified sharing task.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | No | Limit the returned result set |
| `next` | string | No | The cursor to the next page of data. Only one of next or previous may be specified. |
| `offset` | integer | No | Offset for pagination - how many elements to skip |
| `prev` | string | No | The cursor to the previous page of data. Only one of next or previous may be specified. |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "starttime", "-starttime", "+starttime" |
| `status` | string | No | Specifies a filter for a particular field and value of an execution Enum: "successful", "failed" |

#### Responses

##### 200

The sharing-executions list has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `links` | object | No |  |
| `executions` | object[] | No | Gets a list of sharing-executions. |

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
| `appId` | string | No | appId associated to sharing task execution |
| `files` | object[] | No |  |
| `errors` | object[] | No |  |
| `status` | string | No | Status of the task execution Enum: "initialized", "in-progress", "successful", "failed", "cancelled", "invalid", "presuccessful", "cancelling" |
| `endTime` | string | No | Timestamp of execution successful stop |
| `eventID` | string | No | eventID of the trigger NATS event |
| `ownerId` | string | No | Owner of the execution |
| `reloadId` | string | No | If this execution was triggered by an app reload. This will contain the reloadId from reloads service. Otherwise it is empty or omitted. |
| `tenantId` | string | No | The tenant that this execution belongs to |
| `eventTime` | string | No | eventTime of the trigger NATS event |
| `startTime` | string | No | Timestamp of execution start |
| `bookmarkId` | string | No | _(deprecated)_ The ID of a filter in a reporting request |
| `failedTime` | string | No | Timestamp of execution stop |
| `reloadTime` | string | No | If this execution was triggered by an app reload. This will contain the reload time to compare with reporting service when the report is requested. |
| `targetUser` | object | No | User that this execution is targeting as a recipient |
| `totalCount` | integer | No | Total count of reports in this execution |
| `workflowID` | string | No | Workflow that the execution belongs to. Note that in a multi-recipient context we can have multiple executions (one per recipient) that share the same unique workflow. |
| `bookmarkIds` | string[] | No | The ID of a filter in a reporting request |
| `failedCount` | integer | No | Total count of failed reports in this execution |
| `successCount` | integer | No | Total count of successfully generated reports in this execution |
| `cancelledTime` | string | No | Timestamp of execution cancel |
| `sharingTaskID` | string | No | ID for the sharing task that this execution references |
| `cancelledCount` | integer | No | Total count of cancelled reports in this execution |
| `totalUploadCount` | integer | No | Total count of reports to be uploaded in this execution |
| `failedUploadCount` | integer | No | Total count of failed uploaded reports in this execution |
| `successUploadCount` | integer | No | Total count of successfully uploaded reports in this execution |
| `links` | object | No |  |
| `fileLocations` | string[] | No |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "image", "pdf", "pptx", "xlsx", "html", "docx" |
| `fileID` | string | No |  |
| `userId` | string | No | userId associated with the file |
| `fileAlias` | string | No |  |
| `templateId` | string | No | identify the source task template |
| `tempContentsLocation` | string | No |  |

</details>

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `targetUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | type of user eg email, userId, groupId |
| `value` | string | No | contains the value of user type e.g. abc@xyz.com, 213efewr3 |
| `timezone` | string | No | timezone for the timestamp on the attached file name |
| `filterName` | string | No | _(deprecated)_ |
| `filterNames` | string[] | No | contains the value of the user filter |

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks/{taskId}/executions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}/executions',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks/{taskId}/executions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}/executions" \
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
      "appId": "string",
      "files": [
        {
          "type": "image",
          "fileID": "za1b2c3d4z",
          "userId": "string",
          "fileAlias": "small-image",
          "templateId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
          "tempContentsLocation": "string"
        }
      ],
      "errors": [
        {
          "code": "string",
          "title": "string",
          "detail": "string"
        }
      ],
      "status": "initialized",
      "endTime": "string",
      "eventID": "string",
      "ownerId": "string",
      "reloadId": "string",
      "tenantId": "string",
      "eventTime": "string",
      "startTime": "string",
      "bookmarkId": "string",
      "failedTime": "string",
      "reloadTime": "string",
      "targetUser": {
        "type": "string",
        "value": "string",
        "timezone": "string",
        "filterName": "string",
        "filterNames": [
          "string"
        ]
      },
      "totalCount": 42,
      "workflowID": "string",
      "bookmarkIds": [
        "string"
      ],
      "failedCount": 42,
      "successCount": 42,
      "cancelledTime": "string",
      "sharingTaskID": "string",
      "cancelledCount": 42,
      "totalUploadCount": 42,
      "failedUploadCount": 42,
      "successUploadCount": 42,
      "links": {
        "self": {
          "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
        }
      },
      "fileLocations": [
        "string"
      ]
    }
  ]
}
```

---

### GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}

Retrieves a specific sharing task execution.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `executionId` | string | Yes | The execution identifier. If value is "latest", the latest execution will be returned |
| `taskId` | string | Yes | The sharing task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Filter by status. If not present then no filtering is done on the status. This is only relevant when requesting latest execution. Enum: "successful", "failed", "cancelled" |

#### Responses

##### 200

The execution has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Gets the execution identifier. |
| `appId` | string | No | appId associated to sharing task execution |
| `files` | object[] | No |  |
| `errors` | object[] | No |  |
| `status` | string | No | Status of the task execution Enum: "initialized", "in-progress", "successful", "failed", "cancelled", "invalid", "presuccessful", "cancelling" |
| `endTime` | string | No | Timestamp of execution successful stop |
| `eventID` | string | No | eventID of the trigger NATS event |
| `ownerId` | string | No | Owner of the execution |
| `reloadId` | string | No | If this execution was triggered by an app reload. This will contain the reloadId from reloads service. Otherwise it is empty or omitted. |
| `tenantId` | string | No | The tenant that this execution belongs to |
| `eventTime` | string | No | eventTime of the trigger NATS event |
| `startTime` | string | No | Timestamp of execution start |
| `bookmarkId` | string | No | _(deprecated)_ The ID of a filter in a reporting request |
| `failedTime` | string | No | Timestamp of execution stop |
| `reloadTime` | string | No | If this execution was triggered by an app reload. This will contain the reload time to compare with reporting service when the report is requested. |
| `targetUser` | object | No | User that this execution is targeting as a recipient |
| `totalCount` | integer | No | Total count of reports in this execution |
| `workflowID` | string | No | Workflow that the execution belongs to. Note that in a multi-recipient context we can have multiple executions (one per recipient) that share the same unique workflow. |
| `bookmarkIds` | string[] | No | The ID of a filter in a reporting request |
| `failedCount` | integer | No | Total count of failed reports in this execution |
| `successCount` | integer | No | Total count of successfully generated reports in this execution |
| `cancelledTime` | string | No | Timestamp of execution cancel |
| `sharingTaskID` | string | No | ID for the sharing task that this execution references |
| `cancelledCount` | integer | No | Total count of cancelled reports in this execution |
| `totalUploadCount` | integer | No | Total count of reports to be uploaded in this execution |
| `failedUploadCount` | integer | No | Total count of failed uploaded reports in this execution |
| `successUploadCount` | integer | No | Total count of successfully uploaded reports in this execution |
| `links` | object | No |  |
| `fileLocations` | string[] | No |  |

<details>
<summary>Properties of `files`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | Enum: "image", "pdf", "pptx", "xlsx", "html", "docx" |
| `fileID` | string | No |  |
| `userId` | string | No | userId associated with the file |
| `fileAlias` | string | No |  |
| `templateId` | string | No | identify the source task template |
| `tempContentsLocation` | string | No |  |

</details>

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

</details>

<details>
<summary>Properties of `targetUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | type of user eg email, userId, groupId |
| `value` | string | No | contains the value of user type e.g. abc@xyz.com, 213efewr3 |
| `timezone` | string | No | timezone for the timestamp on the attached file name |
| `filterName` | string | No | _(deprecated)_ |
| `filterNames` | string[] | No | contains the value of the user filter |

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}/executions/{executionId}',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks/{taskId}/executions/{executionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}/executions/{executionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "appId": "string",
  "files": [
    {
      "type": "image",
      "fileID": "za1b2c3d4z",
      "userId": "string",
      "fileAlias": "small-image",
      "templateId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
      "tempContentsLocation": "string"
    }
  ],
  "errors": [
    {
      "code": "string",
      "title": "string",
      "detail": "string"
    }
  ],
  "status": "initialized",
  "endTime": "string",
  "eventID": "string",
  "ownerId": "string",
  "reloadId": "string",
  "tenantId": "string",
  "eventTime": "string",
  "startTime": "string",
  "bookmarkId": "string",
  "failedTime": "string",
  "reloadTime": "string",
  "targetUser": {
    "type": "string",
    "value": "string",
    "timezone": "string",
    "filterName": "string",
    "filterNames": [
      "string"
    ]
  },
  "totalCount": 42,
  "workflowID": "string",
  "bookmarkIds": [
    "string"
  ],
  "failedCount": 42,
  "successCount": 42,
  "cancelledTime": "string",
  "sharingTaskID": "string",
  "cancelledCount": 42,
  "totalUploadCount": 42,
  "failedUploadCount": 42,
  "successUploadCount": 42,
  "links": {
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  },
  "fileLocations": [
    "string"
  ]
}
```

---

### GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}

Retrieves the file content for the requested execution and file type.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `executionId` | string | Yes | The execution identifier. |
| `fileAlias` | string | Yes | The execution identifier. If value is "latest", the latest execution will be returned |
| `taskId` | string | Yes | The sharing task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Filter by status. If not present then no filtering is done on the status. This is only relevant when requesting latest execution. Enum: "successful", "failed", "cancelled" |

#### Responses

##### 200

The content of the file has been successfully returned.

**Content-Type:** `image/png`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `image/png` | string | No |  |

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | string | No |  |

##### 404

A task or execution with the specified ID was not found.

**Content-Type:** `image/png`

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

**Content-Type:** `image/png`

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

**Content-Type:** `image/png`

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
"string"
```

---

### POST /api/v1/sharing-tasks/actions/execute

Requests execution of the specified recurring sharing task.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The sharing task execute request definition.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingTaskID` | string | Yes | Identifier of the sharing task to trigger. |

#### Responses

##### 204

The sharing task has been successfully set up for execution.

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

Task not found, if the provided sharing task cannot be found or otherwise unable to be executed

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
// qlik-api has not implemented support for `POST /api/v1/sharing-tasks/actions/execute` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/actions/execute',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      sharingTaskID: 'a1b2c3d4f5',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/sharing-tasks/actions/execute yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/actions/execute" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"sharingTaskID":"a1b2c3d4f5"}'
```

---

### GET /api/v1/sharing-tasks/settings

Retrieves the current settings for sharing tasks, reports, and other related configuration.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The sharing settings have been successfully returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tenantId` | string | No | These persisted sharing settings are only available for this tenant. Extracted from request JWT. |
| `maxRecipients` | number | No | Maximum number of recipients when creating a sharing task |
| `enable-sharing` | boolean | No | Whether API endpoints for sharing are enabled |
| `reportSubscriptionStatus` | string | No | This indicates that there is an ongoing operation to either disable or enable the report subscription feature. none means that no such operation is ongoing. enabling/disabling means that system is currently enabling/disabling the feature Enum: "none", "enabling", "disabling" |
| `maxSubscriptionRecipients` | integer | No | Max Recipients accepted when creating a new subscription (excluding the owner) |
| `enable-report-subscription` | boolean | No | true if report-subscription feature is enabled for this tenant |
| `reporting-service-license-status` | string | No | Whether the license for the tenant has the reportingService feature enabled. Enum: "enabled", "disabled" |
| `reportSubscriptionStatusChangeTime` | string | No | UTC timestamp of the most recent change of reportSubscriptionStatus. If there has not been any such change, this is the timestamp of the initial creation of the record. |

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
// qlik-api has not implemented support for `GET /api/v1/sharing-tasks/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/settings',
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
# qlik-cli has not implemented support for GET /api/v1/sharing-tasks/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/settings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "tenantId": "cgdsAumGmQ6l0Bi7CUKt9V8P_Y9GL0sC",
  "maxRecipients": 200,
  "enable-sharing": true,
  "reportSubscriptionStatus": "disabling",
  "maxSubscriptionRecipients": 42,
  "enable-report-subscription": true,
  "reporting-service-license-status": "enabled",
  "reportSubscriptionStatusChangeTime": "2020-09-02T13:44:33Z"
}
```

---

### PATCH /api/v1/sharing-tasks/settings

Patches the toggle settings for sharing tasks, reports, and other related configuration in the tenant. User must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Request for updating the API settings

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/enable-sharing", "/enable-report-subscription" |
| `value` | object | No | The value to be used for this operation. |

#### Responses

##### 204

Sharing settings have been successfully updated.

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
// qlik-api has not implemented support for `PATCH /api/v1/sharing-tasks/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/settings',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/enable-sharing',
        value: true,
      },
      {
        op: 'replace',
        path: '/enable-sharing',
        value: false,
      },
      {
        op: 'replace',
        path: '/enable-report-subscription',
        value: true,
      },
      {
        op: 'replace',
        path: '/enable-report-subscription',
        value: false,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/sharing-tasks/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/settings" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/enable-sharing","value":true},{"op":"replace","path":"/enable-sharing","value":false},{"op":"replace","path":"/enable-report-subscription","value":true},{"op":"replace","path":"/enable-report-subscription","value":false}]'
```

---

### PUT /api/v1/sharing-tasks/settings

Updates the settings for sharing tasks, reports, and other related configuration in the tenant. User must be assigned the `TenantAdmin` role.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

Request for updating the API settings

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `enable-sharing` | boolean | Yes | Whether API endpoints for sharing are enabled |

#### Responses

##### 204

API settings have been successfully updated.

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
// qlik-api has not implemented support for `PUT /api/v1/sharing-tasks/settings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/sharing-tasks/settings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'enable-sharing': true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/sharing-tasks/settings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks/settings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"enable-sharing":true}'
```

---
