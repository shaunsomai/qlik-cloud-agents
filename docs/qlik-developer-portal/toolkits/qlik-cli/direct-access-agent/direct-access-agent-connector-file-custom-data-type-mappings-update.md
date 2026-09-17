---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-connector-file-custom-data-type-mappings-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# direct-access-agent connector file custom-data-type-mappings update

## qlik direct-access-agent connector file custom-data-type-mappings update

Set connector type mapping configuration

### Synopsis

Completely replaces the contents of the custom data type mapping configuration file for the Generic ODBC connector. Partial updates are not supported. There are property naming differences between the API and the file contents. Use the API property format when making changes. Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.5+.

```
qlik direct-access-agent connector file custom-data-type-mappings update <direct-access-agentId> [flags]
```

### Options

```
  -f, --file file                                   Read request body from the specified file
  -h, --help                                        help for update
      --interval int                                Duration in seconds to wait between retries, at least 1 (default 1)
      --odbcCustomDataTypes-bit                     The IsBit property in the ODBC custom data type mapping file.
      --odbcCustomDataTypes-id string               The Identifier property in the ODBC custom data type mapping file.
      --odbcCustomDataTypes-nativeDataType string   The NativeDataType property in the ODBC custom data type mapping file.
      --odbcCustomDataTypes-qlikDataType string     The QlikDataType property in the ODBC custom data type mapping file.
      --odbcCustomDataTypes-size int                The Size property in the ODBC custom data type mapping file.
  -q, --quiet                                       Return only IDs from the command
      --raw                                         Return original response from server without any processing
      --retry int                                   Number of retries to do before failing, max 10
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
