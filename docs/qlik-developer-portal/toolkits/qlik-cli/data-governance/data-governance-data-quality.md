---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-quality

## qlik data-governance data-quality

Inspect data quality resources

### Synopsis

Data quality resources let you trigger dataset quality computations and retrieve global quality summaries. Use this group to monitor computation status and review dataset-level quality outcomes.

```
qlik data-governance data-quality [flags]
```

### Options

```
  -h, --help   help for data-quality
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
