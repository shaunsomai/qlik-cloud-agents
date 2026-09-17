---
source: https://qlik.dev/manage/oem/operate/maintenance/
last_updated: 2026-05-27T18:16:42+01:00
---

# Maintenance activities

This section covers routine maintenance activities to keep your Qlik Cloud deployment optimized, clean, and
well-governed. These activities complement your monitoring efforts by taking action on the insights you gather.

## Maintenance activities by cadence

The table below organizes maintenance activities by recommended frequency. Click on any item to jump to detailed
instructions on how to perform the task and what tools to use.

| Monthly                                                           | Quarterly                                                     | Yearly                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| [Remove unused data connections](#remove-unused-data-connections) | [Curate extensions](#curate-extensions)                       | [Plan disaster recovery](#plan-disaster-recovery)           |
| [Remove unused spaces](#remove-unused-spaces)                     | [Flag unused sheets](#flag-unused-sheets)                     | [Practice recovery processes](#practice-recovery-processes) |
| [Disable unused automations](#disable-unused-automations)         | [Optimize sheet order](#optimize-sheet-order)                 |                                                             |
|                                                                   | [Quarantine unused apps](#quarantine-unused-apps)             |                                                             |
|                                                                   | [Remove unused private sheets](#remove-unused-private-sheets) |                                                             |
|                                                                   | [Optimize data files](#optimize-data-files)                   |                                                             |

## Monthly maintenance activities

### Remove unused data connections

Clean up data connections that are no longer being used by any applications.

If you have tagged connections with the release version, this simplifies this process significantly as you can simply
iterate all connections on every tenant and remove all connections that are not tagged with the current release version.

**What to do:**

- Identify data connections not used by any apps
- Validate with connection owners before deletion
- Remove connections that are confirmed as unused
- Document any connections being kept for future use

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer) to identify unused data connections
- [Data Connections API](https://qlik.dev/apis/rest/data-connections/) to list all connections

**How to maintain:**

1. Identify connections that aren't used by any applications using the App Analyzer, and verify these connections are
   not used by other services, such as Qlik Answers, data integration projects, etc
2. Contact connection owners to confirm they're no longer needed. In a programmatic deployment, they will likely be
   owned by an OAuth bot user
3. [Delete unused connections](https://qlik.dev/manage/data-connections/delete-data-connections/) using the Data Connections API
4. Document the cleanup in your change log

**Automation approach:**

Use the built-in automation template "Alert app owners and Tenant Admins about orphaned data connections" to identify
candidates, then create a follow-up automation to remove connections after owner confirmation.

If you tag connections with a release version at deployment time, you can iterate all connections across tenants and
remove any not tagged with the current release, without needing to track individual connection IDs. See
[tagging connections at deployment](https://qlik.dev/manage/oem/product-development/dtap-environments/#tag-connections-with-the-release-version)
for how to set these tags when deploying.

### Remove unused spaces

Identify and remove spaces that are no longer actively used.

**What to do:**

- Find spaces with no recent activity
- Identify empty or near-empty spaces
- Validate with space owners before deletion
- Archive any content that should be preserved

**Where to get this information:**

- [Spaces API](https://qlik.dev/apis/rest/spaces/) to list all spaces
- [Items API](https://qlik.dev/apis/rest/items/) to list all first-level resources in a space such as apps, assistants, scripts, etc
- [Data connections API](https://qlik.dev/apis/rest/data-connections/) to list all connections in the space
- [Data files API](https://qlik.dev/apis/rest/data-files/) to list all data files in the space
- [Audits API](https://qlik.dev/apis/rest/audits/) for space activity events

**How to maintain:**

1. Query all spaces and their last activity dates
2. Identify spaces with no activity in the past 90 days
3. Contact space owners to confirm they're no longer needed
4. Delete unused spaces using the Spaces API. If the space contains content, resources must be deleted first to avoid
   orphaning content.

### Disable unused automations

Turn off automation workflows that are no longer needed or haven't run in a long time. This helps to reduce risk of
accidental or malicious execution of these workflows.

**What to do:**

- Identify automations that haven't run in 60+ days
- Disable automations confirmed as no longer needed
- Document why automations are being disabled
- Keep disabled automations for 90 days before deletion

**Where to get this information:**

- [Audits API](https://qlik.dev/apis/rest/audits/) for automation execution events
- [Automation Analyzer](https://github.com/qlik-oss/qlik-cloud-automation-analyzer) monitoring app
- [Automations API](https://qlik.dev/apis/rest/automations/) to query automation status
- Built-in automation template: "Alert on automations without runs in the last X days"

**How to maintain:**

1. Review the automation health report to identify inactive automations
2. Contact automation owners to confirm they're no longer needed
3. Disable automations using the Automations API
4. After 90 days, delete disabled automations if no objections
5. Document the cleanup in your automation inventory

**Automation approach:**

```bash
# Disable automation via API
curl "https://your-tenant.us.qlikcloud.com/api/v1/automations/{id}/actions/disable" \
  -X POST \
  -H "Authorization: Bearer <access_token>"
```

***

## Quarterly maintenance activities

### Curate extensions

Review and curate the extensions deployed across your tenants to ensure security and maintainability.

**What to do:**

- Audit all deployed extensions
- Remove outdated or vulnerable extensions, including deprecated visualization objects
- Update extensions to latest versions
- Consolidate duplicate extensions
- Verify extension governance compliance

**Where to get this information:**

- [Extensions API](https://qlik.dev/apis/rest/extensions/) to list deployed extensions
- [Engine APIs](https://qlik.dev/apis/json-rpc/qix/) to identify which apps use which extensions (or leverage a toolkit such as
  [qlik-cli](https://qlik.dev/toolkits/qlik-cli/))
- Deprecated visualization events from the [Audits API](https://qlik.dev/apis/rest/audits/), which are surfaced in the
  [Qlik Cloud App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)

**How to maintain:**

1. Query all extensions using the Extensions API
2. Identify extensions that are outdated or have known vulnerabilities, including deprecated visualization objects
3. Check for duplicate extensions (same capabilities, different names)
4. Determine which applications depend on each extension, and if the application is still using the extension
5. Remove or update extensions as needed
6. Communicate changes to affected app owners

### Flag unused sheets

Identify sheets within applications that are never accessed by users.

As the number of sheets in an application grows, it can take longer to open the application. Additionally, backups and
restores may be more complicated if there are many orphaned or irrelevant sheets present. Regular sheet cleanup helps
maintain optimal application performance and simplifies management operations.

**What to do:**

- Analyze sheet-level usage across applications
- Flag sheets with no access in the past 90 days
- Recommend sheet cleanup to app owners
- Track sheet removal and adoption improvements

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer) with sheet-level usage data
- [Audits API](https://qlik.dev/apis/rest/audits/) filtered for sheet open events
- Application structure via Engine API sessions

**How to maintain:**

1. Review sheet usage reports in the App Analyzer
2. Identify sheets with zero or minimal access
3. Notify app owners with recommendations
4. Follow up after 30 days to confirm sheet removal or retention

**Important considerations:**

- Community sheets (published by users) are often less governed
- Base sheets (created by app owner) may be strategic even if infrequently used
- Consider seasonal usage patterns before flagging sheets

### Optimize sheet order

Reorganize sheet order within applications to improve user experience and adoption.

**What to do:**

- Analyze sheet access patterns within apps
- Reorder sheets to put most-accessed sheets first
- Create logical groupings of related sheets
- Remove or hide deprecated sheets

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer) for sheet usage metrics
- Application structure via Engine API
- User feedback and surveys

**How to maintain:**

1. Identify applications with poor sheet organization
2. Analyze which sheets users access most frequently
3. Use the Engine API or Qlik Cloud UI to reorder sheets
4. Place high-value, frequently accessed sheets at the top
5. Group related sheets together for better navigation
6. Monitor adoption changes after reordering

**Automation approach:**

While sheet reordering typically requires manual review for UX decisions, you can automate the analysis:

- Pull sheet access counts from monitoring apps
- Generate recommended sheet orders based on usage
- Present recommendations to app owners for manual implementation

### Quarantine unused apps

Move unused applications to a quarantine space before permanent deletion.

Application quarantine is particularly relevant in scenarios where customers create their own applications. While this
isn't necessarily a common part of OEM usage, if you do enable customer-created apps, you'll want to ensure that
you don't have unbounded growth on your customer tenants. Implement a policy to prevent tenants from being littered
with irrelevant apps, which could mislead users and clutter up navigation.

**What to do:**

- Identify apps with no access in 90+ days
- Move apps to a designated quarantine space
- Notify app owners of pending deletion
- Delete apps after 90-day quarantine period if no objections

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) for usage data
- [Apps API](https://qlik.dev/apis/rest/apps/) for app metadata and moves
- Built-in automation template: "Alert app owners about apps that haven't been accessed in X days"

**How to maintain:**

1. Create a dedicated "Quarantine" or "Pending Deletion" space
2. Query apps with no access in the past 90 days
3. Use the Apps API to move apps to the quarantine space
4. Send notifications to app owners about pending deletion
5. After 90 days in quarantine, delete apps with no objections
6. Export app metadata before deletion for record keeping

**API approach:**

```javascript
// Move app to quarantine space
PUT /api/v1/apps/{appId}/space
{
  "spaceId": "{quarantineSpaceId}"
}

// After 90 days, delete the app
DELETE /api/v1/apps/{appId}
```

### Remove unused private sheets

Clean up private sheets created by users that are no longer being accessed.

**What to do:**

- Identify private sheets with no access in 90+ days
- Notify sheet owners before deletion
- Delete abandoned private sheets
- Track storage savings from cleanup

**Where to get this information:**

- [App Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) which provides overall usage data for all
  sheets, but will not list sheets not accessed
- Engine API to query sheet metadata for all sheets irrespective of whether accessed
- [Audits API](https://qlik.dev/apis/rest/audits/) for sheet access events

**How to maintain:**

1. Query all private sheets across applications using the engine API
2. Identify sheets with no access in 90+ days using the audits API usage data
3. Check if sheet owners are still active users
4. Send notifications to sheet owners
5. Delete sheets using the Engine API after confirmation period

**Important considerations:**

- Private sheets are owned by individual users
- Inactive user's sheets are often orphaned, unless they have a published status of `true`, in which case they are
  community sheets, visible to all app users. Sheets with an approved status of `true` are base sheets and cannot
  be orphaned
- Consider whether sheets contain valuable work before deletion
- Document the cleanup policy clearly for users

### Optimize data files

Review and optimize data files used in your data pipelines. Data files are any files stored in the tenant, such as QVD,
Parquet, text, CSV, and other formats.

Consider storing data files in the same space as the application that's using them if you have a simple app
architecture, or leverage managed data storage spaces if you're allowing users to consume from those data files.
Ensure that you trim and maintain data files so that they don't grow over time, exposing more data than required to
the end customer. Additionally, if you orphan data files (which can happen if you're doing something like a time-based
partitioning strategy), make sure you have cleanup processes to remove that lost or unmanaged data.

**What to do:**

- Identify large or slow-loading data files
- Optimize data file structure and compression
- Remove unused data files
- Consolidate redundant data files
- Clean up orphaned data files from time-based partitioning

**Where to get this information:**

- [Reload Analyzer](https://github.com/qlik-oss/qlik-cloud-monitoring-apps) for reload performance
- [Lineage API](https://qlik.dev/apis/rest/lineage-graphs/) to identify data file usage
- [Data files API](https://qlik.dev/apis/rest/data-files/) to list all data files and their last modification date

**How to maintain:**

1. Review reload performance to identify slow data file operations
2. Analyze data file sizes and growth trends
3. Optimize data file creation scripts:
   - Use optimized loads where possible
   - Reduce unnecessary columns
   - Apply appropriate compression
4. Remove data files that are no longer referenced in any apps
5. Consolidate data files with duplicate or overlapping data

**Best practices:**

- Store data files in Managed Spaces for better access control
- Maintain data file documentation (source, refresh schedule, consumers)
- Monitor data file storage consumption monthly
- Test data file changes in non-production environments first

## Yearly maintenance activities

### Plan disaster recovery

Develop and update your disaster recovery plan for Qlik Cloud deployments. While Qlik handles automated disaster
recovery of the overall infrastructure, tenants, and content, it's sensible and pragmatic to maintain your own content
backups. These backups help you recover from specific scenarios like automation failures, accidental deletions by your
customers, or unintended content changes caused by users.

In a large part, your core processes and automation will redeploy most of the tenant, however user created content
needs to be considered.

**What to do:**

- Document recovery time objectives (RTO) and recovery point objectives (RPO)
- Identify critical applications and dependencies
- Establish backup and restore procedures
- Define roles and responsibilities for recovery scenarios
- Document tenant restoration procedures

**Where to get this information:**

- [Tenant management documentation](https://qlik.dev/manage/tenants/)
- Application inventory from monitoring apps
- Data connection documentation
- Integration dependencies

**How to maintain:**

1. Review and update your disaster recovery plan annually
2. Identify critical applications and their dependencies
3. Document backup procedures for tenant metadata:
   - Export app metadata and IDs
   - Document data connection configurations
   - Archive space structures and permissions
4. Define recovery procedures for different scenarios:
   - Accidental tenant deletion
   - Data corruption
   - Security incidents
5. Establish communication protocols for incidents
6. Document external dependencies (data sources, integrations)

**Key considerations for Qlik Cloud:**

- Qlik Cloud handles infrastructure redundancy automatically
- Focus on metadata, configuration, and application backups
- Use monitoring apps to maintain application inventories
- Export critical data to external storage for retention
- Plan for tenant-level restoration scenarios

### Practice recovery processes

Test your disaster recovery procedures to ensure they work when needed.

**What to do:**

- Conduct disaster recovery drills
- Test tenant backup and restore procedures
- Validate application recovery processes
- Update recovery documentation based on learnings
- Train team members on recovery procedures

**Where to get this information:**

- Your disaster recovery plan
- [Tenant management procedures](https://qlik.dev/manage/tenants/)
- Backup data from monitoring applications
- Recovery runbooks and documentation

**How to maintain:**

1. Schedule annual disaster recovery drills
2. Select test scenarios (for example, accidental app deletion, tenant misconfiguration)
3. Execute recovery procedures using test data
4. Time the recovery process and compare to RTO/RPO targets
5. Document issues encountered and lessons learned
6. Update disaster recovery plan with improvements
7. Train team members on updated procedures

**Test scenarios to practice:**

- Restore a deleted application from metadata backup
- Recreate data connections from documentation
- Rebuild space structures and permissions
- Recover from accidental user deletion
- Restore monitoring app data after tenant deletion

**Success criteria:**

- Recovery completes within RTO targets
- All team members understand their roles
- Documentation is clear and complete
- Procedures can be executed by multiple team members
- Lessons learned are incorporated into the plan

## Data handling and cleanup best practices

**General guidelines for maintenance activities:**

1. **Always communicate**: Notify affected users before making changes
2. **Document everything**: Keep records of what was cleaned up and why
3. **Provide grace periods**: Give users time to object before deleting content
4. **Backup first**: Export metadata before permanent deletions
5. **Track metrics**: Measure storage savings and performance improvements
6. **Automate with human review**: Use automation for identification, but often require
   human approval for deletion

**Compliance considerations:**

When performing maintenance activities, remember to:

- Follow any data retention policies in your customer contracts
- Track data handling for compliance and audit purposes
- Maintain metadata exports even after resource deletion
- Document cleanup activities for governance reporting

For more information on data handling, see [Data privacy and security](https://qlik.dev/manage/oem/privacy-security/data-access).

## Next steps

**Ready to continue?** → [Entitlement management](https://qlik.dev/manage/oem/operate/entitlement-management/)
