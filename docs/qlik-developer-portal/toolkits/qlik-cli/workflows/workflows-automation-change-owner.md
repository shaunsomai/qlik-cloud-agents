---
source: https://qlik.dev/toolkits/qlik-cli/workflows/workflows-automation-change-owner/
last_updated: 2026-06-03T09:30:31+02:00
---

# workflows automation change-owner

## qlik workflows automation change-owner

Change automation owner

### Synopsis

Changes the owner of an automation to another user. This action removes the history and change logs of this automation. All linked connections used in the automation are detached and not moved to the new owner. The requesting user must be assigned one of the following roles: `TenantAdmin`, `AnalyticsAdmin` or have at least one of the following scopes: `admin.automations`, `admin.automations:strict`.

```
qlik workflows automation change-owner <automationId> [flags]
```

### Options

```
  -f, --file file       Read request body from the specified file
  -h, --help            help for change-owner
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --userId string   (Required) The unique identifier of the new owner.
```

### Options inherited from parent commands

```
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -v, --verbose                  Log extra information
```
