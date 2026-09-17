---
source: https://qlik.dev/toolkits/qlik-cli/task/task-run-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# task run ls

## qlik task run ls

List task runs

### Synopsis

Returns runs for the specified task.

```
qlik task run ls <taskId> [flags]
```

### Options

```
  -h, --help           help for ls
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --page string    The page cursor.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --sort string    The property of a resource to sort on (default sort is -startedAt).
                       A property must be prefixed by + or - to indicate ascending or descending sort order respectively.
                       Allowed values: "+startedAt", "-startedAt", "+endedAt", "-endedAt", "+status", "-status", "+taskId", "-taskId", "+actionId", "-actionId"
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
