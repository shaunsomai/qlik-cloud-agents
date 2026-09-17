---
source: https://qlik.dev/toolkits/qlik-cli/automation/automation-usage-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation usage ls

## qlik automation usage ls

Get automation usage metrics

### Synopsis

Retrieves paginated usage metrics for automations. The requesting user must be assigned the `TenantAdmin` or `AnalyticsAdmin` role.

```
qlik automation usage ls [flags]
```

### Options

```
      --breakdownBy string   If specified, result will be broken apart for each automation
      --filter string        (Required) Indicates how the metrics should be filtered using a SCIM-style expression. Available parameters:
                             - name (specify one or more enums to return specific metrics. Supported enum values: ˋrunsˋ, ˋscheduledRunsˋ, ˋtriggeredRunsˋ, ˋwebhookRunsˋ, ˋdurationˋ, ˋbandwidthInˋ, ˋbandwidthOutˋ)
                             - date (return a metric for a specific date or range of dates, e.g. "2025-08-01")
  -h, --help                 help for ls
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
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
