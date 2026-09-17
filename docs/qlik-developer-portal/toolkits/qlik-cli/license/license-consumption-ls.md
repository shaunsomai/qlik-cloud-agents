---
source: https://qlik.dev/toolkits/qlik-cli/license/license-consumption-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# license consumption ls

## qlik license consumption ls

Retrieves license consumption for the current tenant

### Synopsis

Retrieves license consumption for the current tenant

```
qlik license consumption ls [flags]
```

### Options

```
      --filter string   The SCIM filter for the query. Filterable property is "endTime".
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --page string     The requested page.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort on; can be prefixed with +/- for ascending/descending sort order.
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
