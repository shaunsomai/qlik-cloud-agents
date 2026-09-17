---
source: https://qlik.dev/manage/access-control/
last_updated: 2026-04-29T13:39:58Z
---

# Overview

Qlik Cloud provides several complementary mechanisms for controlling access to
resources and capabilities. These combine to determine what an individual user - or
an integration acting on behalf of a user - can see and do.

> **API access control vs. UI:** Access control described here reflects the behavior of the Qlik Cloud user
> interface. The REST and JSON-RPC APIs may expose operations not available
> through, or restricted within, a specific UI.\
> For more information about API trust boundary and how API credentials should be treated with privilege commensurate
> with direct platform access, see the [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

Think of access control in tiers:

1. Baseline permissions
2. OAuth client scopes (for integrations)
3. Content-level access

## Baseline permissions: Tenant-wide

Every user in a tenant begins with a baseline set of permissions that apply across
the entire tenant:

1. Default user profile ("User defaults")
   - All users automatically inherit any scopes assigned here.
   - Customized by a tenant administrator, using scopes enabled for user default.
   - In the UI these appear as permissions.
   - Example: grant all users the ability to create API keys.
2. System roles (default roles)
   - Built-in roles such as `TenantAdmin`, `SharedSpaceCreator`, or `Steward`.
   - Each role maps to a bundle of scopes which cannot be customized.
   - Role must be assigned to a user or group of users.
   - Example: assigning a user the TenantAdmin role grants access to most administrative
     functions on the tenant.
3. Custom roles
   - Created by tenant administrators, using the scopes enabled for custom roles.
   - In the UI these appear as permissions.
   - Role must be assigned to a user or group of users.
   - Example: Defining specific task-oriented roles such as giving certain users the
     ability to manage AI assistants across the tenant.

Together, user defaults, system roles, and custom roles define the tenant-wide
baseline for each user.

## OAuth client scopes (integration filtering)

When a user accesses Qlik Cloud through an OAuth integration:

- The OAuth client has its own set of granted scopes.
- The client's scopes act as a filter: the user only has the intersection of their
  own permissions and the scopes assigned to the OAuth client.

This prevents an integration with limited scopes from gaining unintended elevated
privileges, even if the user themselves is an administrator.

Special cases:

- `user_default`: resolves to a dynamic set of all user scopes.
- `admin_classic`: resolves to a dynamic set of administrator scopes.

Learn more about [OAuth and requesting scopes](https://qlik.dev/authenticate/oauth/scopes/).

## Content-level access

Above the baseline tenant-wide permissions, content access is governed by:

1. Space roles
   - Spaces are the primary containers for apps, data, automations, and other assets.
   - Roles such as `Consumer`, `Contributor`, or `Operator` determine what a user
     can do inside a space.
   - Example: A user may be a `Consumer` in the Finance space and a `Contributor` in
     the Marketing space.
   - Learn more about [Working in spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm)
     on Qlik Help.
2. Fine-grained access control
   - Individual assets (select resources such as Qlik Sense apps) can also be
     shared directly with users or groups with a restricted set of space roles.
   - Used for sharing content with anonymous users.
   - Learn more about [Fine-grained access control](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/sharing-content-with-non-space-members.htm)
     and [Sharing app content with anonymous access](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/share-anonymous-access.htm)
     on Qlik Help.

> **Note:** Not all Qlik APIs implement content-level access control. Specifically, APIs serving predefined static responses
> for the Qlik user interface do not involve content-level access control.
> Authentication is the only requirement for such APIs.
> However, all APIs that hold information about customer resources implement content-level access control.

## How it all fits together

A user's effective permissions are determined by:

- Default user profile, plus any roles assigned (default or custom).
- Filtered by OAuth client scopes when accessed through an integration.
- Combined with space roles and fine-grained sharing to allow or restrict access
  to content.

Users assigned administrative roles usually have broad permissions, and may be
able to list or access content across spaces.

Regular users typically rely on space roles for their access, and may have only
minimal tenant-wide permissions.

## Access control enforcement

In Qlik Cloud, some resources reference metadata from other resources, which defines the behaviour
of the consuming resource. This design enables flexible collaborative workflows where you can separate
data governance roles from development roles, but it requires understanding how access control applies
at different stages. For example:

- A Qlik Analytics application load script or Data Flow may reference tables or columns from a data
  connection, which defines what data is loaded into the resulting Analytics app or data assets.
- An Automation may reference schemas, fields, or objects accessed using an automation connection,
  which are used to define the way the workflow runs.
  In these cases, the source resource provides metadata (such as table names or column names),
  while the consuming resource stores and uses that metadata.

### Design time vs execution time enforcement

Qlik Cloud enforces access control at execution time, not at design (reference) time.

- **Design time (reference time)**: Access to source resources is not validated when metadata
  is referenced. Once metadata is embedded into another resource, it is governed by the access
  control of the consuming resource, not the source resource.
- **Execution time**: Access control to the source resource is enforced when the consuming
  resource is executed (for example, when a script reload runs).

### Example scenario

1. A user edits a Analytics application load script and references a column from a data source
   accessed via a data connection they have access to.
2. A second user, with access to the Analytics application, but not to the data connection used
   by the first user to create the app can still edit the load script, because access is controlled
   by permissions on the script itself.
3. When the second user attempts to execute the script, it fails, because access to the data
   connection is enforced at execution time.

To prevent execution failures caused by insufficient access to consumed resources:

- Grant the executing user access to all source resources referenced by the executable resource, or
- Review permissions on the consuming resource to ensure only users with access to all dependencies
  can edit or execute it.

### Security implications

Source resources do not inherit the access control of the consuming resource.
Execution always runs with the permissions of the executing user, not the creator, with access
control being evaluated independently against both the source and consuming resource for the
executing user.

### Guidance

When using executable resources created by others, review which resources are consumed,
especially when those resources are sensitive and your permissions differ from the creator's.

When assigning scopes, space permissions, and execution rights, consider that:

- Metadata may reference resources the author no longer has access to.
- Execution uses the permissions of the current user, not the creator. This flexibility
  enables collaborative workflows and separate governance models, but it requires deliberate
  permission management to avoid unexpected execution failures or access issues.

## Where to go next

Learn:

- How to [Create and manage groups](https://qlik.dev/manage/access-control/groups),
  which simplify managing user permissions at scale.
- About the [default roles](https://qlik.dev/manage/access-control/custom-roles) available in your tenant.
- How to [create and manage custom roles, and update the default user permissions](https://qlik.dev/manage/access-control/custom-roles).
- How to [assign roles to users and groups](https://qlik.dev/manage/access-control/manage-roles).
- How to [control access to spaces and content](https://qlik.dev/manage/access-control/space-roles).
- About the available [scopes in Qlik Cloud](https://qlik.dev/manage/access-control/scopes).
