---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/edit-with-version-control/
last_updated: 2026-06-30T16:46:02Z
---

# Edit a pipeline configuration with version control

## Overview

This guide walks through the developer workflow for updating a pipeline project using
declarative YAML files stored in GitHub.

## Prerequisites

- A Qlik Cloud pipeline project connected to GitHub version control.
- A local clone of the project repository and VS Code set up with YAML schema validation.
  See [Set up your development environment](https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/).
- Write access to the GitHub repository.
- **Can Edit** role in the Qlik Cloud space where the project resides.

> **Note:** If your project is connected to GitHub using the older JSON-based format, migrate to the YAML
> structure first. For more information, see the
> [migration process](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Retrieving-editing-pipeline-configuration.htm#Migrate)
> on Qlik Help.

> **Note:** Replace all `<angle bracket>` placeholders with your own values throughout this guide.

## Step 1: Edit task settings

YAML files in the project define the configuration of your pipeline. To update the pipeline, you edit the YAML files
locally, commit and push to GitHub, and then apply the changes in Qlik Cloud.

1. Open the task file for the task you want to change.

2. Make your edits. VS Code schema validation highlights unknown properties and required fields.
   You only need to include a property when you want to override its default value.

A minimal landing task file looks similar to this:

```yaml
properties:
  name: ingest-customers
  id: onboardingaaa_landing-4sy4
  type: LANDING
settings:
  landingDwSettings:
    landingArtifactsLocation:
      dataAssetSchema: '{{task.Ingest_customers-4sy4.taskSchema}}'
      database: '{{task.Ingest_customers-4sy4.databaseName}}'
```

Properties using the `{{variable-name}}` syntax are resolved using binding values stored
in Qlik Cloud when you run **Apply remote changes**.

> **Tip:** If you are unsure which properties are available for a task type, you can see them in the
> autocompletion suggestions in VS Code or in an export of the project in **All definitions** mode
> from the Qlik Cloud user interface.
> **All definitions** exports include all properties, making the complete schema visible before you
> start editing.

## Step 2: Update binding variables for your target environment

Binding variables have two parts:

- **Declaration**: defined in `qtcp_bindings_definition.json`, committed to GitHub,
  and edited in your IDE like any other project file.
- **Environment-specific value**: the actual value used at runtime for a given environment
  (for example, `DEV` or `PROD`). This is stored in Qlik Cloud and is not part of the
  repository. To view or update it, use the [Bindings API](https://qlik.dev/apis/rest/di-projects/#get-api-v1-di-projects-projectId-bindings/)
  or go to the relevant project in the Qlik Cloud user interface.

If you are introducing a new binding variable:

1. Add the variable to `qtcp_bindings_definition.json`. Apply operations or imports will fail
   if a referenced variable is not declared.
2. Reference the variable using `{{variable-name}}` syntax in the relevant task YAML file.
3. Commit and push both files to GitHub.
4. Set the environment-specific value using the [Bindings API](https://qlik.dev/apis/rest/di-projects/#put-api-v1-di-projects-projectId-bindings/)
   or the Qlik Cloud user interface when you run **Apply remote changes**.

## Step 3: Validate your changes locally

Before committing, check for schema errors in the VS Code Problems panel
(`Ctrl+Shift+M` on Windows, `Cmd+Shift+M` on macOS).
The panel lists all YAML issues across all files in the workspace, not just the file currently open.

You can also run the validation API against a project ZIP before applying changes.
The [Data integration projects API](https://qlik.dev/apis/rest/di-projects/) currently performs limited checks,
such as verifying the ZIP file and checking that task definitions include `settings`.

For more details, see [Validate a declarative pipeline configuration](https://qlik.dev/manage/di-projects/declarative-pipelines/validate-configuration/).

## Step 4: Commit and push to GitHub

1. Stage and commit your changes with a descriptive message that explains what you changed.
   Use VS Code's Source Control panel or your preferred Git client.
2. Push your changes to the GitHub branch that the Qlik Cloud project uses for **Apply remote changes**.

## Step 5: Apply remote changes in Qlik Cloud

Bring the changes into the target Qlik Cloud project:

> **Tip:** If this is the first time you are deploying to a target space, use **GitHub** >
> **Import from version control** to create the project there before applying remote changes.

1. In **Data Integration**, open the pipeline project in the target space (for example, `PROD`).
2. Select **GitHub** > **Apply remote changes**.
3. In the dialog, review the list of changed tasks, select which changes to apply, and confirm.

The project in Qlik Cloud now reflects the YAML files from GitHub.

> **Note:** Apply remote changes does not work across target platforms. For example, changes from a
> Snowflake project cannot be applied to a Databricks project in another space.

## Troubleshooting

### Issue: Apply remote changes shows no differences

**Solution:** Confirm that the branch selected in Qlik Cloud matches the branch your commit was done on,
and that the merge was completed in GitHub before running Apply remote changes.

### Issue: Variable missing error on apply remote changes or import

**Solution:** A binding variable referenced in a YAML task file was not found in
`qtcp_bindings_definition.json`. Add the variable definition to `qtcp_bindings_definition.json`, commit
and push the change, set the environment-specific value in Qlik Cloud, and run
**Apply remote changes** again.

### Issue: Task statuses appear incorrect after applying remote changes

**Solution:** This can occur when applying changes to a project that has been imported more
than once, or when a project has multiple active branches. Refresh the browser to reload the
current task states.

### Issue: Apply remote changes fails with a platform mismatch error

**Solution:** Apply remote changes does not work across target platforms. If the source project
uses Snowflake and the target space uses Databricks, use **GitHub** > **Import from version
control** to create a separate project in the target space.
