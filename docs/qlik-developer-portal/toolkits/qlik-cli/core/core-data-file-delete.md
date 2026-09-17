---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-delete/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file delete

## qlik core data-file delete

Inspect deleted core data-files

### Synopsis

Deleted data-files remain queryable through this command group so you can review removed files and folders. Use it to inspect deletion records and related metadata without restoring the content.

```
qlik core data-file delete [flags]
```

### Options

```
  -h, --help   help for delete
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
