---
source: https://qlik.dev/toolkits/qlik-cli/data-connection/data-connection-get/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-connection get

## qlik data-connection get

Retrieves a connection by connection ID, or by name when the query parameter "type" is set to "connectionname

### Synopsis

Retrieves a connection by connection ID, or by name when the query parameter "type" is set to "connectionname."

```
qlik data-connection get <qID> [flags]
```

### Options

```
      --byCredentialName      If set to true, credentialId in the query will be interpreted as credential's name
      --credentialId string   Credential ID
      --extended              Returns extended list of properties (e.g. encrypted credential string) when set to true.
  -h, --help                  help for get
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --noCache               datafiles connections will be returned from cache by default (if data-connections is configured to use cache), this query parameter is used disable this default behavior, e.g. return an update-to-date datafiles connection if the query is set to true
      --parseConnection       List of connection properties shall be returned when the query is set to true, default is false
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --spaceId string        Filtering on connections by space ID
      --type string           The connection ID in the path becomes a connection name when this query parameter is set.
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
