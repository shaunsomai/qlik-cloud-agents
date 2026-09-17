---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-deploy-themes-extensions/
last_updated: 2026-03-18T16:49:43Z
---

# Deploy Themes and Extensions with Platform Operations

## Deploy themes and extensions

Themes and extensions provide powerful methods to customize the look and
feel of analytics applications. In this example, you will:

- Retrieve a list of extensions on a source tenant
- Retrieve a list of themes on source tenant
- Filter these assets by a tag
- Deploy these assets to a target tenant

This model assumes you have your themes and extensions preloaded to a source tenant
prior to deployment, however it's possible to use other Automations connectors,
such as the GitHub connector, to load these assets from a repository rather
than a source tenant.

For more information on how to achieve this via Qlik APIs and toolkits, review
the pro-code [Add themes and extensions tutorial](https://qlik.dev/manage/platform-operations/add-custom-themes-and-extensions).

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- Valid OAuth client with access to the tenants on which you wish to
  run the automation.
- Access to a source tenant with existing extensions and themes, with at least
  one extension and theme tagged with `deploy`.
- Access to a target tenant.

## Variables you need to complete this tutorial

- `sourceTenant`: The hostname for your source Qlik Cloud tenant (for example
  sourcetenant.eu.qlikcloud.com).
- `targetTenant`: The hostname for your target Qlik Cloud tenant (for example
  targettenant.eu.qlikcloud.com).

## Configuration

Prior to beginning, your `sourceTenant` should have one or more themes and extensions
available and tagged with `deploy`. These will be exported and imported to the
`targetTenant` by the automation.

![Browser window showing source tenant extensions](https://qlik.dev/_astro/qpo-thext-01.CvppeHis.png)

![Browser window showing source tenant themes](https://qlik.dev/_astro/qpo-thext-02.CAufIiAV.png)

Drag two *Get Tenant Name And Region* blocks onto your *Start* block. The first
should be configured with the *Hostname* set to `sourceTenant`, and the second
should be configured with the *Hostname* set to `targetTenant`.

![Browser window showing the get tenant blocks](https://qlik.dev/_astro/qpo-thext-03.BPItioBu.png)

Add a *List Extensions* block, set the *Tenant* to the `sourceTenant`
*Get Tenant Name And Region* block to return extensions in the `sourceTenant`.

![Browser window showing the List Extensions block](https://qlik.dev/_astro/qpo-thext-04.x60b0-lQ.png)

Add a *Filter List* block, set the *List* to
the *List Extensions* block, and the condition to when `tags` contains `deploy`.
This will filter the extension list to only return extensions with that tag. This
is desirable in deployment scenarios, as you may have extensions in varying stages
of development, and you may wish to deploy only those that are production
ready.

![Browser window showing the Filter List block](https://qlik.dev/_astro/qpo-thext-05.OpFqNJk2.png)

Add an *Get Extension Archive* block, set the *Tenant* to the *Get Tenant Name And Region*
block for the `sourceTenant`, and the ID to the extension ID from the *Filter List*.
This exports the extension as a base64-encoded string.

![Browser window showing the Get Extension Archive block](https://qlik.dev/_astro/qpo-thext-06.bknoGPRM.png)

Add a *Create Extension* block, set the *Tenant* to the *Get Tenant Name And Region*
block for the `targetTenant`, and the *File* to the output from the
*Get Extension Archive* block. This will create the extension on the target tenant.

![Browser window showing the Create Extension block](https://qlik.dev/_astro/qpo-thext-07.DXLpeP-d.png)

Add a *Output* block, set the *Data to output* to the *Create Extension*
block to return information on the new extension once it is created.

![Browser window showing the output block](https://qlik.dev/_astro/qpo-thext-08.LbZUFdlK.png)

Now repeat this for themes. The extension and theme blocks work the same way and
return the same data structures, so copy the same attributes into each of these
blocks.

![Browser window showing the theme block section](https://qlik.dev/_astro/qpo-thext-09.BTquqLvB.png)

Select *Run* to trigger the automation. The output will return the theme and extension
metadata for the new assets created on the `targetTenant`.

![Browser window showing the output of the automation on the run screen](https://qlik.dev/_astro/qpo-thext-10.4QFuFSCg.png)

The Platform Operations connector includes blocks for many other features and
capabilities in Qlik Cloud allowing you to load/ store these assets outside
of Qlik Cloud.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/deploy-themes-extensions.json`
</details>

## Next steps

Now that you are have successfully created a tenant, added a user, configured the
tenant, deployed apps, and deployed themes and extensions, you are ready to create
your own, more advanced workflows using the many blocks in the Platform Operations
connector, and the many APIs on Qlik Cloud.
