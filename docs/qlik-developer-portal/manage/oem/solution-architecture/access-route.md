---
source: https://qlik.dev/manage/oem/solution-architecture/access-route/
last_updated: 2026-05-27T18:16:42+01:00
---

# Embedded vs native experience

OEM partners can choose to embed most Qlik Cloud capabilities into their own solution
levering powerful tooling such as [qlik-embed (embedding visuals)](https://qlik.dev/embed/qlik-embed)
and [qlik/api (accessing raw APIs and app models)](https://qlik.dev/toolkits/qlik-api),
as well as provide direct access to the native experiences.

This section explores the options available to you with respect to some of the capabilities
available in Qlik Cloud.

> **Note:** Irrespective of the access approach, you should configure your customer tenant to use an Identity Provider that you
> manage. This provides various [security benefits](https://qlik.dev/manage/oem/privacy-security/data-access),
> as well as greater control over [branding](https://qlik.dev/manage/oem/solution-architecture/brand-customize).

## Embedded access (within your app)

Analytics appear inside your application using Qlik's embedding tools. Users never leave your
product - charts, sheets, or assistants render in your UI with your navigation and branding.

### Two embedding approaches

#### Full sheet or assistant embedding

![Embedded access to a Qlik Sense sheet](https://qlik.dev/_astro/embed-qs-sheet.DL7xIDst.png)

Use `qlik-embed` with the `analytics/sheet` or `ai/assistant` tag to embed a complete Qlik Sense
sheet or the Qlik Answers assistant. The embedded experience includes all standard user
interactions - selections, drill-down, insight advisor - within the bounds of your application
shell. This is the right choice for executive dashboards, operational reports, and interactive
data exploration.

#### Individual chart embedding

![Embedded access to a Qlik Sense chart](https://qlik.dev/_astro/embed-qs-chart.tgoQQrAO.png)

Use `qlik-embed` with the `analytics/chart` tag to embed a single visualization. This is a
lighter-weight integration that gives you maximum positional flexibility - you can place
individual charts alongside your own UI elements, controls, or data. Use this for KPI widgets,
metric cards, or where you want to compose a custom layout from multiple Qlik objects and
your own components.

### When to use embedded access

Embedding is the right choice when analytics need to feel like a native feature of your product
rather than a separate tool. It keeps users in context, removes the need for them to learn a
second interface, and lets you control exactly what is exposed. The cost is development time:
you own authentication flows, and ongoing updates as your
integration evolves.

Embedding may not be appropriate when your customers need full Qlik authoring capabilities -
some advanced features require the native experience - or when development resource is limited
and native access would suffice.

## Native access (Direct link)

Give customers a URL to their Qlik Cloud tenant - for example, `customer-a.us.qlikcloud.com` - and
they interact with Qlik Cloud directly in their browser. You configure identity provider, branding,
and content, but Qlik renders the full interface.

![Direct access to the Qlik Cloud Hub](https://qlik.dev/_astro/embed-native-hub.CfG3bjNS.png)

Native access gives users the full Qlik Cloud feature set: authoring, collaboration,
data alerts, subscriptions, AI assistants, and reporting. Your development effort is limited to
configuration (identity provider setup, branding, space and permission management) rather than
building a custom UI. New Qlik Cloud features become available automatically without any changes
to your integration.

The trade-off is that users leave your application to access analytics. You have limited control
over the overall user experience, and users need to be comfortable working in the Qlik interface.
Some customers require training, and supporting a Qlik-branded experience may not fit your product
positioning.

**Use native access when** your customers need full analytics authoring capabilities,
you want to minimize development investment, or you are offering analytics as a clearly
separated add-on rather than an integrated feature.

![Direct access to a Qlik Sense application](https://qlik.dev/_astro/embed-native-qs.Dkuo3kkQ.png)

## API integration (Custom development)

Beyond embedding UI components, you can build fully custom experiences using [@qlik/api](https://qlik.dev/toolkits/qlik-api/)
and the Qlik REST APIs directly. This gives you complete control over what users see, without
any Qlik UI rendered in the browser.

Typical patterns include:

- [AI chat interfaces built with the NL API](https://qlik.dev/embed/gen-ai/create-chatbot-nl-api) - natural language
  queries that return data, not a Qlik-rendered chart
- [Session apps](https://qlik.dev/examples/qlik-api-examples/create-session-app) - temporary in-memory models generated
  on demand for specific customer scenarios
- [Data cubes](https://qlik.dev/examples/qlik-api-examples/create-cube/) - raw hypercube data returned to your
  frontend for rendering in your own chart library

API integration requires the most development and maintenance effort, but it is the only path
to a completely custom UX or to environments where you cannot use JavaScript (for example,
native mobile apps).

## Choosing your approach

| Consideration                            | Embedded | Native  | API-only |
| ---------------------------------------- | -------- | ------- | -------- |
| Development effort                       | Moderate | Minimal | High     |
| User experience control                  | High     | Low     | Complete |
| Full Qlik feature access                 | Partial  | Yes     | No       |
| Requires ongoing integration maintenance | Yes      | No      | Yes      |
| Works without JavaScript embedding       | No       | Yes     | Yes      |

Most OEM deployments combine approaches: native access for internal administrators or power users
who need authoring capabilities, and embedded access for end consumers who need a curated,
in-product experience. API integration supplements both for specific custom scenarios.

## Next steps

**Ready to continue?** → [Brand Qlik Cloud](https://qlik.dev/manage/oem/solution-architecture/brand-customize/)
