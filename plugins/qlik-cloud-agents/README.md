# qlik-cloud-agents

Six Claude Code subagents for **Qlik Sense SaaS (Qlik Cloud)** development, built around a strict write-approval protocol: nothing touches a live tenant unless the instruction that dispatched the agent explicitly says so.

Working on a local `.qvf` instead? Install [`qlik-desktop-agents`](https://github.com/shaunsomai/qlik-desktop-agents) — the platforms differ enough that the agent sets are not interchangeable.

## The agents

| Agent | Model | What it does |
|---|---|---|
| `qlik-app-inspector` | sonnet | Read-only reconnaissance of an app's content — sheets, master items, expressions, fields, chart data, dataset freshness and lineage — plus a tiered convention audit. Never writes; refuses even if told it's approved. |
| `qlik-script-writer` | inherit | Designs a data model, then writes a production-grade `.qvs` load script in a 3-tier Extract/Transform/Data Model layout. Writes files only, never the tenant. |
| `qlik-script-reviewer` | sonnet | Reviews an existing load script against a 16-point house checklist (synthetic keys, circular refs, un-optimised loads, section access, naming). Tools: Read/Grep/Glob only — it cannot write anything. |
| `qlik-frontend-builder` | inherit | Designs and builds sheets, charts, master measures/dimensions and set analysis on a 24-column grid. Inspects the live app first. Writes to the tenant only under an `APPROVED:` line. |
| `qlik-architect` | inherit | Fit assessments (Qlik vs. Power BI/Tableau/Databricks/ThoughtSpot), tenant design, and QSEoW/QlikView → Cloud migration planning. Web-searches before any current-capability claim. No tenant access at all. |
| `qlik-administrator` | inherit | Operates and monitors the tenant: reloads, automations, spaces, users, licences, catalogue governance. The only agent that uses qlik-cli or the Qlik Cloud REST API. Writes under `APPROVED:`. |

## Prerequisites

A **Qlik Cloud MCP connector** exposing tools named `qlik_search`, `qlik_describe_app`, `qlik_list_sheets` and so on (the `qlik_*` naming convention). These agents don't hardcode a connector's server ID — they discover tool schemas by keyword via `ToolSearch` at runtime, so any MCP server exposing similarly-named tools should work.

For `qlik-administrator`'s spaces/users/licences/app-lifecycle features, additionally either:

- [qlik-cli](https://github.com/qlik-oss/qlik-cli) on your `PATH` with a configured context, or
- a Qlik Cloud API key in `QLIK_TENANT_URL` / `QLIK_API_KEY`

Without either it still covers everything the MCP tools reach (automations, catalogue, glossary, dataset governance) and reports the rest as `Unavailable` with setup steps.

## The permission model

No agent writes to the tenant unless the task it was dispatched with contains a line beginning `APPROVED:` naming the exact objects. Without it, the agent returns what it *would* do under "Proposed changes (awaiting approval)" and stops. A subagent can't pause mid-task to ask, so anything needing a human decision has to be settled before dispatch.

`qlik-administrator` refuses certain things **even when approved**: deleting a space, deleting or disabling a user, deleting an app outright (it proposes only), touching tenant settings, IdP/SSO or API keys, any bulk change over five objects in one approval, or anything that would remove its own admin access. It never asks you to paste a credential into the conversation, and dumping environment variables is banned outright in its own instructions.

## Install

```
/plugin marketplace add shaunsomai/qlik-cloud-agents
/plugin install qlik-cloud-agents@qlik-cloud-agents-marketplace
```

Or copy `agents/*.md` into your project's `.claude/agents/` (or `~/.claude/agents/` for a user-wide install) — nothing in the agent files depends on being loaded as a plugin.

## Conventions

See the [root README](HOUSE-CONVENTIONS.md) for the shipped naming conventions and how to override them from your project's `CLAUDE.md`.

One convention worth calling out, because getting it wrong breaks a reload: **mapping tables are never dropped explicitly.** A `MAPPING LOAD` table is not part of the data model, so `DROP TABLE` cannot resolve it and the reload aborts. Qlik discards them itself at the end of the script. The reviewer treats an explicit `DROP TABLE` on a `MAP_` table as Critical.

## Licence

[MIT](LICENSE).
