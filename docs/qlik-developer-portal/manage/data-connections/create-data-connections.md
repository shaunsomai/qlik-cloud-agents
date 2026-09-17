---
source: https://qlik.dev/manage/data-connections/create-data-connections/
last_updated: 2026-09-01T10:20:53+02:00
---

# Create data connections

## Overview

In this topic, you are going to learn how to create a new data connection
to common data sources. These can be used by Qlik Cloud Analytics apps to create analytics within
the Qlik Cloud platform, as well as by data projects in Qlik Talend Data Integration.

The APIs used to create data connections are shared across analytics and
Data Integration use cases, and the overall workflow is similar.
However, the required configuration and connection properties differ.

The examples in this tutorial are analytics-oriented.

If you are creating connections for a Qlik Talend Data Integration project,
review [Data integration projects](https://qlik.dev/apis/rest/di-projects/) to understand how
connections are used in pipelines, then refer to the dedicated DI examples.

## Requirements

- You have an understanding of [data connections and their supporting APIs](https://qlik.dev/manage/data-connections/).
- cURL for running the inline examples.
- Appropriate space or tenant level role to delete the connection.
  For more information on which permissions a user needs to create, modify, and
  access data connections, see [Working in spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm)
  on Qlik Help.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of variables
referred to in this tutorial.

| Variable             | Description                                                                                                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`           | The hostname for the initial tenant created during account onboarding. Such as `tenantname.region.qlikcloud.com`.                                                                                  |
| `<ACCESS_TOKEN>`     | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate).                                                      |
| `<SPACE_NAME>`       | The name of the space you'll create data connections in.                                                                                                                                           |
| `<SPACE_ID>`         | The ID of the space `<SPACE_NAME>`.                                                                                                                                                                |
| `<DATA_SOURCE_ID>`   | The ID of data source that you wish to create a new data connection to.                                                                                                                            |
| `<CONNECTION_ID>`    | The ID for the data connection created in `<SPACE_NAME>`.                                                                                                                                          |
| `<CONNECTION_NAME>`  | The ID for the data connection to be created in `<SPACE_NAME>`.                                                                                                                                    |
| `<CRED_USERNAME>`    | A username for `<CONNECTION_NAME>`, for use with username and password authentication, or with certificate or OAuth when alternative credentials are provided in replacement of `<CRED_PASSWORD>`. |
| `<CRED_PASSWORD>`    | A password for `<CONNECTION_NAME>`, for use with username and password authentication.                                                                                                             |
| `<CRED_OAUTH>`       | An OAuth code for `<CONNECTION_NAME>`, for use with interactive OAuth - must be copied from an interactive session.                                                                                |
| `<CRED_CERTIFICATE>` | A base64 encoded certificate or key file for `<CONNECTION_NAME>`, for use with certificate or service account key file authentication.                                                             |
| `<CRED_FINGERPRINT>` | The fingerprint for a public key (for example, `SHA256:P8B+630peO/No+Ktb8irH0NdQkcWXwhBxYexd99bMiQ=`).                                                                                             |

## Construct connection properties

The parameters required to create a new data connection will differ depending
on the data source. When creating a connection via API for the first time, you
will need to look up the specification for the API to determine the properties
you can send with the request.

> **Note:** If you wish to copy connection properties from an existing data connection,
> you can retrieve this definition using the `data-connections` API.
> For more information, see
> the [update data connection](https://qlik.dev/manage/data-connections/update-data-connections/#1-retrieve-the-data-connection-definition)
> topic to learn how to do this.

### Identify the data source ID

To
create a new connection, you must know the data source ID (listed as `dataSourceId`),
which is the internal identifier indicating the driver that Qlik Cloud should use
to contact the data source.

To retrieve the supported data sources for the tenant:

```bash
curl -L "https://<TENANT>/api/v1/data-sources/" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

This will return a `200` response and list of sources:

```json
{
    "dataSources": [
        {
            "capabilities": [
                "streaming",
                "STREAMING",
                "SupportFileStreaming"
            ],
            "dataLoadUrlOverride": null,
            "dataSourceId": "File_AmazonS3ConnectorV2",
            "dataSourceName": "Amazon S3 V2",
            "dataSourcePropertyName": "sourceType",
            "provider": "QvWebStorageProviderConnectorPackage.exe",
            "providerName": "Qlik Web Connectors",
            "settings": [],
            "qriDefinition": {
                "qriPrefix": "qri:file:s3://",
                "connectionPart": {
                    "template": "{region}/{bucketName}",
                    "properties": [
                        "region",
                        "bucketName"
                    ]
                },
                "pathPart": {
                    "prefix": "#",
                    "template": "{filePath}",
                    "properties": [
                        "filePath"
                    ]
                },
                "itemPart": {
                    "prefix": "#",
                    "template": "{item}",
                    "properties": [
                        "item"
                    ]
                }
            },
            "name": "Qlik Web Connectors"
        },
        {
            "capabilities": [],
            "dataLoadUrlOverride": null,
            "dataSourceId": "rest",
            "dataSourceName": "REST",
            "dataSourcePropertyName": null,
            "provider": "QvRestConnector.exe",
            "providerName": "Qlik® REST Connector",
            "settings": [],
            "qriDefinition": {
                "qriPrefix": "qri:rest://",
                "connectionPart": {
                    "template": "{url}",
                    "properties": [
                        "url"
                    ]
                },
                "pathPart": {
                    "prefix": "#",
                    "template": "{xpath}",
                    "properties": [
                        "url",
                        "xpath"
                    ]
                }
            },
            "name": "Qlik® REST Connector"
        }
        ...
    ],
    "lastUpdated": "2024-03-01T14:54:51.071Z"
}
```

For the data source `Amazon S3 V2`, the `<dataSourceId>` is `File_AmazonS3ConnectorV2`.
Use this for the value of `<DATA_SOURCE_ID>`.

### Retrieve data source properties

Using the `<DATA_SOURCE_ID>`, you can retrieve the data source properties using
the connection specification endpoint. To retrieve the specification for
the `File_AmazonS3ConnectorV2` connector:

```bash
curl -L "https://<TENANT>/api/v1/data-sources/<DATA_SOURCE_ID>/api-specs" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The response will contain all available properties, a description for each, and
example enumerations if available:

```json
{
    "connectorProvider": "QvWebStorageProviderConnectorPackage.exe",
    "connectorVersion": "4.46.0",
    "connectionProperties": {
        "type": "object",
        "properties": {
            "region": {
                "type": "string",
                "default": "us-east-1",
                "enum": [
                    "af-south-1",
                    "ap-east-1",
                    ...
                ],
                "description": "Amazon S3 region code. (Default=us-east-1). (enum values are case sensitive)"
            },
            "bucketName": {
                "type": "string",
                "description": "The bucket name e.g. 'my-bucket'. You are strongly advised not to use sensitive naming for bucket names and object keys. GovCloud users should follow secure naming practices for buckets and object keys, to avoid using export-controlled and other sensitive data."
            },
            "storeSseHeader": {
                "type": "string",
                "description": "The value to send for the x-amz-server-side-encryption header for store (PutObject) which may be required by some policy conditions for SSE encrypted buckets (for example, AES256, aws:kms)."
            },
            "separateCredentials": {
                "type": "boolean",
                "default": false,
                "description": "When checked, credentials are not saved with the connection and each user will need to provide their own set of credentials."
            },
            "selectedCredentials": {
                "type": "string",
                "description": "Select or create the credentials to associate with the current connection"
            },
            "credentialsName": {
                "type": "string",
                "description": "Give a name for the credentials"
            },
            "accessKey": {
                "type": "string",
                "description": "Amazon S3 access key."
            },
            "secretKey": {
                "type": "string",
                "description": "Amazon S3 secret key."
            }
        }
    }
}
```

From this response you can see that you are able to provide values for `accessKey`,
`secretKey`, `region`, `bucketName`, and `storeSseHeader`. Which values you need to
pass will vary depending on connector configuration and S3 bucket configuration.

The values `separateCredentials` and `selectedCredentials` are standard parameters
which provide support for [separated credentials](https://qlik.dev/manage/data-connections/auth-data-connections).

## Create data connection with non-interactive authentication

*If you are using interactive OAuth for authentication, or you wish to use separated
credentials (where each user brings their own), you should
review [using interactive auth or separated credentials with data connections](https://qlik.dev/manage/data-connections/auth-data-connections).*

This example creates a S3 v2 connection file connection to a bucket called `bucket-name`
in AWS's `us-east-1` region. The request includes the data source ID against
which the connection will be created, `File_AmazonS3ConnectorV2`; the target space ID
for the new connection; and the connection name and credentials.

```bash
curl -L "https://<TENANT>/api/v1/data-connections" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
    \"dataSourceId\": \"File_AmazonS3ConnectorV2\",
    \"qName\": \"<CONNECTION_NAME>\",
    \"space\": \"<SPACE_ID>\",
    \"connectionProperties\": {
        \"accessKey\": \"<CRED_USERNAME>\",
        \"secretKey\": \"<CRED_PASSWORD>\",
        \"region\": \"us-east-1\",
        \"bucketName\": \"bucket-name\"
    }
}"
```

If successful, the system will return an `HTTP 201 created` code and the newly
created data connection:

```json
{
    "created": "2024-03-01T16:00:00.91Z",
    "datasourceID": "File_AmazonS3ConnectorV2",
    "id": "<CONNECTION_ID>",
    "links": {
        "self": {
            "href": "https://<TENANT>/v1/data-connections/<CONNECTION_ID>"
        }
    },
    "privileges": [
        "read",
        "update",
        "delete"
    ],
    "qArchitecture": 0,
    "qConnectStatement": "CUSTOM CONNECT TO \"provider=QvWebConnectorPackage.exe;sourceType=File_AmazonS3ConnectorV2;region=us-east-1;bucketName=bucket-name;\"",
    "qCredentialsID": "bd9d3e11-6023-442e-af4e-a67c678d0a55",
    "qEngineObjectID": "<CONNECTION_ID>",
    "qID": "<CONNECTION_ID>",
    "qLogOn": 1,
    "qName": "<CONNECTION_NAME>",
    "qSeparateCredentials": false,
    "qType": "QvWebStorageProviderConnectorPackage.exe",
    "qri": "qri:file:s3://JLZNzComOveRMUdRBvLCB3LWM32JBwz_RkRNXMHzc8U",
    "space": "<SPACE_ID>",
    "tags": [
        "DcaasAPI:QvWebStorageProviderConnectorPackage.exe:4.46.0"
    ],
    "tenant": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "updated": "2024-03-01T16:00:00.91Z",
    "user": "637390ef6541614d3a88d6c3",
    "version": "V1"
}
```

This response includes the new `<CONNECTION_ID>`, as well as the ID of the associated
credentials, which is useful when using separated credentials.

## Example creation requests

For analytics-oriented sample connections for common configurations, see
[Data connection creation examples](https://qlik.dev/manage/data-connections/examples/data-connection-create-examples#analytics-data-connection-examples).

If you are creating connections for a Qlik Talend Data Integration project,
jump to the [data integration project connector examples](https://qlik.dev/manage/data-connections/examples/data-connection-create-examples#data-integration-project-connector-examples),
then continue with [Data integration connectors reference](https://qlik.dev/manage/di-projects/di-connectors-reference)
and [Deploy a data integration project](https://qlik.dev/manage/di-projects/deploy-di-project).

## Next steps

Now that you know how to create a data connection, why not look at how
to [update existing data connections](https://qlik.dev/manage/data-connections/update-data-connections)?
