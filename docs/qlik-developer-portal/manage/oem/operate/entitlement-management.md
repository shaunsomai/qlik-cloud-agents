---
source: https://qlik.dev/manage/oem/operate/entitlement-management/
last_updated: 2026-05-27T18:16:42+01:00
---

# Entitlement management

For OEM deployments, entitlement management focuses on monitoring usage against your Qlik Cloud subscription agreement,
while also tracking your customer's usage against your set boundaries.

Qlik Cloud's architecture provides unbounded scalability for interactive analytics consumption and authoring,
eliminating
the need to monitor traditional resource constraints like user load or database performance, but there are limits
related to data refreshes and premium services which need to be controlled.

Entitlement management in an OEM deployment has two distinct concerns. The first is your
subscription agreement with Qlik: your contract sets limits on concurrent reloads, data volumes,
and premium services such as Qlik Answers questions and third-party automation runs. Staying
within those limits is your responsibility. The second concern is per-tenant usage: depending
on your billing model, you may need to track how much each customer tenant consumes and
enforce individual limits programmatically.

The tables below list the specific entitlements to monitor and the tools available for each.

> **Note:** For detailed guidance on tiered alert configuration (60/75/90% thresholds), alert setup walkthroughs in the
> Automation Analyzer and Data Capacity Reporting App, and automation examples for enforcement, see
> [How to take control of your Qlik Cloud subscription](https://community.qlik.com/t5/Official-Support-Articles/How-to-take-control-of-your-Qlik-Cloud-subscription-a-guide-to/ta-p/2542870)
> on Qlik Community. It is written for commercial customers but all the tooling and patterns apply equally to OEM
> deployments.

## Usage monitoring against entitlements

While Qlik Cloud handles all the technical scaling automatically, it's important to stay within certain constraints that
are defined by your subscription agreement. These constraints fall into two categories: subscription-level limits that
apply to all tenants, and tenant-level limits that typically apply to individual user actions.

Refer to your contract with Qlik, and depending on your subscription type:

- [Qlik Cloud Analytics (capacity-based)](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-specs-capacity.htm)
- [Qlik Sense Enterprise SaaS (user-based)](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-analytics-user-based.htm)

## Key entitlements to monitor and control

### Data boundary entitlements

| Entitlement           | Description                                                                  | Monitoring tool                           |
| --------------------- | ---------------------------------------------------------------------------- | ----------------------------------------- |
| Data transfer volume  | Monitor gigabytes of data moved by your platform                             | Data consumption report                   |
| Data for analysis     | Track data loaded into tenants (typically managed by OEM, not end customers) | Data consumption report                   |
| Large app consumption | Monitor gigabytes consumed by large applications                             | Qlik Cloud monitoring apps (App Analyzer) |

### Concurrency and processing limits

| Entitlement                 | Description                                              | Monitoring tool                                                                                              |
| --------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Concurrent app reloads      | Track analytics reload operations running simultaneously | Qlik Cloud monitoring apps (Reload Analyzer)                                                                 |
| Automation run concurrency  | Monitor concurrent automation executions                 | Qlik Cloud monitoring apps (Automation Analyzer)                                                             |
| Standard automation runs    | Track total automation executions                        | Qlik Cloud monitoring apps (Automation Analyzer)                                                             |
| Third-party automation runs | Monitor billable automation usage                        | Qlik Cloud monitoring apps (Automation Analyzer) or data consumption report for capacity-based subscriptions |

### Analytics and reporting entitlements

| Entitlement            | Description                                | Monitoring tool                               |
| ---------------------- | ------------------------------------------ | --------------------------------------------- |
| Qlik Answers usage     | Monitor questions asked and pages indexed  | Qlik Cloud monitoring apps (Answers Analyzer) |
| Qlik Predict models    | Track number of deployed predictive models | Qlik Cloud administration console             |
| Qlik Reporting Service | Monitor monthly report generation volume   | Qlik Cloud monitoring apps (Report Analyzer)  |

### Automated entitlement management

| Task                         | Description                                                                                                                                                                                                                                                          | Tool                                                                                                                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Set up automated alerts      | Configure alerts for approaching entitlement limits                                                                                                                                                                                                                  | Qlik Cloud monitoring apps (App Analyzer, Reload Analyzer, Automation Analyzer, Answers Analyzer, Report Analyzer) or data consumption report for capacity-based subscriptions |
| Automate feature disabling   | Disable features when entitlement boundaries are met:• Disable third-party runs when automation run limits are reached• Restrict report generation when premium report limits are exceeded• Disable further question answering when Answers usage limits are reached | Qlik Automate workflows                                                                                                                                                        |
| Implement usage optimization | Develop strategies based on entitlement consumption                                                                                                                                                                                                                  | Qlik Cloud monitoring apps                                                                                                                                                     |
| Plan subscription upgrades   | Analyze usage patterns to forecast capacity needs                                                                                                                                                                                                                    | Qlik Cloud monitoring apps or data consumption report for capacity-based subscriptions                                                                                         |

## Next steps

**Ready to continue?** → [Backup and recovery](https://qlik.dev/manage/oem/operate/backup-recovery/)
