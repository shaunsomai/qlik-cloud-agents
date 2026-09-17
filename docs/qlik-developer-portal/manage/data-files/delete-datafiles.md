---
source: https://qlik.dev/manage/data-files/delete-datafiles/
last_updated: 2026-04-20T13:34:03+01:00
---

# Delete data files from Qlik Cloud

## Overview

In this tutorial, you are going to learn how to delete data files individually,
and in bulk.

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
| `<SPACE_ID>`            | The ID of the shared space `<SPACE_NAME>`.                                                                                                      |
| `<CONNECTION_ID>`       | The ID for the data file connection in `<SPACE_NAME>`.                                                                                          |
| `<DATA_FILE_ID>`        | The ID for the data file.                                                                                                                       |

## Delete a single data file

To delete a single data file in a space, you need to know the data file ID. You
can retrieve this using the steps documented in
the [update data files](https://qlik.dev/manage/data-files/update-datafiles) tutorial.
Once you have the data file ID, you can pass this to the delete endpoint to remove
this data file from Qlik Cloud.

```bash
curl -L -X DELETE "https://<HOSTNAME>/api/v1/data-files/<DATA_FILE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

```bash
qlik data-file rm <DATA_FILE_ID>
```

A `204` response confirms that the data file, as well as any associated datasets,
has been deleted successfully.

## Delete all data files in a space

The examples below accept `<SPACE_ID>` as input, and will remove all data files
from the space when run.

```bash
# Set the space ID
$spaceId = '<SPACE_ID>';

$dataConnection = qlik data-file connection ls --spaceId $spaceId | ConvertFrom-Json

$dataFiles = qlik data-file ls --connectionId $($dataConnection.id) | ConvertFrom-Json
Write-Host $($dataFiles.Length) 'data files found.'

while ($($dataFiles.Length) -gt 1) {

    $dataFiles = $dataFiles | ConvertTo-Json
    $deletedFiles = qlik data-file delete --delete $dataFiles.replace('"','\"')

    $dataFiles = qlik data-file ls --connectionId $($dataConnection.id) | ConvertFrom-Json
    Write-Host 'Checking for more files.'
}

echo $("All data files removed, breaking.");
break;
```

This snippet can be pasted into a Qlik Automate workspace.

```json
{
  "blocks": [
    {
      "id": "D535528C-1A75-492E-949B-059B6B64B2B3",
      "type": "VariableBlock",
      "disabled": false,
      "name": "sourceSpaceName",
      "displayName": "Variable - sourceSpaceName",
      "comment": "Set the name of the source space",
      "childId": "9485F1B8-CAEC-48AB-B120-FCD9510C3095",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 477,
      "y": 110,
      "variableGuid": "14B10A3B-89C1-4B2D-9E1A-5096D5382162",
      "operations": [
        {
          "id": "set_value",
          "key": "A17CE820-EB64-4CF9-97EF-634A871F06D8",
          "name": "Set value of { variable }",
          "value": "data file testing 2"
        }
      ]
    },
    {
      "id": "9485F1B8-CAEC-48AB-B120-FCD9510C3095",
      "type": "VariableBlock",
      "disabled": false,
      "name": "tenantHostname",
      "displayName": "Variable - tenantHostname",
      "comment": "Set the tenant hostname, e.g. `mytenant.us.qlikcloud.com`",
      "childId": "21CD9BC3-EB81-4097-8824-1A21CE1AEBEE",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 0,
      "y": 360,
      "variableGuid": "AE3791C9-D010-4598-8F36-CF21E80554A7",
      "operations": [
        {
          "id": "set_value",
          "key": "A17CE820-EB64-4CF9-97EF-634A871F06D8",
          "name": "Set value of { variable }",
          "value": "orchestration.eu.qlikcloud.com"
        }
      ]
    },
    {
      "id": "21CD9BC3-EB81-4097-8824-1A21CE1AEBEE",
      "type": "SnippetBlock",
      "disabled": false,
      "name": "GetTenantNameAndRegion",
      "displayName": "Qlik Platform Operations - Get Tenant Name And Region",
      "comment": "",
      "childId": "B6E365CE-F6C4-496D-B128-0B9A69733BCC",
      "inputs": [
        {
          "id": "575d1740-b1e2-11ed-958a-598edfec33b8",
          "value": "{$.tenantHostname}",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "datasource",
          "value": null,
          "type": "select",
          "structure": []
        },
        {
          "id": "blendr_on_error",
          "value": "stop",
          "type": "select",
          "structure": []
        },
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": -378,
      "y": 163,
      "datasourcetype_guid": "c7e48240-e0f2-11ec-ada1-d5ef75014b77",
      "snippet_guid": "bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"
    },
    {
      "id": "B6E365CE-F6C4-496D-B128-0B9A69733BCC",
      "type": "EndpointBlock",
      "disabled": false,
      "name": "listSpaces",
      "displayName": "Qlik Platform Operations - List Spaces",
      "comment": "Get source space id",
      "childId": "8F7D7918-8FC7-43E6-B3E1-7796810A85FB",
      "inputs": [
        {
          "id": "7717d000-eb0e-11ec-9b55-c70a3d793cb2",
          "value": "{$.GetTenantNameAndRegion}",
          "type": "string",
          "structure": []
        },
        {
          "id": "cf8b5510-d90e-11ed-a579-cd38900fbf47",
          "value": "name eq \"{$.sourceSpaceName}\"",
          "type": "string",
          "structure": []
        },
        {
          "id": "1d91e290-d90f-11ed-80ea-9fec14e6d987",
          "value": null,
          "type": "string",
          "structure": []
        },
        {
          "id": "71ea7180-d90f-11ed-a399-43da6346f683",
          "value": null,
          "type": "string",
          "structure": []
        },
        {
          "id": "92cd6110-d90f-11ed-a57c-89623b3170d1",
          "value": null,
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "datasource",
          "value": null,
          "type": "select",
          "structure": []
        },
        {
          "id": "maxitemcount",
          "value": "",
          "type": "string",
          "structure": []
        },
        {
          "id": "blendr_on_error",
          "value": "stop",
          "type": "select",
          "structure": []
        },
        { "id": "cache", "value": "0", "type": "select", "structure": [] },
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": true }],
      "x": 0,
      "y": 600,
      "datasourcetype_guid": "c7e48240-e0f2-11ec-ada1-d5ef75014b77",
      "endpoint_guid": "76df5d40-eb0e-11ec-85e6-6fa92818449e",
      "endpoint_role": "list"
    },
    {
      "id": "8F7D7918-8FC7-43E6-B3E1-7796810A85FB",
      "type": "SnippetBlock",
      "disabled": false,
      "name": "ListDataFilesFromSpace",
      "displayName": "Qlik Platform Operations - List Data Files From Space",
      "comment": "",
      "childId": "A1A79246-0527-48A9-B078-6250A46E5A57",
      "inputs": [
        {
          "id": "d8e58e20-fa31-11ed-b2ac-0fffc605aad3",
          "value": "{$.GetTenantNameAndRegion}",
          "type": "string",
          "structure": []
        },
        {
          "id": "d8e63580-fa31-11ed-af74-112f69c5deee",
          "value": "{$.listSpaces[0].id}",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "datasource",
          "value": null,
          "type": "select",
          "structure": []
        },
        {
          "id": "blendr_on_error",
          "value": "stop",
          "type": "select",
          "structure": []
        },
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": true }],
      "x": 0,
      "y": 840,
      "datasourcetype_guid": "c7e48240-e0f2-11ec-ada1-d5ef75014b77",
      "snippet_guid": "f8db6b60-fa26-11ed-b985-a3ee665e0cb9"
    },
    {
      "id": "A1A79246-0527-48A9-B078-6250A46E5A57",
      "type": "ShowBlock",
      "disabled": false,
      "name": "output",
      "displayName": "Output",
      "comment": "",
      "childId": "0ABB775E-009D-4802-A698-8CD87D0403D5",
      "inputs": [
        {
          "id": "input",
          "value": "Deleting {count: {$.ListDataFilesFromSpace}} data files in [{$.sourceSpaceName}/ {$.listSpaces[0].id}]",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "display_mode",
          "value": "add",
          "type": "select",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 0,
      "y": 840
    },
    {
      "id": "0ABB775E-009D-4802-A698-8CD87D0403D5",
      "type": "VariableBlock",
      "disabled": false,
      "name": "fileCount",
      "displayName": "Variable - fileCount",
      "comment": "",
      "childId": "CD1F19AA-B91E-452B-93FC-FF333407F8BF",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 0,
      "y": 1200,
      "variableGuid": "CDB8E7BC-B1D2-48A5-9E24-682F890038BB",
      "operations": [
        {
          "id": "set_value",
          "key": "262E2EC6-DD62-4C17-BEE2-944CEED1ED86",
          "name": "Set value of { variable }",
          "value": "0"
        }
      ]
    },
    {
      "id": "CD1F19AA-B91E-452B-93FC-FF333407F8BF",
      "type": "ForEachBlock",
      "disabled": false,
      "name": "loop",
      "displayName": "Loop over Qlik Platform Operations - List Data Files From Space - Loop",
      "comment": "Iterate over data files",
      "childId": "71C9029E-A638-4FEF-9FAF-2D93512A3462",
      "inputs": [
        {
          "id": "input",
          "value": "{ $.ListDataFilesFromSpace }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": -411,
      "y": 1005.6025390625,
      "loopBlockId": "C18D04E6-107A-42B3-9A2A-76AF2BF17EC2"
    },
    {
      "id": "71C9029E-A638-4FEF-9FAF-2D93512A3462",
      "type": "VariableBlock",
      "disabled": false,
      "name": "message",
      "displayName": "Variable - message",
      "comment": "",
      "childId": "B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 370,
      "y": 1420,
      "variableGuid": "43473F0A-CB5C-48A2-8F49-2FC102415E9D",
      "operations": [
        {
          "id": "set_value",
          "key": "00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8",
          "name": "Set value of { variable }",
          "value": "Deleted {count: {$.ListDataFilesFromSpace}} data files in [{$.sourceSpaceName}/ {$.listSpaces[0].id}]"
        }
      ]
    },
    {
      "id": "B0A08A14-B044-428D-BBC7-EC7FBAE4C3EE",
      "type": "ShowBlock",
      "disabled": false,
      "name": "output3",
      "displayName": "Output 3",
      "comment": "",
      "childId": "0A5A4664-638D-4226-9184-343D9E973627",
      "inputs": [
        {
          "id": "input",
          "value": "{ $.message }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "display_mode",
          "value": "add",
          "type": "select",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 0,
      "y": 2100
    },
    {
      "id": "0A5A4664-638D-4226-9184-343D9E973627",
      "type": "UpdateJobBlock",
      "disabled": false,
      "name": "updateRunTitle2",
      "displayName": "Update Run Title 2",
      "comment": "",
      "childId": null,
      "inputs": [
        {
          "id": "title",
          "value": "{ $.message }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 370,
      "y": 1540
    },
    {
      "id": "C18D04E6-107A-42B3-9A2A-76AF2BF17EC2",
      "type": "VariableBlock",
      "disabled": false,
      "name": "fileCount",
      "displayName": "Variable - fileCount",
      "comment": "",
      "childId": "AF8CF1D7-6399-45A7-8E88-D048C2A1132E",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 120,
      "y": 1460,
      "variableGuid": "CDB8E7BC-B1D2-48A5-9E24-682F890038BB",
      "operations": [
        {
          "id": "add",
          "key": "A0D439AD-2311-4084-B745-1B83BD193F20",
          "name": "Add to { variable }",
          "value": "1"
        }
      ]
    },
    {
      "id": "AF8CF1D7-6399-45A7-8E88-D048C2A1132E",
      "type": "VariableBlock",
      "disabled": false,
      "name": "message",
      "displayName": "Variable - message",
      "comment": "",
      "childId": "A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4",
      "inputs": [],
      "settings": [],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 120,
      "y": 1420,
      "variableGuid": "43473F0A-CB5C-48A2-8F49-2FC102415E9D",
      "operations": [
        {
          "id": "set_value",
          "key": "00EE0CFE-EFD8-4FB1-825E-363F4EAD1EC8",
          "name": "Set value of { variable }",
          "value": "> Deleting data file {$.fileCount}/{count: { $.ListDataFilesFromSpace }} ({$.loop.item.name})"
        }
      ]
    },
    {
      "id": "A43DD7D2-B99F-4E4D-B5F6-FBA68AE414C4",
      "type": "UpdateJobBlock",
      "disabled": false,
      "name": "updateRunTitle",
      "displayName": "Update Run Title",
      "comment": "",
      "childId": "0E220820-B4E0-46B5-9C9A-D7A9CD2140AE",
      "inputs": [
        {
          "id": "title",
          "value": "{ $.message }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 120,
      "y": 1540
    },
    {
      "id": "0E220820-B4E0-46B5-9C9A-D7A9CD2140AE",
      "type": "ShowBlock",
      "disabled": false,
      "name": "output2",
      "displayName": "Output 2",
      "comment": "",
      "childId": "072B240A-968F-4B5F-95BD-E091BEC23679",
      "inputs": [
        {
          "id": "input",
          "value": "{ $.message }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "display_mode",
          "value": "add",
          "type": "select",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": 120,
      "y": 1780
    },
    {
      "id": "072B240A-968F-4B5F-95BD-E091BEC23679",
      "type": "EndpointBlock",
      "disabled": false,
      "name": "DeleteDataFile",
      "displayName": "Qlik Platform Operations - Delete Data File",
      "comment": "",
      "childId": null,
      "inputs": [
        {
          "id": "f7e7b480-d863-11ed-a28a-370787b39f57",
          "value": "{ $.GetTenantNameAndRegion }",
          "type": "string",
          "structure": []
        },
        {
          "id": "f7eef030-d863-11ed-908a-53c868154f98",
          "value": "{ $.loop.item.id }",
          "type": "string",
          "structure": []
        }
      ],
      "settings": [
        {
          "id": "datasource",
          "value": null,
          "type": "select",
          "structure": []
        },
        {
          "id": "blendr_on_error",
          "value": "stop",
          "type": "select",
          "structure": []
        },
        {
          "id": "automations_censor_data",
          "value": false,
          "type": "checkbox",
          "structure": []
        }
      ],
      "collapsed": [{ "name": "loop", "isCollapsed": false }],
      "x": -326,
      "y": 1519.811767578125,
      "datasourcetype_guid": "c7e48240-e0f2-11ec-ada1-d5ef75014b77",
      "endpoint_guid": "f7d86270-d863-11ed-a50a-f77431b8290d",
      "endpoint_role": "delete"
    }
  ],
  "variables": [
    {
      "guid": "43473F0A-CB5C-48A2-8F49-2FC102415E9D",
      "name": "message",
      "type": "string"
    },
    {
      "guid": "CDB8E7BC-B1D2-48A5-9E24-682F890038BB",
      "name": "fileCount",
      "type": "number"
    },
    {
      "guid": "AE3791C9-D010-4598-8F36-CF21E80554A7",
      "name": "tenantHostname",
      "type": "string"
    },
    {
      "guid": "14B10A3B-89C1-4B2D-9E1A-5096D5382162",
      "name": "sourceSpaceName",
      "type": "string"
    }
  ]
}
```

A `204` response confirms that the data files, as well as any associated datasets,
have been deleted successfully.
