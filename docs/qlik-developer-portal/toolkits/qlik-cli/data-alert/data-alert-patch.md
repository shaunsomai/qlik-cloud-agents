---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert patch

## qlik data-alert patch

Update data alert task

### Synopsis

Updates one or more properties of a specific data alerting task.

```
qlik data-alert patch <data-alertId> [flags]
```

### Options

```
  -f, --file file       Read request body from the specified file
  -h, --help            help for patch
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string       The operation to be performed
                        Allowed values: "replace"
      --path string     A JSON Patch document as defined in https://datatracker.ietf.org/doc/html/rfc6902
                        Allowed values: "/ownerName", "/ownerId", "/conditionId", "/enabledAction", "/bookmarkId", "/name", "/description", "/throttling", "/triggerType", "/scheduleOptions"
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --value unknown   The value to be used for this operation.
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
