---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task patch

## qlik scheduling task patch

Patch a task

### Synopsis

Partially updates a specific task using a JSON Patch document (RFC 6902). Only the fields included in the patch operations are modified. All other fields remain unchanged. If the task is owned by another user, ownership is transferred to the requesting user.

```
qlik scheduling task patch <taskId> [flags]
```

### Options

```
  -f, --file file                                   Read request body from the specified file
  -h, --help                                        help for patch
      --interval int                                Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                                   The patch operation to perform.
                                                    Allowed values: "add", "remove", "replace", "move", "copy"
      --path string                                 A JSON Pointer (RFC 6901) identifying the field to patch.
  -q, --quiet                                       Return only IDs from the command
      --raw                                         Return original response from server without any processing
      --retry int                                   Number of retries to do before failing, max 10
      --value string|int|int|bool|unknown|unknown   The value to use in a JSON Patch operation.
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
