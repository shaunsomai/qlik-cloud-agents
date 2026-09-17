---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-cancel-job/
last_updated: 2025-06-18T09:34:47+02:00
---

# ml cancel-job

## qlik ml cancel-job

Cancel jobs

### Synopsis

Cancels jobs for an experiment version or batch prediction.

```
qlik ml cancel-job [flags]
```

### Options

```
      --corrType string   (Required) The type of a resource paired with a corrId
  -h, --help              help for cancel-job
      --interval int      Duration in seconds to wait between retries, at least 1 (default 1)
      --jobId string      (Required) The ID of a correlated resource of corrType
  -q, --quiet             Return only IDs from the command
      --raw               Return original response from server without any processing
      --retry int         Number of retries to do before failing, max 10
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
