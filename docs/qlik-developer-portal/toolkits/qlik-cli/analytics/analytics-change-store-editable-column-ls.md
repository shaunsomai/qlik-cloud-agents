---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-change-store-editable-column-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# analytics change-store editable-column ls

## qlik analytics change-store editable-column ls

Get a list of editable-columns

### Synopsis

Returns a paginated list of editable-columns that belong to the specified change store, supporting optional filtering and sorting.

```
qlik analytics change-store editable-column ls <change-storeId> [flags]
```

### Options

```
      --filter string   A SCIM filter expression used to filter the result.
                        The filter parameter allows complex logical expressions using comparison operators and grouping.
                        - **Supported attributes:** ˋreferenceIdˋ, ˋspaceIdˋ, ˋcreatedByˋ, ˋtypeˋ, ˋcolumnNameˋ, ˋusedBy.appIdˋ, ˋusedBy.chartIdˋ 
                        - **Supported operators:** ˋeqˋ, ˋneˋ, ˋcoˋ, ˋswˋ, ˋewˋ, ˋprˋ, ˋgtˋ, ˋgeˋ, ˋltˋ, ˋleˋ  
                        - **Logical operators:** ˋandˋ, ˋorˋ, ˋnotˋ
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       Defines the size of each paged result (maximum 100).
      --page string     Used for cursor-based pagination.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Sort results by a field, with optional + (asc) or - (desc) prefix
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
