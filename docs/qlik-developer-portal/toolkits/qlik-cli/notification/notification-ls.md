---
source: https://qlik.dev/toolkits/qlik-cli/notification/notification-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# notification ls

## qlik notification ls

List all supported notifications

### Synopsis

List all supported notifications

```
qlik notification ls [flags]
```

### Options

```
  -h, --help                     help for ls
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --locale string            If present, idenfies the language of the returned 'friendlyName' property.
      --manageableInHub string   If present, represents the 'manageableInHub' value to filter by.
                                 Allowed values: "true", "false"
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
      --subscribable string      If present, represents the 'subscribable' value to filter by.
                                 Allowed values: "true", "false"
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
