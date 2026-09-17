---
source: https://qlik.dev/manage/data-connections/examples/data-connection-create-examples/
last_updated: 2026-05-05T09:59:43+01:00
---

# Data connection creation examples

These examples demonstrate how to create data connections. To learn more,
review [Create data connections](https://qlik.dev/manage/data-connections/create-data-connections/).

This page includes examples for two different personas that use the same
`data-connections` API, but with different configurations and required properties:

- Analytics data connections are used by Qlik Cloud Analytics apps and load
  scripts. The examples below start with that connector stack.
- Data integration project connections are used by Qlik Talend Data Integration
  projects as source, target, platform, or staging connections. Jump to
  [Data integration project connector examples](#data-integration-project-connector-examples),
  then continue with [Data integration connectors reference](https://qlik.dev/manage/di-projects/di-connectors-reference)
  and [Deploy a data integration project](https://qlik.dev/manage/di-projects/deploy-di-project).

> **Choose the right connector stack:** Use the analytics examples when the connection will be consumed by an app or
> load script. Use the data integration examples when the connection will be
> bound to a Qlik Talend Data Integration project or task. Analytics gateway
> examples typically use `DG_...` `dataSourceId` values with
> `gatewayInstance`. Data integration examples typically use `repsrc_...` or
> `reptgt_...` `dataSourceId` values with `agentId`.

The examples below start with analytics-oriented connections. If you are
building a Qlik Talend Data Integration project, skip ahead to
[Data integration project connector examples](#data-integration-project-connector-examples).

## Analytics data connection examples

## Athena connection

<details>
    <summary>Standard - IAM credentials</summary>

    This example connects to an athena host directly from Qlik Cloud, using a service
    OAuth account.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"athena\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"AwsRegion\": \"<REGION>\",
            \"Catalog\": \"<CATALOG>\",
            \"Schema\": \"<SCHEMA>\",
            \"Workgroup\": \"<WORKGROUP>\",
            \"AuthenticationType\": \"<IAM_CREDENTIALS>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"S3OutputLocation\": \"<OUTPUT_BUCKET>\"
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - IAM credentials</summary>

    This example connects to an athena host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections),
    using a service OAuth account.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_athena\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"AwsRegion\": \"<REGION>\",
            \"Catalog\": \"<CATALOG>\",
            \"Schema\": \"<SCHEMA>\",
            \"Workgroup\": \"<WORKGROUP>\",
            \"AuthenticationType\": \"<IAM_CREDENTIALS>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"S3OutputLocation\": \"<OUTPUT_BUCKET>\"
        }
    }"
    ```
</details>

## AWS S3 connection

<details>
    <summary>File connection (S3 v2) - access key and secret key</summary>

    Creates a file connection to a bucket named `<BUCKET_NAME>`.

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
            \"region\": \"<BUCKET_REGION>\",
            \"bucketName\": \"<BUCKET_NAME>\"
        }
    }"
    ```
</details>

<details>
    <summary>File connection (S3 v2) - access key and secret key, new separated credentials</summary>

    Creates a file connection to a bucket
    named `<BUCKET_NAME>`, and creates
    a new set of credentials `<CREDENTIAL_NAME>` for the current user. Other
    users of this connection will need to provide their own credentials.

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
            \"separateCredentials\": \"true\",
            \"credentialsName\": \"<CREDENTIAL_NAME>\",
            \"region\": \"<BUCKET_REGION>\",
            \"bucketName\": \"<BUCKET_NAME>\"
        }
    }"
    ```
</details>

<details>
    <summary>File connection (S3 v2) - access key and secret key, existing separated credentials</summary>

    Creates a file connection to a bucket
    named `<BUCKET_NAME>`, and associates an existing
    set of credentials `<CREDENTIAL_ID>` for the current user. Other
    users of this connection will need to provide their own credentials.

    A list of credentials can be retrieved using
    the [Data credentials API](/apis/rest/data-credentials/).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: Bearer <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"File_AmazonS3ConnectorV2\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"region\": \"<BUCKET_REGION>\",
            \"bucketName\": \"<BUCKET_NAME>\",
            \"separateCredentials\": \"true\",
            \"selectedCredentials\": \"<CREDENTIAL_ID>\"
        }
    }"
    ```
</details>

<details>
    <summary>Metadata connection (S3 v2) - access key and secret key</summary>

    Creates a metadata connection to a bucket named `<BUCKET_NAME>`.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: Bearer <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"AmazonS3ConnectorV2\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"accessKey\": \"<CRED_USERNAME>\",
            \"secretKey\": \"<CRED_PASSWORD>\",
            \"region\": \"<BUCKET_REGION>\",
            \"bucketName\": \"<BUCKET_NAME>\"
        }
    }"
    ```
</details>

## Google Cloud Storage connection

<details>
    <summary>File connection - service account</summary>

    Creates a file connection to a bucket named `<BUCKET_NAME>`.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: Bearer <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"File_GoogleCloudStorageConnector\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"serviceAccountKeyFile\": 
            [
            {
                \"name\": \"mykeyfile.json\",
                \"value\": \"<KEY_FILE_CONTENTS>\"
            }
        ],
            \"bucketName\": \"<BUCKET_NAME>\"
        }
    }"
    ```
</details>

<details>
    <summary>Metadata connection - service account</summary>

    Creates a metadata connection to a bucket named `<BUCKET_NAME>`.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: Bearer <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"GoogleCloudStorageConnector\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"serviceAccountKeyFile\": 
            [
            {
                \"name\": \"mykeyfile.json\",
                \"value\": \"<KEY_FILE_CONTENTS>\"
            }
        ],
            \"bucketName\": \"<BUCKET_NAME>\"
        }
    }"
    ```
</details>

## Databricks connection

<details>
    <summary>Standard - username and password</summary>

    This example connects to a databricks host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"databricks\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"443\",
            \"Catalog\": \"<CATALOG>\",
            \"Schema\": \"<SCHEMA>\",
            \"HTTPPath\": \"<HTTP_PATH>\",
            \"AuthMech\": \"3\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"SSL\": \"true\"
        }
    }"
    ```
</details>

<details>
    <summary>Standard - username and password with trusted certificate</summary>

    This example connects to a databricks host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"databricks\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"443\",
            \"Catalog\": \"<CATALOG>\",
            \"Schema\": \"<SCHEMA>\",
            \"HTTPPath\": \"<HTTP_PATH>\",
            \"AuthMech\": \"3\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"SSL\": \"true\"
            \"TrustedCerts\": [
                {
                    \"name\": \"certificate.pem\",
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ]
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - username and password</summary>

    This example connects to a MySQL host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections).

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_databricks\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"443\",
            \"Catalog\": \"<CATALOG>\",
            \"Schema\": \"<SCHEMA>\",
            \"HTTPPath\": \"<HTTP_PATH>\",
            \"AuthMech\": \"3\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"SSL\": \"true\"
        }
    }"
    ```
</details>

## Google Big Query connection

<details>
    <summary>Standard - service account</summary>

    This example connects to a GBQ host directly from Qlik Cloud, using a service
    OAuth account.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"gbq\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"OAuthMechanism\": \"0\",
            \"Email\": \"<EMAIL>\",
            \"Catalog\": \"<CATALOG>\",
            \"KeyFilePath\": [
                {
                    \"name\": \"credentials.p12\",
                    \"value\": \"<CREDENTIALS>\"
                }
            ],
            \"P12CustomPwd\": \"<CREDENTIAL_PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - service account</summary>

    This example connects to a QBG host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections),
    using a service OAuth account.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_gbq\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"OAuthMechanism\": \"0\",
            \"Email\": \"<EMAIL>\",
            \"Catalog\": \"<CATALOG>\",
            \"KeyFilePath\": [
                {
                    \"name\": \"credentials.p12\",
                    \"value\": \"<CREDENTIALS>\"
                }
            ],
            \"P12CustomPwd\": \"<CREDENTIAL_PASSWORD>\"
        }
    }"
    ```
</details>

## MSSQL connection

<details>
    <summary>Standard - username and password</summary>

    This example connects to a MSSQL host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"mssql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"1433\",
            \"database\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - username and password</summary>

    This example connects to a MSSQL host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections).

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_mssql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"host\": \"<HOST>\",
            \"port\": \"1433\",
            \"database\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

## MySQL connection

<details>
    <summary>Standard - username and password</summary>

    This example connects to a MySQL host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"mysql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"3306\",
            \"database\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - username and password</summary>

    This example connects to a MySQL host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections).

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_mysql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"host\": \"<HOST>\",
            \"port\": \"3306\",
            \"database\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

## REST connection

<details>
    <summary>Qlik Cloud - encrypted header token</summary>

    This example connects to the users endpoint on the current tenant, and applies
    some endpoint specific limits and sorting. It also allows the `withConnection`
    statement which is required for dynamic control of the connection from application
    load scripts.

    When connecting to Qlik Cloud, a header is used for authorization. In this example,
    you are connecting to the same tenant in which you're creating the data connection,
    so you can use the same `<ACCESS_TOKEN>` for both the `data-connections` and `users` APIs.
    The `Authorization` header is encrypted using the `encrypt` attribute.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"https://<TENANT>/api/v1/users\",
            \"queryParameters\": [
              {
                  \"name\": \"sort\",
                  \"value\": \"+name\"
              },
              {
                  \"name\": \"limit\",
                  \"value\": \"50\"
              }
          ],
          \"queryHeaders\": [
              {
                  \"name\": \"Authorization\",
                  \"value\": \"Bearer <ACCESS_TOKEN>\",
                  \"encrypt\": true
              }
          ],
          \"allowWithConnection\": \"true\"
        }
    }"
    ```
</details>

<details>
    <summary>Standard - no auth</summary>

    This example connects to a REST endpoint with no authentication.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\"
        }
    }"
    ```
</details>

<details>
    <summary>Standard - Basic authentication</summary>

    This example connects to a REST endpoint with basic authentication.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\",
            \"serverCertificateValidation\": \"None\",
            \"authSchema\": \"basic\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD\"
        }
    }"
    ```
</details>

<details>
    <summary>Certificate validation - Basic authentication</summary>

    This example connects to a REST endpoint with basic authentication, and validates
    the connection certificate matches the one provided.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\",
            \"serverCertificateValidation\": \"Custom\",
            \"rootCertificates\": [
                {
                    \"name\": \"rootCA.cer\",
                    \"value\": \"<KEY_FILE_CONTENTS>\"
                }
            ],
            \"authSchema\": \"basic\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD\"
        }
    }"
    ```
</details>

<details>
    <summary>Certificate validation and mutual SSL/TLS - no auth</summary>

    This example connects to a REST endpoint, validates
    the connection certificate matches the one provided, with mutual SSL/TLS.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\",
            \"serverCertificateValidation\": \"Custom\",
            \"rootCertificates\": [
                {
                    \"name\": \"rootCA.cer\",
                    \"value\": \"<KEY_FILE_CONTENTS>\"
                }
            ],
            \"enableMutualSSL\": \"true\",
            \"mutualPfxCertificateFiles\": [
                {
                    \"name\": \"certificate.pfx\",
                    \"value\": \"<KEY_FILE_CONTENTS>\"
                }
            ],
            \"mutualPfxCertificateKey\": \"<CERTIFICATE_PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Offset pagination - no auth</summary>

    This example connects to a REST endpoint and passes offset pagination params.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\",
            \"PaginationType\": \"Offset\",
            \"OffsetStartField\": \"header-startAt\",
            \"IsOffsetStartFieldHeader\": \"true\",
            \"OffsetStartFieldValue\": \"500\",
            \"OffsetCountFieldName\": \"count\",
            \"OffsetCountValue\": \"1000\",
            \"OffsetTotalPath\": \"root/Total\",
            \"OffsetDataPath\": \"\"
        }
    }"
    ```
</details>

<details>
    <summary>Query params - no auth</summary>

    This example connects to a REST endpoint with no authentication, and passes
    two query params.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"rest\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"url\": \"<REST_ENDPOINT>\",
            \"queryParameters\": [
                {
                    \"name\": \"Name0\",
                    \"value\": \"Value0\"
                },
                {
                    \"name\": \"Name1\",
                    \"value\": \"Value1\"
                }
            ]
        }
    }"
    ```
</details>

## SFTP connection

<details>
    <summary>Standard - public key with username and password</summary>

    This example connects to a SFTP host using a public key
    alongside the user and password auth.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"File_FileTransferConnector\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<SFTP_HOSTNAME>\",
            \"sftpPort\": \"<SFTP_PORT>\",
            \"publicKeyAlgorithm\": \"RSA\",
            \"publicKey\": \"<CRED_PUBLIC_KEY>\",
            \"username\": \"<CRED_USERNAME>\",
            \"password\": \"<CRED_PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Standard - public key fingerprint with private key</summary>

    This example connects to AWS Transfer Family's SFTP service, on
    host `abs.server.transfer.us-east-1.amazonaws.com`. It uses a public key fingerprint
    alongside the full private key and username for auth.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"File_FileTransferConnector\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"abs.server.transfer.us-east-1.amazonaws.com\",
            \"sftpPort\": \"22\",
            \"publicKeyAlgorithm\": \"RSA\",
            \"publicKeyFingerprint\": \"<CRED_FINGERPRINT>\",
            \"username\": \"<CRED_USERNAME>\",
            \"privateKey\": [
                {
                    \"name\": \"mykey.pem\",
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ]
        }
    }"
    ```
</details>

<details>
    <summary>Standard - public key fingerprint with username and password</summary>

    This example connects to a SFTP host using a public key fingerprint
    alongside the user and password auth.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"File_FileTransferConnector\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<SFTP_HOSTNAME>\",
            \"sftpPort\": \"<SFTP_PORT>\",
            \"publicKeyAlgorithm\": \"RSA\",
            \"publicKeyFingerprint\": \"<CRED_FINGERPRINT>\",
            \"username\": \"<CRED_USERNAME>\",
            \"password\": \"<CRED_PASSWORD>\"
        }
    }"
    ```
</details>

## Snowflake connection

<details>
    <summary>Standard - username and password</summary>

    This example connects to a Snowflake host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"snowflake\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"server\": \"<HOST>\",
            \"port\": \"443\",
            \"database\": \"<DATABASE_NAME>\",
            \"schema\": \"<SCHEMA_NAME>\",
            \"warehouse\": \"<WAREHOUSE_NAME>\",
            \"role\": \"<USER_ROLE>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
    }
    ```
</details>

<details>
    <summary>Standard - Key-pair</summary>

    This example connects to a Snowflake host directly from Qlik Cloud using
    key-pair authentication.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"snowflake\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"server\": \"<HOST>\",
            \"port\": \"443\",
            \"database\": \"<DATABASE_NAME>\",
            \"schema\": \"<SCHEMA_NAME>\",
            \"warehouse\": \"<WAREHOUSE_NAME>\",
            \"role\": \"<USER_ROLE>\",
            \"username\": \"<USERNAME>\",
            \"authenticator\": \"snowflake_jwt\",
            \"PRIV_KEY_FILE\": [
                {
                    \"name\" : \"<NAME_OF_KEY_FILE>\", 
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ]
    }
    ```
</details>

<details>
    <summary>Direct Access Gateway - username and password</summary>

    This example connects to a Snowflake host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections).

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_snowflake\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"server\": \"<HOST>\",
            \"port\": \"443\",
            \"database\": \"<DATABASE_NAME>\",
            \"schema\": \"<SCHEMA_NAME>\",
            \"warehouse\": \"<WAREHOUSE_NAME>\",
            \"role\": \"<USER_ROLE>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

## Teradata connection

<details>
    <summary>Standard - username and password</summary>

    This example connects to a Teradata host directly from Qlik Cloud.

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"teradata\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"host\": \"<HOST>\",
            \"port\": \"1025\",
            \"db\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Direct Access Gateway - username and password</summary>

    This example connects to a Teradata host via
    the [Qlik Direct Access Gateway](/manage/data-connections/gateway-data-connections).

    If you wish to
    utilize [separated credentials](/manage/data-connections/auth-data-connections#using-separated-credentials)
    for this connection, review the [AWS S3 examples](#aws-s3-connection).

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"DG_teradata\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"gatewayInstance\": \"<GATEWAY_ID>\",
            \"host\": \"<HOST>\",
            \"port\": \"1433\",
            \"db\": \"<DATABASE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

## Data integration project connector examples

These examples create connections for the Qlik Talend Data Integration
connector stack. Use them when the connection will be selected as a source,
target, platform, or staging connection in a data integration project, not when
you are loading data directly into an analytics app.

Most source connectors and self-managed targets in this stack use
`repsrc_...` or `reptgt_...` `dataSourceId` values and expect an `agentId`
that points to your Data Gateway - Data Movement agent. Some managed cloud
targets use a Qlik-managed gateway identifier instead, represented in the
examples below as `<QLIK_MANAGED_GATEWAY_ID>`. For the exact property schema
for each connector, retrieve the connector spec with the
[Data Sources API](https://qlik.dev/apis/rest/data-sources/).

### Source connectors

<details>
    <summary>MySQL source</summary>

    This example creates a MySQL source connection for a data integration
    project that runs through a Data Movement agent.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"repsrc_mysql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"<HOST>\",
            \"port\": \"3306\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"mysql###None\",
            \"sshEnable\": false,
            \"sslMode\": \"PREFER\",
            \"eventsPollInterval\": \"5\"
        }
    }"
    ```
</details>

<details>
    <summary>Microsoft SQL Server source</summary>

    This example creates a Microsoft SQL Server source connection for a data
    integration project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"repsrc_mssql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"<HOST>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"sqlServer###None\",
            \"useEncryptedConnection\": false,
            \"databaseManualInput\": false,
            \"database\": \"<DATABASE_NAME>\",
            \"safeguardPolicy\": \"RELY_ON_SQL_SERVER_REPLICATION_AGENT\",
            \"safeguardFrequency\": \"300\",
            \"TlogAccessMode\": \"PreferTlog\",
            \"useWindowsAuthentication\": false,
            \"use3rdPartyBackupDevice\": false
        }
    }"
    ```
</details>

<details>
    <summary>PostgreSQL source</summary>

    This example creates a PostgreSQL source connection for a data integration
    project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"repsrc_postgresql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"<HOST>\",
            \"port\": \"5432\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"postgresqlsource###None\",
            \"database\": \"<DATABASE_NAME>\",
            \"sslMode\": \"PREFER\",
            \"sslCompression\": true,
            \"captureDDLs\": true,
            \"heartbeatEnable\": false,
            \"ddlArtifactsSchema\": \"public\"
        }
    }"
    ```
</details>

<details>
    <summary>Oracle source</summary>

    This example creates an Oracle source connection for a data integration
    project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"repsrc_oracle\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"//<HOST>:1521/<SERVICE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"numberDatatypeScale\": \"10\",
            \"allowSelectNestedTables\": false,
            \"replicateInvisibleColumns\": false,
            \"retryInterval\": \"5\",
            \"archivedLogDestId\": \"0\",
            \"additionalArchivedLogDestId\": \"0\",
            \"archivedLogsOnly\": false,
            \"useLogminerReader\": false,
            \"parallelASMReadThreads\": \"1\"
        }
    }"
    ```
</details>

### Target connectors

<details>
    <summary>MySQL target</summary>

    This example creates a MySQL target connection for a data integration
    project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdimysql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"<HOST>\",
            \"port\": \"3306\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"mysqltarget###None\",
            \"targetDbType\": \"MULTIPLE_DATABASES\",
            \"maxFileSize\": \"32000\",
            \"parallelLoadThreads\": \"2\"
        }
    }"
    ```
</details>

<details>
    <summary>Microsoft SQL Server target</summary>

    This example creates a Microsoft SQL Server target connection for a data
    integration project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_mssqltarget\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"<HOST>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"sqlServer###None\",
            \"AuthenticationModes\": \"SQL_CREDENTIALS\",
            \"useEncryptedConnection\": false,
            \"useWindowsAuthentication\": false,
            \"suspendTableWithComputedColumn\": true,
            \"databaseManualInput\": false,
            \"database\": \"<DATABASE_NAME>\"
        }
    }"
    ```
</details>

<details>
    <summary>PostgreSQL target</summary>

    This example creates a PostgreSQL target connection for a data integration
    project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdipostgresql\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"host\": \"<HOST>\",
            \"port\": \"5432\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\",
            \"replicateEndpointType\": \"postgresql###None\",
            \"database\": \"<DATABASE_NAME>\",
            \"sslMode\": \"PREFER\",
            \"sslCompression\": true,
            \"maxFileSize\": \"32000\"
        }
    }"
    ```
</details>

<details>
    <summary>Oracle target</summary>

    This example creates an Oracle target connection for a data integration
    project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdioracle\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<AGENT_ID>\",
            \"server\": \"//<HOST>:1521/<SERVICE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"password\": \"<PASSWORD>\"
        }
    }"
    ```
</details>

<details>
    <summary>Snowflake target</summary>

    This example creates a Snowflake target connection for a data integration
    project using key-pair authentication.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdisnowflake\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"server\": \"<HOST>\",
            \"port\": \"443\",
            \"databaseManualInput\": true,
            \"databaseQcsString\": \"<DATABASE_NAME>\",
            \"warehouse\": \"<WAREHOUSE_NAME>\",
            \"username\": \"<USERNAME>\",
            \"authentication_mode\": \"KEY_PAIR\",
            \"privateKeyFile\": [
                {
                    \"name\": \"snowflake_rsa_key.p8\",
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ],
            \"privateKeyPassphrase\": \"<PRIVATE_KEY_PASSPHRASE>\"
        }
    }"
    ```
</details>

<details>
    <summary>Databricks target</summary>

    This example creates a Databricks target connection for a data integration
    project using a personal access token.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdidatabricks\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"server\": \"<HOST>\",
            \"port\": \"443\",
            \"httpPath\": \"<HTTP_PATH>\",
            \"password\": \"<PERSONAL_ACCESS_TOKEN>\",
            \"authenticationMode\": \"PERSONAL_ACCESS_TOKEN\"
        }
    }"
    ```
</details>

<details>
    <summary>Google BigQuery target</summary>

    This example creates a Google BigQuery target connection for a data
    integration project.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdibigquery\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"datasetLocation\": \"<DATASET_LOCATION>\",
            \"jsonCredentials\": [
                {
                    \"name\": \"service-account.json\",
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ]
        }
    }"
    ```
</details>

<details>
    <summary>Azure Data Lake Storage target</summary>

    This example creates an Azure Data Lake Storage target connection for a data
    integration project using the Qlik-managed gateway.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdiadls\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<QLIK_MANAGED_GATEWAY_ID>\",
            \"adlsLoginUrl\": \"https://login.microsoftonline.com/\",
            \"storageAccount\": \"<STORAGE_ACCOUNT>\",
            \"fileSystem\": \"<FILE_SYSTEM>\",
            \"adlstenantid\": \"<TENANT_ID>\",
            \"adlsclientappid\": \"<CLIENT_ID>\",
            \"adlsclientappkey\": \"<CLIENT_SECRET>\"
        }
    }"
    ```
</details>

<details>
    <summary>Amazon S3 target</summary>

    This example creates an Amazon S3 target connection for a data integration
    project using the Qlik-managed gateway.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdis3\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<QLIK_MANAGED_GATEWAY_ID>\",
            \"bucketName\": \"<BUCKET_NAME>\",
            \"s3AccessKey\": \"<ACCESS_KEY>\",
            \"s3SecretKey\": \"<SECRET_KEY>\",
            \"useAwsPrivateLink\": false
        }
    }"
    ```
</details>

<details>
    <summary>Google Cloud Storage target</summary>

    This example creates a Google Cloud Storage target connection for a data
    integration project using the Qlik-managed gateway.

    ```bash
    curl -L "https://<TENANT>/api/v1/data-connections" ^
    -H "Content-Type: application/json" ^
    -H "Authorization: <ACCESS_TOKEN>" ^
    -d "{
        \"dataSourceId\": \"reptgt_qdigooglecloudstorage\",
        \"qName\": \"<CONNECTION_NAME>\",
        \"space\": \"<SPACE_ID>\",
        \"connectionProperties\": {
            \"agentId\": \"<QLIK_MANAGED_GATEWAY_ID>\",
            \"bucketName\": \"<BUCKET_NAME>\",
            \"jsonCredentials\": [
                {
                    \"name\": \"service-account.json\",
                    \"value\": \"<BASE_64_ENCODED_KEY_FILE_CONTENTS>\"
                }
            ]
        }
    }"
    ```
</details>
