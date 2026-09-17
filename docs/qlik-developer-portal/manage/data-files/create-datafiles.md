---
source: https://qlik.dev/manage/data-files/create-datafiles/
last_updated: 2026-04-20T13:34:03+01:00
---

# Create data files in Qlik Cloud

## Overview

In this tutorial, you are going to learn how to create a new data file via
direct file upload, and how to duplicate an existing data file.

## Requirements

- If running the `@qlik/api` examples:
  - [`@qlik/api`](https://qlik.dev/toolkits/qlik-api).
  - [Node.js](https://nodejs.org/en/download) version 20 or higher.
  - An OAuth client that is a member of the space and has the `can manage` role.
    For more information, see [Working in shared spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm)
    on Qlik Help.
- If running the qlik-cli examples:
  - [qlik-cli](https://qlik.dev/toolkits/qlik-cli/install-qlik-cli/) v2.19.0+.
  - A [valid context](https://qlik.dev/toolkits/qlik-cli/qlik-cli-contexts) created to your tenant.
- If running the cURL examples, cURL for running the inline examples.
- A text editor or IDE of your choice, for example, Visual Studio Code.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable                | Description                                                                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `<HOSTNAME>`            | The hostname for the initial tenant created during account onboarding. Such as `tenantname.region.qlikcloud.com`.                               |
| `<ACCESS_TOKEN>`        | A bearer token for authorizing `https` requests to the `<HOSTNAME>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<OAUTH_CLIENT_ID>`     | An OAuth client ID for authorizing requests if using the platform SDK.                                                                          |
| `<OAUTH_CLIENT_SECRET>` | An OAuth client secret for authorizing requests if using the platform SDK.                                                                      |
| `<PATH_TO_DATA_FILE>`   | The path on your local system to a data file, such as `/path/to/datafile.csv`.                                                                  |
| `<DATA_FILE_NAME>`      | The name that will be displayed for the uploaded data file, for example `mydatafile.csv`.                                                       |
| `<SPACE_NAME>`          | The name of the shared space you'll create data files in.                                                                                       |
| `<SPACE_ID>`            | The ID of the shared space `<SPACE_NAME>`.                                                                                                      |
| `<CONNECTION_ID>`       | The ID for the data file connection in `<SPACE_NAME>`.                                                                                          |
| `<DATA_FILE_ID>`        | The ID for the data file.                                                                                                                       |
| `<DATA_SET_ID>`         | The ID for the data set generated from an uploaded data file.                                                                                   |

## Upload a data file

Uploading a data file from your local system to Qlik Cloud can be done using the [Data files](https://qlik.dev/apis/rest/data-files)
API.
This tutorial series walks you through creating a new space, uploading files, updating files, and deleting them.

### Create a space

Spaces are logical containers used to store content in Qlik Cloud tenants, and
each space will automatically generate a data files connection, to which you can
upload data. By default, if a space is not specified, the data file will be
uploaded to your personal space.

First, create a `shared` space using the [Spaces](https://qlik.dev/apis/rest/spaces) API with the POST method.
The name of the space and the type of space is passed in the body of the request.

```bash
curl -L "https://<HOSTNAME>/api/v1/spaces" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{
    \"name\": \"<SPACE_NAME>\",
    \"type\": \"shared\"
}"
```

```bash
qlik space create --name "<SPACE_NAME>" --type shared
```

The response should look something like this if using qlik-cli:

<details>
  <summary>Example qlik-cli response</summary>

  ```json
  {
    "createdAt": "2023-04-25T11:07:58.974Z",
    "createdBy": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "description": "",
    "id": "<SPACE_ID>",
    "meta": {
      "actions": [
        "create",
        "delete",
        "read",
        "update"
      ],
      "assignableRoles": [
        "consumer",
        "dataconsumer",
        "facilitator",
        "producer"
      ],
      "roles": []
    },
    "name": "<SPACE_NAME>",
    "ownerId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "tenantId": "G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk",
    "type": "shared",
    "updatedAt": "2023-04-25T11:07:58.974Z"
  }
  ```
</details>

Take note of the `<SPACE_ID>` as it will be needed to find the connection ID for
the data files connection that was automatically created in the space.

### Get the connection ID

A data files connection allows you to interact with files uploaded to a space.
To upload a data file to a space, you need to know the ID of the
`Datafiles` connection in that space, which is unique to that space. To get
the connection ID, use the [Data files](https://qlik.dev/apis/rest/data-files) API.

```bash
curl -L "https://<HOSTNAME>/api/v1/data-files/connections?spaceId=<SPACE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

```bash
qlik data-file connection ls --spaceId <SPACE_ID>
```

The response should look something like this if using qlik-cli:

<details>
  <summary>Example qlik-cli response</summary>

  ```json
  [
    {
      "id": "<CONNECTION_ID>",
      "privileges": [
        "read"
      ],
      "qArchitecture": 0,
      "qConnectStatement": "CUSTOM CONNECT TO \"provider=qix-datafiles.exe;path=<SPACE_NAME>:datafiles;\"",
      "qEngineObjectID": "967ee1bf-a2a8-4a50-81be-9574c75f3fb7",
      "qID": "967ee1bf-a2a8-4a50-81be-9574c75f3fb7",
      "qLogOn": 0,
      "qName": "DataFiles",
      "qType": "qix-datafiles.exe",
      "space": "<SPACE_ID>",
      "tenant": "G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk"
    }
  ]
  ```
</details>

From the response in the example, capture the `<CONNECTION_ID>`, which you will
use with the file upload request.

### Upload a new data file

To upload a new data file to a space, use
the [Data files](https://qlik.dev/apis/rest/data-files) API with the POST method.
Add the filename and path of the local data file to the body of the request using
the multipart/form-data format. You also need to pass the destination filename
and connection ID in the body of the request, as shown in the following example.

> **Note:** If you are uploading data files larger than 500 MB, you will need to adjust the
> upload approach. This is because larger files must be uploaded to the
> `temp-contents` API, which supports chunked uploads for these larger files.
> When using qlik-cli, you add an additional flag, but for raw API approaches
> you will need to amend your code.

```bash
curl -L "https://<HOSTNAME>/api/v1/data-files" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-F "file=@\"<PATH_TO_DATA_FILE>\"" ^
-F "json={\"name\":\"<DATA_FILE_NAME>\",\"connectionId\":\"<CONNECTION_ID>\"}"
```

This multi-step process supports files up to your entitled limits in Qlik Cloud.
Instead of uploading directly to the `data-files` API, you upload first to
`temp-contents` using a chunked upload, and then import this file to `data-files`.

If you are using Windows, you should update the line continuation character to `^`.

```bash
# Upload data file to temp-contents, and capture temp-contents file ID
TEMP_CONT_ID=$(curl -L "https://<HOSTNAME>/api/v1/temp-contents?filename=<DATA_FILE_NAME>" -v \
-X POST \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/octet-stream" \
-H "Transfer-Encoding: chunked" \
-T "<PATH_TO_DATA_FILE>" 2>&1 \
| grep -F "< location:" | awk '{print $3}' | tr -d '[:space:]' | awk -F / '{print $NF}')

# Create data-file from temp-contents
curl -L "https://<HOSTNAME>/api/v1/data-files" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Accept: application/json" \
-F "json={\"name\":\"<DATA_FILE_NAME>\",\"connectionId\":\"<CONNECTION_ID>\",\"tempContentFileId\":\"${TEMP_CONT_ID}\"}"
```

If your file is larger than 500 MB in size, add `--resumable` to have qlik-cli
automatically handle the upload of this file via `temp-contents`.

```bash
qlik data-file create --connectionId <CONNECTION_ID> --name "<DATA_FILE_NAME>" --file "<PATH_TO_DATA_FILE>"
```

This snippet can be pasted into a Qlik Automate workspace.
Data files up to 20 MB in size are supported via this approach.

```json
{"blocks":[{"id":"CE34F98D-6BA4-4DD1-A080-7525EF7940B2","type":"FormBlock","disabled":false,"name":"inputs","displayName":"Inputs","comment":"","childId":"9519B53A-E6F5-4EEE-866C-10948E9A62E3","inputs":[],"settings":[{"id":"persist_data","value":"no","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-440,"y":217,"form":[{"id":"inputs-input-0","label":"Tenant","helpText":"Enter tenant hostname, e.g. `mytenant.us.qlikcloud.com`","type":"input","values":null,"isRequired":true,"options":{},"order":0},{"id":"inputs-input-1","label":"Data file name","helpText":"Enter a name for the new data file, e.g. `MyFile.csv`","type":"input","values":null,"isRequired":true,"options":{},"order":1},{"id":"inputs-input-2","label":"Data file format","helpText":"Enter the encoding for the new data file, e.g. `text/csv; charset=utf-8`","type":"input","values":null,"isRequired":true,"options":{},"order":2},{"id":"inputs-input-3","label":"Data file contents","helpText":"The base64 encoded string for the file (up to 20MB)","type":"input","values":null,"isRequired":true,"options":{},"order":3}],"persistData":"no"},{"id":"9519B53A-E6F5-4EEE-866C-10948E9A62E3","type":"SnippetBlock","disabled":false,"name":"GetTenantNameAndRegion","displayName":"Qlik Platform Operations - Get Tenant Name And Region","comment":"","childId":"677CCEF5-7A55-4726-B230-5DAF51FBB035","inputs":[{"id":"575d1740-b1e2-11ed-958a-598edfec33b8","value":"{$.inputs.Tenant}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-326,"y":135,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"},{"id":"677CCEF5-7A55-4726-B230-5DAF51FBB035","type":"EndpointBlock","disabled":false,"name":"CreateDataFile","displayName":"Qlik Platform Operations - Create Data File","comment":"","childId":null,"inputs":[{"id":"40f122d0-d478-11ed-8c10-135c7af2f657","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"ebc40ca0-f88a-11ed-8d3a-fdae4a5586d5","value":"{$.inputs.'Data file name'}","type":"string","structure":{}},{"id":"f35afef0-f88a-11ed-bb54-93ec020fbe2e","value":null,"type":"string","structure":{}},{"id":"8bff6e00-f88e-11ed-a714-fb38c2e41e1e","value":"{ $.inputs.'Data file format' }","type":"select","structure":{}},{"id":"40fef4c0-d478-11ed-9030-0f5d6a0118ae","value":"{$.inputs.'Data file contents'}","type":"longtext","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-376,"y":216,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"40d7f620-d478-11ed-ac88-87852ef35cc7","endpoint_role":"create"}],"variables":[]}
```

The response should look something like this if using qlik-cli:

<details>
  <summary>Example qlik-cli response</summary>

  ```json
  {
    "createdDate": "2023-04-25T11:50:37.2046053Z",
    "id": "<DATA_FILE_ID>",
    "modifiedDate": "2023-04-25T11:50:37.4226807Z",
    "name": "<DATA_FILE_NAME>",
    "ownerId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "size": 43589,
    "spaceId": "<SPACE_ID>"
  }
  ```
</details>

The response indicates that the data file has been successfully uploaded to the tenant
in the designated space, with the specified name.

## Retrieve the data set for a data file

To retrieve the data set for a data file, you can use the [Items](https://qlik.dev/apis/rest/items) API to retrieve the data set, and
then call the [Data sets](https://qlik.dev/apis/rest/data-sets) API for metadata generated on the file.

### Retrieve the data set ID

```bash
curl -L "https://<HOSTNAME>/api/v1/items?resourceType=dataset&name=<DATA_FILE_NAME>&spaceId=<SPACE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json"
```

```bash
qlik item ls --spaceId <SPACE_ID> --resourceType dataset --name "<DATA_FILE_NAME>"
```

The response should look something like this if using qlik-cli:

<details>
  <summary>Example qlik-cli response</summary>

  ```json
  [
    {
      "actions": [
        ...
      ],
      "collectionIds": [],
      "createdAt": "2023-05-12T09:56:27Z",
      "creatorId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
      "id": "645e0d4beea64e3da17d780c",
      "isFavorited": false,
      "itemViews": {},
      "meta": {
        "actions": [
          ...
        ],
        "collections": [],
        "isFavorited": false,
        "tags": []
      },
      "name": "<DATA_FILE_NAME>",
      "ownerId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
      "resourceAttributes": {
        "appType": "QIX-DF",
        "dataStoreName": "DataFilesStore",
        "dataStoreType": "qix-datafiles",
        "qri": "qdf:qix-datafiles:G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk:sid@6447b48e8f1ff8bae0abc06d:<DATA_FILE_NAME>",
        "secureQri": "qri:qdf:space://SMRdll7Sm5pgfaAla9DW3mnEhZa9vc2qbqS6mDASQcE#P5MFmetJPJ7ihdQzzEwsnmUKEyaoz60tREjwEnesS_o",
        "sourceSystemId": "QIX-DF_d987e774-b30a-4eec-b74b-48fd0e61858f",
        "technicalDescription": "",
        "technicalName": "<DATA_FILE_NAME>",
        "type": "xml",
        "version": "1"
      },
      "resourceCreatedAt": "2023-05-12T09:56:26Z",
      "resourceCustomAttributes": null,
      "resourceId": "<DATA_SET_ID>",
      "resourceReloadEndTime": "",
      "resourceReloadStatus": "",
      "resourceSize": {
        "appFile": 0,
        "appMemory": 0
      },
      "resourceSubType": "qix-df",
      "resourceType": "dataset",
      "resourceUpdatedAt": "2023-05-12T09:56:33Z",
      "spaceId": "<SPACE_ID>",
      "tenantId": "G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk",
      "updatedAt": "2023-05-12T09:56:33Z",
      "updaterId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn"
    }
  ]
  ```
</details>

The response indicates that the data set exists. There are multiple IDs in this
response - the relevant ID for the data set is in the `resourceId` attribute.
Capture this as `<DATA_SET_ID>`.

### Retrieve the data set metadata

```bash
curl -L "https://<HOSTNAME>/api/v1/data-sets/<DATA_SET_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json"
```

```bash
qlik raw get v1/data-sets/<DATA_SET_ID>
```

The response should look something like this if using qlik-cli:

<details>
  <summary>Example qlik-cli response</summary>

  ```json
  {
    "classifications": {
      "personalInformation": [],
      "sensitiveInformation": []
    },
    "createdBy": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "createdTime": "2023-05-12T09:56:26.920Z",
    "dataAssetInfo": {
      "dataStoreInfo": {
        "id": "601c40bbc1fdfb4324a75a4d",
        "name": "DataFilesStore",
        "type": "qix-datafiles"
      },
      "id": "64497d05c67d6117d0f64da1",
      "name": "<SPACE_NAME>"
    },
    "description": "",
    "id": "<DATA_SET_ID>",
    "lastModifiedBy": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "lastModifiedTime": "2023-05-12T09:56:33.123Z",
    "name": "<DATA_FILE_NAME>",
    "operational": {
      "contentUpdated": true,
      "lastLoadTime": "2023-05-12T09:56:26.920Z",
      "lastUpdateTime": "2023-05-12T09:56:27.337Z",
      "location": "40f8dab3-6965-4d99-8695-59a5c1151d56",
      "logMessage": "{\n  \"cloudEventsVersion\": \"0.1\",\n  \"source\": \"com.qlik/qix-datafiles\",\n  \"contentType\": \"application/json\",\n  \"eventID\": \"40f8dab3-6965-4d99-8695-59a5c1151d56\",\n  \"eventType\": \"com.qlik.datafile.created\
  ",\n  \"eventTypeVersion\": \"0.0.1\",\n  \"eventTime\": \"2023-05-12T09:56:27.3414906Z\",\n  \"extensions\": {\n    \"tenantId\": \"G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk\",\n    \"userId\": \"CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn\",\n    \"header\": {\n
      \"traceparent\": [\n        \"00-0000000000000000b96c01cc6a74cf19-6676b3130bc7530b-01\"\n      ]\n    }\n  },\n  \"data\": {\n    \"id\": \"d987e774-b30a-4eec-b74b-48fd0e61858f\",\n    \"name\": \"<DATA_FILE_NAME>\",\n    \"createdDate\": \"2
  023-05-12T09:56:26.9205165Z\",\n    \"modifiedDate\": \"2023-05-12T09:56:27.3378401Z\",\n    \"createdByUser\": \"CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn\",\n    \"modifiedByUser\": \"CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn\",\n    \"ownerId\": \"CBg-NdDpqyFZI
  HRxylm03Pr2Gp3U7Ynn\",\n    \"spaceId\": \"<SPACE_ID>\",\n    \"size\": 85316,\n    \"contentUpdated\": true,\n    \"isInternal\": false,\n    \"qri\": \"qri:qdf:space://SMRdll7Sm5pgfaAla9DW3mnEhZa9vc2qbqS6mDASQcE#P5MFmetJPJ7ihdQzzE
  wsnmUKEyaoz60tREjwEnesS_o\"\n  },\n  \"messageTopic\": \"system-events.datafiles/Created/G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk/d987e774-b30a-4eec-b74b-48fd0e61858f\"\n}",
      "rowCount": 1040,
      "size": 85316,
      "status": "com.qlik.datafile.created"
    },
    "ownerId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "properties": {
      "ModifiedByProfileService": false
    },
    "qri": "qdf:qix-datafiles:G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk:sid@6447b48e8f1ff8bae0abc06d:<DATA_FILE_NAME>",
    "schema": {
      "dataFields": [
        {
          "dataType": {
            "properties": {
              "qType": "U",
              "qUseThou": 0,
              "qnDec": 0
            },
            "type": "INTEGER"
          },
          "encrypted": false,
          "index": 0,
          "name": "Id",
          "nullable": false,
          "orphan": false,
          "primaryKey": false,
          "sensitive": false,
          "tags": [
            "$integer",
            "$numeric"
          ]
        },
        {
          "dataType": {
            "properties": {
              "qType": "U",
              "qUseThou": 0,
              "qnDec": 0
            },
            "type": "STRING"
          },
          "encrypted": false,
          "index": 1,
          "name": "TagName",
          "nullable": false,
          "orphan": false,
          "primaryKey": false,
          "sensitive": false,
          "tags": [
            "$text",
            "$ascii"
          ]
        },
        {
          "dataType": {
            "properties": {
              "qType": "U",
              "qUseThou": 0,
              "qnDec": 0
            },
            "type": "INTEGER"
          },
          "encrypted": false,
          "index": 2,
          "name": "Count",
          "nullable": false,
          "orphan": false,
          "primaryKey": false,
          "sensitive": false,
          "tags": [
            "$integer",
            "$numeric"
          ]
        },
        {
          "dataType": {
            "properties": {
              "qType": "U",
              "qUseThou": 0,
              "qnDec": 0
            },
            "type": "INTEGER"
          },
          "encrypted": false,
          "index": 3,
          "name": "ExcerptPostId",
          "nullable": false,
          "orphan": false,
          "primaryKey": false,
          "sensitive": false
        },
        {
          "dataType": {
            "properties": {
              "qType": "U",
              "qUseThou": 0,
              "qnDec": 0
            },
            "type": "INTEGER"
          },
          "encrypted": false,
          "index": 4,

          "name": "WikiPostId",
          "nullable": false,
          "orphan": false,
          "primaryKey": false,
          "sensitive": false
        }
      ],
      "effectiveDate": "2023-05-12T09:56:33.149Z",
      "loadOptions": {
        "qDataFormat": {
          "qCodePage": 0,
          "qDelimiter": {
            "qNumber": 0
          },
          "qHeaderSize": 0,
          "qRecordSize": 0,
          "qTabSize": 0,
          "qType": "XML"
        }
      },
      "overrideSchemaAnomalies": false
    },
    "secureQri": "qri:qdf:space://SMRdll7Sm5pgfaAla9DW3mnEhZa9vc2qbqS6mDASQcE#P5MFmetJPJ7ihdQzzEwsnmUKEyaoz60tREjwEnesS_o",
    "spaceId": "<SPACE_ID>",
    "technicalDescription": "",
    "technicalName": "<DATA_FILE_NAME>",
    "tenantId": "G8r1kgLOO2OQDx8twJrgLJN7MchF3hDk",
    "type": "xml",
    "version": 1
  }
  ```
</details>

## Duplicate a data file

You can duplicate (copy) data files already in Qlik Cloud. This is done
using the import command, but passing the ID of the existing data file instead
of a new file.

Ensure that you use a new `<DATA_FILE_NAME>` for the duplicated file, unless you
are moving it to a different space, as data file names must be unique per space.

```bash
curl -L "https://<HOSTNAME>/api/v1/data-files" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-F "json={\"name\":\"<DATA_FILE_NAME>\",\"connectionId\":\"<CONNECTION_ID>\",\"sourceId\":\"<DATA_FILE_ID>\"}"
```

```bash
qlik data-file create --connectionId <CONNECTION_ID> --name "<DATA_FILE_NAME>" --sourceId "<DATA_FILE_ID>"
```

This snippet can be pasted into a Qlik Automate workspace.

```json
{"blocks":[{"id":"CE34F98D-6BA4-4DD1-A080-7525EF7940B2","type":"FormBlock","disabled":false,"name":"inputs","displayName":"Inputs","comment":"","childId":"9519B53A-E6F5-4EEE-866C-10948E9A62E3","inputs":[],"settings":[{"id":"persist_data","value":"no","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-440,"y":217,"form":[{"id":"inputs-input-0","label":"Tenant","helpText":"Enter tenant hostname, e.g. `mytenant.us.qlikcloud.com`","type":"input","values":null,"isRequired":true,"options":{},"order":0},{"id":"inputs-input-1","label":"Data file id","helpText":"Enter the id of the data file you wish to copy, e.g. `1ug21g212o8go8ugo3`","type":"input","values":null,"isRequired":true,"options":{},"order":1}],"persistData":"no"},{"id":"9519B53A-E6F5-4EEE-866C-10948E9A62E3","type":"SnippetBlock","disabled":false,"name":"GetTenantNameAndRegion","displayName":"Qlik Platform Operations - Get Tenant Name And Region","comment":"","childId":"5B485808-74DE-4A51-9834-32FD3E7BB1E0","inputs":[{"id":"575d1740-b1e2-11ed-958a-598edfec33b8","value":"{$.inputs.Tenant}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-326,"y":135,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"},{"id":"5B485808-74DE-4A51-9834-32FD3E7BB1E0","type":"EndpointBlock","disabled":false,"name":"GetDataFile","displayName":"Qlik Platform Operations - Get Data File","comment":"","childId":"4AC3B4EC-1B80-4E93-913C-702AFA09209E","inputs":[{"id":"c754f6f0-d863-11ed-a149-41239dd5935e","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"c762e080-d863-11ed-bbd1-556f5f5ed50f","value":"{$.inputs.'Data file id'}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-405,"y":83,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"c72d9500-d863-11ed-9518-617ecb039472","endpoint_role":"get"},{"id":"4AC3B4EC-1B80-4E93-913C-702AFA09209E","type":"SnippetBlock","disabled":false,"name":"CopyDataFileInSpace","displayName":"Qlik Platform Operations - Copy Data File In Space","comment":"","childId":null,"inputs":[{"id":"af8d6430-fbc4-11ed-9dc3-87cc8aa895e7","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"af8ea110-fbc4-11ed-9783-0591e6edc93a","value":"{$.GetDataFile.spaceId}","type":"string","structure":{}},{"id":"af8f41c0-fbc4-11ed-923f-ddd07477ae2b","value":"Copy of {$.GetDataFile.name}","type":"string","structure":{}},{"id":"f1d10b30-fbc4-11ed-9aed-2f4bfd6392e2","value":"{$.GetDataFile.id}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-406,"y":149,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"af7aaed0-fbc4-11ed-877e-433d7b3257cb"}],"variables":[]}
```

Successfully duplicating the data file will result in the same response as creating
a new data file.

## Next steps

Now that you know how to create and copy data files, why not look at how
to [update existing data files](https://qlik.dev/manage/data-files/update-datafiles)?
