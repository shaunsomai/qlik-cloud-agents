---
source: https://qlik.dev/manage/analytics-applications/
last_updated: 2026-04-20T13:34:03+01:00
---

# Overview

Reloading data into Qlik Sense apps is a necessary step in the business intelligence
workflow. Qlik Sense relies on in-memory analytics as the basis for various features
like embedded analytics, natural language insights, reporting, and alerting.
Before users can access these capabilities, data must be fetched from its source and
loaded into the analytics app.

If you're interested in delivering data directly from sources
to targets via Qlik Cloud Data Integration, review the
[introduction to Qlik Cloud Data Integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-services-introduction.htm)
on Qlik Help.

## Understanding in-memory analytics with Qlik Sense

Qlik Sense is primarily an in-memory analytics engine that updates data in apps
based on a schedule or an external trigger, like database updates. This action is referred
to as a **reload**. When users access the Qlik Sense app, they view a snapshot of this refreshed
data instead of querying the data source directly, resembling a cached version stored by
Qlik Cloud.

Where there are requirements for fast-moving, or large datasets, it is possible
to leverage direct-to-database hybrid models with
approaches such as [dynamic views](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DynamicViews/dynamic-views.htm), [on-demand apps](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/Manage-big-data.htm), SQL generation
via [direct query](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/direct-access-with-direct-query.htm),
or some combination such as [direct query with on-demand drill down](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/create-odag-links-direct-query.htm).

As a rule, land the data into, or in close proximity to, your Qlik Cloud tenant.
Minimizing the distance and number of transfers reduces both complexity and cost.

In Qlik Cloud, analytics reloads are limited to a maximum duration of 3 hours. Exceeding
reload concurrency limits results in reloads being queued for up to 6 hours. If either limit
is hit, your reload will fail.

## Application engine placement

Applications are placed on compute engines based on calculated metrics that define how much
compute is required for that app. This applies to both reloads and consumption. Qlik Cloud
automatically determines the appropriate engine size based on the app's resource requirements.

There are some use cases where you need to pin applications to larger engine sizes than would
be automatically assigned. This is particularly important when you have large chart objects that
generate large hypercubes, which consume all memory on the pod and crash the app. By pinning
an app, you control the size of the engine for both reloads and consumption.

As long as the app is in a space with [Large Apps support](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/large-app-support.htm)
enabled, it will be reloaded or run on the selected engine. If you disable Large Apps
support on the space, the app will be placed on a standard engine and may fail during reload
or consumption.

Apps on pinned engines use large app engines and consume large app capacity. You can track
this consumption through the standard consumption events, which are the
[quota events in the API specification section](https://qlik.dev/apis/event/quotas/).

For more information about pinning applications to specific engine sizes, see
[Pin applications to engine sizes](https://qlik.dev/manage/analytics-applications/analytics-engine-size-override).

## Analytics reload concurrency

Your contract specifies the number of concurrent reloads allowed
in Qlik Cloud. This is per entitlement, meaning that if you are entitled to 30
concurrent reloads in your contract, this is the total you will have access to,
regardless of the number of tenants you have deployed.

Analytics reload concurrency refers to the number of Qlik Sense apps that
can be reloaded at the same time. This metric is not impacted by background
tasks related to other capabilities such as data integration, alerts, reports, and AI.
It is exclusively for the analytics dashboard and any data preparation done in Qlik script
via schedule, the hub, or API (including reloads via Qlik Automate).

You can think of 30 concurrent reloads as 30 lanes available all day. So you have
`30 concurrent reloads * 24 hours in a day * 60 minutes in an hour = 43,200 reload minutes`
in a normal day. How you choose to use these credits is up to you, and as your deployment
scales you'll need to design for efficiency. These examples demonstrate how many
apps you could sustain at different reload frequencies and durations.

| Average reload duration (minutes) | Reload frequency | Number of apps |
| --------------------------------- | ---------------- | -------------- |
| 5                                 | Once daily       | 8640           |
| 5                                 | Every 6 hours    | 2160           |
| 5                                 | Every 2 hours    | 720            |
| 5                                 | Hourly           | 360            |
| 30                                | Once daily       | 1440           |
| 30                                | Every 6 hours    | 360            |
| 30                                | Every 2 hours    | 120            |
| 30                                | Hourly           | 60             |
| 60                                | Once daily       | 720            |
| 60                                | Every 6 hours    | 180            |
| 60                                | Every 2 hours    | 60             |
| 60                                | Hourly           | 30             |

As an example, if you have a requirement to reload all of your apps every two hours, and they
take 30 minutes on average to reload, you'll be able to support 120 apps in the environment.

> **Note:** These figures are estimates.
> You should test and verify how your deployment  performs before rolling out your solution.
> For example, if all apps need to be reloaded in  a 6-hour window,
> you'll have only `30 concurrent reloads * 6 hours in a day * 60 minutes in an hour = 10,800 reload minutes` available.

When loading data into Qlik Cloud, consider the following recommendations:

- Use change-data-capture (CDC) or incremental load (a Qlik Sense
  term for a load strategy loading only changed data) to minimize data
  moved from the source into Qlik Cloud.
- Store data close to the app in the Qlik Cloud tenant using the most efficient
  file format. In most cases, this is Parquet file format in data-files, or alternatively
  an AWS S3 bucket in the same region as the tenant.
- Minimize data-transfer time by optimizing the data sources for maximum throughput,
  staggering requests to reduce concurrency, or computing the model in a persisted
  table in the data source to reduce compute duration.
- Minimize the number of apps per customer where possible, as the analytics reload
  queue carries a certain overhead, resulting in delays between one app reload
  completing and the next beginning. Additionally, other system processes may impact
  the load process.
- When storing data in Qlik Cloud, aim for fewer, larger data files when apps load from
  large data sets. For example, consider organizing transactional records into separate
  data files per transaction month if storing 36 months of history. This approach balances
  the file size, the number of files, and how many files need to be updated on
  each reload.

## Next steps

Now that you've learnt about how reloads and concurrency works, explore further
by learning how to:

- [Pin applications to engine sizes](https://qlik.dev/manage/analytics-applications/analytics-engine-size-override)
- [Manage task chaining using webhooks in Qlik Automate](https://qlik.dev/manage/analytics-applications/task-chaining-automations)
- [Manage task chaining using polling with qlik-cli](https://qlik.dev/manage/analytics-applications/task-chaining-qlik-cli)
