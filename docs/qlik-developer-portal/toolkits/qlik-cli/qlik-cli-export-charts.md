---
source: https://qlik.dev/toolkits/qlik-cli/qlik-cli-export-charts/
last_updated: 2026-01-19T14:21:00Z
---

# Export charts from Qlik Sense apps for non-interactive use

This guide demonstrates how to export chart objects from a Qlik Sense app using
[qlik-cli](https://qlik.dev/toolkits/qlik-cli/) and a bash or Powershell script. This is useful
for automation, documentation, embedding, or further analysis outside of Qlik Sense.

## Prerequisites

- [qlik-cli](https://qlik.dev/tools/qlik-cli/) installed on a computer with bash
  or Powershell available.
- If running this script against a Qlik Cloud tenant, create or activate a
  [qlik-cli context for Qlik Cloud](https://qlik.dev/toolkits/qlik-cli/qlik-cli-contexts/#creating-a-new-context-for-qlik-cloud).
- IIf running this script against a Qlik Sense Enterprise client-managed site, create
  or activate a [qlik-cli context for Qlik Sense Enterprise client-managed](https://qlik.dev/toolkits/qlik-cli/qlik-cli-qrs-get-started/).
- Access to the app you want to export objects from with the configured context
  and user defined in the context (which may not be the same user as your interactive
  login user if using JWT or OAuth2).
- If following the bash example:
  - [jq](https://stedolan.github.io/jq/) installed for JSON processing.

## Usage

These scripts can be run manually, or by an external scheduler to create JSON files
containing the current visible data for Qlik Sense charts.

In Qlik Sense Enterprise client-managed, this can be run on a scheduler node on the
site using an [external program task](https://help.qlik.com/en-US/sense-admin/latest/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/create-edit-external-program-tasks.htm)
that it is triggered immediately after a Qlik Sense app is reloaded.

## Output

- Each exported object will be saved as `<appId>/<objectId>.json` in the current directory.
- Only objects matching the allowed types will be exported.

## Code example

Both examples will work against either Qlik Cloud or Qlik Sense Enterprise client-managed,
but are included because it's often easier to run Powershell natively on Windows servers
for client-managed.

### Bash

Export all default chart types from an app:

```sh
./get-all-app-objects.sh 0ef9c2e0-a9d7-4a54-912b-1d982effdf38
```

Export only barcharts and piecharts:

```sh
./get-all-app-objects.sh 0ef9c2e0-a9d7-4a54-912b-1d982effdf38 barchart,piechart
```

`embed:./snippets/qlik-cli-snippets/get-all-app-objects.sh`

### Powershell

Export all default chart types from an app:

```powershell
./get-all-app-objects.ps1 -appId 0ef9c2e0-a9d7-4a54-912b-1d982effdf38
```

Export only barcharts and piecharts (comma-separated list):

```powershell
./get-all-app-objects.ps1 -appId 0ef9c2e0-a9d7-4a54-912b-1d982effdf38 -allowedTypes barchart,piechart
```

If you are running this locally on a Qlik Sense Enterprise client-managed site,
you may be using unsigned certificates, in which case use the `-insecure` flag.

This can be configured as an external program task in Qlik Sense Enterprise client-managed.
As an example, on Windows Server 2019, the task should be created with a config like this:

- Path: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
- Parameters: `\\server\QlikShare\scripts\get-all-app-objects.ps1 -appId b1e3643e-c2c6-4e35-a11d-5b6ce1815c7e -insecure`

This assumes your script is stored on your central share. You can then add triggers
which are hooked onto reload tasks to initiate the export immediately after the
app is reloaded.

`embed:./snippets/qlik-cli-snippets/get-all-app-objects.ps1`
