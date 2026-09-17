---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality-computation/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-quality computation

## qlik data-governance data-quality computation

Manage data quality computations

### Synopsis

Data quality computations run profiling and quality assessment asynchronously for a dataset. Use this group to start a computation and poll for its status until results are available.

```
qlik data-governance data-quality computation [flags]
```

### Options

```
  -h, --help   help for computation
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
