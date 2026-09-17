---
source: https://qlik.dev/manage/data-connections/auth-data-connections/
last_updated: 2026-09-01T10:20:53+02:00
---

# Use interactive auth or separated credentials

## Overview

Some data connections in Qlik Cloud support interactive authentication
patterns, and/or support the storage of their credentials separate to the data
connection definition.

Interactive credentials are those which require a user to visit a web page to log
in and click a button to authorize the use of these credentials with the connection.

Separated credentials allow each user of a data connection to bring their own
authentication, rather than requiring the owner of the data connection to embed
their credentials in the connection.

If you are not familiar with creating data connections, or you wish to
create a connection using password, key, or certificate based credentials, see
[Create data connections](https://qlik.dev/manage/data-connections/create-data-connections).

## Requirements

- You have reviewed the prerequisites in [Create data connections](https://qlik.dev/manage/data-connections/create-data-connections).

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
| `<SPACE_ID>`        | The ID of the space you'll create data connections in.                                                                                        |
| `<CONNECTION_ID>`   | The ID for the data connection created in `<SPACE_NAME>`.                                                                                     |
| `<CONNECTION_NAME>` | The ID for the data connection to be created in `<SPACE_NAME>`.                                                                               |
| `<CRED_OAUTH>`      | An OAuth code for `<CONNECTION_NAME>`, for use with interactive OAuth - must be copied from an interactive session.                           |

## Using separated credentials

By default, the credentials that you enter when you create the data connection
are shared with all users of that data connection. Some data sources support a
feature called separated credentials, which means that when another user uses the
data connection, they are required to bring their own credentials for the connection.

If you wish to use separated credentials, verify that the data source supports
the attribute `separateCredentials`, and then set this to `true`.

> **Note:** Credentials created on data connections where `separateCredentials` is set to `true` will not be deleted if the data
> connection is deleted. These can be reused with other data connections made to the same data source, or they can be
> deleted using the `data-credentials` API.

> **Note:** When you use `PATCH /data-connections/{id}` to change the host of a connection that uses separate credentials, the
> associated credentials are deassociated automatically. You must re-associate or supply new credentials after the
> update.

To create a new connection to AWS S3 with a set of separated credentials
named `serviceAccount123` for the current user:

```bash
curl -L "https://<TENANT>/api/v1/data-connections" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
    \"dataSourceId\": \"File_AmazonS3Connector\",
    \"qName\": \"<CONNECTION_NAME>\",
    \"space\": \"<SPACE_ID>\",
    \"connectionProperties\": {
        \"accessKey\": \"<CRED_USERNAME>\",
        \"secretKey\": \"<CRED_PASSWORD>\",
        \"separateCredentials\": \"true\",
        \"credentialsName\": \"serviceAccount123\",
        \"region\": \"<BUCKET_REGION>\",
        \"bucketName\": \"<BUCKET_NAME>\"
    }
}"
```

If you wish to create another connection to AWS S3, leveraging a previously created
set of credentials with the name `serviceAccount123`, you should first
retrieve the ID of these credentials from `data-credentials`:

```bash
curl -L "https://<TENANT>/api/v1/data-credentials/serviceAccount123?byCredentialName=true" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

If found, this returns a `200`:

```json
{
    "connectionId": "",
    "created": "2024-03-01T14:35:23.829Z",
    "datasourceID": "File_AmazonS3Connector",
    "links": {
        "self": {
            "href": "https://<TENANT>/v1/data-credentials/<CREDENTIAL_ID>"
        }
    },
    "qConnCount": 0,
    "qID": "<CREDENTIAL_ID>",
    "qName": "serviceAccount123",
    "qSeparated": 1,
    "qType": "QvWebStorageProviderConnectorPackage.exe",
    "updated": "2024-03-01T14:35:23.829Z"
}
```

Using the `<CREDENTIAL_ID>` you can now create a new connection to the same
data source with the credential:

```bash
curl -L "https://<TENANT>/api/v1/data-connections" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{
    \"dataSourceId\": \"File_AmazonS3Connector\",
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

If successful it will return `201` created, and the new data connection definition.

## Create data connection with interactive authentication

*If you are not using interactive OAuth for authentication, such as a certificate or username and password credentials,
see [Create data connections](https://qlik.dev/manage/data-connections/create-data-connections).*
Some data sources support or require the use of interactive OAuth authorization,
which requires a different API call flow to retrieve the callback URL for the
connector.

There is a three step process:

1. Send an unauthenticated request to the `data-connections` API to request creation of the
   new connection. This will return a URL which must be accessed interactively.
2. Manually go to the returned URL to complete the OAuth auth, and collect the
   provided auth code.
3. Send a second request to the `data-connections` API with the correct auth code.

For creating a connection to a Google Big Query Catalog by the name of `gbq-example-catalog`,
you first send this request with the `authUrlOnly` parameter set to `true`:

```bash
curl -L "https://<TENANT>/api/v1/dcaas/actions/data-connections" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{ 
    \"dataSourceId\": \"gbq\", 
    \"connectionName\": \"<CONNECTION_NAME>\", 
    \"spaceId\": \"<SPACE_ID>\", 
    \"authUrlOnly\": \"true\", 
    \"connectionProperties\": { 
        \"OAuthMechanism\": \"1\", 
        \"Catalog\": \"gbq-example-catalog\", 
        \"authCode\": \"\" 
    } 
}"
```

The system will return a `HTTP 201` code and the following response:

```json
{
    "authUrl": "https://accounts.google.com/o/oauth2/v2/auth?client_id=apps.googleusercontent.com&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fbigquery&redirect_uri=https%3A%2F%2Fconnector.qlik.com&prompt=consent&access_type=offline&state=fb9...&code_challenge=0b1...&code_challenge_method=S256"
}
```

Opening the `authUrl` will begin an interactive prompt which results in an authentication
code, which is `<CRED_OAUTH>`. This code can be used in the final response to the system.
Either set the value of `authUrlOnly` to `false`, or omit it:

```bash
curl -L "https://<TENANT>/api/v1/dcaas/actions/data-connections" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{ 
    \"dataSourceId\": \"gbq\", 
    \"connectionName\": \"<CONNECTION_NAME>\", 
    \"spaceId\": \"<SPACE_ID>\", 
    \"connectionProperties\": { 
        \"OAuthMechanism\": \"1\", 
        \"Catalog\": \"gbq-example-catalog\", 
        \"authCode\": \"<CRED_OAUTH>\" 
    } 
}"
```

This results in the normal `HTTP 201` response and the new connection being
returned by the API.
