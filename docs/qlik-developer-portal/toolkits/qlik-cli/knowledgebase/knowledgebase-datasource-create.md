---
source: https://qlik.dev/toolkits/qlik-cli/knowledgebase/knowledgebase-datasource-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# knowledgebase datasource create

## qlik knowledgebase datasource create

Add a datasource to a knowledgebase

### Synopsis

Adds a datasource to a knowledgebase.

```
qlik knowledgebase datasource create [flags]
```

### Options

```
  -f, --file file                                 Read request body from the specified file
      --fileConfig-connectionId string            (Required) connection id to be used to retrieve the raw data
      --fileConfig-crawlPatterns-pattern string   Regex patterna to filter links on
      --fileConfig-crawlPatterns-type string      include or exclude
                                                  Allowed values: "include", "exclude"
      --fileConfig-files strings                  Specification on where to fetch the files for. This is required when the type == 'file'. Only one of path and files can be set. Path takes precedence if both are provided.
      --fileConfig-folder string                  Root folder for traversing.
      --fileConfig-scope-depth int                (Required) The number of levels of sub folders that should be considered
      --fileConfig-scope-extensions strings       list of file extensions to be considered
      --fileConfig-scope-maxFilesPerFolder int    Maximum number of files per folder that should be considered
      --fileConfig-scope-maxFilesTotal int        Total number of files that should be considered
      --fileConfig-scope-maxSize int              Optional parameter. Max size of downloaded files in bytes
      --fileConfig-scope-modifiedAfter string     only files modified after this time should be indexed. If set older files will be removed from index.
      --fileConfig-userId string                  (Required) userId of the owner of the datasource fileConfig
  -h, --help                                      help for create
      --interval int                              Duration in seconds to wait between retries, at least 1 (default 1)
      --knowledgebaseId string                    (Required) The id of the knowledgebase.
      --name string                               (Required) Name of the datasource
  -q, --quiet                                     Return only IDs from the command
      --raw                                       Return original response from server without any processing
      --retry int                                 Number of retries to do before failing, max 10
      --type string                               (Required) 
                                                  Allowed values: "file", "web", "database"
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
