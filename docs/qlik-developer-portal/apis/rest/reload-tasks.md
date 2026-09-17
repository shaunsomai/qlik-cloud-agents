# Reload tasks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Reloads tasks allow you to schedule reloads of analytics applications in your tenant.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/reload-tasks`](#get-apiv1reload-tasks) | Finds and returns the tasks that the user has access to. |
| `POST` | [`/api/v1/reload-tasks`](#post-apiv1reload-tasks) | Creates a task for a specified app. |
| `GET` | [`/api/v1/reload-tasks/{taskId}`](#get-apiv1reload-taskstaskid) | Finds and returns a task. |
| `PUT` | [`/api/v1/reload-tasks/{taskId}`](#put-apiv1reload-taskstaskid) | Updates an existing task |
| `DELETE` | [`/api/v1/reload-tasks/{taskId}`](#delete-apiv1reload-taskstaskid) | Deletes a task |

## API Reference

### GET /api/v1/reload-tasks _(deprecated)_

Finds and returns the tasks that the user has access to.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. This endpoint is deprecated and will be removed after 2026-09. Use the `/scheduling/tasks` endpoint instead.

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | The case sensitive string used to search for a task by app ID. |
| `limit` | integer | No | The maximum number of resources to return for a request. The limit must be an integer between 1 and 100 (inclusive). |
| `next` | string | No | The cursor to the next page of resources. Provide either the next or prev cursor, but not both. |
| `partial` | boolean | No | The boolean value used to search for a task is partial or not |
| `prev` | string | No | The cursor to the previous page of resources. Provide either the next or prev cursor, but not both. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 200

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes |  |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | Yes | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `id` | string | Yes | The ID of the task. |
| `log` | string | No | _(deprecated)_ The reason why the task was disabled. |
| `links` | object | Yes |  |
| `state` | string | Yes | Toggle for enabling and disabling the reload task Enum: "Enabled", "Disabled", "Completed" |
| `userId` | string | Yes | The ID of the user who owns the task. |
| `spaceId` | string | No | The space ID of the application |
| `migrated` | boolean | No | A flag indicating whether the task has been migrated to the new scheduling service. |
| `tenantId` | string | Yes | The ID of the tenant who owns the task. |
| `fortressId` | string | No | _(deprecated)_ The fortress ID of the application |
| `disabledCode` | string | No | The reason why the task was disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "OWNER-DELETED", "OWNER-DISABLED" |
| `lastExecutionTime` | string | No | The last time the task executed. |
| `nextExecutionTime` | string | No | The next time the task will execute. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |
| `next` | object | No |  |
| `prev` | object | No |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for retrieval of this task.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 429

Too Many Requests.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 503

Service Unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reload-tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reload-tasks',
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
# qlik-cli has not implemented support for GET /api/v1/reload-tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
      "partial": false,
      "timeZone": "America/Toronto",
      "autoReload": false,
      "recurrence": [
        "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0",
        "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"
      ],
      "endDateTime": "2022-10-12T23:59:00",
      "startDateTime": "2022-09-19T11:18:00",
      "autoReloadPartial": false,
      "id": "5be59decca62aa00097268a4",
      "log": "Scheduled reload has been disabled since exceeded limit of 5 consecutive reload failures. Please fix error and re-enable schedule.",
      "links": {
        "self": {
          "href": "http://example.com"
        }
      },
      "state": "Enabled",
      "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
      "spaceId": "602c2c2be2be220002a22a22",
      "migrated": false,
      "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
      "fortressId": "5c5b097116d25a0001a48b06",
      "disabledCode": "CONSECUTIVE-FAILURES",
      "lastExecutionTime": "2022-09-20T17:17:00Z",
      "nextExecutionTime": "2022-09-20T17:17:00Z"
    }
  ],
  "links": {
    "self": {
      "href": "http://example.com"
    },
    "next": {
      "href": "http://example.com"
    },
    "prev": {
      "href": "http://example.com"
    }
  }
}
```

---

### POST /api/v1/reload-tasks _(deprecated)_

Creates a task for a specified app.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. This endpoint is deprecated and will be removed after 2026-09. Use the `/scheduling/tasks` endpoint instead.

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Request Body

**Required**

Request body specifying the task parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | Yes | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `type` | string | No | _(deprecated)_ Type of task being created - only contains the "scheduled_reload" value. Type value is not used for creating a schedule reload. It has been deprecated since 2022-04-05. Enum: "scheduled_reload" |

#### Responses

##### 201

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | Yes | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `id` | string | Yes | The ID of the task. |
| `log` | string | No | _(deprecated)_ The reason why the task was disabled. |
| `links` | object | Yes |  |
| `state` | string | Yes | Toggle for enabling and disabling the reload task Enum: "Enabled", "Disabled", "Completed" |
| `userId` | string | Yes | The ID of the user who owns the task. |
| `spaceId` | string | No | The space ID of the application |
| `migrated` | boolean | No | A flag indicating whether the task has been migrated to the new scheduling service. |
| `tenantId` | string | Yes | The ID of the tenant who owns the task. |
| `fortressId` | string | No | _(deprecated)_ The fortress ID of the application |
| `disabledCode` | string | No | The reason why the task was disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "OWNER-DELETED", "OWNER-DISABLED" |
| `lastExecutionTime` | string | No | The last time the task executed. |
| `nextExecutionTime` | string | No | The next time the task will execute. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for retrieval of this task.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 503

Service Unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/reload-tasks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reload-tasks',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      appId:
        '116dbfae-7fb9-4983-8e23-5ccd8c508722',
      partial: false,
      timeZone: 'America/Toronto',
      autoReload: false,
      recurrence: [
        'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0',
        'RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0',
      ],
      endDateTime: '2022-10-12T23:59:00',
      startDateTime: '2022-09-19T11:18:00',
      autoReloadPartial: false,
      type: 'scheduled_reload',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/reload-tasks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks" \
-X POST \
-H "Authorization: Bearer <access_token>" \
-H "Content-type: application/json" \
-d '{"appId":"116dbfae-7fb9-4983-8e23-5ccd8c508722","partial":false,"timeZone":"America/Toronto","autoReload":false,"recurrence":["RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0","RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"],"endDateTime":"2022-10-12T23:59:00","startDateTime":"2022-09-19T11:18:00","autoReloadPartial":false,"type":"scheduled_reload"}'
```

**Example Response:**

```json
{
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "partial": false,
  "timeZone": "America/Toronto",
  "autoReload": false,
  "recurrence": [
    "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0",
    "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"
  ],
  "endDateTime": "2022-10-12T23:59:00",
  "startDateTime": "2022-09-19T11:18:00",
  "autoReloadPartial": false,
  "id": "5be59decca62aa00097268a4",
  "log": "Scheduled reload has been disabled since exceeded limit of 5 consecutive reload failures. Please fix error and re-enable schedule.",
  "links": {
    "self": {
      "href": "http://example.com"
    }
  },
  "state": "Enabled",
  "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
  "spaceId": "602c2c2be2be220002a22a22",
  "migrated": false,
  "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
  "fortressId": "5c5b097116d25a0001a48b06",
  "disabledCode": "CONSECUTIVE-FAILURES",
  "lastExecutionTime": "2022-09-20T17:17:00Z",
  "nextExecutionTime": "2022-09-20T17:17:00Z"
}
```

---

### GET /api/v1/reload-tasks/{taskId} _(deprecated)_

Finds and returns a task.

- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. This endpoint is deprecated and will be removed after 2026-09. Use the `/scheduling/tasks/{id}` endpoint instead.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The unique identifier of the task. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 200

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | Yes | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `id` | string | Yes | The ID of the task. |
| `log` | string | No | _(deprecated)_ The reason why the task was disabled. |
| `links` | object | Yes |  |
| `state` | string | Yes | Toggle for enabling and disabling the reload task Enum: "Enabled", "Disabled", "Completed" |
| `userId` | string | Yes | The ID of the user who owns the task. |
| `spaceId` | string | No | The space ID of the application |
| `migrated` | boolean | No | A flag indicating whether the task has been migrated to the new scheduling service. |
| `tenantId` | string | Yes | The ID of the tenant who owns the task. |
| `fortressId` | string | No | _(deprecated)_ The fortress ID of the application |
| `disabledCode` | string | No | The reason why the task was disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "OWNER-DELETED", "OWNER-DISABLED" |
| `lastExecutionTime` | string | No | The last time the task executed. |
| `nextExecutionTime` | string | No | The next time the task will execute. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for creation or retrieval of this engine session.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 429

Too Many Requests.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 503

Service Unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reload-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reload-tasks/{taskId}',
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
# qlik-cli has not implemented support for GET /api/v1/reload-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks/{taskId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "partial": false,
  "timeZone": "America/Toronto",
  "autoReload": false,
  "recurrence": [
    "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0",
    "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"
  ],
  "endDateTime": "2022-10-12T23:59:00",
  "startDateTime": "2022-09-19T11:18:00",
  "autoReloadPartial": false,
  "id": "5be59decca62aa00097268a4",
  "log": "Scheduled reload has been disabled since exceeded limit of 5 consecutive reload failures. Please fix error and re-enable schedule.",
  "links": {
    "self": {
      "href": "http://example.com"
    }
  },
  "state": "Enabled",
  "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
  "spaceId": "602c2c2be2be220002a22a22",
  "migrated": false,
  "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
  "fortressId": "5c5b097116d25a0001a48b06",
  "disabledCode": "CONSECUTIVE-FAILURES",
  "lastExecutionTime": "2022-09-20T17:17:00Z",
  "nextExecutionTime": "2022-09-20T17:17:00Z"
}
```

---

### PUT /api/v1/reload-tasks/{taskId} _(deprecated)_

Updates an existing task

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. This endpoint is deprecated and will be removed after 2026-09. Use the `/scheduling/tasks/{id}` endpoint instead.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The unique identifier of the task. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Request Body

**Required**

Request body specifying the task parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | No | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `state` | string | No | Toggle for enabling and disabling the reload task Enum: "Enabled", "Disabled", "Completed" |

#### Responses

##### 200

Expected response to a valid request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes | The ID of the app. |
| `partial` | boolean | No | The task is partial reload or not |
| `timeZone` | string | Yes | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format. |
| `autoReload` | boolean | No | A flag that indicates whether a reload is triggered when data of the app is changed |
| `recurrence` | string[] | No | List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events |
| `endDateTime` | string | No | The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. |
| `startDateTime` | string | No | The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set. |
| `autoReloadPartial` | boolean | No | A flag that indicates whether it is a partial reload or not for the auto reload |
| `id` | string | Yes | The ID of the task. |
| `log` | string | No | _(deprecated)_ The reason why the task was disabled. |
| `links` | object | Yes |  |
| `state` | string | Yes | Toggle for enabling and disabling the reload task Enum: "Enabled", "Disabled", "Completed" |
| `userId` | string | Yes | The ID of the user who owns the task. |
| `spaceId` | string | No | The space ID of the application |
| `migrated` | boolean | No | A flag indicating whether the task has been migrated to the new scheduling service. |
| `tenantId` | string | Yes | The ID of the tenant who owns the task. |
| `fortressId` | string | No | _(deprecated)_ The fortress ID of the application |
| `disabledCode` | string | No | The reason why the task was disabled. Enum: "MANUALLY", "CONSECUTIVE-FAILURES", "OWNER-DELETED", "OWNER-DISABLED" |
| `lastExecutionTime` | string | No | The last time the task executed. |
| `nextExecutionTime` | string | No | The next time the task will execute. |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes |  |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes |  |

</details>

</details>

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for creation or retrieval of this engine session.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 503

Service Unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/reload-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reload-tasks/{taskId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      appId:
        '116dbfae-7fb9-4983-8e23-5ccd8c508722',
      partial: false,
      timeZone: 'America/Toronto',
      autoReload: false,
      recurrence: [
        'RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0',
        'RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0',
      ],
      endDateTime: '2022-10-12T23:59:00',
      startDateTime: '2022-09-19T11:18:00',
      autoReloadPartial: false,
      state: 'Disabled',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/reload-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks/{taskId}" \
-X PUT \
-H "Authorization: Bearer <access_token>" \
-H "Content-type: application/json" \
-d '{"appId":"116dbfae-7fb9-4983-8e23-5ccd8c508722","partial":false,"timeZone":"America/Toronto","autoReload":false,"recurrence":["RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0","RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"],"endDateTime":"2022-10-12T23:59:00","startDateTime":"2022-09-19T11:18:00","autoReloadPartial":false,"state":"Disabled"}'
```

**Example Response:**

```json
{
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "partial": false,
  "timeZone": "America/Toronto",
  "autoReload": false,
  "recurrence": [
    "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=11;BYMINUTE=18;BYSECOND=0",
    "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TU;BYHOUR=13;BYMINUTE=17;BYSECOND=0"
  ],
  "endDateTime": "2022-10-12T23:59:00",
  "startDateTime": "2022-09-19T11:18:00",
  "autoReloadPartial": false,
  "id": "5be59decca62aa00097268a4",
  "log": "Scheduled reload has been disabled since exceeded limit of 5 consecutive reload failures. Please fix error and re-enable schedule.",
  "links": {
    "self": {
      "href": "http://example.com"
    }
  },
  "state": "Enabled",
  "userId": "FyPG6xWp6prDU6BXQ3g7LY9gWR_YRkkx",
  "spaceId": "602c2c2be2be220002a22a22",
  "migrated": false,
  "tenantId": "efSCcpNYuayTysONkUcE3F80zYQ_LV9w",
  "fortressId": "5c5b097116d25a0001a48b06",
  "disabledCode": "CONSECUTIVE-FAILURES",
  "lastExecutionTime": "2022-09-20T17:17:00Z",
  "nextExecutionTime": "2022-09-20T17:17:00Z"
}
```

---

### DELETE /api/v1/reload-tasks/{taskId} _(deprecated)_

Deletes a task

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-09. This endpoint is deprecated and will be removed after 2026-09. Use the `/scheduling/tasks/{id}` endpoint instead.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The unique identifier of the task. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | JWT containing tenant credentials. |

#### Responses

##### 204

Task deleted successfully.

##### 400

Bad Request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 403

Forbidden, the requesting JWT does not allow for creation or retrieval of this engine session.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

##### 404

Not Found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

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
| `code` | string | Yes |  |
| `title` | string | Yes |  |
| `detail` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/reload-tasks/{taskId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reload-tasks/{taskId}',
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
# qlik-cli has not implemented support for DELETE /api/v1/reload-tasks/{taskId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks/{taskId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---
