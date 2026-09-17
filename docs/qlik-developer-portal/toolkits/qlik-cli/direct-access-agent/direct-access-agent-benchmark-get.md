---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-benchmark-get/
last_updated: 2026-06-03T09:30:31+02:00
---

# direct-access-agent benchmark get

## qlik direct-access-agent benchmark get

Get benchmark status

### Synopsis

Retrieves the current status and progress of a running or completed benchmark task. Use this endpoint to monitor benchmark execution and retrieve performance metrics once the task is completed. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

```
qlik direct-access-agent benchmark get <benchmarkId> [flags]
```

### Options

```
      --direct-access-agentId string   (Required) The agent ID
  -h, --help                           help for get
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
