---
source: https://qlik.dev/toolkits/qlik-cli/data-file/data-file-connection-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-file connection ls

## qlik data-file connection ls

Get the list of built-in connections used by the engine to load/write data files

### Synopsis

The non-filtered list contains a set of hardcoded connections, along with one connection per team space that
the given user has access to.

```
qlik data-file connection ls [flags]
```

### Options

```
      --appId string        If present, get connections with connection strings that are scoped to the given app ID.
  -h, --help                help for ls
      --includeSpaceStats   If set to true, include computed space-level statistics for the spaces represented by the connections in the
                            returned list.  If false, this information is not returned.
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int           The total number of resources to retrieve.
      --name string         If present, only return connections with the given name.
      --page string         If present, the cursor that starts the page of data that is returned.
      --personal            If true, only return the connections that access data in a personal space.  Default is false.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --sort string         The name of the field used to sort the result.  By default, the sort is ascending.  Putting a '+' prefix on
                            the sort field name explicitly indicates ascending sort order.  A '-' prefix indicates a descending sort order.
                            Allowed values: "spaceId", "+spaceId", "-spaceId"
      --spaceId string      If present, only return the connection that accesses data files in the specified space.
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
