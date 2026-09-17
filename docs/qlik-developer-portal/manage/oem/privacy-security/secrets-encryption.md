---
source: https://qlik.dev/manage/oem/privacy-security/secrets-encryption/
last_updated: 2026-05-27T18:16:42+01:00
---

# Secrets & encryption

This section details the encryption options in Qlik Cloud and highlights some common
secret management activities.

## Encryption

Every tenant in Qlik Cloud has multiple layers of security to protect your data.
While the default, out-of-the-box configuration is secure, you can opt to provide your own encryption
key if you have specific requirements, such as HIPAA.

Learn more about [tenant encryption](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/tenant-encryption.htm)
on Qlik Help or discover how to [configure tenant encryption](https://qlik.dev/manage/tenants/tenant-encryption).

## Secret management

Everything in the modern web relies on secrets. Qlik Cloud is no different and accepts
various secret types across services. To help you assess how to manage these secrets
to comply with rotation and offboarding processes, the following table outlines the most
commonly leveraged services, their secret types, and the update approach.

| Qlik Cloud service         | Usage                                                                                  | Common secrets        | Management approach                                                                                                                                                                                                                                                                         |
| -------------------------- | -------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Analytics data connections | Loading and storing data using Qlik Sense applications                                 | Various               | Can be updated using the [Data Connections API](https://qlik.dev/apis/rest/data-connections/), with the exception of data connections leveraging interactive OAuth authentication. See more at [update data connections](https://qlik.dev/manage/data-connections/update-data-connections/) |
| API keys                   | Connecting to legacy backend systems which don't yet support OAuth M2M clients         | Bearer token          | API keys can be generated using the [API Keys API](https://qlik.dev/apis/rest/api-keys/)                                                                                                                                                                                                    |
| Automations (triggered)    | Automations can be triggered using an execution token                                  | Execution token       | Automations can be duplicated using the [Automations API](https://qlik.dev/apis/rest/automations)                                                                                                                                                                                           |
| Automation connections     | Connecting to your data sources in Qlik Automate workflows                             | Various               | Connections can be updated using the [Automation Connections API](https://qlik.dev/apis/rest/automation-connections)                                                                                                                                                                        |
| OAuth clients              | Connecting Qlik Cloud to any third-party systems, and for orchestration of deployments | Client ID and secret  | Secrets can be regenerated using the [OAuth Clients API](https://qlik.dev/apis/rest/oauth-clients/)                                                                                                                                                                                         |
| Tenant email               | Sending tenant-wide notifications, alerts, and subscriptions                           | Username and password | Can be updated using the [Transports API](https://qlik.dev/apis/rest/transports/)                                                                                                                                                                                                           |

Regardless of whether your organization enforces secret rotation on a schedule,
you should have a approach for updating secrets across your tenants.

## Secret rotation for Qlik Cloud services

For secrets that are generated and maintained by Qlik Cloud, you can manage rotation
with your own scripts or Qlik Automate. The approach varies slightly
for each secret type.

### API keys

[API keys](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm)
are per-user tokens with a fixed expiry time set upon creation. They can't
be extended and don't support custom scopes, instead acting with the permissions
of the owner.

To rotate, your tooling should create a new API key, cut services across, and
then delete the old key (or let it expire). This can be done using the user interface
or the [API keys API](https://qlik.dev/apis/rest/api-keys/).

API keys are usually used for observability by the [monitoring apps](https://qlik.dev/manage/oem/operate/monitoring),
as the REST connector in Qlik Sense doesn't support OAuth.
Where possible, use OAuth clients for programmatic auth.

### OAuth clients

[OAuth clients](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-oauth-client.htm)
come in several types. Only confidential clients (machine-to-machine) OAuth clients
provide a client secret which may need to be rotated. These secrets do not expire.

It is possible to create multiple secrets for a single OAuth client, so to rotate,
create a new secret, cut services across, and then delete the old secret.
This can be done using the user interface
or the [OAuth clients API](https://qlik.dev/apis/rest/oauth-clients/).

### Execution tokens for triggered Automations

[Triggered runs of Qlik Automate](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm#triggered-webhooks)
expose automations via a REST endpoint. When enabled, an execution token unique
to that automation is generated. This token does not expire.

To change the execution token, you must duplicate the automation, and remove the
original automation. This can be done using the user interface
or the [Automations API](https://qlik.dev/apis/rest/automations/).

## Next steps

**Ready to start building your product?** → [Product development](https://qlik.dev/manage/oem/product-development/)
