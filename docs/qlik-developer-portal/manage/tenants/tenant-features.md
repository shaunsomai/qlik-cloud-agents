---
source: https://qlik.dev/manage/tenants/tenant-features/
last_updated: 2026-04-20T13:34:03+01:00
---

# Configure tenant settings

In this topic, you will learn about how to programmatically control access to features
and capability settings found on the *Settings* pane in a Qlik Cloud tenant's management
console.

When using the management console of a tenant as a user with the Tenant Admin role,
you will see various settings that help you control which features your users
have access to. The configuration method varies by service, both in terms of the
API calls required, and the level at which it can be configured. Some services support
user or space-level access, while others are available only at the tenant level.

| Setting                          | Setting description                                                                          | Setting scope  | API support | Guide                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------- | -------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------- |
| API keys                         | Allow users to create and manage their API keys, if they have the Manage API keys permission | Tenant         | Yes         | [API keys](https://qlik.dev/manage/tenants/tenant-features/#configure-api-keys)                                                 |
| Qlik Automate                    | Allow users to access Qlik Automate                                                          | Users & Groups | Yes         | [Qlik Automate](https://qlik.dev/manage/tenants/tenant-features/#configure-qlik-automate)                                       |
| Automatic entitlement assignment | Enable automatic license assignment if using Professional and Analyzer licenses              | Tenant         | Yes         | [Automatic entitlement assignment](https://qlik.dev/manage/tenants/tenant-features/#configure-automatic-entitlement-assignment) |
| AutoML                           | Allow users to configure ML deployments and experiments                                      | Users & Groups | Yes         | [AutoML](https://qlik.dev/manage/tenants/tenant-features/#configure-automl)                                                     |
| Chart sharing via email          | Allow users to share charts via email                                                        | Tenant         | Yes         | [Chart sharing via email](https://qlik.dev/manage/tenants/tenant-features/#configure-chart-sharing-by-email)                    |
| Data alerts                      | Allow users to create and manage data alerts                                                 | Tenant         | Yes         | [Data alerts](https://qlik.dev/manage/tenants/tenant-features/#configure-data-alerts)                                           |
| Dynamic views                    | Enable dynamic views for Qlik Sense apps                                                     | Tenant         | No          |                                                                                                                                 |
| Email server                     | Configure an SMTP server to send tenant notifications, share content, tabular reporting, etc | Tenant         | Yes         | [Email server](https://qlik.dev/manage/tenants/email-provider)                                                                  |
| Groups                           | Create groups if sent via group claims from your identity provider                           | Tenant         | Yes         | [Groups](https://qlik.dev/manage/tenants/tenant-features/#configure-automatic-group-creation)                                   |
| ML endpoints                     | Analytics endpoints for machine learning endpoints                                           | Tenant         | No          |                                                                                                                                 |
| Mobile offline usage             | Allow offline mobile usage                                                                   | Tenant         | No          |                                                                                                                                 |
| Notes                            | Allow users to create and manage notes                                                       | Tenant         | Yes         | [Notes](https://qlik.dev/manage/tenants/tenant-features/#configure-notes)                                                       |
| On-demand app generation         | Enable on-demand Qlik Sense apps                                                             | Tenant         | No          |                                                                                                                                 |
| SCIM auto provisioning           | Set the token expiration period                                                              | Tenant         | Yes         | [SCIM auto provisioning](https://qlik.dev/manage/tenants/tenant-features/#configure-scim-auto-provisioning)                     |
| Subscriptions                    | Allow users to create and manage chart and sheet subscriptions                               | Tenant         | Yes         | [Subscriptions](https://qlik.dev/manage/tenants/tenant-features/#configure-chart--object-subscriptions)                         |
| Tabular reporting                | Allow users to configure Excel reports in Qlik Cloud                                         | Tenant         | Yes         | [Tabular reporting](https://qlik.dev/manage/tenants/tenant-features/#configure-tabular-reporting)                               |
| Tenant alias hostname            | Set the "friendly" tenant hostname                                                           | Tenant         | Yes         | [Tenant alias hostname](https://qlik.dev/manage/tenants/update-tenants/)                                                        |
| Tenant encryption                | Configure tenant key providers                                                               | Tenant         | Yes         | [Tenant encryption](https://qlik.dev/manage/tenants/tenant-encryption/)                                                         |
| Tenant name                      | Set the name of your tenant                                                                  | Tenant         | Yes         | [Tenant name](https://qlik.dev/manage/tenants/update-tenants/)                                                                  |
| Usage metrics                    | Display usage information for content in the hub                                             | Tenant         | Yes         | [Usage metrics](https://qlik.dev/manage/tenants/tenant-features/#configure-usage-metrics-in-the-hub)                            |

## Prerequisites

- You have a basic understanding of Qlik Cloud and the features available to users.
- cURL for running the inline examples, or access to Qlik Automate
  and the Qlik Platform Operations connector.
- An access token or API key for an account with the Tenant Admin role -
  see [Authentication](https://qlik.dev/authenticate).

> **Note:** The cURL examples in this topic show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this topic, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable         | Description                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`       | The URL for the tenant that you are configuring. Equivalent to `tenanthostname.region.qlikcloud.com`.                                         |
| `<ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<TENANT_ID>`    | The tenant ID for the `<TENANT>`. Can be retrieved via `https://<TENANT>/api/v1/tenants/me`.                                                  |

## Configure API Keys

API keys can be used by developers to gain programmatic access to the Qlik platform,
acting as their own user. APIs are bound to a user, and the user must have the Manage API keys permission, either
through a [custom role](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-custom-roles-capacity-model.htm)
or by having the permission enabled in the User Default settings.

> **&#x20;No code option:** Using Qlik Automate, you can use the `Get API Key Settings` and `Update API Key Settings` blocks from the
> Qlik Platform Operations connector to do this without code.

To update API key settings, retrieve the current settings:

```bash
curl -L "https://<TENANT>/api/v1/api-keys/configs/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

If successful, responds with `200` and the current configuration:

```json
{
  "api_keys_enabled": true,
  "max_api_key_expiry": "P365D",
  "max_keys_per_user": 5,
  "scim_externalClient_expiry": "P365D"
}
```

To change these values, send one or multiple operations to update the configuration:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/api-keys/configs/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/api_keys_enabled\",
        \"value\": true
    },
    {
        \"op\": \"replace\",
        \"path\": \"/max_keys_per_user\",
        \"value\": 10
    },
    {
        \"op\": \"replace\",
        \"path\": \"/max_api_key_expiry\",
        \"value\": \"P365D\"
    }
]"
```

If successful, responds with a `204` and an empty response.

Learn more about:

- The [API keys](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm)
  capability.
- The [API keys](https://qlik.dev/apis/rest/api-keys/) API.

## Configure Qlik Automate

Qlik Automate is available by default to all users with the appropriate
roles or permissions in the tenant.

You can determine who can create, update, and delete automations in their personal
spaces by adding or removing the `Automation Creator` role from the `Everyone` group.
Automations access in shared spaces is controlled by the `Shared Automations` permission
and the `Can edit` space role.

### Automations in personal spaces

If you are not familiar with groups in Qlik Cloud, review
[Manage groups](https://qlik.dev/manage/manage-groups/).

> **&#x20;No code option:** Using Qlik Automate, you can use the `Add Role To Group By Name` and `Remove Role From Group By Name` blocks from the
> Qlik Platform Operations connector to do this without code.
> Use group name `com.qlik.Everyone` and role name `AutomationCreator`.

To remove this role from the `Everyone` group, thereby removing the ability for
users to use automations, you must first retrieve the list of roles assigned to
the `Everyone` group. The `Everyone` group always has the
ID of `000000000000000000000001`.

```bash
curl -L "https://<TENANT>/api/v1/groups/000000000000000000000001" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return the group definition for the `Everyone` group:

```json
{
    "id": "000000000000000000000001",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    ...
    "name": "com.qlik.Everyone",
    ...
    "assignedRoles": [
        {
            "id": "6467dcd960754c03a3ed402c",
            "name": "AutomationCreator",
            "type": "default",
            "level": "user"
        },
        {
            "id": "63580b8d5cf9728f19217be0",
            "name": "PrivateAnalyticsContentCreator",
            "type": "default",
            "level": "user"
        },
        {
            "id": "605a1c2151382ffc836af862",
            "name": "SharedSpaceCreator",
            "type": "default",
            "level": "user"
        }
    ],
    ...
}
```

This response indicates that there are three roles assigned to the `Everyone`
group; `AutomationCreator`, `PrivateAnalyticsContentCreator` and `SharedSpaceCreator`.
Your next request will patch this group, requesting that the roles are replaced
with just `PrivateAnalyticsContentCreator` and `SharedSpaceCreator`.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/groups/000000000000000000000001" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/assignedRoles\", \"value\": [{\"name\": \"PrivateAnalyticsContentCreator\"}, {\"name\": \"SharedSpaceCreator\"}]}]"
```

If successful, an empty response with an `HTTP 204` code is returned.

For more information on this endpoint, review the API specification
for [groups](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2F-groupId-patch).
If you then wish to add this capability back to a subset of your users, you can
opt to assign this role on a user-by-user or group-by-group basis with a patch
call to the [users](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers%2F-userId-patch) or [groups](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2F-groupId-patch) APIs.

### Automations in shared spaces

To manage automations in a shared space, the user must be assigned the
`Shared Automations` permission, either via User Default, or via a custom role. Refer
to the [custom roles guide](https://qlik.dev/manage/roles/custom-roles/) for further information.

To run an automation in a shared space, the user must be assigned the `Can edit` role
in the space. Refer to the [space roles matrix](https://qlik.dev/manage/roles/#space-roles) for
additional information.

## Configure automatic entitlement assignment

If you are a customer leveraging Qlik's user entitlement model,
users will be assigned a named Professional or Analyzer entitlement, or consume
Analyzer Capacity as they use the platform. For more information on this model,
see [Managing user entitlements](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-allocations.htm)
on Qlik Help.

> **&#x20;No code option:** Using Qlik Automate, you can use the `Get Tenant Auto License Assign Settings`
> and `Update Tenant Auto License Assign Settings` blocks from the Qlik Platform Operations connector to do this without
> code.

To turn off the automatic assignment of named entitlements to new
users as they are created, or as they access content in the tenant, change the
values of `autoAssignProfessional` and `autoAssignAnalyzer` to false in this API call:

```bash
curl -L -X PUT "https://<TENANT>/api/v1/licenses/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{\"autoAssignProfessional\":false,\"autoAssignAnalyzer\":false}"
```

If successful, the result of the request is returned with an `HTTP 200` code.

```json
{
  "autoAssignProfessional": false,
  "autoAssignAnalyzer": false
}
```

For more information on this endpoint, review the API specification
for [licenses/settings](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fsettings-put).

Learn more about:

- The way [user assignments](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-allocations.htm)
  works in Qlik Cloud for user-based subscriptions.
- The [licenses](https://qlik.dev/apis/rest/licenses/) API.

## Configure automatic group creation

Security in Qlik Cloud can be applied to both users and groups. Using groups to
secure access to content and resources simplifies access management by allowing
an identity provider outside of Qlik to manage user access to Qlik resources
using group membership. As group membership changes, Qlik automatically picks up
the changes and ensures that users can only access content and resources
according to their group memberships.

> **&#x20;No code option:** Using Qlik Automate, you can use the `Get Auto Create Group Settings` and `Update Auto Create Group Settings`
> blocks from the Qlik Platform Operations connector to do this without code.

To enable group management on a tenant, access
[`/groups/settings`](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2Fsettings-patch)
endpoint and set the `autoCreateGroups` property to
`true` to permit group creation on user login, and the `syncIdpGroups` property
to `true` if you are using a compatible interactive Identity Provider and wish
groups to be synchronized:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/groups/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/autoCreateGroups\", \"value\": true},{\"op\": \"replace\", \"path\": \"/syncIdpGroups\", \"value\": true}]"
```

The response from this request is an `HTTP 204 updated` status code. There are no
additional details provided in the response.

Learn more about:

- The [groups](https://qlik.dev/apis/rest/groups/) API.

## Configure AutoML

Qlik AutoML is available by default to all users with the appropriate
user entitlement in the tenant.

You can determine who can create,
update, run, and delete ML experiments and deployments by adding or removing
the relevant roles from the `Everyone` group. To learn more about
the controls for managing access to AutoML, see [Who can work with Qlik Predict](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/who-can-work-with-automl.htm)
on Qlik Help.

If you are not familiar with groups in Qlik Cloud, review
[managing groups](https://qlik.dev/manage/manage-groups) topic.

> **&#x20;No code option:** With Qlik Automate, you can manage roles without writing any code.
> Use the `Add Role To Group By Name` and `Remove Role From Group By Name`
> blocks from the Qlik Platform Operations connector. Specify group name as
> `com.qlik.Everyone` and role names as `AutomlDeploymentContributor`
> and `AutomlExperimentContributor`.

To remove these roles from the `Everyone` group, thereby removing the ability for
users to use AutoML, you must first retrieve the list of roles assigned to
the `Everyone` group. The `Everyone` group always has
ID `000000000000000000000001`.

```bash
curl -L "https://<TENANT>/api/v1/groups/000000000000000000000001" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This will return the group definition for the `Everyone` group:

```json
{
    "id": "000000000000000000000001",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    ...
    "name": "com.qlik.Everyone",
    ...
    "assignedRoles": [
        {
            "id": "6467dcd960754c03a3ed402c",
            "name": "AutomlDeploymentContributor",
            "type": "default",
            "level": "user"
        },
        {
            "id": "63580b8d5cf9728f19217be0",
            "name": "AutomlExperimentContributor",
            "type": "default",
            "level": "user"
        },
        {
            "id": "605a1c2151382ffc836af862",
            "name": "SharedSpaceCreator",
            "type": "default",
            "level": "user"
        }
    ],
    ...
}
```

The response in this example indicates that there are three roles assigned to the `Everyone`
group: `AutomlDeploymentContributor`, `AutomlExperimentContributor`, and `SharedSpaceCreator`.
Your next request will patch this group, requesting that the roles are replaced
with only `SharedSpaceCreator`.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/groups/000000000000000000000001" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/assignedRoles\", \"value\": [{\"name\": \"SharedSpaceCreator\"}]}]"
```

If successful, an empty response with an `HTTP 204` code is returned.

For more information on this endpoint, review the API specification
for [groups](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2F-groupId-patch).

To re-enable this capability for specific users or groups, you can assign this role individually with a patch call to
the respective [Users API](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers%2F-userId-patch) or [Groups API](https://qlik.dev/apis/rest/groups/#%23%2Fentries%2Fv1%2Fgroups%2F-groupId-patch).

## Configure chart & object subscriptions

Subscription reports let you schedule recurring emails containing your preferred
sheets or chart. You can set your desired filters and have a report with the newest
data delivered to your inbox at a scheduled time. For example, you could receive
overnight order information in an email every morning.

To turn off chart & object subscriptions for all users, set the value
of `/enable-report-subscription` to `false`:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/sharing-tasks/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/enable-report-subscription\",
        \"value\": false
    }
]"
```

The response from this request is an `HTTP 204 updated` status code. There are no
additional details provided in the response.

Learn more about:

- The [chart & object subscriptions capability](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Subscription-reports.htm)
  on Qlik Help.
- The [Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/).

## Configure chart sharing by email

Chart sharing by email is offered via the right-click context menu while navigating
Qlik Sense apps. Clicking `Share`, then `Image` will prompt for an email address
to which you can send an image of the selected chart.

To turn off chart sharing for all users, set the value of `/enable-sharing` to `false`:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/sharing-tasks/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/enable-sharing\",
        \"value\": false
    }
]"
```

The response from this request is an `HTTP 204 updated` status code. There are no
additional details provided in the response.

Learn more about:

- The [sharing visualizations by email capability](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/sharing-visualizations.htm)
  on Qlik Help.
- The [Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/).

## Configure Data Alerts

Data alerts are enabled by default in new tenants, and can be configured at a
tenant-wide level. This setting affects all users in a tenant, and will hide the
feature context menus in Qlik Sense.

> **&#x20;No code option:** Using Qlik Automate, you can use the `Get Data Alert Settings` and `Update Data Alert Settings`
> blocks from the Qlik Platform Operations connector to do this without code.

To turn off data alerts, set the value of `enable-data-alerting` to `false`:

```bash
curl -L -X PUT "https://<TENANT>/api/v1/data-alerts/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{\"enable-data-alerting\": false }"
```

If successful, an empty response with an `HTTP 204` code is returned.

Learn more about:

- The [data alerts capability](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/monitoring-changes-with-alerts.htm)
  on Qlik Help.
- The [Data alerts API](https://qlik.dev/apis/rest/data-alerts/).

## Configure Notes

Notes allow users to collaborate on insights and analysis in Qlik Sense by adding comments and annotations directly to
sheets and visualizations.
Access to notes is controlled by the `notes` permission scope, which you can grant through User Default settings or by
assigning a custom role.

Tenant administrators can also control access to the Notes capability in Qlik Cloud by using the
Administration activity center.
For detailed instructions, see [Controlling user access to Notes](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes-notes.htm)
on Qlik Help.

### Method 1: Enable notes via User Default settings

User Default settings define the baseline permissions automatically granted to all users in a tenant.
Enabling the `notes` scope in User Default settings grants every user in the tenant permission to create and manage
notes.

Use the Roles API to enable notes for all users via the `UserDefault` role.
Retrieve the role ID first:

```bash
curl -L "https://<TENANT>/api/v1/roles" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Accept: application/json"
```

Find the role with `"type": "default"` and `"name": "UserDefault"` in the response and note its `id` value.
Then, patch the role to add the `notes` scope:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/roles/<USERDEFAULT_ROLE_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
  {
    \"op\": \"replace\",
    \"path\": \"/assignedScopes\",
    \"value\": [<EXISTING_SCOPES>, \"notes\"]
  }
]"
```

Replace `<EXISTING_SCOPES>` with the list of scopes already assigned to the `UserDefault` role.
To extract the scopes, locate the `assignedScopes` array in the `GET` response, copy its values, and append `"notes"`.
For example, if the response shows `"assignedScopes": ["scope1", "scope2"]`, use `["scope1", "scope2", "notes"]`
in the `PATCH` request.

> **Note:** Alternatively, you can use the JSON Patch `add` operation to append the scope without needing to fetch and manage the
> complete scope list.
> For complete examples and other approaches to modifying roles, see [Modify role scopes](https://qlik.dev/manage/access-control/custom-roles/#modify-role-scopes).

If successful, returns an `HTTP 204` response with no content.

To verify the change, run the GET request again and confirm that `notes` now appears in the `assignedScopes` array.

### Method 2: Create a custom role and assign it to users or groups

For more granular control, create a [custom role](https://qlik.dev/manage/access-control/custom-roles/) that includes the `notes` scope
and assign it to specific users or groups.
This lets you grant note access selectively rather than to all users in the tenant.

1. Create a custom role with the `notes` scope:

```bash
curl -L -X POST "https://<TENANT>/api/v1/roles" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
    \"name\": \"Notes users\",
    \"description\": \"Grants permission to create and manage notes\",
    \"assignedScopes\": [
        \"notes\"
    ]
}"
```

If successful, returns an `HTTP 201` response with the new role definition.
You'll use the role name (`Notes users`) in the next step when assigning it to users or groups.

```json
{
    "id": "<ROLE_ID>",
    "name": "Notes users",
    "description": "Grants permission to create and manage notes",
    "type": "custom",
    "assignedScopes": [
        "notes"
    ]
}
```

2. Assign the custom role to users or groups

Use the [Users API](https://qlik.dev/apis/rest/users/) or [Groups API](https://qlik.dev/apis/rest/groups/) to assign the custom role.
For example, to assign the role to a user:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/users/<USER_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{
    \"op\": \"replace\",
    \"path\": \"/assignedRoles\",
    \"value\": [
        { \"name\": \"<EXISTING_ROLE>\" },
        { \"name\": \"Notes users\" }
    ]
}]"
```

For detailed step-by-step instructions on assigning roles to users and groups, see [Assigning roles to users and groups](https://qlik.dev/manage/access-control/manage-roles/).

### Legacy tenant-wide toggle (deprecated)

> **Deprecation notice:** The `/api/v1/notes/settings` endpoint is deprecated and will be removed on or after **March 31, 2026**.
> Migrate to the permissions-based approach to ensure continued control over note access after this date.

The legacy approach toggles notes on or off for all users in the tenant. To disable notes tenant-wide,
set `toggledOn` to `false`:

```bash
curl -L -X PUT "https://<TENANT>/api/v1/notes/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{ \"toggledOn\": false }"
```

If successful, returns the updated configuration with an `HTTP 200` code:

```json
{
  "available": false,
  "reason": "toggle",
  "lastFetch": "2023-07-21T16:26:30.158Z",
  "toggledOn": false
}
```

For more information on this endpoint, review the API specification for [notes/settings](https://qlik.dev/apis/rest/notes/#%23%2Fentries%2Fv1%2Fnotes%2Fsettings-put).

## Configure SCIM auto provisioning

SCIM (System for Cross-Identity Management) is an open standard for automating
the exchange of user identity information between identity providers and enterprise
applications. It aims to simplify user management by providing a common API for
creating, updating, and deleting user accounts across different systems.

To update SCIM auto provisioning expiry settings, retrieve the current settings:

```bash
curl -L "https://<TENANT>/api/v1/api-keys/configs/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

If successful, returns the current configuration with a `200` status code:

```json
{
  "api_keys_enabled": true,
  "max_api_key_expiry": "P365D",
  "max_keys_per_user": 5,
  "scim_externalClient_expiry": "P365D"
}
```

To change these values, send one or multiple operations to update the configuration:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/api-keys/configs/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/scim_externalClient_expiry\",
        \"value\": P365D
    }
]"
```

If successful, returns an empty response with a `204` status code.

Learn more about:

- The [SCIM provisioning capability](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-using-SCIM.htm)
  on Qlik Help.
- The [API keys API](https://qlik.dev/apis/rest/api-keys/).

## Configure tabular reporting

Create dynamic tabular reports by combining the Qlik add-in for Microsoft Excel
with report preparation features available within a Qlik Sense app. Deliver report
output by email and to folders defined in Microsoft SharePoint connections.

Tenant administrators can configure permissions to control whether users have full, partial, or no access to the
value-add capabilities of the Qlik Reporting Service.
For detailed instructions, see [Setting permissions for metered reporting features](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-permissions-reporting.htm)
on Qlik Help.

### Legacy toggle (deprecated)

> **Deprecation notice:** The `/enable-reporting-template-subscription` toggle in the Sharing tasks API settings is deprecated and will be removed on or after April 28, 2026.
> Migrate to the permissions-based approach to ensure continued control over template reporting access after this date.
> For more information, see [Setting permissions for metered reporting features](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-permissions-reporting.htm)
> on Qlik Help.

The legacy approach toggles template reporting on or off for all users in the tenant.
To disable template reporting tenant-wide, set the value of `/enable-reporting-template-subscription` to `false`:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/sharing-tasks/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/enable-reporting-template-subscription\",
        \"value\": false
    }
]"
```

The response from this request is an `HTTP 204 updated` status code. There are no
additional details provided in the response.

Learn more about:

- The [tabular reporting capability](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/cloud-tabular-reports-intro.htm)
  on Qlik Help.
- The [Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/).

## Configure usage metrics in the hub

Usage metrics are enabled by default in new tenants, and can be configured at a
tenant-wide level. This setting affects all users in a tenant, and will hide the
usage metrics visible in the hub.

> **&#x20;No code option:** Using Qlik Automate, you can use the `Get Item Settings` and `Update Item Settings`
> blocks from the Qlik Platform Operations connector to do this without code.

To turn off usage metrics, set the value of `/usageMetricsEnabled` to `false`:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/items/settings" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/usageMetricsEnabled\", \"value\": false }]"
```

If successful, the result of the request is returned with an `HTTP 200` code.

```json
{
  "usageMetricsEnabled": false
}
```

This indicates that usage metrics are no longer available or visible to users.

For more information on this endpoint, review the API specification
for [items/settings](https://qlik.dev/apis/rest/items/#%23%2Fentries%2Fv1%2Fitems%2Fsettings-patch).
