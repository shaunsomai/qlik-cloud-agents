---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant ls

## qlik assistant ls

List assistants

### Synopsis

Retrieves the list of assistants. The result can be filtered, sorted, and paginated.

```
qlik assistant ls [flags]
```

### Options

```
      --countTotal       (Deprecated) Optional parameter to request total count for query.
  -h, --help             help for ls
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int        The total number of resources to retrieve.
      --next string      Optional parameter to request the next page.
      --prev string      Optional parameter to request the previous page.
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --sort string      Optional resource field name to sort on, case insensitive, e.g. ˋnameˋ. Can be prefixed with ˋ-ˋ to set descending order; defaults to ascending.
                         Allowed values: "NAME", "-NAME", "DESCRIPTION", "-DESCRIPTION", "CREATED", "-CREATED", "UPDATED", "-UPDATED"
      --spaceId string   Optional parameter to filter assistants by space ID.
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
