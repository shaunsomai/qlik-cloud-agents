---
source: https://qlik.dev/toolkits/qlik-cli/lineage-graph/lineage-graph-node-expand/
last_updated: 2026-06-03T09:30:31+02:00
---

# lineage-graph node expand

## qlik lineage-graph node expand

Get expanded node and its edges

### Synopsis

Returns the expanded node and its edges. Up and downstream nodes are not part of the response, edges are. The id is the root node that lineage is requested for. The QRI of the node to expand is sent as the query parameter "node" for expansion.

```
qlik lineage-graph node expand <nodeId> [flags]
```

### Options

```
      --collapse       To collapse internal nodes, set to true, false otherwise.
  -h, --help           help for expand
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --level string   (Required) The level to expand to.
                       Allowed values: "field", "table"
      --node string    (Required) The QRI of the node in the upstream graph for expansion.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --up int         The number of upstream levels of nodes retrieved to expand. (5 if not provided, -1 means unlimited)
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
