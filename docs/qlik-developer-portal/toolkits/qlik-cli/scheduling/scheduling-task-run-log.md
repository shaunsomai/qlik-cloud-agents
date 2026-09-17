---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-run-log/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task run log

## qlik scheduling task run log

Get task run log

### Synopsis

Retrieves the execution log for a specific task run. Set the `Accept` header to `text/plain` to receive the raw log as a downloadable file, or `application/json` (default) to receive it wrapped in a JSON object with a `logContent` field.

```
qlik scheduling task run log [flags]
```

### Options

```
  -h, --help            help for log
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --runId string    (Required) The unique identifier of the task run.
      --taskId string   (Required) The unique identifier of the task.
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
