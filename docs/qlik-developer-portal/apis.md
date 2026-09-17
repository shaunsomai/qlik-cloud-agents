---
source: https://qlik.dev/apis/
last_updated: 2026-04-29T13:39:58Z
---

# Qlik APIs

> **Note:** [Namespaces for REST and Events APIs](https://qlik.dev/apis/namespaces/) are being introduced in Qlik Cloud. Make sure you understand
> how APIs and their paths will be changing, and how to update your integrations.

> **API access is not constrained to the UI:** The Qlik Cloud REST and JSON-RPC APIs expose a broader capability surface than
> any single Qlik UI. The API may permit operations not available through, or
> restricted within, the Qlik Cloud user interface. Administrators should treat
> API credentials with privilege commensurate with direct platform access.\
> For more information, see [API access control and trust
> boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

Qlik provides APIs to support automation, configuration, observability, and integration with third-party applications to
incorporate Qlik Cloud capabilities directly into those applications.

New to Qlik APIs? Start with the [Authentication Guide](https://qlik.dev/authenticate), then see
[Authentication: when to use which method](https://qlik.dev/manage/key-concepts#authentication-when-to-use-which-method)
for recommended patterns and API key security tradeoffs. Then try [Manage](https://qlik.dev/manage) tutorials or the [REST API reference](https://qlik.dev/apis/rest).

## Choose your interface

You can call Qlik APIs directly over HTTP, or use higher-level interfaces that build on the same underlying APIs.

- **Direct REST calls** (`curl`, Postman, custom clients): best when you need full request-level control.
- `@qlik/api` (JavaScript/TypeScript): adds typed API calls plus developer experience improvements such as
  built-in auth patterns, automatic CSRF handling, and response caching helpers. See [qlik-api overview](https://qlik.dev/toolkits/qlik-api),
  [authentication](https://qlik.dev/toolkits/qlik-api/authentication/), and [features](https://qlik.dev/toolkits/qlik-api/features/).
- `qlik-cli`: exposes public APIs through a command-line workflow for scripting and automation. See [qlik-cli](https://qlik.dev/toolkits/qlik-cli/).
- **Qlik Automate**: provides no-code connectors and orchestration that leverage the same platform capabilities in
  workflow form.
  See [No-code overview](https://qlik.dev/toolkits/no-code/).
- **MCP-based workflows**: if your tool of choice is an AI assistant or generative AI tool,
  [Qlik MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm)
  access can be used where available in your tenant.

## APIs and libraries

For more details on each API type and specific APIs, see their dedicated documentation pages.

- [Configure, manage, and observe operations across your Qlik Cloud tenant.](https://qlik.dev/apis/rest/)
- [Manage resources across your entire Qlik Cloud organization.](https://qlik.dev/apis/org-rest/)
- [Use web native frameworks to quickly bring the power of Qlik into your apps and experiences.](https://qlik.dev/apis/javascript/)
- [Connect to the Qlik Associative Engine to access and interact with data in Qlik Sense apps.](https://qlik.dev/apis/json-rpc/)
- [Leverage events via Audits or webhooks to observe and help automate your deployment.](https://qlik.dev/apis/event/)
- [Leverage UI events via Audits to track interactions within the Qlik Cloud user interface.](https://qlik.dev/apis/ui-event/)
