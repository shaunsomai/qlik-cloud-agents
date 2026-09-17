---
source: https://qlik.dev/toolkits/qlik-cli/automation-connection/automation-connection-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation-connection ls

## qlik automation-connection ls

List automation connections

### Synopsis

Retrieves a list of automation connections the requesting user has access to.

```
qlik automation-connection ls [flags]
```

### Options

```
      --cursor string   Pagination cursor returned from a previous request.
      --filter string   Filters the result based on the specified criteria: name, connectorId, ownerId, or spaceId.
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --listAll         When true, list all connections. Restricted to tenant admins and analytics admins.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort by, with +- prefix indicating sort order. (ˋ?sort=-nameˋ => sort on the ˋnameˋ field using descending order).
                        Allowed values: "id", "name", "createdAt", "updatedAt", "+id", "+name", "+createdAt", "+updatedAt", "-id", "-name", "-createdAt", "-updatedAt"
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
