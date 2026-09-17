---
source: https://qlik.dev/manage/platform-operations/add-an-interactive-user-to-a-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Add an interactive user to a tenant

## Add an interactive Qlik Account user to a tenant

If your Qlik Cloud entitlement includes multiple-tenant creation and
provisioning capabilities, you can create tenants programmatically. You may want
to access the tenant interactively through a browser to validate the
configuration or provide administrative support to your end customers,
but programmatically provisioned tenants do not have native support for
interactive login.

In this tutorial, you are going to add an existing `Qlik Account` user
by copying the user details from an existing
source tenant to a new target tenant that you've created programmatically.

If you prefer, you can use the [user invite](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers%2Factions%2Finvite-post)
endpoint to invite users, and then use the [user update](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers%2F-userId-patch)
endpoint to update the user's `status` to `active`. If you invite a user but
do not change the `status` value to `active`, the invite will expire.

## Context: Qlik Account & Interactive Identity Providers (IdPs)

By default, Qlik Cloud tenants in public regions take advantage of the
`Qlik Account` IdP. `Qlik Account` is a central authentication mechanism to access
properties within the qlik.com and qlikcloud.com domains. The email address for
which you received the welcome email to create a tenant is a member of
`Qlik Account`.

Because your `Qlik Account` works across qlikcloud.com domains, you can add your
identity to tenants you control through your entitlement and valid OAuth
credentials. Specifically, you can uniquely identify your `Qlik Account` by
it's `subject`.

Each Qlik Cloud tenant supports 1 interactive IdP. If you deploy your own interactive
IdP, then this will replace the `Qlik Account` IdP in that tenant.

If you wish to use the provided tenant recovery options (via `/login/recover`)
then you must ensure you have at least 1 Qlik Account user provisioned to the tenant
with the `TenantAdmin` role assigned directly to that user. Qlik Account does not
provide the option for using groups.

For more information on Qlik Cloud IdP configurations, including how to map
`Qlik Account` users to another IdP, see
[Identity Providers in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm)
on Qlik Help.

## Prerequisites

- You have reviewed previous tutorials in
  the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview), as this tutorial assumes your knowledge
  of concepts and steps covered earlier.
- You have not yet configured your own interactive IdP
  on the target tenant (this is because the tutorial uses `Qlik Account`,
  and adding a new OIDC IdP will replace `Qlik Account` as the default login
  flow on the tenant).
- cURL for running the inline examples.

For this guide, you will be looking up the `subject` for a user on a tenant created
via My Qlik during the [Create a tenant tutorial](https://qlik.dev/manage/platform-operations/create-a-tenant), referred to as the
`source` tenant.
You will then add this user information to the `target` tenant.

It is also possible to add users to the tenant for use with your own IdP, but this
is outside the scope of this tutorial.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable                | Description                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`       | The domain for the initial tenant created during account onboarding. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                                                           |
| `<TARGET_TENANT>`       | The domain for the new tenant that this tutorial will create. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                                                                  |
| `<REGION>`              | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore and `us` for North America.                                |
| `<SOURCE_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<SOURCE_TENANT>`. Refer to the [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant) tutorial for guidance on generating this token. |
| `<TARGET_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`. Refer to the [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant) tutorial for guidance on generating this token. |
| `<EMAIL_ADDRESS>`       | The email address of the user that you are adding to the target tenant.                                                                                                                                               |
| `<IDP_SUBJECT>`         | A unique identifier for the user from the target tenant's IdP.                                                                                                                                                        |
| `<USER_NAME>`           | The friendly name associated with the email address and subject combination.                                                                                                                                          |

## 1 Obtain the user subject by email on the source tenant

Use the `<SOURCE_ACCESS_TOKEN>` to request the user information for the user you
want to add to the target tenant from
the [Users API](https://qlik.dev/apis/rest/users).

```bash
curl -G "https://<SOURCE_TENANT>/api/v1/users" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
--data-urlencode "filter=email eq \"<EMAIL_ADDRESS>\""
```

The source tenant responds with JSON including the `<IDP_SUBJECT>` of the user.
Record the `<IDP_SUBJECT>` for use when you add the user on the target tenant.

```json
{
   "id":"62daccb20452a739b722e042",
   "tenantId":"7WZ_qyWDvlS8AvNkye9y20dn-miC0URe",
   "status":"active",
   "subject":"<IDP_SUBJECT>",
   "name":"<USER_NAME>",
   "email":"<EMAIL_ADDRESS>",
   "locale":"en_US",
   "zoneinfo":"America/Los_Angeles",
   "roles":[...],
   "groups":[...],
   "links":{...}
}
```

## 2 Add the user to the target tenant as a TenantAdmin

Use the `<IDP_SUBJECT>`, `<EMAIL_ADDRESS>`, and `<USER_NAME>` from
the source tenant alongside the role `TenantAdmin` to
add the `Qlik Account` user to the target tenant.

The JSON body for the request format:

```json
{
    "name": "<USER_NAME>",
    "email": "<EMAIL_ADDRESS>",
    "status": "active",
    "subject": "<IDP_SUBJECT>",
    "assignedRoles": [
        {
            "name": "TenantAdmin"
        }
    ]
}
```

and the cURL request:

```bash
curl -L -X POST "https://<TARGET_TENANT>/api/v1/users" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"name\": \"<USER_NAME>\",
    \"email\": \"<EMAIL_ADDRESS>\",
    \"status\": \"active\",
    \"subject\": \"<IDP_SUBJECT>\",
    \"assignedRoles\": [
        {
            \"name\": \"TenantAdmin\"
        }
    ]
}"
```

If the user subject and email don't already exist on the tenant, you will receive
a 201 created status and the details of the new user.

The `id` of the new user record is specific to the tenant, unlike the `subject`.

```json
{
    "id": "63808c151d6142f5fa96e670",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "status": "active",
    "subject": "<IDP_SUBJECT>",
    "name": "<USER_NAME>",
    "email": "<EMAIL_ADDRESS>",
    "roles": [
        "TenantAdmin"
    ],
    "assignedRoles": [
        {
            "id": "12345c151d6142f5fa96e123",
            "name": "TenantAdmin",
            "type": "default",
            "level": "admin"
        }
    ],
    ...
}
```

## 3 Test authentication through a web browser

Once the user is added to the target tenant, navigate to the tenant using a web
browser and authenticate to Qlik Cloud via `Qlik Account`.

Your browser will present the Qlik Cloud hub, and you will also be able to access
the management console if needed.

## Next steps

With your recovery user set up, the stage is set
for [configuring your tenant](https://qlik.dev/manage/platform-operations/configure-a-tenant).
