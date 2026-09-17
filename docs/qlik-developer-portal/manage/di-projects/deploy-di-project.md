---
source: https://qlik.dev/manage/di-projects/deploy-di-project/
last_updated: 2026-06-30T16:09:07Z
---

# Deploy a data integration project

In this tutorial, you'll learn how to export a data integration project from a development data space and import it into
a production data space using the [Data Integration Projects API](https://qlik.dev/apis/rest/di-projects).

## Overview

The example scenario is a replication project with a single task that retrieves employee records from a MySQL source and
loads the data to a Google BigQuery target:

- The project is created in a development data space, where you can design and test it.
- The project is then exported from that development data space and imported into the production data space.

> **Note:** You must create and configure projects and tasks in the Qlik Cloud UI.
> The API is for deployment, configuration, and monitoring only.

> **Tip:** This tutorial demonstrates a direct API export and import workflow. If your project is
> connected to GitHub version control, a Git-based workflow using declarative pipeline YAML
> files is also available. See
> [Declarative pipelines](https://qlik.dev/manage/di-projects/declarative-pipelines/).

## What you'll learn

In this tutorial, you'll learn:

- How to list your existing projects to get the right project ID
- How to export a project ZIP from your development data space
- How to retrieve and update project export variables
- How to import into a new project in your production data space
- How to prepare and execute the project

## Prerequisites

- You have access to both your development and production data spaces.
- You have already [created a data integration project](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Designing-data-pipeline.htm)
  in your development data space.
- You have set up connections to [data sources](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/connecting-data-2.htm) and [targets](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/data-project-connections.htm)
  in your development and production data spaces.
- An access token or API key with sufficient [permissions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/permissions-data-space.htm),
  see [Authentication](https://qlik.dev/authenticate).

> **Note:** Replace everything in `<angle brackets>` or `{curly braces}` with your own values.
> For example, replace `<TENANT>` with your tenant name.

## Step 1: Find your project ID in your development data space

Before exporting, you need to find the project's unique ID:

```bash
curl -X GET "https://<TENANT>/api/v1/di-projects" ^
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
[
    {
        "id": "687a1a143430b13b69d00d85",
        "name": "replicate-employee-db",
        "description": "Replicates data from a MySQL source containing employee records into a BigQuery target/",
        "ownerId": "66cd95575011929d135e71ef",
        "spaceId": "6870e39d3fa005ebd94fae89"
    },
    ...
]
```

Look for the project you created in your development data space.

Copy the `id` field. You will use this ID in the next step.

## Step 2: Export the project from your development data space

Export your project as a ZIP file from your development data space:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/actions/export" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"includeBindings\": false
  }" ^
  -o "<FILE_NAME>.zip"
```

This creates a .zip file containing your project definition and metadata.

## Step 3: Retrieve the project export variables (bindings)

Bindings are the project export variables.
For example, these variables include the ones your project uses to connect to the correct sources and targets.

Retrieve the export variables for the project:

```bash
curl -X GET "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/bindings" ^
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
{
    "nameToIdMap": {
        "{{id(connection, DEV_SPACE.BigQuery_DEV)}}": "7b9fa853-a16d-49e3-b92b-cba102db1c33",
        "{{id(connection, DEV_SPACE.MySQL_DEV)}}": "3c3deb70-61f8-4603-9331-0ea646eb9335"
    },
    "variables": {
        "projectName": "replicate-employee-db",
        "platformConnection": null,
        "cloudStagingConnection": null,
        "task.replicate_employees-kh7j.targetConnection": "{{id(connection, DEV_SPACE.BigQuery_DEV)}}",
        "task.replicate_employees-kh7j.targetStorageConnection": null,
        "task.replicate_employees-kh7j.sourceConnection": "{{id(connection, DEV_SPACE.MySQL_DEV)}}",
        "task.replicate_employees-kh7j:null$_$employees_dev.schema": "employees_dev"
    }
}
```

> **Note:** This example shows variables for a replication project.
> Your project may have different variables depending on its configuration.

Copy and save the variables. You will use them in later steps.

## Step 4: Create a new project in your production data space

Before importing the exported ZIP file, create a new empty project in your production data space:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"name\": \"<PROJECT_NAME>\",
    \"type\": \"<PROJECT_TYPE>\",
    \"space\": \"<SPACE_ID>\",
    \"description\": \"<PROJECT_DESCRIPTION>\",
    \"platformType\": \"<TARGET_PLATFORM>\",
    \"platformConnection\": \"<PLATFORM_CONNECTION>\"
  }"
```

Example request for this replication project:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"name\": \"replicate-prod\",
    \"type\": \"DATA_MOVEMENT\",
    \"space\": \"6870e39d3fa005ebd94fae89\",
    \"description\": \"Replicates data from a MySQL source containing employee records into a BigQuery target\",
    \"platformType\": \"BIGQUERY\",
    \"platformConnection\": \"882da0ef-a9ce-497c-91ee-0c78e1f5812e\"
  }"
```

Example response:

```json
{
    "id": "687a1a143430b13b69d00d85",
    "name": "replicate-prod",
    "description": "Replicates data from a MySQL source containing employee records into a BigQuery target",
    "ownerId": "66cd95575011929d135e71ef",
    "spaceId": "6870e3a444d81cf9707d65e8"
}
```

Copy the `id` and `name` fields. You will use them in the next steps.

## Step 5: Update the project variables for production

You need to update the export variables (bindings) saved
in [step #3](#step-3-retrieve-the-project-export-variables-bindings) so your imported project in production points to
the correct data sources, targets, and schema:

1. Update connection variables.\
   Change any variables that reference development connections to their production equivalents in the production data
   space.\
   For example:

   - Change `{{id(connection, DEV_SPACE.BigQuery_DEV)}}` to `{{id(connection, PROD_SPACE.BigQuery_PROD)}}`
   - Change `{{id(connection, DEV_SPACE.MySQL_DEV)}}` to `{{id(connection, PROD_SPACE.MySQL_PROD)}}`

2. Update schema names (if needed).\
   Change any schema and database names that are different in production.\
   For example, change `"employees_dev"` to `"employees_prod"`.

3. Update the project name\
   Set `projectName` to your production project name created in [step 4](#step-4-create-a-new-project-in-your-production-data-space).

> **Tip:** If you're not sure what your production connection IDs are, you can list them using the
> [Data connections API](https://qlik.dev/apis/rest/data-connections/#get-api-v1-data-connections).

### Example updated variables

Development variables:

```json
"variables": {
  "projectName": "replicate-employee-db",
  "platformConnection": null,
  "cloudStagingConnection": null,
  "task.replicate_employees-kh7j.targetConnection": "{{id(connection, DEV_SPACE.BigQuery_DEV)}}",
  "task.replicate_employees-kh7j.targetStorageConnection": null,
  "task.replicate_employees-kh7j.sourceConnection": "{{id(connection, DEV_SPACE.MySQL_DEV)}}",
  "task.replicate_employees-kh7j:null$_$employees_dev.schema": "employees_dev"
}
```

Production variables:

```json
"variables": {
  "projectName": "replicate-prod",
  "platformConnection": null,
  "cloudStagingConnection": null,
  "task.replicate_employees-kh7j.targetConnection": "{{id(connection, PROD_SPACE.BigQuery_PROD)}}",
  "task.replicate_employees-kh7j.targetStorageConnection": null,
  "task.replicate_employees-kh7j.sourceConnection": "{{id(connection, PROD_SPACE.MySQL_PROD)}}",
  "task.replicate_employees-kh7j:null$_$employees_dev.schema": "employees_prod"
}
```

### Example request

Example request to update the bindings in your production project:

```bash
curl -X PUT "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/bindings" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"variables\": {
      \"projectName\": \"replicate-prod\",
      \"platformConnection\": null,
      \"cloudStagingConnection\": null,
      \"task.replicate_employees-kh7j.targetConnection\": \"{{id(connection, PROD_SPACE.BigQuery_PROD)}}\",
      \"task.replicate_employees-kh7j.targetStorageConnection\": null,
      \"task.replicate_employees-kh7j.sourceConnection\": \"{{id(connection, PROD_SPACE.MySQL_PROD)}}\",
      \"task.replicate_employees-kh7j:null$_$employees_dev.schema\": \"employees_prod\"
    }
  }"
```

> **Warning:** Verify all variables, especially connection IDs and schema names.
> If your production and development names are inconsistent, you may see errors during import or prepare.

If successful, you will receive a `200 OK` response.

## Step 6: Import the project ZIP file into the production data space

Import the exported project ZIP file into your production data space:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/actions/import" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: multipart/form-data" ^
  -F "file=@project-export.zip"
```

If successful, you will receive a `200 OK` response.

## Step 7: Prepare the project for execution

Prepare the imported project:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/actions/prepare" ^
  -H "Authorization: Bearer <API_KEY>" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"allowRecreate\": false,
    \"selectedTasks\": [
    ]
  }"
```

Leave the `selectedTasks` array empty to prepare all tasks in the project.
If you want to prepare specific tasks, list their IDs in the array.

> **Note:** Set `allowRecreate` to `true` if you want to allow recreating tasks that already exist in the project during the
> preparation.

Example response:

```json
{
    "actionId": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
}
```

This operation is asynchronous.
You will receive a `202 Accepted` response with an `actionId` that you can use to verify the status of the preparation.

## Step 8: Verify the project preparation status

Poll for the async action status endpoint using the returned `actionId`:

```bash
curl -X GET "https://<TENANT>/api/v1/di-projects/actions/{actionId}" ^
  -H "Authorization: Bearer <API_KEY>"
```

Example response for a completed action:

```json
{
    "startTime": null,
    "endTime": null,
    "taskDetails": null,
    "name": "Prepare di project with project id '687a1a143430b13b69d00d85'",
    "type": "PROJECT_PREPARE",
    "state": "COMPLETED",
    "taskProgress": {
        "pending": 0,
        "executing": 0,
        "completed": 1,
        "failed": 0,
        "canceled": 0,
        "skipped": 0
    },
    "error": null
}
```

When the status is `COMPLETED`, you can proceed to start the task.

## Step 9: Start the task in the project

List the tasks in your project to find the task ID:

```bash
curl -X GET "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/di-tasks" ^
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
[
    {
        "id": "replicate_employees-kh7j",
        "name": "replicate-employees",
        "description": "Replicates the employees database from a MySQL source to a BigQuery target using full load and change data capture (CDC).",
        "type": "REPLICATION",
        "ownerId": "66cd95575011929d135e71ef",
        "spaceId": "6870e3a444d81cf9707d65e8"
    }
]
```

Run the task using its ID:

```bash
curl -X POST "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/di-tasks/{taskId}/runtime/actions/start" ^
  -H "Authorization: Bearer <API_KEY>"
```

If successful, you will receive a `204 No Content` response.

## Step 10: (Optional) Get the task execution status

Verify the runtime status of the task:

```bash
curl -X GET "https://<TENANT>/api/v1/di-projects/<PROJECT_ID>/di-tasks/{taskId}/runtime/state" ^
  -H "Authorization: Bearer <API_KEY>"
```

<details>
<summary>

Example response

</summary>

```json
{
  "name": "replicate_employees-kh7j",
  "type": "REPLICATION",
  "lastRun": {
    "state": "RUNNING",
    "endTime": null,
    "general": {
      "gatewayId": "gw-123",
      "gatewayName": "OnPremGateway1",
      "datasetCount": 2,
      "gatewayTaskName": "replicate_employees-kh7j",
      "dataTaskUpdatedTo": "2025-07-22T16:18:39.157Z",
      "liveViewsUpdatedTo": null,
      "datasetsInErrorCount": 0,
      "lakehouseClusterName": null
    },
    "message": "",
    "duration": "01:30:45",
    "fullLoad": {
      "errorCount": 0,
      "queuedCount": 0,
      "loadingCount": 0,
      "completedCount": 2
    },
    "cdcStatus": {
      "latency": "00:05:23",
      "totalProcessedCount": 1200,
      "applyingChangesCount": 10,
      "accumulatingChangesCount": 0,
      "throughputInKilobytesPerSecond": 150.2
    },
    "startTime": "2025-07-22T16:18:39.157Z",
    "lastBatchOfChanges": {
      "relatesToRecordsTo": "2025-07-22T16:00:00.000Z",
      "totalProcessedCount": 100,
      "relatesToRecordsFrom": "2025-07-22T15:00:00.000Z",
      "throughputInRecordsPerSecond": 5
    }
  },
  "runReadiness": {
    "state": "ALREADY_RUNNING",
    "message": ""
  }
}
```

</details>

Your data integration project is now deployed and running in your production data space.

## Next steps

For more information about the Data Integration Projects API, see the [API Reference](https://qlik.dev/apis/rest/di-projects).
