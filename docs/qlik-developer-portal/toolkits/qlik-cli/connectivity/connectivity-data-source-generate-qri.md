---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-source-generate-qri/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-source generate-qri

## qlik connectivity data-source generate-qri

Generate QRI values

### Synopsis

Generates Qlik Resource Identifiers (QRIs) for a batch of connections. Each
connection can be identified by ID, name, or connection string. Partial
failures are reported per entry in the response — a `207 Multi-Status`
response is always returned regardless of individual entry outcomes.

```
qlik connectivity data-source generate-qri [flags]
```

### Options

```
      --data-connection string             The connection identifier — a UUID, name, or connection string — corresponding to the value of ˋconnectionTypeˋ.
      --data-connectionType string         Type of connection identifier used in QRI generation requests:
                                             * ˋidˋ — connection UUID
                                             * ˋnameˋ — connection name, optionally space-qualified (for example, ˋMySpace:MyConnectionˋ or ˋ:MyConnectionˋ)
                                             * ˋpropertiesˋ — connection string in Qlik CONNECT format
                                           Allowed values: "id", "name", "properties"
      --data-dataSourceId string           The unique identifier of the datasource for the connection. Must match the datasource type when ˋconnectionTypeˋ is ˋpropertiesˋ.
      --data-itemProperties-name string    The name of the property as defined in the QRI definition template. When omitted, properties are treated as an ordered array.
      --data-itemProperties-value string   The value to substitute for this property in the QRI template.
      --data-pathProperties-name string    The name of the property as defined in the QRI definition template. When omitted, properties are treated as an ordered array.
      --data-pathProperties-value string   The value to substitute for this property in the QRI template.
      --data-requestId string              Optional caller-provided identifier used to correlate this request entry with its response. Should be unique within a batch request.
      --data-spaceId string                The unique identifier of the space containing the connection. Required for name-based lookups; ignored when ˋconnectionTypeˋ is ˋpropertiesˋ.
  -f, --file file                          Read request body from the specified file
  -h, --help                               help for generate-qri
      --interval int                       Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                              Return only IDs from the command
      --raw                                Return original response from server without any processing
      --rawValues                          When ˋtrueˋ, returns raw QRI values. When ˋfalseˋ, returns hashed QRI values.
      --retry int                          Number of retries to do before failing, max 10
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
