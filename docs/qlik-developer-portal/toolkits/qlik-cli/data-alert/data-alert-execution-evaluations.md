---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-execution-evaluations/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert execution evaluations

## qlik data-alert execution evaluations

Get data alert task execution evaluation

### Synopsis

Retrieves the content of an evaluation for a specified data alerting task execution.

```
qlik data-alert execution evaluations [flags]
```

### Options

```
      --data-alertId string   (Required) The alerting task identifier.
      --executionId string    (Required) The execution identifier.
  -h, --help                  help for evaluations
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
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
