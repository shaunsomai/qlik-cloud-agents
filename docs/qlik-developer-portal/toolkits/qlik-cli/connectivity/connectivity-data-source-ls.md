---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source ls

## qlik connectivity data-source ls

List datasources

### Synopsis

Returns the list of datasources available on the connector node. Each entry
includes the connector provider, capabilities, and optional UI metadata. Filter
by `dataSourceId` to retrieve a specific datasource, or set `includeDisabled`
to `true` to include datasources that have been disabled.

```
qlik connectivity data-source ls [flags]
```

### Options

```
      --dataSourceId string   Filters results to the specified datasource ID. When this parameter appears multiple times, only the last value is used.
      --detail                When ˋtrueˋ, includes connector node details in the response.
  -h, --help                  help for ls
      --includeDisabled       When ˋtrueˋ, includes disabled datasources in the response. Disabled datasources are excluded by default.
      --includeui             When ˋtrueˋ, includes UI metadata such as connect, credentials, and select dialog URLs in the response.
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
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
