---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-connection/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file connection

## qlik core data-file connection

Manage core data-file connections

### Synopsis

Data-file connections expose the built-in storage connections available to apps and spaces. Use this group to list or filter those connections when working with uploaded files and folders.

```
qlik core data-file connection [flags]
```

### Options

```
  -h, --help   help for connection
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
