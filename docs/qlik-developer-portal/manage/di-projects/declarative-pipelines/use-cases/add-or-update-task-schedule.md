---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-or-update-task-schedule/
last_updated: 2026-06-30T16:09:07Z
---

# Add or update a task schedule

## Overview

Use this guide to add or update a schedule for an existing task in a declarative pipeline project.

Task schedules are defined in `schedule.yaml` in the task folder.
Create this file only for task types that support scheduling.

## Prerequisites

- A declarative pipeline project connected to GitHub version control or exported as a project package.
- VS Code configured with YAML schema validation.
- An existing task that supports scheduling.

## Supported task types

Create `schedule.yaml` only for task types that support scheduling.

| Task type                   | Supported schedule types  |
| --------------------------- | ------------------------- |
| `STORAGE`                   | Time-based                |
| `QVD_STORAGE`               | Time-based                |
| `LAKEHOUSE_STORAGE`         | Time-based                |
| `TRANSFORM`                 | Time-based or event-based |
| `DATAMART`                  | Time-based or event-based |
| `KNOWLEDGE_MART`            | Time-based or event-based |
| `FILE_BASED_KNOWLEDGE_MART` | Time-based or event-based |
| `LAKEHOUSE_MIRROR`          | Time-based or event-based |
| `STREAMING_TRANSFORM`       | Time-based or event-based |

Do not create `schedule.yaml` for task types not listed in the previous table.

## Step 1: Confirm that the task supports scheduling

Open the task's `task.yaml` and check the task type (`properties.type`).

If the task type is not listed as supporting schedules, do not create `schedule.yaml`.

## Step 2: Create or open schedule.yaml

In the task folder, create or open `schedule.yaml`:

```text
qtcp_tasks/
  prepare_customers/
    task.yaml
    schedule.yaml
```

## Step 3: Choose a schedule type

Use one of the following schedule types, depending on the task type and workflow:

- `TIME_BASED`: runs the task on a time-based schedule.
- `EVENT_BASED`: runs the task when upstream task events occur.

### Add a time-based schedule

For a time-based schedule, add a `TIME_BASED` scheduling entry.

For example, to run the task daily:

```yaml
scheduling:
  - schedulingType: TIME_BASED
    enabled: true
    timeBasedScheduling:
      schedule:
        - 'RRULE:FREQ=DAILY;INTERVAL=1'
      startDateTime: '2026-03-18T15:30:00.0000000Z'
      timezone: Etc/UTC
```

The `startDateTime` value defines when the schedule starts. Use UTC value.

In this example, the task will run every day at 15:30 UTC, starting on March 18, 2026.

### Add an event-based schedule

For a task that should run when upstream tasks complete, add an `EVENT_BASED` scheduling entry.

Use `ANY_INPUT_TASK` when the task should run after any input task completes:

```yaml
scheduling:
  - schedulingType: EVENT_BASED
    enabled: true
    eventBasedScheduling:
      eventSchedulingType: ANY_INPUT_TASK
```

Use `ANY_SELECTED_TASK` when the task should run only after specific tasks complete:

```yaml
scheduling:
  - schedulingType: EVENT_BASED
    enabled: true
    eventBasedScheduling:
      eventSchedulingType: ANY_SELECTED_TASK
      triggerApps:
        - projectId: '{{ref(project.current.projectId)}}'
          dataAppId: ingest-customers-4821
```

Use the upstream task ID as the `dataAppId` value.

In this example, the task will run when the `ingest-customers-4821` task completes.

## Step 4: Update an existing schedule

To modify an existing schedule, edit the relevant entry in schedule.yaml.

For example, to change a daily schedule to run every six hours:

```yaml
scheduling:
- schedulingType: TIME_BASED
  enabled: true
  timeBasedScheduling:
    schedule:
      - 'RRULE:FREQ=HOURLY;INTERVAL=6'
    startDateTime: '2026-03-18T15:30:00.0000000Z'
    timezone: Etc/UTC
```

If the schedule includes `enabled: false`, set it to `true` when you want the schedule to run.

In this example, the task will run every six hours, starting on March 18, 2026 at 15:30 UTC.

## Step 5: Validate and synchronize

Before applying the change:

1. Check the VS Code Problems panel for YAML schema errors.
2. Commit and push the updated files if you use version control, or create a ZIP archive for the project.
3. Apply remote changes in Qlik Cloud, or import the updated project package.
4. Verify that the task schedule is shown correctly in Qlik Cloud.

## Troubleshooting

### Issue: The schedule is not applied

Confirm that `schedule.yaml` is in the correct task folder and that the task type supports scheduling.

### Issue: The task does not run on schedule

Confirm that the schedule entry has `enabled:true` and that the `startDateTime` and `timezone` values are correct.

### Issue: The schedule fails schema validation

Check that the file uses the scheduling array and that each entry includes a valid `schedulingType`.
