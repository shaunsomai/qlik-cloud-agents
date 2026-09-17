---
source: https://qlik.dev/manage/oem/privacy-security/
last_updated: 2026-05-27T18:16:42+01:00
---

# Privacy and security overview

As an OEM partner, you are responsible for the data your end customers upload or generate within
their Qlik Cloud tenants. That responsibility is different from operating Qlik Cloud for internal
use only: you are holding data belonging to third-party organizations, typically under contractual
data processing agreements, and subject to the privacy and compliance requirements of those
organizations' industries and geographies.

This section covers three areas:

- **[Regional deployments](https://qlik.dev/manage/oem/privacy-security/regional-deployment/)** - Qlik Cloud is
  available in multiple AWS regions. Provisioning a customer's tenant in the correct region meets
  data residency requirements and reduces latency for their end users. Regional deployment also
  enables internal AWS network connectivity for S3 data sources in the same region.

- **[Data privacy & security](https://qlik.dev/manage/oem/privacy-security/data-access/)** - Covers identity
  provider configuration (OIDC, SAML, JWT, OAuth), the layered access control model (tenant roles,
  space roles, section access), customer offboarding and tenant deactivation, and audit logging.

- **[Encryption & secrets](https://qlik.dev/manage/oem/privacy-security/secrets-encryption/)** - Covers Qlik Cloud's
  default encryption, the option to supply customer-managed encryption keys for regulated workloads,
  and the recommended approach for rotating the secrets (OAuth client credentials, API keys, automation
  tokens) that your deployment depends on.

## Next steps

**Start with regional deployments:** → [Regional deployments](https://qlik.dev/manage/oem/privacy-security/regional-deployment/)
