---
source: https://qlik.dev/manage/analytics-applications/migrate-reload-tasks-to-tasks/
last_updated: 2026-04-20T13:34:03+01:00
---

# Migrate reload tasks to the new Tasks API

## Overview

This guide helps you migrate your existing [reload tasks](https://qlik.dev/apis/rest/reload-tasks/) to the new [Tasks API](https://qlik.dev/apis/rest/tasks/).

## Step 1: Locate your existing reload task

First, you need to retrieve the details for the reload task that you want to migrate.
Replace `<TENANT>` with the hostname for your tenant:

```bash
curl -X GET https://<TENANT>/api/v1/reload-tasks ^
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Example response for a scheduled reload task:

```json
{
    "id": "67ffd32c08e939e2f3a31184",
    "partial": false,
    "autoReload": false,
    "autoReloadPartial": false,
    "tenantId": "TwX68dLFX3GS1GXXSoIkTtz4Coa-pp2x",
    "userId": "67890d4f54918fed2faa2df5",
    "appId": "659fb48b-85eb-4ec9-bb06-9527691f998c",
    "fortressId": "",
    "log": "",
    "disabledCode": "",
    "spaceId": "67ffd1a958505bf21fd86284",
    "startDateTime": "2025-04-17T06:00:00",
    "recurrence": [
        "RRULE:FREQ=HOURLY;BYHOUR=10;BYMINUTE=20"
    ],
    "timeZone": "UTC",
    "nextExecutionTime": "2025-04-17T10:20:00Z",
    "migrated": true,
    "links": {
        "self": {
            "href": "https://<TENANT>/api/v1/reload-tasks/67ffd32c08e939e2f3a31184"
        }
    }
}
```

Note the following fields for the task you want to migrate:

- `"id"` is the reload task ID.
- `"appId"` is the ID of the analytics app being reloaded. This value will be passed to the reload function in the new
  task.
- `"recurrence"`, `"startDateTime"`, `"endDateTime"`, and `"timeZone"`. For more information, see the
  [Reload tasks API reference documentation](https://qlik.dev/apis/rest/reload-tasks/#get-v1-reload-tasks).

## Step 2: Migrate the reload task

Call `POST /v1/tasks` using the `migrateFrom=<RELOAD_TASK_ID>` query parameter, and include the required task definition
fields in the request body:

- `name` sets the new task name.
- `specVersion` sets the serverless workflow version.
- `"enabled": true` enables the migrated task.
- `metadata.spaceId` sets the space ID where the task will operate.
- `metadata.usage` sets the product domain the resource is used.
- `"start"` defines the start workflow, which includes a `schedule` definition and a name (`stateName`).
- `"states"` defines an event-driven state that calls the `app.reload` function.

The `migrateFrom` query parameter tells the API to treat the new task as a migration from an existing reload task.

Example:

```bash
curl -X POST "https://<TENANT>/api/v1/tasks?migrateFrom=67ffd32c08e939e2f3a31184" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Content-Type: application/json" ^
  -d '{
    "name": "my-migrated-task",
    "specVersion": "0.8",
    "enabled": true,
    "metadata": {
      "spaceId": "67ffd1a958505bf21fd86284",
      "usage": "ANALYTICS"
    },
    "start": {
      "stateName": "reload",
      "schedule": {
        "recurrence": "RRULE:FREQ=HOURLY;BYHOUR=10;BYMINUTE=20",
        "startDateTime": "2025-04-17T06:00:00",
        "endDateTime": "2025-04-18T06:00:00",
        "timezone": "UTC"
      }
    },
    "states": [
      {
        "name": "reload",
        "type": "event",
        "onEvents": [
          {
            "eventRefs": [],
            "actions": [
              {
                "name": "reload-action",
                "functionRef": {
                  "refName": "app.reload",
                  "arguments": {
                    "appId": "659fb48b-85eb-4ec9-bb06-9527691f998c",
                    "partial": false
                  }
                }
              }
            ]
          }
        ],
        "end": true
      }
    ]
  }'
```

The following table includes common pitfalls to help you handle the migration correctly:

| Issue                              | Cause                                             | Fix                                                                                                                    |
| ---------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `task has 0 states instead of 1`   | The `"states"` array is missing or malformed      | Include a proper state with one action                                                                                 |
| `task has 0 Actions instead of 1`  | Missing `actions` under `onEvents`                | Add the `reload-action`                                                                                                |
| `Start has no StartdefOneOf field` | `"start"` is not a valid object                   | Use `{ "stateName": "reload", "schedule": {...} }`                                                                     |
| The task is not enabled            | You didn't explicitly enable the task             | Add `"enabled": true` in the request body when creating the task, or enable it afterwards calling `PUT /v1/tasks/{id}` |
| 403 error                          | You don't have the "reload" permission on the app | Make sure you have "reload" permission on the app                                                                      |

> **Warning:** After a task is created for an app using the new Tasks API, reload tasks are turned off for that app.
> Make sure the migration is complete before deleting the original reload task.

## Step 3: Test your migrated task

To test the migrated task, you can run it manually. Replace `<TENANT>` with the hostname for your tenant and `<TASK_ID>`
with your task ID:

```bash
curl -X POST https://<TENANT>/api/v1/tasks/<TASK_ID>/actions/start ^
  -H "Authorization: Bearer <token>"
```

If the task starts successfully, you'll get a response similar to the following one:

```json
{
    "status_code": 200,
    "code": "CHO-000",
    "message": "",
    "context": "StartTask",
    "timestamp": "2025-04-17T14:35:14.878521494Z",
    "value": null
}
```
