---
source: https://qlik.dev/toolkits/qlik-cli/group/group-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# group patch

## qlik group patch

Update group by ID

### Synopsis

Updates the requested group.

```
qlik group patch <groupId> [flags]
```

### Options

```
      --body unknowns       (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file           Read request body from the specified file
  -h, --help                help for patch
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --op string           The operation to be performed. Currently "replace" is the only supported operation.
                            Allowed values: "replace"
      --path string         Attribute name of a field of the Groups entity. "Name" and "description" is only available for custom groups.
                            Allowed values: "assignedRoles", "name", "description"
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --value string        The roles to assign to the group (limit of 100 roles per group) or the new custom group name or description.
      --value-id string     The unique role identitier
      --value-name string   The name of the role
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
