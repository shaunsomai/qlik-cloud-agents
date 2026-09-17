---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/use-cases/add-sql-transformations/
last_updated: 2026-06-30T16:09:07Z
---

# Add SQL transformations

## Overview

Use this guide to add a SQL transformation to an existing transform task.

SQL transformations are defined as dataset files under the transform task's `datasets/` folder.

Use this approach when you need to create an output dataset from joins, aggregations, calculated columns, or other SQL
expressions.

Do not hand-author transformation data flow files.
Create visual data flow transformations in the Qlik Cloud user interface only.

## Prerequisites

- An existing transform task under `qtcp_tasks/`.
- One or more upstream datasets available from a source task.
- The upstream task ID and dataset IDs. Find these in the upstream task's `task.yaml` (task ID in `properties.id`) and
  dataset files (dataset IDs in dataset YAML files).
- VS Code configured with YAML schema validation.

## Step 1: Confirm the transform task

Open the transform task's `task.yaml` and confirm that the task type is `TRANSFORM`:

```yaml
properties:
  name: transform_customers
  id: transform-customers-4823
  type: TRANSFORM
```

## Step 2: Add source selection for the upstream datasets

Open or create `sourceSelection.yaml` in the transform task folder.

For example, to make the `Customers` and `Orders` datasets from a storage task available to the transform task:

```yaml
explicitlySelected:  
- name: Customers  
  sourceTask: prepare-customers-4822  
  type: TABLE  
  sourceTableId: customers  
- name: Orders  
  sourceTask: prepare-customers-4822  
  type: TABLE  
  sourceTableId: orders
```

Use the upstream task ID as `sourceTask`.
Use the upstream dataset ID as `sourceTableId`.

## Step 3: Create the output dataset file

Create a dataset file under the transform task's `datasets/` folder.

For example:

```text
qtcp_tasks/
  transform_customers/
    datasets/
      customerOrders.yaml
```

Add the custom SQL dataset definition:

```yaml
properties:
  id: customer-orders-4823
  name: customerOrders
  inputDatasets:
    - datasetId: customers
      name: customers
      taskId: prepare-customers-4822
    - datasetId: orders
      name: orders
      taskId: prepare-customers-4822
customDatasetSettings:
  customSql:
    expressionStatement: "SELECT c.customer_id, c.customer_name, o.order_id FROM ${customers} AS c INNER JOIN ${orders} AS o ON c.customer_id = o.customer_id"  
    alias:
      - name: customers
        value: '{{ref(project.current.projectId)}}$\_$prepare-customers-4822$\_$customers'  
      - name: orders
        value: '{{ref(project.current.projectId)}}$\_$prepare-customers-4822$\_$orders'  
    incremental: false
```

The `inputDatasets` entries identify the datasets used by the SQL expression.

The SQL expression uses `${alias}` placeholders.
Each placeholder must match:

- an `inputDatasets[].name` value;
- an `alias[].name` value.

The `alias[].value` value identifies the project, upstream task, and upstream dataset.

## Step 4: Validate aliases and dataset references

Before applying the change, confirm that:

- Each SQL placeholder has a matching alias.
- Each alias has a matching input dataset name.
- Each input dataset references the correct upstream taskId.
- Each datasetId matches the upstream dataset ID.
- The dataset file is under the transform task's `datasets/` folder.

## Step 5: Validate and synchronize

Before applying the change:

1. Check the VS Code Problems panel for YAML schema errors.
2. Commit and push the updated files if you use version control or create an archive ZIP file.
3. Apply remote changes in Qlik Cloud, or import the updated project package.
4. Verify that the transform task contains the new output dataset.
5. Run the pipeline and confirm that the SQL transformation produces the expected output.

## Troubleshooting

### Issue: The SQL expression cannot resolve a dataset

Confirm that every `${alias}` placeholder in the SQL expression has a matching entry in the alias array and a matching
`inputDatasets[].name`.

### Issue: The transformation points to the wrong source data

Confirm that `taskId` and `datasetId` reference the intended upstream task and dataset.
