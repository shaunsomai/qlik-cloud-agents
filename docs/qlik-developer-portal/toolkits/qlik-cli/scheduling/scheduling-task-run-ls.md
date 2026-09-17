---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-run-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task run ls

## qlik scheduling task run ls

List task runs

### Synopsis

Retrieves a paginated list of execution runs for the specified task, ordered by most recent run by default. Each run record includes the start and end time, status, and the identity that triggered it.

```
qlik scheduling task run ls <taskId> [flags]
```

### Options

```
  -h, --help           help for ls
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --page string    Cursor token for fetching the next page of results.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --sort string    Field and direction to sort results by. Prefix the field name with ˋ+ˋ for ascending or ˋ-ˋ for descending order. Defaults to ˋ-startedAtˋ.
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
