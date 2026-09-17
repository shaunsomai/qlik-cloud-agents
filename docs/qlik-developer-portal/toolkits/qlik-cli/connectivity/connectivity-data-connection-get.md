---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-get/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection get

## qlik connectivity data-connection get

Get a connection

### Synopsis

Use this operation to retrieve a single data connection by its unique identifier. To look up a connection by name instead of ID, set the `type` query parameter to `connectionname`. Returns the full connection object including the caller's access privileges.

```
qlik connectivity data-connection get <qID> [flags]
```

### Options

```
      --byCredentialName      When ˋtrueˋ, the value of the ˋcredentialIdˋ in the query is interpreted as the credential's name rather than its unique identifier.
      --credentialId string   Filter by credential ID.
      --extended              When ˋtrueˋ, returns an extended set of properties, including the encrypted credential string.
  -h, --help                  help for get
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --noCache               When ˋtrueˋ, bypasses the cache and returns the most up-to-date data file connections. By default, datafile connections may be served from cache.
      --parseConnection       When ˋtrueˋ, includes a list of parsed connection properties in the response. Default is ˋfalseˋ.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --spaceId string        Filter connections by space ID.
      --type string           When set to ˋconnectionnameˋ, the value of the connection ID in the path is interpreted as the connection's name rather than its unique identifier.
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
