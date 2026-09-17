---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-api-spec/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source api-spec

## qlik connectivity data-source api-spec

Get datasource connection schema

### Synopsis

Retrieves the connection property schema for the specified datasource,
including the connector provider, version, and the full list of properties
required to establish a connection. Use this operation to discover which
fields must be supplied when creating or generating a connection string for
this datasource.

```
qlik connectivity data-source api-spec <data-sourceId> [flags]
```

### Options

```
  -h, --help           help for api-spec
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
