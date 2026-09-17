---
source: https://qlik.dev/manage/data-connections/delete-data-connections/
last_updated: 2026-04-20T13:34:03+01:00
---

# Delete data connections

## Overview

In this topic, you are going to learn how to delete data connections
from Qlik Cloud.

Deletion of a data connection requires the use of the [Data connections API](https://qlik.dev/apis/rest/data-connections).

## Requirements

- Review the prerequisites in the [Create data connections tutorial](https://qlik.dev/manage/data-connections/create-data-connections).
- Appropriate space or tenant level role to delete the connection.
  For more information, see [Working in spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm)
  on Qlik Help.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable            | Description                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`          | The hostname for the initial tenant created during account onboarding. Such as `tenantname.region.qlikcloud.com`.                             |
| `<ACCESS_TOKEN>`    | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<SPACE_ID>`        | The ID of the space from which you wish to delete a connection.                                                                               |
| `<CONNECTION_NAME>` | The name of the data connection.                                                                                                              |
| `<CONNECTION_ID>`   | The ID of the data connection.                                                                                                                |

## Retrieve connection ID

If you wish to verify the data connection prior to deletion, you can send a `GET`
request to retrieve connection metadata. For example, you can pass in the
space ID which you want to search for the connection in, and the connection name
to retrieve connections in that space which match the provided name:

```bash
curl -L "https://<TENANT>/api/v1/data-connections/<CONNECTION_NAME>?type=connectionname&spaceId=<SPACE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return an `HTTP 200` with a response which describes the connection:

```json
{
    "created": "2023-06-08T18:02:20.392Z",
    "datasourceID": "File_GoogleCloudStorageConnector",
    "id": "<CONNECTION_ID>",
    "links": {
        "self": {
            "href": "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>"
        }
    },
    "privileges": [
        "change_owner",
        "change_space",
        "delete",
        "list",
        "read",
        "update"
    ],
    "qArchitecture": 0,
    "qConnectStatement": "CUSTOM CONNECT TO \"provider=QvWebConnectorPackage.exe;sourceType=File_GoogleCloudStorageConnector;bucketName=mybucket;\"",
    "qCredentialsID": "0bb28d27-e9d4-413b-9c7d-aff083e55efb",
    "qEngineObjectID": "<CONNECTION_ID>",
    "qID": "<CONNECTION_ID>",
    "qLogOn": 1,
    "qName": "GoogleCloudStorage_mybucket",
    "qSeparateCredentials": false,
    "qType": "QvWebStorageProviderConnectorPackage.exe",
    "qri": "qri:file:gcs://8x2MU3IXd0JKmvhD3CtNM1-dZ17fUAp2FYBeXe7eEY5",
    "space": "<SPACE_ID>",
    "tenant": "Hj5p89bylz1r2AUC6joLNuHzVx5Ya8cF",
    "updated": "2023-06-08T18:02:20.392Z",
    "user": "6422bbf043af68ebe8abbb71",
    "version": "V1"
}
```

Use the `<CONNECTION_ID>` from the response to identify it for the delete command.

## Delete a data connection

Once you have the data connection ID, you can pass this to the delete endpoint to remove
this data connection from Qlik Cloud.

```bash
curl -L -X DELETE "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

A `204` response confirms that the data connection has been deleted successfully.
