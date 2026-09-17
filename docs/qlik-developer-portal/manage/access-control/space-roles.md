---
source: https://qlik.dev/manage/access-control/space-roles/
last_updated: 2025-09-23T15:01:34+01:00
---

# Space roles

> **Note:** To learn about access control in Qlik Cloud, read the [access control overview](https://qlik.dev/manage/access-control/).

Space roles are the roles which provide access to resources on a space-by-space basis.

| UI name                       | API name        | Supported in shared space | Supported in managed space | Supported in data space | Supported in fine-grained share |
| ----------------------------- | --------------- | ------------------------- | -------------------------- | ----------------------- | ------------------------------- |
| Can view                      | `consumer`      | Yes                       | Yes                        | Yes                     | Yes                             |
| Can contribute                | `contributor`   | No                        | Yes                        | No                      | Yes                             |
| Can consume data              | `dataconsumer`  | Yes                       | Yes                        | Yes                     | No                              |
| Can manage                    | `facilitator`   | Yes                       | Yes                        | Yes                     | No                              |
| Can operate                   | `operator`      | No                        | Yes                        | Yes                     | No                              |
| Can edit                      | `producer`      | Yes                       | No                         | Yes                     | No                              |
| Can publish                   | `publisher`     | No                        | Yes                        | Yes                     | No                              |
| Has restricted view           | `basicconsumer` | No                        | Yes                        | No                      | Yes                             |
| Can edit data in applications | `codeveloper`   | Yes                       | No                         | No                      | No                              |
| Can view data                 | `datapreview`   | No                        | No                         | Yes                     | No                              |

Space roles are assigned via the [Spaces API](https://qlik.dev/apis/rest/spaces/).
Available roles vary by space type. Roles are case-sensitive, and
the API name may differ from the name in the user interface.
