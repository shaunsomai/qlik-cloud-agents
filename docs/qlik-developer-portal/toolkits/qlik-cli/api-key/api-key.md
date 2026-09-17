---
source: https://qlik.dev/toolkits/qlik-cli/api-key/api-key/
last_updated: 2025-06-18T09:34:47+02:00
---

# api-key

## qlik api-key

Manage API keys used for authorization

### Synopsis

API keys can be used by developers to gain programmatic access to the Qlik platform, acting as their own user.

```
qlik api-key [flags]
```

### Options

```
  -h, --help   help for api-key
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
