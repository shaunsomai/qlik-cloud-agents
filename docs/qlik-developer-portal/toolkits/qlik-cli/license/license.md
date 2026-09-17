---
source: https://qlik.dev/toolkits/qlik-cli/license/license/
last_updated: 2025-06-18T09:34:47+02:00
---

# license

## qlik license

Licenses is the resource representing tenant and user entitlements

### Synopsis

Licenses define tenant and user entitlements, and can be used in conjunction with the consumption API to get a picture of entitlement usage.

```
qlik license [flags]
```

### Options

```
  -h, --help   help for license
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
