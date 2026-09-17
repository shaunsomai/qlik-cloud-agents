---
source: https://qlik.dev/toolkits/qlik-cli/lineage-graph/lineage-graph-impact-overview/
last_updated: 2026-06-03T09:30:31+02:00
---

# lineage-graph impact overview

## qlik lineage-graph impact overview

Get all RESOURCE level nodes

### Synopsis

Returns all RESOURCE level nodes that are impacted by a change in the source node. The number of tables and fields that are impacted for each resource are included as metadata. The id (QRI) can be on any level (FIELD, TABLE or RESOURCE) and the impact will be collected based on the starting QRI.

```
qlik lineage-graph impact overview <impactId> [flags]
```

### Options

```
      --down int       The number of downstream resource levels nodes to retrieve. (5 if not provided, -1 means unlimited and 1 means direct lineage)
  -h, --help           help for overview
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
