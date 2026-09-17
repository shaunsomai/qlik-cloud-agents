---
source: https://qlik.dev/toolkits/qlik-cli/web-integration/web-integration/
last_updated: 2025-06-18T09:34:47+02:00
---

# web-integration

## qlik web-integration

Manage whitelisted origins that can make requests to a specified tenant (CORS)

### Synopsis

A web integration is a resource representing a list of whitelisted origins that can make requests to a specified tenant. It is the implementation of the CORS mechanism within Qlik Cloud.

```
qlik web-integration [flags]
```

### Options

```
  -h, --help   help for web-integration
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
