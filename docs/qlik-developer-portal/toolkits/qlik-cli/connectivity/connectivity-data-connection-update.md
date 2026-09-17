---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection update

## qlik connectivity data-connection update

Update a connection

### Synopsis

Use this operation to replace a data connection with the values provided in the request body. All required fields must be included. To update a connection by name instead of ID, set the `type` query parameter to `connectionname`. Credentials embedded in or associated with the connection are created or updated based on the fields provided.

```
qlik connectivity data-connection update <qID> [flags]
```

### Options

```
      --datasourceID string        ID of the datasource associated with this connection
  -f, --file file                  Read request body from the specified file
  -h, --help                       help for update
      --interval int               Duration in seconds to wait between retries, at least 1 (default 1)
      --qArchitecture int          Indicates the data connector architecture. ˋ0ˋ for 64-bit, ˋ1ˋ for 32-bit. Default is ˋ0ˋ, if not specified.
                                   Allowed values: "0", "1"
      --qConnectStatement string   (Required) Connection string for the data connection
      --qConnectionSecret string   A connection-specific secret or password. When provided, replaces the existing secret. When set to an empty string, clears the existing secret. When omitted, the existing secret is preserved.
      --qCredentialsID string      ID of the credential associated with the connection
      --qCredentialsName string    Name of the credential associated with the connection
      --qEngineObjectID string     (Required) Unique identifier for the data connection as specified by the Sense engine
      --qID string                 (Required) Unique identifier for the data connection
      --qLogOn string              Logon type for the connection. ˋLOG_ON_SERVICE_USERˋ (or ˋ0ˋ) indicates service user logon; ˋLOG_ON_CURRENT_USERˋ (or ˋ1ˋ) indicates current user logon.
                                   Allowed values: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER"
      --qName string               (Required) Descriptive name of the data connection
      --qPassword string           Any logon password associated with the data connection
      --qSeparateCredentials       Indicates whether or not this is a credential-less connection
      --qType string               (Required) The connection type, identifying the provider of the underlying connector.
      --qUsername string           Any logon username associated with the data connection
  -q, --quiet                      Return only IDs from the command
      --raw                        Return original response from server without any processing
      --retry int                  Number of retries to do before failing, max 10
      --space string               ID of the space to which the connection belongs
      --spaceId string             Filter connections by space ID.
      --type string                When set to ˋconnectionnameˋ, the value of the connection ID in the path is interpreted as the connection's name rather than its unique identifier.
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
