---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-configure-tenant/
last_updated: 2025-11-07T09:45:47Z
---

# Configure a tenant with Platform Operations

## Configure a tenant

Automated tenant configuration is an important step, irrespective of use case. In
this tutorial, you will:

- Set license assignment settings
- Seed groups to the tenant for preparing access control
- Set up spaces ready for analytics content deployment
- Assign members to these spaces
- Disable an unwanted tenant feature

This example seeds a set of groups, and creates a `dev-finance` shared space with
the `Developers` group assigned full access, and a `Finance` managed space with
the `Developers` group assigned full access, and the `Finance` group assigned consume
access.

For more information on how to achieve this via Qlik APIs and toolkits, review
the pro-code [Configure a tenant tutorial](https://qlik.dev/manage/platform-operations/configure-a-tenant).

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- Valid OAuth client with access to the tenants on which you wish to
  run the automation.
- Access to a target tenant.

## Variables you need to complete this tutorial

- `targetTenant`: The hostname for your target Qlik Cloud tenant (for example
  targettenant.eu.qlikcloud.com).

## Configuration

Drag a *Get Tenant Name And Region* block onto your *Start* block. This should
be configured with the *Hostname* set to `targetTenant`.

![Browser window showing the get tenant block](https://qlik.dev/_astro/qpo-configure-01.CT3_ZfKv.png)

Add a *Update Tenant Auto License Assignment* block, set the *Tenant* to
the *Get Tenant Name And Region* block, and the automatic assignment rules to
match your requirements. This controls what licenses new users are created by
default in the tenant.

![Browser window showing the Update Tenant Auto License Assignment block](https://qlik.dev/_astro/qpo-configure-02.V9PXJP5D.png)

Add a *Update Auto Create Group Settings* block, set the *Tenant* to
the *Get Tenant Name And Region* block, and set *Enable Auto Group Creation* to
`true`. This is required for seeding groups in the tenant.

![Browser window showing the Update Auto Create Group Settings block for the target tenant](https://qlik.dev/_astro/qpo-configure-03.BvNOOH-B.png)

Add a *Create Group* block, set the *Tenant* to the *Get Tenant Name And Region*
block, and enter the groups you wish to deploy to the tenant. This example deploys
5 groups: `developers`, `sales`, `marketing`, `finance`, and `administrators`.

![Browser window showing the Create Group block on the target tenant](https://qlik.dev/_astro/qpo-configure-04.CmwDoiQF.png)

Add a *List Groups* block, and set the *Tenant* to the *Get Tenant Name And Region*
block. This will return the newly created groups.

![Browser window showing the List Groups block](https://qlik.dev/_astro/qpo-configure-05.DEQ9pcSE.png)

Add a *Create Space* block, set the *Tenant* to the *Get Tenant Name And Region*
block, and add attributes to create a shared space for developers. In this example,
the shared space will be named `dev-finance`, and show the description
`A development space for finance apps`.

![Browser window showing the create space block](https://qlik.dev/_astro/qpo-configure-06.BjiSbS0Z.png)

Add a *Filter List* block, set the *List* to the *List Groups* block, and filter
the results to return only where *name* equals `developers`. You will need the
ID for this group when assigning it to a space.

![Browser window showing the Filter List block](https://qlik.dev/_astro/qpo-configure-07.vUvzSLh0.png)

Add a *Add Member To Space* block, set the *Tenant* to the
*Get Tenant Name And Region* block, the *Space ID* to the ID of the space created
using the *Create Space* block, the *Assignee ID* to the ID of the group
returned by the *Filter List* block, the *Roles* to
`["codeveloper", "consumer", "dataconsumer", "facilitator", "producer"]`, and
the *Type* to `group`.

> **Note:** While this example shows the addition of a single group, moving the *Add Member To Space* block to the loop on
> the *Filter List* block would allow you to assign multiple groups to the space with no additional blocks.

![Browser window showing the Add Member To Space block](https://qlik.dev/_astro/qpo-configure-08.DP9OLmIZ.png)

Add another *Create Space* block, set the *Tenant* to the *Get Tenant Name And Region*
block, and add attributes to create a managed space for finance users. In this example,
the managed space will be named `Finance`, and show the description
`A space for finance apps`.

![Browser window showing the Create space block](https://qlik.dev/_astro/qpo-configure-09.D7fKodL5.png)

Add another *Filter List* block, set the *List* to the *List Groups* block and filter
the results to return only where *name* equals `finance`. You will need the
ID for this group when assigning it to a space.

You will use the output of both this block and the previous *Filter List* block
to add both the `Developers` and `Finance` groups to the space.

![Browser window showing the Filter List block](https://qlik.dev/_astro/qpo-configure-10.dunNL1gr.png)

Add a *Add Member To Space* block, set the *Tenant* to the
*Get Tenant Name And Region* block, the *Space ID* to the ID of the space created
using the *Create Space* block, the *Assignee ID* to the ID of the group
returned by the second *Filter List* block, the *Roles* to `["consumer"]`, and
the *Type* to `group`.

This will provide the `Finance` group with consume access to the `Finance` managed
space.

![Browser window showing the Add Member To Space block](https://qlik.dev/_astro/qpo-configure-11.Cojg46Nh.png)

Add another *Add Member To Space* block, set the *Tenant* to the
*Get Tenant Name And Region* block, the *Space ID* to the ID of the space created
using the second *Create Space* block, the *Assignee ID* to the ID of the
group returned by the first *Filter List* block, the *Roles* to
`["consumer", "contributor", "dataconsumer", "facilitator", "publisher"]`, and
the *Type* to `group`. Note that these roles are different than the previous
assignment, as the space type is different.

This will provide the `Developers` group with full access to the `Finance` managed
space.

![Browser window showing the Add Member To Space block](https://qlik.dev/_astro/qpo-configure-12.BlYe5E4r.png)

Add a *Update Notes Settings* block, set the *Tenant* to the
*Get Tenant Name And Region* block, and both the *Note Toggle* and *Snapshot Relations*
values to `false`. This will turn off the Notes feature in the tenant for all users.

This is an example of how you can customize different tenants to suit different
use cases or customer profiles.

![Browser window showing the Update Notes Settings block](https://qlik.dev/_astro/qpo-configure-13.BOzLHLSF.png)

Add a *List Spaces* block, and set the *Tenant* to the
*Get Tenant Name And Region* block. This will return the spaces in the tenant
as well as their configuration.

![Browser window showing the List Spaces block](https://qlik.dev/_astro/qpo-configure-14.BcgkiQDC.png)

Add a *Output* block, set the *Data to output* to the
*List Groups* block, to output this to the run screen on execution.

![Browser window showing the Output block](https://qlik.dev/_astro/qpo-configure-15.CaI5Gdlq.png)

Add a *Output* block, set the *Data to output* to the
*List Spaces* block, to output this to the run screen on execution.

![Browser window showing the Output block](https://qlik.dev/_astro/qpo-configure-16.D077IE_H.png)

Select *Run* to trigger the automation. The output will return the group and space
metadata created on the `targetTenant`.

![Browser window showing the output of the automation on the run screen](https://qlik.dev/_astro/qpo-configure-17.Qcaevfv9.png)

The Platform Operations connector includes blocks for many other features and
capabilities in Qlik Cloud.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/configure-tenant.json`
</details>

## Next steps

Now that you are have configured your tenant, move on
to [Deploy Qlik Sense applications](https://qlik.dev/manage/platform-operations/no-code/qpo-deploy-application).
