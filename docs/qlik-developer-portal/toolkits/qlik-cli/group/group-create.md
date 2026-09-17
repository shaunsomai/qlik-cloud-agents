---
source: https://qlik.dev/toolkits/qlik-cli/group/group-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# group create

## qlik group create

Create group

### Synopsis

Creates a new group. The maximum number of groups a tenant can have is 10,000. Group names are case-sensitive, and must be unique.

```
qlik group create [flags]
```

### Options

```
      --assignedRoles unknowns      (Deprecated) Array of JSON-objects to send as the property assignedRoles.
      --assignedRoles-id string     The unique role identitier
      --assignedRoles-name string   The name of the role
      --description string          The description of the group.
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                 (Required) The name of the group (maximum length of 256 characters).
      --providerType string         The type of group provider. Must be "idp" or "custom". Defaults to "idp" if not provided.
                                    Allowed values: "idp", "custom"
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --status string               The status of the created group within the tenant. Defaults to active if empty.
                                    Allowed values: "active"
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
