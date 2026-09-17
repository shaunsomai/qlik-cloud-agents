---
source: https://qlik.dev/toolkits/qlik-cli/workflows/workflows-automation-run-debug-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# workflows automation run debug ls

## qlik workflows automation run debug ls

Get automation run debug log

### Synopsis

Retrieves the debug log for a specific run of an automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement:

- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

```
qlik workflows automation run debug ls [flags]
```

### Options

```
      --automationId string   (Required) The unique identifier for the automation.
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --runId string          (Required) The unique identifier for the run.
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
