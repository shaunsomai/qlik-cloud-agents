---
source: https://qlik.dev/toolkits/qlik-cli/lineage-graph/lineage-graph-node-search/
last_updated: 2026-06-03T09:30:31+02:00
---

# lineage-graph node search

## qlik lineage-graph node search

Search all labels

### Synopsis

Returns result per level by searching all labels within a lineage graph on all available levels.

```
qlik lineage-graph node search <nodeId> [flags]
```

### Options

```
      --collapse        To collapse internal nodes, set to true, false otherwise.
      --filter string   (Required) The expression that matches the SCIM filter format. The filter has to be encoded.
                        The currently supported attribute is "label", attribute operator "co" (contains), and grouping operator "or". Example: 'label co "label1" or label co "label2"'. The search queries are case insensitive.
  -h, --help            help for search
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --up int          The number of upstream levels of nodes retrieved to search. (5 if not provided, -1 means unlimited)
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
