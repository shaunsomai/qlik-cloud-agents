---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection create

## qlik connectivity data-connection create

Create a connection

### Synopsis

Use this operation to create a new data connection in your tenant. Depending on the fields provided in the request body, credentials embedded in or associated with the connection are created or updated alongside the connection.

```
qlik connectivity data-connection create [flags]
```

### Options

```
      --authUrlOnly                    When ˋtrueˋ, only the authentication URL is returned and no connection is created, provided the data source supports OAuth. All other request properties are ignored. Has no effect if the data source does not support OAuth.
      --connectionProperties unknown   Connection properties required to establish the connection for the specified data source. The expected properties are defined by the response of ˋGET /connectivity/data-sources/{datasourceId}/api-specsˋ.
      --datasourceID string            
  -f, --file file                      Read request body from the specified file
  -h, --help                           help for create
      --interval int                   Duration in seconds to wait between retries, at least 1 (default 1)
      --ownerId string                 App ID
      --qArchitecture int              Indicates the data connector architecture. ˋ0ˋ for 64-bit, ˋ1ˋ for 32-bit. Default is ˋ0ˋ, if not specified.
                                       Allowed values: "0", "1"
      --qConnectStatement string       Connection string for the data connection
      --qConnectionSecret string       String that contains connection specific secret (or password) that requires encryption before persist to database. This field is connection level secret
      --qCredentialsID string          ID of the credential associated with the connection
      --qCredentialsName string        Name of the credential associated with the connection
      --qEngineObjectID string         Unique identifier (UUID) for the data connection as specified by the Qlik Sense engine. A UUID will be generated automatically if this field is not specified or empty.
      --qID string                     Unique identifier (UUID) for the data connection. A UUID will be generated automatically if ˋqIDˋ is not specified or empty.
      --qLogOn string                  Logon type for the connection. ˋLOG_ON_SERVICE_USERˋ (or ˋ0ˋ) indicates service user logon; ˋLOG_ON_CURRENT_USERˋ (or ˋ1ˋ) indicates current user logon.
                                       Allowed values: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER"
      --qName string                   
      --qPassword string               Any logon password associated with the data connection (connector encoded)
      --qSeparateCredentials           When ˋtrueˋ, creates a credential-less connection that does not embed authentication details. Default is ˋfalseˋ.
      --qType string                   The connection type, identifying the provider of the underlying connector.
      --qUsername string               Any logon username associated with the data connection
      --qriInRequest string            The QRI (Qlik Resource Identifier) string for the connection. When provided by a trusted client, this value is persisted as the connection's QRI to ensure consistency.
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
