---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-endpoint/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source endpoint

## qlik connectivity data-source endpoint

Manage connectivity data-source endpoints

### Synopsis

Datasource endpoints provide gRPC sessions for loading data through a resolved connection. Use this group to list active endpoint references or provision a new endpoint for a data load.

```
qlik connectivity data-source endpoint [flags]
```

### Options

```
  -h, --help   help for endpoint
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
