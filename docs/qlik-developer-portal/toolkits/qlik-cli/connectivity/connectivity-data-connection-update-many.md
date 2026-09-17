---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-update-many/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection update-many

## qlik connectivity data-connection update-many

Update multiple connections

### Synopsis

Use this operation to update multiple data connections in a single request. Requires the Admin role. Returns a 207 Multi-Status response with the outcome for each connection. When transferring ownership, credentials associated with the connection are not automatically transferred to the new owner; the new owner must provide their own credentials.

```
qlik connectivity data-connection update-many [flags]
```

### Options

```
      --connections-id string          Connection ID
      --connections-name string        Connection name
      --connections-ownerId string     The user ID to transfer ownership to. If omitted, the connection's owner is not changed.
      --connections-spaceId string     The space ID to move the connection to. If omitted, the connection's space is not changed. If set to an empty string, the connection is moved to the personal space of the user identified by ˋownerIdˋ. If ˋownerIdˋ is also omitted, the connection is moved to the original owner's personal space.
      --connections-spaceType string   The type of the target space. Required when ˋspaceIdˋ is specified.
                                       Allowed values: "personal", "shared", "managed", "data"
  -f, --file file                      Read request body from the specified file
  -h, --help                           help for update-many
      --interval int                   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                          Return only IDs from the command
      --raw                            Return original response from server without any processing
      --retry int                      Number of retries to do before failing, max 10
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
