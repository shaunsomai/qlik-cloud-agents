---
source: https://qlik.dev/toolkits/qlik-cli/knowledgebase/knowledgebase-datasource-cancel/
last_updated: 2025-06-18T09:34:47+02:00
---

# knowledgebase datasource cancel

## qlik knowledgebase datasource cancel

Cancel sync of a knowledgebase datasource

### Synopsis

Cancels ongoing sync for a specified datasource.

```
qlik knowledgebase datasource cancel [flags]
```

### Options

```
      --datasourceId string      (Required) The id of the datasource to cancel sync for.
  -h, --help                     help for cancel
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --knowledgebaseId string   (Required) The id of the knowledgebase the datasource belongs to.
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
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
