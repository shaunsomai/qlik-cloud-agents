---
source: https://qlik.dev/manage/access-control/groups/
last_updated: 2026-04-20T13:34:03+01:00
---

# Manage users with groups

> **Note:** To learn about access control in Qlik Cloud, read the [access control overview](https://qlik.dev/manage/access-control/).

Groups are used for access control and sharing of content in Qlik Cloud. They are most commonly populated from your
Identity Provider, either as users log in or via SCIM if you are using a compatible Identity Provider such as Azure AD.

There are three types of groups within Qlik Cloud:

- Identity Provider managed groups: these groups are created by your Identity Provider as users log in or manually via
  APIs.
- Custom groups: these user-defined groups are created and managed within the Qlik Cloud tenant.
- Qlik system groups: these groups are created and managed by Qlik. For example, the "Everyone" group automatically
  contains every user in the tenant.

## Overview of groups

Groups enable tenant administrators to manage permissions based on group memberships. You can assign security roles and
space roles to Identity Provider managed groups and custom groups to control permissions across the tenant.

### Identity Provider managed groups

Identity Provider managed groups are synchronized with your Identity Provider. Deleting these groups from a tenant
will not prevent them from reappearing. You will need to update your Identity Provider configuration to filter these
groups out of user claims before they are sent to Qlik Cloud. For more information on configuring Identity Providers,
see [Identity providers in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm)
on Qlik Help.

Using Identity Provider managed groups delegates the majority of access control in the platform to your Identity
Provider. Any Identity Provider managed group created in your tenant via API relies on relationships passed via the
user's claims from the Identity Provider.

> **Note:** Identity Provider managed groups must be passed in a valid claim from your chosen Identity Provider to be
> associated with a user. You cannot manage the relationship between users and these groups in Qlik Cloud.

### Custom groups

Custom groups can be created, updated, and deleted entirely using Qlik APIs. Tenant administrators can create, edit,
delete, and manage custom groups. Both Qlik Account users and users provisioned from Identity Providers can be added to
custom groups.

> **Considerations for using custom groups:**
>
> - You can create a custom group with the same name as an existing Identity Provider managed group, but not another custom group. You can also create an Identity Provider managed group with the same name as an existing custom group. The differentiator between group types is the prefix (Custom or IDP).
> - To avoid confusion, it is recommended to use unique group names. For example, you can prefix custom group names with `CG-` to distinguish them easily.
> - Identity Provider managed groups and custom groups have different icons in the user interface, making it easier to distinguish between them.
>
>   ![A screenshot of the user interface showing an Identity Provider managed group and a custom group with their respective icons](https://qlik.dev/_astro/custom-idp-groups-ui.C16mPcTK.png)
> - Custom groups support Section Access. For more information, see [Managing data security with Section Access](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm) on Qlik Help.

### Qlik system groups

Qlik system groups are created and managed by Qlik. You cannot delete them or update their membership, name, and other
properties.

## Prerequisites

- You have a basic understanding of Qlik Cloud and its access control rules for
  creating content and managing spaces.
- cURL for running the inline examples.
- [qlik-cli@1.5.0](https://qlik.dev/toolkits/qlik-cli) or greater if running qlik-cli commands.

> **Note:** The cURL examples in this topic show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables are used as placeholder values.
The variable substitution format is `<VARIABLE_NAME>`.
The following table lists the variables referenced in this tutorial.

| Variable         | Description                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`       | The URL of the tenant where you are setting up a new group. Equivalent to `tenanthostname.region.qlikcloud.com`.                              |
| `<ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<GROUP_NAME>`   | The name of the group.                                                                                                                        |
| `<GROUP_ID>`     | The unique identifier of the group.                                                                                                           |
| `<USER_ID>`      | The unique identifier of the user.                                                                                                            |

## Create a custom group and assign a role to it

Creating groups on the tenant facilitates the setup of spaces and security before users first log in.
By assigning roles, space access, or section access to groups, you remove the need to assign these to each user.
This also means that the user has immediate access to the required content as soon as they log in, without waiting for
someone to add them to a resource.

For a description of the various security roles that can be applied to groups, see
[Assigning security roles and custom roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles-capacity-model.htm)
on Qlik Help.

> **Notes:**
>
> - Roles are case sensitive.
> - For a full list of tenant roles, refer to the [List Roles](https://qlik.dev/apis/rest/roles/#get-v1-roles) endpoint.
> - For a full list of space roles, retrieve the space using the [List Spaces](https://qlik.dev/apis/rest/spaces/#get-v1-spaces)
>   endpoint.

The following cURL example shows you how to create a custom group and assign the `AuditAdmin` role to it:

```bash
curl -L "https://<TENANT>/api/v1/groups" ^
-X POST ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{\"name\": \"<GROUP_NAME>\", \"status\": \"active\", \"providerType\": \"custom\", \"assignedRoles\": [{\"name\": \"AuditAdmin\"}]}"
```

The API returns a JSON object containing the details of the created group. The `id` field corresponds to the `<GROUP_ID>`.
You will need this `<GROUP_ID>` to update group roles in the next section of this tutorial.

```json
{
    "id": "649c6d64cf28896726e572ae",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "createdAt": "2025-01-24T17:34:46.210Z",
    "lastUpdatedAt": "2025-01-24T17:34:46.210Z",
    "name": "<GROUP_NAME>",
    "status": "active",
    "providerType": "custom",
    "createdBy": "67890d4f54978fef2caa2df5",
    "updatedBy": "67890d4f54978fef2caa2df5",
    "assignedRoles": [
        {
            "id": "608050f7634644db3678b1a2",
            "name": "AuditAdmin",
            "type": "default",
            "level": "admin"
        }
    ],
    ...
}
```

## List groups

Once you have the ID of a group, you can update its roles, assign it to spaces,
or use it with section access.

> **Note:** The *List Groups* endpoint does not return Identity Provider managed, custom, and Qlik system groups in the same
> response. To retrieve all groups in the  tenant, you will need to make two separate API calls.

### List Identity Provider managed and custom groups

To retrieve groups that have been created via API calls or your Identity Provider,
you can leverage all available filters on the [List Groups](https://qlik.dev/apis/rest/groups/#get-v1-groups) endpoint, with
`systemGroups` left blank or set to `false`.

```bash
curl -L "https://<TENANT>/api/v1/groups" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

This will return only the Identity Provider managed and custom groups in the tenant.

### List Qlik system groups

To retrieve system groups, use the same *List Groups* endpoint but
set `systemGroups` to `true`. No other filters can be applied when using this parameter.

```bash
curl -L "https://<TENANT>/api/v1/groups?systemGroups=true" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

This will return the system groups, which have present names and IDs that are
the same across all tenants. For example, the *Everyone* group manifests as:

```json
{
    "data": [
        {
            "id": "000000000000000000000001",
            "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
            "createdAt": "2023-05-25T07:52:58.816Z",
            "lastUpdatedAt": "2023-05-25T07:52:58.816Z",
            "name": "com.qlik.Everyone",
            "status": "active",
            "assignedRoles": [],
            ...
        }
    ],
    ...
}
```

Assigning a role to the *Everyone* group will provide that capability to all users in
the tenant.

## Update roles assigned to a group

This step shows you how to replace any existing group assignments
with two new assignments for `TenantAdmin` and `AuditAdmin`. It is
not possible to add or remove individual roles from a group.

```bash
curl -L "https://<TENANT>/api/v1/groups/<GROUP_ID>" ^
-X PATCH ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/assignedRoles\", \"value\": [ {\"name\": \"TenantAdmin\"}, {\"name\": \"AuditAdmin\" }]}]"
```

The response from this request is an HTTP `204` status code, indicating that the update was successful.
There are no additional details provided in the response.

## Add and remove users from custom groups

You can manage custom group membership for a user using the user's `assignedGroups` property with `PATCH`
operations on the user resource. These operations modify the list of group IDs or named groups assigned
to a user. For both `add` and `replace` operations, you can reference custom groups by name
and `providerType=custom` instead of by ID.

> **Caution:**
>
> - You cannot add or remove Identity Provider (IdP) managed group memberships via this API.
>   These memberships are controlled by the IdP and attempts to modify them return an HTTP `400` status code.
> - Adding a custom group that the user already has returns an HTTP `400` status code and no changes are applied.

### Add custom groups to a user

Use `op: "add"` with the JSON Patch array index `-` to append one or more custom group IDs
to a user's `assignedGroups`.
This operation appends to the existing list without removing any current group memberships.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-d "[
  {
    \"op\": \"add\",
    \"path\": \"/assignedGroups/-\",
    \"value\": \"<GROUP_ID_1>\"
  },
  {
    \"op\": \"add\",
    \"path\": \"/assignedGroups/-\",
    \"value\": \"<GROUP_ID_2>\"
  }
]"
```

This example appends two custom group IDs to the user's existing `assignedGroups` array.

### Remove a custom group from a user

To remove a specific custom group from a user's membership, use the `remove-value` operation and
provide the custom group ID you want to remove.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-d "[
  {
    \"op\": \"remove-value\",
    \"path\": \"/assignedGroups\",
    \"value\": \"<GROUP_ID>\"
  }
]"
```

### Replace a user's assigned groups

You can replace the user's entire `assignedGroups` list with a new array of group objects or named groups.
This is useful when you want to enforce a specific set of group memberships.

> **Caution:** If the user has Identity Provider (IdP) managed groups, a full `replace` may fail because you might not have
> permission to remove IdP-managed memberships.
> In that case prefer `add` and `remove-value` operations to change membership incrementally.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-d "[
  {
    \"op\": \"replace\",
    \"path\": \"/assignedGroups\",
    \"value\": [
      { \"id\": \"<GROUP_ID>\" }
    ]
  }
]"
```

### Use named group objects when adding or replacing

For both `add` and `replace` operations, you can reference groups by name and `providerType` instead of by ID.
This is especially useful in automation where groups are created and assigned in the same workflow.
Always use `providerType: "custom"` for tenant-created groups.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-d "[
  {
    \"op\": \"replace\",
    \"path\": \"/assignedGroups\",
    \"value\": [
      {
        \"name\": \"My Custom group Name\",
        \"providerType\": \"custom\"
      }
    ]
  }
]"
```

## Delete a group

You can delete Identity Provider managed groups in your tenant. If you have enabled
**Automatic group creation on login**, these groups will be recreated the next time a user with that group in their
claims logs in.

You can also delete custom groups in your tenant, but only if no users are assigned to the group.

To delete a group, first retrieve the group ID using the *List Groups* endpoint. Then, use the following API call:

```bash
curl -L "https://<TENANT>/api/v1/groups/<GROUP_ID>" ^
-X DELETE ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

The response from this request is an HTTP `204` status code, indicating that the deletion was successful.
There are no additional details provided in the response.

## Delete all groups

You may also need to remove all groups in a tenant to support scenarios
such as when your Identity Provider has sent:

- GUIDs rather than friendly group names
- All groups, rather than groups related to Qlik Cloud
- Groups that you need to remove prior to configuring a different Identity Provider

![a screenshot of a group with a guid in the list of
friendly group names](https://qlik.dev/_astro/guid-groups.D_5qLtsL.png)

You are going to learn how to use qlik-cli in PowerShell and Automate
to delete one or more unwanted groups.

<details>
  <summary>Delete all groups (powershell/qlik-cli)</summary>

  This script deletes all groups in the tenant using
  the [group ls](/toolkits/qlik-cli/group/group-ls) command.

  ```powershell
  # Retrieve the list of groups
  $groups=$(qlik group ls --limit 1000) | ConvertFrom-Json

  # Write out count of groups returned
  Write-Host $groups.count "groups returned."

  # Loop over each group if you have more than 0
  if ($groups.count -ne 0) {

      $groups | ForEach {

          $group = $_.id
          Write-Host "Deleting group" $_.name
          $deleteResponse=$(qlik group rm $_.id)
      }
  } else {
      Write-Host "No groups found."
  }
  ```
</details>

<details>
  <summary>Delete matching groups (powershell/qlik-cli)</summary>

  This script deletes groups in the tenant that match specific criteria using
  the [group filter](/toolkits/qlik-cli/group/group-filter) command.

  ```powershell
  # Retrieve the list of groups
  $groups=$(qlik group filter --filter 'name eq ""DeleteMeGroup""' --limit 1000) | ConvertFrom-Json

  # Write out count of groups returned
  Write-Host $groups.count "groups returned."

  # Loop over each group if you have more than 0
  if ($groups.count -ne 0) {

      $groups | ForEach {

          $group = $_.id
          Write-Host "Deleting group" $_.name
          $deleteResponse=$(qlik group rm $_.id)
      }
  } else {
      Write-Host "No groups found."
  }
  ```
</details>

<details>
  <summary>Delete all groups (no-code)</summary>

  If you prefer no-code methods, consider leveraging [no-code tools](/toolkits/no-code/) such as the *Qlik Cloud* or
  *Platform Operations* connectors in Automate.

  This example will loop over every group in the tenant running the automation
  and delete each group as it goes.

  <Image
    src={groupautomation}
    alt="a screenshot of an automation that deletes all
groups in a tenant"
    style="display:block; margin-left: auto; margin-right: auto;"
  />

  To recreate this automation, copy the snippet below and paste it into an
  automation workspace in edit mode.

  `embed:./snippets/qlik-cli-snippets-manage-groups/automation-delete-all-groups.json`
</details>
