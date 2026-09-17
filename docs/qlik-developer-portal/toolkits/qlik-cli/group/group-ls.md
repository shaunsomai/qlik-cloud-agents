---
source: https://qlik.dev/toolkits/qlik-cli/group/group-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# group ls

## qlik group ls

List groups

### Synopsis

Returns a list of groups with cursor-based pagination.

```
qlik group ls [flags]
```

### Options

```
      --filter string   The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive.
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --next string     The next page cursor.
      --prev string     The previous page cursor.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending.
      --systemGroups    Return system groups (e.g. Everyone) instead of regular groups. Cannot be combined with any other query parameters.
      --totalResults    Whether to return a total match count in the result. Defaults to false.
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
