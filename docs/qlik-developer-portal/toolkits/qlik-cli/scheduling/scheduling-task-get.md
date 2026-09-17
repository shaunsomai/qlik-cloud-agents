---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-get/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task get

## qlik scheduling task get

Get a task

### Synopsis

Retrieves the full definition and metadata for a specific task, including its trigger configuration, state definitions, owner, and last run status. Use this operation to inspect a task before updating or starting it.

```
qlik scheduling task get <taskId> [flags]
```

### Options

```
  -h, --help           help for get
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
