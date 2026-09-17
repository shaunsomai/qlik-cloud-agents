---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/
last_updated: 2026-06-30T16:09:07Z
---

# Declarative pipeline use case examples

## Overview

Use these examples to learn how to modify an existing declarative pipeline project by editing
YAML files.

The examples start from a project that is already connected to GitHub version control or exported
as a project package. Each example shows which files to edit, how to validate the changes, and how
to synchronize the updated project with Qlik Cloud.

## Before you begin

Before following these examples, make sure that you have:

- A declarative pipeline project connected to GitHub version control or exported as a ZIP file.
- A local copy of the project files.
- VS Code configured with YAML schema validation.
- Access to the target Qlik Cloud project where you want to apply or import the changes.

For setup steps, see
[Set up your development environment](https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/).

## Use case examples

### Modify a landing task

Add source tables, include or exclude table patterns, task-level transformation rules, and binding
variables for an existing landing task.

[Modify a landing task](https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/modify-landing-task/)

### Add a task

Add a task folder, create `task.yaml`, connect the task to upstream data, update binding variables,
and synchronize the project.

[Add a task to a declarative pipeline](https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-task/)

### Add or update a task schedule

Create or update `schedule.yaml` for task types that support scheduling.

[Add or update a task schedule](https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-or-update-task-schedule/)

### Add SQL transformations

Create a SQL transformation dataset in an existing transform task.

[Add SQL transformations](https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-sql-transformations/)

## Validate and synchronize changes

After editing project files, validate and synchronize the project using one of the supported
workflows:

- For GitHub version control, commit and push the files, then apply remote changes in Qlik Cloud.
- For export and import, create a project ZIP and import it into the target project.

For more information, see:

- [Validate a declarative pipeline configuration](https://qlik.dev/manage/di-projects/declarative-pipelines/validate-configuration/)
- [Edit a declarative pipeline with version control](https://qlik.dev/manage/di-projects/declarative-pipelines/edit-with-version-control/)
- [Export and import declarative pipelines](https://qlik.dev/manage/di-projects/declarative-pipelines/export-and-import/)
