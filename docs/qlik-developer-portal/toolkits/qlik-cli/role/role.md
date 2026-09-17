---
source: https://qlik.dev/toolkits/qlik-cli/role/role/
last_updated: 2025-06-18T09:34:47+02:00
---

# role

## qlik role

Resource representing a role in the system

### Synopsis

Tenant roles are assigned to users or groups in the tenant, and define what permissions they have.

```
qlik role [flags]
```

### Options

```
  -h, --help   help for role
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
