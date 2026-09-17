---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-di-task-request-reload/
last_updated: 2026-06-03T09:30:31+02:00
---

# di-project di-task request-reload

## qlik di-project di-task request-reload

Request dataset reload

### Synopsis

Registers a request to reload the datasets associated with the specified data task. The reload does not occur immediately; it will take effect on the next scheduled or manual run of the task.

```
qlik di-project di-task request-reload [flags]
```

### Options

```
      --di-projectId string                 (Required) Identifier of the data project.
      --di-taskId string                    (Required) Identifier of the data task.
  -f, --file file                           Read request body from the specified file
  -h, --help                                help for request-reload
      --interval int                        Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                               Return only IDs from the command
      --raw                                 Return original response from server without any processing
      --reloadStrategy string               Reload strategy (optional, applies to materialized SQL transformations and transformation flows tasks)
                                            Allowed values: "NONE", "TRUNCATE", "COMPARE_AND_APPLY"
      --retry int                           Number of retries to do before failing, max 10
      --selectedDatasets-datasetId string   Datasets to reload (optional, if omitted or empty, all datasets will be reloaded).
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
