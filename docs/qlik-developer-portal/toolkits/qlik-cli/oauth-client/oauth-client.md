---
source: https://qlik.dev/toolkits/qlik-cli/oauth-client/oauth-client/
last_updated: 2025-06-18T09:34:47+02:00
---

# oauth-client

## qlik oauth-client

Create and manage OAuth clients

### Synopsis

Create and manage the configuration of OAuth clients in your tenant.

```
qlik oauth-client [flags]
```

### Options

```
  -h, --help   help for oauth-client
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
