---
source: https://qlik.dev/manage/platform-operations/third-party/move-apps-between-tenants/
last_updated: 2026-03-18T16:49:43Z
---

# Move hydrated apps between tenants with third-party tools

This topic demonstrates using a third-party tool (in this case, GitHub, and GitHub
Actions) to support programmatic deployment of applications from Qlik Cloud.
Using third-party tools such as GitHub enables you to chain together automation
tasks such as capturing snapshots, version control, release reviews and testing
using tools that are familiar to developers.

The example exports apps from a source tenant, and imports them to a target tenant.
This supports the movement of Qlik Sense applications up to 10 GB in memory,
using GitHub Actions. This is intended for use as part of a build pipeline
integrated into a larger GitHub workflow.

> **Note:** It is your responsibility to ensure that your usage of GitHub and GitHub Actions
> adheres to GitHub terms and conditions of service. This is provided as an example
> of how you can leverage Qlik APIs and third-party tooling to build integrated
> CICD and release processes.

## Code examples

To run this tutorial as provided, you can fork
the [example repository](https://github.com/qlik-oss/qlikdev-move-apps-third-party),
then follow the tutorial to set up the integration with your tenants.

## Prerequisites

- You have reviewed previous tutorials in
  the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview), as this tutorial assumes your knowledge of
  concepts and steps covered earlier.
- You have access to two tenants, and regional OAuth client credentials.
- You have access to a GitHub account in which to run the example.
- You have access to Qlik Automate.
- You have [set up a connection](https://qlik.dev/manage/platform-operations/no-code/qpo-configure-connector) for the
  Platform Operations connector in Qlik Automate. This connection should have access to both tenants.
- You have set up a connection for the GitHub connector in Qlik Automate.

## Variable substitution

Throughout this topic, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this topic.

| Variable                    | Description                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`           | The domain for the tenant where the apps are retrieved from. Equivalent to `tenanthostname.region.qlikcloud.com`.                                                                                                             |
| `<TARGET_TENANT>`           | The domain for the tenant where the apps will be deployed to. Equivalent to `tenanthostname.region.qlikcloud.com`.                                                                                                            |
| `<CLIENT_ID>`               | The client ID for an OAuth client, specific to the region you're sending requests to.                                                                                                                                         |
| `<CLIENT_SECRET>`           | The client secret for the specific OAuth `<CLIENT_ID>`. This should be treated as a secret.                                                                                                                                   |
| `<RETURN_AUTOMATION>`       | The path to the return automation, called from GitHub. Equivalent to `https://orchestration.eu.qlikcloud.com/api/v1/automations/2c35d470-1f0b-11ee-ba84-db515e47c00a/actions/execute`. Should not contain an execution token. |
| `<RETURN_AUTOMATION_TOKEN>` | The execution token for the `<RETURN_AUTOMATION>`. This should be treated as a secret. Does not contain spaces.                                                                                                               |
| `<SOURCE_APP_ID>`           | The Qlik Cloud ID for the app `<APP_NAME>` in a shared space on the `<SOURCE_TENANT>`.                                                                                                                                        |
| `<SHARED_SPACE_ID>`         | The Qlik Cloud ID for the shared space on the `<TARGET_TENANT>`.                                                                                                                                                              |

## Why move apps?

When using multiple tenants in Qlik Cloud, you have two choices for how you
refresh Qlik Sense application data on each tenant:

- Distributed: Each tenant receives an empty application template, and an app reload
  on that tenant hydrates the template with data.
- Centralized: A central tenant reloads a copy of the application for every tenant,
  and a service distributes the fully reloaded applications (already hydrated)
  out to each tenant.

The distributed method is supported using no-code tooling within the platform,
but if you wish to use the centralized method, it is likely that your apps will
exceed the supported limits for Qlik no-code tools, and you will need to use Qlik APIs
directly to move this data.

You can learn how to do this in the [deploying Qlik Sense apps](https://qlik.dev/manage/platform-operations/deploy-content-to-a-tenant) tutorial.
This tutorial builds on that foundation to
demonstrate how you can leverage SaaS tooling (Qlik Automate in
conjunction, supported by a third-party tool) to achieve the same outcome.

## Deploying the solution

This design uses an Automation running on a central (source) tenant that orchestrates
the movement of apps to the other (target) tenants. As Automations doesn't support
the movement of large files, the app movement step is completed by a GitHub action,
and the repository maintains the history of deployments.

![Workflow runs denoting deployments](https://qlik.dev/_astro/tpg-workflow-runs.B7hSnVJ5.png)

Summary of process:

1. On the source tenant, an application is reloaded.
2. An Automation on the source tenant triggers on successful completion of the
   reload task, and commits a deployment manifest to a GitHub repository, and
   opens a pull request.
3. After the pull request is opened, a GitHub Action workflow retrieves the app from
   the source tenant, then uploads and imports this to the target tenant. Once the
   transfer is complete, the pull request is merged to the `main` branch of the
   repository to maintain a history of transferred apps, and the action triggers
   another automation on the source tenant.
4. The second automation on the source tenant handles any publishing/ updates of
   the newly imported app on the target tenant.

Although it is possible to use the action to handle all operations on the target
tenant, you call back to automations to reduce the number of lines of code running
outside of Qlik Cloud, and to reduce the runtime of the action.

This solution is formed of:

- A GitHub repository.
- A GitHub action.
- An automation on the source tenant to deploy the manifest to your repository.
- An automation on the source tenant to publish and replace the application
  after it's been moved.

### 1 Create and configure your GitHub repository

> **Note:** You can skip this step if you cloned the example repository.

Create a new private GitHub repository, and enable actions. Make a note of
the repository owner (`<REPO_OWNER>`), repository name (`<REPO_NAME>`). You
can find these via your repository URL, for
example, `https://github.com/<REPO_OWNER>/<REPO_NAME>`.

### 2 Deploy the action

> **Note:** You can skip this step if you cloned the example repository.

In your repository, create the file `.github/workflows/moveApp.yml` using this
snippet:

<details>
  <summary>moveApp.yml</summary>

  ```yml
  # Exports an app from a tenant, imports it to another, calls automations back

  name: Move app from source to target

  on:
    # On PR against main
    pull_request:
      branches: [ "main" ]

    # Manual run
    workflow_dispatch:

  jobs:
    # Single moveApp workflow
    moveApp:
      # Run on ubuntu-latest for additional curl features
      runs-on: ubuntu-latest
      permissions: write-all 
      steps:
      
        # Checks-out your repository under $GITHUB_WORKSPACE
        - name: "Checkout repo"
          uses: actions/checkout@v3
          
        - name: "Check curl version"
          run: curl --version
            
        - name: "Check jq version"
          run: jq --version
         
        - name: "Convert ${{ github.head_ref }}.json to .env"
          uses: ricosandyca/convert-env-json@main
          with:
            type: json-to-env
            input_path: "deployments/${{ github.head_ref }}.json"
            output_path: ".env"
        
        - name: "Load .env"
          uses: aarcangeli/load-dotenv@v1.0.0

        - name: "Retrieve OAuth token for source tenant"
          run: |
            SOURCE_TOKEN=$(curl -L "https://${{ env.sourceTenant }}/oauth/token" \
            -X POST \
            -H "Accept: application/json" \
            -H "Content-Type: application/json" \
            -d '{"client_id":"${{ vars.OAUTH_ID }}", "client_secret":"${{ secrets.OAUTH_SECRET }}", "grant_type":"client_credentials"}')
            echo "SOURCE_TOKEN=$SOURCE_TOKEN" >> $GITHUB_ENV

        - name: "Run export command on source tenant"
          run: |
            SOURCE_LOCATION=$(curl -I "https://${{ env.sourceTenant }}/api/v1/apps/${{ env.sourceAppId }}/export" \
            -X POST \
            -H "Content-Type: application/octet-stream" \
            -H "Authorization: Bearer ${{ fromJson(env.SOURCE_TOKEN).access_token }}" \
            | grep -F "location:" | awk '{print $2}' | tr -d '[:space:]')
            echo "SOURCE_LOCATION=$SOURCE_LOCATION" >> $GITHUB_ENV
            
        - name: "Download exported app from source tenant"
          run: |
            curl --output "export.qvf" \
            -X GET "https://${{ env.sourceTenant }}${{ env.SOURCE_LOCATION }}" \
            -H "Authorization: Bearer ${{ fromJson(env.SOURCE_TOKEN).access_token }}" \
            -H "Content-Type: application/octet-stream"
            ls -l
            
        - name: "Retrieve OAuth token for target tenant"
          run: |
            TARGET_TOKEN=$(curl -L "https://${{ env.targetTenant }}/oauth/token" \
            -X POST \
            -H "Accept: application/json" \
            -H "Content-Type: application/json" \
            -d '{"client_id":"${{ vars.OAUTH_ID }}", "client_secret":"${{ secrets.OAUTH_SECRET }}", "grant_type":"client_credentials"}')
            echo "TARGET_TOKEN=$TARGET_TOKEN" >> $GITHUB_ENV
            
        - name: "Upload app to target tenant"
          run: |
            TARGET_LOCATION=$(curl -L "https://${{ env.targetTenant }}/api/v1/temp-contents?filename=export.qvf" -v \
            -X POST \
            -H "Authorization: Bearer ${{ fromJson(env.TARGET_TOKEN).access_token }}" \
            -H "Content-Type: application/octet-stream" \
            -H "Transfer-Encoding: chunked" \
            -T "export.qvf" 2>&1 \
            | grep -F "< location:" | awk '{print $3}' | tr -d '[:space:]' | awk -F / '{print $NF}')
            echo "TARGET_LOCATION=$TARGET_LOCATION" >> $GITHUB_ENV
            echo $TARGET_LOCATION
            
        - name: "Import app to shared space"
          run: |
            echo "APP_NAME=$(${{ env.name }} | sed 's/ /%20/g' )" >> $GITHUB_ENV
            IMPORTED_APP=$(curl "https://${{ env.targetTenant }}/api/v1/apps/import" \
            -X POST -G \
            --data-urlencode 'fileId=${{ env.TARGET_LOCATION }}' \
            --data-urlencode 'name=${{ env.APP_NAME }}' \
            --data-urlencode 'spaceId=${{ env.targetSpaceId }}' \
            -H "Authorization: Bearer ${{ fromJson(env.TARGET_TOKEN).access_token }}" \
            -H "Content-Type: application/json" \
            -H "Accept: application/json"  | jq -r '.attributes.id')
            echo "IMPORTED_APP=$IMPORTED_APP" >> $GITHUB_ENV
            echo $IMPORTED_APP

        - name: "Send callback to automations"
          run: |
            AUTOMATION_RESPONSE=$(curl '${{ vars.RETURN_AUTOMATION }}' \
            -X POST \
            -s -o /dev/null -w "%{http_code}" \
            -H 'X-Execution-Token: ${{ secrets.RETURN_AUTOMATION_TOKEN }}' \
            --data-urlencode 'id=${{ env.id }}' \
            --data-urlencode 'name=${{ env.name }}' \
            --data-urlencode 'sourcetenant=${{ env.sourceTenant }}' \
            --data-urlencode 'targettenant=${{ env.targetTenant }}' \
            --data-urlencode 'targetspaceid=${{ env.targetSpaceId }}' \
            --data-urlencode 'sourceappid=${{ env.sourceAppId }}' \
            --data-urlencode 'newappid=${{ env.IMPORTED_APP }}')
            echo "AUTOMATION_RESPONSE=$AUTOMATION_RESPONSE" >> $GITHUB_ENV
        
        - name: "Verify automation response code"
          run: if [ "${{ fromJson( env.AUTOMATION_RESPONSE ) }}" -ne 200 ]; then exit "${{ fromJson( env.AUTOMATION_RESPONSE ) }}"; fi
          
        - name: Comment PR
          uses: thollander/actions-comment-pull-request@v2.3.1
          with:
            message: |
              Content deployed successfully (${{ env.AUTOMATION_RESPONSE }} response) to [${{ env.targetTenant }}](https://${{ env.targetTenant }}/sense/app/${{ env.IMPORTED_APP }}).
        
        - id: automerge
          name: Merge the PR
          uses: "pascalgn/automerge-action@v0.15.6"
          env:
            GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
            MERGE_LABELS: "!x"
            
        - name: Confirm PR merged
          if: steps.automerge.outputs.mergeResult == 'merged'
          run: |
            echo "Pull request ${{ steps.automerge.outputs.pullRequestNumber }} merged."
      
  ```
</details>

Save this onto the `main` branch of your repository. This will trigger each time
a new pull request is opened against the `main` branch of your repository (for
newly created repositories, `main` is the default primary branch). It can also
be triggered manually using the actions tab in the GitHub repository.

![First few lines of the workflow for GitHub actions](https://qlik.dev/_astro/tpg-workflow.B3Gzjerb.png)

This workflow specifies permissions, rather than configuring them in the repository
settings. You should review these are appropriate before deploying this solution.

The workflow leverages third-party actions to make tasks in the workflow more
straightforward, although all calls to Qlik Cloud are made using cURL.

### 3 Deploy the deployment automation

On your source tenant, navigate to the Hub and create a new blank automation.
Copy the JSON from the snippet below and paste it into the workspace window. Connect
the new blocks to the start block.

> **Note:** This automation requires a valid connection on both the Platform Operations
> and GitHub connectors. The automation will prompt you to configure these connections
> if they do not already exist. Ensure the Platform Operations connection has access
> to your source tenant, and your GitHub connection has access to the repository.

<details>
  <summary>Deployment Automation</summary>

  ```json
  {"blocks":[{"id":"712F2587-CEC9-4F0C-AD95-566EC16804DB","type":"StartBlock","disabled":false,"name":"Start","displayName":"Start","comment":"","childId":"A86CFD38-73D8-46AD-8A39-4D66753C4E0B","inputs":[{"id":"run_mode","value":"triggered","type":"select","structure":{}},{"id":"async","value":"no","type":"select","structure":{}},{"id":"","value":null,"type":"custom","structure":{}}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":0,"logo":null},{"id":"EE90CC59-4183-469E-B950-26D3297437A2","type":"SnippetBlock","disabled":false,"name":"createBranch","displayName":"Git Hub - Create Branch","comment":"Create a new branch (runId)","childId":"3493BD96-7CEE-48BC-82F9-9087637E13A8","inputs":[{"id":"9eba70d0-1ed9-11ed-9ddc-9dd0fb7fb287","value":"{ $.repoOwner }","type":"string","structure":[]},{"id":"9ebbf060-1ed9-11ed-afa2-9f7291db7342","value":"{ $.repoName }","type":"string","structure":[]},{"id":"9ebcabc0-1ed9-11ed-bcd0-df5f43c0ceea","value":"{$.rawAPIRequest.commit.sha}","type":"string","structure":[]},{"id":"9ebdc940-1ed9-11ed-8015-f5fe505509e5","value":"{$.runId}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1120,"datasourcetype_guid":"0d87808f-27c0-11ea-921c-022e6b5ea1e2","snippet_guid":"9eac2bb0-1ed9-11ed-8b73-814457c25da5"},{"id":"BD72214A-6C3E-484F-BAEF-999E55F519EF","type":"SnippetBlock","disabled":false,"name":"CreateOrUpdateFileContent","displayName":"Git Hub - Create Or Update File Content","comment":"Add deploy file","childId":"0F3B39F7-5EFD-4A10-A501-CF7BA7D145E2","inputs":[{"id":"70b4a4c0-4074-11ec-a8e6-c1dc761dcfb1","value":"{ $.repoOwner }","type":"string","structure":[]},{"id":"70b5c000-4074-11ec-969e-792346f99f92","value":"{ $.repoName }","type":"string","structure":[]},{"id":"70b63220-4074-11ec-b55b-7725e494603a","value":"deployments/{$.runId}.json","type":"string","structure":[]},{"id":"b27fff40-4074-11ec-9f16-55d8428ec62c","value":"{$.createBranch.ref}","type":"string","structure":[]},{"id":"70b75130-4074-11ec-84ab-e102a3b0c185","value":"Add deployment file","type":"string","structure":[]},{"id":"70b84f80-4074-11ec-9358-b5650774d83c","value":"{base64encode: {$.deployPayload}}","type":"string","structure":[]}],"settings":[{"id":"datasource","value":"a393f260-d268-11ed-b651-5984b643ec93","type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1080,"datasourcetype_guid":"0d87808f-27c0-11ea-921c-022e6b5ea1e2","snippet_guid":"70a930c0-4074-11ec-9bb6-b36e27de5d04"},{"id":"727536F8-9504-4949-AAEC-3681DD769AC4","type":"EndpointBlock","disabled":false,"name":"createPullRequest","displayName":"GitHub - Create Pull Request","comment":"","childId":"E8D4732E-E344-4E66-B804-05786F63185A","inputs":[{"id":"e6e87240-1ee9-11ed-9d00-3785e1aca73f","value":"{ $.repoOwner }","type":"string","structure":[]},{"id":"e6f18960-1ee9-11ed-a46e-e3baf7e46151","value":"{ $.repoName }","type":"string","structure":[]},{"id":"e70e78b0-1ee9-11ed-89bc-3fb25bbea0b0","value":"Deploy {$.runId}: {$.getApp.attributes.name}","type":"string","structure":[]},{"id":"e7178460-1ee9-11ed-aac4-5b2648b3e3c2","value":"{$.createBranch.ref}","type":"string","structure":[]},{"id":"774a7250-1eea-11ed-a20f-79bf2609fe81","value":"main","type":"string","structure":[]},{"id":"a5267490-1eea-11ed-a4d8-f5ddd930d117","value":"Generated by automation run {$.runId}.","type":"longtext","structure":[]}],"settings":[{"id":"datasource","value":"a393f260-d268-11ed-b651-5984b643ec93","type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1560,"datasourcetype_guid":"0d87808f-27c0-11ea-921c-022e6b5ea1e2","endpoint_guid":"e6b09740-1ee9-11ed-8cef-637581512ebf","endpoint_role":"create"},{"id":"0A7659CB-6FD6-4C9B-8BC7-0025D9C2EAF4","type":"VariableBlock","disabled":false,"name":"runId","displayName":"Variable - runId","comment":"Generate a partially-random runId (job guid + random)","childId":"19CF6589-1534-471D-BA42-6F94ABEC7692","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":480,"variableGuid":"CDCC5AA1-AC17-4794-BE6F-8091860EF65B","operations":[{"id":"set_value","key":"BC1FF9F6-B1B5-4DAB-99FE-96D060020CF4","name":"Set value of { variable }","value":"{jobguid}-{randomtext: 8}"}]},{"id":"3493BD96-7CEE-48BC-82F9-9087637E13A8","type":"VariableBlock","disabled":false,"name":"deployPayload","displayName":"Variable - deployPayload","comment":"Build contents for the deploy json file","childId":"BD72214A-6C3E-484F-BAEF-999E55F519EF","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":600,"variableGuid":"69682C7D-BC52-420E-A6C0-72616246D9CE","operations":[{"id":"set_value","key":"BC1FF9F6-B1B5-4DAB-99FE-96D060020CF4","name":"Set value of { variable }","value":"{\n    \"id\":\"{$.runId}\",\n    \"name\":\"{ $.getApp.attributes.name }\",\n    \"sourceTenant\":\"{ $.inputs.sourceTenant }\",\n    \"targetTenant\":\"{ $.inputs.targetTenant }\",\n    \"targetSpaceId\":\"{ $.inputs.targetSpaceId }\",\n    \"sourceAppId\":\"{ $.inputs.sourceAppId }\"\n}"}]},{"id":"D30C9F25-FBD3-4B12-B55F-2861D0A9A772","type":"FormBlock","disabled":false,"name":"inputs","displayName":"Inputs","comment":"Require user inputs for deployment params","childId":"F9AED707-92E1-4E45-B502-AF9A1B0F6E64","inputs":[],"settings":[{"id":"persist_data","value":"yes","type":"select","displayValue":"Yes","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-436,"y":206,"form":[{"id":"inputs-input-0","label":"sourceTenant","helpText":"The path to the tenant from which the app is being exported, e.g. `source.eu.qlikcloud.com`.","type":"input","values":null,"isRequired":true,"options":{},"order":0},{"id":"inputs-input-1","label":"targetTenant","helpText":"The path to the tenant to which the app is being imported, e.g. `target.eu.qlikcloud.com`.","type":"input","values":null,"isRequired":true,"options":{},"order":1},{"id":"inputs-input-2","label":"sourceAppId","helpText":"The ID of the application being exported from the sourceTenant, e.g. `946d5af4-e089-42d3-9ba7-1d21adb68472`.","type":"input","values":null,"isRequired":true,"options":{},"order":2},{"id":"inputs-input-3","label":"targetSpaceId","helpText":"The ID of the space on the targetTenant into which the app will be imported, e.g. `64abe07168324a95cc4eccc9`.","type":"input","values":null,"isRequired":true,"options":{},"order":3}],"persistData":"yes"},{"id":"3DD1FE61-35F7-4017-9980-BC194CD124A9","type":"EndpointBlock","disabled":false,"name":"getApp","displayName":"Qlik Platform Operations - Get App","comment":"Retrieve the app metadata","childId":"7C4B9A14-BFA9-4DCE-9D3D-47C1A40B50F4","inputs":[{"id":"c22f5e00-d2e9-11ed-95ca-4984fc043633","value":"{ $.GetTenantNameAndRegion }","type":"string","structure":[]},{"id":"c228f500-d2e9-11ed-b72f-0dd96429cc49","value":"{ $.inputs.sourceAppId }","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-380,"y":82,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"c217ba80-d2e9-11ed-b24d-f13f5583f119","endpoint_role":"get"},{"id":"F9AED707-92E1-4E45-B502-AF9A1B0F6E64","type":"SnippetBlock","disabled":false,"name":"GetTenantNameAndRegion","displayName":"Qlik Platform Operations - Get Tenant Name And Region","comment":"","childId":"3DD1FE61-35F7-4017-9980-BC194CD124A9","inputs":[{"id":"575d1740-b1e2-11ed-958a-598edfec33b8","value":"{ $.inputs.sourceTenant }","type":"string","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-327,"y":148,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"bd5c1ce0-ad14-11ed-83f6-1d42e53790dd"},{"id":"A86CFD38-73D8-46AD-8A39-4D66753C4E0B","type":"VariableBlock","disabled":false,"name":"repoOwner","displayName":"Variable - repoOwner","comment":"Set the GitHub repository owner","childId":"B51B4743-96FB-4A8E-AE7C-2D4174ACCC38","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":120,"variableGuid":"D7B747F9-2117-4718-A50B-09FF89181684","operations":[{"id":"set_value","key":"BC1FF9F6-B1B5-4DAB-99FE-96D060020CF4","name":"Set value of { variable }","value":"withdave"}]},{"id":"B51B4743-96FB-4A8E-AE7C-2D4174ACCC38","type":"VariableBlock","disabled":false,"name":"repoName","displayName":"Variable - repoName","comment":"Set the GitHub repository name","childId":"D30C9F25-FBD3-4B12-B55F-2861D0A9A772","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":250,"y":120,"variableGuid":"64A1AD30-782F-4129-A5C3-4E9306870F00","operations":[{"id":"set_value","key":"BC1FF9F6-B1B5-4DAB-99FE-96D060020CF4","name":"Set value of { variable }","value":"qlik-app-migrator"}]},{"id":"0F3B39F7-5EFD-4A10-A501-CF7BA7D145E2","type":"SnippetBlock","disabled":false,"name":"CreateOrUpdateFileContent2","displayName":"Git Hub - Create Or Update File Content 2","comment":"Add copy of deployed resource","childId":"727536F8-9504-4949-AAEC-3681DD769AC4","inputs":[{"id":"70b4a4c0-4074-11ec-a8e6-c1dc761dcfb1","value":"{ $.repoOwner }","type":"string","structure":[]},{"id":"70b5c000-4074-11ec-969e-792346f99f92","value":"{ $.repoName }","type":"string","structure":[]},{"id":"70b63220-4074-11ec-b55b-7725e494603a","value":"deployments/{$.runId}.qvf","type":"string","structure":[]},{"id":"b27fff40-4074-11ec-9f16-55d8428ec62c","value":"{$.createBranch.ref}","type":"string","structure":[]},{"id":"70b75130-4074-11ec-84ab-e102a3b0c185","value":"Add template QVF","type":"string","structure":[]},{"id":"70b84f80-4074-11ec-9358-b5650774d83c","value":"{ $.ExportAppToBase64EncodedFile }","type":"string","structure":[]}],"settings":[{"id":"datasource","value":"a393f260-d268-11ed-b651-5984b643ec93","type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":250,"y":1080,"datasourcetype_guid":"0d87808f-27c0-11ea-921c-022e6b5ea1e2","snippet_guid":"70a930c0-4074-11ec-9bb6-b36e27de5d04"},{"id":"7C4B9A14-BFA9-4DCE-9D3D-47C1A40B50F4","type":"SnippetBlock","disabled":false,"name":"ExportAppToBase64EncodedFile","displayName":"Qlik Platform Operations - Export App To Base 64 Encoded File","comment":"Export an empty copy of the app to version","childId":"0A7659CB-6FD6-4C9B-8BC7-0025D9C2EAF4","inputs":[{"id":"d426c290-9af1-11ed-9b71-c99af7f97e39","value":"{ $.GetTenantNameAndRegion }","type":"string","structure":[]},{"id":"ca854070-fc5a-11ec-8017-27122a46811b","value":"{ $.inputs.sourceAppId }","type":"string","structure":[]},{"id":"6251d660-ca35-11ed-be4b-a5921229ac8e","value":"true","type":"select","displayValue":"true","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-342,"y":650,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","snippet_guid":"ca7c1640-fc5a-11ec-9506-815ae94ddd6e"},{"id":"E8D4732E-E344-4E66-B804-05786F63185A","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"","childId":null,"inputs":[{"id":"input","value":"Distribution {$.runId} landed in [{$.createPullRequest.html_url}]({$.createPullRequest.html_url}).","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-449,"y":995},{"id":"19CF6589-1534-471D-BA42-6F94ABEC7692","type":"EndpointBlock","disabled":false,"name":"rawAPIRequest","displayName":"GitHub - Raw API Request","comment":"","childId":"EE90CC59-4183-469E-B950-26D3297437A2","inputs":[{"id":"8f4de2b0-3022-11ec-a5b4-87316230bddd","value":"repos/{$.repoOwner}/{$.repoName}/branches/main","type":"string","structure":[]},{"id":"25ffbea0-3023-11ec-8c1e-09eaa54261e0","value":"fcadbef0-324e-11ec-8b03-31990722a432","type":"select","displayValue":"GET","structure":[]},{"id":"8f549300-3022-11ec-9d26-d9caac715625","value":null,"type":"object","mode":"keyValue","structure":[]},{"id":"ea0065a0-3254-11ec-9f49-73f027588309","value":null,"type":"object","mode":"keyValue","structure":[]}],"settings":[{"id":"datasource","value":null,"type":"select","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-422,"y":1308,"datasourcetype_guid":"0d87808f-27c0-11ea-921c-022e6b5ea1e2","endpoint_guid":"8f260cf0-3022-11ec-9ab9-598ae95629cc","endpoint_role":"get"}],"variables":[{"guid":"CDCC5AA1-AC17-4794-BE6F-8091860EF65B","name":"runId","type":"string"},{"guid":"69682C7D-BC52-420E-A6C0-72616246D9CE","name":"deployPayload","type":"string"},{"guid":"64A1AD30-782F-4129-A5C3-4E9306870F00","name":"repoName","type":"string"},{"guid":"D7B747F9-2117-4718-A50B-09FF89181684","name":"repoOwner","type":"string"}]}
  ```
</details>

To configure the automation:

1. Set the value on the `Variable - repoOwner` block to your `<REPO_OWNER>`.
2. Set the value on the `Variable - repoName` block to your `<REPO_NAME>`.

This automation is currently configured to accept a series of inputs to specify
which app needs to be deployed, and to where. It can be modified to run
on a webhook based on the successful reload of an app by changing the start
block type and replacing the input with variables.

![First blocks of the webhook automation](https://qlik.dev/_astro/tpg-webhook-automation.C2eIK_9z.png)

It deploys a manifest file and an empty copy of the app to the repository, then
opens a pull request against the `main` branch.

### 4 Deploy the triggered automation

On your source tenant, navigate to the Hub and create a new blank automation.
Copy the JSON from the snippet below and paste it into the workspace window. Connect
the new blocks to the start block.

<details>
  <summary>Triggered Automation</summary>

  ```json
  {"blocks":[{"id":"9CAC3346-A933-42FA-8895-E14751E137F4","type":"StartBlock","disabled":false,"name":"Start","displayName":"Start","comment":"","childId":"50790DDF-A949-47BE-A512-60467982F8F4","inputs":[{"id":"run_mode","value":"triggered","type":"select","structure":{}},{"id":"async","value":"no","type":"select","structure":{}},{"id":"","value":null,"type":"custom","structure":{}}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":0},{"id":"50790DDF-A949-47BE-A512-60467982F8F4","type":"FormBlock","disabled":false,"name":"inputs","displayName":"Inputs","comment":"","childId":"8D129363-45F6-4F07-9252-F8F2CE2C7F5D","inputs":[],"settings":[{"id":"persist_data","value":"no","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-457,"y":214,"form":[{"id":"inputs-input-0","type":"input","label":"id","order":0,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-1","type":"input","label":"name","order":1,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-2","type":"input","label":"sourceTenant","order":2,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-3","type":"input","label":"targetTenant","order":3,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-4","type":"input","label":"targetSpaceId","order":4,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-5","type":"input","label":"sourceAppId","order":5,"values":null,"options":[],"helpText":null,"isRequired":true},{"id":"inputs-input-6","type":"input","label":"newAppId","order":6,"values":null,"options":[],"helpText":null,"isRequired":true}],"persistData":"no"},{"id":"8D129363-45F6-4F07-9252-F8F2CE2C7F5D","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"","childId":null,"inputs":[{"id":"input","value":"{ $.inputs }","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-411,"y":215}],"variables":[]}
  ```
</details>

This automation is intended to be used as a triggered automation, which exists to
catch the response from GitHub after the workflow is completed successfully.

![First blocks of the triggered automation](https://qlik.dev/_astro/tpg-triggered-automation.7XYpMed2.png)

To configure the automation:

1. Select the `Start` block and change the `Run Mode` to `Triggered`.
2. Make a note of the automation path as `<RETURN_AUTOMATION>`. This is shown in
   the properties pane for the start block as the first value after `curl`.
3. Make a note of the automation execution token as `<RETURN_AUTOMATION_TOKEN>`.
   This is also shown in the properties pane for the start block, this time as the
   value following `X-Execution-Token:`. Do not include leading or trailing spaces
   when copying this token.

![Triggered window showing the automation path and execution token](https://qlik.dev/_astro/tpg-get-trigger-details.YZLu0INp.png)

It is simple, and can be used as a starting point for adding follow-on
logic from the app import, such as publishing and replacing over any existing copies
of the app in managed spaces, sending notifications, alerts, and more.

### 5 Configure your GitHub repository

In the GitHub user interface, navigate to your repository and
select `Settings > Secrets and variables > Actions` and create the following
variables:

- `OAUTH_ID` - this is the client ID of the OAuth client with access to
  both the source and target tenant, for example `6426a04d5a9c8cad4c8cdb8c`. Use
  the value from `<CLIENT_ID>`.
- `RETURN_AUTOMATION` - this is the URL of the return automation, excluding the
  execution token, for
  example `https://mytenant.region.qlikcloud.com/api/v1/automations/e2ab0000-15b8-11ee-8d82-cd3e0d520000/actions/execute`.
  Use the value from `<RETURN_AUTOMATION>`.

Next, create the following secrets:

- `OAUTH_SECRET` - this is the client secret corresponding to the `OAUTHID`. Use
  the value from `<CLIENT_SECRET>`.
- `RETURN_AUTOMATION_TOKEN` - this is the execution token for the `RETURN_AUTOMATION`,
  for example `TRtQFltLMFJbhplTlSlPZVb9H1znmwilqBR3deUWNjwl6IcSsIiRTmxbtOb6CUy7`.
  Use the value from `<RETURN_AUTOMATION_TOKEN>`.

Next, navigate to `Settings > General > Pull Requests` and
enable `Automatically delete head branches`. This automatically removes branches
after the pull request is merged, which helps keep your repository more manageable.

You're now ready to test the process.

## Running a deployment

To deploy apps, open the *Deployment automation* and select `Run`. You will need
to provide some deployment data:

- SourceTenant: the tenant from which the app will be copied.
- TargetTenant: the tenant to which the app will be copied.
- SourceAppId: the ID of the Qlik Sense app on the source tenant.
- TargetSpaceId: the ID of the shared space on the target tenant in which to copy the app.

Press `Submit` to continue.

![Automation input window](https://qlik.dev/_astro/tpg-run-1.CFHLkpgT.png)

After the automation is complete, it will return a link to the new pull request. Click
this link to go to GitHub to review progress.

![Automation run pane finished output](https://qlik.dev/_astro/tpg-run-2.tnuNFAAj.png)

The `moveApp` workflow will have run when the pull request was opened, and once
complete the pull request is automatically merged into `main`.

![Pull request will be merged once workflow has completed successfully](https://qlik.dev/_astro/tpg-run-3.D_kdK0ce.png)

You can review the workflow by clicking the workflow status indicator on the last commit
on the pull request, or by going to the `Actions` tab on the repository. The run
steps on the workflow allow you to review which requests were sent to Qlik Cloud.

![Review of a successful workflow run](https://qlik.dev/_astro/tpg-run-4.Bz6K-XfC.png)

You can review the merge diff for every deploy on GitHub, which contains both the
deploy JSON file, and the binary file for that release.

![Merge diff for the pull request](https://qlik.dev/_astro/tpg-run-5.C1ve_4I1.png)

On the target tenant, the app will have been deployed into the specified space.

![New app landed in the target tenant](https://qlik.dev/_astro/tpg-run-6.DtFcJMLW.png)

When the `moveApp` workflow ran, it also sent a request back to the return automation,
which allows you to build follow on actions within the automation tooling.

![Metadata response landed in the return automation](https://qlik.dev/_astro/tpg-run-7.Da9Mfu-a.png)

At any time, you can go to the `Pull requests` tab in GitHub to review all previous
deployments. Successful deployments will be `Closed`, while unsuccessful or
in-progress will be `Open`.

![Merged pull requests indicate successful deployments](https://qlik.dev/_astro/tpg-pr-merged.C450Q5av.png)

## Further reading

Now you've seen how to move larger apps with the support of third-party tooling,
ensure that you have reviewed how to [deploy a Qlik Sense application to a tenant with your own code](https://qlik.dev/manage/platform-operations/deploy-content-to-a-tenant).
