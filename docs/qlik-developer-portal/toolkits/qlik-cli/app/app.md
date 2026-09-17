---
source: https://qlik.dev/toolkits/qlik-cli/app/app/
last_updated: 2025-06-18T09:34:47+02:00
---

# app

## qlik app

Manage, build, edit and analyze apps

### Synopsis

Apps are a core part of Qlik Cloud Analytics, and represent either an Analytics app (Qlik Sense or QlikView application) or a script (headless Qlik Sense application).

```
qlik app [flags]
```

### Options

```
  -h, --help   help for app
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
