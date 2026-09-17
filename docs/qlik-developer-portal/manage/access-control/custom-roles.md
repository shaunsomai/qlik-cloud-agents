---
source: https://qlik.dev/manage/access-control/custom-roles/
last_updated: 2026-04-20T13:34:03+01:00
---

# Manage custom roles

> **Note:** To learn about access control in Qlik Cloud, read the [access control overview](https://qlik.dev/manage/access-control/).

[Custom roles and the User Default role](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes.htm)
allow you to create and assign specific scopes to users or groups, providing
more granular control than the built-in roles alone.

In this topic, you will create a new custom role, assign scopes to it,
assign the role to a user, update assigned scopes, then delete the role to demonstrate
a full lifecycle for a custom role.

## Prerequisites

- An access token or API key (`<ACCESS_TOKEN>`) for a user assigned the `TenantAdmin`
  role. For more information, see [Authentication](https://qlik.dev/authenticate).
- cURL for running the inline examples.

## Create a custom role

When creating a new custom role, it is possible to assign scopes at the point of creation.
In this example, you will assign just two scopes from the [scopes which support
custom roles](https://qlik.dev/manage/access-control/scopes), which means the role will provide assigned
users or groups with image and PDF export from Qlik Sense, and AutoML model approval.

```bash
curl -L "https://tenant.region.qlikcloud.com/api/v1/roles" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"name\": \"My first custom role\",
    \"description\": \"This is the first custom role created via API\",
    \"assignedScopes\": [
        \"automl-models:approve\",
        \"apps.image:export\"
    ]
}"
```

If successful, you'll be returned an `HTTP 201` response with the following body:

```json
{
    "id": "6724d8f5a4acfa155351afa7",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "name": "My first custom role",
    "description": "This is the first custom role created via API",
    "type": "custom",
    "canEdit": true,
    "canDelete": true,
    "fullUser": false,
    "userEntitlementType": "",
    "level": "user",
    "assignedScopes": [
        "automl-models:approve",
        "apps.image:export"
    ],
    "permissions": [],
    "createdAt": "2024-11-01T13:34:45.511Z",
    "lastUpdatedAt": "2024-11-01T13:34:45.511Z",
    "createdBy": "637390ec6541614d3a88d6c1",
    "updatedBy": "637390ec6541614d3a88d6c1",
    "links": {
        "self": {
            "href": "https://tenant.region.qlikcloud.com/api/v1/roles/6724d87be21e7c1194a9e1a7"
        }
    }
}
```

Note the `id` value in the response, as this will be needed for the update and delete
steps later on as `<ROLE_ID>`.

## Assign the custom role to a user

Assigning a role to a user or a group follows the same process, but using different
endpoints. Review the tutorial on [assigning roles](https://qlik.dev/manage/access-control/manage-roles/)
to learn how to assign roles.

## Modify role scopes

If you need to amend the scopes assigned to a role, you can use the
[update role endpoint](https://qlik.dev/apis/rest/roles#patch-v1-roles-id) with JSON Patch operations.

This applies to both custom roles and the `UserDefault` role.

The role you created earlier has the following definition:

```json
"assignedScopes": [
    "automl-models:approve",
    "apps.image:export"
]
```

### Replace scopes

To update the assigned scopes by replacing the entire list, use the `replace` operation.
This is useful when you need to perform bulk updates or set the complete scope configuration.

For example, to remove autoML approval permissions from the previous example role and keep only `apps.image:export`,
use the following request:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/roles/<ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/assignedScopes\",
        \"value\": [
            \"apps.image:export\"
        ]
    }
]"
```

If successful, you'll receive an `HTTP 204` response with no content.

### Add a scope

If you want to add a single scope to an existing role without needing to fetch and manage the complete scope list,
use the `add` operation.
For example, to add the `api-keys` scope to the role while keeping existing scopes, use the following request:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/roles/<ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"add\",
        \"path\": \"/assignedScopes/-\",
        \"value\": \"api-keys\"
    }
]"
```

### Remove a scope (remove specific scopes)

To remove a specific scope from a role without replacing the entire list, use the `remove-value` operation.
For example, to remove autoML approval permissions while keeping all other assigned scopes:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/roles/<ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"remove-value\",
        \"path\": \"/assignedScopes\",
        \"value\": \"automl-models:approve\"
    }
]"
```

### Update the scope of the UserDefault role

The `UserDefault` role can be modified using the same operations.
This allows you to set baseline permissions for all users in your tenant.

1. Retrieve the `UserDefault` role ID:

```bash
curl -L "https://tenant.region.qlikcloud.com/api/v1/roles" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json"
```

2. Find the role with `"type": "default"` and `"name": "UserDefault"`.

3. Use its `id` in the same PATCH requests shown previously.
   For example, to add the `notes` scope to all users without modifying their existing scopes, use the `add` operation:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/roles/<USERDEFAULT_ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"add\",
        \"path\": \"/assignedScopes/-\",
        \"value\": \"notes\"
    }
]"
```

## Delete the custom role

Before deleting a custom role, you must ensure that no users or groups are assigned it.
Attempting to delete an assigned role will result in an `HTTP 403` response. Review
the tutorial on [assigning roles](https://qlik.dev/manage/access-control/manage-roles/) to learn how to unassign
roles.

Once no users or groups are assigned the role, you can delete it using a `DELETE` call:

```bash
curl -L -X DELETE "https://tenant.region.qlikcloud.com/api/v1/roles/<ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

If successful, you'll receive an `HTTP 204` response with no content. The role is now deleted.
