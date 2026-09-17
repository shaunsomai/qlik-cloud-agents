---
source: https://qlik.dev/manage/oem/privacy-security/regional-deployment/
last_updated: 2026-05-27T18:16:42+01:00
---

# Regional deployments

As part of your deployment with Qlik Cloud, you may opt to leverage a multiple tenant
deployment, as outlined in [single vs multiple tenants](https://qlik.dev/manage/oem/solution-architecture/single-multi-tenant),
to create regional deployments.

## Benefits of regional deployments

In addition to the benefits of deploying a tenant per customer, leveraging the available
Qlik Cloud regions can help to:

- Improve end customer experience by reducing the physical distance for the
  rapid data exchanges required for interactive analytics and insights.
  This improves performance and reduces latency for end users.
- Meet security and compliance requirements by addressing scenarios where
  customers need data to reside in specific physical locations, or where you
  wish to leverage
  [the internal AWS (Amazon Web Services) network for S3 connectivity](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-S3-AWS-internal-network.htm).
- Save money by reducing cross-region transfers and data transfer duration,
  speeding up data loading, lowering concurrent load on systems, and minimizing
  errors from long-distance network connections.

## Leveraging multiple regions in Qlik Cloud

Qlik Cloud is deployed in multiple AWS regions, as detailed in
the [Authenticate for Platform Operations](https://qlik.dev/manage/platform-operations/authenticate-platform-ops/#what-happens-when-an-oauth-client-is-created)
guide.

Each Qlik Cloud region is physically distinct, meaning that tenants created in
a region can't be moved to another region by Qlik. Once you select a region, the
tenant you're provisioned is assigned a unique hostname in that region (for
example, for the `US` region in `us-east-1`, the hostname would be
`randomstring.us.qlikcloud.com`), and tenant operations will execute in that
region. More information on regional coverage and certifications
can be found on the [Qlik Trust page](https://www.qlik.com/us/trust).

When using a multiple region deployment, it is important to note:

- Qlik provides regional-level authentication, meaning that you need to generate
  an OAuth client *per region* and handle this in your automation tool.
- Qlik's in-platform automation tool, Qlik Automate, supports
  cross-region API calls natively but requires blocks to specify which regional credentials
  are used for each call.
- Qlik operates continuous deployment of releases but may stagger this across regions
  for operational reasons, meaning that occasionally, two regions may have slight
  variances in experiences.
- Tenant hostnames and aliases are unique per-region rather than globally,
  meaning that you can opt to deploy `companyname.us.qlikcloud.com` as well as
  `companyname.eu.qlikcloud.com`.
- API-based tenant creation and deactivation, and regional OAuth clients aren't available
  in Qlik Cloud Government regions.

## Client-managed hybrid deployment

If Qlik Cloud isn't available in a required region, you can leverage Qlik's
client-managed software for that deployment.

Qlik Sense Enterprise Client-managed is self-hosted software which provides the base
features of Qlik Cloud Analytics, without features such as collaboration,
automation, alerting, reporting, AI, or data integration. It provides an approach for
delivering base analytics to customers with the most stringent data privacy and
security requirements which are not met by Qlik Cloud.

Most visualization options present in Qlik Sense in Qlik Cloud will be
compatible with Qlik Sense Enterprise client-managed, however advanced features which
require components that are uneconomical or impractical to deploy on a customer-managed
Microsoft Windows server will not be available (for example, direct query to database
for big data solutions, and advanced AI helpers, etc.).

## Cross-platform development tools

Frameworks and tools such as the [qlik-cli command line utility](https://qlik.dev/toolkits/qlik-cli),
[qlik/api javascript framework](https://qlik.dev/toolkits/qlik-api),
and [qlik/embed embedding framework](https://qlik.dev/embed/qlik-embed)
support both Qlik Cloud and client-managed Qlik Sense.

Using these tools across your hybrid deployment allows for a shared
implementation approach, with the key difference being the authentication
methods required on each platform.

Note that, while Qlik Cloud
maintains a continuous release cadence, client-managed has a fixed release schedule
which may result in delays receiving the latest updates and capabilities.

## Next steps

**Ready to continue?** → [Learn about data privacy & security](https://qlik.dev/manage/oem/privacy-security/data-access/)
