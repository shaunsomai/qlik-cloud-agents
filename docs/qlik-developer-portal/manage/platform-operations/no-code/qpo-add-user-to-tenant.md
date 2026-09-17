---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-add-user-to-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Add a user to a tenant with Platform Operations

## Add user to a tenant

Tenants provisioned in Qlik Cloud programmatically are deployed without any
user accounts. This guide shows you how to copy a user from one tenant
to another.

For more information on how to achieve this via Qlik APIs and toolkits, review
the pro-code [Add user to a tenant](https://qlik.dev/manage/platform-operations/add-an-interactive-user-to-a-tenant) tutorial.

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- Valid OAuth client with access to the tenants on which you wish to
  run the automation.
- Access to a source tenant with existing users.
- Access to a target tenant.

## Variables you need to complete this tutorial

- `sourceTenant`: The hostname for your source Qlik Cloud tenant (for example
  platformoperations.eu.qlikcloud.com).
- `targetTenant`: The hostname for your target Qlik Cloud tenant (for example
  targettenant.eu.qlikcloud.com).
- `userEmail`: The email of the user that you wish to move to the new tenant.

## Configuration

Drag a *Get Tenant Name And Region* block onto your *Start* block. This should
be configured with the *Hostname* set to `sourceTenant`.

![Browser window showing the get tenant block](https://qlik.dev/_astro/qpo-create-user-01.DnXU__fJ.png)

Add a *List Users* block, and set the *Tenant* to
the *Get Tenant Name And Region* block, and the *Filter* to match the
format `email eq "myname@qlik.com"`, substituting the email with your `userEmail`.
This will retrieve any users on the tenant who have that email address, allowing
you to copy their attributes to the target tenant.

![Browser window showing the List users block](https://qlik.dev/_astro/qpo-create-user-02.BHuGj2Cq.png)

Add another *Get Tenant Name And Region* block, this time setting the *Hostname*
to the `targetTenant`.

![Browser window showing the get tenant block for the target tenant](https://qlik.dev/_astro/qpo-create-user-03.DjPDZ_D2.png)

Add a *List Roles* block, specifying the second *Get Tenant Name And Region* block
to load these roles from the `targetTenant`, and entering a filter to return only
the role for *TenantAdmin* with `name eq "TenantAdmin"`.

![Browser window showing the list roles block on the target tenant](https://qlik.dev/_astro/qpo-create-user-04.CddcOuxT.png)

Add a *Transform List* block, using the *List Roles* block as input, and add a
single field in the output list, ID. This field should map to the ID field in
the input list. This will clean up the output from the *List Roles* block so that
it can be directly passed back into Qlik Cloud when creating a new user.

![Browser window showing the transform list block](https://qlik.dev/_astro/qpo-create-user-05.cIbXlbTh.png)

Add a *Create User* block, specifying the `targetTenant` as the *Tenant* using the
corresponding *Get Tenant Name And Region* block. Configure the other *Inputs*
(*Name*, *Email*, and *Subject*) on the block to match the user returned from
the *List Users* block run against the `sourceTenant`. Use the output from the
*Transform List* block as the input for *AssignedRoles*.

![Browser window showing the create user block](https://qlik.dev/_astro/qpo-create-user-06.BvX4OSrQ.png)

Add an *Output* block to return the newly created user.

![Browser window showing the output block](https://qlik.dev/_astro/qpo-create-user-07.Sl3r8X6G.png)

Select *Run* to trigger the automation. The output will return the user metadata
for the user on the `targetTenant`. That user will now be immediately able to
sign in, if the tenant is using Qlik Account as the Identity Provider.

![Browser window showing the automation run screen](https://qlik.dev/_astro/qpo-create-user-08.BJiXiih3.png)

If you wish to use a custom Identity Provider, then you can use a similar process
as for these Qlik Account users, but you will need to pre-provision the Identity
Provider to the tenant, which is beyond the scope of this tutorial.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/add-user-to-tenant.json`
</details>

## Next steps

Now that you are connected, move on
to [Configure a tenant](https://qlik.dev/manage/platform-operations/no-code/qpo-configure-tenant).
