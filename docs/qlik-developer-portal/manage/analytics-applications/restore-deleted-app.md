---
source: https://qlik.dev/manage/analytics-applications/restore-deleted-app/
last_updated: 2026-06-18T10:08:14+01:00
---

# Restore a deleted analytics app

> **Warning:** App restoration is a disaster recovery pattern, not a recycle bin. Associated content
> such as collections, tags, data alerts, subscriptions, and notes is permanently lost
> and cannot be restored.

## Overview

When a Qlik Cloud analytics app is deleted and it was created more than 45 minutes
before deletion, it enters a soft delete state rather than being immediately and
permanently removed. A soft-deleted app retains its core content and can be restored
within 14 days.

Once restored, the app returns to its state at the point of deletion with the same app
ID. The app script and data model are intact, but associated content such as collections, tags,
data alerts, subscriptions, and notes is permanently lost and cannot be recovered.

Apps deleted within their first 45 minutes of creation are hard-deleted immediately
and cannot be restored.

If you are new to managing analytics applications, first read the
[analytics applications overview](https://qlik.dev/manage/analytics-applications).

## Before you begin

- The app ID (GUID) of the deleted app.
- A Qlik Cloud API key or OAuth access token. For more information, see
  [Authentication](https://qlik.dev/authenticate).
- To query deletion events: the `Tenant Admin` or `Audit Admin` role.
- To restore the app: the `Tenant Admin` role, or the app owner role provided the
  original space still exists and the owner retains delete permission in that space.

## Determine whether the app can be restored

Before attempting a restore, confirm that the app was soft-deleted and that the
14-day recovery window has not passed.

App deletion events represent different moments in the deletion lifecycle:

- `com.qlik.app.deleted`: Indicates that an app deletion occurred.
- `com.qlik.app.softdeleted`: Indicates that the app entered the recovery window and
  includes the `purgeAt` field.
- `com.qlik.app.harddeleted`: Indicates that the app was permanently deleted and
  cannot be restored.

Use one of the following options to inspect the event data.

### Option 1: Check the event data in the Administration activity center

Use this option for a manual check.

1. Go to the **Administration activity center** and select **Events**.
2. Locate the `com.qlik.app.deleted` event for the app. Use the event type, time, and
   user columns to help identify the relevant event.
3. Expand the event row.
4. Verify that the `id` field in the event data matches your app ID.
5. Check the `deleteType` field:
   - If `deleteType` is `SOFT`, the app entered the recovery window.
   - If `deleteType` is `HARD`, the app was hard-deleted and cannot be restored.
6. If `deleteType` is `SOFT`, locate and expand the related
   `com.qlik.app.softdeleted` event.
7. Check the `purgeAt` field to find the recovery deadline.

If you find a `com.qlik.app.harddeleted` event for the same app ID, the app has been
permanently deleted and cannot be restored.

### Option 2: Query the event data with the Audits API

Use this option for a precise or repeatable check.

Query the [Audits API](https://qlik.dev/apis/rest/audits) for `com.qlik.app.deleted` events and
match the event to your app using the `data.id` field.

The following cURL command retrieves app deleted events, sorted by most recent first:

```bash
curl -X GET "https://<TENANT>/api/v1/audits?eventType=com.qlik.app.deleted&sort=-eventTime" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

A soft-deleted app produces an event similar to the following:

```json
{
  "eventType": "com.qlik.app.deleted",
  "eventTime": "2026-05-27T13:49:51Z",
  "data": {
    "id": "<APP_ID>",
    "name": "My Analytics App",
    "deleteType": "SOFT",
    "resourceType": "app",
    "spaceId": "6a17fb8183f4781e079a7371"
  }
}
```

If the `deleteType` value is `HARD`, the app was hard-deleted and cannot be restored.

If the `deleteType` value is `SOFT`, query for the related
`com.qlik.app.softdeleted` event to retrieve the purge date.

```bash
curl -X GET "https://<TENANT>/api/v1/audits?eventType=com.qlik.app.softdeleted&sort=-eventTime" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Match the event to your app using the `data.id` field. The response includes a
`purgeAt` field:

```json
{
  "eventType": "com.qlik.app.softdeleted",
  "eventTime": "2026-05-27T13:49:51Z",
  "data": {
    "id": "<APP_ID>",
    "name": "My Analytics App",
    "purgeAt": "2026-06-10",
    "resourceType": "app",
    "spaceId": "6a17fb8183f4781e079a7371"
  }
}
```

The `purgeAt` date is the earliest date on which the app may be permanently deleted.
Once this date is reached, permanent deletion can happen at any time and is not under
user control. Restore the app before this date to remain within the recovery window.

## Restore the app

Once you have confirmed the app is soft-deleted and within the recovery window, send
a `POST` request to the restore endpoint.

The operation is available to tenant administrators and the app owner. The app owner
can only restore the app if the original space still exists and they retain delete
permission in that space. If either condition is not met, the API returns `403 Forbidden`.

```bash
curl -X POST "https://<TENANT>/api/analytics/apps/<APP_ID>/actions/restore" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

```js
const response = await fetch(
  `https://<TENANT>/api/analytics/apps/<APP_ID>/actions/restore`,
  {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <ACCESS_TOKEN>',
    },
  }
);
const app = await response.json();
```

```python
import requests

response = requests.post(
    "https://<TENANT>/api/analytics/apps/<APP_ID>/actions/restore",
    headers={"Authorization": "Bearer <ACCESS_TOKEN>"},
)
app = response.json()
```

A successful response returns the restored app object. The app is available
immediately under the same app ID it held before deletion.

## What is recovered

The restore operation returns the app to its state at the point of deletion. The
following table shows what is and is not recovered.

| Content                                          | Recovered |
| ------------------------------------------------ | --------- |
| Sheets, charts, and visualizations               | Yes       |
| Bookmarks                                        | Yes       |
| Stories                                          | Yes       |
| App script and data model                        | Yes       |
| App ID                                           | Yes       |
| Loaded data                                      | Yes       |
| Collections                                      | No        |
| Tags                                             | No        |
| Data alerts                                      | No        |
| Subscriptions                                    | No        |
| Notes                                            | No        |
| App evaluation results                           | No        |
| App usage metrics in activity centers            | No        |
| Other associated content not embedded in the app | No        |

## Next steps

After restoring the app, you may want to:

- Recreate any tags and collections that were associated with the app.
- Reconfigure data alerts, subscriptions, and notes as needed.

For more information, see the
[analytics applications overview](https://qlik.dev/manage/analytics-applications).
