---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/
last_updated: 2026-06-30T16:46:02Z
---

# Declarative pipelines

## Overview

A declarative pipeline is a representation of a pipeline project as YAML configuration files.
Instead of building pipelines exclusively through the Qlik Cloud user interface, teams maintain
human-readable configuration files in their IDE (Integrated Development Environment), review changes, and deploy
to Qlik Cloud using version control or import capabilities.

Declarative pipelines let data and platform teams apply standard engineering practices to data
pipelines: version control, code review, validation, and repeatable multi-environment
deployments from development to production.

Because YAML stores the pipeline configuration, changes are readable, comparable in a diff,
reusable across environments, and accessible to version-control, API, and automation tooling.

GitHub version control is the recommended workflow for collaborative authoring and CI/CD practices.
Export and import are also supported for deployment and promotion scenarios, including headless
workflows that use the [API](https://qlik.dev/apis/rest/di-projects/).

## When to use declarative pipelines

Use declarative pipelines when you need to:

- **Define pipelines in code**: manage pipeline configuration as YAML files to enable
  continuous integration and deployment automation.
- **Deploy across environments**: promote the same pipeline definition across development,
  verification, and production while supplying environment-specific binding values.
- **Reuse and share definitions**: reuse pipeline definitions as templates across projects or teams
  to maintain consistency and reduce duplication.
- **Automate at scale**: create and update projects programmatically without manual work
  in the Qlik Cloud user interface.

You might not need declarative pipelines for small, one-off projects managed through the
Qlik Cloud user interface in a single environment with no automation or collaboration
requirements.

## How it works

When a project is connected to GitHub version control, Qlik Cloud exports the project configuration
as YAML files and stores them in the repository. Changes made in the Qlik Cloud user interface are
committed to the repository when you select **Commit changes** in the project. Changes pushed
to GitHub from your IDE are applied to Qlik Cloud when you select **Apply remote changes**
in the project.

Both directions are supported, which means you can start designing a project in the user
interface and switch to code-first editing at any point, or manage the pipeline entirely from
code. Once your project is connected to a repository, you can work on it from any IDE or
machine, making the project portable across teams and environments.

## End-to-end workflow

The following steps describe how each part of the Declarative Pipelines workflow connects,
from retrieving project files to running a pipeline in the target environment.

Before you start, set up your development environment with YAML schema validation.
See [Set up your development environment](https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/).

1. **Retrieve the project files**: clone the GitHub repository to your machine, or export the
   project as a ZIP from Qlik Cloud. The project files include `qtcp_project.yaml`,
   `qtcp_bindings_definition.json`, and task files under `qtcp_tasks/`.

2. **Edit locally**: open the project YAML files in your IDE and make changes. Schema validation
   highlights errors in real time. For complex configurations, configure an AI assistant with
   the project instructions file to help generate and refine YAML.

3. **Validate**: check the VS Code Problems panel for schema errors before committing.
   For a pre-import check, call the validation API on a project ZIP.
   See [Validate a pipeline configuration](https://qlik.dev/manage/di-projects/declarative-pipelines/validate-configuration/).

4. **Commit or package**: push changes to GitHub (version-control workflow) or export the
   project as a ZIP file (export and import workflow).

5. **Deploy to Qlik Cloud**: bring the changes into the target project:

   - Version-control workflow: select **Apply remote changes** in the target project.
   - Export and import workflow: call the import API or import from the Qlik Cloud user interface.

   See [Edit with version control](https://qlik.dev/manage/di-projects/declarative-pipelines/edit-with-version-control/)
   and [Export and import a pipeline configuration](https://qlik.dev/manage/di-projects/declarative-pipelines/export-and-import/).

6. **Set binding values**: confirm that environment-specific binding values are set on the target
   project before running the pipeline.

7. **Run and monitor**: schedule and run the pipeline through the Qlik Cloud user interface or
   the [Data integration projects API](https://qlik.dev/apis/rest/di-projects/).

## Project structure

A declarative pipeline project uses the same folder layout regardless of how you work with it:
connected to a GitHub repository, exported as a ZIP file, or both.

For a reference to the files and folders that can appear in a project package, see
[Project structure reference](https://qlik.dev/manage/di-projects/declarative-pipelines/project-structure-reference/).

## Environment promotion with binding variables

Pipeline properties often differ between environments. A source connection name in development
may not match the same connection in production. A Snowflake warehouse name may vary per
environment.

Binding variables let you define environment-specific values as placeholders in YAML task files
using the syntax `{{variable-name}}`. You declare every variable in `qtcp_bindings_definition.json`
before referencing it in a task file. This file is part of the project definition and is committed
to the repository in the version-control workflow, or included in the ZIP file when doing an export.

> **Note:** For YAML-based declarative pipeline projects, binding variable definitions are stored
> in `qtcp_bindings_definition.json`.
>
> For Legacy exports or existing GitHub projects that still use the JSON-based format,
> the equivalent file is named `bindingTemplate.json`.

How you provide the actual values for each environment depends on the workflow you use:

**Version control-based workflow:** binding values are stored in Qlik Cloud, not in a file in
the repository. Set or update them by applying remote changes through the Qlik Cloud user interface
or by uploading them using the [Bindings API](https://qlik.dev/apis/rest/di-projects/#put-api-v1-di-projects-projectId-bindings/).

**Export-based workflow:** binding values can be included in an exported package as `bindings.json`
when the export request includes `includeBindings: true`. The `bindings.json` file is always JSON,
even when the project definition uses YAML.

All other project files stay identical across environments, which minimizes errors and keeps
code reviews focused on actual logic changes. This separation also makes the project portable:
the same YAML files run in any environment by providing the correct binding values.

> **Warning:** If a binding variable is referenced in a YAML task file but is not defined in
> `qtcp_bindings_definition.json`, applying or importing the project can fail.
> Add the variable to `qtcp_bindings_definition.json` before referencing it in a task file.

## Choose your workflow

Select the workflow that matches how you author, review, and deploy pipeline changes.

### Version control-based workflow

Connect an existing Qlik Cloud project to GitHub using the built-in version control user
interface. The project YAML files are stored in your repository and can be cloned to any
machine. Edit the files in your preferred IDE, commit and push the changes to GitHub, and
apply them to Qlik Cloud using **Apply remote changes**.

> **Note:** Version-control commits do not include `bindings.json`.
> Binding values remain stored in Qlik Cloud.

For detailed setup steps, see [Set up your development environment](https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/)
and [Edit a pipeline configuration with version control](https://qlik.dev/manage/di-projects/declarative-pipelines/edit-with-version-control/).

### Export-based workflow

Export a project ZIP from Qlik Cloud using the API or the user interface, edit the YAML files,
and import the revised package into a target project. Use this approach across tenants or in
environments where version control is not connected.

When exporting through the API, you can use the `mode` field to choose the export mode:

- `MINIMAL`: YAML project structure with default values omitted. (default)
- `ALL`: YAML project structure with all values included.
- `LEGACY`: legacy JSON project structure.

Use `MINIMAL` exports for day-to-day exports.
The resulting YAML contains only properties that differ from server defaults, which keeps diffs clean and pull requests
easy to review.

Use `ALL` when you need to inspect all available properties or discover the full schema.

Use `LEGACY` only for backward compatibility with older import workflows.

## Version control migration

If your project is already connected to GitHub using the older JSON-based format,
you can upgrade to the new YAML structure directly from the Qlik Cloud user interface.

For more information, see the
[migration process](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Retrieving-editing-pipeline-configuration.htm#Migrate)
on Qlik Help.
