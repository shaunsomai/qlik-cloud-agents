---
source: https://qlik.dev/toolkits/qlik-cli/user/user-filter/
last_updated: 2025-06-18T09:34:47+02:00
---

# user filter

## qlik user filter

Filter users

### Synopsis

Retrieves a list of users matching the filter using an advanced query string.

```
qlik user filter [flags]
```

### Options

```
      --fields string   A comma-delimited string of the requested fields per entity. If the 'links' value is omitted, then the entity HATEOAS link will also be omitted.
  -f, --file file       Read request body from the specified file
      --filter string   The advanced filtering to be applied the query. All conditional statements within this query parameter are case insensitive.
  -h, --help            help for filter
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The number of user entries to retrieve.
      --next string     Get users with IDs that are higher than the target user ID. Cannot be used in conjunction with prev.
      --prev string     Get users with IDs that are lower than the target user ID. Cannot be used in conjunction with next.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort by, with +/- prefix indicating sort order
                        Allowed values: "name", "+name", "-name"
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
