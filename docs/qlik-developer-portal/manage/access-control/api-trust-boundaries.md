---
source: https://qlik.dev/manage/access-control/api-trust-boundaries/
last_updated: 2026-04-29T13:39:58Z
---

# API access control and trust boundaries

## Introduction

Qlik Cloud provides multiple interfaces for accessing platform capabilities:
the Qlik Cloud UI, REST and JSON-RPC APIs, and programmatic integrations.

These share the same underlying access control model.
However, the Qlik Cloud UI represents documented, warranted product behavior with specific controls and
restrictions, while the APIs expose a broader capability surface.
Sometimes, features may be released via API before they are brought into the UI.
In all cases, use the APIs per the documented product behaviors.

This guide is for security administrators, operations teams, system integrators,
and developers implementing integrations.
You should be familiar with [Qlik roles](https://qlik.dev/manage/access-control/default-roles/),
[OAuth scopes](https://qlik.dev/authenticate/oauth/scopes/), and REST API basics.
If you're new to Qlik access control, start with the [Access control overview](https://qlik.dev/manage/access-control/).

> **Quick reference: The trust boundary in three points:**
>
> - **UI:** The designed product experience. Documented, warranted behavior with guardrails that reflect intended
>   usage patterns
> - **API:** A documented, warranted extension of the platform, intended to be used in conjunction with UI documentation
>   and API specifications. Provides access to a broader capability surface than the UI exposes
> - **API credentials:** Generally honor role assignments.
>   The exception is the Embedded Analytics User role, which restricts UI access only.
>   Users assigned this role retain full API access regardless.
>   If authenticated via OAuth, access is filtered by requested OAuth scopes.

## Understanding the trust boundary

The trust boundary is the difference in how the Qlik Cloud UI and the REST/JSON-RPC
APIs enforce the same underlying permissions model.

**Why this matters:** Both layers enforce the same permissions, but the *mechanism* differs.
If a user has a permission, the API validates and allows the operation regardless
of whether a UI affordance exists. This is by design, not a security gap.

### The UI layer

The UI enforces access control through documented product workflows:

- Role-based access control at the tenant and space level
- Content-level permissions and fine-grained sharing restrictions
- UI-level action restrictions (for example, hiding delete buttons for users without delete permission)
- OAuth client scope filtering
- Specific workflows and validation steps

### The API layer

The Qlik Cloud UI is itself built on these same APIs - an access token grants the same fundamental
access in both UI and API contexts. The differences are in presentation and workflow coverage:

- The UI presents a curated view of API responses; the API may return additional fields and
  metadata you won't see in the UI
- The UI maps platform capabilities to documented product workflows.
  Published API endpoints are supported for their documented purposes, but APIs
  may allow undocumented operation combinations not represented in the UI or product documentation.
  These custom workflows can depend on behaviors outside the intended product model,
  and those behaviors may change as the platform evolves.
  To reduce the risk of future impact, integrations should follow documented workflows
  and usage patterns wherever possible.
- API access uses the same permission model (scopes, roles, content-level access), without
  UI-level workflow constraints

> **UI restrictions are not security boundaries:** UI-level restrictions, such as hiding delete buttons to prevent accidental app
> deletion, are user experience affordances, not security controls.
> If a user has the underlying permission (scope or role), they can perform the
> operation via the API, regardless of UI presentation.
>
> For example, a user might be prevented from deleting an app in the UI, but if
> they have delete permission, they can still delete it via the API.
>
> Similarly, API responses may include fields and metadata not presented in the UI.
> If a user has permission to access a resource, receiving additional fields in the
> API response is expected behavior, not a data exposure vulnerability.
>
> This is expected behavior, not a security bypass.

## API access control principles

### API credentials represent direct platform access

When you issue an API key or OAuth credentials to a user or service account, you
are granting them direct, programmatic access to the Qlik Cloud platform.
Most roles apply equally to API access as they do to UI access. The one
exception is the Embedded Analytics User role, which restricts UI access only.

Treat API credentials with privilege commensurate with platform access:

- Manage API credentials with the same rigor as administrative access
- Consider the principle of least privilege: grant only the scopes and roles
  actually needed for the integration
- Rotate credentials
- Audit API usage through tenant audit logs
- Do not embed credentials in client-side code or version control

### Service accounts and privilege escalation

Service accounts (OAuth bot users and API key users) inherit permissions from their
assigned roles but are not limited to UI workflows.

**Example:** A service account backing an Model Context Protocol (MCP) server that manages tenant-wide
configurations needs `TenantAdmin` role. This gives it full administrative access via
the API, including operations not visible in the UI.

Treat service account assignments with the same rigor as direct admin access.
Audit them on a regular basis and revoke immediately when integrations are retired.

### OAuth scopes further constrain API access

OAuth scopes filter what an API client can do, as described in the [OAuth and requesting
scopes](https://qlik.dev/authenticate/oauth/scopes/) documentation. Within the scopes granted, the API
provides full access to the capability surface, not just operations visible in a specific UI.

**Key point:** OAuth scopes and user role permissions work together. The most restrictive
constraint applies.

For example, if a service account has `TenantAdmin` role but only
`apps:read` scope, it can only read apps, not modify them, despite having
administrative role.

**Examples:**

- An OAuth client with `apps:read` scope can list all apps accessible to the user,
  but the API may also return metadata or filter options not exposed in the UI
- An OAuth client with `spaces:manage` scope can perform any space management
  operation the user is permitted to do, via the API, regardless of whether that
  operation is available in the UI

## Multiple client types on the same API surface

All client types access Qlik Cloud through the same underlying API surface and
inherit the same access model.

They all use the same permission model (roles, scopes, content-level access).
They all see the same capability surface.
Therefore, any operation accessible to one client type via the API is accessible
to another, subject to the same permission checks.

> **MCP integrations are not sandboxed:** MCP servers access Qlik Cloud via the same REST API as any other integration.
> They are not sandboxed or restricted to a specific API surface.

## Permission caching and session lifecycle

Qlik Cloud caches permissions during user sessions to ensure performance at scale.
Understanding when permissions are refreshed is critical for access control.

> **Permission changes don't take effect immediately:** If a user's role or permissions change while they are signed in, those changes
> may not take effect until they sign out and back in or their session expires.
>
> For urgent permission revocation, ensure affected users sign out.
> Session timeout alone is too slow for sensitive scenarios.

### When permissions refresh

Permissions are refreshed when:

- A user logs in (initial authentication)
- A user's session expires

Permissions are not continuously refreshed during a session.

### Implications for administrators

- **Audit trail timing:** Audit logs reflect the permissions active at the time
  of the action, not permissions at the time of audit review.
  This can make it difficult to determine whether a user should have had access.
- **User communication:** When revoking permissions, tell users to sign out and
  back in immediately. Changing their role is not sufficient.
- **IdP sync delays (SCIM organizations):** If using IdP-based role assignment,
  permission changes may have additional delays depending on your directory sync frequency.
  Check with your IdP administrator.

This caching behavior applies to:

- User default permissions
- System roles and custom role assignments
- Group memberships (if groups are used for role assignment)
- OAuth client scope grants (for OAuth clients)

> **API tokens and permission caching:** API keys and long-lived OAuth tokens do not expire based on session timeouts.
> Token expiry varies by type:
>
> - OAuth tokens: 6-hour expiry
> - API keys: User-configurable expiry, up to several years
> - OAuth client credentials: No configured expiry
>
> Permissions are evaluated at request time based on current role and scope assignments, not cached from a session.

### IdP integration: Session timeout and re-authentication

If you use an external IdP for authentication, Qlik Cloud session expiry and IdP session expiry
are independent:

- **Qlik Cloud session timeout is configurable.** Tenant administrators can adjust it via the
  [Authentication Settings API](https://qlik.dev/apis/rest/core/auth-settings/).
- **Session expiry does not force IdP re-authentication.** If a Qlik Cloud session expires but
  the user's IdP token is still valid, they can sign back in without re-authenticating at the
  IdP. Permissions are refreshed at sign-in, but the user may not be prompted for credentials.
- **To force IdP re-authentication on every session expiry,** align the Qlik Cloud session
  timeout to your IdP's token time-to-live (TTL). This ensures users must re-authenticate at the IdP each
  time a Qlik Cloud session expires.

## Guidance for administrators

### Treat API credentials as high-privilege access

API credentials are not equivalent to UI logins. They are programmatic access
credentials that grant direct platform access and must be managed with heightened
security discipline, comparable to administrative credentials.

1. **Manage credential lifecycle:** Rotate API keys and OAuth secrets on a schedule.
   Protect them in transit and at rest using environment variables, secrets managers, or HSM.
   If a credential is committed to version control, immediately revoke it and issue a new one.
   Revoke all credentials when integrations are retired.

2. **Apply least privilege:** Grant only the scopes and roles actually needed.
   For example, if an integration only reads apps, grant `apps:read` scope, not
   broader scopes or administrative roles.

3. **Audit and monitor:** Review audit logs for service account activity to detect
   unusual patterns or unexpected access. See [Audits API](https://qlik.dev/apis/rest/audits) for details.

4. **Verify assignments:** Verify each service account has only the roles it needs.
   A service account's access is not limited by the UI role of the user who created it.

### Permission change communication

When revoking or modifying user permissions, communicate to affected users:

- The change may not take effect immediately if they are signed in
- They should sign out and back in to refresh permissions
- For urgent revocation, the primary enforcement mechanism is session timeout

> **Evaluating API capabilities:** When assessing API operations or security findings: API access to operations not
> visible in the UI is by design if the user holds the underlying permission
> (scope or role). The trust boundary is the API permission model, not UI
> visibility.

## Related resources

- [Access control in Qlik Cloud](https://qlik.dev/manage/access-control/): Comprehensive guide to
  Qlik Cloud access control mechanisms
- [OAuth and requesting scopes](https://qlik.dev/authenticate/oauth/scopes/): Scope filtering and
  OAuth client configuration
- [Default roles](https://qlik.dev/manage/access-control/default-roles/): Standard tenant roles
  and their capabilities
- [Custom roles](https://qlik.dev/manage/access-control/custom-roles/): Creating and managing
  custom roles with specific scopes
- [REST API](https://qlik.dev/apis/rest/): Full REST API reference
- [JSON-RPC (QIX) API](https://qlik.dev/apis/json-rpc/): Data and visualization API for apps
- [Roles and permissions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Manage/manage-users.htm)
  on Qlik Help
