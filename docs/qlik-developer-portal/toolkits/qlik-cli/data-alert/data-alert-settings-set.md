---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-settings-set/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert settings set

## qlik data-alert settings set

Update data alert settings

### Synopsis

Updates the settings for data alerts. User must be assigned the `TenantAdmin` role.

```
qlik data-alert settings set [flags]
```

### Options

```
      --enable-data-alerting   (Required) true if data-alerting feature is enabled. A status change could potentially result in a considerable amount of API operations to enable/disable triggers. Enabling this feature also requires that the license has this feature enabled.
  -f, --file file              Read request body from the specified file
  -h, --help                   help for set
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --retry int              Number of retries to do before failing, max 10
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
