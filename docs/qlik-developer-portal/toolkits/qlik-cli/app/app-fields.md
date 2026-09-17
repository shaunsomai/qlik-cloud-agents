---
source: https://qlik.dev/toolkits/qlik-cli/app/app-fields/
last_updated: 2025-06-18T09:34:47+02:00
---

# app fields

## qlik app fields

Print field list

### Synopsis

Print all the fields in an app, and for each field also some sample content, tags and and number of values

```
qlik app fields [flags]
```

### Examples

```
qlik app fields
```

### Options

```
  -a, --app string   Name or identifier of the app
  -h, --help         help for fields
      --no-data      Open app without data
  -q, --quiet        Only print IDs. Useful for scripting
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
