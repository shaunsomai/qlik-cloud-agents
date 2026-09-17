---
source: https://qlik.dev/toolkits/qlik-cli/glossary/glossary-category-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# glossary category create

## qlik glossary category create

Creates a new category

### Synopsis

Creates a new category.

```
qlik glossary category create [flags]
```

### Options

```
      --description string   
  -f, --file file            Read request body from the specified file
      --glossaryId string    (Required) The glossary id.
  -h, --help                 help for create
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          The name of the category. May not be identical to another category belonging to the same parent.
      --parentId string      
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --stewards strings     This list contains the UIDs of the stewards of the category.
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
