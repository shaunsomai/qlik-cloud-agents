---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-rm/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection rm

## qlik connectivity data-connection rm

Delete a connection

### Synopsis

Use this operation to delete a data connection by its unique identifier. To delete a connection by name instead of ID, set the `type` query parameter to `connectionname`. This action cannot be undone.

```
qlik connectivity data-connection rm <qID> [flags]
```

### Options

```
  -h, --help             help for rm
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --spaceId string   Filter connections by space ID.
      --type string      When set to ˋconnectionnameˋ, the value of the connection ID in the path is interpreted as the connection's name rather than its unique identifier.
                         Allowed values: "connectionname"
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
