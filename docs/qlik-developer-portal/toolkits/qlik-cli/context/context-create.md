---
source: https://qlik.dev/toolkits/qlik-cli/context/context-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# context create

## qlik context create

Create a context with the specified configuration

### Synopsis

Create a context with the specified configuration

This command creates a context by using the supplied flags.
The information stored will be server url, headers and certificates
(if present) along with comment and the context-name.
Note that some global flags are also applicable such as
insecure and server-type which can be set as default for a context.

```
qlik context create <context name> [flags]
```

### Examples

```
qlik context create me@cloud --server https://my-tenant.eu.qlikcloud.com --api-key MY-API-KEY
qlik context create local --server localhost:9076 --comment "Local engine"
qlik context create me@qseow --server https://qseow.domain.com/jwt --comment "Qlik Sense Enterprise on Windows" --api-key MY-API-KEY --insecure
```

### Options

```
      --api-key string               API-key to be used for Qlik Cloud
      --comment string               Comment for the context
  -h, --help                         help for create
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
