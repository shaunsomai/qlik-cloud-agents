---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection ls

## qlik connectivity data-connection ls

List connections

### Synopsis

Use this operation to retrieve a list of data connections available to the caller. Results are filtered based on the caller's space access permissions. Use the `spaceId`, `personal`, or `filter` parameters to narrow results to a specific scope.

```
qlik connectivity data-connection ls [flags]
```

### Options

```
      --caseinsensitive   When ˋtrueˋ, sorting is applied case-insensitively. Only applies when ˋsortˋ is also specified.
      --dataName string   Provides an alternate name to be used for data[] element in GET response.
      --extended          When ˋtrueˋ, returns an extended set of properties, including the encrypted credential string.
      --filter string     Filter connections by property values using a SCIM filter string. Only filterable properties are supported. Filtering does not apply to datafile connections. Datetime values must be in RFC 3339 format, for example: ˋcreated gt "2000-01-10T15:04:05Z"ˋ.
  -h, --help              help for ls
      --includeDisabled   When ˋtrueˋ, includes connections that use disabled data sources.
      --includeQris       When ˋtrueˋ, includes the encrypted base QRI string in the response. Default is ˋfalseˋ.
      --interval int      Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int         The total number of resources to retrieve.
      --locale string     An ICU locale identifier that controls case-insensitive sort order. Only applies when ˋcaseinsensitiveˋ is ˋtrueˋ. Defaults to ˋenˋ if not specified.
      --noDatafiles       When ˋtrueˋ, datafile connections are excluded from the results.
      --ownedByMe         Filtering on connections, return connections owned by the caller if set to true (doesn't apply to datafiles connections)
      --owner string      Filter data file connections by owner (app) ID.
      --page string       Pagination cursor string, which is generated automatically in previous pagination query.
      --personal          When ˋtrueˋ, returns only personal connections. Ignored if ˋspaceIdˋ is also specified.
  -q, --quiet             Return only IDs from the command
      --raw               Return original response from server without any processing
      --retry int         Number of retries to do before failing, max 10
      --sort string       Field to sort results by. Prefix the field name with ˋ+ˋ for ascending order or ˋ-ˋ for descending order. This parameter is only applicable to paginated requests (e.g. ˋ?limit=30&sort=+qNameˋ) For data connections, sorting only applies to non-datafile connections. Datafile connections are always returned after standard connections, regardless of sort order.
                          Allowed values: "+_id", "-_id", "+qName", "-qName", "+created", "-created", "+updated", "-updated"
      --spaceId string    Filter connections by space ID.
      --userId string     Filter by ˋuserIdˋ. Requires Admin role if specified ˋuserIdˋ doesn't match that is defined in JWT.
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
