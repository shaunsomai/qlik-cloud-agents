---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/validate-configuration/
last_updated: 2026-06-30T16:09:07Z
---

# Validate a declarative pipeline configuration

## Overview

The validation endpoint in the Data integration projects API checks a declarative pipeline
project package before you apply or import changes. Use this endpoint as an early check when
you edit project files locally or automate deployment with the API.

> **Note:** The validation endpoint performs limited checks. It verifies the uploaded ZIP file,
> checks supported file types, detects empty files, and reports task definitions where
> `settings` is missing. It does not validate binding variable resolution, unused
> bindings, task relationships, or all schema constraints.

## Prerequisites

- A declarative pipeline project with YAML task files.
- Access to Qlik Cloud with valid credentials.
- `curl` or an HTTP client to call the API.
- A valid `<TENANT_URL>` and `<BEARER_TOKEN>` for authentication.

## Steps

### Step 1: Create a project ZIP

Create a ZIP file from the declarative pipeline project files you want to validate.

You can get the project files from either of these sources:

- **Version control workflow:** use your local clone of the GitHub repository.
- **Export workflow:** export the project from Qlik Cloud using the API or the user interface.

If you create the ZIP manually, place the project files at the ZIP root:

```text
qtcp_project.yaml
qtcp_bindings_definition.json
qtcp_tasks/
  task-1/
    task.yaml
```

For the full project structure, see [Project structure reference](https://qlik.dev/manage/di-projects/declarative-pipelines/project-structure-reference/).

### Step 2: Call the API

Send a POST request to the validation endpoint with your project files as a ZIP:

```bash
curl -X POST \
  https://<TENANT_URL>/api/v1/di-projects/utils/actions/validate-project-definitions \
  -H "Authorization: Bearer <BEARER_TOKEN>" \
  -F "zip=@my-project.zip"
```

Replace `<TENANT_URL>` with your Qlik Cloud tenant, for example `tenant.us.qlikcloud.com`.
Replace `<BEARER_TOKEN>` with your API token.

### Step 3: Interpret the response

The API returns a JSON response with a `reports` array. If validation succeeds, the array is empty:

```json
{
  "reports": []
}
```

If validation finds an issue, the response includes one or more reports:

```json
{
  "reports": [
    {
      "level": "ERROR",
      "path": "qtcp_tasks/task-1/task.yaml",
      "reason": "Property 'settings' is missing."
    }
  ]
}
```

Review each report and use the `path` value to locate the affected file.
The `level` value indicates the severity of the report.

### Step 4: Fix errors and revalidate

Fix the reported issues, create a new ZIP file, and call the API again.

## Verification

The API returns status `200 OK` with an empty `reports` array:

```json
{
  "reports": []
}
```

## Troubleshooting

### Issue: The ZIP file is rejected

**Solution:** Confirm that the file has a `.zip` extension, is not empty, and does not exceed the 10 MB size limit.

### Issue: A file in the ZIP is rejected

**Solution:** Confirm that each file in the ZIP uses a supported file type.
The validation endpoint accepts YAML and JSON declarative pipeline project files.

### Issue: A task report says Property 'settings' is missing

**Solution:** Open the task file shown in the `path` value and add the required `settings` section.
Then, create a new ZIP file and run validation again.
