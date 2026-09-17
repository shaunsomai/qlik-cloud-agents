---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-graph-subgraph/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task graph subgraph

## qlik scheduling task graph subgraph

Get task subgraph

### Synopsis

Retrieves the combined ancestor-and-descendant subgraph for a specific task, with the requested task as the root vertex. Traverses both parent and child relationships breadth-first up to the depth specified by `level`. Use this to see the full dependency context for a task in one request.

```
qlik scheduling task graph subgraph <taskId> [flags]
```

### Options

```
  -h, --help           help for subgraph
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --level int      Maximum ancestor and descendant depth to traverse breadth-first.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --withTask       When ˋtrueˋ, includes the full task document for each accessible vertex in the response.
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
