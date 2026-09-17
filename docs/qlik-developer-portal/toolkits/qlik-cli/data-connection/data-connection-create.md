---
source: https://qlik.dev/toolkits/qlik-cli/data-connection/data-connection-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-connection create

## qlik data-connection create

Creates a new connection

### Synopsis

Creates a new connection. Depending on the fields defined in the request body, credentials embedded (or associated) in the connection can be updated or created.

```
qlik data-connection create [flags]
```

### Options

```
      --authUrlOnly                    When set to true, only authentication URL will be returned (i.e. no connection will be created) if datasource supports OAuth, and other properties set in the request will ignored. This property will be ignored if the request is not OAuth or datasource doesn't support OAuth
      --connectionProperties unknown   Connection properties required to create dataconnection for the given datasource, which is defined by the response of 'GET /v1/data-sources/:{datasourceId}/api-specs'
      --datasourceID string            
  -f, --file file                      Read request body from the specified file
  -h, --help                           help for create
      --interval int                   Duration in seconds to wait between retries, at least 1 (default 1)
      --owner string                   App ID
      --qArchitecture int              0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified.
                                       Allowed values: "0", "1"
      --qConnectStatement string       Connection string for the data connection
      --qConnectionSecret string       String that contains connection specific secret (or password) that requires encryption before persist to database. This field is connection level secret
      --qCredentialsID string          ID of the credential associated with the connection
      --qCredentialsName string        Name of the credential associated with the connection
      --qEngineObjectID string         Unique identifier (UUID) for the data connection as specified by the Sense engine. A UUID will be generated automatically if this field is not specified or empty
      --qID string                     Unique identifier (UUID) for the data connection. A UUID will be generated automatically if qID is not specified or empty
      --qLogOn string                  Indicates the type of user associated with the data connection.
                                       Allowed values: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER"
      --qName string                   
      --qPassword string               Any logon password associated with the data connection (connector encoded)
      --qSeparateCredentials           Indicates whether or not to create a credential-less connection
      --qType string                   Type of connection - indicates connection provider type
      --qUsername string               Any logon username associated with the data connection
      --qriInRequest string            QRI string of the connection. The string will be persisted to mongo when the request is originated from trusted client (i.e. dcaas) to avoid invalid QRi string.
  -q, --quiet                          Return only IDs from the command
      --raw                            Return original response from server without any processing
      --retry int                      Number of retries to do before failing, max 10
      --space string                   
      --tags strings                   
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
