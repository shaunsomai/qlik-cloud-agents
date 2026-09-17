---
source: https://qlik.dev/toolkits/qlik-cli/context/context-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# context update

## qlik context update

Update a context with the specified configuration

### Synopsis

Update a context with the specified configuration

```
qlik context update <context name> [flags]
```

### Examples

```
qlik context update local-engine
qlik context update me@qseow --server https://qseow.domain.com/jwt --comment "Qlik Sense Enterprise on Windows"
qlik context update me@qseow --insecure"
```

### Options

```
      --api-key string               API-key to be used for Qlik Cloud
      --comment string               Comment for the context
  -h, --help                         help for update
      --oauth-client-id string       The ID of the configured OAuth client, obtained from My Qlik (https://account.myqlik.qlik.com/account)
      --oauth-client-secret string   The secret of the configured OAuth client, obtained from My Qlik (https://account.myqlik.qlik.com/account)
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
