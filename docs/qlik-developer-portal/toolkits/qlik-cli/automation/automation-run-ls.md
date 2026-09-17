---
source: https://qlik.dev/toolkits/qlik-cli/automation/automation-run-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation run ls

## qlik automation run ls

List automation runs

### Synopsis

Retrieves a list of runs for a specific automation. The requesting user must be the owner of the automation, or be assigned the one of roles: `TenantAdmin`, `AnalyticsAdmin`. Alternatively, the user must have at least one of the following scopes: `admin.automation-runs`, `automation-runs.private`, or `automation-runs.shared`.

```
qlik automation run ls [flags]
```

### Options

```
      --automationId string   (Required) The unique identifier for the automation.
      --cursor string         Pagination cursor returned from a previous request.
      --filter string         Allowed filters: ˋstatusˋ, ˋcontextˋ, ˋstartTimeˋ, ˋtitleˋ, ˋspaceIdˋ, ˋownerIdˋ, ˋexecutedByIdˋ, ˋbillableˋ.
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort string           The field to sort by, with +- prefix indicating sort order. (ˋ?query=-startTimeˋ => sort on the ˋstartTimeˋ field using descending order).
                              Allowed values: "id", "status", "startTime", "-id", "-status", "-startTime", "+id", "+status", "+startTime"
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
