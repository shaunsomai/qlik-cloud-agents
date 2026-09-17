---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection

## qlik connectivity data-connection

Manage connectivity data-connections

### Synopsis

Connectivity data-connections define how Qlik Cloud connects to external data sources, including connection properties, ownership, and linked credentials. Use this group to create, inspect, update, duplicate, and remove those connections.

```
qlik connectivity data-connection [flags]
```

### Options

```
  -h, --help   help for data-connection
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
