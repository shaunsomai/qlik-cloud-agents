---
source: https://qlik.dev/manage/data-connections/examples/audit-data-connections-examples/
last_updated: 2026-03-18T16:49:43Z
---

# Data connection audit examples

These examples demonstrate how to audit data connections and delete
connections to unapproved data sources.

> **Note:** Tenant administrators can enable or disable specific data sources on a tenant using the
> [data-sources API](https://qlik.dev/changelog/172-api-updates-data-source-settings/).

A common requirement in enterprise deployments is for users to have authoring
access to create Qlik Sense applications, but to specific data sources only. This aims
to reduce the risk of data being exported to unapproved or third-party data sources
such as personal Dropbox or other external accounts.

One solution is to set up a script that runs on a regular schedule to detect and delete data connections
to unapproved sources while logging the users who created the connections.

To learn more about data connection APIs in Qlik Cloud,
review the [data connections overview](https://qlik.dev/manage/data-connections/).

<details>
    <summary>
    
    ## Remove data connections - Powershell/ qlik-cli
    
    </summary>

    This example deletes any S3 file connections found on the tenant and logs
    information about the connection to the local disk.

    ```powershell
    # This script doesn't do error handling or tracking, it simply 'does'
    # Set the connection type to delete
    $connectionToDeleteType = 'File_AmazonS3Connector';

    # Grab all non-datafile connections
    $dataConnections = qlik raw get v1/data-connections --query noDatafiles=true | ConvertFrom-Json

    # Create a new object containing only connections with the connection type we want to delete
    $connectionsToDelete = Foreach ($dataConnection in $dataConnections) {
        If ($dataConnection.datasourceID -eq $connectionToDeleteType) {
            New-Object PSObject $dataConnection;
        }
    }

    # Save this object down into a CSV file before attempting deletion
    $connectionsToDelete | Export-Csv -Path ".\ConnectionsToDelete_$($connectionToDeleteType)_$(get-date -f yyyyMMdd_hhmmss).csv" -NoTypeInformation

    # Delete connections of the specified type
    Foreach ($connectionToDelete in $connectionsToDelete) {
        If ($connectionToDelete.datasourceID -eq $connectionToDeleteType) {
            qlik raw delete v1/data-connections/$($connectionToDelete.id)
        }
    }
    ```
</details>

<details>
    <summary>
    
    ## Remove data connections - Qlik Automate
    
    </summary>

    This example deletes any connection with a data source not specified
    in the `approvedSources` variable . It sends an email to each user to notify them
    of the deletion, and outputs the deleted connections and their definitions.

Email notification:
    <Image src={auditDataConnections} alt="email output send when connection has been deleted" />

Copy, and paste this snippet into a new automation workspace:

    ```json
    {"blocks":[{"id":"EA8CFA07-3EBE-4297-BBFB-BA6A263CD80D","type":"VariableBlock","disabled":false,"name":"approvedSources","displayName":"Variable - approvedSources","comment":"Add each permitted data source here as an item in the list","childId":"4E6CFE3D-D8E2-4EA9-8D9B-BCB83E0C046D","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-375,"y":213,"variableGuid":"B5594ED9-5EEC-4499-91F9-8E7A7D5D093F","operations":[{"id":"add_item","key":"B8F26C62-B4BC-4136-848B-82714601E9B8","name":"Add item to { variable }","value":"rest"}]},{"id":"4E6CFE3D-D8E2-4EA9-8D9B-BCB83E0C046D","type":"EndpointBlock","disabled":false,"name":"getCurrentTenantInfo","displayName":"Qlik Cloud Services - Get Current Tenant Info","comment":"","childId":"CC69A96E-AED6-42F8-96A4-8FB167C34533","inputs":[],"settings":[{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":508,"y":242,"datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"55051480-cb86-11ec-b746-892c1d04114e","endpoint_role":"get"},{"id":"CC69A96E-AED6-42F8-96A4-8FB167C34533","type":"EndpointBlock","disabled":false,"name":"listDataConnections","displayName":"Qlik Cloud Services - List Data Connections","comment":"","childId":"26D4F41F-78C9-4473-A2C8-F2FFE78471A6","inputs":[],"settings":[{"id":"maxitemcount","value":"","type":"string","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":360,"loopBlockId":"3D976CA8-1314-419F-AA92-4E4EE8F9DB58","datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"2c30aa50-4f34-11eb-9ed0-85d3ebe3b610","endpoint_role":"list"},{"id":"26D4F41F-78C9-4473-A2C8-F2FFE78471A6","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"","childId":null,"inputs":[{"id":"input","value":"{$.connections}","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":808,"y":480},{"id":"3D976CA8-1314-419F-AA92-4E4EE8F9DB58","type":"IfElseBlock","disabled":false,"name":"condition","displayName":"Condition","comment":"If data source isn't in the approvedSources list","childId":null,"inputs":[{"id":"conditions","value":{"mode":"all","conditions":[{"input1":"{ $.approvedSources }","operator":"notInList","input2":"{ $.listDataConnections.item.datasourceID }"},{"input1":"{$.listDataConnections.item.qName}","operator":"!=","input2":"DataFiles"},{"input1":"{$.listDataConnections.item.user}","operator":"notEmpty","input2":null}]},"type":"custom","structure":[]}],"settings":[],"collapsed":[{"name":"both","isCollapsed":false},{"name":"yes","isCollapsed":false},{"name":"no","isCollapsed":false}],"x":-333,"y":206,"childTrueId":"F32CA5BE-6A48-4FE3-9F8B-14EE92693F14","childFalseId":null},{"id":"F32CA5BE-6A48-4FE3-9F8B-14EE92693F14","type":"EndpointBlock","disabled":false,"name":"getUser","displayName":"Qlik Cloud Services - Get User","comment":"","childId":"590984B4-F951-4FC7-87AD-2F21EAB6E98E","inputs":[{"id":"8eedf1d0-c7a5-11ea-9022-0fb2ce625902","value":"{$.listDataConnections.item.user}","type":"string","structure":[]}],"settings":[{"id":"blendr_on_error","value":"warning","type":"select","displayValue":"Warning - Continue Automation and report errors","structure":[]},{"id":"cache","value":"0","type":"select","displayValue":"None","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":612,"y":372,"datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"7e670290-c7a5-11ea-9a9c-6dd2b282df86","endpoint_role":"get"},{"id":"590984B4-F951-4FC7-87AD-2F21EAB6E98E","type":"EndpointBlock","disabled":false,"name":"getSpace","displayName":"Qlik Cloud Services - Get Space","comment":"","childId":"B81C27E9-C7B4-416F-8921-A1FE89A3E7FD","inputs":[{"id":"92f7bcd0-6d2d-11eb-9088-69419de8f253","value":"{$.listDataConnections.item.space}","type":"string","structure":[]}],"settings":[{"id":"blendr_on_error","value":"ignore","type":"select","displayValue":"Ignore - Continue Automation and ignore errors","structure":[]},{"id":"cache","value":"0","type":"select","displayValue":"None","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":612,"y":252,"datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"92afefd0-6d2d-11eb-aee2-055653605a8e","endpoint_role":"get"},{"id":"B81C27E9-C7B4-416F-8921-A1FE89A3E7FD","type":"VariableBlock","disabled":false,"name":"iterConnection","displayName":"Variable - iterConnection","comment":"","childId":"A7D26CAE-F739-496D-876E-CD6449AE5AF6","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":240,"y":660,"variableGuid":"01319518-C1A3-491F-A4B3-EB9FC0DBF22E","operations":[{"id":"empty","key":"C22DF790-11D0-4894-ACF1-8C8C84C9F7BA","name":"Empty { variable }","value":null},{"id":"set_key_value","key":"652A5032-49ED-4B99-9FB2-34B928BAB9DD","name":"Set key/values of { variable }","value":[{"key":"connectionId","value":"{$.listDataConnections.item.id}"},{"key":"datasourceId","value":"{$.listDataConnections.item.datasourceID}"},{"key":"connectionDefinition","value":"{$.listDataConnections.item}"},{"key":"userId","value":"{ $.listDataConnections.item.user }"},{"key":"user","value":"{ $.getUser }"},{"key":"spaceId","value":"{ $.listDataConnections.item.space }"},{"key":"space","value":"{ $.getSpace }"}]}]},{"id":"A7D26CAE-F739-496D-876E-CD6449AE5AF6","type":"VariableBlock","disabled":false,"name":"connections","displayName":"Variable - connections","comment":"","childId":"56F204C1-98B4-4C5B-8409-90351CFD15F6","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":250,"y":240,"variableGuid":"AF111FE3-BF00-4A6C-B44D-36A779BE9E97","operations":[{"id":"add_item","key":"76DD31C0-CCFE-4E8A-A30B-C475425097AD","name":"Add item to { variable }","value":"{$.iterConnection}"}]},{"id":"56F204C1-98B4-4C5B-8409-90351CFD15F6","type":"IfElseBlock","disabled":false,"name":"condition2","displayName":"Condition 2","comment":"If the user has an email, send them a message to say their connection has been deleted","childId":"3BF2EB07-A4BC-419E-BA9C-AF9B2C4322CB","inputs":[{"id":"conditions","value":{"mode":"all","conditions":[{"input1":"{$.getUser.email}","operator":"notEmpty","input2":null}]},"type":"custom","structure":{}}],"settings":[],"collapsed":[{"name":"both","isCollapsed":false},{"name":"yes","isCollapsed":false},{"name":"no","isCollapsed":false}],"x":-439,"y":539,"childTrueId":"3B0A7D22-751F-49EE-8545-BF8E6D964BDA","childFalseId":null},{"id":"3BF2EB07-A4BC-419E-BA9C-AF9B2C4322CB","type":"EndpointBlock","disabled":false,"name":"rawAPIRequest","displayName":"Qlik Cloud Services - Raw API Request","comment":"Delete the data connection","childId":null,"inputs":[{"id":"4add8960-2078-11ec-be2c-7fc55d771fe6","value":"data-connections/{ $.listDataConnections.item.id }","type":"string","structure":{}},{"id":"3b992a40-2072-11ec-9f0e-ed01586a7e1b","value":"3ba2a970-2072-11ec-be02-2dd5c73abb12","type":"select","displayValue":"DELETE","structure":{}},{"id":"3b8b9090-2072-11ec-8c77-5195fbb0ca65","value":null,"type":"object","mode":"keyValue","structure":{}},{"id":"993585d0-2839-11ec-b431-df4deed6c1ae","value":null,"type":"object","mode":"keyValue","structure":{}}],"settings":[{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":827,"y":894,"datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"3b75dd80-2072-11ec-9043-3b2aff6123af","endpoint_role":"get"},{"id":"3B0A7D22-751F-49EE-8545-BF8E6D964BDA","type":"EndpointBlock","disabled":false,"name":"SendMail","displayName":"Mail - Send Mail","comment":"","childId":null,"inputs":[{"id":"442845a0-cd00-11eb-9aa5-b966a68573b7","value":"{$.getUser.email}","type":"string","structure":{}},{"id":"543f08c0-cd00-11eb-b9c6-af8e23cc2439","value":"admin@example.com","type":"string","structure":{}},{"id":"5cbdb1d0-cd00-11eb-8afd-ddd4ecc002ac","value":null,"type":"string","structure":{}},{"id":"72cad1e0-cd00-11eb-aa1b-3f42c1d22e38","value":"Your data connection has been deleted","type":"string","structure":{}},{"id":"79af8c50-cd24-11eb-a019-dfdc9a7f7317","value":"8ca918e0-cd24-11eb-a713-779c5b59e5f7","type":"select","displayValue":"text","structure":{}},{"id":"7d225d00-cd00-11eb-8493-055760e8b45a","value":"Hi {$.getUser.name},\n\nThe data connection [{ $.listDataConnections.item.qName }] that you created in space [{ if: {$.getSpace.name} empty , 'personal or deleted', $.getSpace.name }] has been deleted from Qlik Cloud tenant [{ $.getCurrentTenantInfo.name }] as the connector type [{ $.listDataConnections.item.datasourceID }] is not in the approved list.\n\nThanks,\nQlik Admin","type":"longtext","structure":{}},{"id":"bb841f10-3341-11ec-b9a3-9d6de0bb7866","value":null,"type":"custom","structure":{}}],"settings":[{"id":"datasource","value":"663610e0-d94e-11ed-8000-1314af971326","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-404,"y":332,"datasourcetype_guid":"05407a80-ccfd-11eb-b098-7140f6ac27f4","endpoint_guid":"84a79bf0-ccff-11eb-a508-7d415a725ea7","endpoint_role":"create"}],"variables":[{"guid":"AF111FE3-BF00-4A6C-B44D-36A779BE9E97","name":"connections","type":"list"},{"guid":"01319518-C1A3-491F-A4B3-EB9FC0DBF22E","name":"iterConnection","type":"object"},{"guid":"B5594ED9-5EEC-4499-91F9-8E7A7D5D093F","name":"approvedSources","type":"list"}]}
    ```
</details>
