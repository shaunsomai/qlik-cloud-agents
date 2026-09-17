---
source: https://qlik.dev/manage/data-connections/update-data-connections/
last_updated: 2026-07-16T09:40:34Z
---

# Update data connections

## Overview

This topic shows you how to update various properties of an analytic data connection,
including owner, space, name, credentials, and more. To do this, you will use the
[data-connection](https://qlik.dev/apis/rest/data-connections) API.

## Requirements

- Review the prerequisites in the [create data connections](https://qlik.dev/manage/data-connections/create-data-connections)
  tutorial.
- Appropriate space or tenant level role to update the connection.
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
| `<SPACE_ID>`        | The ID of the space the connection will be moved to.                                                                                          |
| `<OWNER_ID>`        | The ID of user who owns the specified data connection.                                                                                        |
| `<CONNECTION_ID>`   | The ID of the data connection being updated.                                                                                                  |
| `<CONNECTION_NAME>` | The name of the data connection being updated.                                                                                                |

## Retrieve connection ID and metadata

To update a data connection, you need to know its name or ID. You can send a `GET`
request to retrieve connection metadata.

> **Note:** The `parseConnection=true` parameter returns the connection properties in the same
> format as required to create and update connections, rather than bundled into the
> connection string in `qConnectStatement`.

For example, you can pass in the
space ID which you want to search for the connection in, and the connection name
to retrieve connections in that space which match the provided name:

```bash
curl -L "https://<TENANT>/api/v1/data-connections/<CONNECTION_NAME>?type=connectionname&space=<SPACE_ID>&parseConnection=true" ^
    -H "Authorization: Bearer <ACCESS_TOKEN>" ^
    -H "Content-Type: application/json" ^
    -H "Accept: application/json"
```

This will return an `HTTP 200` with a response which describes the connection:

```json
{
    "created": "2023-08-10T10:49:56.914Z",
    "datasourceID": "File_AmazonS3ConnectorV2",
    "id": "<CONNECTION_ID>",
    "links": {
        "self": {
            "href": "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>"
        }
    },
    "connectionProperties": {
        "bucketName": "bucket-name",
        "region": "us-east-1"
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
    "qConnectStatement": "CUSTOM CONNECT TO \"provider=QvWebConnectorPackage.exe;sourceType=File_AmazonS3ConnectorV2;region=us-east-1;bucketName=bucket-name;\"",
    "qCredentialsID": "5d7deb43-2a41-4ed3-81f9-0d02c37d8a89",
    "qEngineObjectID": "<CONNECTION_ID>",
    "qID": "<CONNECTION_ID>",
    "qLogOn": 1,
    "qName": "<CONNECTION_NAME>",
    "qSeparateCredentials": false,
    "qType": "QvWebStorageProviderConnectorPackage.exe",
    "qri": "qri:file:s3://KKj_7B9Gj09qbldOzS6-7NkcFiLT5XRm2jPoS9FY3KI",
    "space": "<SPACE_ID>",
    "tenant": "Hj5p89bylz1r2AUC6joLNuHzVx5Ya8cF",
    "updated": "2023-08-10T10:49:56.914Z",
    "user": "<OWNER_ID>",
    "version": "V1"
}
```

Use the `<CONNECTION_ID>` from the response to update it. You may also need other
parts of this response if you are updating other properties.

## Change connection owner

You can make batch requests to update connection metadata for space and owner if
you have the `TenantAdmin` role on the tenant. Many requests can be grouped together
in a single `POST` call.

If your user does not have an administrator role, you cannot change the owner
of a connection.

Assuming you wish to update both the space and owner of a single connection, and
the new target space is of type `shared`:

```bash
curl -L "https://<TENANT>/api/v1/data-connections/actions/update" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
    \"connections\": [
        {
            \"id\": \"<CONNECTION_ID>\",
            \"ownerId\": \"<OWNER_ID>\",
            \"spaceId\": \"<SPACE_ID>\",
            \"spaceType\": \"shared\"
        }
    ]
}"
```

To change only the owner, remove the `spaceId` and `spaceType` attributes.

You will receive an `HTTP 207 multi-status` response, with the payload containing
a separate `status` per data connection you requested be updated.

```json
{
    "data": [
        {
            "id": "<CONNECTION_ID>",
            "status": 204
        }
    ]
}
```

In this example, a `status` of `204` is shown, which indicates the updates were
successfully made to the connection.

## Change connection properties or credentials

There are two ways to update a data connection using the Data connections API:

- Use `PATCH` requests when you want to update specific properties.
  `PATCH` requests are ideal for rotating credentials or making small property changes without affecting the rest of the
  connection. *This is the recommended method for updating a connection.*
- Use `PUT` when you want to replace the entire connection definition.
  With `PUT` requests, you must send all required properties, including the full `qConnectStatement`.
  This is useful if you want to rebuild the connection in one request, but it can't update individual name/value pairs
  inside the connection string, and requires you to know how to encode the connection string.

> **Note:** Use `PATCH` to update credentials unless you use separately managed credentials referenced by ID.
> `PUT` cannot update inline credentials.

The result of update operations will be an empty response with an `HTTP 204` code, if successful.

> **Note:** The following security and data protection restrictions apply to `PATCH /data-connections/{id}`
> requests:
>
> - You cannot include both `qConnectStatement` and `connectionProperties` fields in the same
>   request body.
> - Changing the connection string (`qConnectStatement`) or the host property
>   (`connectionProperties/host`, `connectionProperties/server`, or `connectionProperties/url`)
>   requires credentials in the same request.
> - You cannot supply credentials using both `/qPassword` and a `connectionProperties` password
>   field simultaneously.
> - If the host changes and the connection uses separate credentials, the associated
>   credentials are deassociated after the update.

### Example: Update Amazon S3 connection

This `PATCH` request updates multiple properties of an Amazon S3 connection in one call: the bucket name, credentials,
region, and the connection's display name.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "[
    {\"op\": \"replace\", \"path\": \"/connectionProperties/bucketName\", \"Value\": \"my-bucket-name\"},
    {\"op\": \"replace\", \"path\": \"/qName\", \"Value\": \"Amazon_S3_Updated\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/accessKey\", \"Value\": \"AxY*****************\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/secretKey\", \"Value\": \"Zxy**************\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/region\", \"Value\": \"us-east-1\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/separateCredentials\", \"value\": true},
    {\"op\": \"add\", \"path\": \"/connectionProperties/credentialsName\", \"Value\": \"Amazon_S3_Credentials_New\"}
  ]"
```

### Example: Update Microsoft SQL Server connection

This `PATCH` request updates the host, port, database, username, password, and connection name.
It also sets tags and connection options such as maximum string length and query timeout.
Because the host changes, include credentials (`username` and `password`) in the same request.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "[
    {\"op\": \"add\", \"path\": \"/tags\", \"Value\": [\"SQL-Test\"]},
    {\"op\": \"replace\", \"path\": \"/qName\", \"Value\": \"MS-SQL\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/host\", \"Value\": \"mysqlserver.sqlhost\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/port\", \"Value\": 1433},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/database\", \"Value\": \"AdventureWorks\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/username\", \"Value\": \"ad*******\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/password\", \"Value\": \"ec**********\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/separateCredentials\", \"Value\": true},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/credentialsName\", \"Value\": \"MSSQLCredentials\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/maxStringLength\", \"Value\": 3000},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/QueryTimeout\", \"Value\": 100}
  ]"
```

### Example: Update Google BigQuery connection

This `PATCH` request updates the connection name and credentials for a Google BigQuery connection.
It replaces the key file used for authentication by sending the filename and its base64-encoded content.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "[
    {\"op\": \"replace\", \"path\": \"/connectionProperties/OAuthMechanism\", \"Value\": \"0\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/KeyFilePath/0/name\", \"Value\": \"test-automation-owner.json\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/KeyFilePath/0/value\", \"Value\": \"{base64 encoded file content}\"},
    {\"op\": \"replace\", \"path\": \"/qName\", \"Value\": \"GBQ_Updated\"},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/separateCredentials\", \"Value\": true},
    {\"op\": \"replace\", \"path\": \"/connectionProperties/credentialsName\", \"Value\": \"GBQ_Credentials\"}
  ]"
```

### Example: Replace the entire connection definition

This `PUT` request completely replaces a connection definition.
You must include all required properties such as `qID`, `qType`, `space`, the full `qConnectStatement`, and credentials.
This is useful if you want to rebuild the connection or apply a new connection string in one step.

*This is not the recommended method for updating a connection due to the complexity of the request body.*

> **Note:** Credential rotation is only supported via `PATCH`, unless you use separately managed credentials referenced by ID.

```bash
curl -L -X PUT "https://<TENANT>/api/v1/data-connections/<CONNECTION_ID>" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"qID\": \"<CONNECTION_ID>\",
    \"qEngineObjectID\": \"<CONNECTION_ID>\",
    \"qName\": \"<CONNECTION_NAME>\",
    \"qType\": \"QvWebStorageProviderConnectorPackage.exe\",
    \"space\": \"<SPACE_ID>\",
    \"qConnectStatement\": \"CUSTOM CONNECT TO \\\"provider=QvWebStorageProviderConnectorPackage.exe;sourceType=File_AmazonS3ConnectorV2;region=us-west-2;bucketName=new-bucket-name;\\\"\", 
    \"qCredentialsID\": \"<NEW_CREDENTIALS_ID>\",
    \"datasourceID\": \"File_AmazonS3ConnectorV2\"
  }"
```

For a complete list of properties you can update, see the [API reference](https://qlik.dev/apis/rest/data-connections).

## Next steps

Now that you know how to update a data connection, why not look at how
to [delete existing data connections](https://qlik.dev/manage/data-connections/delete-data-connections)?
