---
source: https://qlik.dev/toolkits/qlik-cli/reload-task/reload-task-edit/
last_updated: 2026-06-03T09:30:31+02:00
---

# reload-task edit

## qlik reload-task edit

(Deprecated) Modify a reload-task interactively in a text-editor

### Synopsis

(Deprecated) Modify a reload-task interactively in a text-editor

This command will fetch a reload-task and open it in the editor 'vi'.
You can change the default editor by setting the 'EDITOR' environment variable.
Default editors are 'vi' for Linux/Darwin and 'notepad' for Windows.
The resource will be updated according to the changes made in the editor upon save.

```
qlik reload-task edit <reload-taskId> [flags]
```

### Options

```
  -h, --help           help for edit
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
