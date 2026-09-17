---
source: https://qlik.dev/toolkits/qlik-cli/reload-task/reload-task-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# reload-task ls

## qlik reload-task ls

(Deprecated) Find and return tasks

### Synopsis

(Deprecated) Finds and returns the tasks that the user has access to.

```
qlik reload-task ls [flags]
```

### Options

```
      --appId string   The case sensitive string used to search for a task by app ID.
  -h, --help           help for ls
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --next string    The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --partial        The boolean value used to search for a task is partial or not
      --prev string    The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
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
