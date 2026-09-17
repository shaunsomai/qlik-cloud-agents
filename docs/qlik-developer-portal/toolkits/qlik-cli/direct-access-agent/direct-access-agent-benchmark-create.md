---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-benchmark-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# direct-access-agent benchmark create

## qlik direct-access-agent benchmark create

Start agent benchmark

### Synopsis

Starts a background benchmark task to measure the performance of a Direct Access agent. Use this endpoint to evaluate agent throughput and latency for capacity planning and performance optimization. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

```
qlik direct-access-agent benchmark create [flags]
```

### Options

```
      --direct-access-agentId string   (Required) The agent ID
      --force                          Forces the benchmark to start regardless of the state of the agent. Does not override QCS resource limits. Use with caution.
      --gigaBytesToTransfer int        The volume of data in GB to transfer during the throughput measurement part of the benchmark.
  -h, --help                           help for create
      --interval int                   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                          Return only IDs from the command
      --raw                            Return original response from server without any processing
      --retry int                      Number of retries to do before failing, max 10
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
