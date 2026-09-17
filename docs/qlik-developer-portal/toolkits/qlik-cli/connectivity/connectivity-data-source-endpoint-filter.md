---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-endpoint-filter/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source endpoint filter

## qlik connectivity data-source endpoint filter

Create a data loading endpoint

### Synopsis

Provisions a gRPC endpoint for loading data using the specified connection.
The connection can be resolved by name, ID, connection string, or datasource
ID. Returns the endpoint reference and resolved connection details required to
initiate a data load session.

```
qlik connectivity data-source endpoint filter [flags]
```

### Options

```
      --checkCredentials          
      --connectionId string       The unique identifier of the connection to use for the endpoint.
      --connectionName string     The name of the connection to use for the endpoint. The service resolves
                                  the connection name to an active instance. If the name is space-qualified
                                  (for example, ˋMySpace:ConnectionNameˋ), ˋspaceIdˋ is not required and is
                                  ignored. If the name uses the current-space format (for example,
                                  ˋ:ConnectionNameˋ), ˋspaceIdˋ is used for resolution; the personal space
                                  is assumed when ˋspaceIdˋ is omitted.
      --connectionString string   Connection string in Qlik CONNECT format.
      --dataSourceId string       The unique identifier of the datasource to use for the endpoint.
  -f, --file file                 Read request body from the specified file
  -h, --help                      help for filter
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --reloadId string           
      --retry int                 Number of retries to do before failing, max 10
      --spaceId string            The unique identifier of the space containing the connection. Required only when ˋconnectionNameˋ is unqualified (not space-prefixed).
      --type string               
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
