---
source: https://qlik.dev/toolkits/qlik-cli/knowledgebase/knowledgebase-datasource-history-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# knowledgebase datasource history ls

## qlik knowledgebase datasource history ls

List knowledgebase datasource sync histories

### Synopsis

Retrieves sync history for a specified datasource in a knowledgebase. Returns a `404` if there is no sync history, or if the calling user doesn't have access to the datasource.

```
qlik knowledgebase datasource history ls [flags]
```

### Options

```
      --datasourceId string      (Required) The id of the datasource.
  -h, --help                     help for ls
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --knowledgebaseId string   (Required) The id of the knowledgebase the datasource belongs to.
      --limit int                The total number of resources to retrieve.
      --next string              Optional parameter to request the next page.
      --prev string              Optional parameter to request the previous page.
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
      --sort string              Optional resource field name to sort on, case insensitive, eg. name. Can be prefixed with - to set descending order, defaults to ascending.
                                 Allowed values: "COMPLETED", "-COMPLETED"
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
