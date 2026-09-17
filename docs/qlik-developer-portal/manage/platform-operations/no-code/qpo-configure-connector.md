---
source: https://qlik.dev/manage/platform-operations/no-code/qpo-configure-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Configure the Platform Operations connector

## Connector configuration

The Qlik Platform Operations connector needs to be configured before use. The
connector contains blocks for calling various APIs, which will also need to be
configured to suit the task you're trying to achieve.

## Requirements

- A Qlik Cloud tenant with access to Qlik Automate.
- A valid OAuth client with access to the tenant that you wish to run the automation
  against.

## Variables you need to complete this tutorial

- `hostname`: The hostname for your Qlik Cloud tenant (for example
  platformoperations.eu.qlikcloud.com).
- `clientId`: The client ID for the machine-to-machine OAuth client.
- `clientSecret`: The client secret for the machine-to-machine OAuth client.

## Configuration

Most blocks in the Platform Operations connector require a minimum of two attributes:

- A connection - this defines the credentials that are used for the block.
- A tenant - this defines the tenant to which the block acts on.

This example will walk through creating a new connection, and configuring a block
to verify that the connection is valid.

### Create a new connection

To create a new connection for a connector that you haven't used before, create
a new Automation, and drag a *Get Tenant Name And Region* block from the
Platform operations connector onto the canvas, and attach it to the start block.

Once the block is in place, select it to access the *Block configuration*, and
then access the *Connection* tab.

![Browser window showing the Connect button for Platform Operations](https://qlik.dev/_astro/qpo-config-01.CRD4hlTs.png)

Clicking on *Connect your Qlik Platform Operations* button will open a dialog
box where you can enter your OAuth `clientId` and `clientSecret`. These will be saved for
future use to the tenant under your user account.

![Browser window showing the Connect dialog box for Platform Operations](https://qlik.dev/_astro/qpo-config-02.C_3U9z0i.png)

After clicking *Save*, click the *pencil* icon on the new connection.

![Browser window showing a newly created connection to Platform Operations](https://qlik.dev/_astro/qpo-config-03.CJRT_Gsk.png)

Change the name of the connection to reflect the license and region (or tenant)
that the OAuth client has access to. This will help you correctly identify which
connection to use in future.

![Browser window showing the edit connection window for Platform Operations](https://qlik.dev/_astro/qpo-config-04.Cg4vUqy7.png)

This example shows what it looks like when you have two connections deployed, in
this case, for the EU and AP regions.

![Browser window showing two connections for Platform Operations](https://qlik.dev/_astro/qpo-config-05.CBt7jrgn.png)

By default, the first connection is used for the block. If you want to use a
different connection, then select it, and it will highlight in green.

![Browser window showing a selection other than the default connection for Platform Operations](https://qlik.dev/_astro/qpo-config-06.BmZcnVNe.png)

Now that you've created the connection, navigate back to the *Inputs* tab in the
*Block configuration* pane.

> **Note:** The `Tenant` input on most blocks supports the passing of either the full
> hostname: `platformoperations.eu.qlikcloud.com`, or the legacy tenant shorthand
> version: `platformoperations.eu`. It is recommended to use the full hostname on blocks.
> If you are deploying in Qlik Cloud Government, you should not use the *Get Tenant Name And Region* block.

You can either use a generic *Variable* block, or the *Get Tenant Name And Region* block
to store and pass the hostname into following blocks. This is a good practice, as
following blocks then refer to this single reference, rather than having the hostname
manually set on each and every block.

![Browser window showing a Get Tenant Name And Region block on the canvas](https://qlik.dev/_astro/qpo-config-07.hQQt-KYi.png)

Any following blocks can then use the *Get Tenant Name And Region* block as the
input. This means when using a loop, the only block you need to update an input
reference in is the *Get Tenant Name And Region* block.

![Browser window showing a List users block on the canvas](https://qlik.dev/_astro/qpo-config-08.BNajmBPF.png)

![Browser window showing a List users block on the canvas](https://qlik.dev/_astro/qpo-config-09.dI0UyVm-.png)

Clicking *Run* will take you to the run screen, where you will be able to
review all previous and current runs of that automation.

![Browser window showing the automation run screen](https://qlik.dev/_astro/qpo-config-10.q3FZkQNh.png)

As there was no *Output* block on the canvas, the *Output* pane will have no output.
Click on the *Chronologically* block to review preview outputs for each of the
blocks.

![Browser window showing the automation run screen chronological view](https://qlik.dev/_astro/qpo-config-11.B0HXU3Qx.png)

The output from the *Qlik Platform Operations - List Users* block verifies
that the connection is valid.

## Full automation snippet

<details>
  <summary>Full automation snippet</summary>

  To import this snippet to your own automation, either:

  - Save the snippet as a JSON file, right click the canvas in an automation, and
    select *Upload workspace*.
  - Copy the snippet to the clipboard, right click the canvas in an automation,
    and select *Paste blocks*.

  `embed:./snippets/platform-ops-connector-tutorials/create-connection.json`
</details>

## Next steps

Now that you are connected, move on
to [Create tenants](https://qlik.dev/manage/platform-operations/no-code/qpo-create-tenant).
