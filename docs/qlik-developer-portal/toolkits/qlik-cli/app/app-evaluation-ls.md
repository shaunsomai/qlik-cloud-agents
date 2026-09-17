---
source: https://qlik.dev/toolkits/qlik-cli/app/app-evaluation-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# app evaluation ls

## qlik app evaluation ls

Retrieve a list of all historic evaluations for an app GUID

### Synopsis

Find all evaluations for an app GUID.
Supports paging via next, prev which are sent in the response body

```
qlik app evaluation ls [flags]
```

### Options

```
      --all             Get the full data of the evaluation
      --appId string    (Required) The app guid.
      --fileMode        Add file transfer headers to response
      --format string   Specify output format, currently supported are 'json' and 'xml'
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --next string     The app evaluation id to get next page from
      --prev string     The app evaluation id to get previous page from
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Property to sort list on
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
