---
source: https://qlik.dev/toolkits/qlik-cli/space/space-assignment-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# space assignment ls

## qlik space assignment ls

List assignments for a space

### Synopsis

Retrieves the assignments of the space matching the query. Each assignment represents one user or group and their corresponding roles in the space. Assignments are not shown for the owner of a space, who receive all `assignableRoles` by default.

```
qlik space assignment ls [flags]
```

### Options

```
      --assigneeId string   Filters assignment for a specific assigneeid.
  -h, --help                help for ls
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int           The total number of resources to retrieve.
      --next string         The next page cursor. Next links make use of this.
      --prev string         The previous page cursor. Previous links make use of this.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --spaceId string      (Required) The ID of the space of the assignment.
      --type string         The type of assignment. Supported values are user or group.
                            Allowed values: "user", "group", "bot"
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
