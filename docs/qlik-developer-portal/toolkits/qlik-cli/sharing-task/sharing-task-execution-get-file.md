---
source: https://qlik.dev/toolkits/qlik-cli/sharing-task/sharing-task-execution-get-file/
last_updated: 2026-06-03T09:30:31+02:00
---

# sharing-task execution get-file

## qlik sharing-task execution get-file

Get sharing task execution file

### Synopsis

Retrieves the file content for the requested execution and file type.

```
qlik sharing-task execution get-file <fileAlias> [flags]
```

### Options

```
      --executionId string      (Required) The execution identifier.
  -h, --help                    help for get-file
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
      --output-file string      Filepath specifying where to write the response body.
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
      --sharing-taskId string   (Required) The sharing task identifier.
      --status string           Filter by status. If not present then no filtering is done on the status. This is only relevant when requesting latest execution.
                                Allowed values: "successful", "failed", "cancelled"
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
