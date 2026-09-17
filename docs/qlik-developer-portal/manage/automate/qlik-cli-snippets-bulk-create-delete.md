---
source: https://qlik.dev/manage/automate/qlik-cli-snippets-bulk-create-delete/
last_updated: 2025-07-08T16:09:30Z
---

# Creating and deleting apps in bulk with qlik-cli

## Overview

This tutorial covers bulk creation and deletion of apps featured in the "Do More
with Qlik" webinar series.

You can watch the video here.

You are going to learn how to perform bulk operations using qlik-cli with
PowerShell and Bash.

## Prerequisites

- [qlik-cli@1.00](https://qlik.dev/toolkits/qlik-cli) or greater
- A text editor for manipulating PowerShell or Bash scripts

## Creating apps and retrieving appIds

Consider a scenario where you need to automate creating multiple Qlik apps at
one time. You work for a commercial power company and need to slice apps by
region so the sales teams only see the relevant information related to their
territory. As the BI administrator, you don't want to have to do this slicing
manually so you open PowerShell and write the following code.

### PowerShell createApps

Begin with creating a function in the PowerShell script that checks if an
app exists in the tenant.

`embed:./snippets/qlik-cli-snippets/createApps.ps1#L5-9`

The `appExists` function takes an `appName` parameter and sends the value to
qlik-cli using the item list command. The command pipes the response to the
`ConvertFrom-Json` function to transform the content into a `system.object`
type. The return value is the resource ID for the app, also known as the appId.

Next, create an empty array for collecting the appIds returned in this script.

`embed:./snippets/qlik-cli-snippets/createApps.ps1#L12`

From the example in the video, a for loop counts from 0 to 9 to generate fake
app names. In a real-life example, you may have an array of values or app names
available to pass into the loop.

`embed:./snippets/qlik-cli-snippets/createApps.ps1#L16-28,31`

The for loop takes the value passed in and appends it to the app name. Then,
the appExists function is called to evaluate if the app exists in the tenant. If
the app doesn't exist, the `qlik app create` command using the
`--attributes-name` flag is used to pass the name for the new app along with
`-q` which quiets the response from the CLI to provide only the appId. The appId
gets piped out to a string stored in the `$app` variable and is added to the array.

As the script completes, the contents of the array are returned to the calling
command.

### Bash createApps

Bash scripting is a bit different than PowerShell, but equally as powerful. Here
is how the script compares.

Like the previous script, begin with creating a function in the Bash script that
evaluates if an app exists in the tenant.

`embed:./snippets/qlik-cli-snippets/createApps.sh#L6-10`

Some subtle differences can be seen here from the PowerShell version.
The app name parameter is passed in as a generic argument `${1}` and is sent
through to qlik through `qlik item ls` using the `--name` flag. The response
is piped to jq, a JSON parser for Bash, assigning the raw resourceId response
to the `result` variable. If the result is empty, the function returns
`null`, otherwise it sends back the appId.

Next, create an empty array for collecting the appIds returned in this script.

`embed:./snippets/qlik-cli-snippets/createApps.sh#L13`

Bash does for loops a bit differently than PowerShell. In this example, supplying
a range to iterate through helps create the app name. The appExists
function is called to evaluate if the app exists in the tenant.
If the app doesn't exist, the `qlik app create` command using the
`--attributes-name` flag is used to pass the name for the new app along with
`-q` which quiets the response from the CLI to provide only the appId. The appId
gets piped out to a string stored in the `$app` variable and added to the array.

`embed:./snippets/qlik-cli-snippets/createApps.sh#L17-33`

As the script completes, the contents of the array are returned to the calling
command.

`embed:./snippets/qlik-cli-snippets/createApps.sh#L36`

Running these scripts results in the creation of ten apps in your tenant. You can
copy the scripts in their entirety in the [Complete scripts](#complete-scripts)
section below.

## Deleting apps in case you want to start over again

Sometimes, automating app creation can lead to some unfavorable app creep in
your tenant. Here are PowerShell and Bash scripts for deleting apps from a
tenant.

### PowerShell deleteApps

qlik-cli's `item ls` command has a `--name` switch you can use to return items
matching a string pattern. In this example, the `--resourceType` switch limits
results to apps and the `--limit` switch controls how many results are returned
in a single call.

`embed:./snippets/qlik-cli-snippets/deleteApps.ps1#L5`

Take the list of apps returned from the item command and use `ConvertFrom-Json`
to change the variable into a `system.object` collection.

`embed:./snippets/qlik-cli-snippets/deleteApps.ps1#L8`

Loop through the objects and use the app command to remove the app completely
from the tenant.

`embed:./snippets/qlik-cli-snippets/deleteApps.ps1#L10-16`

### Bash deleteApps

qlik-cli's `item ls` command has a `--name` switch you can use to return items
matching a string pattern. In this example, the `--resourceType` switch limits
results to apps and the `--limit` switch controls how many results are returned
in a single call.

With Bash, jq is used to parse the JSON response from the items API. The jq
command `jq -r '.[] | .resourceId'` loops through the JSON array.

`embed:./snippets/qlik-cli-snippets/deleteApps.sh#L7-8`

Loop through the objects and use the app command to remove the app completely
from the tenant.

`embed:./snippets/qlik-cli-snippets/deleteApps.sh#L10-15`

## Complete scripts

### PowerShell scripts

`embed:./snippets/qlik-cli-snippets/createApps.ps1`

`embed:./snippets/qlik-cli-snippets/deleteApps.ps1`

### Bash scripts

`embed:./snippets/qlik-cli-snippets/createApps.sh`

`embed:./snippets/qlik-cli-snippets/deleteApps.sh`
