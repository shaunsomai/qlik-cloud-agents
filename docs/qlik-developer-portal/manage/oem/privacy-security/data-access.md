---
source: https://qlik.dev/manage/oem/privacy-security/data-access/
last_updated: 2026-05-27T18:16:42+01:00
---

# Data privacy & security

Tenants in Qlik Cloud can be configured to meet your organization's privacy and security
requirements. They can also be isolated to simplify offboarding, auditing, and data residency
needs.

Consider these tenant management aspects:

- Configuring your identity provider and authenticate users to the tenant
- Setting up security configuration in the tenant
- Auditing user activity
- Managing customer deactivation and off-boarding

## Identity providers and authentication

As the administrator of a tenant, you can opt to configure:

- A single interactive identity provider (Qlik Account, OIDC, or SAML)
- One or more OAuth clients (supporting embedded access to limited tenant interfaces
  or API access to the tenant, depending on the OAuth client configuration).
- One or more JSON Web Token (JWT) identity providers (supporting direct and embedded access
  to the tenant interfaces).

The recommended pattern for customers who have web apps without a back end, or
who have all users accessing a tenant in a single interactive identity provider is to:

- Deploy an OIDC or SAML identity provider containing both internal (such as
  administrators or developers) and external (end customer) users.
- Leverage OAuth SPA to authorize those users to access Qlik Cloud, if embedding the solution.

If your web app has a back end and you prefer to authenticate users through your web app
rather than redirecting to the configured identity provider, use OAuth M2M impersonation
instead of OAuth SPA.

### Interactive identity providers

A newly deployed tenant (excluding Qlik Cloud Government tenants) will be configured
for interactive logins with a Qlik Account. This allows accounts managed by Qlik
to be invited to the tenant and is also used for tenant recovery by the service
account owner if needed. Any unauthenticated user attempting to access the tenant
will be redirected to the configured interactive identity provider to log in.

You should opt to configure your own OIDC or SAML-compatible interactive identity
provider as soon as possible after deploying the tenant. This will turn off the
ability for users, other than the service account owner, to sign in to the tenant using
their Qlik Account.

Using your own identity provider provides benefits such as:

- Full control over which users can access the tenant, their authentication, and lifecycle.
- Full control and visibility of audit, logging, and governance controls provided by
  the identity provider. When using Qlik Account, you can't track events such as failed logins
  or unexpected login patterns.
- The ability to send group claims with user logins, allowing you to maintain
  most of your access control pattern in your identity provider and simplifying
  configuration in Qlik Cloud.

> **Deploy your own identity provider:** Even if it's only used by your administrator team to troubleshoot deployments and support customers, deploying your
> own identity provider is a recommended practice.
> End customers will access the tenant authenticate using JWT or OAuth configurations.

For more information about identity providers, see [Identity providers in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm)
on Qlik Help.

### OAuth clients

You can deploy multiple OAuth clients in a Qlik Cloud tenant, which support a full
range of use cases across interactive embedded, integration, and API use cases both
in the front and back ends of your application.

For embedded use cases, you will typically leverage one of the following OAuth patterns:

- OAuth SPA: leverage a configured interactive identity provider to authenticate
  the user, with the user granting login consent for the application once authenticated.
  This pattern is the most simple pattern as it doesn't require handling of secrets
  in the web application.
- OAuth machine-to-machine impersonation: for web apps with a back end, use an OAuth
  client and secret to generate a token to impersonate a user. While this pattern is similarly
  functional to using a JWT identity provider, you manage users, roles, and groups
  via API calls, read about [managing users and groups with OAuth impersonation](https://qlik.dev/embed/qlik-embed/authenticate/manage-users-groups-impersonation/).

OAuth also supports specifying user scopes when a token is requested. These scopes
can be used to further restrict the access that a user has via their roles. A scope
will not give a user more access than their roles permit.

Learn more about the various [OAuth patterns](https://qlik.dev/authenticate/oauth)
supported in Qlik Cloud.

### JWT identity providers

JWT (JSON Web Token) identity providers allow you to leverage public and private
keys to establish trust between Qlik Cloud and your application backend. Your backend
will be able to sign JWTs, which in turn can be used by clients accessing the tenant
directly or via embedded frameworks to authorize users to access Qlik Cloud.

> **Note:** When using JWTs in embedded solutions, you will need to leverage proxy solutions to mitigate for browser third-party
> blocking. Consider using OAuth instead of JWT for these use cases.

Learn more about [implementing JWT authorization](https://qlik.dev/authenticate/jwt/implement-jwt-authorization),
but consider whether you can employ [OAuth](https://qlik.dev/authenticate/oauth)
as an alternative in your project.

## Securing the tenant

Once your users have authenticated and been authorized to access the tenant,
several layers of access control define what they can see and do:

- Tenant roles: define the overall capabilities a user can access.
- Space roles: define which spaces and content a user can access.
- Section access: controls access to Qlik Sense applications, and row and field
  level data reduction.

[Tenant and space roles](https://qlik.dev/manage/access-control/) can be set via REST APIs in the
tenant. [Section access](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm) is
defined within the load script of a Qlik Sense application, and applied on reload
of that application. All can be set on to users and / or groups.

When securing the tenant, consider these good practices:

- Use groups for assigning access to roles or section access,
  with your identity provider supplying these as part of the claim each time the user
  logs in. This reduces the implementation complexity in the tenant and centralizes
  user management to your identity provider.
- Apply least privilege principles when adding roles to users in the tenant. Apply only
  necessary roles to users and use custom roles to define appropriate access if the
  default roles don't fit your use case.
- Avoid the use of user-scoped API keys, since these operate with full permissions
  of the user and can be used directly to the tenant.
- Leverage scopes with OAuth clients, applying only the scopes required for an
  OAuth client to undertake planned activities. If using machine-to-machine impersonation
  follow the [guiding principles](https://qlik.dev/authenticate/oauth/guiding-principles-oauth-impersonation).

## Audit user activity

You should aim to integrate Qlik Cloud into your monitoring and observability suite,
just as you do with your own web app. To achieve this, consider the following:

- Using your own identity provider to audit and govern user authentication attempts.
- Use OAuth token events in the Qlik Cloud tenant (and token requests from your
  web application if using OAuth machine-to-machine impersonation) to monitor authorization
  against Qlik Cloud tenants from your web application.
- Leverage Qlik Sense app open events and sheet open events (supported for direct access
  or with the `classic/app` pattern in qlik-embed) to track which assets users are
  accessing in the tenant.

## Customer deactivation and off-boarding

At the end of a customer's contract, you may need to deactivate their access, delete the
tenant, and remove all data.

As subscription owner, you can use a special set of OAuth clients to
deactivate a tenant and schedule it for deletion. When you deactivate a tenant, you set
a period between 10 and 90 days, after which the tenant is purged from Qlik
Cloud. Although you can reactivate the tenant at any point up until the purge,
once purged, there is no way of recovering data from the tenant.

Disabling a tenant will

- Block all logins and requests to the tenant.
- Pause all tasks, automations, and other activity in the tenant.

A tenant purge removes:

- All content in the tenant, such as apps, connections, credentials, and configurations.
  Ensure you have a backup of all relevant content before deletion.
- All usage information, such as events for user sessions, app usage, reloads.
  Ensure you have exported any log information that you need to keep for audit, regulatory, or
  governance requirements before tenant deletion.

Your off-boarding process should also handle deletion of any secrets used by that specific
tenant for integrations with your identity providers, systems, data sources, etc.

If you have [exported usage metadata](https://qlik.dev/manage/oem/operate/monitoring)
from the tenant to a cloud file store or to another Qlik Cloud tenant, ensure you
have a process to purge that data in line with your data handling policies.

Learn how to [deactivate and delete tenants](https://qlik.dev/manage/tenants/delete-tenants).

## Next steps

**Ready to continue?** → [Learn about managing secrets & encryption](https://qlik.dev/manage/oem/privacy-security/secrets-encryption/)
