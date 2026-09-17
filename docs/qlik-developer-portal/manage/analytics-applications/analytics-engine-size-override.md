---
source: https://qlik.dev/manage/analytics-applications/analytics-engine-size-override/
last_updated: 2026-05-07T07:59:16Z
---

# Pin applications to engine sizes

## Overview

Qlik Cloud automatically places applications on compute engines based on calculated metrics
that determine the required resources. This automatic placement works well for most apps,
but some require manual intervention.

Apps with large chart objects that generate large hypercubes can consume all available
memory and crash. By pinning an app to a specific engine size, you control the minimum
compute resources available for interactive consumption.

If you're new to this topic, first read the
[managing analytics applications overview](https://qlik.dev/manage/analytics-applications).

## Prerequisites

- The app must be in a space with
  [Large Apps support](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/large-app-support.htm)
  enabled.
- An access token or API key for a user with the `Tenant Admin` or `Analytics Admin` role, or
  a custom security role that includes the **Manage engine assignments for applications**
  (`apps:manage`) scope. For more information, see [Authentication](https://qlik.dev/authenticate).
- The app ID and tenant URL.

## Understanding engine placement

When you pin an app, it runs on large app engines and consumes large app capacity. You can
track this usage through [quota events](https://qlik.dev/apis/event/quotas/).

> **Warning:** If Large Apps support is disabled on the space, the app returns to a standard engine and
> may fail during reload or consumption.

### Valid engine sizes

| Size  | Description                       |
| ----- | --------------------------------- |
| `0`   | No override (automatic placement) |
| `40`  | 40 GB or larger pod               |
| `60`  | 60 GB or larger pod               |
| `80`  | 80 GB or larger pod               |
| `120` | 120 GB or larger pod              |
| `160` | 160 GB or larger pod              |
| `200` | 200 GB or larger pod              |

## Determining which engine size to use

You should select an engine of an appropriate size relative to your application.
Qlik by default places applications on engines four times larger than the size
of the application in memory.

For example:

- For a 10 GB application, it would be `10 * 4 = 40` and use a 40 GB pod.
- For a 25 GB application, it would be `25 * 4 = 100` and use a 120 GB pod, the
  next available size.

When pinning apps, you are forcing a minimum size engine for your app. Qlik will
use the minimum, or a larger size engine if required by the app.

## Quota consumption

Pinned apps consume quota from your Large Apps capacity. When you pin an app,
it will use the greater of:

- The pinned capacity divided by four, for example:
  - On a 40 GB engine, `40 / 4 = 10`, therefore 10 GB.
  - On a 120 GB engine, `120 / 4 = 30`, therefore 30 GB.
- The actual size of the application in memory (visible in the administration
  console, or on the app details page).

## Set an engine size override

To pin an app to a specific engine size, call the placement endpoint with the
`minEngineSize` attribute in the payload:

```bash
curl -L -X PUT "https://<TENANT>/api/v1/apps/<APP_ID>/placement" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{
    \"minEngineSize\": \"40\"
}"
```

Replace `<TENANT>` with your tenant hostname, `<APP_ID>` with the app GUID, and
`<ACCESS_TOKEN>` with your API key or OAuth access token.

A `200` response indicates success. Omitting the `minEngineSize` attribute sets the
value to `0`, which removes any existing override.

## Verify the override

To retrieve the current placement override for an app:

```bash
curl "https://<TENANT>/api/v1/apps/<APP_ID>/placement" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

The API returns `200` if an override exists, or `404` if no override exists.

## Remove an engine size override

To delete the override and return to automatic placement:

```bash
curl -X DELETE "https://<TENANT>/api/v1/apps/<APP_ID>/placement" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

The API returns `200` if the override was removed, or `404` if no override existed.

## Monitor capacity consumption

Pinned apps consume large app capacity. The [quota events](https://qlik.dev/apis/event/quotas/) track:

- Quota consumed when an app opens or reloads
- Quota released when an app unloads
- Allocation failures when capacity is insufficient

These events are available via the [Audits API](https://qlik.dev/apis/rest/audits/) for tenants with
Large Apps support.
