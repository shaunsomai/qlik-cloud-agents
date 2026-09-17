---
source: https://qlik.dev/manage/platform-operations/configure-a-tenant/
last_updated: 2025-11-07T09:45:47Z
---

# Configure a tenant

## Configure a tenant

In this tutorial, you are going to configure a tenant using Qlik Cloud
management APIs so you can automate the process of analytics delivery to your
end customers.

You will configure settings which allow you to deploy content to the tenant,
as well as enable users to authenticate to the tenant and access that content.

## Code examples

Complete script examples for configuring a tenant using qlik-cli, curl,
Python, and API collections are available
in the [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations).

## Prerequisites

- You have reviewed previous tutorials in
  the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview), as this
  tutorial assumes your knowledge of concepts and steps covered earlier.
- cURL for running the inline examples.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable                | Description                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<CLIENT_ID>`           | The client ID for an OAuth client, specific to the region you're sending requests to.                                                                                                                                 |
| `<CLIENT_SECRET>`       | The client secret for the specific OAuth `<CLIENT_ID>`.                                                                                                                                                               |
| `<TARGET_TENANT>`       | The domain for the tenant you are configuring. Equivalent to `tenant.<REGION>.qlikcloud.com`.                                                                                                                         |
| `<TARGET_TENANT_ID>`    | The Qlik Cloud `id` of the tenant that you are configuring.                                                                                                                                                           |
| `<TARGET_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`.                                                                                                                                             |
| `<REGION>`              | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore and `us` for North America.                                |
| `<SHARED_SPACE_NAME>`   | The space name for the shared space you will use as the staging space when deploying content. Note that this cannot be the same as the `<MANAGED_SPACE_NAME>` as all space names should be unique.                    |
| `<SHARED_SPACE_ID>`     | The Qlik Cloud `id` for `<SHARED_SPACE_NAME>`.                                                                                                                                                                        |
| `<MANAGED_SPACE_NAME>`  | The space name for the managed spaces that you will use as the production space where users will consume content. Note that this cannot be the same as the `<SHARED_SPACE_NAME>` as all space names should be unique. |
| `<MANAGED_SPACE_ID>`    | The Qlik Cloud `id` for `<MANAGED_SPACE_NAME>`. `<MANAGED_SPACE_NAME>`                                                                                                                                                |
| `<GROUP_ID>`            | The Qlik Cloud `id` for the group that you're giving access to the `<MANAGED_SPACE_NAME>` managed space.                                                                                                              |

## Quick start

If you want to dive right into the code, all of the commands in this tutorial
are available on the
[Qlik open source software](https://github.com/qlik-oss/qlik-cloud-examples)
GitHub repository. Example commands are provided in multiple formats including
Python, cURL, and qlik-cli.

## 1 Configure entitlement and provisioning settings

There are several tenant-level settings that you may want to configure before
allowing end customers to access embedded analytics.

This tutorial provides a few examples, but to understand what else you can
configure as part of initial onboarding, review [configure tenant featuresConfigure tenant settings](https://qlik.dev/manage/tenants/tenant-features).

### Enable auto creation of groups

Security in Qlik Cloud can be applied to both users and groups. Using groups to
secure access to content and resources simplifies access management by allowing
an identity provider outside of Qlik to manage user access to Qlik resources
using group membership. As group membership changes, Qlik automatically picks up
the changes and ensures that users can only access content and resources
according to their group memberships.

To enable group management on a tenant, access
the [`/groups/settings`](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2Fsettings-patch)
endpoint and set the `autoCreateGroups` property to
`true` to permit group creation on user login, and the `syncIdpGroups` property
to `true` if you are using a compatible interactive Identity Provider and wish
groups to be synchronized:

```bash
curl -L "https://<TARGET_TENANT>/api/v1/groups/settings" ^
-X PATCH ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/autoCreateGroups\", \"value\": true},{\"op\": \"replace\", \"path\": \"/syncIdpGroups\", \"value\": true}]"
```

The response from this request is an `HTTP 204 updated` status code. There are no
additional details provided in the response.

### Set user entitlement assignment behavior

You can entitle a user either as an analyzer or a professional
user in the tenant.

- The analyzer entitlement allows a user to consume content and resources
  that they are assigned to on the tenant.

- A professional entitlement adds creator and self-service capabilities to users.

In both cases, this entitlement provides access to
content in the tenant. Tenant roles grant the entitled user additional
capabilities in the tenant. Space permissions and roles allow further
refinement to the content users and groups access depending on the location of
the content in the tenant.

> **Note:** For more information about the different user entitlements for Qlik Cloud, see [Analyzer capacity license](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/analyzer-capacity-consumption.htm)
> on Qlik Help.

To enable a tenant to automatically set users with the analyzer entitlement,
send a request to the [`/licenses/settings`](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fsettings-put) endpoint
to set the `autoAssignProfessional` property to `false` and the `autoAssignAnalyzer` to `true`:

```bash
curl -L "https://<TARGET_TENANT>/api/v1/licenses/settings" ^
-X PUT ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{\"autoAssignProfessional\":false,\"autoAssignAnalyzer\":true}"
```

## 2 Add a group to the tenant

Creating groups on the tenant helps to facilitate the setup of spaces and
security before users first log in.

Here's a cURL example that shows you how to create a group.

```bash
curl -L "https://<TENANT>/api/v1/groups" ^
-X POST ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{\"name\": \"<GROUP_NAME>\", \"status\": \"active\"}"
```

The result is a JSON object where `id` is the `<GROUP_ID>`. Keep a note of this
`<GROUP_ID>` because you will need it when you update group roles in the next section
of this tutorial.

```json
{
    "id": "<GROUP_ID>",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "createdAt": "2023-06-28T17:27:00.502Z",
    "lastUpdatedAt": "2023-06-28T17:27:00.502Z",
    "name": "<GROUP_NAME>",
    "status": "active",
    "assignedRoles": [],
    ...
}
```

## 3 Assign roles to a group

By assigning roles, space access, or section access to groups, you remove the
need to assign these to each user, but it also means that the user has immediate
access to the required content as soon as they log in, without waiting for
someone to add them to a resource.

For a description of the various security roles that can be applied to groups, see
[What is a security role](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles-capacity-model.htm)
on Qlik Help.

> **Note:** Roles are case sensitive.\
> For a full list of tenant roles, refer to the [List Roles](https://qlik.dev/apis/rest/roles/#%23%2Fentries%2Fv1%2Froles-get) endpoint.\
> For a full list of space roles, retrieve the space using the [List Spaces](https://qlik.dev/apis/rest/spaces/#%23%2Fentries%2Fv1%2Fspaces-get) endpoint.

Here's a cURL example that shows you how to assign the `AuditAdmin` and
`AnalyticsAdmin` roles to the group you created in the previous step using the
group ID.

```bash
curl -L "https://<TENANT>/api/v1/groups/<GROUP_ID>" ^
-X PATCH ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "[{\"op\": \"replace\", \"path\": \"/assignedRoles\", \"value\": [ {\"name\": \"AuditAdmin\"}, {\"name\": \"AnalyticsAdmin\" }]}]"
```

The response from this request is an `HTTP 204` status code. There are no
additional details provided in the response.

## 4 Create spaces in a tenant

A space allows you to define access control rules based on users or groups for the content
contained within the space. There are three types of spaces in a tenant: personal, shared,
and managed spaces.

- Personal spaces reference content only the owner can access. They are not used
  in embedded use cases.
- Shared spaces enable multiple users to collaborate on content creation. Put
  another way, shared spaces are the main branch for the analytics content
  deployed to a tenant.
- Managed spaces represent the release area for analytics content. When content is
  published to a managed space, the main content, business logic, and content code
  cannot be manipulated.

Access to spaces and their content can be provided to named users in a tenant or
through group membership. To learn more about spaces, see
[Working in spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm)
on Qlik Help.

Implementing a shared space for staging deployed content and a managed space to
support release consumption is a good design pattern for embedded analytics.
Here's how to programmatically create spaces and set access control on them.

### Create the shared space

Creating a shared space uses the [Spaces API](https://qlik.dev/apis/rest/spaces).
The request for space creation requires a `name` for the space and a `type` for
the space, which is either `shared` or `managed`. You may add a description for
the space in this request using the `description` attribute.

```bash
curl -L "https://<TARGET_TENANT>/api/v1/spaces" ^
-X POST ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"<SHARED_SPACE_NAME>\", \"description\": \"none\", \"type\": \"shared\"}"
```

The JSON response when a space is created on a tenant includes metadata
describing the access control available on the space. Make note of the space
`id` as `<SHARED_SPACE_ID>` as you may need this later to assign groups and permissions.

```json
{
  "id": "<SHARED_SPACE_ID>",
  "type": "shared",
  "ownerId": "00cbb22c600e823ed278d5e3d976f85a",
  "tenantId": "<TARGET_TENANT_ID>",
  "name": "<SHARED_SPACE_NAME>",
  "description": "none",
  "meta": {
    "actions": ["create", "delete", "read", "update"],
    "roles": [],
    "assignableRoles": ["consumer", "dataconsumer", "facilitator", "producer"]
  },
  "links": {"..."},
  "createdAt": "2022-06-17T12:55:11.574Z",
  "createdBy": "00cbb22c600e823ed278d5e3d976f85a",
  "updatedAt": "2022-06-17T12:55:11.574Z"
}
```

By default, the creator of a space has full access to that space. As this use case
leverages the shared space as a staging area for your content prior to publishing
to the managed space, you will not assign any additional users or groups at this stage.
This is because the API user will be the only user accessing
the space, and as that user created the space, it already has full access.

### Create the managed space

Creating a managed space uses the same Spaces API with the same format as the shared space request,
but the type value sent in the request is `managed`.

```bash
curl -L "https://<TARGET_TENANT>/api/v1/spaces" ^
-X POST ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"<MAMAGED_SPACE_NAME>\", \"description\": \"none\", \"type\": \"managed\"}"
```

The JSON response when you create a managed space is exactly the same as a
shared space, but with slightly different metadata including the `type` set to
`managed`.

```json
{
  "id": "<MANAGED_SPACE_ID>",
  "type": "managed",
  "ownerId": "00cbb22c600e823ed278d5e3d976f85a",
  "tenantId": "<TARGET_TENANT_ID>",
  "name": "<MANAGED_SPACE_NAME>",
  "description": "none"
}
```

Record the `id` attribute of the managed space as `<MANAGED_SPACE_ID>`
for adding a group to the space.

### Add a group to a managed space with the consumer role

Access control in spaces is set by adding members (users or groups) to the space
and [assigning them permissions tied to roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-managed-spaces.htm).

> **Note:** Some space permissions may also depend on the user also having the appropriate license allocated, and the user or
> group having any [specific roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles.htm)
> assigned.

To provide a group whose users have permission to act as a consumer on a managed
space you need:

- The `id` of the group or groups you want to assign permissions (`<GROUP_ID>`).
- The `id` of the managed space to assign the group (`<MANAGED_SPACE_ID>`).

### Add a group and assign it a role on the managed space

Assigning a group and the role permissions of that group to a space uses
the [/assignments endpoint](https://qlik.dev/apis/rest/spaces/#post-api-v1-spaces-spaceId-assignments).
The JSON payload for the request requires `type`, `assigneeId`, and
`roles` attributes. The `assigneeId` attribute value should be the group `id`.
In this example you will set the `consumer` role, which permits the specified group
the ability to consume analytics, but not any editing or self-service capabilities.

```json
{
  "type": "group",
  "assigneeId": "<GROUP_ID>",
  "roles": ["consumer"]
}
```

The request path contains the `id` of the managed space that you created in the previous step.

```bash
curl -L "https://<TARGET_TENANT>/api/v1/spaces/<MANAGED_SPACE_ID>/assignments" ^
-X POST ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json" ^
-d "{\"type\": \"group\", \"assigneeId\": \"<GROUP_ID>\", \"roles\": [\"consumer\"]}"
```

The JSON response from the tenant confirms the assignment of the group to the
managed space was successful.

```json
{
  "id":"626ff52f7ca0dba484332c21",
  "type":"group",
  "assigneeId":"<GROUP_ID>",
  "roles":["consumer"],
  "spaceId":"<MANAGED_SPACE_ID>",
  "tenantId":"<TARGET_TENANT_ID>",
  "createdAt":"2022-05-02T15:13:51.12Z",
  "createdBy":"00cbb22c600e823ed278d5e3d976f85a",
  "updatedAt":"2022-05-02T15:13:51.12Z",
  "links":{"..."}
}
```

## Next steps

With your tenant, IdP, and spaces ready to go, the stage is set
for [deploying content to your tenant](https://qlik.dev/manage/platform-operations/deploy-content-to-a-tenant).
