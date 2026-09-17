---
source: https://qlik.dev/manage/data-files/update-datafiles/
last_updated: 2026-04-20T13:34:03+01:00
---

# Update data files in Qlik Cloud

## Overview

In this tutorial, you are going to learn how to update data file contents, spaces,
and ownership.

## Requirements

- Review the prerequisites in the [create data files](https://qlik.dev/manage/data-files/create-datafiles) tutorial.

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
| `<SPACE_ID>`            | The ID of the shared space that the data file resides in.                                                                                       |
| `<NEW_SPACE_ID>`        | The ID of the shared space that you wish to move the data file to.                                                                              |
| `<DATA_FILE_ID>`        | The ID for the data file.                                                                                                                       |
| `<USER_ID>`             | The ID for the user who you wish to transfer ownership of the data file to.                                                                     |

## Update the data file

To update a file in an existing data file asset, use the data file ID and pass
the new file. Optionally, you can also update the data file metadata using these
endpoints and calls.

> **Note:** When updating some data file metadata, such as the filename, the corresponding data set is not automatically updated.
> If your users use the Qlik Cloud hub to search for data, ensure you also update the data set.

```bash
curl -L -X PUT "https://<HOSTNAME>/api/v1/data-files/<DATA_FILE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-F "file=@\"<PATH_TO_DATA_FILE>\""
```

This multi-step process supports files up to your entitled limits in Qlik Cloud.
Instead of uploading directly to the `data-files` API, you upload first to
`temp-contents` using a chunked upload, and then import this file to `data-files`.

If you are using Windows, you should update the line continuation character to `^`.

```bash
# Upload data file to temp-contents, and capture temp-contents file id
TEMP_CONT_ID=$(curl -L "https://<HOSTNAME>/api/v1/temp-contents?filename=<DATA_FILE_NAME>" -v \
-X POST \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/octet-stream" \
-H "Transfer-Encoding: chunked" \
-T "<PATH_TO_DATA_FILE>" 2>&1 \
| grep -F "< location:" | awk '{print $3}' | tr -d '[:space:]' | awk -F / '{print $NF}')

# Update data-file from temp-contents
curl -L -X PUT "https://<HOSTNAME>/api/v1/data-files/<DATA_FILE_ID>" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-F "json="{"tempContentFileId":"$TEMP_CONT_ID"}""
```

If your file is larger than 500 MB in size, add `--resumable` to have qlik-cli
automatically handle the upload of this file via `temp-contents`.

```bash
qlik data-file update <DATA_FILE_ID> --file "<PATH_TO_DATA_FILE>"
```

If using qlik-cli, the response will look similar to:

<details>
<summary>Example qlik-cli response</summary>

```json
{
    "id": "<DATA_FILE_ID>",
    "name": "<DATA_FILE_NAME>",
    "size": 24743,
    "createdDate": "2023-03-23T11:26:20.631Z",
    "modifiedDate": "2023-04-28T15:41:19.8263046Z",
    "ownerId": "637390ec6541614d3a88d6c1"
}
```

</details>

A `201` status code indicates the data file was updated successfully.

## Move a data file to a different space

To move a data file to a different space, you need to know the file ID and the
ID of the space you want to move the data file to.

```bash
curl -L "https://<HOSTNAME>/api/v1/data-files/<DATA_FILE_ID>/actions/change-space" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{\"spaceId\": \"<NEW_SPACE_ID>\"}"
```

```bash
qlik data-file change-space <DATA_FILE_ID> --spaceId <NEW_SPACE_ID>
```

A `204` response confirms that the ownership of the data file has been updated
successfully.

## Move all data files in a space to a different space

To move all data files to a different space, you need to know the space ID of the
space the files currently reside in, and the space ID of the space to move them
to.

```powershell
# qlik-cli/powershell
# Set the space ID of the space containing the data files to move
$spaceId = '<SPACE_ID>';
# Set the space ID of the space you wish to move the data files to
$targetSpaceId = '<NEW_SPACE_ID>';

$dataConnection = qlik data-file connection ls --spaceId $spaceId | ConvertFrom-Json
$dataFiles = qlik data-file ls --connectionId $dataConnection.id --limit 1000 | ConvertFrom-Json

$dataFileCount = $dataFiles.Length;
$dataFileIter = 0;

Write-Host "$dataFileCount data files found."

foreach ($dataFile in $dataFiles) {
    $dataFileIter += 1;
    qlik data-file change-space $dataFile.id --spaceId $targetSpaceId;
    Write-Host "Moved data file $dataFileIter of $dataFileCount.";
}

```

This snippet can be pasted into a Qlik Automate workspace.

```json
{"blocks":[{"id":"D535528C-1A75-492E-949B-059B6B64B2B3","type":"VariableBlock","disabled":false,"name":"sourceSpaceName","displayName":"Variable - sourceSpaceName","comment":"Set the name of the source space","childId":"E2CB80A2-F3F6-4A99-918B-CD06741B8F47","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":477,"y":110,"variableGuid":"14B10A3B-89C1-4B2D-9E1A-5096D5382162","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"source space name"}]},{"id":"E2CB80A2-F3F6-4A99-918B-CD06741B8F47","type":"VariableBlock","disabled":false,"name":"targetSpaceName","displayName":"Variable - targetSpaceName","comment":"Set the name of the target space","childId":"9485F1B8-CAEC-48AB-B120-FCD9510C3095","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":240,"variableGuid":"E47E907C-D900-42B5-9704-41B5D8DF475F","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"target space name"}]},{"id":"9485F1B8-CAEC-48AB-B120-FCD9510C3095","type":"VariableBlock","disabled":false,"name":"tenantHostname","displayName":"Variable - tenantHostname","comment":"Set the tenant hostname, e.g. `mytenant.us.qlikcloud.com`","childId":"21CD9BC3-EB81-4097-8824-1A21CE1AEBEE","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":250,"y":240,"variableGuid":"AE3791C9-D010-4598-8F36-CF21E80554A7","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"orchestration.eu.qlikcloud.com"}]},{"id":"21CD9BC3-EB81-4097-8824-1A21CE1AEBEE","type":"SnippetBlock","disabled":false,"name":"GetTenantNameAndRegion","displayName":"Qlik Platform Operations - Get Tenant Name And Region","comment":"","childId":"B6E365CE-F6C4-496D-B128-0B9A69733BCC","inputs":[{"id":"575d1740-b1e2-11ed-958a-598edfec33b8","value":"{$.tenantHostname}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-378,"y":163,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"},{"id":"B6E365CE-F6C4-496D-B128-0B9A69733BCC","type":"EndpointBlock","disabled":false,"name":"listSpaces","displayName":"Qlik Platform Operations - List Spaces","comment":"Get source space id","childId":"F3E87ABF-21FE-4590-97FF-CEF91E37080D","inputs":[{"id":"7717d000-eb0e-11ec-9b55-c70a3d793cb2","value":"{$.GetTenantNameAndRegion}","type":"string","structure":[]},{"id":"cf8b5510-d90e-11ed-a579-cd38900fbf47","value":"name eq \"{$.sourceSpaceName}\"","type":"string","structure":[]},{"id":"1d91e290-d90f-11ed-80ea-9fec14e6d987","value":null,"type":"string","structure":[]},{"id":"71ea7180-d90f-11ed-a399-43da6346f683","value":null,"type":"string","structure":[]},{"id":"92cd6110-d90f-11ed-a57c-89623b3170d1","value":null,"type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"maxitemcount","value":"","type":"string","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":0,"y":600,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"76df5d40-eb0e-11ec-85e6-6fa92818449e","endpoint_role":"list"},{"id":"F3E87ABF-21FE-4590-97FF-CEF91E37080D","type":"EndpointBlock","disabled":false,"name":"listSpaces2","displayName":"Qlik Platform Operations - List Spaces 2","comment":"Get target space id","childId":"8F7D7918-8FC7-43E6-B3E1-7796810A85FB","inputs":[{"id":"7717d000-eb0e-11ec-9b55-c70a3d793cb2","value":"{$.GetTenantNameAndRegion}","type":"string","structure":[]},{"id":"cf8b5510-d90e-11ed-a579-cd38900fbf47","value":"name eq \"{$.targetSpaceName}\"","type":"string","structure":[]},{"id":"1d91e290-d90f-11ed-80ea-9fec14e6d987","value":null,"type":"string","structure":[]},{"id":"71ea7180-d90f-11ed-a399-43da6346f683","value":null,"type":"string","structure":[]},{"id":"92cd6110-d90f-11ed-a57c-89623b3170d1","value":null,"type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"maxitemcount","value":"","type":"string","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":250,"y":600,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"76df5d40-eb0e-11ec-85e6-6fa92818449e","endpoint_role":"list"},{"id":"8F7D7918-8FC7-43E6-B3E1-7796810A85FB","type":"SnippetBlock","disabled":false,"name":"ListDataFilesFromSpace","displayName":"Qlik Platform Operations - List Data Files From Space","comment":"","childId":"A1A79246-0527-48A9-B078-6250A46E5A57","inputs":[{"id":"d8e58e20-fa31-11ed-b2ac-0fffc605aad3","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"d8e63580-fa31-11ed-af74-112f69c5deee","value":"{$.listSpaces[0].id}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":-360,"y":656.40673828125,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"f8db6b60-fa26-11ed-b985-a3ee665e0cb9"},{"id":"A1A79246-0527-48A9-B078-6250A46E5A57","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"","childId":"0ABB775E-009D-4802-A698-8CD87D0403D5","inputs":[{"id":"input","value":"Moving {count: {$.ListDataFilesFromSpace}} data files from [{$.sourceSpaceName}/ {$.listSpaces[0].id}] to ({$.targetSpaceName}/ {$.listSpaces2[0].id}).","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":960},{"id":"0ABB775E-009D-4802-A698-8CD87D0403D5","type":"VariableBlock","disabled":false,"name":"fileCount","displayName":"Variable - fileCount","comment":"","childId":"CD1F19AA-B91E-452B-93FC-FF333407F8BF","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1200,"variableGuid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","operations":[{"id":"set_value","key":"262E2EC6-DD62-4C17-BEE2-944CEED1ED86","name":"Set value of { variable }","value":"0"}]},{"id":"CD1F19AA-B91E-452B-93FC-FF333407F8BF","type":"ForEachBlock","disabled":false,"name":"loop","displayName":"Loop over Qlik Platform Operations - List Data Files From Space - Loop","comment":"Iterate over data files","childId":"71C9029E-A638-4FEF-9FAF-2D93512A3462","inputs":[{"id":"input","value":"{ $.ListDataFilesFromSpace }","type":"string","structure":{}}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-411,"y":1005.6025390625,"loopBlockId":"C18D04E6-107A-42B3-9A2A-76AF2BF17EC2"},{"id":"71C9029E-A638-4FEF-9FAF-2D93512A3462","type":"VariableBlock","disabled":false,"name":"message","displayName":"Variable - message","comment":"","childId":"B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":370,"y":1420,"variableGuid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","operations":[{"key":"00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8","id":"set_value","name":"Set value of { variable }","value":"Moved {count: {$.ListDataFilesFromSpace}} data files from [{$.sourceSpaceName}/ {$.listSpaces[0].id}] to ({$.targetSpaceName}/ {$.listSpaces2[0].id})."}]},{"id":"B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE","type":"ShowBlock","disabled":false,"name":"output3","displayName":"Output 3","comment":"","childId":"0A5A4664-638D-4226-9184-343D9E973627","inputs":[{"id":"input","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":2100},{"id":"0A5A4664-638D-4226-9184-343D9E973627","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle2","displayName":"Update Run Title 2","comment":"","childId":null,"inputs":[{"id":"title","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":370,"y":1540},{"id":"C18D04E6-107A-42B3-9A2A-76AF2BF17EC2","type":"VariableBlock","disabled":false,"name":"fileCount","displayName":"Variable - fileCount","comment":"","childId":"AF8CF1D7-6399-45A7-8E88-D048C2A1132E","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1460,"variableGuid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","operations":[{"id":"add","key":"A0D439AD-2311-4084-B745-1B83BD193F20","name":"Add to { variable }","value":"1"}]},{"id":"AF8CF1D7-6399-45A7-8E88-D048C2A1132E","type":"VariableBlock","disabled":false,"name":"message","displayName":"Variable - message","comment":"","childId":"A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1420,"variableGuid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","operations":[{"key":"00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8","id":"set_value","name":"Set value of { variable }","value":"> Moving file {$.fileCount}/{count: { $.ListDataFilesFromSpace }} ({ $.loop.item.name })"}]},{"id":"A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle","displayName":"Update Run Title","comment":"","childId":"0E220820-B4E0-46B5-9C9A-D7A9CD2140AE","inputs":[{"id":"title","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1540},{"id":"0E220820-B4E0-46B5-9C9A-D7A9CD2140AE","type":"ShowBlock","disabled":false,"name":"output2","displayName":"Output 2","comment":"","childId":"EF353E6F-1816-49C7-BC01-1C444D8F7C54","inputs":[{"id":"input","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1780},{"id":"EF353E6F-1816-49C7-BC01-1C444D8F7C54","type":"EndpointBlock","disabled":false,"name":"ChangeDataFileSpace","displayName":"Qlik Platform Operations - Change Data File Space","comment":"","childId":null,"inputs":[{"id":"b1f16520-f960-11ed-9f21-71df00e40f5e","value":"{ $.GetTenantNameAndRegion }","type":"string","structure":{}},{"id":"b1f8e9d0-f960-11ed-a8cf-393a6fc5dacb","value":"{ $.loop.item.id }","type":"string","structure":{}},{"id":"e33066f0-f960-11ed-9b1c-2747929eec1d","value":"{ $.listSpaces2[0].id }","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-372,"y":1436.67626953125,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"b1dcf780-f960-11ed-9260-09742bae58c8","endpoint_role":"create"}],"variables":[{"guid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","name":"message","type":"string"},{"guid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","name":"fileCount","type":"number"},{"guid":"AE3791C9-D010-4598-8F36-CF21E80554A7","name":"tenantHostname","type":"string"},{"guid":"E47E907C-D900-42B5-9704-41B5D8DF475F","name":"targetSpaceName","type":"string"},{"guid":"14B10A3B-89C1-4B2D-9E1A-5096D5382162","name":"sourceSpaceName","type":"string"}]}
```

A `204` response on each update action confirms that each data file has been updated
successfully.

## Change the owner of a data file

To change the owner of the data file, you need to know the file ID and the ID
of the user who will own the file.

```bash
curl -L "https://<HOSTNAME>/api/v1/data-files/<DATA_FILE_ID>/actions/change-owner" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{\"ownerId\": \"<USER_ID>\"}"
```

```bash
qlik data-file change-owner <DATA_FILE_ID> --ownerId <USER_ID>
```

A `204` response confirms that the owner of the data file was successfully updated.

## Change the owner of all data files in a space

To change the owner of all data files in a space, you need to know the space ID
and the ID of the user who will own these files.

```powershell
# qlik-cli/powershell
# Set the space ID of the space containing the data files to change ownership of
$spaceId = '<SPACE_ID>';
# Set the user ID of the new owner for the data files
$ownerId = '<USER_ID>';

$dataConnection = qlik data-file connection ls --spaceId $spaceId | ConvertFrom-Json
$dataFiles = qlik data-file ls --connectionId $dataConnection.id --limit 1000 | ConvertFrom-Json

$dataFileCount = $dataFiles.Length;
$dataFileIter = 0;

Write-Host "$dataFileCount data files found."

foreach ($dataFile in $dataFiles) {
    $dataFileIter += 1;
    if($dataFile.ownerId -eq $ownerId) {
        Write-Host "No action needed for data file $dataFileIter of $dataFileCount ($($dataFile.name)).";
    } else {
        qlik data-file change-owner $dataFile.id --ownerId $ownerId;
        Write-Host "Changed owner of data file $dataFileIter of $dataFileCount ($($dataFile.name)).";
    }
}
```

This snippet can be pasted into a Qlik Automate workspace.

```json
{"blocks":[{"id":"D535528C-1A75-492E-949B-059B6B64B2B3","type":"VariableBlock","disabled":false,"name":"sourceSpaceName","displayName":"Variable - sourceSpaceName","comment":"Set the name of the source space","childId":"E2CB80A2-F3F6-4A99-918B-CD06741B8F47","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":477,"y":110,"variableGuid":"14B10A3B-89C1-4B2D-9E1A-5096D5382162","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"source space name"}]},{"id":"E2CB80A2-F3F6-4A99-918B-CD06741B8F47","type":"VariableBlock","disabled":false,"name":"ownerId","displayName":"Variable - ownerId","comment":"Set the name of the target space","childId":"9485F1B8-CAEC-48AB-B120-FCD9510C3095","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":240,"variableGuid":"515AD7CE-B66D-41F6-889A-45388C6242B8","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"63999551d89a3017b5a64188"}]},{"id":"9485F1B8-CAEC-48AB-B120-FCD9510C3095","type":"VariableBlock","disabled":false,"name":"tenantHostname","displayName":"Variable - tenantHostname","comment":"Set the tenant hostname, e.g. `mytenant.us.qlikcloud.com`","childId":"21CD9BC3-EB81-4097-8824-1A21CE1AEBEE","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":250,"y":240,"variableGuid":"AE3791C9-D010-4598-8F36-CF21E80554A7","operations":[{"id":"set_value","key":"A17CE820-EB64-4CF9-97EF-634A871F06D8","name":"Set value of { variable }","value":"orchestration.eu.qlikcloud.com"}]},{"id":"21CD9BC3-EB81-4097-8824-1A21CE1AEBEE","type":"SnippetBlock","disabled":false,"name":"GetTenantNameAndRegion","displayName":"Qlik Platform Operations - Get Tenant Name And Region","comment":"","childId":"B6E365CE-F6C4-496D-B128-0B9A69733BCC","inputs":[{"id":"575d1740-b1e2-11ed-958a-598edfec33b8","value":"{$.tenantHostname}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-378,"y":163,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"},{"id":"B6E365CE-F6C4-496D-B128-0B9A69733BCC","type":"EndpointBlock","disabled":false,"name":"listSpaces","displayName":"Qlik Platform Operations - List Spaces","comment":"Get source space id","childId":"8F7D7918-8FC7-43E6-B3E1-7796810A85FB","inputs":[{"id":"7717d000-eb0e-11ec-9b55-c70a3d793cb2","value":"{$.GetTenantNameAndRegion}","type":"string","structure":[]},{"id":"cf8b5510-d90e-11ed-a579-cd38900fbf47","value":"name eq \"{$.sourceSpaceName}\"","type":"string","structure":[]},{"id":"1d91e290-d90f-11ed-80ea-9fec14e6d987","value":null,"type":"string","structure":[]},{"id":"71ea7180-d90f-11ed-a399-43da6346f683","value":null,"type":"string","structure":[]},{"id":"92cd6110-d90f-11ed-a57c-89623b3170d1","value":null,"type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"maxitemcount","value":"","type":"string","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":0,"y":600,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"76df5d40-eb0e-11ec-85e6-6fa92818449e","endpoint_role":"list"},{"id":"8F7D7918-8FC7-43E6-B3E1-7796810A85FB","type":"SnippetBlock","disabled":false,"name":"ListDataFilesFromSpace","displayName":"Qlik Platform Operations - List Data Files From Space","comment":"","childId":"7E814126-E063-47A0-995E-0F01ED947794","inputs":[{"id":"d8e58e20-fa31-11ed-b2ac-0fffc605aad3","value":"{$.GetTenantNameAndRegion}","type":"string","structure":[]},{"id":"d8e63580-fa31-11ed-af74-112f69c5deee","value":"{$.listSpaces[0].id}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":true}],"x":0,"y":840,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"f8db6b60-fa26-11ed-b985-a3ee665e0cb9"},{"id":"7E814126-E063-47A0-995E-0F01ED947794","type":"EndpointBlock","disabled":false,"name":"getUser","displayName":"Qlik Platform Operations - Get User","comment":"","childId":"A1A79246-0527-48A9-B078-6250A46E5A57","inputs":[{"id":"dfb7c880-9caa-11ed-bae1-3325829d9725","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"dfc724b0-9caa-11ed-8d7a-a5bc1a965960","value":"{$.ownerId}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"cache","value":"0","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-387,"y":403.29541015625,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"df9f1570-9caa-11ed-ac68-8ffd59764433","endpoint_role":"get"},{"id":"A1A79246-0527-48A9-B078-6250A46E5A57","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"","childId":"0ABB775E-009D-4802-A698-8CD87D0403D5","inputs":[{"id":"input","value":"Changing owner of {count: {$.ListDataFilesFromSpace}} data files in [{$.sourceSpaceName}/ {$.listSpaces[0].id}] to [{$.getUser.name} / {$.getUser.id}]","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":960},{"id":"0ABB775E-009D-4802-A698-8CD87D0403D5","type":"VariableBlock","disabled":false,"name":"fileCount","displayName":"Variable - fileCount","comment":"","childId":"CD1F19AA-B91E-452B-93FC-FF333407F8BF","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1200,"variableGuid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","operations":[{"id":"set_value","key":"262E2EC6-DD62-4C17-BEE2-944CEED1ED86","name":"Set value of { variable }","value":"0"}]},{"id":"CD1F19AA-B91E-452B-93FC-FF333407F8BF","type":"ForEachBlock","disabled":false,"name":"loop","displayName":"Loop over Qlik Platform Operations - List Data Files From Space - Loop","comment":"Iterate over data files","childId":"71C9029E-A638-4FEF-9FAF-2D93512A3462","inputs":[{"id":"input","value":"{ $.ListDataFilesFromSpace }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-411,"y":1005.6025390625,"loopBlockId":"C18D04E6-107A-42B3-9A2A-76AF2BF17EC2"},{"id":"71C9029E-A638-4FEF-9FAF-2D93512A3462","type":"VariableBlock","disabled":false,"name":"message","displayName":"Variable - message","comment":"","childId":"B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":370,"y":1420,"variableGuid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","operations":[{"id":"set_value","key":"00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8","name":"Set value of { variable }","value":"Changed owner of {count: {$.ListDataFilesFromSpace}} data files in [{$.sourceSpaceName}/ {$.listSpaces[0].id}] to [{$.getUser.name} / {$.getUser.id}]"}]},{"id":"B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE","type":"ShowBlock","disabled":false,"name":"output3","displayName":"Output 3","comment":"","childId":"0A5A4664-638D-4226-9184-343D9E973627","inputs":[{"id":"input","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":2100},{"id":"0A5A4664-638D-4226-9184-343D9E973627","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle2","displayName":"Update Run Title 2","comment":"","childId":null,"inputs":[{"id":"title","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":370,"y":1540},{"id":"C18D04E6-107A-42B3-9A2A-76AF2BF17EC2","type":"VariableBlock","disabled":false,"name":"fileCount","displayName":"Variable - fileCount","comment":"","childId":"AF8CF1D7-6399-45A7-8E88-D048C2A1132E","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1460,"variableGuid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","operations":[{"id":"add","key":"A0D439AD-2311-4084-B745-1B83BD193F20","name":"Add to { variable }","value":"1"}]},{"id":"AF8CF1D7-6399-45A7-8E88-D048C2A1132E","type":"VariableBlock","disabled":false,"name":"message","displayName":"Variable - message","comment":"","childId":"A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1420,"variableGuid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","operations":[{"id":"set_value","key":"00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8","name":"Set value of { variable }","value":"> Changing owner of {$.fileCount}/{count: { $.ListDataFilesFromSpace }} ({$.loop.item.name})"}]},{"id":"A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle","displayName":"Update Run Title","comment":"","childId":"0E220820-B4E0-46B5-9C9A-D7A9CD2140AE","inputs":[{"id":"title","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1540},{"id":"0E220820-B4E0-46B5-9C9A-D7A9CD2140AE","type":"ShowBlock","disabled":false,"name":"output2","displayName":"Output 2","comment":"","childId":"8CD025CF-4D22-4F21-9BCB-3BF027815951","inputs":[{"id":"input","value":"{ $.message }","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":1780},{"id":"8CD025CF-4D22-4F21-9BCB-3BF027815951","type":"EndpointBlock","disabled":false,"name":"ChangeDataFileOwner","displayName":"Qlik Platform Operations - Change Data File Owner","comment":"","childId":null,"inputs":[{"id":"842c17d0-f963-11ed-a721-2528ebd7c656","value":"{$.GetTenantNameAndRegion}","type":"string","structure":{}},{"id":"84339850-f963-11ed-bd9d-67b12608eb6a","value":"{$.loop.item.id}","type":"string","structure":{}},{"id":"843ee920-f963-11ed-a54a-39f55e8ed332","value":"{$.ownerId}","type":"string","structure":{}}],"settings":[{"id":"datasource","value":null,"type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-316,"y":1666.44921875,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"841b8440-f963-11ed-808d-03748ef4d7d3","endpoint_role":"create"}],"variables":[{"guid":"43473F0A-CB5C-48A2-8F49-2FC102415E9D","name":"message","type":"string"},{"guid":"CDB8E7BC-B1D2-48A5-9E24-682F890038BB","name":"fileCount","type":"number"},{"guid":"AE3791C9-D010-4598-8F36-CF21E80554A7","name":"tenantHostname","type":"string"},{"guid":"515AD7CE-B66D-41F6-889A-45388C6242B8","name":"ownerId","type":"string"},{"guid":"14B10A3B-89C1-4B2D-9E1A-5096D5382162","name":"sourceSpaceName","type":"string"}]}
```

A `204` response on each update action confirms that each data file has been updated
successfully.

## Next steps

Now that you know how to update data files, why not look at how
to [delete existing data files](https://qlik.dev/manage/data-files/delete-datafiles)?
