---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/export-and-import/
last_updated: 2026-06-30T16:09:07Z
---

# Export and import a pipeline configuration

## Overview

Use export and import to move a declarative pipeline project between projects, spaces, tenants,
or environments without relying on a connected GitHub repository.

The workflow on this page shows the API-based process. You can also export and import project
packages from the Qlik Cloud user interface.

A project package contains files such as `qtcp_project.yaml`,
`qtcp_bindings_definition.json`, and files under `qtcp_tasks/`.

## Export modes

When exporting through the API, use the `mode` field to choose the export mode:

- `MINIMAL`: YAML project structure with default values omitted.
- `ALL`: YAML project structure with all values included.
- `LEGACY`: legacy JSON project structure.

When declarative pipelines are enabled, `MINIMAL` is the default export mode.

Use `MINIMAL` for day-to-day deployment and promotion workflows. The resulting YAML contains only
properties that differ from server defaults, which keeps package contents and diffs smaller.

Use `ALL` when you need to inspect all available properties or discover the full schema.

Use `LEGACY` only for backward compatibility with older import workflows.

> **Note:** The YAML-based export formats (`MINIMAL` and `ALL`) and the legacy JSON format (`LEGACY`) are
> both supported during a 12-month transition period. The JSON format will be deprecated with
> notifications sent at 6 months, 3 months, and 1 month before the end of the transition period.

Binding values are not included in exported packages by default. To include `bindings.json` in the
exported package, set `includeBindings` to `true`.

## Binding values

Binding variables separate the project definition from environment-specific values such as
connections, schemas, warehouses, and other target-environment settings.

Binding variable declarations are stored in `qtcp_bindings_definition.json`. Use this file to
identify which variables need values in the target environment.

> **Note:** `bindings.json` is included in an exported package only when `includeBindings` is set to `true`.
> Use it as a reference for resolved values from the source environment.
> For deployment to another environment, set the target values on the target project before importing.
> Do not rely on `bindings.json` to provide target environment values during import.

## Export and import workflow

Use this workflow to export a project package from a source environment and import it into a
target project.

### Step 1: Export the source project package

Call the export endpoint for the source project:

```bash
curl -X POST "https://<TENANT_URL>/api/v1/di-projects/<SOURCE_PROJECT_ID>/actions/export" \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -H "Accept: application/octet-stream" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "MINIMAL"
  }' \
  --output my-project.zip
```

To include resolved binding values from the source environment, add `includeBindings`:

```json
{
  "mode": "MINIMAL",
  "includeBindings": true
}
```

### Step 2: Identify the required binding values

Inspect `qtcp_bindings_definition.json` in the exported package to identify the variables that
need values in the target environment.

If the package includes `bindings.json`, you can use it as a reference for the source
environment values.

### Step 3: Create or select a target project

Import requires an existing target project. Create a target project in the target space, or select
an existing compatible project.

The required project properties depend on the project type and target platform.

The following example creates a data pipeline project:

```bash
curl -X POST "https://<TENANT_URL>/api/v1/di-projects" \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<PROJECT_NAME>",
    "space": "<SPACE_ID>",
    "type": "DATA_PIPELINE",
    "platformType": "<PLATFORM_TYPE>",
    "platformConnection": "<CONNECTION_ID>"
  }'
```

Save the target project ID from the response.

### Step 4: Set binding values for the target project

If your zip file does not include the bindings.json file, you need to set the
target environment values before importing the package by using the
[Bindings API](https://qlik.dev/apis/rest/di-projects/#put-api-v1-di-projects-projectId-bindings):

```bash
curl -X PUT "https://<TENANT_URL>/api/v1/di-projects/<TARGET_PROJECT_ID>/bindings" \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "variables": {
      "<VARIABLE_NAME>": "<TARGET_VALUE>"
    }
  }'
```

Repeat the variable entries for each binding value required by the project.

### Step 5: Optionally validate the package

You can run the validation endpoint before importing the project package. The validation endpoint
currently performs limited checks, such as verifying the ZIP file and checking that task
definitions include `settings`.

```bash
curl -X POST "https://<TENANT_URL>/api/v1/di-projects/utils/actions/validate-project-definitions" \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -F "zip=@my-project.zip"
```

For more information, see
[Validate a declarative pipeline configuration](https://qlik.dev/manage/di-projects/declarative-pipelines/validate-configuration/).

### Step 6: Import the package into the target project

Call the import endpoint with the project package:

```bash
curl -X POST "https://<TENANT_URL>/api/v1/di-projects/<TARGET_PROJECT_ID>/actions/import" \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -F "zip=@my-project.zip"
```

A successful import returns `200 OK` with an empty response object.

## Verify the imported project

After importing the package, verify the target project in Qlik Cloud:

- The expected tasks are present.
- Binding values are set for the target environment.
- Task settings, schedules, and transformation rules match the imported project definition.
- The pipeline runs successfully in the target environment.

## Project package structure

For project package structure details, see
[Project structure reference](https://qlik.dev/manage/di-projects/declarative-pipelines/project-structure-reference/).

## Troubleshooting

### Issue: Import fails because binding values are missing

Confirm that the target project is compatible with the source project and has binding values set before import.
Use `qtcp_bindings_definition.json` to identify the required variables, then set values by using the
Bindings API or the Qlik Cloud user interface.

### Issue: The imported project uses the wrong environment values

Confirm that each binding variable on the target project has the correct value for the target
environment, if the package includes `bindings.json`.

### Issue: The package is rejected

Confirm that the package contains supported declarative pipeline project files and that files are
not empty. You can run the validation endpoint before import for a limited package check.

### Issue: Import fails with a platform or project type mismatch

Confirm that the target project is compatible with the imported package. For example, do not import
a package from a Snowflake project into a Databricks target project unless that cross-platform
workflow is supported.
