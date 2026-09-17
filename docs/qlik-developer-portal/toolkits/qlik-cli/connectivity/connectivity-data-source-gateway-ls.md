---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-gateway-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source gateway ls

## qlik connectivity data-source gateway ls

List datasource gateways

### Synopsis

Returns the list of gateway IDs available for the specified Direct Access
Gateway datasource. Gateways enable on-premises datasources to be accessed
from Qlik Cloud. Results are returned from a cache by default; set
`forceRefresh` to `true` to retrieve the current list from the backend.

```
qlik connectivity data-source gateway ls <data-sourceId> [flags]
```

### Options

```
      --forceRefresh   When ˋtrueˋ, bypasses the cache and retrieves the current gateway list from the backend. When ˋfalseˋ or omitted, a cached list is returned.
  -h, --help           help for ls
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
