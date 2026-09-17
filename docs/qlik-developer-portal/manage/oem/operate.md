---
source: https://qlik.dev/manage/oem/operate/
last_updated: 2026-05-27T18:16:42+01:00
---

# Management and operations overview

Once your Qlik Cloud integration is deployed, you need to keep it healthy across
hundreds of customer tenants. Because you cannot log in to each customer tenant to check it
manually, operations at OEM scale means automated monitoring, automated alerting, and automated
response to common issues.

This section covers the four areas you need to address:

- **[Monitoring and observability](https://qlik.dev/manage/oem/operate/monitoring/)** - The Qlik Cloud monitoring
  apps suite provides pre-built Qlik Sense applications that aggregate usage, reload health,
  automation execution, and entitlement consumption across all your customer tenants.
  Webhooks and the Audits API let you connect this telemetry to your own monitoring stack.

- **[Entitlement management](https://qlik.dev/manage/oem/operate/entitlement-management/)** - Your Qlik contract
  defines limits on concurrent reloads, data volumes, and premium services. Tracking usage
  against these limits - and automating responses when tenants approach them - prevents
  unexpected overage.

- **[Operations and maintenance](https://qlik.dev/manage/oem/operate/maintenance/)** - Routine cleanup tasks
  (removing unused connections, spaces, automations, and extensions) keep your tenant estate
  tidy and reduce security surface area. This section organizes those tasks by recommended cadence.

- **[Backup and recovery](https://qlik.dev/manage/oem/operate/backup-recovery/)** - Qlik Cloud includes built-in
  disaster recovery for the infrastructure. Your responsibility is to store deployment configuration
  as code and, where customers create their own content, to back up application files and object
  metadata so you can restore a tenant if needed.

## Next steps

**Monitor your deployment:** → [Monitoring & observability](https://qlik.dev/manage/oem/operate/monitoring/)
