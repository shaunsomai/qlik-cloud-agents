---
source: https://qlik.dev/toolkits/qlik-cli/data-connection/data-connection-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-connection update

## qlik data-connection update

Update multiple connections, only available to Admin

### Synopsis

Update multiple connections, only available to Admin. When update is to change ownership of a connection, the credentials associated with the connection will NOT be transferred to the new owner, and new owner is expected to provide their own credentials for the connection.

```
qlik data-connection update [flags]
```

### Options

```
      --connections-id string          Connection ID
      --connections-name string        Connection name
      --connections-ownerId string     User ID to which the connection will be updated. If not present, the connection's owner wont be changed
      --connections-spaceId string     Space ID to which the connection will be updated. If not present, the connection's space wont be changed. If it is empty string, then the connection will be moved to the personal space of the user identified by ownerId (If ownerId is undefined, then the connection will be in oroginal owner's personal space)
      --connections-spaceType string   Space type. Required when spaceId is specified
                                       Allowed values: "personal", "shared", "managed", "data"
  -f, --file file                      Read request body from the specified file
  -h, --help                           help for update
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
