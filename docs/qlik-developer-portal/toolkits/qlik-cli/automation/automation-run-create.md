---
source: https://qlik.dev/toolkits/qlik-cli/automation/automation-run-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation run create

## qlik automation run create

Run an automation

### Synopsis

Creates a run for a specific automation. Depending on the space the automation belongs to, the requesting user must meet the following requirement:

- Private space: be the owner of the automation and have the `automations.private` scope
- Shared space: be editor or operator in shared space and have `automations.shared` scope.

```
qlik automation run create [flags]
```

### Options

```
      --automation-context string   (Required) The source that triggers the automation will set the context.
                                    Allowed values: "api"
      --automationId string         (Required) The unique identifier for the automation.
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
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
