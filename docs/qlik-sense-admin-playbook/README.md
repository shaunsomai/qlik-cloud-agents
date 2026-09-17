# Qlik Sense Admin Playbook: Markdown summaries

76 source pages are represented by separate Markdown summaries. Subfolders mirror the playbook topic paths.

These are original concise summaries, not full transcriptions of the copyrighted website. Detailed procedures, scripts, complete tables, screenshots, and diagrams remain on the linked source pages. Every file records its source and retrieval date.

Scope: English [Qlik Sense Admin Playbook](https://help.qlik.com/en-US/qs-admin-playbook/Content/home.htm) pages, retrieved on 2026-09-16. External documentation, projects, and videos are linked as references rather than included in this collection.

[Cadence index](CADENCE.md) | [Coverage and source issues](COVERAGE.md) | [Machine-readable manifest](manifest.json)

## Using these files

- Start with [About](about.md) for how to apply the guidance.
- Browse categories below or open individual files.
- Use front matter for source attribution and cadence filtering.
- Planning subsections identify frequency inherited from a parent routine.
- Open the original page for implementation details.

## Topics

### Overview

- [Qlik Sense Admin Playbook](home.md)
- [About Qlik Sense Admin Playbook](about.md)
- [Changelog — Qlik Sense Admin Playbook](changelog.md)

### Asset management

- [Asset Management](asset_management.md)
- [Apps](asset_management/apps.md)
- [Analyze App Adoption](asset_management/apps/analyze_app_adoption.md) - Quarterly
- [Analyze App Metadata Analyzer](asset_management/apps/analyze_app_metadata_analyzer.md) - Weekly
- [Check for New Apps](asset_management/apps/check_new_apps.md) - Weekly
- [Flag Unused Base/Community Sheets](asset_management/apps/flag_unused_base_community_sheets.md) - Monthly
- [Optimize Sheet Order for Adoption](asset_management/apps/optimize_sheet_order_for_adoption.md) - Quarterly
- [Remove/Quarantine Unused Apps](asset_management/apps/remove_quarantine_unused_apps.md) - Quarterly
- [Remove Unused Private Sheets](asset_management/apps/remove_unused_private_sheets.md) - Quarterly
- [Review App Cache Warming](asset_management/apps/review_app_cache_warming.md) - Quarterly
- [Review Pinning/Load Balancing](asset_management/apps/review_pinning_load_balancing.md) - Quarterly
- [Custom Properties](asset_management/custom_properties.md)
- [Check for New/Modified Custom Properties](asset_management/custom_properties/custom_properties.md) - Weekly
- [Data Connections](asset_management/data_connections.md)
- [Analyze Data Connections](asset_management/data_connections/analyze_data_connections.md) - Monthly
- [Check for New Data Connections](asset_management/data_connections/check_new_data_connections.md) - Weekly
- [Remove Unused Data Connections](asset_management/data_connections/remove_unused_data_connections.md) - Monthly
- [Extensions](asset_management/extensions.md)
- [Analyze/Curate Extensions](asset_management/extensions/analyze_curate_extensions.md) - Quarterly
- [QVDs](asset_management/qvds.md)
- [Review/Optimize QVDs](asset_management/qvds/review_optimize_qvds.md) - Quarterly
- [Security Rules](asset_management/security_rules.md)
- [Analyze Security Rules](asset_management/security_rules/analyze_security_rules.md) - Monthly
- [Check for New/Modified Security Rules](asset_management/security_rules/check_security_rules.md) - Weekly
- [Streams](asset_management/streams.md)
- [Check for New Streams](asset_management/streams/check_new_streams.md) - Weekly
- [Remove Unused Streams](asset_management/streams/remove_unused_streams.md) - Monthly
- [Tasks](asset_management/tasks.md)
- [Analyze Tasks](asset_management/tasks/analyze_tasks.md) - Weekly
- [Check for Tasks](asset_management/tasks/new_tasks.md) - Weekly
- [Remove/Disable Unused Tasks](asset_management/tasks/remove_disable_unused_tasks.md) - Monthly

### Audit

- [Audit](audit.md)
- [Audit User Access](audit/audit_user_access.md) - Quarterly
- [Review Data Exports](audit/review_data_exports.md) - Monthly

### Backup and archiving

- [Backup & Archiving](backup_and_archiving.md)
- [Archive Old Archived Logs](backup_and_archiving/archive_old_archived_logs.md) - Quarterly
- [Verify/Execute Backups](backup_and_archiving/verify_backup_execution.md) - Monthly

### Licensing

- [Licensing](licensing.md)
- [License Maintenance](licensing/license_maintenance.md) - Monthly
- [Review License Allocations](licensing/review_license_allocations.md) - Weekly

### System planning

- [System Planning](system_planning.md)
- [Optimize Batch Window](system_planning/optimize_batch_window.md) - Quarterly
- [Plan Disaster Recovery](system_planning/plan_disaster_recovery.md) - Yearly
- [Plan/Review Upgrade Strategy](system_planning/plan_review_upgrade_strategy.md) - Yearly
- [Practice Recovery Processes](system_planning/practice_recovery_processes.md) - Yearly
- [Review Architecture/Scale Plan](system_planning/review_architecture_scale_plan.md) - Yearly
- [Architecture 101 (Components, Terminology)](system_planning/review_architecture_scale_plan/architecture_101.md) - Yearly (parent routine)
- [Example Production Architectures](system_planning/review_architecture_scale_plan/example_production_architectures.md) - Yearly (parent routine)
- [Load Balancing Concepts](system_planning/review_architecture_scale_plan/load_balancing_concepts.md) - Yearly (parent routine)
- [Resiliency & High Availability](system_planning/review_architecture_scale_plan/resiliency_ha.md) - Yearly (parent routine)
- [Review Disk Space](system_planning/review_disk_space.md) - Monthly
- [Review/Update Capacity Plan](system_planning/review_update_capacity_plan.md) - Quarterly
- [Capacity Plan: Applications](system_planning/review_update_capacity_plan/applications.md) - Quarterly (parent routine)
- [Capacity Plan: Licenses](system_planning/review_update_capacity_plan/licenses.md) - Quarterly (parent routine)
- [Capacity Plan: System](system_planning/review_update_capacity_plan/system.md) - Quarterly (parent routine)
- [Capacity Plan: Users](system_planning/review_update_capacity_plan/users.md) - Quarterly (parent routine)

### System spot checks

- [System Spot Check](system_spot_check.md)
- [Review 24 Hour Summary (Ops Monitor)](system_spot_check/24_hour_summary.md) - Daily
- [Spot-Check: Node Health](system_spot_check/nodes.md) - Daily
- [Spot-Check: Tasks](system_spot_check/tasks.md) - Daily
- [Review Expensive Objects (Telemetry)](system_spot_check/telemetry.md) - Daily

### Tooling

- [Tooling Appendix](tooling_appendix.md)
- [App Metadata Analyzer](tooling/app_metadata_analyzer.md)
- [Cache Warming](tooling/cache_warming.md)
- [Data Connection Analyzer](tooling/data_connection_analyzer.md)
- [Extension Usage Dashboard](tooling/extension_usage_dashboard.md)
- [License Monitor](tooling/license_monitor.md)
- [Operations Monitor](tooling/operations_monitor.md)
- [Qlik CLI for Windows](tooling/qlik_cli.md)
- [QVD Monitor](tooling/qvd_monitor.md)
- [Reloads Monitor](tooling/reloads_monitor.md)
- [Security Rule Analyzer](tooling/security_rule_analyzer.md)
- [Telemetry Dashboard](tooling/telemetry_dashboard.md)
