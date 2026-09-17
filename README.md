# qlik-cloud-agents

Independent Claude Code plugin for Qlik cloud. Version 2.1.2.

## Install

    /plugin marketplace add https://github.com/shaunsomai/qlik-cloud-agents.git --sparse .claude-plugin plugins
    /plugin install qlik-cloud-agents@qlik-cloud-agents-marketplace

Private repository: collaborators need GitHub access and authenticated Git. Remove duplicate legacy installations first. Local testing: claude --plugin-dir ./plugins/qlik-cloud-agents

[Plugin guide](plugins/qlik-cloud-agents/README.md) | [Sharing contract](SHARING.md) | [House conventions](HOUSE-CONVENTIONS.md) | [MIT license](LICENSE)

## Resources

Cloud needs an external tenant MCP connector. Desktop needs Qlik Sense Desktop running and Python 3.8+; its MCP server is bundled. Both plugins can be installed together: inspect server-qualified tools and confirm the target app.

[Worked example](examples/sales-demo/) | [Themes](themes/) | [Developer Markdown](https://github.com/shaunsomai/qlik-dev-agents-plugin/tree/master/docs/qlik-developer-portal) | [Enterprise Windows reference](https://github.com/shaunsomai/qlik-dev-agents-plugin/tree/master/docs/qlik-sense-admin-playbook)

The Markdown reference libraries are kept only in the original repository, linked above. This repository contains the platform plugin, themes and worked examples.

Examples are separate from installed plugins. Configure QVD folders and DEMO_QVDS_LOCAL before Desktop reloads; map connections for Cloud. Read the script porting contract.

## Validate and package

Repository tooling needs Python 3.10+; Desktop MCP runtime remains Python 3.8+.

    python scripts/package.py

Packaging checks manifests, agents, guide links, themes and Desktop MCP stdio/tool schemas offline, builds a ZIP with SHA-256 sidecar under dist/, then validates the extracted package. CI uploads these packages as artifacts. Live Qlik operations, rendering and Claude installation require their runtime environments.

Split from https://github.com/shaunsomai/qlik-dev-agents-plugin at 89bea773cd25e028ef2fdadcabbf075d37ca0d98. Original history remains there.
