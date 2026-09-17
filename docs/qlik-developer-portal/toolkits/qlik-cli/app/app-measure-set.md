---
source: https://qlik.dev/toolkits/qlik-cli/app/app-measure-set/
last_updated: 2025-06-18T09:34:47+02:00
---

# app measure set

## qlik app measure set

Set or update the measures in the current app

### Synopsis

Set or update the measures in the current app

```
qlik app measure set <glob-pattern-path-to-measures-files.json> [flags]
```

### Examples

```
qlik app measure set ./my-measures-glob-path.json
```

### Options

```
  -h, --help      help for set
      --no-save   Do not save the app
```

### Options inherited from parent commands

```
  -a, --app string               Name or identifier of the app
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
      --no-data                  Open app without data
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -t, --traffic                  Log JSON websocket traffic to stderr
      --ttl string               The Engine session's time to live in seconds (default "0")
  -v, --verbose                  Log extra information
```
