---
source: https://qlik.dev/toolkits/qlik-cli/app/app-script-set/
last_updated: 2025-06-18T09:34:47+02:00
---

# app script set

## qlik app script set

Set the script in the current app

### Synopsis

Set the script in the current app

```
qlik app script set <path-to-script-file.qvs> [flags]
```

### Examples

```
qlik app script set ./my-script-file.qvs
```

### Options

```
  -a, --app string   Name or identifier of the app
  -h, --help         help for set
      --no-data      Open app without data
      --no-save      Do not save the app
  -t, --traffic      Log JSON websocket traffic to stderr
      --ttl string   The Engine session's time to live in seconds (default "0")
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
