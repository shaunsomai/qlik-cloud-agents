---
source: https://qlik.dev/toolkits/qlik-cli/qlik-cli-qrs-get-started/
last_updated: 2026-01-26T09:52:22+01:00
---

# Using qlik-cli with Qlik Sense Enterprise client-managed Repository API (QRS)

## Overview

In this tutorial, you are going to learn how to authorize qlik-cli to connect to
Qlik Sense Enterprise client-managed instances using JSON web tokens (JWT).

- Create a public / private key pair for signing JWTs
- Configure JWT virtual proxy
- Create a JWT
- Configure a context in qlik-cli
- Test the connection
- Review the available Qlik Repository Service (QRS) commands
- Review the Token.js code

## Requirements

- qlik-cli version 1.5.0 or higher
- A Qlik Sense Enterprise client-managed instance
- Access to create virtual proxies in Qlik Sense. This demo uses
  an account with the *RootAdmin* role assigned.

## Configure JWT virtual proxy

To configure a JWT virtual proxy, follow the instructions in [JWT authentication](https://help.qlik.com/en-US/sense-admin/latest/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/JWT-authentication.htm), which includes information on how to:

- Create a public/private key pair.
- Configure a virtual proxy for JWT in Qlik Sense Enterprise on Windows.
- Create a JWT using Token.js.

## Configure a context in qlik-cli

Open a terminal window and use the context command to add the Qlik Sense
Enterprise on Windows server to qlik-cli.

```shell
##qlik context create <contextName> --server <serverUrl> --server-type windows --api-key <JWTToken>

qlik context create QSEoW --server https://192.168.254.243/jwt --server-type windows --api-key eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiJoYXJyeSIsInVzZXJkaXJlY3RvcnkiOiJxc2VmdyIsIm5hbWUiOiJIYXJkY29yZSBIYXJyeSIsImVtYWlsIjoiaGFycnlAZXhhbXBsZS5jb20iLCJncm91cHMiOlsiQWRtaW5zdHJhdG9ycyIsIlNhbGVzIiwiTWFya2V0aW5nIl0sImlhdCI6MTYwMzgxOTYyOSwiZXhwIjoxNjM1MzU1NjI5LCJhdWQiOiIxMTJhZGFtcyJ9.gDWFqJ8fZbo9QpF52CnlhKCMsHal2AcobIVwhVCpnbLfpmc-Z_k4uUWGh2TxaSucjQ5-k5I9s9sNgIPskqaVQN2JanFXxIJKRFow9LbuSbImZs74RsQ6TqsoJTu7_5eKLv2VRAqoh6Tqabl5vma1JdhHbsTKGixt8yGZI7Q2QNjObQq8hAh6VveNWcUVkB60LEMOPiipij7VTKQ7IQg-rG4XA8xgYxbOb6i3Q6miY4kGSGujbsjtYLevEJQlEZtij2JMMDeH_nwH2MWhWhOBL1TpAAUKkCOxPFDjGacxGvkObAOFjL-Ztx0LdVwF2BXxVerQ1xKyl0YpLErS4d576Q
```

To use the context after setting it, enter `qlik context use <contextName>`

## Test the connection

In the terminal window opened earlier, test the connection by entering the
command to list the applications on the server.

> **Note:** Access QRS commands in qlik-cli starting with `qlik qrs`. In addition, when you
> connect to the server using the qlik-cli, if there is no trusted certificate
> installed on the system certificate validation fails. Instruct qlik-cli to
> ignore certificate validation errors by using the `--insecure` flag.

```bash
# set the context to the Qlik Sense Enterprise on Windows server
# replacing <contextName> with the context name set in qlik-cli
# qlik context use <contextName>

qlik context use QSEoW

# list the applications on the server

qlik qrs app ls --insecure
```

```json
// returns JSON like below
[
  {
    "id": "931d847e-b36a-4511-9547-6cc0f46b1b9c",
    "name": "ConsumerSales",
    "appId": "",
    "publishTime": "2020-10-21T12:48:16.987Z",
    "published": true,
    "stream": {
      "id": "387f4d65-c171-4120-9db0-3cd537b469a8",
      "name": "CNPDemo",
      "privileges": null
    },
    "savedInProductVersion": "12.688.0",
    "migrationHash": "64d115e925e2167bba72939c2d8a80e6beef4a56",
    "availabilityStatus": 5,
    "privileges": null
  }
]
```

## List of available Qlik Repository Service (QRS) commands

Here is a list of commands available in qlik-cli to interact with QRS.

```shell
qlik qrs --help

Usage:
  qlik qrs [flags]
  qlik qrs [command]

Available Commands:
  app                           Manage apps
  appcontent                    Upload or remove content used in apps
  applicationlog                Get the log for a specific application
  appstatus                     Get migration status of an app
  binarydownload                Download binary
  cache                         Empty the cache in the Qlik Sense Repository Service (QRS)
  compositeevent                Manage composite event triggers for specific
                                tasks e.g. reload
  compositeeventoperational     Get the status of a composite event
  compositeeventruleoperational Get the rule status of a composite event
  contentlibrary                Manage static content that can be used in
                                e.g. Qlik Sense apps
  custom                        Manage custom resources
  custompropertydefinition      Manage custom properties that can be applied to a resource
  dataconnection                Manage data connections that enables selection
                                and loading of data from different data sources
  download                      Download exported apps, reload tasks or
                                SAML metadata
  executionresult               Get the execution result for a specific task
  executionsession              Get the status of a specific task during execution
  extension                     Manage extensions used for apps
  managementconsolelog          Get the log for the management console
  reloadtask                    Create reload tasks and corresponding triggers (events)
  reloadtaskoperational         Get the status of a reload task
  schemaevent                   Manage schema event triggers
  schemaeventoperational        Get the status of a schema event
  selection                     Manage selections that refer to a specific enitity type
  servicestatus                 Get status of the service
  staticcontent                 Get a list of the static content files in,
                                for example, a content library.
  staticcontentreference        Get the mapping between the external path
                                and the physical file in the repository
                                for all static content
  staticcontentreferencebase    Get the mapping between the external path and
                                the physical file in the repository for base
                                static content
  stream                        Manage streams that are used for published apps
  tag                           Manage tags that can be applied to a resource
  task                          Manage tasks that can be executed by
                                the Qlik Sense Scheduler
  taskoperational               Get status of a task
  user                          Manage resources owned by a specific user
  userdirectory                 Manage user directory connectors (UDCs)
```

## Token.js code sample

This is the full code to generate a JWT.

`embed:./snippets/qlik-cli-qrs-get-started/token.js`
