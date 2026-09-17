---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-settings-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source settings update

## qlik connectivity data-source settings update

Update datasource settings

### Synopsis

Updates the configuration settings for the specified datasource. Use this
operation to enable or disable a datasource for the tenant. The full settings
object must be supplied; partial updates are not supported.

```
qlik connectivity data-source settings update <data-sourceId> [flags]
```

### Options

```
      --disabled       (Required) When ˋtrueˋ, disables the datasource. When ˋfalseˋ, enables it.
  -f, --file file      Read request body from the specified file
  -h, --help           help for update
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
