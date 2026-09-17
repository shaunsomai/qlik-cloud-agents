---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-task/
last_updated: 2026-06-30T16:09:07Z
---

# Add a task to a declarative pipeline

Use this guide to add a task to an existing declarative pipeline project by editing the project YAML files.

A task is stored in its own folder under `qtcp_tasks/`. At minimum, a task has a `task.yaml` file.

Additional files, such as `sourceSelection.yaml`, `schedule.yaml`, or `transformationRules.yaml`, are added only when
they apply to the task.

## Prerequisites

- A declarative pipeline project connected to GitHub version control or exported as a project package.
- VS Code configured with YAML schema validation.
- The source task, source connection, or target settings required by the new task.

## Step 1: Confirm that the task type is supported

Check the project type in `qtcp_project.yaml`.

For a DATA\_MOVEMENT project, supported task types are:

- `REPLICATION`
- `LAKE_LANDING`

For a DATA\_PIPELINE project, supported task types include data pipeline task types such as:

- `LANDING`
- `STORAGE`
- `TRANSFORM`
- `REGISTERED_DATA`
- `LAKE_LANDING`

Do not create `DATAMART` or `KNOWLEDGE_MART` tasks manually.
Create those task types in the Qlik Cloud user interface only.

## Step 2: Create the task folder

Create a folder for the new task under `qtcp_tasks/`.

For example:

```text
qtcp_tasks/
  prepare_customers/
    task.yaml
```

The folder name is the task name.

## Step 3: Create task.yaml

Create a minimal task definition with `properties.name`, `properties.id`, `properties.type`, and the required settings
for the task type.

For example, this `task.yaml` file adds a storage task:

```yaml
properties:
  name: prepare_customers
  id: prepare-customers-4822
  type: STORAGE
settings:
  artifactsLocation:
    internalSchema: '{{task.prepare-customers-4822.internalSchema}}'
    taskSchema: '{{task.prepare-customers-4822.taskSchema}}'
    databaseName: '{{task.prepare-customers-4822.databaseName}}'
taskRuntime:
  warehouseSelection:
    warehouseName: '{{task.prepare-customers-4822.warehouseName}}'
```

Use a unique task ID.
One common pattern is a sanitized task name followed by four digits, for example `prepare-customers-4822`.

## Step 4: Connect the task to upstream data

Create `sourceSelection.yaml` in the new task folder and set the datasources.

For example, to read the Customers dataset from an upstream landing task:

```yaml
explicitlySelected:
- name: Customers
  sourceTask: ingest-customers-4821
  type: TABLE
  sourceTableId: customers
```

Use the upstream task ID as the `sourceTask` value.

Do not add `sourceConnection` to non-landing tasks.
Non-landing tasks read from upstream tasks, not directly from source connections.

## Step 5: Update binding variable declarations

Add every binding variable referenced in the new files to `qtcp_bindings_definition.json`.

If you wish to use the value set to the task type, you can use the variable of
`{{task-type.<taskType>.<property>}}`. In this case, you need to add this new variable to
the file as well.

If a `task-type.*` variable already exists, do not add a duplicate.

For the storage task example, add or merge entries similar to the following:

```json
{
  "variables": {
    "task-type.storage.databaseName": "",
    "task-type.storage.warehouseName": "",
    "task.prepare-customers-4822.internalSchema": "",
    "task.prepare-customers-4822.taskSchema": "",
    "task.prepare-customers-4822.databaseName": "{{task-type.storage.databaseName}}",
    "task.prepare-customers-4822.warehouseName": "{{task-type.storage.warehouseName}}"
  }
}
```

## Step 6: Validate and synchronize

Before applying the change:

1. Check the VS Code **Problems** panel for YAML schema errors.
2. Confirm that all binding variables are declared in `qtcp_bindings_definition.json`.
3. Commit and push the new files if you use version control or create a ZIP archive.
4. Apply remote changes in Qlik Cloud, or import the updated project package.
5. Verify that the new task appears in the project and has the expected configuration.

## Next steps

If your task type supports scheduling, see [Add or update a task schedule](https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-or-update-task-schedule/)
to configure a schedule for the new task.

## Troubleshooting

### Issue: The new task does not appear after apply or import

Confirm that the task folder is under `qtcp_tasks/` and that the folder contains a valid `task.yaml`.

### Issue: The task cannot resolve a binding variable

Confirm that every `{{...}}` variable used in the new files is declared in `qtcp_bindings_definition.json` and has a
value in the target Qlik Cloud project.

### Issue: The task cannot read from the upstream task

Confirm that `sourceTask` uses the upstream task ID, and that `sourceTableId` matches the upstream dataset ID.
