---
source: https://qlik.dev/manage/access-control/default-roles/
last_updated: 2026-01-26T15:49:02+01:00
---

# Default roles

> **Note:** To learn about access control in Qlik Cloud, read the [access control overview](https://qlik.dev/manage/access-control/).

Default roles (also known as security roles) are the roles which come out of the box
on your tenant, and which cannot be edited or deleted. Some roles will be hidden and
unavailable to assign to users if you do not have the corresponding feature in your
subscription.

| UI name                           | API name                         | Role level | Permission type |
| --------------------------------- | -------------------------------- | ---------- | --------------- |
| Analytics Admin                   | `AnalyticsAdmin`                 | Admin      | Permissive      |
| Audit Admin                       | `AuditAdmin`                     | Admin      | Permissive      |
| Automation Creator                | `AutomationCreator`              | User       | Permissive      |
| Automl Deployment Contributor     | `AutomlDeploymentContributor`    | User       | Permissive      |
| Automl Experiment Contributor     | `AutomlExperimentContributor`    | User       | Permissive      |
| Collaboration Platform User       | `CollaborationPlatformUser`      | User       | Permissive      |
| Data Admin                        | `DataAdmin`                      | Admin      | Permissive      |
| Data Product Manager              | `DataProductManager`             | User       | Permissive      |
| Data Services Contributor         | `DataServicesContributor`        | User       | Permissive      |
| Data Space Creator                | `DataSpaceCreator`               | User       | Permissive      |
| Embedded Analytics User           | `EmbeddedAnalyticsUser`          | User       | Restrictive     |
| Managed Space Creator             | `ManagedSpaceCreator`            | User       | Permissive      |
| Private Analytics Content Creator | `PrivateAnalyticsContentCreator` | User       | Permissive      |
| Shared Space Creator              | `SharedSpaceCreator`             | User       | Permissive      |
| Steward                           | `Steward`                        | User       | Permissive      |
| Tenant Admin                      | `TenantAdmin`                    | Admin      | Permissive      |

You can use the APIs to [assign roles to users or groups](https://qlik.dev/manage/access-control/manage-roles/),
or [create custom roles](https://qlik.dev/manage/access-control/custom-roles/) if you need
specific permissions for your users.
