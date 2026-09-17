---
source: https://qlik.dev/toolkits/qlik-cli/collection/collection-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# collection update

## qlik collection update

Update a collection's name and description

### Synopsis

Updates a collection's name and description and returns the updated collection. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value.

```
qlik collection update <collectionId> [flags]
```

### Options

```
      --description string   
  -f, --file file            Read request body from the specified file
  -h, --help                 help for update
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
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
