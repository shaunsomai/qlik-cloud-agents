---
source: https://qlik.dev/manage/access-control/manage-roles/
last_updated: 2026-04-20T13:34:03+01:00
---

# Manage roles

> **Note:** To learn about access control in Qlik Cloud, read the [access control overview](https://qlik.dev/manage/access-control/).

Tenant roles, or security roles, are assigned to users or groups to grant them general
access to features or capabilities in the tenant. To learn more about the types of
roles available in a tenant, see the [access control overview](https://qlik.dev/manage/access-control/).

In this topic, you will retrieve a list of roles available in the tenant, and then
both assign and remove a role from a user and a group.

Assigning a role to a user or a group follows the same process, but using different
endpoints. In this example, you will assign the custom role to a user using the
[Users API](https://qlik.dev/apis/rest/users/), but groups can be assigned roles using the
[Groups API](https://qlik.dev/apis/rest/groups/).

Both default and custom roles are assigned in the same way, as all role names are
unique within a tenant.

## Prerequisites

- An access token or API key (`<ACCESS_TOKEN>`) for a user assigned the `TenantAdmin`
  role. For more information, see [Authentication](https://qlik.dev/authenticate).
- cURL for running the inline examples.

## Manage user role assignments

### Assign roles to users

**1 Retrieve the user's current assigned roles**

The Users API only supports replacement of roles. You must retrieve the
current roles assigned to the user before assigning the new role.
You can retrieve a list of users in the tenant using the [List users endpoint](https://qlik.dev/apis/rest/users/#get-v1-users).

In this example, you retrieve the user definition for the user with the subject
`user1234`:

```bash
curl -L -G "https://tenant.region.qlikcloud.com/api/v1/users" ^
--data-urlencode "filter=subject eq 'user1234'" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The response contains `assignedRoles`, which is an array of roles assigned
to the user. You will need to append the new custom role to this array:

```json
{
    "data": [
        {
            "id": "637390ec6541614d3a88d6c1",
            "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
            "clientId": "f0e92f326ac77427df155940fec39e6a",
            "status": "active",
            "subject": "user1234",
            ...
            "assignedRoles": [
                {
                    "id": "608050f7634644db3678b1a2",
                    "name": "AuditAdmin",
                    "type": "default",
                    "level": "admin"
                },
                {
                    "id": "605a1c2151382ffc836af862",
                    "name": "SharedSpaceCreator",
                    "type": "default",
                    "level": "user"
                }
            ],
            ...
            "links": {
                "self": {
                    "href": "https://tenant.region.qlikcloud.com/api/v1/users/637390ec6541614d3a88d6c1"
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://tenant.region.qlikcloud.com/api/v1/users?limit=1&filter=subject%20eq%20%22user1234%22"
        }
    }
}
```

**2 Replace the user's assigned roles**

Send a `PATCH` request to the Users API containing both the existing roles and the name
of the role that you wish to add. To find the role name, send a request to the
[List roles endpoint](https://qlik.dev/apis/rest/roles/#get-v1-roles).

Change the `<USER_ID>` value to match the `id` value from the
call to `/api/v1/users`.

In this example, you are adding the `ManagedSpaceCreator` role to this user:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/assignedRoles\",
        \"value\": [
            {
                \"name\": \"AuditAdmin\"
            },
            {
                \"name\": \"SharedSpaceCreator\"
            },
            {
                \"name\": \"ManagedSpaceCreator\"
            }
        ]
    }
]"
```

If successful, you'll receive an `HTTP 204` response with no content. The role is now
assigned to the user.

### Unassign roles from users

As with assigning a role, you must retrieve the current roles assigned to the user,
remove the role you wish to unassign, and then send a `PATCH` request to the Users API
with the updated list of roles.

If you wish to find all users assigned a particular role, you can once again
use the [List users endpoint](https://qlik.dev/apis/rest/users/#get-v1-users), this time passing
the assigned role name in the filter param:

```bash
curl -L -G "https://tenant.region.qlikcloud.com/api/v1/users" ^
--data-urlencode "filter=assignedRoles.name eq 'ManagedSpaceCreator'" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return an `HTTP 200` response with a list of users assigned the specified
role. You can then send `PATCH` requests to each user to update their assigned roles.

## Manage group role assignments

### Assign roles to groups

**1 Retrieve the group's current assigned roles**

To assign a role to a group, you must first identify the ID of the group you wish to
update, and retrieve the list of roles currently assigned to the group.
You can retrieve a list of groups in the tenant using the [List groups endpoint](https://qlik.dev/apis/rest/groups/#get-v1-groups).

Send a request to the Groups API to retrieve a list of groups in the tenant, specifying
the name of the group you wish to update in the filter param (in this case, `My Group`):

```bash
curl -L -G "https://tenant.region.qlikcloud.com/api/v1/groups" ^
--data-urlencode "filter=name eq 'My Group'" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The response will contain the `id` of the group you wish to update:

```json
{
    "data": [
        {
            "id": "6425d62641d2b80a9a0f92c3",
            "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
            "createdAt": "2023-03-30T18:34:14.006Z",
            "lastUpdatedAt": "2023-03-30T18:34:14.006Z",
            "name": "My Group",
            "status": "active",
            "idpId": "6425d61fbb406d75678f1204",
            "providerType": "idp",
            ...
            "assignedRoles": [
                {
                    "id": "608050f7634644db3678b1a2",
                    "name": "AuditAdmin",
                    "type": "default",
                    "level": "admin"
                },
                {
                    "id": "605a1c2151382ffc836af862",
                    "name": "SharedSpaceCreator",
                    "type": "default",
                    "level": "user"
                }
            ],
            ...
            "links": {
                "self": {
                    "href": "https://tenant.region.qlikcloud.com/api/v1/groups/6425d62641d2b80a9a0f92c3"
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://tenant.region.qlikcloud.com/api/v1/groups?filter=name%20eq%20%22My%20Group%22"
        }
    }
}
```

Use the `id` value for `<GROUP_ID>` in the following steps.

The response also contains `assignedRoles`, which is an array of roles assigned
to the user. You will need to append the new custom role to this array.

**2 Replace the group's assigned roles**

Send a `PATCH` request to the Groups API containing both the existing roles and the name
of the role that you wish to add. To find the role name, send a request to the
[List roles endpoint](https://qlik.dev/apis/rest/roles/#get-v1-roles).

Change the `<GROUP_ID>` value to match the `id` value from the
call to `/api/v1/groups`.

In this example, you are adding the `ManagedSpaceCreator` role to this group:

```bash
curl -L -X PATCH "https://tenant.region.qlikcloud.com/api/v1/groups/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/assignedRoles\",
        \"value\": [
            {
                \"name\": \"AuditAdmin\"
            },
            {
                \"name\": \"SharedSpaceCreator\"
            },
            {
                \"name\": \"ManagedSpaceCreator\"
            }
        ]
    }
]"
```

If successful, you'll receive an `HTTP 204` response with no content. The role is now
assigned to the group.

### Unassign roles from groups

As with assigning a role, you must retrieve the current roles assigned to the group,
remove the role you wish to unassign, and then send a `PATCH` request to the Groups API
with the updated list of roles.

If you wish to find all groups assigned a particular role, you can once again
use the [List groups endpoint](https://qlik.dev/apis/rest/groups/#get-v1-groups), this time passing
the assigned role name in the filter param:

```bash
curl -L -G "https://tenant.region.qlikcloud.com/api/v1/groups" ^
--data-urlencode "filter=assignedRoles.name eq 'ManagedSpaceCreator'" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return an `HTTP 200` response with a list of groups assigned the specified
role. You can then send `PATCH` requests to each group to update their assigned roles.
