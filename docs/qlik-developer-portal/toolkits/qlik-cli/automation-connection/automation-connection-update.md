---
source: https://qlik.dev/toolkits/qlik-cli/automation-connection/automation-connection-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation-connection update

## qlik automation-connection update

Update an automation connection

### Synopsis

Updates the specified properties of an automation connection.

```
qlik automation-connection update <automation-connectionId> [flags]
```

### Options

```
  -f, --file file             Read request body from the specified file
  -h, --help                  help for update
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --name string           The new name of the automation connection to be renamed to.
      --params unknowns       (Deprecated) Array of JSON-objects to send as the property params.
      --params-id string      The unique identifier of the automation connection parameter option.
      --params-value string   The value of the automation connection parameter option.
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
