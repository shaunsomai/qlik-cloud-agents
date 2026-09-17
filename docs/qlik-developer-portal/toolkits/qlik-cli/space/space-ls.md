---
source: https://qlik.dev/toolkits/qlik-cli/space/space-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# space ls

## qlik space ls

List spaces

### Synopsis

Retrieves spaces that the current user has access to and match the query.

```
qlik space ls [flags]
```

### Options

```
      --action string             Action on space. Supports only "?action=publish".
      --environment.name string   Environment name to filter by. For example, "?environment.name=Development". Use an empty value to return spaces with no environment.
      --environmentId string      Environment ID to filter by. For example, "?environmentId=67f4fba37f7cbb2f04ce727a". Use an empty value to return spaces with no environment.
  -h, --help                      help for ls
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                 The total number of resources to retrieve.
      --name string               Space name to search and filter for. Case-insensitive open search with wildcards both as prefix and suffix. For example, "?name=fin" will get "finance", "Final" and "Griffin".
      --next string               The next page cursor. Next links make use of this.
      --ownerId string            Space ownerId to filter by. For example, "?ownerId=123".
      --prev string               The previous page cursor. Previous links make use of this.
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --retry int                 Number of retries to do before failing, max 10
      --roles strings             Comma-separated list of roles to filter spaces by the caller's assignment role. For example, "?roles=publisher,facilitator" returns spaces where the caller has the publisher or facilitator role.
                                  Allowed values: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper"
      --sort string               Field to sort by. Prefix with +/- to indicate asc/desc. For example, "?sort=+name" to sort ascending on Name. Supported fields are "type", "name" and "createdAt".
      --type string               Type(s) of space to filter. For example, "?type=managed,shared".
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
