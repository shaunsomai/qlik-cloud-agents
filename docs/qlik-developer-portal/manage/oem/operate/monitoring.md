---
source: https://qlik.dev/manage/oem/operate/monitoring/
last_updated: 2026-05-27T18:16:42+01:00
---

# Monitor your deployment

This page covers the monitoring tools available for your Qlik Cloud deployment and the recommended
activities to run against them, organized by cadence.

## Monitoring tools

### Qlik Cloud monitoring apps

The [Qlik Cloud monitoring apps](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) are the fastest way to gain
operational visibility across your tenant base. Deploy them to a single tenant to simplify credential management, and
use the [Multiple Tenant Installer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps/blob/main/automations/multipleTenantInstaller.md)
to pull data from across all your customer tenants.

| Application             | Description                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| **OEM Dashboard**       | Single pane across all customer tenants - review usage, compare trends, and spot issues at a glance. |
| **App Analyzer**        | Application performance, load times, data refresh rates, user engagement, and sheet-level usage.     |
| **Reload Analyzer**     | Reload success rates, execution times, failure causes, and duration trends.                          |
| **Automation Analyzer** | Automation run frequency, success/failure rates, third-party block usage, and execution duration.    |
| **Access Evaluator**    | User access patterns, permission assignments, and compliance visibility.                             |
| **Answers Analyzer**    | Qlik Answers usage patterns, question types, and knowledge base sizes.                               |
| **Report Analyzer**     | Report task execution, distribution patterns, and reporting service consumption.                     |

These apps build historical snapshots so no data is lost when assets are deleted. Schedule incremental reloads -
the apps are designed to pull only recent data on each run. Use Qlik Cloud's native data alerts and subscriptions to
push notifications for critical thresholds rather than polling dashboards manually.

For capacity-based subscriptions, also deploy the
[Data Capacity Reporting App](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/usage-metrics-app.htm).
This is the official, billable record of consumption - it updates once daily and is the authoritative source when any
discrepancy exists between it and other monitoring sources. Automate its deployment with the
[Capacity consumption app deployer](https://community.qlik.com/t5/Official-Support-Articles/Automate-deployment-of-the-Capacity-consumption-app-with-Qlik/ta-p/2529176)
automation template.

### Automation workflow templates

Qlik Automate includes ready-made templates for common operational alerts. These templates can be used as-is or as
starting points for custom workflows:

- [Alert on failed automation in the last X days](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-12)
- [Alert on automations without runs in the last X days](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-12)
- [Alert app owners about reload failures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-2)
- [Alert app owners and Tenant Admins about orphaned data connections](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-2)
- [Alert app owners about apps that haven't been accessed in the last 28 days](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-12)
- [Alert API key owners about API key expiration within X days](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm#anchor-12)

### Events, audits, and webhooks

Qlik Cloud's microservices publish events to an internal event bus whenever state changes - an app is created,
deleted, a reload completes, a user logs in. These events are captured in the [Audits API](https://qlik.dev/apis/rest/audits/) and
provide a complete audit trail of tenant activity.

Use the [Webhooks API](https://qlik.dev/apis/rest/webhooks/) to subscribe your external services to a subset of these events for
real-time integration. Note that events contain identifiers but not full object metadata - if you need a complete
record (for example, app size at deletion time), you must fetch that data from the relevant service while the asset
still exists.

## Monitoring activities

The table below organizes monitoring activities by recommended review frequency.

| Daily                                                     | Weekly                                                                | Monthly                                                       | Quarterly                                                           |
| --------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- |
| [Review failed automations](#review-failed-automations)   | [Review reload performance](#review-reload-performance)               | [Analyze user engagement](#analyze-user-engagement)           | [Review export activity patterns](#review-export-activity-patterns) |
| [Review reload tasks](#review-reload-tasks)               | [Monitor automation health](#monitor-automation-health)               | [Analyze application adoption](#analyze-application-adoption) | [Review tenant health metrics](#review-tenant-health-metrics)       |
| [Monitor API key expiration](#monitor-api-key-expiration) | [Check for new apps](#check-for-new-apps)                             | [Audit user access](#audit-user-access)                       | [Analyze feature adoption](#analyze-feature-adoption)               |
|                                                           | [Check for new spaces](#check-for-new-spaces)                         | [Monitor application sizing](#monitor-application-sizing)     | [Analyze extensions usage](#analyze-extensions-usage)               |
|                                                           | [Review orphaned data connections](#review-orphaned-data-connections) | [Review knowledge base sizes](#review-knowledge-base-sizes)   |                                                                     |
|                                                           | [Track inactive applications](#track-inactive-applications)           | [Monitor resource consumption](#monitor-resource-consumption) |                                                                     |

## Daily monitoring activities

### Review failed automations

Monitor automation execution failures to identify and resolve issues in automated workflows.

**What to review:** Automations that failed in the last 24 hours, error messages, and impact on dependent processes.

**Where to get this information:**

- [Automation Analyzer](https://github.com/qlik-oss/qlik-cloud-automation-analyzer) monitoring app
- [Automations API](https://qlik.dev/apis/rest/automations/) to query run status
- Automation run events via the [Audits API](https://qlik.dev/apis/rest/audits/) or [Webhooks](https://qlik.dev/apis/rest/webhooks/)
- Built-in template: Alert on failed automation in the last X days

**How to monitor:** Configure a data alert in Automation Analyzer for failed runs, or set up the automation template
to notify administrators. Review the dashboard daily for red flags, or use a subscription for email delivery.

### Review reload tasks

Monitor data reload tasks to ensure applications are refreshing successfully and on schedule.

**What to review:** Reload tasks that failed in the last 24 hours, tasks running longer than expected, and tasks
that haven't executed as scheduled.

**Where to get this information:**

- [Reload Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Reloads API](https://qlik.dev/apis/rest/reloads/) to query reload status
- Reload finished events via the [Audits API](https://qlik.dev/apis/rest/audits/) or [Webhooks](https://qlik.dev/apis/rest/webhooks/)
- Built-in templates: Alert on failed reload tasks, Create a ServiceNow incident when reload fails

**How to monitor:** Create a bookmark in Reload Analyzer showing failed reloads in the last 24 hours. Set up email
alerts for critical reload failures using data alerts or Qlik Automate workflows.

### Monitor API key expiration

Track API keys approaching expiration to prevent service interruptions.

**What to review:** API keys expiring within the next 7–14 days, their owners, and usage patterns.

**Where to get this information:**

- [API Keys API](https://qlik.dev/apis/rest/api-keys/) to query key expiration dates
- Built-in template: Alert API key owners about API key expiration within X number of days

**How to monitor:** Configure the automation template to alert key owners 7 days before expiration. Maintain an
inventory of critical API keys and their renewal schedule.

## Weekly monitoring activities

### Review reload performance

Analyze reload duration trends to identify database slowdowns, data growth, or network issues.

**What to review:** Applications with increasing reload times, reload duration compared to historical baselines,
and failed reloads and error patterns.

**Where to get this information:**

- [Reload Analyzer](https://github.com/qlik-oss/qlik-cloud-reload-analyzer) monitoring app
- [Reloads API](https://qlik.dev/apis/rest/reloads/) for reload metadata

**How to monitor:** Review the reload duration trend chart in Reload Analyzer. Identify applications with reload times
exceeding thresholds and investigate source data or connection issues.

### Monitor automation health

Review automation workflows to ensure they execute as expected. In a fully automated OEM deployment, failures are
operational issues that need fixing rather than user errors to investigate.

**What to review:** Automations without runs in the past 7 days, execution success rates, and workflow performance
trends.

**Where to get this information:**

- [Automation Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Automations API](https://qlik.dev/apis/rest/automations/) to query runs and metrics
- Built-in template: Alert on automations without runs in the last X days

**How to monitor:** Review the automation health dashboard in Automation Analyzer. Configure alerts for automations
that haven't run in 7 days.

### Review orphaned data connections

Identify data connections orphaned by space deletion or owner removal. Rare in automated deployments, but orphaned
connections contain credentials and should be removed.

**What to review:** Connections without an owner, connections in deleted spaces, and unused connections.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Data Connections API](https://qlik.dev/apis/rest/data-connections/)
- Built-in template: Alert app owners and Tenant Admins about orphaned data connections

**How to monitor:** Review connections in Reload Analyzer that are not used by any analytics apps. Note that
connections may also be used by Qlik Answers or data integration projects. Set up the automation template to alert
administrators of orphaned connections.

### Check for new apps

Review newly created applications to ensure they align with governance policies and naming conventions. Important
both for verifying correct deployments and for cases where you permit end customers to create their own apps.

**What to review:** Applications created in the past 7 days, app naming conventions, ownership, and space assignment.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Apps API](https://qlik.dev/apis/rest/apps/) to query recent apps
- App creation events via the [Audits API](https://qlik.dev/apis/rest/audits/) or [Webhooks](https://qlik.dev/apis/rest/webhooks/)

**How to monitor:** Review the new apps section in App Analyzer. Validate naming conventions, ownership, and space
assignment for recently created apps.

### Check for new spaces

Monitor newly created spaces to ensure proper configuration and access controls. In a fully automated deployment,
any space creation outside of automation should be flagged and reviewed.

**What to review:** Spaces created in the past 7 days, space types, ownership, and access control configuration.

**Where to get this information:**

- [Spaces API](https://qlik.dev/apis/rest/spaces/) to list recent spaces
- [Audits API](https://qlik.dev/apis/rest/audits/) filtered for space creation events

**How to monitor:** Query the Spaces API for recently created spaces. Validate space configuration and confirm
permissions align with security policies.

### Track inactive applications

Monitor applications that haven't been accessed recently to identify unused content and at-risk customers who are
not engaging with the product as expected.

**What to review:** Applications not accessed in the past 7 days, usage trends, and apps with no owner activity.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Audits API](https://qlik.dev/apis/rest/audits/) filtered for app access events
- Built-in template: Alert app owners about apps that haven't been accessed in X days

**How to monitor:** Review the application usage dashboard in App Analyzer. Configure the template to notify owners
of inactive apps, and identify candidates for archival or deletion.

## Monthly monitoring activities

### Analyze user engagement

Understand how users interact with your analytics platform and identify engagement patterns.

**What to review:** Active users per tenant, session duration trends, feature utilization, and login frequency.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [OEM Dashboard](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) for multi-tenant view
- [Audits API](https://qlik.dev/apis/rest/audits/) filtered for user activity events

**How to monitor:** Review user engagement metrics in App Analyzer and the OEM Dashboard. Compare month-over-month
trends in active users and identify power users and top-performing applications.

### Analyze application adoption

Track which applications and features users access most frequently to inform product decisions.

**What to review:** Most accessed applications, sheet-level usage patterns, new application adoption rates, and
usage distribution across users.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Audits API](https://qlik.dev/apis/rest/audits/) for app and sheet access events

**How to monitor:** Review the application adoption dashboard in App Analyzer. Identify top-performing and
underutilized content. Analyze adoption patterns for newly deployed applications.

### Audit user access

Review user permissions and access patterns to ensure compliance with security policies.

**What to review:** User role assignments, permission changes, and access patterns across tenants.

**Where to get this information:**

- [Access Evaluator](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Users API](https://qlik.dev/apis/rest/users/) and [Spaces API](https://qlik.dev/apis/rest/spaces/) for permission data

**How to monitor:** Review the Access Evaluator dashboard for permission anomalies. Identify users with access beyond
their normal role and confirm changes align with approved requests.

### Monitor application sizing

Ensure applications remain within their tier thresholds as data grows over time. Apps can grow through scheduled
reloads or incremental data updates, exceeding tier limits if not tracked.

**What to review:** File and memory sizes relative to tier thresholds, apps approaching or exceeding limits, and
month-over-month growth trends.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) monitoring app
- [Apps API](https://qlik.dev/apis/rest/apps/) for application metadata including size

**How to monitor:** Review the application sizing dashboard in App Analyzer. Set up alerts when apps reach 80% of
their tier capacity limits. Track month-over-month growth to predict when optimization or tier changes will be needed.

### Review knowledge base sizes

Monitor knowledge base growth to control costs and maintain optimal Qlik Answers performance.

**What to review:** Knowledge base storage consumption, document counts, and growth trends.

**Where to get this information:**

- [Answers Analyzer](https://github.com/qlik-oss/qlik-cloud-answers-analyzer) monitoring app

**How to monitor:** Review knowledge base size metrics in Answers Analyzer. Identify knowledge bases with unexpected
growth and evaluate whether document retention policies are needed.

### Monitor resource consumption

Track resource usage across tenants to optimize costs and performance relative to entitlements.

**What to review:** Capacity units consumed by tenant, consumption trends, usage relative to entitlements, and cost
allocation by customer.

**Where to get this information:**

- [Data Capacity Reporting App](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/usage-metrics-app.htm)
  for capacity subscriptions
- [OEM Dashboard](https://github.com/qlik-oss/qlik-cloud-oem-dashboard) for multi-tenant resource view

**How to monitor:** Review the capacity consumption report monthly and compare against purchased entitlements.
Identify tenants with unusual consumption patterns. For detailed guidance on tiered alert configuration and automation
examples, see [How to take control of your Qlik Cloud subscription](https://community.qlik.com/t5/Official-Support-Articles/How-to-take-control-of-your-Qlik-Cloud-subscription-a-guide-to/ta-p/2542870)
on Qlik Community.

## Quarterly monitoring activities

### Review export activity patterns

Track what users export to understand reporting patterns and data access needs.

**What to review:** Export volume by type (Excel, PDF, images), users with high export volumes, and applications
with frequent exports.

**Where to get this information:**

- [Report Analyzer](https://github.com/qlik-oss/qlik-cloud-report-analyzer) for metered report metadata
- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer) for general export activity
- [Audits API](https://qlik.dev/apis/rest/audits/) filtered for export events

**How to monitor:** Review the export activity dashboard in Report Analyzer. Identify heavy export users and analyze
patterns to inform caching or pre-generation strategies. Monitor for unusual export activity that may indicate
unintended data exposure.

### Review tenant health metrics

Conduct a comprehensive review of tenant health across all monitoring dimensions.

**What to review:** Overall tenant performance, user satisfaction indicators, system stability, and application
portfolio health.

**Where to get this information:**

- [OEM Dashboard](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) for comprehensive multi-tenant view
- All specialized monitoring apps for deep dives
- [Organization REST APIs](https://qlik.dev/apis/org-rest/) to enumerate and filter all tenants across all subscriptions in a
  single call, using an [organization-level OAuth client](https://qlik.dev/authenticate/oauth/create/create-organization-level-oauth-client).
  This is useful as a starting point when your tenant estate spans multiple subscriptions or regions.

**How to monitor:** Review the OEM Dashboard for high-level health. Identify tenants requiring attention, compare
against benchmarks, and document patterns and trends for continuous improvement.

### Analyze feature adoption

Monitor usage of platform features to inform product roadmap decisions.

**What to review:** Feature utilization across the tenant base, adoption of new features, and underutilized
capabilities.

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer) for application feature usage
- [Answers Analyzer](https://github.com/qlik-oss/qlik-cloud-answers-analyzer) for Qlik Answers adoption
- [Report Analyzer](https://github.com/qlik-oss/qlik-cloud-report-analyzer) for reporting feature usage

**How to monitor:** Review feature usage metrics across all monitoring apps. Identify features with low adoption
that may need promotion or training. Track adoption curves for recently released features.

### Analyze extensions usage

Monitor extensions deployed across your tenants to ensure proper usage and identify potential issues.

**What to review:** Extensions deployed across tenants, usage patterns, versions needing updates, and potential
security or performance concerns.

**Where to get this information:**

- [Extensions API](https://qlik.dev/apis/rest/extensions/) to list deployed extensions
- [Audits API](https://qlik.dev/apis/rest/audits/) for extension usage events

**How to monitor:** Query the Extensions API for all deployed extensions. Review usage across applications, identify
outdated extensions that need updates, and confirm deployed extensions align with governance policies.

## Data handling and off-boarding

A common requirement for product deployments is compliance with data handling terms in your customer contracts. While
you can [delete a tenant](https://qlik.dev/manage/tenants/delete-tenants/) (which purges all tenant-related data from Qlik
Cloud), you should keep track of any usage data exported to cloud file storage, other Qlik Cloud tenants, or your
own systems. This simplifies [data privacy and security](https://qlik.dev/manage/oem/privacy-security/data-access/) processes.

If you have all monitoring deployed to a single tenant, off-boarding a customer is simply a matter of archiving
their monitoring data until the retention period expires, then removing the tenant records.

## Next steps

**Ready to continue?** → [Maintenance activities](https://qlik.dev/manage/oem/operate/maintenance/)
