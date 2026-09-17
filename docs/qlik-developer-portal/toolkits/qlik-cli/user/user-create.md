---
source: https://qlik.dev/toolkits/qlik-cli/user/user-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# user create

## qlik user create

Create user

### Synopsis

Creates an invited user.

```
qlik user create [flags]
```

### Options

```
      --assignedRoles unknowns      (Deprecated) Array of JSON-objects to send as the property assignedRoles.
      --assignedRoles-id string     The unique identitier
      --assignedRoles-name string   The name of the entity
      --email string                The email address for the user. This is a required field when inviting a user.
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                 The name of the user.
      --picture string              A static url linking to the avatar of the user.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --status string               The status of the created user within the tenant.
                                    Allowed values: "invited"
      --subject string              (Required) The unique user identitier from an identity provider.
      --tenantId string             The tenant that the user will belong too.
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
