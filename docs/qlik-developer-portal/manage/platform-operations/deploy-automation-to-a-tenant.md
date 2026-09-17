---
source: https://qlik.dev/manage/platform-operations/deploy-automation-to-a-tenant/
last_updated: 2026-07-24T08:27:55-02:30
---

# Deploy an automation to a tenant

## Deploy an automation to a tenant

In this tutorial, you are going to learn how to deploy an automation for Qlik
Automate from a source to a target tenant.

There are many use cases where automations can make management or operations
more efficient, in this example automating the provisioning of user access to a
space when the user logs into the tenant for the first time - this is useful in
scenarios where your Identity Provider doesn't support sending groups for space level
access control. This removes the need for manual user onboarding steps and provides
a timely (near-instant) onboarding for new users joining the tenant.

This guide is part
of the Platform Operations path for creating and configuring target tenants to
support embedded analytics in host applications like other SaaS software or
enterprise applications.

## Code examples

Complete script examples for deploying Qlik content using qlik-cli, curl,
Python, and API collections are available
in the [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations).

## Prerequisites

- You have reviewed previous tutorials in
  the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview),
  since this tutorial builds upon concepts covered in those earlier.
- You have the `name` or `id` of an automation on your source tenant that you
  want to deploy to your target tenant.
- You have deployed a sample automation to your source tenant. You can use the
  example payload provided in section 1.4, or import the workspace example
  from the [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/blob/main/qlik.dev/tutorials/platform-operations/deployment-assets/automation_user_created_add_to_space.json).
- cURL for running the inline examples.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable                | Description                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`       | The domain for the initial tenant created during account onboarding. Equivalent to `tenanthostname.region.qlikcloud.com`.           |
| `<TARGET_TENANT>`       | The domain for the new tenant that this tutorial will create. Equivalent to `tenanthostname.region.qlikcloud.com`.                  |
| `<SOURCE_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<SOURCE_TENANT>`.                                                           |
| `<TARGET_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`.                                                           |
| `<BOT_USER_ID>`         | The user `id` for the `bot user` (or whichever user is making the API calls) to the `<SOURCE_TENANT>`.                              |
| `<DUMMY_USER_ID>`       | The user `id` for the dummy account you created on the `<TARGET_TENANT>` for verifying that the deployed automation is functioning. |
| `<ORIGINAL_USER_ID>`    | The user `id` for the original owner of the automation on the `<SOURCE_TENANT>`.                                                    |
| `<AUTOMATION_NAME>`     | The name of the automation that you're deploying from the `<SOURCE_TENANT>` to `<TARGET_TENANT>`.                                   |
| `<SOURCE_ATM_ID>`       | The Qlik Cloud `id` for the automation `<AUTOMATION_NAME>` on the `<SOURCE_TENANT>`.                                                |
| `<TARGET_ATM_ID>`       | The Qlik Cloud `id` for the automation `<AUTOMATION_NAME>` on the `<TARGET_TENANT>`.                                                |
| `<TARGET_SPACE_ID>`     | The Qlik Cloud `id` for the space on the `<TARGET_TENANT>` used for verifying that the deployed automation is functioning.          |

## 1 Export a Qlik automation from the source tenant

Exporting automations from a tenant requires the following actions via
the [Automations API](https://qlik.dev/apis/rest/automations):

- Retrieving the automation `id` (if you don't know this already).
- Choosing how your OAuth client will access an automation it doesn't own: either
  with a trusted machine-to-machine (M2M) client, or by temporarily transferring
  ownership to the bot user.
- Retrieving the automation definition.

### 1.1 Retrieve the automation ID and owner

You can use filters to search for the correct automation. This example demonstrates
searching for an automation by `<AUTOMATION_NAME>`,
however as automation names are not unique within a tenant, additional filter
attributes may be required.

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/automations?filter=name eq \"<AUTOMATION_NAME>\"" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The response carries the `<SOURCE_ATM_ID>`, and the owner of the automation
`<ORIGINAL_USER_ID>`, which you will use later.

```json
{
  "data": [
      {
          "id": "<SOURCE_ATM_ID>",
          "ownerId": "<ORIGINAL_USER_ID>",
          "name": "<AUTOMATION_NAME>",
          "state": "available",
          "description": "This webhook-driven automation assigns a new user as a consumer to a managed space named \"Production\" once the user logs into Qlik for the first time.",
          "lastRunStatus": "success",
          "runMode": "webhook",
          "createdAt": "2022-12-22T17:53:05.000000Z",
          "updatedAt": "2022-12-22T17:57:04.000000Z",
          "lastRunAt": "2022-12-22T17:53:47.000000Z"
      }
  ],
  ...
}

```

The automation will normally have been created by an interactive user on the
`<SOURCE_TENANT>`, while your automation scripts will be running under a `bot user`.

For this tutorial, use either a trusted M2M OAuth client with the `admin.automations`
scope or the temporary ownership-transfer method.

If your OAuth client uses machine-to-machine (M2M) authentication, is configured as **Trusted**,
and includes the `admin.automations` scope, its bot user can retrieve and update the
automation directly, regardless of owner or space.
No additional space role is required, and you do not need to transfer ownership.

This capability does not extend to connections used by the automation.

With this approach, you can skip steps 1.2, 1.3, and 1.5.
Continue to [1.4 Retrieve the automation definition](#14-retrieve-the-automation-definition)
using this OAuth client's access token, then proceed to
[2 Deploy the automation to the target tenant](#2-deploy-the-automation-to-the-target-tenant).

For setup instructions,
see [Get started with OAuth machine-to-machine](https://qlik.dev/authenticate/oauth/getting-started-oauth-m2m)
and [Create an OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).

If you are following the tenant-admin workflow, continue to
[1.2 Retrieve the bot user ID](#12-retrieve-the-bot-user-id) to temporarily
transfer the automation to the bot user.

> **Note:** If you change ownership of an automation, any connections (other than the Qlik Cloud connector) will stop working as
> these are not transferred with the automation. Changelog history will be lost.
> Creating or recreating connections is not yet supported via API.

### 1.2 Retrieve the bot user ID

To retrieve the user `id` of the identity making these API calls, use
the [Users API](https://qlik.dev/apis/rest/users):

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/users/me" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

If you follow the redirect response from this endpoint, you will return
the user's information and be able to retrieve the `<BOT_USER_ID>`:

```json
{
    "id": "<BOT_USER_ID>",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "clientId": "f0e92f326ac77427df155940fec39e6a",
    "status": "active",
    "subject": "qlikbot\\f0e92f326ac77427df155940fec39e6a",
    "name": "EU OAuth Client",
    "roles": [
        "TenantAdmin"
    ],
    ...
}

```

### 1.3 Change the owner of the automation to the bot user

Now change the ownership of the automation with a `POST` request:

```bash
curl -L -X POST "https://<SOURCE_TENANT>/api/v1/automations/<SOURCE_ATM_ID>/actions/move" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"userId\": \"<BOT_USER_ID>\"
}"
```

The automation will now be owned by the `bot user`, and you will now be able to
access the automation definition.

### 1.4 Retrieve the automation definition

You can retrieve the automation definition and metadata with:

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/automations/<SOURCE_ATM_ID>" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The response will be a large JSON object which details the automation name,
description, other metadata, and the blocks and logic within the automation.
This can be used as the payload for the request into the
`<TARGET_TENANT>` as the API will strip out any redundant fields or metadata
during the import process.

The JSON response is shown in full here in case you wish to use it directly
in your tenant, but the automation workspace file is also referenced in the
prerequisites section if you prefer to build the request yourself.

```json
{
    "id": "74b4a630-8225-11ed-a03f-afd11588e895",
    "ownerId": "637390ec6541614d3a88d6c1",
    "name": "Add new user to Production managed space",
    "state": "available",
    "description": "This webhook-driven automation assigns a new user as a consumer to a managed space named \"Production\" once the user logs into Qlik for the first time.",
    "schedules": [
        {
            "id": "74c5be00-8225-11ed-b81c-77de9cdb8edd",
            "startAt": null,
            "stopAt": null,
            "lastStartAt": null,
            "interval": -1,
            "timezone": "Europe/London"
        }
    ],
    "snippetIds": [],
    "endpointIds": [
        "272d9c70-6d31-11eb-870f-67624392ed86",
        "590a1a20-6d2e-11eb-9714-df1bbaac055d"
    ],
    "connectorIds": [
        "61a87510-c7a3-11ea-95da-0fb0c241e75c"
    ],
    "workspace": {
        "blocks": [
            {
                "x": 0,
                "y": 0,
                "id": "2252CA1C-FDAF-4634-B1B4-F43283AA074B",
                "name": "UserCreated",
                "type": "StartBlock",
                "inputs": [
                    {
                        "id": "run_mode",
                        "type": "select",
                        "value": "webhook",
                        "structure": []
                    },
                    {
                        "id": "datasourcetype_guid",
                        "type": "select",
                        "value": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
                        "structure": [],
                        "displayValue": "Qlik Cloud Services"
                    },
                    {
                        "id": "webhook_event_guid",
                        "type": "select",
                        "value": "5be4c220-6156-11eb-a3df-fdbac6cc38a0",
                        "structure": [],
                        "displayValue": "User Created"
                    },
                    {
                        "id": "test_payload",
                        "type": "json",
                        "value": "{\n  \"data\": {\n    \"id\": \"example_4Py5kq5i3OhUWAfBauEyPd423eSNJF8X\",\n    \"subject\": \"example_auth0|f6b3fd7b7a3f625904134b89379372375300cff2dafc31a65a17cc093bb690b2\",\n    \"tenantId\": \"example_WL69WlNT4PRbwAA8EZ1sDblqjthluHL1\"\n  },\n  \"source\": \"com.qlik/users\",\n  \"eventId\": \"example_CGMoX8zP3RaPcGLKxQ_Sy5N4O0bh9XxE\",\n  \"eventTime\": \"2021-09-09T09:32:53.782Z\",\n  \"eventType\": \"com.qlik.v1.user.created\",\n  \"extensions\": {\n    \"userId\": \"example_BlVarUAUM9I0ei3MmKMejlDaF1sKPnN5\",\n    \"tenantId\": \"example_WL69WlNT4PRbwAA8EZ1sDblqjthluHL1\"\n  },\n  \"contentType\": \"application/json\",\n  \"eventTypeVersion\": \"1.0.0\",\n  \"cloudEventsVersion\": \"0.1\"\n}",
                        "structure": []
                    },
                    {
                        "id": "webhook_documentation",
                        "type": "string",
                        "value": null,
                        "structure": []
                    }
                ],
                "childId": "689E8B00-5803-4A44-B0C2-BBE363933BBC",
                "comment": null,
                "disabled": false,
                "settings": [],
                "collapsed": [
                    {
                        "name": "loop",
                        "isCollapsed": false
                    }
                ],
                "displayName": "User Created",
                "loopBlockId": null
            },
            {
                "x": -60,
                "y": 277,
                "id": "9303A69B-E135-4911-A930-A50904EB9D3E",
                "name": "addMemberToSpace",
                "type": "EndpointBlock",
                "inputs": [
                    {
                        "id": "3162f740-6d33-11eb-a089-71f7ccab24b9",
                        "type": "string",
                        "value": "{$.searchSpaces.item.id}",
                        "structure": []
                    },
                    {
                        "id": "27499b00-6d31-11eb-bbe5-5b3db3c974dc",
                        "type": "string",
                        "value": "{$.UserCreated.data.id}",
                        "structure": []
                    },
                    {
                        "id": "2751b870-6d31-11eb-9d77-41c5fae28bc5",
                        "type": "string",
                        "value": "[\"consumer\"]",
                        "structure": []
                    },
                    {
                        "id": "275e2c50-6d31-11eb-8eeb-157347755492",
                        "type": "select",
                        "value": "aec7c5b0-6d32-11eb-a4b2-f5e181a2c241",
                        "structure": [],
                        "displayValue": "user"
                    }
                ],
                "childId": null,
                "comment": null,
                "disabled": false,
                "settings": [
                    {
                        "id": "blendr_on_error",
                        "type": "select",
                        "value": "stop",
                        "structure": []
                    }
                ],
                "collapsed": [
                    {
                        "name": "loop",
                        "isCollapsed": false
                    }
                ],
                "displayName": "Qlik Cloud Services - Add Member To Space",
                "loopBlockId": null,
                "endpoint_guid": "272d9c70-6d31-11eb-870f-67624392ed86",
                "datasourcetype_guid": "61a87510-c7a3-11ea-95da-0fb0c241e75c"
            },
            {
                "x": 249,
                "y": 200,
                "id": "689E8B00-5803-4A44-B0C2-BBE363933BBC",
                "name": "searchSpaces",
                "type": "EndpointBlock",
                "inputs": [
                    {
                        "id": "592e21a0-6d2e-11eb-9985-3ff14fb3335f",
                        "type": "string",
                        "value": "managed",
                        "structure": []
                    },
                    {
                        "id": "5935dec0-6d2e-11eb-8365-ab8493d4c237",
                        "type": "string",
                        "value": null,
                        "structure": []
                    },
                    {
                        "id": "593c5340-6d2e-11eb-a82b-e17cfa6c8a6d",
                        "type": "string",
                        "value": "+name",
                        "structure": []
                    },
                    {
                        "id": "59429c60-6d2e-11eb-b7b1-e7ca1f22830c",
                        "type": "string",
                        "value": "Production",
                        "structure": []
                    },
                    {
                        "id": "5949c230-6d2e-11eb-b345-99be61e9908c",
                        "type": "string",
                        "value": null,
                        "structure": []
                    }
                ],
                "childId": null,
                "comment": null,
                "disabled": false,
                "settings": [
                    {
                        "id": "maxitemcount",
                        "type": "string",
                        "value": null,
                        "structure": []
                    },
                    {
                        "id": "blendr_on_error",
                        "type": "select",
                        "value": "stop",
                        "structure": []
                    }
                ],
                "collapsed": [
                    {
                        "name": "loop",
                        "isCollapsed": false
                    }
                ],
                "displayName": "Qlik Cloud Services - Search Spaces",
                "loopBlockId": "9303A69B-E135-4911-A930-A50904EB9D3E",
                "endpoint_guid": "590a1a20-6d2e-11eb-9714-df1bbaac055d",
                "datasourcetype_guid": "61a87510-c7a3-11ea-95da-0fb0c241e75c"
            }
        ],
        "variables": []
    },
    "lastRun": {
        "id": "c45cdd10-82ad-11ed-834b-63e6d75919cb",
        "context": "webhook",
        "status": "finished",
        "title": null,
        "isTestRun": false,
        "isArchived": true,
        "error": null,
        "startTime": "2022-12-23T10:37:15.000000Z",
        "stopTime": "2022-12-23T10:37:15.000000Z",
        "scheduledStartTime": null,
        "createdAt": "2022-12-23T10:37:15.000000Z",
        "updatedAt": null
    },
    "lastRunStatus": "finished",
    "executionToken": "H1uYyOyeziIvUVKljy5rgd9ypneELVSTwg08uN2FNIyxrkveOhEwuAuHjw2E2tYH",
    "runMode": "webhook",
    "createdAt": "2022-12-22T18:21:30.000000Z",
    "updatedAt": "2022-12-23T10:37:15.000000Z",
    "lastRunAt": "2022-12-23T10:37:15.000000Z"
}
```

### 1.5 Return the automation to the original owner

> **Note:** Complete this step only if you transferred ownership in section 1.3. If you used
> the trusted M2M client method, skip this step.

To ensure the former owner of the automation regains access to it, you should
move the automation back to that user with another `POST` request, this time
specifying the `<ORIGINAL_USER_ID>`:

```bash
curl -L -X POST "https://<SOURCE_TENANT>/api/v1/automations/<SOURCE_ATM_ID>/actions/move" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"userId\": \"<ORIGINAL_USER_ID>\"
}"
```

## 2 Deploy the automation to the target tenant

Now that you have the automation definition, you can deploy it to the target
tenant. You can use the definition returned from the source tenant, or construct
the JSON payload using a workspace
and provide your own automation configuration and metadata. See
the [Automations API](https://qlik.dev/apis/rest/automations) specification for the attributes that are respected from the payload.

In this example, you send the unmodified payload from section 1.4 and use this
to recreate the automation in the target tenant:

```bash
curl -L -X POST "https://<TARGET_TENANT>/api/v1/automations" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-d "{
    \"id\": \"74b4a630-8225-11ed-a03f-afd11588e895\",
    \"ownerId\": \"637390ec6541614d3a88d6c1\",
    \"name\": \"Add new user to Production managed space\",
    \"state\": \"available\",
    \"description\": \"This webhook-driven automation assigns a new user as a consumer to a managed space named \\\"Production\\\" once the user logs into Qlik for the first time.\",
    \"schedules\": [
        {
            \"id\": \"74c5be00-8225-11ed-b81c-77de9cdb8edd\",
            \"startAt\": null,
            \"stopAt\": null,
            \"lastStartAt\": null,
            \"interval\": -1,
            \"timezone\": \"Europe/London\"
        }
    ],
    \"snippetIds\": [],
    \"endpointIds\": [
        \"272d9c70-6d31-11eb-870f-67624392ed86\",
        \"590a1a20-6d2e-11eb-9714-df1bbaac055d\"
    ],
    \"connectorIds\": [
        \"61a87510-c7a3-11ea-95da-0fb0c241e75c\"
    ],
    \"workspace\": {
        \"blocks\": [
            {
                \"x\": 0,
                \"y\": 0,
                \"id\": \"2252CA1C-FDAF-4634-B1B4-F43283AA074B\",
                \"name\": \"UserCreated\",
                \"type\": \"StartBlock\",
                \"inputs\": [
                    {
                        \"id\": \"run_mode\",
                        \"type\": \"select\",
                        \"value\": \"webhook\",
                        \"structure\": []
                    },
                    {
                        \"id\": \"datasourcetype_guid\",
                        \"type\": \"select\",
                        \"value\": \"61a87510-c7a3-11ea-95da-0fb0c241e75c\",
                        \"structure\": [],
                        \"displayValue\": \"Qlik Cloud Services\"
                    },
                    {
                        \"id\": \"webhook_event_guid\",
                        \"type\": \"select\",
                        \"value\": \"5be4c220-6156-11eb-a3df-fdbac6cc38a0\",
                        \"structure\": [],
                        \"displayValue\": \"User Created\"
                    },
                    {
                        \"id\": \"test_payload\",
                        \"type\": \"json\",
                        \"value\": \"{\n  \\\"data\\\": {\n    \\\"id\\\": \\\"example_4Py5kq5i3OhUWAfBauEyPd423eSNJF8X\\\",\\n    \\\"subject\\\": \\\"example_auth0|f6b3fd7b7a3f625904134b89379372375300cff2dafc31a65a17cc093bb690b2\\\",\\n    \\\"tenantId\\\": \\\"example_WL69WlNT4PRbwAA8EZ1sDblqjthluHL1\\\"\\n  },\\n  \\\"source\\\": \\\"com.qlik/users\\\",\\n  \\\"eventId\\\": \\\"example_CGMoX8zP3RaPcGLKxQ_Sy5N4O0bh9XxE\\\",\\n  \\\"eventTime\\\": \\\"2021-09-09T09:32:53.782Z\\\",\\n  \\\"eventType\\\": \\\"com.qlik.v1.user.created\\\",\\n  \\\"extensions\\\": {\\n    \\\"userId\\\": \\\"example_BlVarUAUM9I0ei3MmKMejlDaF1sKPnN5\\\",\\n    \\\"tenantId\\\": \\\"example_WL69WlNT4PRbwAA8EZ1sDblqjthluHL1\\\"\\n  },\\n  \\\"contentType\\\": \\\"application/json\\\",\\n  \\\"eventTypeVersion\\\": \\\"1.0.0\\\",\\n  \\\"cloudEventsVersion\\\": \\\"0.1\\\"\\n}\",
                        \"structure\": []
                    },
                    {
                        \"id\": \"webhook_documentation\",
                        \"type\": \"string\",
                        \"value\": null,
                        \"structure\": []
                    }
                ],
                \"childId\": \"689E8B00-5803-4A44-B0C2-BBE363933BBC\",
                \"comment\": null,
                \"disabled\": false,
                \"settings\": [],
                \"collapsed\": [
                    {
                        \"name\": \"loop\",
                        \"isCollapsed\": false
                    }
                ],
                \"displayName\": \"User Created\",
                \"loopBlockId\": null
            }
        ],
        \"variables\": []
    },
    \"lastRun\": {
        \"id\": \"c45cdd10-82ad-11ed-834b-63e6d75919cb\",
        \"context\": \"webhook\",
        \"status\": \"finished\",
        \"title\": null,
        \"isTestRun\": false,
        \"isArchived\": true,
        \"error\": null,
        \"startTime\": \"2022-12-23T10:37:15.000000Z\",
        \"stopTime\": \"2022-12-23T10:37:15.000000Z\",
        \"scheduledStartTime\": null,
        \"createdAt\": \"2022-12-23T10:37:15.000000Z\",
        \"updatedAt\": null
    },
    \"lastRunStatus\": \"finished\",
    \"executionToken\": \"H1uYyOyeziIvUVKljy5rgd9ypneELVSTwg08uN2FNIyxrkveOhEwuAuHjw2E2tYH\",
    \"runMode\": \"webhook\",
    \"createdAt\": \"2022-12-22T18:21:30.000000Z\",
    \"updatedAt\": \"2022-12-23T10:37:15.000000Z\",
    \"lastRunAt\": \"2022-12-23T10:37:15.000000Z\"
}"
```

The response will contain the definition for the new automation:

```json
{
    "id": "2e59b3c0-82ac-11ed-9a55-0f12ebd2b675",
    "ownerId": "CBg-NdDpqyFZIHRxylm03Pr2Gp3U7Ynn",
    "name": "Add new user to Production managed space",
    "state": "available",
    "description": "This webhook-driven automation assigns a new user as a consumer to a managed space named \"Production\" once the user logs into Qlik for the first time.",
    "schedules": [
        {
            "id": "2e69ca60-82ac-11ed-9db9-31ce2f4c6db4",
            "startAt": null,
            "stopAt": null,
            "lastStartAt": null,
            "interval": -1,
            "timezone": "Europe/London"
        }
    ],
    "snippetIds": [],
    "endpointIds": [
        "272d9c70-6d31-11eb-870f-67624392ed86",
        "590a1a20-6d2e-11eb-9714-df1bbaac055d"
    ],
    "connectorIds": [
        "61a87510-c7a3-11ea-95da-0fb0c241e75c"
    ],
    "workspace": {
        ...
    },
    ...
}
```

## 3 Test the automation by creating a test user

If you deployed the example automation referenced in this guide, you can verify
it is functioning correctly by creating a dummy user in the tenant. The automation
will trigger on creation of the user and assign them access to a managed space
named `Production`.

Prior to running this test, ensure that you have either:

- Created a managed space called `Production`, or
- Amended the automation to point to a space that you have created with a different
  name.

### 3.1 Create a dummy user

To create a dummy user, specify a subject and email address that don't exist and
send the request to the target tenant:

```bash
curl -L -X POST "https://<TARGET_TENANT>/api/v1/users" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"name\": \"AutomationTestUser\",
    \"email\": \"null@null.null\",
    \"status\": \"active\",
    \"subject\": \"thiswontwork|doesntwork\"
}"
```

If the user is created successfully, a new user record will be returned with a
new `<DUMMY_USER_ID>`:

```json
{
    "id": "<DUMMY_USER_ID>",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "status": "active",
    "subject": "thiswontwork|doesntwork",
    "name": "AutomationTestUser",
    "email": "null@null.null",
    ...
}
```

At this point, you can verify the last run state of the automation by loading
the definition as you did in section 1.4, or you can review the target space to
validate that the user was correctly assigned with the expected roles.

### 3.2 Get the id of the managed space

If you wish to review what role the user was assigned, you need to load the details
for the space.

To load the assignments to the managed space you need to retrieve the space `id`.
This can be done using a filter on
the [Spaces API](https://qlik.dev/apis/rest/spaces) for `name eq "Production"`:

```bash
curl -L -X GET "https://<TARGET_TENANT>/api/v1/spaces?filter=name eq \"Production\"" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return the space definition, from which you can retrieve the `id` as
`<TARGET_SPACE_ID>`:

```json
{
    "data": [
        {
            "id": "<TARGET_SPACE_ID>",
            "type": "managed",
            "ownerId": "637390ec6541614d3a88d6c1",
            "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
            "name": "Production",
            "description": "External production space for app consumption",
            ...
        }
    ],
    ...
}
```

### 3.3 Review space assignment listing

Using `<TARGET_SPACE_ID>` you can retrieve the users assigned to the space
to verify that the automation was successful:

```bash
curl -L -X GET "https://<TARGET_TENANT>/api/v1/spaces/<TARGET_SPACE_ID>/assignments" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

You can review the response to locate the `<DUMMY_USER_ID>` user
and verify that they were correctly assigned the `consumer` role as specified
in the automation:

```json
{
    "data": [
        {
            "id": "63a584db606b935ecf83c547",
            "type": "user",
            "assigneeId": "<DUMMY_USER_ID>",
            "roles": [
                "consumer"
            ],
            "spaceId": "6373a8d19ae129379863f613",
            "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
            ...
        },
        ...
    ],
    ...
}
```

### 3.4 Delete the test user

With the test complete, it is good practice to delete any dummy users. You can
do this with a `DELETE` call to the [Users API](https://qlik.dev/apis/rest/users):

```bash
curl -L -X DELETE "https://<TARGET_TENANT>/api/v1/users/<DUMMY_USER_ID>" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>"
```

A `204` response indicates that the dummy user has been successfully deleted from
the target tenant.

## Next steps

Now that you have a tenant configured and hydrated with content, you
can [delete the tenant](https://qlik.dev/manage/platform-operations/delete-a-tenant).
