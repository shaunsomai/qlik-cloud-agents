---
source: https://qlik.dev/manage/analytics-applications/task-chaining-automations/
last_updated: 2026-04-20T13:34:03+01:00
---

# Task chaining with Automate

## Overview

In this tutorial, you are going to learn how to use Qlik Automate
and webhooks to chain analytics reloads in Qlik Cloud using events. This avoids the need
for long-running automations, polling, or external systems and data, with each automation
run lasting a couple of seconds rather than a couple of hours.

If you are new to this topic, first read the [reloads overview](https://qlik.dev/manage/analytics-applications).

If you prefer scheduling instead, continue reading, as this tutorial includes
a scheduled example. For those interested in using code from within your own
infrastructure, see [task chaining using polling with qlik-cli](https://qlik.dev/manage/analytics-applications/task-chaining-qlik-cli).
Additionally, you can define the reload order within a long-running automation using the
templates built into Automate.

## Reloading using webhooks and the Reloads API

A reload in Qlik Cloud emits a [reload finished event](https://qlik.dev/apis/event/apps/#%23%2Fentries%2Fcom.qlik.v1.app.reload.finished)
upon completion. You can subscribe to this event within Qlik Cloud to
initiate other reloads using the [Reloads API](https://qlik.dev/apis/rest/reloads).

Learn more about [webhooks in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm)
and [webhook triggers](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm)
in the Qlik Cloud connector, on Qlik Help.

## How the task runner automation works

This automation is designed to be configured and deployed by a tenant administrator.
It has the following configuration variables:

- Variable `prefixForChain` sets the tag prefix used to detect tags indicating apps
  to reload next. By default this is `next-`, so it will pick up tags of the format
  `next-<app GUID>` (for example, `next-17dfd44a-746b-48fa-9cf4-f83411f50375` will
  trigger a reload of an app with ID `17dfd44a-746b-48fa-9cf4-f83411f50375`).
- Variable `defaultTolerance` sets the minimum duration after a previous reload in
  which a new reload will be triggered. This prevents apps from being reloaded
  too often, or causing reload storms. By default, this is `10`, representing
  10 minutes.
- Variable `onlyManagedSpaces` indicates whether apps should only be reloaded if
  found in managed spaces. By default, it is set to `0`, so it will attempt to reload
  any apps (not just those in managed spaces).
- Variable `autoResolveAccessIssues` determines whether the automation attempts to add
  access to the space for the app it is attempting to reload, if it doesn't already have
  access under the current user. By default, it is set to `1`, so it
  will add the current user to any spaces where they do not have permission to access
  data connections or start a reload of an app with full permissions. When apps are in personal
  spaces, or use data connections in spaces other than the app space (and the current
  user does not currently have access), it will not be successful.

When configured with the default values, the automation operates as follows:

1. Starts when called by the webhooks service after the `qlik.v1.app.reload.finished` event
   is emitted.
2. Uses the metadata in the `qlik.v1.app.reload.finished` event to look up the app
   in the tenant. This is to retrieve the list of tags on that app.
3. Reviews the tags on the app for any prefixed with `next-`.
4. Loops over any matching tags found on the app, retrieving the app information,
   space information, and last reload of each.
5. If the last reload was less than 10 minutes ago, or is still running, or if
   the app cannot be found, skip the reload.
6. If the current user doesn't have access to the app space, add the user to the
   space with full roles ([review roles for more information](https://qlik.dev/manage/roles/)).

Once the reloads of any apps started by this automation have completed, a new event
will be emitted for each reload, and the automation will
start for each of those events. Each run of the automation is triggered by an app reload.

> **Note:** If you would rather use a service account for reload chains, you can create an OAuth client and do the same activities
> using the Qlik Platform Operations connector in Automate
> Learn more about that connector in the [Platform Operations no-code guide](https://qlik.dev/manage/platform-operations/no-code/overview/).

## Create a reload task

The first task in your reload chain should have an associated reload task. You
can [configure this in the Qlik Cloud hub](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/reloading-apps-cloud-hub.htm).
Once the chain is initiated, all subsequent
tasks will be triggered directly by your automation.

![Set up a reload task with a schedule](https://qlik.dev/_astro/tca01.CReF8Ggv.png)

The schedule you set in this task determines the frequency of other reloads in
the chain, since it initiates the entire process.

In this example, it creates a simple reload flow which reloads four
apps/scripts after a scheduled reload of the `Extract data from finance system` script:

- Script `Extract data from finance system` in space `Data prep`, on success:
  - Script `Transform finance data` in space `Data prep`, on success:
    - Qlik Sense app `Finance historical` in space `Finance`
    - Qlik Sense app `Finance analytics` in space `Finance`
    - Qlik Sense app `Finance Exec` in space `Finance`

## Create a reload chain

With the reload task created for your first app, find your second app in the
Qlik Cloud hub. Right-click the app and select `Details`.

![Look up the App or Script ID for your target content](https://qlik.dev/_astro/tca02.CkqIyl4w.png)

This view will show either an App ID for Qlik Sense apps or a Script ID for load
scripts, which you must reference when triggering a reload.

Next, go back to your first app or load script in the hub. Right-click and
select `Rename`, then add tags to the item.

![Add the ID of the target item to the source item](https://qlik.dev/_astro/tca03.Qh5PH5JR.png)

Prefix the ID of the target content with `next-` (for example,
`next-82353b5d-9a9c-4022-9aa4-7a0e5da8a838`), drop it into the tags section,
select the newly created tag, and click `Save` to exit.

![The tag will be visible on the item card, and in the detail view for the item](https://qlik.dev/_astro/tca04.CmCOIVgL.png)

Repeat this process for each app you need to trigger from the source or move to the target
to add tags for its targets. Once tags are set up, you're ready to import
the automation.

## Configure the automation

Create a new automation from the Qlik Cloud hub, and name it `Reload runner`.
Import the automations from [the full automation snippet section](#full-automation-snippet):

In the example, the first block should be configured by:

1. Select the first `Start` block.
2. Set the run type to `Webhook`.
3. Select the `Qlik Cloud Services` connector from the dropdown.
4. Filter to `Reload finished` events only.

This will create a webhook in the tenant that calls this automation.
The webhook will show as having been created by the current user.

## Run the automation

The automation will automatically start on any reload in the platform. Trigger a
reload of your first app from the hub by selecting `Reload now`.

![A run will be triggered for the reload, and it'll pick up the tags from the item](https://qlik.dev/_astro/tca05.Cs2zIVQt.png)

The automation will pick up the run, and the associated tags, stripping `next-` and
attempting to start reloads of those items. If it fails for any reason, it will report
this in the output and run title.

This reload triggered the next reload, which had links to the dashboard apps in:

![The next reload picked up more tags, and triggered multiple apps](https://qlik.dev/_astro/tca06.DZPGSInC.png)

As the dashboard apps had no tags on, their reloads were detected, but no further
action was taken.

![The resulting chain of automations that triggered the reloads](https://qlik.dev/_astro/tca07.DQpMKQAf.png)

All output is logged to the automation console, and could be logged to other sources
as needed. The five automation runs triggered from reload finished events drove
the reloads of the apps in the pattern configured in tags on those resources.

## Scheduled alternative

If you prefer the automation not to execute every time a reload completes
in your tenant, you can opt to use a variant which checks for all successful reloads
since the last run.

This automation is largely the same as the webhook version, with additional blocks
at the beginning to:

- Determine the last run of the automation.
- Retrieve all `qlik.v1.app.reload.finished` events that occurred since that timestamp.

As a result, the automation scans multiple apps at once to trigger ongoing tasks.

![A single run of this automation can trigger many target apps from many source apps](https://qlik.dev/_astro/tca08.Da9rwTnB.png)

How frequently you schedule this automation to run will determine how soon new
reloads start after the completion of previous reloads in the chain. For example, running
it every 15 minutes would result in about 3,000 runs per month. If your environment has
fewer reloads than this or if you require reloads to start as soon as possible after the
preceding app finishes, consider using the event-triggered automation.

## Summary

Reloading apps is required to obtain the latest data for a
Qlik Sense app. For large deployments, reloads are multi-layered and often
generate datasets as part of a downstream app reload. Chaining reloads
together simplifies this process significantly.

Using this automation, a single administrator can configure a runner which any
user in the tenant can use to chain their reloads. This approach is scalable
and includes safeguards against users reloading apps too frequently.

You can customize this example with per-user, per-space, per-group restrictions
by adding in checks for other metadata from the [Qlik Cloud APIs](https://qlik.dev/apis).

## Full automation snippet

To import one of these snippets to your own automation, either:

- Save the snippet as a JSON file, right-click the canvas in an automation, and
  select *Upload workspace*.
- Copy the snippet to the clipboard, right-click the canvas in an automation,
  and select *Paste blocks*.

<details>
  <summary>Full automation snippet - webhook version</summary>

  This is the webhook-triggered version.

  `embed:./snippets/reloads/reload-automation-webhook.json`
</details>

<details>
  <summary>Full automation snippet - scheduled version</summary>

  This is the scheduled version.

  `embed:./snippets/reloads/reload-automation-scheduled.json`
</details>
