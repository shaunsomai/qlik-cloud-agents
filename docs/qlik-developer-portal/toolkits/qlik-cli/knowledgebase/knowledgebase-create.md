---
source: https://qlik.dev/toolkits/qlik-cli/knowledgebase/knowledgebase-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# knowledgebase create

## qlik knowledgebase create

Create new knowledgebase

### Synopsis

Creates a new knowledgebase.

```
qlik knowledgebase create [flags]
```

### Options

```
      --advancedIndexing          User opt in to advanced parsing and chunking pipeline. Default is false, which will run legacy parsing and chunking.
      --description string        Description of the knowledgebase
  -f, --file file                 Read request body from the specified file
  -h, --help                      help for create
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
      --name string               (Required) Name of the knowledgebase
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --retry int                 Number of retries to do before failing, max 10
      --selectedErrorsCount int   Number of selected errors to store in the case of any failed datasources. Optional value with a default of 10.
      --spaceId string            (Required) Unique identifier of the space to contain the knowledgebase
      --tags strings              List of tags for knowledgebase
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
