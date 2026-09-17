---
source: https://qlik.dev/toolkits/qlik-cli/automation/automation-disable/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation disable

## qlik automation disable

Disable an automation

### Synopsis

Disables an automation so that it cannot be run. To disable an automation, the requesting user must meet at least one of the following conditions:

- be the owner of the automation
- be assigned one of the following roles: `TenantAdmin`, `AnalyticsAdmin`
- have at least one of the following scopes: `admin.automations`, `admin.automations:strict`, `automations.private`, or `automations.shared`

```
qlik automation disable <automationId> [flags]
```

### Options

```
  -h, --help           help for disable
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
