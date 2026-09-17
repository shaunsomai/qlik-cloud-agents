---
source: https://qlik.dev/toolkits/qlik-cli/data-set/data-set-profiles/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-set profiles

## qlik data-set profiles

Get profile for the given dataset and connection Id pair, if the profile already exists in the system

### Synopsis

Get profile for the given dataset and connection Id pair, if the profile already exists in the system. Profile returned can be either latest or Stale one based on when it was computed.

```
qlik data-set profiles <data-setId> [flags]
```

### Options

```
      --dataConnectionIds strings   Comma-separated data connection IDs.
  -h, --help                        help for profiles
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                   The total number of resources to retrieve.
      --page int                    
      --projections strings         Comma-separated fields to return in the response.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --sort strings                
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
