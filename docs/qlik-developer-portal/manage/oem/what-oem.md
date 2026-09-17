---
source: https://qlik.dev/manage/oem/what-oem/
last_updated: 2026-05-27T18:16:42+01:00
---

# What is Qlik OEM & ISV

**OEM** stands for **Original Equipment Manufacturer**. In software, it means embedding a third-party platform
into your own product rather than building those capabilities yourself. With Qlik Cloud, you integrate
analytics, data, and AI directly into your application - your customers interact with Qlik capabilities
through your product, under your brand, without necessarily knowing Qlik is involved.

![Qlik Cloud analytics capabilities can be embedded into your software product to provide analytics, AI, and data to your end customers](https://qlik.dev/_astro/embed_qlik_theory.DId8x-zh.png)

Think of it as "buying rather than building" - instead of creating your own analytics
engine, you embed Qlik's proven platform into your application, joining Qlik customers
who already run tens of thousands of end-customer deployments in Qlik Cloud.

## What Qlik Cloud gives you as a developer

Qlik Cloud exposes three main capability areas through its APIs and SDKs.

**Embedded analytics (Qlik Sense)** is Qlik's in-memory analytics engine. You load your customers'
data into isolated Qlik Sense applications on a schedule or trigger, and users interact with that
snapshot. Because the engine works associatively rather than with predefined queries, users can explore
data at will - clicking a value in one chart instantly filters every other chart in the app - without
you writing query logic for each interaction. You embed this experience using
[qlik-embed](https://qlik.dev/embed/qlik-embed/) web components or the [@qlik/api](https://qlik.dev/toolkits/qlik-api/) SDK.

**Data integration (Qlik Cloud Data Integration)** moves data in both directions. Inbound, it lands
your customers' data into Qlik Cloud ready for analytics and AI - extracting, transforming, and staging
it into your tenants on a schedule. Outbound, it enables the data provider use case: an OEM can use
Qlik pipelines to deliver processed data directly into a customer's own database or warehouse, making
Qlik the integration engine behind your product rather than just the analytics layer. See the
[Qlik Cloud Data Integration overview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-services-introduction.htm)
on Qlik Help for full details.

**AI and natural language (Qlik Answers, Qlik Predict)** lets users interact with data using plain language.
Qlik Answers is a retrieval-augmented assistant that you can embed into your product, giving your users
answers from both structured analytics and unstructured documents. Qlik Predict gives you access to
AutoML-built predictive models. Both are accessible via the same embedding and API surface as analytics.

## How the multi-tenant architecture works

In a typical OEM deployment, you provision a separate Qlik Cloud tenant for each of your customers.
Provisioning is an API call - there is no manual infrastructure to configure per customer.
Each tenant is an isolated environment: separate data, separate users, separate configuration.
Your infrastructure (the master subscription) spans all tenants and lets you deploy and manage
them programmatically. Qlik handles the underlying infrastructure, scaling, and disaster recovery;
your concern is the application templates, data pipelines, authentication configuration, and the
user experience you build on top.

## Integration surface

The pattern for most OEM integrations has three layers:

- **UI integration**: [qlik-embed](https://qlik.dev/embed/qlik-embed/) provides web components that render Qlik Sense
  sheets, individual charts, or the Qlik Answers assistant inside your web application.
  Authentication flows through your existing identity provider via OAuth or JWT, so users
  are not redirected to a Qlik login screen.

- **Programmatic data and model access**: [@qlik/api](https://qlik.dev/toolkits/qlik-api/) is a JavaScript/TypeScript
  SDK for reading and writing app models, triggering reloads, and managing objects.
  REST APIs cover all platform operations and are also available as a
  [Python SDK](https://qlik.dev/toolkits/) and .NET client.

- **Tenant operations**: [Platform Operations APIs](https://qlik.dev/manage/platform-operations/overview/) handle
  tenant lifecycle - creation, configuration, user provisioning, monitoring, and deactivation.
  Webhooks expose real-time events from all Qlik Cloud services, letting you react to reloads,
  user activity, or entitlement thresholds in your own systems.

## Common integration patterns

**Embedded dashboards and self-service**: Most OEM deployments present preconfigured Qlik Sense apps
to end users. Users interact with visualizations, make selections, and export reports - all within
your application UI. For self-service scenarios, users can also create their own sheets and bookmarks
within the bounds you define. The degree of self-service is controlled by the space type and user
roles you configure.

**AI assistant integration**: You can embed Qlik Answers as a chat-style interface inside your product.
Users ask questions in natural language; Answers retrieves information from both your structured
analytics models and unstructured document sources (PDFs, knowledge bases) indexed in a knowledge base.
This is particularly useful in SaaS products where end users vary widely in technical confidence.

**Data pipeline embedding**: For products where your customers supply their own data, Qlik Cloud Data
Integration can act as the pipeline your product uses to collect, transform, and stage that data into
analytic models - removing the need to build and maintain ETL infrastructure in your own stack.

## Next steps

Begin your implementation with the [OEM playbook](https://qlik.dev/manage/oem/introducing-playbook/), which walks through
architecture, security, development, and operations in sequence.
