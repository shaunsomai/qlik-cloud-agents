---
source: https://qlik.dev/manage/automate/move-distributed-apps/
last_updated: 2026-01-19T14:21:00Z
---

# Auto publish apps distributed from Qlik Sense Enterprise Client-Managed

## Auto-publishing a distributed app

When distributing apps from Qlik Sense Enterprise Client-Managed (QSECM), the app
is by default placed into a staging area, requiring an administrator to manually
assign the app to a managed space.

This no-code example identifies apps published to the tenant with the properties:

- `spaceId` is empty
- `published` is `true`
- `originAppId` is empty

Any identified apps are moved to a space. You can add additional blocks to
perform other activities such as changing the app name, owner, and more, if required.

You can run this automation manually, on a schedule, or on the "app created" webhook
from the Qlik Cloud Services connector.

![Automation overview](https://qlik.dev/_astro/move-distributed-apps.DJhg3mGU.png)

For more information about app distribution, see
[Distributing apps to Qlik Cloud](https://help.qlik.com/en-US/sense-admin/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/Multi-Cloud/distributing-apps-QSEoW-to-QCS.htm)
on Qlik Help.

<details>
<summary>Move distributed app to managed space (Qlik Automate)</summary>

```json
{
    "blocks": [
        {
            "id": "BE76460A-8A9E-498A-A40E-321E950B5894",
            "type": "StartBlock",
            "disabled": false,
            "name": "Start",
            "displayName": "Start",
            "comment": "",
            "childId": "DFF3A5B8-88DC-44FC-810E-9AABF76B8BDE",
            "inputs": [
                {
                    "id": "run_mode",
                    "value": "manual",
                    "type": "select",
                    "structure": {}
                }
            ],
            "settings": [],
            "collapsed": [
                {
                    "name": "loop",
                    "isCollapsed": false
                }
            ],
            "x": 0,
            "y": 0,
            "logo": null
        },
        {
            "id": "DFF3A5B8-88DC-44FC-810E-9AABF76B8BDE",
            "type": "EndpointBlock",
            "disabled": false,
            "name": "rawAPIListRequest",
            "displayName": "Qlik Cloud Services - Raw API List Request",
            "comment": "Return items of type app, not in shared spaces, with no actions",
            "childId": null,
            "inputs": [
                {
                    "id": "c3a1c780-2076-11ec-98c4-dd329f9ef682",
                    "value": "items",
                    "type": "string",
                    "structure": {}
                },
                {
                    "id": "c6915fb0-2839-11ec-a450-03c7d8aebbe7",
                    "value": [
                        {
                            "key": "resourceType",
                            "value": "app"
                        },
                        {
                            "key": "shared",
                            "value": "false"
                        },
                        {
                            "key": "noActions",
                            "value": "true"
                        }
                    ],
                    "type": "object",
                    "mode": "keyValue",
                    "structure": {}
                }
            ],
            "settings": [
                {
                    "id": "maxitemcount",
                    "value": null,
                    "type": "string",
                    "structure": {}
                },
                {
                    "id": "blendr_on_error",
                    "value": "stop",
                    "type": "select",
                    "structure": {}
                },
                {
                    "id": "cache",
                    "value": "0",
                    "type": "select",
                    "structure": {}
                },
                {
                    "id": "automations_censor_data",
                    "value": false,
                    "type": "checkbox",
                    "structure": {}
                }
            ],
            "collapsed": [
                {
                    "name": "loop",
                    "isCollapsed": false
                }
            ],
            "x": -257,
            "y": 142,
            "loopBlockId": "37A26683-5C7B-4811-A784-48714B218E97",
            "datasourcetype_guid": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
            "endpoint_guid": "4b993580-2072-11ec-8f59-e5aaa8656a36",
            "endpoint_role": "list"
        },
        {
            "id": "37A26683-5C7B-4811-A784-48714B218E97",
            "type": "IfElseBlock",
            "disabled": false,
            "name": "condition",
            "displayName": "Condition",
            "comment": "If app is published, has no space, and no origin app id",
            "childId": null,
            "inputs": [
                {
                    "id": "conditions",
                    "value": {
                        "mode": "all",
                        "conditions": [
                            {
                                "input1": "{$.rawAPIListRequest.item.resourceAttributes.originAppId}",
                                "operator": "empty",
                                "input2": null
                            },
                            {
                                "input1": "{$.rawAPIListRequest.item.resourceAttributes.published}",
                                "operator": "isTrue",
                                "input2": null
                            },
                            {
                                "input1": "{$.rawAPIListRequest.item.resourceAttributes.spaceId}",
                                "operator": "empty",
                                "input2": null
                            }
                        ]
                    },
                    "type": "custom",
                    "structure": {}
                }
            ],
            "settings": [],
            "collapsed": [
                {
                    "name": "both",
                    "isCollapsed": false
                },
                {
                    "name": "yes",
                    "isCollapsed": false
                },
                {
                    "name": "no",
                    "isCollapsed": false
                }
            ],
            "x": -316,
            "y": 222,
            "childTrueId": "3BC3781D-E106-4ED9-9C2E-882E7306FE79",
            "childFalseId": null
        },
        {
            "id": "3BC3781D-E106-4ED9-9C2E-882E7306FE79",
            "type": "EndpointBlock",
            "disabled": false,
            "name": "moveAppToSpace",
            "displayName": "Qlik Cloud Services - Move App To Space",
            "comment": "Move the app to a specific managed space",
            "childId": null,
            "inputs": [
                {
                    "id": "11432860-5f18-11eb-86e0-f705b887e205",
                    "value": "{$.rawAPIListRequest.item.resourceAttributes.id}",
                    "type": "string",
                    "structure": {}
                },
                {
                    "id": "27141ca0-5f18-11eb-b41a-733bee69f00a",
                    "value": "65096a85afb58f1ff572af75",
                    "type": "string",
                    "displayValue": "aqh (65096a85afb58f1ff572af75)",
                    "structure": {}
                }
            ],
            "settings": [
                {
                    "id": "blendr_on_error",
                    "value": "stop",
                    "type": "select",
                    "structure": {}
                },
                {
                    "id": "automations_censor_data",
                    "value": false,
                    "type": "checkbox",
                    "structure": {}
                }
            ],
            "collapsed": [
                {
                    "name": "loop",
                    "isCollapsed": false
                }
            ],
            "x": 240,
            "y": 420,
            "datasourcetype_guid": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
            "endpoint_guid": "112ad1d0-5f18-11eb-883a-255ecdc2b5bb",
            "endpoint_role": "update"
        }
    ],
    "variables": []
}
```

</details>
