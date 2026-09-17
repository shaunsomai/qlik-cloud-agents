---
source: https://qlik.dev/toolkits/qlik-cli/tenant-settings/tenant-settings-toggle-cross-region-inference/
last_updated: 2026-06-03T09:30:31+02:00
---

# tenant-settings toggle-cross-region-inference

## qlik tenant-settings toggle-cross-region-inference

Toggle cross-region inference

### Synopsis

Sets the cross-region inference setting for the tenant. Creates tenant settings if none exist, or updates existing settings. This is access controlled by the permission `admin.tenant-settings:update`.
When cross-region inference is required, you must include an additional header `x-qlik-consent-verified: true` in your API requests to confirm that you have the authority to enable this feature and accept the associated terms.

```
qlik tenant-settings toggle-cross-region-inference [flags]
```

### Options

```
  -f, --file file      Read request body from the specified file
  -h, --help           help for toggle-cross-region-inference
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --value          (Required) Set to true to enable cross-region inference, false to disable.
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
