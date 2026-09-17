---
source: https://qlik.dev/manage/oem/solution-architecture/design-automation/
last_updated: 2026-05-27T18:16:42+01:00
---

# Design automation

Automation is not optional at OEM scale. Managing tens or hundreds of customer tenants through manual processes
is not practical - tenant provisioning, content deployment, user lifecycle management, and monitoring all need to
run programmatically. The question is which tools you use and in what combination.

## Recommended progression

### Start with Qlik Automate

Qlik Automate is Qlik Cloud's built-in no-code automation platform. For teams new to Qlik Cloud, starting here
is the fastest path to a working automation layer. Qlik provides pre-built workflow templates for the most common
OEM operations: tenant provisioning, user management, content deployment, and monitoring alerting. You can wire
these up through a visual workflow designer without writing script, which also makes the underlying API calls
visible - a useful way to learn the API surface before building against it directly.

Qlik Automate is also the recommended runtime for standard Qlik Cloud operations once you do move to CI/CD.
Rather than re-implementing Qlik-specific logic in your own pipeline scripts, you can trigger Automate workflows
via webhook or API call from CI/CD and let Automate handle the Qlik-specific steps.

### Integrate with CI/CD as you mature

Once you have established your development and deployment processes and are comfortable with the Qlik API surface,
integrate Qlik Cloud operations into your existing CI/CD pipelines. Your CI/CD tooling orchestrates the overall
flow - triggering tenant provisioning on a new customer signup event, promoting a new app template version through
development and acceptance spaces, rolling out a change across all customer tenants in stages. Qlik Automate handles
Qlik-specific steps within that flow, triggered by webhook or API call from your pipeline.

This hybrid approach - CI/CD for orchestration, Qlik Automate for Qlik-specific operations - gives you full
control over deployment logic while avoiding the need to reimplement what Automate already provides.

## Automation patterns

### Single tenant automation

For deployments with a single shared tenant (or a small, fixed set of tenants), a simple CI/CD pipeline
handles the full lifecycle:

1. **Code commit** - A change to an app template triggers the pipeline via webhook, which unbuilds the app
   and commits the artifact to version control
2. **Build and test** - Validate the app in the test managed space; run app evaluation for performance
3. **Deploy to acceptance** - Promote to the acceptance managed space; require human approval before proceeding
4. **Deploy to production** - Roll the validated change into the production managed space
5. **Monitor and validate** - Confirm the deployment succeeded via monitoring apps or API checks

### Multiple tenant automation

For deployments serving many customer tenants, automation covers the full tenant lifecycle from
creation to deactivation:

1. **Tenant provisioning** - Create a new tenant via the Platform Operations API when a customer
   purchases; configure branding, identity provider, and spaces
2. **Regional deployment** - Provision in the correct geographic region based on customer requirements
3. **Identity integration** - Configure the customer's identity provider or OAuth client
4. **Content deployment** - Deploy current application templates from version control
5. **User provisioning** - Create initial user accounts and assign roles
6. **Monitoring setup** - Deploy monitoring applications and configure alerting

Content updates across the existing tenant estate follow a staged rollout: deploy to a canary group of tenants
first, validate, then extend to the full estate. Qlik Automate's multi-tenant installer and bulk operation
workflows handle this without requiring you to loop through tenants in your own scripts.

## Hands-off tenant management

Customer tenants should require no interactive administrative access. All administrative operations -
provisioning, configuration changes, user management, app updates, monitoring - should be executable
through APIs and automation workflows. This is necessary for scale (you cannot hire administrators
faster than you can add customers), and it is better for security: removing interactive admin access
eliminates a class of misconfiguration risk and provides a clean, auditable trail for every
change made to a customer environment.

Design your automation to cover tenant provisioning and configuration, user lifecycle (provisioning,
role changes, deprovisioning), application and content deployment, security policy enforcement,
and monitoring setup - so that no administrative action requires a human to log in to a customer
tenant.

## Choosing your approach

You should start with Qlik Automate if your team is new to the Qlik API surface, you need to
deploy automation fast, or you want to validate patterns before investing in custom pipeline
code. Transition to CI/CD orchestration when you need tighter integration with your existing
DevOps tooling, you want deployment decisions (approvals, canary rollouts, rollbacks) to live
in the same system as the rest of your infrastructure, or you are at a scale where custom
orchestration logic is unavoidable.

These two paths are not mutually exclusive. The mature pattern for most OEM deployments is
CI/CD orchestrating Qlik Automate workflows for standard Qlik Cloud operations, with custom
CI/CD scripts handling application code promotion and non-Qlik integrations.

## Next steps

**Ready to continue?** → [Move to privacy & security](https://qlik.dev/manage/oem/privacy-security/)
