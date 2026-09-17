---
source: https://qlik.dev/manage/analytics-applications/task-chaining-qlik-cli/
last_updated: 2026-04-20T13:34:03+01:00
---

# Task Chaining with qlik-cli

## Overview

In this tutorial, you are going to learn how to use the [Reloads API](https://qlik.dev/apis/rest/reloads)
to create tasks, loop to catch reload status changes, and set up task chaining using
a script. This solution monitors Qlik Cloud for reload completion.

If you are new to this topic, first read the [reloads overview](https://qlik.dev/manage/analytics-applications).

For a code-free option using events, review how
to [chain reloads in Qlik Automate](https://qlik.dev/manage/analytics-applications/task-chaining-automations).

## Prerequisites

- [qlik-cli version 1.0.0](https://qlik.dev/toolkits/qlik-cli) or greater
- A text editor for manipulating PowerShell or Bash scripts

## Reload using CLI basics

You can access reloads using qlik-cli through the `qlik reload` command. Running
the command with the `--help` flag lists the different sub-commands and flags
available.

## Create a reload task

To use the create command, first obtain the app metadata of the application
using the item command.

`embed:./snippets/qlik-cli-snippets/create-reload.ps1#L5-6`

> **Note:** Qlik Sense Apps in Qlik Cloud have an `itemId` and a `resourceId`.
> The resourceId is often referred to as the appId and is a GUID.
> The `itemId` is the unique ID of the app in the items collection.

Issue the create command referencing the `resourceId` property from the app
metadata object.

`embed:./snippets/qlik-cli-snippets/create-reload.ps1#L9,11`

The response returns all of the relevant information related to the
newly created reload entity. If you add a `-q` to the end of the CLI command,
only the `ID` for the reload task is returned. This can be useful when chaining
multiple commands together.

```json
{
  "appId": "dae9a0b6-ef7b-4cf5-8153-126ef9aef3b0",
  "creationTime": "2020-06-29T13:32:03.833Z",
  "id": "5ef9ed53a45bbd0001116aa9",
  "status": "CREATED",
  "tenantId": "TohbNbUjAGrVXhrvVujU73hzgDQ6DxnG",
  "type": "hub",
  "userId": "BewQZxFax8r47sLrGUmfy4K8YKzYAkjA"
}
```

## Check reload status

Check the status of the reload you created by using the `get` command and
passing the item ID. The item ID is the value in the response from the `create`
command.

`embed:./snippets/qlik-cli-snippets/create-reload.ps1#L14-15`

Because the reload API is RESTful, the commands in the CLI are
request/response in nature. The system doesn't notify you when the reload
reaches a completed state. To evaluate the status of reloads, put the `get`
command in a loop.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L34-41,75`

As long as the status of the reload isn't `SUCCEEDED` or `FAILED`, the loop keeps
running.

## Task chaining example

The ability to execute a reload upon the completion status of a preceding reload
is a desired capability in the Qlik platform. Task chaining, as this process is
commonly called, needs to be able to accept an instruction set to know what to do
based on the outcome of a previously run reload. qlik-cli isn't opinionated
with regard to the instruction set because there aren't specific task chaining
commands available in the tool. That said, functions like the `loopReloadStatus`
example and a mechanism to facilitate the next step in an instruction set
use the standard reload CLI commands, giving you the flexibility to design an
instruction set that works for your requirements.

### Make a task chain instruction set

In this example, the instruction set is a JSON array with simple logic. Each
entry in the array has a `name` for the task, the name of the Qlik app to `run`
the reload command, the array item (by number) to go to next upon a `SUCCEEDED`
reload outcome, and the array item (by number) to go to next upon a `FAILED`
outcome. A `-1` value in the succeed or failed properties instructs the process
to end.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L7-12`

### Check reload success or failure

The [Check reload status](#check-reload-status) section covers the
`loopReloadStatus` function that observes the reload task status before going
to the next step.

### Run the task chain

To run the task chain in a logical fashion, employ another function called
`runTaskChainItem` that accepts two arguments: one passing the instruction set,
the `$taskObject` and another passing the specific item to run, the `$task`.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L45-46,70`

The function gets the app name to reload and calls `qlik item ls` to retrieve
the application properties.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L49-50`

With the app properties returned, run `qlik reload create` passing the
`resourceId` from the app properties to start the reload task.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L54`

Once created, the `loopReloadStatus` function is run passing in the reload ID
from the previous command. The function loops until a success or failure
status prints in the response from the tenant.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L55`

The `$reloadResult` variable contains `SUCCEEDED` or `FAILED` for a value. The
next command evaluates the value to return from a matching property name.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L59`

Based on the `$result` variable value, the function either runs the
corresponding task item in the instruction set or finishes running.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L63-68`

Now that the functions and instruction set are written, call the
`runTaskChainItem` function.

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1#L73-74`

## Summary

Reloading apps is useful to obtain the latest data for a
Qlik app. But for large deployments, reloads are multi-layered and often
generate datasets as part of a downstream app reload. That's why chaining
reloads together is so useful. Using qlik-cli, you can combine reloads and tasks
with operational workflows from other applications to increase efficiency and
automate insight to action.

## Complete scripts

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.ps1`

`embed:./snippets/qlik-cli-snippets/reload-task-chaining.sh`
