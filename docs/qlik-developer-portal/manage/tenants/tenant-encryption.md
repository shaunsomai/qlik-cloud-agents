---
source: https://qlik.dev/manage/tenants/tenant-encryption/
last_updated: 2026-04-20T13:34:03+01:00
---

# Configure tenant encryption

In this tutorial, you are going to learn how to perform Customer Managed Key
encryption key lifecycle management tasks using Qlik Cloud management APIs.

Qlik Cloud supports the following key management service providers:

- Qlik Internal KMS (this is the default KMS using Qlik-managed keys).
- Amazon Web Service Key Management Service (AWS KMS).

> **Note:** The CMK APIs allow for lifecycle management of key provider entries within
> Qlik Cloud. Creation and management of the lifecycle of AWS KMS Keys needs to be
> performed within AWS KMS.

## Prerequisites

- You have a basic understanding of Qlik Cloud and access control rules for
  creating content and managing spaces.
- You have a Symmetric AWS KMS key and you have configured a key policy. For more information, see
  [Configure the AWS KMS key policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-tenant-encryption.htm)
  on Qlik Help.
- cURL for running the inline examples.

> **Note:** The cURL examples in this topic show the command syntax for
> Windows Command Prompt. If you are using another command line interface,
> different syntax may be required for line continuation. You may also need to
> adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable              | Description                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`            | The URL for the tenant where you are managing encryption keys. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                         |
| `<ACCESS_TOKEN>`      | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<TENANT_ID>`         | The unique identifier of the tenant.                                                                                                          |
| `<KMS_KEY_ARN>`       | The Amazon Resource Name of the KMS key.                                                                                                      |
| `<ARN_FINGERPRINT>`   | The unique identifier of the KMS key.                                                                                                         |
| `<KEY_PROVIDER_NAME>` | The name of the key provider that you are adding to the tenant.                                                                               |

## Create a new key provider in the tenant

Before you create the key provider, verify that your AWS KMS key and policy have
been correctly configured in AWS KMS. For more information, see [AWS Key Management Service (KMS)](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-tenant-encryption.htm)
on Qlik Help.
Take note of the KMS key ARN as you will need it to create a new key provider.

Here's an example of a cURL command that creates a new key provider:

```bash
curl -L "<TENANT>/api/v1/encryption/keyproviders" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"<KEY_PROVIDER_NAME>\", \"arn\": \"<KMS_KEY_ARN>\", \"keyprovider\": \"AWS-KMS\" }"
```

The result is a JSON object that shows the details of the newly created KMS key provider.

```json
{
    "name": "<KEY_PROVIDER_NAME>",
    "tenantId": "<TENANT_ID>",
    "arn": "<KMS_KEY_ARN>",
    "arnFingerPrint": "<ARN_FINGERPRINT>",
    "keyprovider": "AWS-KMS",
    "createdAt": "2023-07-14T18:17:23Z",
    "promotedToCurrentAt": "0001-01-01T00:00:00Z",
    "demotedFromCurrentAt": "0001-01-01T00:00:00Z"
}
```

## Get key provider details

If you want to know the details of a specific key provider, for example,
you want to know its `<ARN_FINGERPRINT>`, you can make a request to retrieve
key provider details.

Here's an example of a cURL command that retrieves details of all the key
providers registered in the tenant:

```bash
curl -L "<TENANT>/api/v1/encryption/keyproviders" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" 
```

The result is an array of JSON objects that shows the details of the key providers.

```bash
[
    {
        "name": "keyProvider1",
        "tenantId": "<TENANT_ID>",
        "arn": "<KMS_KEY_ARN>",
        "arnFingerPrint": "<ARN_FINGERPRINT>",
        "keyprovider": "AWS-KMS",
        "createdAt": "2023-07-14T12:32:02Z",
        "promotedToCurrentAt": "2023-07-14T13:12:35Z",
        "demotedFromCurrentAt": "2023-07-17T11:40:32Z"
    },
    {
        "name": "keyProvider2",
        "tenantId": "<TENANT_ID>",
        "arn": "<KMS_KEY_ARN>",
        "arnFingerPrint": "<ARN_FINGERPRINT>",
        "keyprovider": "AWS-KMS",
        "current": true,
        "createdAt": "2023-07-14T18:17:23Z",
        "promotedToCurrentAt": "2023-07-18T12:08:04Z",
        "demotedFromCurrentAt": "0001-01-01T00:00:00Z"
    }
]
```

## Change the key provider in the tenant

You can migrate a key provider from Qlik KMS to AWS KMS, AWS KMS to another
AWS KMS, or revert to Qlik KMS from AWS KMS. During the key migration process,
the tenant will continue to function as usual with no impact to users.
Only one key migration activity can be active for a tenant at a time.

Here's an example of a cURL command that migrates the currently active key
provider to another key provider specified by `<ARN_FINGERPRINT>`. Upon
successful migration, the migrated key provider becomes active.

```bash
curl -L -X POST "https://<TENANT>/api/v1/encryption/keyproviders/<ARN_FINGERPRINT>/actions/migrate" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The result is a JSON object that shows the details of the key provider migration.

```json
{
    "migrationId": "c75088bc-cfba-410a-aeda-2a5dd797f528",
    "tenantId": "<TENANT_ID>",
    "migratingFrom": "v1:rTfjXBtXurvLxUJqE4dvgyXIm6zLiaIE:iiTaqy+LNXkmCVEBN9mOwKwsNQZ0UdNUWW7s5TptbOrU67qAALinKb+UZUKBHYgVGflHmp2t2CvtBK4G",
    "migratingTo": "<KMS_KEY_ARN>",
    "migratingToFingerPrint": "<ARN_FINGERPRINT>",
    "migratingToPrefix": "#BYOKv1#:<ARN_FINGERPRINT>",
    "state": "New",
    "initiatedAt": "2023-07-18T12:08:04.634711507Z",
    "completedAt": "0001-01-01T00:00:00Z"
}
```

## Delete a key provider in the tenant

Any key provider, with the exception of the default Qlik key provider, can be
deleted if it is inactive in the tenant.

Here's an example of a cURL command that deletes the key provider in the tenant:

```bash
curl -L -X DELETE "https://<TENANT>/api/v1/encryption/keyproviders/<ARN_FINGERPRINT>" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The result is a JSON object that displays a message.

```json
{
    "message": "Keyprovider metadata deleted successfully"
}
```
