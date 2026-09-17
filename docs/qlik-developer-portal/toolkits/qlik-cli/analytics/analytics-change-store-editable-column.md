---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-change-store-editable-column/
last_updated: 2026-06-03T09:30:31+02:00
---

# analytics change-store editable-column

## qlik analytics change-store editable-column

Inspect editable columns in change-stores

### Synopsis

Editable columns define which fields in a change-store can be updated and tracked. Use this group to inspect the editable column definitions available for a specific change store.

```
qlik analytics change-store editable-column [flags]
```

### Options

```
  -h, --help   help for editable-column
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
