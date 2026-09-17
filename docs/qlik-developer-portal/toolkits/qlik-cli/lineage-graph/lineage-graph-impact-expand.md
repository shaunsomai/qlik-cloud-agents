---
source: https://qlik.dev/toolkits/qlik-cli/lineage-graph/lineage-graph-impact-expand/
last_updated: 2026-06-03T09:30:31+02:00
---

# lineage-graph impact expand

## qlik lineage-graph impact expand

Get next-level nodes

### Synopsis

Returns next-level nodes inside a specified node on an impact analysis graph retrieved using a base node.

```
qlik lineage-graph impact expand <impactId> [flags]
```

### Options

```
      --down int       The number of downstream resource levels nodes to retrieve. (5 if not provided, -1 means unlimited and 1 means direct lineage)
  -h, --help           help for expand
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --level string   (Required) The level to get the nodes on.
                       Allowed values: "field", "table"
      --node string    (Required) The node in the downstream graph to get next-level nodes for. For instance, to get the TABLE level nodes inside a RESOURCE level node,
                       use the RESOURCE level QRI for the node. Similarly, use the TABLE level QRI to get the FIELD level nodes.
                       If a TABLE level QRI is used with ˋlevelˋ parameter being ˋTABLEˋ, only the RESOURCE level of the node will be
                       taken into consideration.
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
