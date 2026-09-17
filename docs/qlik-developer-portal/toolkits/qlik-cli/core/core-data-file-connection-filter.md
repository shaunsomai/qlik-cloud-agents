---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-connection-filter/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file connection filter

## qlik core data-file connection filter

Filter connections

### Synopsis

Use this operation to retrieve data file connections for a specified set of space IDs.
This is useful when the list of space IDs is too large to pass as query parameters.

```
qlik core data-file connection filter [flags]
```

### Options

```
  -f, --file file           Read request body from the specified file
  -h, --help                help for filter
      --includeSpaceStats   If set to true, include computed space-level statistics for the spaces represented by the connections in the
                            returned list.  If false, this information is not returned.
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --name string         If present, only return connections with the given name.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --spaceIds strings    The list of space IDs that is used to filter the connection result set.
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
