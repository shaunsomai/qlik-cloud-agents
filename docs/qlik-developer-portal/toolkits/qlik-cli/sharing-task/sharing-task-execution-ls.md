---
source: https://qlik.dev/toolkits/qlik-cli/sharing-task/sharing-task-execution-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# sharing-task execution ls

## qlik sharing-task execution ls

List sharing task executions

### Synopsis

Lists executions for the specified sharing task.

```
qlik sharing-task execution ls [flags]
```

### Options

```
  -h, --help                    help for ls
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int               Limit the returned result set
      --next string             The cursor to the next page of data. Only one of next or previous may be specified.
      --offset int              Offset for pagination - how many elements to skip
      --prev string             The cursor to the previous page of data. Only one of next or previous may be specified.
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
      --sharing-taskId string   (Required) The sharing task identifier.
      --sort strings            Sort the returned result set by the specified field
                                Allowed values: "starttime", "-starttime", "+starttime"
      --status string           Specifies a filter for a particular field and value of an execution
                                Allowed values: "successful", "failed"
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
