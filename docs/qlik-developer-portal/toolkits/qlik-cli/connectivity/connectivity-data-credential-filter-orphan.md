---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-credential-filter-orphan/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-credential filter-orphan

## qlik connectivity data-credential filter-orphan

List orphan credentials

### Synopsis

Use this operation to retrieve data credentials that are not associated with any data connection. Filter results by credential type, data source ID, or separation status using the request body.

```
qlik connectivity data-credential filter-orphan [flags]
```

### Options

```
      --datasourceID string   Filter orphan credentials by data source ID.
  -f, --file file             Read request body from the specified file
  -h, --help                  help for filter-orphan
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --qSeparated int        Filter orphan credentials by separation status. ˋ0ˋ returns only embedded credentials. ˋ1ˋ returns only separated credentials.
                              Allowed values: "0", "1"
      --qType string          Filter orphan credentials by credential type.
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
