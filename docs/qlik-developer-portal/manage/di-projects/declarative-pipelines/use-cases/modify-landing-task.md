---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/modify-landing-task/
last_updated: 2026-06-30T16:09:07Z
---

# Modify a landing task

## Overview

Use this guide to modify an existing landing task in a declarative pipeline project.

You can use this workflow to:

- Add source tables.
- Add include or exclude patterns.
- Add task-level transformation rules.

## Prerequisites

- A declarative pipeline project with a landing task with at least one source.
- The project is connected to GitHub version control or exported as a project package.
- Source table names and schemas for the tables you want to add.

## Step 1: Locate the landing task

1. Open the task folder under `qtcp_tasks/` and navigate to the required landing task folder.
2. Open the desired `task.yaml` file and copy the task `id`. In the following example, the task id is
   `ingest-customers-4821`:

   ```yaml
   properties:
     name: ingest_customers
     id: ingest-customers-4821
     type: LANDING
   ```

   You will use this `id` to create binding variable names later.

## Step 2: Add source tables

Open or create `sourceSelection.yaml` in the landing task folder.

If this is the first data source, define the connection and add the dataset.

It is best to use variables which contain the task `id` for the `sourceConnection` and schema properties as in the
following example.

For example, to add a `Customers` table from the `dbo` schema:

```yaml
sourceConnection: '{{task.ingest-customers-4821.sourceConnection}}'
explicitlySelected:
  - name: Customers
    schema: '{{task.ingest-customers-4821:null$\_$dbo.schema}}'
    type: TABLE
```

Use `explicitlySelected` when you want to list individual tables.

To select tables by pattern instead, use `includePatterns` and `excludePatterns`:

```yaml
sourceConnection: '{{task.ingest-customers-4821.sourceConnection}}'
includePatterns:
  - tablePattern: 'dim\_%'
    schemaPattern: 'dbo'
    type: TABLE
excludePatterns:
  - tablePattern: 'temp\_%'
    schemaPattern: 'dbo'
    type: TABLE
```

## Step 3: Add task-level transformation rules

To apply a rule across tables in the task, open or create `transformationRules.yaml`.

For example, to convert matching table names to uppercase:

```yaml
rules:  
- name: Rule_1
  actionType: RENAME_TABLE
  scope:
    whereTableName: '%'
  action:
    renameType: TO_UPPER
```

Use `transformationRules.yaml` for task-level rules that apply across tables.
Dataset-level transformations are defined in the dataset files.

## Step 4: Update binding variable declarations

Every binding variable referenced with `{{...}}` must be declared in `qtcp_bindings_definition.json`.
This file holds the list of variables, not their value, so keep the value as empty string.

For the previous examples, add the source connection and schema variables:

```json
{
  "variables": {
    "task.ingest-customers-4821.sourceConnection": "",
    "task.ingest-customers-4821:null$_$dbo.schema": ""
  }
}
```

If `qtcp_bindings_definition.json` already contains variables, merge the new entries into the existing `variables`
object.

## Step 5: Validate and synchronize

Before applying the change:

1. Check the VS Code Problems panel for YAML schema errors.
2. Commit and push the updated files if you use version control or create a ZIP archive for the project.
3. Apply remote changes in Qlik Cloud, or import the updated project package.
4. Verify that the task includes the expected source tables and transformation rules.

## Troubleshooting

### Issue: The source table is not added

Confirm that the table is listed in `sourceSelection.yaml`.

### Issue: Apply or import fails because a variable is missing

Confirm that every `{{...}}` variable used in the YAML files is declared in `qtcp_bindings_definition.json`.
