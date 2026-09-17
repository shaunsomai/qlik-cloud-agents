---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/project-structure-reference/
last_updated: 2026-06-30T16:09:07Z
---

# Project structure reference

## Overview

A declarative pipeline project uses the same folder layout whether it is connected to a GitHub
repository, exported as a ZIP file, or both. This page describes the project-level files and the
task-level files and folders that can appear in a declarative pipeline project.

## Folder structure

```text
my-pipeline-project/
  qtcp_project.yaml
  qtcp_bindings_definition.json
  bindings.json                 # export only, included only when binding values are requested
  qtcp_tasks/
    newTaskDefaults.yaml        # optional
    {taskName}/
      task.yaml
      transformationRules.yaml  # optional
      sourceSelection.yaml      # optional
      schedule.yaml             # optional
      model.yaml                # optional, transform task types only
      transformationDataFlows/  # optional, transform task types only
        {transformationDataFlowName}.yaml
      datasets/                 # optional, task-dependent
        {datasetName}.yaml
```

## Project-level files

**`qtcp_project.yaml`** defines project-wide settings, such as the project name, platform type
(for example, Snowflake or Databricks), and space assignment. This is the root file for
the project and is always present.

**`qtcp_bindings_definition.json`** is the variable registry for the project. Every binding variable
used in the YAML files must be declared here. The file lists variable names and is part of the
project definition. Qlik Cloud uses this file to resolve binding references and expose
environment-specific values through the Bindings API.

**`bindings.json`** contains the resolved, environment-specific values for variables declared
in `qtcp_bindings_definition.json`. This file can be included in exported project packages when
binding values are requested. It is always a JSON file, even when the project definition uses YAML.

Version-control commits do not include `bindings.json`. In the version-control workflow, binding
values are stored in Qlik Cloud and resolved when you run **Apply remote changes** or use the
Bindings API.

## Task files

Each task lives in its own folder under `qtcp_tasks/`. The folder name matches the task name.

**`newTaskDefaults.yaml`** is optional and lives at the `qtcp_tasks/` level.
It sets project-wide default settings for each task type when new tasks of that type are created.
The file is absent if no task-type defaults have been overridden.

**`task.yaml`** contains the core task configuration: task name, type, and settings that
override defaults.

**`transformationRules.yaml`** is present when task-level transformation rules are defined.
It holds rules that apply across all datasets in the task, such as global table or column renames.

**`sourceSelection.yaml`** defines which source tables or objects the task ingests.
For tasks that read from a structured source, this file lists the selected tables.

**`schedule.yaml`** is present only when the task has a schedule defined. It contains
the schedule type and cadence settings. If the task runs on demand only, this file is omitted.

**`model.yaml`** is present for transform task types. It contains the relationship definitions
between datasets in the task. The file has a `relationships` array with one entry per
defined relationship.

## Dataset files

The `datasets/` folder contains dataset files when dataset-level configuration is included for the task.
On landing tasks, datasets without explicit rules can be omitted and regenerated
from source selection metadata on import.

A dataset file contains the dataset properties and either a `sourceTable` section
(for landing, lake landing, registered, and streaming landing task types) or an
`inputDatasets` section (for all other task types), followed by any explicit rules.

## Transformation data flow files

The `transformationDataFlows/` folder is present for transform task types when the task contains transformation flows.
Each flow is a separate YAML file named after the flow.
