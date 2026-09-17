---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-deploy-application/
last_updated: 2025-07-08T16:09:30Z
---

# Deploy apps with Platform Operations

## Deploy Qlik Sense applications

The core part of an analytics experience in Qlik Cloud is the Qlik Sense application.
This tutorial demonstrates how to migrate applications to a new tenant.

This model assumes you have your applications preloaded to a source tenant
prior to deployment, however it's possible to use other Automations connectors,
such as the GitHub connector, to load these assets from a repository rather
than a source tenant.

> **Note:** This approach supports Qlik Sense applications up to 20 MB in size on disk.
> This means that for most scenarios, you should export an empty template from your source, import this to your target
> tenant, and then reload it on the target tenant. This limitation does not exist when using the pro-code tooling.

For more information on how to achieve this via Qlik APIs and toolkits, review
the pro-code [Deploy a Qlik Sense app](https://qlik.dev/manage/platform-operations/deploy-content-to-a-tenant) tutorial.

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- Valid OAuth client with access to the tenants on which you wish to
  run the automation.
- Access to a source tenant with existing apps published to a shared
  space called `Production`, with at least one app tagged with `deploy`.
  The OAuth client user (bot user) with the `Can manage` role must be a member
  of the shared space.
- Access to a target tenant.

## Variables you need to complete this tutorial

- `sourceTenant`: The hostname for your source Qlik Cloud tenant (for example
  sourcetenant.eu.qlikcloud.com).
- `targetTenant`: The hostname for your target Qlik Cloud tenant (for example
  targettenant.eu.qlikcloud.com).
- `sharedSpaceName`: The name of the space on the source tenant that contains
  the apps you wish to deploy.
- `managedSpaceName`: The name of the space on the target tenant to which you
  wish to publish the apps.

## Configuration

Prior to beginning, your `sourceTenant` should have one or more Qlik Sense apps
available in a shared space named `sharedSpaceName`. These will be exported and
imported to the `targetTenant` by the automation to new shared and managed
spaces on that tenant.

![Browser window showing source tenant apps](https://qlik.dev/_astro/qpo-app-01.BsUn7ikW.png)

Drag two *Get Tenant Name And Region* blocks onto your *Start* block. The first
should be configured with the *Hostname* set to `sourceTenant`, and the second
should be configured with the *Hostname* set to `targetTenant`.

![Browser window showing Get Tenant Name And Region blocks](https://qlik.dev/_astro/qpo-app-02.vR2a21tY.png)

Add two *Variable* blocks, setting the value of variable `sharedSpaceName` to
the name of your shared space on the source tenant, and the value of variable
`managedSpaceName` to the desired name for the managed space on the target tenant.
These spaces will be created on the targetTenant as part of the provisioning workflow.

![Browser window showing a Variable block](https://qlik.dev/_astro/qpo-app-03.DzL3_lP8.png)

![Browser window showing a Variable block](https://qlik.dev/_astro/qpo-app-04.BC6PbSoQ.png)

Add a *List Spaces* block, set the *Tenant* to the *Get Tenant Name And Region*
block for the `sourceTenant`, the *Filter* to `name eq` followed by the
variable for the `sharedSpaceName`, and the *Type* to `shared`. This will
retrieve the metadata for this space from the source tenant.

> **Note:** You must use a shared space.
> It is not possible to export applications from a managed space.

![Browser window showing the List Spaces block](https://qlik.dev/_astro/qpo-app-05.CiiXW8lq.png)

Add a *Create Space* block, set the *Tenant* to the *Get Tenant Name And Region*
block for the `targetTenant`, the *Name* to the name of the space returned from
the *List Spaces* block, the *Type* to `shared`, and the *Description* to the value
returned by the *List Spaces* block. This will create a new shared space on the
target tenant for importing the app to.

![Browser window showing the Create Space block](https://qlik.dev/_astro/qpo-app-06.DsX7MbBb.png)

Add a *Create Space* block, set the *Tenant* to the *Get Tenant Name And Region*
block for the `targetTenant`, the *Name* to the variable for the `managedSpaceName`,
and the *Type* to `managed`. This will create a new managed space on the
target tenant, which you will publish the imported app to.

![Browser window showing the Create Space block](https://qlik.dev/_astro/qpo-app-07.De503NVf.png)

Add a *List Apps* block, set the *Tenant* to the *Get Tenant Name And Region* for
the `sourceTenant`, and the *Space ID* to the output of the *List Spaces* block.
This will return all apps in the shared space on the source tenant.

![Browser window showing the List App block](https://qlik.dev/_astro/qpo-app-08.BVeJfGxf.png)

Within the *List Apps* loop, add a *Export App To Base 64 Encoded File* block, set
the *Tenant* to the *Get Tenant Name And Region* for the `sourceTenant`, the
*App ID* to `resource attributes>id` from the *List Apps* block, and *Exclude Data*
to `false`, if your apps are 20 MB or smaller in size. If they are larger, then set
this to `true`.

![Browser window showing the Export App to Base 64 block](https://qlik.dev/_astro/qpo-app-09.DFLXzceT.png)

Add a *Import App From Base 64 Encoded File* block, set
the *Tenant* to the *Get Tenant Name And Region* for the `targetTenant`, the
*File Data Base 64 Encoded* to the output from the
*Export App To Base 64 Encoded File* block, the *Name* from the *List Apps* block
(although this is optional, if not specified then the app name will be loaded
from the exported file), and the *Space ID* from the *Create Space* block that
created the shared space. This will import the app into that shared space, ready
for publishing.

![Browser window showing the Import App from Base 64 block](https://qlik.dev/_astro/qpo-app-10.CavRoUfh.png)

Add a *Publish App To Managed Space* block, set
the *Tenant* to the *Get Tenant Name And Region* for the `targetTenant`, the
*App ID* to the ID returned via the *Import App From Base 64 Encoded File* block,
the *Space ID* to the ID returned via the *Create Space* block that created
the managed space, and the *Data* to `source` to use the data from the imported
app. This will publish a copy of the app from the shared space into the managed
space, where end users will consume it.

![Browser window showing the Export App to Base 64 block](https://qlik.dev/_astro/qpo-app-11.B30mQE13.png)

Select *Run* to trigger the automation. On the `targetTenant`, the spaces will be
created, apps imported, and then published.

![Browser window showing the apps now deployed and published to the target tenant](https://qlik.dev/_astro/qpo-app-12.odUCvNFr.png)

Navigate to the tenant to view the newly deployed spaces and apps.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/deploy-applications.json`
</details>

## Next steps

Now that you are have successfully deployed apps, move on
to [Deploying themes and extensions](https://qlik.dev/manage/platform-operations/no-code/qpo-deploy-themes-extensions).
