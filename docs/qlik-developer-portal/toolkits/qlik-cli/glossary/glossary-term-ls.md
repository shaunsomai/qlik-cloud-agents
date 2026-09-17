---
source: https://qlik.dev/toolkits/qlik-cli/glossary/glossary-term-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# glossary term ls

## qlik glossary term ls

Returns a list of terms for a glossary

### Synopsis

Returns a list of terms for a glossary.

```
qlik glossary term ls [flags]
```

### Options

```
      --countTotal          Optional parameter to request total count for query
      --filter string       Optional SCIM filter to be used to filter terms
                            Usable fields are
                            
                            - id
                            - name
                            - relatedInformation
                            - description
                            - abbreviation
                            - tags
                            - stewards
                            - status
                            - categories
      --glossaryId string   (Required) The glossary id.
  -h, --help                help for ls
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int           The total number of resources to retrieve.
      --next string         Optional parameter to request the next page.
      --prev string         Optional parameter to request the previous page.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --sort string         Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending.
                            Allowed values: "abbreviation", "+abbreviation", "-abbreviation", "description", "+description", "-description", "name", "+name", "-name", "status", "+status", "-status", "updated", "+updated", "-updated"
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
