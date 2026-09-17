---
source: https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/
last_updated: 2026-09-07T10:22:18+02:00
---

# Set up your development environment for declarative pipelines

## Overview

This guide covers setting up VS Code with YAML schema validation to edit Qlik pipeline YAML
files with autocompletion and inline error detection. VS Code is the recommended editor for
this workflow, but you can use any editor that supports YAML schema validation.

## Prerequisites

- A Qlik Cloud pipeline project connected to GitHub version control.
  For setup steps, see
  [Manage your pipeline projects with version control](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/VersionControl/Project-version-control.htm).
- A GitHub account with read access to the repository that contains the project.
- [Git](https://git-scm.com/downloads) installed on your machine.

## Step 1: Install the Red Hat YAML extension and configure schema validation

The [Red Hat YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
adds schema-based autocompletion and inline validation to the VS Code YAML editor.

1. Open VS Code.
2. Go to **Extensions** (Ctrl+Shift+X on Windows, Cmd+Shift+X on macOS).
3. Search for `YAML` and install the extension published by **Red Hat**.

Qlik pipeline YAML schemas are published to [SchemaStore.org](https://www.schemastore.org/).
The Red Hat YAML extension automatically downloads schemas from SchemaStore
and applies them based on file naming conventions. Files named `qtcp_project.yaml` and files
under `qtcp_tasks/` are recognized automatically.

With schemas configured, VS Code shows:

- Inline errors for invalid or missing required properties.
- Autocompletion suggestions as you type property names.
- Hover documentation for each property.

## Step 2: Use AI assistants to configure pipelines

Use AI assistants (such as GitHub Copilot or Anthropic Claude) to streamline YAML configuration creation and editing.
To ensure accuracy and adherence to project standards, follow these best practices:

1. Select a high-capability model. Use a premium, large-context model (for example, Anthropic Claude Sonnet 4.6 or
   higher) rather than a standard or "auto" model for complex YAML generation and schema adherence.
   Advanced models correctly interpret complex pipeline schemas and produce more accurate configurations.
2. Configure project-specific AI instructions. Improve AI-generated configuration quality by providing project context
   to the model.
   Create an instruction file in the root of your VS Code workspace. Choose one of the following:

   - CLAUDE.md (for Anthropic Claude Code extension)
   - .github/copilot-instructions.md (for GitHub Copilot)

   The content of your instruction file should be as follows:

   ```text
   This is a Qlik Talend Cloud Pipeline (QTCP) project.
   Before any project advice or YAML edits, I MUST read the source of truth first:
   https://raw.githubusercontent.com/qlik-oss/schemas/refs/heads/main/qtcp/ai-instructions.md
   ```

### Use AI assistants with Qlik MCP tools

When you deploy a Qlik MCP server in your tenant, AI assistants can use dedicated MCP tools to help manage
pipeline projects programmatically.

**MCP prerequisites**

- Qlik MCP server is deployed in your tenant.
- You have the **Qlik MCP: Allowed** permission assigned through a custom role.
- You have permissions to create or edit pipeline projects.
- An AI client with MCP support (such as VS Code with GitHub Copilot) is configured to use the Qlik MCP server.

**Available MCP capabilities for data pipelines:**

AI assistants can use the following capabilities to configure and manage pipeline projects:

- Search for spaces, connections, or projects (`qlik_search`): get a list of available spaces, data connections, or
  pipeline projects.
- Search for connection objects (`qlik_search_connection_objects`): discover available tables and views from a data
  connection.
- Get pipeline project details (`qlik_get_pipeline_project_details`): retrieve project binding values.

**Related resources:**

- To deploy the MCP server, see [Qlik MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm)
  on Qlik Help.
- For detailed MCP tool documentation, see [Qlik MCP tools](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server-tools.htm)
  on Qlik Help.
- For permission requirements, see [Qlik MCP server access and permissions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-Permissions.htm)
  on Qlik Help.

## Step 3: Clone the repository

You can clone the GitHub repository containing your pipeline project using VS Code's built-in Git features or your
preferred Git method.

> **Tip:** VS Code has built-in Git functionality.
> You can use the Source Control panel (`Ctrl+Shift+G` on Windows, `Cmd+Shift+G` on macOS)
> to clone a repository directly, or use the command line if you prefer.

1. Clone the repository to your local machine.
2. Open the project folder in VS Code.
   You should see the project YAML files in the Explorer panel.
3. Open `qtcp_project.yaml` to confirm that schema validation is active.
   VS Code displays the associated schema for the open YAML file.
   Hover over a property to view its documentation.

## Using schemas with other IDEs

Qlik publishes pipeline YAML schemas to [SchemaStore.org](https://www.schemastore.org/) and
maintains them in the
[qlik-oss/schemas GitHub repository](https://github.com/qlik-oss/schemas/tree/main/qtcp).

Most editors that support JSON Schema validation can use these schemas. The general approach is:

1. Locate the schema for the file type you want to validate. Browse the
   [qlik-oss/schemas repository](https://github.com/qlik-oss/schemas/tree/main/qtcp) or search
   the [SchemaStore catalog](https://www.schemastore.org/json/) for entries starting with `qtcp`.
2. Configure your editor to associate the schema URL with the corresponding file pattern:
   `qtcp_project.yaml` for the project file, or the task file pattern under `qtcp_tasks/`.
   The configuration method varies by editor. Refer to your editor's documentation for details.

## Next steps

With your environment set up, you can
[edit a declarative pipeline with version control](https://qlik.dev/manage/di-projects/declarative-pipelines/edit-with-version-control/).
