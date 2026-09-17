---
source: https://qlik.dev/toolkits/qlik-cli/data-connection/data-connection-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-connection patch

## qlik data-connection patch

Patches a connection specified by connection ID (or by name when type=connectionname is set in query)

### Synopsis

Patches a connection specified by connection ID (or by name when type=connectionname is set in query).

```
qlik data-connection patch <qID> [flags]
```

### Options

```
  -f, --file file                       Read request body from the specified file
  -h, --help                            help for patch
      --interval int                    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                       Operation type
                                        Allowed values: "add", "replace", "remove"
      --path string                     Path to the target field to be patched
  -q, --quiet                           Return only IDs from the command
      --raw                             Return original response from server without any processing
      --retry int                       Number of retries to do before failing, max 10
      --type string                     The connection ID in the path becomes a connection name when this query parameter is set.
                                        Allowed values: "connectionname"
      --value string|bool|int|unknown   Value used for the patch. Required only for ˋaddˋ or ˋreplaceˋ operations. The value type should match the type of the target field.
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
