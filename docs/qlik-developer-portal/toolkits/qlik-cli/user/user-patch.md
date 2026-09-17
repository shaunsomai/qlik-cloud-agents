---
source: https://qlik.dev/toolkits/qlik-cli/user/user-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# user patch

## qlik user patch

Update user by ID

### Synopsis

Updates fields for a user resource

```
qlik user patch <userId> [flags]
```

### Options

```
      --body unknowns               (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for patch
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                   The operation to be performed. The fields ˋsetˋ and ˋunsetˋ are deprecated.
                                    Allowed values: "replace", "set", "unset", "add", "renew", "remove-value"
      --path string                 A JSON Pointer. The field ˋrolesˋ is deprecated.
                                    Allowed values: "/name", "/roles", "/assignedRoles", "/inviteExpiry", "/preferredZoneinfo", "/preferredLocale", "/status", "/assignedGroups"
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --value string|bool|unknown   The value to be used for this operation.
      --value-id string             The unique identitier
      --value-name string           The value to be used for this operation.
      --value-providerType string   The type of provider for the group.
                                    Allowed values: "idp", "custom"
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
