---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-settings/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source settings

## qlik connectivity data-source settings

Manage connectivity data-source settings

### Synopsis

Datasource settings control whether a datasource is enabled for tenant use. Use this group to view and update the operational settings for a specific datasource.

```
qlik connectivity data-source settings [flags]
```

### Options

```
  -h, --help   help for settings
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
