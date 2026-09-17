---
source: https://qlik.dev/toolkits/qlik-cli/role/role-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# role create

## qlik role create

Create role

### Synopsis

Creates a custom role. Role names must be unique, and there is a maximum of 500 custom roles per tenant. Requestor must be assigned the `TenantAdmin` role.

```
qlik role create [flags]
```

### Options

```
      --assignedScopes strings   Selection of scopes to assign to role
      --description string       Role description
  -f, --file file                Read request body from the specified file
  -h, --help                     help for create
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --name string              (Required) Role name, needs to be unique
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
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
