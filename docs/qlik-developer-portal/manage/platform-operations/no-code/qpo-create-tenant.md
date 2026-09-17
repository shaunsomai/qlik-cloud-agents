---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-create-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Create a new tenant with Platform Operations

## Create a new tenant

Where a subscription has a multi-tenant entitlement, the region-level OAuth clients
can be used to create new tenants.

For more information on how to achieve this via Qlik APIs and toolkits, review
the pro-code [Create a tenant](https://qlik.dev/manage/platform-operations/create-a-tenant) tutorial.

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- A valid region-level OAuth client with access to the tenant which you wish to
  run the automation against.
- A subscription with a multi-tenant entitlement.

## Variables you need to complete this tutorial

- `sourceTenant`: The hostname for your source Qlik Cloud tenant (for example
  platformoperations.eu.qlikcloud.com).

## Configuration

Drag a *Get Tenant Name And Region* block onto your *Start* block. This should
be configured with the *Hostname* set to `sourceTenant`.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-create-01.DBf33RTy.png)

Add a *Get License Overview* block, and set the *Tenant* to
the *Get Tenant Name And Region* block. This will retrieve the license information
that you need as an input to create a new tenant.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-create-02.DRy92qif.png)

Add a *Create Tenant* block, setting the *Region* to the region you wish to create
the new tenant in. Set the *License Key* to the *License Key* returned from the
*Get License Overview* block.

> **Note:** You must use the corresponding region OAuth client to generate new tenants.
> For example, if you wish to create a new tenant in the `us` region, you should use an
> OAuth client generated for the `us` region.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-create-03.FwKjlMb0.png)

Add an *Output* block to output the result from the *Create tenant* block, and
select *Run*.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-create-04.BzSzqLOF.png)

The automation will create a new tenant in the specified region and on the
specified subscription.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-create-05.yxlaoARq.png)

Ensure that you record the *Hostnames* of the created tenant for future
reference.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/create-a-tenant.json`
</details>

## Next steps

Now that you are connected, move on
to [Adding a user to a tenant](https://qlik.dev/manage/platform-operations/no-code/qpo-add-user-to-tenant).
