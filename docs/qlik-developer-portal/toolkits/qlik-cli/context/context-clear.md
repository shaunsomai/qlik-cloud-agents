---
source: https://qlik.dev/toolkits/qlik-cli/context/context-clear/
last_updated: 2025-06-18T09:34:47+02:00
---

# context clear

## qlik context clear

Set the current context to none

### Synopsis

Set the current context to none

```
qlik context clear [flags]
```

### Examples

```
qlik context clear
```

### Options

```
  -h, --help   help for clear
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
