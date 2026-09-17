---
source: https://qlik.dev/manage/reports/deploy-tabular-reports/
last_updated: 2026-04-20T13:34:03+01:00
---

# Deploy Tabular Reports

## Overview

In this tutorial, you are going to learn how to deploy a Tabular Report between a development
and test space in a Qlik Cloud tenant. This is relevant for the following use cases:

- When you want to use practices such as Continuous Integration, Continuous Deployment (CICD), and DevOps.
- When you want to support third party backup and restore.
- When you want to handle multitenant or OEM use cases where each of your customers requires their own report
  deployment.

The same pattern can be used whether you use a single tenant, or more than one
tenant in Qlik Cloud.

If you want to see this working end to end, the [example API collection](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/deploy-tabular-reports)
can be run in tools such as Postman. This includes built-in tests to
handle passing variables between steps, and is configured to use OAuth M2M credentials.
The flow is slightly different to this tutorial, but the same concepts are covered.

If you're new to reporting in Qlik Cloud, review the [manage reports overview](https://qlik.dev/manage/reports/)
to understand the reporting capabilities available to you.

## The services behind a Tabular Report

The Tabular Reporting capability relies on the following services:

- [Qlik Sense apps](https://qlik.dev/apis/rest/apps/): contain objects,
  definitions, distribution lists, data, filters, and more, which are used within
  both the template and task definition.
- [Report templates](https://qlik.dev/apis/rest/report-templates/): store the Excel
  templates which contain the layouts, configuration, and styling for the generated output.
- [Report tasks](https://qlik.dev/apis/rest/sharing-tasks/): define the criteria
  for when reports will be generated, and who will receive them.

This tutorial will guide you through the API calls required to export, import, and
execute the generation of a tabular report output for a new Qlik Sense application.

## Distribution list good practices

If your target app distribution list is different than your source app distribution
list, you should configure the source Report Task with Groups that are common
between the two distribution lists. Avoid using named users in the Report Task
configuration.

Additionally, once landed, execute a Target App reload to ensure that the target
distribution list has been updated in the target apps prior to any reports being
generated.

## Requirements

- A Qlik Sense app with a deployed report task. You can download example assets from the
  [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/deploy-tabular-reports/example-assets)
  to import the app and create the report task in your own tenant.
- An access token or API key for a user with access to both the source and target spaces -
  see [Authentication](https://qlik.dev/authenticate).
- cURL for running the inline examples.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable               | Description                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `<HOSTNAME>`           | The hostname for your tenant. Such as `tenantname.region.qlikcloud.com`.                                                                        |
| `<ACCESS_TOKEN>`       | A bearer token for authorizing `https` requests to the `<HOSTNAME>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<SOURCE_APP_ID>`      | The ID of the source app, which will be duplicated into the target space.                                                                       |
| `<EXPORT_PATH>`        | The path in the temp-contents service into which the app export was generated.                                                                  |
| `<APP_FILE>`           | The local path to the app that you download from the `<EXPORT_PATH>`.                                                                           |
| `<SOURCE_TEMPLATE_ID>` | The ID of the template associated with the source app.                                                                                          |
| `<TEMPLATE_FILE>`      | The local path to the template that you download from the `<SOURCE_TEMPLATE_ID>`.                                                               |
| `<TARGET_SPACE_ID>`    | The ID of the shared space into which the app and associated content will be deployed.                                                          |
| `<TARGET_APP_ID>`      | The ID of the Qlik Sense app imported to the target space, `<TARGET_SPACE_ID>`.                                                                 |

## 1 Generate credentials

An access token or API key for a user with access to the content you wish to migrate (via space roles) -
see [Authentication](https://qlik.dev/authenticate).

The access token will be referred to as `<ACCESS_TOKEN>`.

## 2 Export content

Export the app and relevant report content from the source space, prior to importing
into the target space. You could amend this step to optionally store this data into a
version control repository, such as GitHub, to support a GitOps integration.

Make a note of how to export each piece of metadata:

- Qlik Sense App: can be exported as a binary file, with or without data, from `/apps`.
- Report Tasks: exported as JSON objects from `/sharing-tasks`.
- Report Filters: exported as part of the Qlik Sense app, or independently via `/apps`.
- Report Recipients & Groups: exported as part of the Qlik Sense app.
- Report Templates: exported as a JSON object and an associated `.XLSX` template file
  from `/report-templates`.

### 2.1 Export the Qlik Sense app

Report templates and task definitions relate to a specific app, meaning you should aim to keep the
exported app in sync with the exported templates and tasks. If you later try to import
templates against an app where the object IDs or other properties differ, you will
experience errors.

To request an export of the source Qlik Sense app:

```bash
curl -L -X POST "https://<HOSTNAME>/api/v1/apps/<SOURCE_APP_ID>/export" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The response will return a `201` status if successful, with an empty body. Retrieve
the download path for the app from the `Location` key in the response headers:

```json
Location: <EXPORT_PATH>
```

The `<EXPORT_PATH>` will look like `/api/v1/temp-contents/65785b6e3c03abccc03dda36`.

Once the export has been created, download it:

```bash
curl -L "https://<HOSTNAME><EXPORT_PATH>" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The response will be the app binary file, record the local path to the file as `<APP_FILE>`.

### 2.2 Export the report task definition

Retrieve the report tasks defined against the source application. A report task
can reference only one report template, but there may be multiple report tasks
per application:

```bash
curl -L "https://<HOSTNAME>/api/v1/sharing-tasks?appid=<SOURCE_APP_ID>&type=template-sharing" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

You will receive a `200` response, and a list of report tasks if successful:

<details>
  <summary>Example JSON response</summary>

  This example
  shows a single report task definition, and key values listed as variables.

  ```json
  {
      "currentPageCount": 1,
      "totalCount": 1,
      "links": {
          "self": {
              "href": "https://<HOSTNAME>/api/v1/sharing-tasks?appid=<SOURCE_APP_ID>&type=template-sharing"
          }
      },
      "sharingTasks": [
          {
              "appId": "<SOURCE_APP_ID>",
              "appName": "Reporting App Example",
              "createdBy": "6560c8259181e895e9470b0c",
              "dateCreated": "2023-11-30T14:20:16Z",
              "description": "The first report task on this Qlik Sense app",
              "distributionListId": "6569de4293a86697c382942c",
              "emailContent": {
                  "body": "This exceptions report is generated daily via this report task",
                  "subject": "Daily exceptions report"
              },
              "enabledBySystem": true,
              "enabledByUser": true,
              "id": "<SOURCE_TASK_ID>",
              "lastExecutionDate": "2023-12-01T13:23:20Z",
              "lastRun": "2023-12-01T13:23:15Z",
              "lastUpdated": "2023-12-01T13:23:20Z",
              "multiInsightURLs": null,
              "name": "Daily exception report",
              "owner": "6560c8259181e895e9470b0c",
              "ownerName": "Dave Channon",
              "recipients": {
                  "DLGroups": [
                      {
                          "enabled": true,
                          "filters": null,
                          "membersCount": 2,
                          "name": "ReportRecipients",
                          "taskGroupRecipientErrors": null
                      }
                  ],
                  "DLUsers": [],
                  "emailAddresses": [],
                  "groupIds": null,
                  "userIds": []
              },
              "retentionPolicy": {
                  "historySize": 1,
                  "overrideInterval": "FREQ=HOURLY;INTERVAL=1"
              },
              "selectionErrors": [],
              "spaceId": "6568984404f5168a7ff854f7",
              "startTime": "2023-11-30T14:20:16Z",
              "state": {
                  "fields": null,
                  "queryItems": null,
                  "selections": []
              },
              "statusCode": "VALID",
              "subType": "xlsx",
              "tags": [],
              "taskErrors": [],
              "templateId": "<SOURCE_TEMPLATE_ID>",
              "templates": [
                  {
                      "excelData": [
                          {
                              "appId": "<SOURCE_APP_ID>",
                              "name": "ExceptionReportTemplate",
                              "persistentBookmark": {
                                  "id": "4432722a-2bea-4aa5-a211-16e0c1306f79"
                              },
                              "selectionType": "persistentBookmark",
                              "templateId": "<SOURCE_TEMPLATE_ID>"
                          }
                      ],
                      "fileName": "ExceptionReport",
                      "fileTimeStamp": "yyyy-MM-dd_HH-mm",
                      "multiSheetData": null,
                      "subType": "xlsx",
                      "type": "excel"
                  }
              ],
              "tenant": "Qoz4NNVMQkAT4NljRG60Ia3kkBkcz9Tz",
              "transportChannels": [
                  "email"
              ],
              "trigger": {
                  "chronosJobID": "",
                  "executeOnAppReload": true,
                  "recurrence": null
              },
              "type": "template-sharing",
              "updatedBy": "6560c8259181e895e9470b0c",
              "enabled": true,
              "latestExecutionFilesURL": null,
              "latestExecutionURL": "https://<HOSTNAME>/api/v1/sharing-tasks/<SOURCE_TASK_ID>/executions/latest",
              "links": {
                  "self": {
                      "href": "https://<HOSTNAME>/api/v1/sharing-tasks/<SOURCE_TASK_ID>"
                  }
              }
          }
      ]
  }

  ```
</details>

### 2.3 Export the report template definitions

Retrieve the report templates defined against the source application. A report definition
can be used in multiple report tasks. Multiple report templates may exist per
Qlik Sense application.

> **Note:** If you wish to retrieve only the template for a specific report task, send a `GET` request to
> `https://<HOSTNAME>/api/v1/sharing-tasks/<SOURCE_TEMPLATE_ID>`.

To retrieve a list of all report templates for the app:

```bash
curl -L "https://<HOSTNAME>/api/v1/report-templates?appid=<SOURCE_APP_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

You will receive a `200` response, and a list of one or more report tasks if successful:

<details>
  <summary>Example JSON response</summary>

  This example
  shows a single report template definition, and key values listed as variables.

  ```json
  {
      "data": [
          {
              "id": "<SOURCE_TEMPLATE_ID>",
              "name": "ExceptionReportTemplate",
              "description": "The exception report template",
              "ownerId": "6560c8259181e895e9470b0c",
              "createdAt": "2023-11-30T14:19:13.223Z",
              "updatedAt": "2023-11-30T14:19:13.223Z",
              "createdBy": "6560c8259181e895e9470b0c",
              "updatedBy": "6560c8259181e895e9470b0c",
              "sourceAppId": "<SOURCE_APP_ID>",
              "sourceAppName": "Reporting App Example",
              "metadataVersion": 1
          }
      ],
      "links": {
          "self": {
              "href": "https://<HOSTNAME>/api/v1/report-templates?SourceAppId=<SOURCE_APP_ID>&Limit=20&Skip=0"
          }
      }
  }
  ```
</details>

### 2.3 Export the report template excel file

Now that you have a list of report templates, you can download each template to
local storage:

```bash
curl -L -X POST "https://<HOSTNAME>/api/v1/report-templates/<SOURCE_TEMPLATE_ID>/actions/download" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

You will receive a `200` response, and a binary file in the response body, which you
should save as `<TEMPLATE_FILE>`.

## 3 Import content

Once you have the definitions and assets, you can import them back into Qlik Cloud.
The APIs help support mapping where IDs might change between spaces, apps, or tenants.

### 3.1 Import the Qlik Sense app

Import a new copy of the Qlik Sense app into the tenant, to become the target app
against which you will import the report templates and tasks. The Qlik Sense app contains:

- The objects and data upon which the report will be based, and which the report
  template refers to.
- The recipients, groups, and filters used in the report task.

> **Note:** If you have exported the Qlik Sense app without data, you will need to reload
> it before you import the reporting task to ensure data such as the recipient list is available for the report task.

To import the app to a new space:

```bash
curl -L -X POST "https://<HOSTNAME>/api/v1/apps/import?spaceId=<TARGET_SPACE_ID>" ^
-H "Content-Type: application/octet-stream" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
-d "@<APP_FILE>"
```

You will receive a `200` response and metadata about the new app if successful:

<details>
  <summary>Example JSON response</summary>

  ```bash
  {
      "attributes": {
          "id": "<TARGET_APP_ID>",
          "name": "Reporting App Example",
          "description": "",
          "thumbnail": "",
          "lastReloadTime": "2023-12-01T13:23:13.142Z",
          "createdDate": "2023-12-13T17:35:16.618Z",
          "modifiedDate": "2023-12-13T17:35:17.308Z",
          "owner": "qlikbot\\7730fec7b4e9242de8b0badd60ca547d",
          "ownerId": "65689fc7ce65d4ce5a3c77ac",
          "dynamicColor": "",
          "published": false,
          "publishTime": "",
          "custom": {},
          "hasSectionAccess": false,
          "encrypted": true,
          "originAppId": "",
          "isDirectQueryMode": false,
          "usage": "ANALYTICS",
          "spaceId": "<TARGET_SPACE_ID>",
          "_resourcetype": "app"
      },
      ...
  ```
</details>

The app name will match the name of the exported app, if you wish to alter this,
you should add the `name=` parameter to
the [import call](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fv1%2Fapps%2Fimport-post).

## 3.2 Import the Report Template

With the Qlik Sense app imported, you can add back the Report Templates to the app.

Importing a template is a two step process, where you must first upload the excel
template from your local system to `/temp-contents`, and then create the template
from this import.

### 3.2.1 Upload the Report Template

To import a report template, you first need to upload it to the Qlik Cloud tenant.
To do this:

```bash
curl -L "https://<HOSTNAME>/api/v1/temp-contents?filename=ExceptionReportTemplate.xlsx" ^
-H "Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "@<TEMPLATE_FILE>"
```

The response will return a `201` status if successful, with an empty body. Retrieve
the download path for the app from the `Location` key in the response headers:

```json
Location: /api/v1/temp-contents/<TEMPLATE_IMPORT_ID>
```

From the `Location` key, retrieve just the `<TEMPLATE_IMPORT_ID>`.

### 3.2.2 Import the Report Template

To complete the import process, create a new report template on your target app. There are
two import actions you can use for this call:

- `"sourceAppAction": "replace"` - use when the template is being imported to an
  app with **a different** App ID to the app it was exported from. The references in
  the excel template will automatically be updated to point to the new app.
- `"sourceAppAction": "validate"` - use when the template is being imported to an
  app with **the same** App ID to the app it was exported from.

When moving templates between copies of an app, you must use the `replace` action.

To import:

```bash
curl -L "https://<HOSTNAME>/api/v1/report-templates" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
  \"name\": \"ExceptionReportTemplate\",
  \"description\": \"The exception report template\",
  \"temporaryContentId\": \"<TEMPLATE_IMPORT_ID>\",
  \"sourceAppId\": \"<TARGET_APP_ID>\",
  \"sourceAppAction\": \"replace\"
}"
```

The response will return a `201` status if successful, returning the metadata
for the new report template:

```json
{
    "id": "<TARGET_TEMPLATE_ID>",
    "name": "ExceptionReportTemplate",
    "description": "The exception report template",
    "ownerId": "65689fc7ce65d4ce5a3c77ac",
    "createdAt": "2023-12-14T13:26:11.8023359Z",
    "updatedAt": "2023-12-14T13:26:11.8023359Z",
    "createdBy": "65689fc7ce65d4ce5a3c77ac",
    "updatedBy": "65689fc7ce65d4ce5a3c77ac",
    "sourceAppId": "<TARGET_APP_ID>",
    "sourceAppName": "Reporting App Example",
    "metadataVersion": 1
}
```

Take note of the new template ID, `<TARGET_TEMPLATE_ID>`. You will need this when
recreating the report task.

## 3.3 Import the Report Task

Once the Qlik Sense app (which includes filters & recipients) and the report templates
are ready, you can recreate the report task.

When recreating the Report Task, you should replace `<TARGET_APP_ID>` and `<TARGET_TEMPLATE_ID>`.
If you wish to replace recipients, it is recommended that you consider using `DLGroups`
rather than `DLUsers`, as this reduces the amount of configuration you need to do
in the report tasks API. Instead, the heavy lifting is handled by the recipient list
in the app data model.

To create a new report task:

```bash
curl -L "https://<HOSTNAME>/api/v1/sharing-tasks" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
    \"name\": \"Daily exception report\",
    \"appName\": \"Reporting App Example\",
    \"description\": \"The first report task on this Qlik Sense app\",
    \"emailContent\": {
        \"body\": \"This exceptions report is generated daily via this report task\",
        \"subject\": \"Daily exceptions report\"
    },
    \"recipients\": {
        \"DLGroups\": [
            {
                \"enabled\": true,
                \"filters\": null,
                \"membersCount\": 2,
                \"name\": \"ReportRecipients\",
                \"taskGroupRecipientErrors\": null
            }
        ],
        \"DLUsers\": [],
        \"emailAddresses\": [],
        \"groupIds\": null,
        \"userIds\": []
    },
    \"retentionPolicy\": {
        \"historySize\": 1,
        \"overrideInterval\": \"FREQ=HOURLY;INTERVAL=1\"
    },
    \"state\": {
        \"fields\": null,
        \"queryItems\": null,
        \"selections\": []
    },
    \"subType\": \"xlsx\",
    \"templates\": [
        {
            \"excelData\": [
                {
                    \"appId\": \"<TARGET_APP_ID>\",
                    \"name\": \"ExceptionReportTemplate\",
                    \"persistentBookmark\": {
                        \"id\": \"4432722a-2bea-4aa5-a211-16e0c1306f79\"
                    },
                    \"selectionType\": \"persistentBookmark\",
                    \"templateId\": \"<TARGET_TEMPLATE_ID>\"
                }
            ],
            \"fileName\": \"ExceptionReport\",
            \"fileTimeStamp\": \"yyyy-MM-dd_HH-mm\",
            \"multiSheetData\": null,
            \"subType\": \"xlsx\",
            \"type\": \"excel\"
        }
    ],
    \"transportChannels\": [
        \"email\"
    ],
    \"trigger\": {
        \"recurrence\": [],
        \"executeOnAppReload\": true
    },
    \"type\": \"template-sharing\"
}"
```

The response will return a `201` status if successful, returning the metadata for
the newly created report task:

<details>
  <summary>Example JSON response</summary>

  ```json
  {
      "appId": "<TARGET_APP_ID>",
      "appName": "Reporting App Example",
      "createdBy": "65689fc7ce65d4ce5a3c77ac",
      "dateCreated": "2023-12-14T14:31:27Z",
      "description": "The first report task on this Qlik Sense app",
      "distributionListId": "657b0ecbc67606bf8669d58e",
      "emailContent": {
          "body": "This exceptions report is generated daily via this report task",
          "subject": "Daily exceptions report"
      },
      "enabledBySystem": true,
      "enabledByUser": true,
      "id": "657b11bf58f39ab83be7a391",
      "lastUpdated": "2023-12-14T14:31:27Z",
      "multiInsightURLs": null,
      "name": "Daily exception report",
      "owner": "65689fc7ce65d4ce5a3c77ac",
      "ownerName": "aqh-bot",
      "recipients": {
          "DLGroups": [],
          "DLUsers": [
              {
                  "email": "ingrid.hendrix@example.com",
                  "enabled": true,
                  "filters": [
                      {
                          "name": "Alpha"
                      }
                  ],
                  "groups": [],
                  "name": "Ingrid Hendrix",
                  "taskRecipientErrors": []
              },
              {
                  "email": "rob.carsson@example.com",
                  "enabled": true,
                  "filters": [
                      {
                          "name": "Alpha"
                      }
                  ],
                  "groups": [],
                  "name": "Rob Carsson",
                  "taskRecipientErrors": []
              }
          ],
          "emailAddresses": [],
          "groupIds": null,
          "userIds": []
      },
      "retentionPolicy": {
          "historySize": 1,
          "overrideInterval": "FREQ=HOURLY;INTERVAL=1"
      },
      "spaceId": "<TARGET_SPACE_ID>",
      "startTime": "2023-12-14T14:31:27Z",
      "state": {
          "fields": null,
          "queryItems": null,
          "selections": []
      },
      "statusCode": "VALID",
      "subType": "xlsx",
      "tags": null,
      "taskErrors": null,
      "templateId": "<TARGET_TEMPLATE_ID>",
      "templates": [
          {
              "excelData": [
                  {
                      "appId": "<TARGET_APP_ID>",
                      "name": "ExceptionReportTemplate",
                      "persistentBookmark": {
                          "id": "4432722a-2bea-4aa5-a211-16e0c1306f79"
                      },
                      "selectionType": "persistentBookmark",
                      "templateId": "<TARGET_TEMPLATE_ID>"
                  }
              ],
              "fileName": "myReport",
              "fileTimeStamp": "yyyy-MM-dd_HH-mm",
              "multiSheetData": null,
              "subType": "xlsx",
              "type": "excel"
          }
      ],
      "tenant": "Qoz4NNVMQkAT4NljRG60Ia3kkBkcz9Tz",
      "transportChannels": [
          "email"
      ],
      "trigger": {
          "chronosJobID": "",
          "executeOnAppReload": true,
          "recurrence": []
      },
      "type": "template-sharing",
      "updatedBy": "65689fc7ce65d4ce5a3c77ac",
      "enabled": true,
      "latestExecutionFilesURL": null,
      "latestExecutionURL": "https://<HOSTNAME>/api/v1/sharing-tasks/657b11bf58f39ab83be7a391/executions/latest",
      "links": {
          "self": {
              "href": "https://<HOSTNAME>/api/v1/sharing-tasks/657b11bf58f39ab83be7a391"
          }
      }
  }
  ```
</details>

## 4 Generate the tabular report

With the Qlik Sense app imported, report templates deployed, and report tasks
configured, you can now trigger generation of any outputs.

In the example in this tutorial, the report task is triggered on application reload.

To trigger a reload of the application:

```bash
curl -L "https://<HOSTNAME>/api/v1/reloads" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
  \"appId\": \"<TARGET_APP_ID>\"
}"
```

You will receive a `201` response, and metadata on the new reload if successful:

```json
{
    "id": "657b13208b6e5b1c05f5ab91",
    "appId": "<TARGET_APP_ID>",
    "tenantId": "Qoz4NNVMQkAT4NljRG60Ia3kkBkcz9Tz",
    "userId": "65689fc7ce65d4ce5a3c77ac",
    "type": "hub",
    "status": "QUEUED",
    "partial": false,
    "creationTime": "2023-12-14T14:37:20Z",
    "links": {
        "self": {
            "href": "https://<HOSTNAME>/api/v1/reloads/657b13208b6e5b1c05f5ab91"
        }
    }
}
```

Your tabular report outputs will be generated and distributed per the report task
once the application reload is complete.
