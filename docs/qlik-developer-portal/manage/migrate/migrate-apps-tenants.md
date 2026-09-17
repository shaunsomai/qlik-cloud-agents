---
source: https://qlik.dev/manage/migrate/migrate-apps-tenants/
last_updated: 2025-12-12T09:07:11Z
---

# Migrate apps between Qlik Cloud tenants

## Overview

In this tutorial, you are going to learn how to migrate Qlik Sense applications
from one tenant to another, including all private content.

You will use qlik-cli in PowerShell to export the apps metadata (which users own which
sheets, stories, etc) and Qlik Automate to import these
back into a different tenant, and reassign ownership.

The tutorial will cover the migration of all objects, and remap ownership of:

- Sheets
- Bookmarks
- Stories

Other object types such as snapshots and ODAG links are not covered in this tutorial. Apps
in managed spaces need additional consideration to maintain user objects and app lineage
correctly. Apps in personal spaces can be imported to the personal space of the OAuth
user used for the automation, and reassigned to the original owner.

This tutorial is not exhaustive, and does not migrate other resources such as
spaces, automations, data alerts, subscriptions, notes, etc. Qlik offers solutions via
[Qlik Professional Services](https://www.qlik.com/us/services/qlik-consulting)
for complete tenant to tenant migrations.

The terms **source tenant** and **target tenant** are used throughout this tutorial.
They refer to the tenant that you are migrating content from (**source tenant**),
and the tenant that you are migrating content to (**target tenant**).

## Understanding ownership

Ownership of objects is a topic relevant to user-created content and is important for governance, access control, and
app lifecycle management.
You may need to update object ownership in several scenarios:

- Leavers and joiners within your organization
- Identity provider reconfigurations
- Mergers and acquisitions
- [Migrations between tenants and from Qlik Sense Enterprise client-managed to Qlik Cloud](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate/)

Any object that is not part of the base (approved) part of an app can have an owner different from the parent app.
In the engine, a `userId` and optionally a `userSubject` are stored to identify this owner.

Use `userId` for Qlik Cloud app, as it is the attribute Qlik supports for cloud deployments.
The `userSubject` field is a legacy field that Qlik is phasing out for Qlik Cloud and is not updated in all cases.
It is primarily used for client-managed to cloud migrations and is not recommended for apps already in Qlik Cloud.

When updates to object ownership are made, they propagate with eventual consistency.
Users connected to compute instances that opened an app before ownership updates may not receive the new ownership
information immediately.
Updates take effect after user sessions end and the app is cleared from memory, or when triggered by events such as
publishing the app.

## Prerequisites

To complete this tutorial, ensure that the following prerequisites have been met:

- [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) version 2.25.0 or higher
- An [OAuth qlik-cli context](https://qlik.dev/toolkits/qlik-cli/qlik-cli-contexts/#connecting-to-qlik-cloud-with-oauth) for
  your **source tenant**, assigned the `admin_classic` and `admin.apps` scopes, named
  `source-tenant`.
- A connection in [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/qpo-configure-connector) for
  your **source tenant**, assigned the `admin_classic` and `admin.apps` scopes, named
  `source-tenant`. You can use the same credentials as for the qlik-cli context.
- A connection in [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/qpo-configure-connector) for
  your **target tenant**, assigned the `admin_classic` and `admin.apps` scopes, named
  `target-tenant`.
- All users who own content exist in the target tenant,
  with the same user subject as in the source tenant.
- All spaces and space assignments have been copied to the target tenant.
- Data connections have been recreated in the target tenant in the same
  spaces and with the same names as in the source tenant.

## Step 1: Export app metadata from source tenant

The *Qlik Platform Operations* connector in *Qlik Automate* cannot
interact with the engine APIs to retrieve information about object
ownership. This means you must retrieve this information using another tool. This
section explains how to do this with [qlik-cli](https://qlik.dev/toolkits/qlik-cli/), and uploads
it to the **source tenant** for consumption by Automate.

> **Note:** The qlik-cli example in this section is formatted for PowerShell 5 on the Microsoft Windows operating system.
> Some reformatting may be required for other operating systems, PowerShell versions, or command lines.

![a screenshot of the OAuth configuration for the source
tenant with admin.apps and admin\_classic scopes assigned.](https://qlik.dev/_astro/oauthScopes.U1B8Jphn.png)

Ensure you have a context named `source-tenant` in qlik-cli for your source tenant with
the `admin_classic` and `admin.apps` scopes assigned in the management console.
If the context name is different, update it in the code below. Your OAuth client
name in the management console will reflect the user name for the user in the tenant.

This PowerShell code will iterate over all apps in shared spaces on the tenant, open
them without data, and in the same session (with `--headers="X-Qlik-Session=recycle"`)
to improve performance.

<details>
  <summary>
    PowerShell snippet: create a local CSV and JSON of object ownership, and upload to source tenant
  </summary>

  ```powershell
  # Set context to source tenant
  # Returns up to 1000 apps, increase this value as required
  $context = qlik context use source-tenant
  $sourceAppList = (qlik item ls --resourceType "app" --limit 1000 | ConvertFrom-Json)
  $sourceAppListCount = $sourceAppList.Length;
  $sourceAppListIter = 0;
  $objects = @()

  # Create a hash table to cache user lookups
  $userCache = @{}

  # Retrieve metadata for each app
  foreach ($sourceApp in $sourceAppList) {
      $sourceAppListIter += 1;
      
      Write-Host "Working on app $($sourceAppListIter)/$($sourceAppListCount): [$($sourceApp.name)]"

      # Get content list from app
      $listObjects = (qlik app object ls --app $($sourceApp.resourceId) --no-data --headers="X-Qlik-Session=recycle" --json | ConvertFrom-Json)

      # Iterate over these and add to list
      foreach ($listObject in $listObjects) {
          if ($listObject.qType -in ('sheet','story')) {
              $objectLayout = (qlik app object layout $($listObject.qId) --app $($sourceApp.resourceId) --no-data --headers="X-Qlik-Session=recycle" --json | ConvertFrom-Json)
              
              # Look up the user subject from the ownerId
              $ownerId = $objectLayout.qMeta.ownerId
              if (-not $userCache.ContainsKey($ownerId)) {
                  $user = (qlik user get $ownerId --json | ConvertFrom-Json)
                  $userCache[$ownerId] = $user.subject
              }
              
              $object = [pscustomobject]@{
                  appId = $($sourceApp.resourceId)
                  objectId = $($objectLayout.qInfo.qId)
                  objectType = $($objectLayout.qInfo.qType)
                  objectName = $($objectLayout.qMeta.title)
                  objectOwnerId = $ownerId
                  objectOwnerSubject = $userCache[$ownerId]
              }
              
              $objects += $object
          }
      }

      # Repeat for bookmarks
      $listObjects = (qlik app bookmark ls --app $($sourceApp.resourceId) --no-data --headers="X-Qlik-Session=recycle" --json | ConvertFrom-Json)

      # Iterate over these and add to list
      foreach ($listObject in $listObjects) {
          $objectLayout = (qlik app bookmark layout $($listObject.qId) --app $($sourceApp.resourceId) --no-data --headers="X-Qlik-Session=recycle" --json | ConvertFrom-Json)
          
          # Look up the user subject from the ownerId
          $ownerId = $objectLayout.qMeta.ownerId
          if (-not $userCache.ContainsKey($ownerId)) {
              $user = (qlik user get $ownerId --json | ConvertFrom-Json)
              $userCache[$ownerId] = $user.subject
          }
          
          $object = [pscustomobject]@{
              appId = $($sourceApp.resourceId)
              objectId = $($objectLayout.qInfo.qId)
              objectType = $($objectLayout.qInfo.qType)
              objectName = $($objectLayout.qMeta.title)
              objectOwnerId = $ownerId
              objectOwnerSubject = $userCache[$ownerId]
          }
              
          $objects += $object

      }

  }

  # Store a copy of this to CSV
  $objects | Export-Csv -Path .\sourceObjects.csv -NoTypeInformation

  # Store a copy of this to JSON
  $objects | ConvertTo-Json | Set-Content -Path .\sourceObjects.json

  # Upload to the tenant for Automate
  $upload = (qlik raw post v1/temp-contents --body-file ".\sourceObjects.json" --query "filename=temp.json,ttl=259200" --verbose --raw )
  ```
</details>

This will output two files, a CSV for validation on your computer, and a JSON file
for Automate to consume. The last step in the script uploads this
JSON file to the tenant, copy the ID from the location header:

```bash
...
< Cache-Control: no-store
< Connection: keep-alive
< Content-Length: 0
< Date: Fri, 19 Jul 2024 17:31:57 GMT
< Location: /v1/temp-contents/669aa30d65f8f5ff38d1522e
< Pragma: no-cache
< Set-Cookie: **omitted**
< Strict-Transport-Security: max-age=15724800; includeSubDomains
Response time: 127ms
Status: 201 Created
Empty response body
```

From the line `< Location: /v1/temp-contents/669aa30d65f8f5ff38d1522e`, extract
just the `669aa30d65f8f5ff38d1522e`. You will need this for the automation, as it
references the data file in the tenant. As configured, this file will be deleted
from Qlik Cloud after 3 days (259200 seconds).

## Step 2: Migrate the apps and reassign ownership

The automation snippet below will export apps without data from the **source tenant**
and import them to the respective space in the **target tenant**. All spaces and
users should exist in the **target tenant** before running this automation.

The automation will:

![Blocks showing: Load the object ownership information
uploaded to the temp-contents service by the PowerShell script.](https://qlik.dev/_astro/migrateQpo1.DWdf5g9z.png)

Load the object ownership information uploaded to the temp-contents service
by the PowerShell script.

![Blocks showing: Loop over all apps in shared spaces
(see note in introduction regarding managed and personal space apps), exiting if an
app is found where no metadata was extracted by the PowerShell script, and exporting
without data otherwise.](https://qlik.dev/_astro/migrateQpo2.DFwRrdWT.png)

Loop over all apps in shared spaces (see the note in the introduction regarding managed and personal space apps).
Exit if an app has no metadata from the PowerShell script.
Otherwise, export the app without data.

![Blocks showing: Import the exported app to the target
tenant, reassigning content to the original owner (assuming they exist with the same
subject in the target tenant), and finally
reassigning ownership of the app to the original owner.](https://qlik.dev/_astro/migrateQpo3.DmvOkKk5.png)

Import the exported app to the **target tenant**, reassign content to the original owner.
The automation looks up users in the **target tenant** by their `subject` value.
This value is retrieved from the **source tenant** via the Users API.
This ensures correct ownership mapping even when user IDs differ between tenants.

> **Ownership reassignment:** **User subjects and edge cases:** If user subjects differ between tenants, or if objects or apps are owned by OAuth
> client users, add logic to your automation to reassign ownership as needed.
>
> **Eventual consistency:** Ownership changes are propagated to users with eventual consistency.
> Since no users should be accessing the apps during the migration, the changes take effect when users first access
> the migrated apps in the target tenant.
> If you need to force immediate updates for users already accessing the apps in managed spaces,
> you can add a Publish App block in your automation to republish each app after ownership changes
> are complete.

The end result of the automation will be that you have your apps in your **target
tenant**, with the correct sheets, stories, and bookmarks owned by the correct
users.

> **Note:** Qlik Sense sheets with show conditions may not be visible after importing without data.
> To make these sheets appear, owners need to enter edit mode in the Qlik Sense client.

<details>
  <summary>
    Qlik Automate snippet: export app, import app, reassign content, reassign app
  </summary>

  To use this snippet, copy the whole code string to your clipboard, right click
  on an Automate workspace, and click paste.

  Update the following blocks:

  - `Variable - sourceTenant`: set this to the URL of your source tenant
  - `Variable - targetTenant`: set this to the URL of your target tenant
  - `Export Base 64 Encoded File From Temporary Contents`: set the `ID` value to the
    ID returned from the location header from the PowerShell script.

  <Image
    src={migrateQpo4}
    alt="Example block with [TT] in the comments which
will need to be linked to the target tenant."
    style="height:600px; display: block;margin-left: auto;
margin-right: auto;"
  />

  You will need to relink connection to blocks. You can do this by selecting each block,
  going to *Connection* in the block pane, and selecting the new connection. Blocks
  with `[TT]` in the comments should be relinked to your **target tenant** connection. All
  other *Qlik Platform Operations* blocks can be relinked to your **source tenant** connection.

  ```json
  {"blocks":[{"id":"7C5058B2-DE51-4258-9952-4113999100E2","type":"StartBlock","disabled":false,"name":"Start","displayName":"Start","comment":"","childId":"92023D5F-470D-4EC0-BBEB-1FCCCBFAD71C","inputs":[{"id":"run_mode","value":"manual","type":"select","structure":{}}],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":0},{"id":"92023D5F-470D-4EC0-BBEB-1FCCCBFAD71C","type":"VariableBlock","disabled":false,"name":"sourceTenant","displayName":"Variable - sourceTenant","comment":"INPUT: Set your source tenant","childId":"07086954-A233-45B7-8AFC-A875D8465049","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-12,"y":344,"variableGuid":"F13A8D06-C8CF-435D-8858-8DB5FA6FFFF9","operations":[{"key":"313A2660-6692-4044-9217-28B4BE7D7364","id":"set_value","name":"Set value of { variable }","value":"source-tenant.eu.qlikcloud.com"}]},{"id":"07086954-A233-45B7-8AFC-A875D8465049","type":"VariableBlock","disabled":false,"name":"targetTenant","displayName":"Variable - targetTenant","comment":"INPUT: Set your target tenant","childId":"DF43324A-B4E0-4942-9564-DE28FFC79641","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":240,"variableGuid":"22DC8F03-324A-4005-8952-20A62C70E1F7","operations":[{"key":"0E1B7D39-C5DD-4EBC-A9CC-07B4B98922AF","id":"set_value","name":"Set value of { variable }","value":"target-tenant.uk.qlikcloud.com"}]},{"id":"2EC9D041-16ED-42D1-B1C7-83D37E1619BA","type":"EndpointBlock","disabled":false,"name":"listApps","displayName":"Qlik Platform Operations - List Apps","comment":"","childId":null,"inputs":[{"id":"e9b6c6e0-fc5c-11ec-a80b-6bcbe0fce3f9","value":"{$.sourceTenant}","type":"string","structure":{}},{"id":"828395d0-fc5c-11ec-84c0-7d10388a4509","value":null,"type":"string","structure":{}},{"id":"a2e67870-fc5c-11ec-8908-03acdf4e0f6b","value":null,"type":"string","structure":{}},{"id":"0861ad80-7bb3-11ed-adf0-0bf7b3e68eef","value":null,"type":"string","structure":{}},{"id":"664373d0-8481-11ee-9cc8-3382d4210b28","value":"71e9b950-8481-11ee-841f-633719df7fed","type":"select","displayValue":"shared","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"maxitemcount","value":null,"type":"string","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":1,"y":804,"loopBlockId":"FB8D3605-6C2E-4F21-A259-561ACA5CD2BC","datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"8263bab0-fc5c-11ec-8f4a-433e011739ae","endpoint_role":"list"},{"id":"0D5970EF-941B-4110-8E2D-20CB3D0E4F12","type":"SnippetBlock","disabled":false,"name":"ExportAppToBase64EncodedFile","displayName":"Qlik Platform Operations - Export App To Base 64 Encoded File","comment":"Export the app","childId":"46C65DA0-6F44-4385-ABA5-838708946C52","inputs":[{"id":"d426c290-9af1-11ed-9b71-c99af7f97e39","value":"{$.sourceTenant}","type":"string","structure":{}},{"id":"ca854070-fc5a-11ec-8017-27122a46811b","value":"{$.listApps.item.resourceId}","type":"string","structure":{}},{"id":"6251d660-ca35-11ed-be4b-a5921229ac8e","value":"true","type":"select","displayValue":"true","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":940,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"ca7c1640-fc5a-11ec-9506-815ae94ddd6e"},{"id":"46C65DA0-6F44-4385-ABA5-838708946C52","type":"EndpointBlock","disabled":false,"name":"getSpace","displayName":"Qlik Platform Operations - Get Space","comment":"Get the source space name","childId":"425E4DE2-56A1-45CF-94A7-1D76592F611B","inputs":[{"id":"bb5493b0-d2ea-11ed-8c68-af1defa1a0cb","value":"{$.sourceTenant}","type":"string","structure":{}},{"id":"bb5c2210-d2ea-11ed-b414-1dccaac5089a","value":"{$.listApps.item.spaceId}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-421,"y":252,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"bb404160-d2ea-11ed-8ebf-2bc37ad7109f","endpoint_role":"get"},{"id":"425E4DE2-56A1-45CF-94A7-1D76592F611B","type":"EndpointBlock","disabled":false,"name":"listSpaces2","displayName":"Qlik Platform Operations - List Spaces 2","comment":"[TT]","childId":"646FF3CF-FD31-4924-86CC-6F1EAB0A711F","inputs":[{"id":"7717d000-eb0e-11ec-9b55-c70a3d793cb2","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"cf8b5510-d90e-11ed-a579-cd38900fbf47","value":"name eq \"{$.getSpace.name}\"","type":"string","structure":{}},{"id":"1d91e290-d90f-11ed-80ea-9fec14e6d987","value":null,"type":"string","structure":{}},{"id":"71ea7180-d90f-11ed-a399-43da6346f683","value":null,"type":"select","structure":{}},{"id":"92cd6110-d90f-11ed-a57c-89623b3170d1","value":null,"type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"maxitemcount","value":null,"type":"string","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":-410,"y":342,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"76df5d40-eb0e-11ec-85e6-6fa92818449e","endpoint_role":"list"},{"id":"646FF3CF-FD31-4924-86CC-6F1EAB0A711F","type":"EndpointBlock","disabled":false,"name":"importAppFromBase64EncodedFile","displayName":"Qlik Platform Operations - Import App From Base 64 Encoded File","comment":"[TT]","childId":"A866362A-86DE-4375-8A73-E81667112657","inputs":[{"id":"4be04370-fc5b-11ec-8758-ddba95fb24da","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"4bce30a0-fc5b-11ec-ab0b-cb01fdfeeec0","value":"{$.ExportAppToBase64EncodedFile}","type":"string","structure":{}},{"id":"a7fab740-fc5b-11ec-9e27-8d6654541393","value":null,"type":"string","structure":{}},{"id":"cfd90fa0-fc5b-11ec-81c3-ef55794fd2e8","value":"{$.listSpaces2[0].id}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-384,"y":393,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"4bbfdf70-fc5b-11ec-b1c1-311f2248f446","endpoint_role":"create"},{"id":"33A798FB-CB1C-40A4-A244-B6FCF3B1B17E","type":"VariableBlock","disabled":false,"name":"objectMapping","displayName":"Variable - objectMapping","comment":"This is built from the upload from the associated powershell script","childId":"2EC9D041-16ED-42D1-B1C7-83D37E1619BA","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":600,"variableGuid":"9A414BCD-4B65-41D4-AA13-F9202DA8256B","operations":[{"key":"8F9448D8-0DD3-4337-B299-897093B212B8","id":"merge","name":"Merge other object into { variable }","object":"{object: '{base64decode: {$.ExportBase64EncodedFileFromTemporaryContents}}'}"}]},{"id":"A8BB0DE7-37F0-42EE-A614-80B56EEE5B9E","type":"EndpointBlock","disabled":false,"name":"ChangeAppObjectOwner","displayName":"Qlik Platform Operations - Change App Object Owner","comment":"[TT]","childId":null,"inputs":[{"id":"e1aa4820-f3eb-11ed-9fa8-bf0de2f3ebc5","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"e1a3d820-f3eb-11ed-bb21-232d10fe8379","value":"{$.importAppFromBase64EncodedFile.attributes.id}","type":"string","structure":{}},{"id":"2b043300-f3ec-11ed-b09d-2d33d2348f2e","value":"{$.filterList.item.objectId}","type":"string","structure":{}},{"id":"e1bdb7e0-f3eb-11ed-a00f-7bc248e7454d","value":"{ $.listUsers3[0].id }","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":709,"y":1309,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"e18f71e0-f3eb-11ed-b8c5-1de6942838dd","endpoint_role":"update"},{"id":"A866362A-86DE-4375-8A73-E81667112657","type":"FilterListBlock","disabled":false,"name":"filterList","displayName":"Filter List","comment":"","childId":"E0EAFBAF-4454-466D-B1AD-F0656CAEAE4C","inputs":[{"id":"list","value":"{$.objectMapping}","type":"string","structure":{}},{"id":"conditions","value":{"mode":"all","conditions":[{"input1":"appId","operator":"=","input2":"{$.listApps.item.resourceId}"}]},"type":"custom","structure":{}}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-410,"y":824,"loopBlockId":"FB65129F-EE0D-4C69-9C0B-9D54502B4A9F"},{"id":"DF43324A-B4E0-4942-9564-DE28FFC79641","type":"EndpointBlock","disabled":false,"name":"ExportBase64EncodedFileFromTemporaryContents","displayName":"Qlik Platform Operations - Export Base 64 Encoded File From Temporary Contents","comment":"INPUT: Set the ID of the file uploaded by the powershell script (found in the Location header)","childId":"33A798FB-CB1C-40A4-A244-B6FCF3B1B17E","inputs":[{"id":"ee0ab290-d6fb-11ee-a9ec-c3d3ad6bbd0c","value":"{$.sourceTenant}","type":"string","structure":{}},{"id":"ee00a630-d6fb-11ee-bca6-d1e60f82da56","value":"669a7b8627a96496bba7facf","type":"string","structure":{}},{"id":"ee16de40-d6fb-11ee-9bae-0143b9238833","value":null,"type":"string","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-372,"y":88,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"edefb080-d6fb-11ee-be7b-5bcb8756357f","endpoint_role":"get"},{"id":"323FCD3C-33FC-4AA8-98BC-D6666CE811B2","type":"EndpointBlock","disabled":false,"name":"listUsers3","displayName":"Qlik Platform Operations - List Users 3","comment":"[TT] Look up user by subject","childId":"A8BB0DE7-37F0-42EE-A614-80B56EEE5B9E","inputs":[{"id":"447b9eb0-7634-11ed-a9df-a788128e422e","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"eb56ff20-9ca8-11ed-82cb-752b6b37b1a7","value":"subject eq \"{regexreplace: { $.getUser.subject }, '\\\\', '\\\\\\\\'}\"","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"maxitemcount","value":"","type":"string","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":240,"y":1400,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"445157c0-7634-11ed-9b40-9720b0f37135","endpoint_role":"list"},{"id":"FB65129F-EE0D-4C69-9C0B-9D54502B4A9F","type":"EndpointBlock","disabled":false,"name":"getUser","displayName":"Qlik Platform Operations - Get User","comment":"","childId":"323FCD3C-33FC-4AA8-98BC-D6666CE811B2","inputs":[{"id":"dfb7c880-9caa-11ed-bae1-3325829d9725","value":"{ $.sourceTenant }","type":"string","structure":{}},{"id":"dfc724b0-9caa-11ed-8d7a-a5bc1a965960","value":"{ $.filterList.item.objectOwnerId }","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":240,"y":1280,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"df9f1570-9caa-11ed-ac68-8ffd59764433","endpoint_role":"get"},{"id":"A2E3696A-3F9D-45A3-BF9E-89C4974920E6","type":"EndpointBlock","disabled":false,"name":"changeAppOwner","displayName":"Qlik Platform Operations - Change App Owner","comment":"[TT]","childId":null,"inputs":[{"id":"88793e70-e8e2-11ed-bf7e-9b54dd716b7d","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"88752c10-e8e2-11ed-bc8b-19bdb1fee672","value":"{$.importAppFromBase64EncodedFile.attributes.id}","type":"string","structure":{}},{"id":"c7000120-e8e2-11ed-9922-71d6ab1036e6","value":"{ $.listUsers4[0].id }","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-368,"y":711,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"88691a50-e8e2-11ed-8746-6f07a78cade9","endpoint_role":"update"},{"id":"C0859705-5F77-4E90-80A6-55BD00C8A2EA","type":"EndpointBlock","disabled":false,"name":"listUsers4","displayName":"Qlik Platform Operations - List Users 4","comment":"[TT] Look up user by subject","childId":"A2E3696A-3F9D-45A3-BF9E-89C4974920E6","inputs":[{"id":"447b9eb0-7634-11ed-a9df-a788128e422e","value":"{$.targetTenant}","type":"string","structure":{}},{"id":"eb56ff20-9ca8-11ed-82cb-752b6b37b1a7","value":"subject eq \"{regexreplace: { $.getUser2.subject }, '\\\\', '\\\\\\\\'}\"","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"0beb6795-43b3-43e8-b381-f7017d0573cb","type":"select","structure":{}},{"id":"maxitemcount","value":"","type":"string","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":490,"y":1400,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"445157c0-7634-11ed-9b40-9720b0f37135","endpoint_role":"list"},{"id":"E0EAFBAF-4454-466D-B1AD-F0656CAEAE4C","type":"EndpointBlock","disabled":false,"name":"getUser2","displayName":"Qlik Platform Operations - Get User 2","comment":"","childId":"C0859705-5F77-4E90-80A6-55BD00C8A2EA","inputs":[{"id":"dfb7c880-9caa-11ed-bae1-3325829d9725","value":"{ $.sourceTenant }","type":"string","structure":{}},{"id":"dfc724b0-9caa-11ed-8d7a-a5bc1a965960","value":"{$.listApps.item.ownerId}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":"9d2125ab-35b4-4bd1-b733-c8b8f7f7cab3","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":490,"y":1280,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"df9f1570-9caa-11ed-ac68-8ffd59764433","endpoint_role":"get"},{"id":"FB8D3605-6C2E-4F21-A259-561ACA5CD2BC","type":"IfElseBlock","disabled":false,"name":"condition","displayName":"Condition","comment":"If this app doesn't have at least one object mapping, error","childId":null,"inputs":[{"id":"conditions","value":{"mode":"all","conditions":[{"input1":"{$.objectMapping[*].appId}","operator":"inList","input2":"{ $.listApps.item.resourceId }"}]},"type":"custom","structure":{}}],"settings":[],"collapsed":[{"name":"both","isCollapsed":false},{"name":"yes","isCollapsed":false},{"name":"no","isCollapsed":false}],"x":-407,"y":524,"childTrueId":"0D5970EF-941B-4110-8E2D-20CB3D0E4F12","childFalseId":"38544A6D-42ED-44A3-9634-503AEEE8D0CC"},{"id":"38544A6D-42ED-44A3-9634-503AEEE8D0CC","type":"ErrorBlock","disabled":false,"name":"error","displayName":"Error","comment":"","childId":null,"inputs":[{"id":"message","value":"Missing mapping data for [{ $.listApps.item.name }]","type":"string","structure":{}},{"id":"action","value":"stop","type":"select","structure":{}}],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-440,"y":1413}],"variables":[{"guid":"F13A8D06-C8CF-435D-8858-8DB5FA6FFFF9","name":"sourceTenant","type":"string"},{"guid":"22DC8F03-324A-4005-8952-20A62C70E1F7","name":"targetTenant","type":"string"},{"guid":"9A414BCD-4B65-41D4-AA13-F9202DA8256B","name":"objectMapping","type":"object"}]}
  ```
</details>
