---
source: https://qlik.dev/manage/data-connections/gateway-data-connections/
last_updated: 2026-09-01T10:20:53+02:00
---

# Connect via a direct access data gateway

## Overview

Businesses commonly enforce strict firewall policies that block external access
to their data sources. This presents a challenge when such businesses need to
access their data from the cloud for analytics. Qlik Data Gateway - Direct
Access overcomes this challenge by eliminating the need to open inbound firewall ports.
Operating behind your organization's firewall, the Direct Access gateway allows
Qlik Cloud applications to securely access behind-the-firewall data, over a
an outbound-only, encrypted, and mutually authenticated connection.

For more information, see the [Direct Access gateway documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm)
on Qlik Help.

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
| `<CONNECTION_NAME>` | The ID for the data connection to be created in `<SPACE_ID>`.                                                                                 |
| `<USERNAME>`        | The username for connecting to the data source.                                                                                               |
| `<PASSWORD>`        | The password for connecting to the data source.                                                                                               |

## Create connections via a direct access data gateway

Prior to creating a connection via a direct access data gateway, you must [install
and configure a direct access gateway](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

Once created, you can retrieve a list of available data gateways for your required
data source using the [Data sources API](https://qlik.dev/apis/rest/data-sources/).

This example retrieves all data gateways on the tenant for the `DG_mssql` data source,
which connects to MSSQL hosts via a gateway:

```bash
curl -L "https://<TENANT>/api/v1/data-sources/DG_mssql/gateways" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

If the data source supports data gateways and you have a supported data gateway
on the tenant, it will return a `200` response:

```json
{
    "gateways": [
        {
            "name": "My Direct Access Gateway (in Azure)",
            "id": "Rm5Qk-KThkESl5ajnVxuiXZAczfSHo7h::dL1IyMf6DGSp3FV1NmrPJ7eAEA0qd-YR",
            "default": true
        }
    ],
    "refreshedAt": "2024-02-29T17:34:00.689Z"
}
```

Once you have the data gateway ID, you can add this to the `connectionProperties`
for your new connection. In most cases, the only difference between standard
(direct from Qlik Cloud) and gateway connection requests is the `dataSourceId`
field (for example, `DG_mssql` rather than `mssql`) and the addition of the
`gatewayInstance` property.

This example connects to a MSSQL host via
the [Qlik Direct Access Gateway](https://qlik.dev/manage/data-connections/gateway-data-connections).

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

Successful creation of the connection will result in a `201` response:

```json
{
    "created": "2024-03-01T10:21:12.659Z",
    "datasourceID": "DG_mssql",
    "id": "5bdc7893-866d-4374-98bf-0a0a5fa480b6",
    "links": {
        "self": {
            "href": "https://orchestration.eu.qlikcloud.com/v1/data-connections/5bdc7893-866d-4374-98bf-0a0a5fa480b6"
        }
    },
    "privileges": [
        "read",
        "update",
        "delete"
    ],
    "qArchitecture": 0,
    "qConnectStatement": "<CONNECTION_STRING>",
    "qCredentialsID": "d27e78a4-d411-468e-9118-4a17b0a4f802",
    "qEngineObjectID": "5bdc7893-866d-4374-98bf-0a0a5fa480b6",
    "qID": "5bdc7893-866d-4374-98bf-0a0a5fa480b6",
    "qLogOn": 1,
    "qName": "<CONNECTION_NAME>",
    "qSeparateCredentials": false,
    "qType": "QlikConnectorsCommonService.exe",
    "qri": "qri:db:sqlserver://ep2ro0_lZFOCjDjSa1jNvI7tihjx0NGcfeKTJ9Nb0Hs",
    "space": "65cf6b6c51618b6abd5848d1",
    "tags": [
        "DcaasAPI:QlikConnectorsCommonService.exe:1.202.0"
    ],
    "tenant": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "updated": "2024-03-01T10:54:56.996Z",
    "user": "637390ef6541614d3a88d6c3",
    "version": "V1"
}
```
