---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-thread-interaction-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# assistant thread interaction ls

## qlik assistant thread interaction ls

List interactions

### Synopsis

Retrieves the list of interactions for the thread.

```
qlik assistant thread interaction ls [flags]
```

### Options

```
      --assistantId string   (Required) The ID of the assistant from which to retrieve the interactions.
  -h, --help                 help for ls
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int            The total number of resources to retrieve.
      --next string          Optional parameter to request the next page.
      --prev string          Optional parameter to request the previous page.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --sort string          Optional resource field name to sort on, case insensitive, e.g. ˋcreatedˋ. Can be prefixed with ˋ-ˋ to set descending order; defaults to ascending.
                             Allowed values: "CREATED", "-CREATED", "UPDATED", "-UPDATED"
      --threadId string      (Required) The ID of the thread from which to retrieve the interactions.
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
