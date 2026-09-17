# Installation verification

Tested 2026-09-17 with official Claude Code 2.1.274, plugin version 2.1.1.

Both plugins installed together from their private GitHub repositories using authenticated HTTPS and sparse checkout of .claude-plugin and plugins. A separate CLAUDE_CONFIG_DIR held the test configuration/cache. Claude reported both enabled. Native marketplace and plugin validation passed with no warnings. Agent YAML was corrected after native validation identified an unquoted colon in the Desktop administrator description.

The install instructions use HTTPS to avoid requiring SSH host-key setup, and sparse checkout to avoid Windows path-length failures in the large documentation library. The documentation libraries have since been removed from the platform repositories and remain available in the original repository. Sparse checkout now also excludes worked examples.

The repeatable scripts/test-installation.py validates and installs into temporary settings, verifies enabled status and bundled assets, then checks the installed Desktop MCP handshake/tool inventory. CI executes it on an ephemeral Ubuntu runner. Use --github with authenticated Git to exercise remote installation; set CLAUDE_TEST_BINARY to the executable path if it is not on PATH.

No model calls, tenant credentials, live Cloud operations, Desktop app changes or chart rendering were used. Installation checks do not prove that an external Cloud connector is configured or that a running Desktop engine accepts live operations. Windows testing used isolated configuration under the workspace, not a separate operating-system VM.
