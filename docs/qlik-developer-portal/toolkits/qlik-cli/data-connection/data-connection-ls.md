---
source: https://qlik.dev/toolkits/qlik-cli/data-connection/data-connection-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-connection ls

## qlik data-connection ls

Gets a list of connections

### Synopsis

Gets a list of connections

```
qlik data-connection ls [flags]
```

### Options

```
      --caseinsensitive   Sort results will be returned in case insensitive order if set to true (Only used along with sort query)
      --dataName string   Provides an alternate name to be used for data[] element in GET response.
      --extended          Returns extended list of properties (e.g. encrypted credential string) when set to true.
      --filter string     Filtering resources by properties (filterable properties only) using SCIM filter string. Note the filter string only applies to connections managed by data-connections service, i.e. filtering doesn't apply to DataFile connections. When filtering on datetime property (e.g. created, updated), datetime should be in RFC3339 format.
  -h, --help              help for ls
      --includeDisabled   Includes connections that uses disabled datasources
      --includeQris       Base Qri (encrypted) will be returned when the query is set to true, default is false
      --interval int      Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int         The total number of resources to retrieve.
      --locale string     ICU locale ID, used only when caseinsensitive is set to true, default to 'en' if undefined
      --noDatafiles       Datafiles connections will not be returned if set to true
      --ownedByMe         Filtering on connections, return connections owned by the caller if set to true (doesn't apply to datafiles connections)
      --owner string      Filtering on datafile connections by owner (i.e. app) ID.
      --page string       Pagination cursor string, which is generated automatically in previous pagination query.
      --personal          Filtering on personal connections, ignored if spaceId is defined in same request
  -q, --quiet             Return only IDs from the command
      --raw               Return original response from server without any processing
      --retry int         Number of retries to do before failing, max 10
      --sort string       Field to sort results by. Prefix the field name with ˋ+ˋ for ascending order or ˋ-ˋ for descending order. This parameter is only applicable to paginated requests (e.g. ˋ?limit=30&sort=+qNameˋ) For data connections, sorting only applies to non-datafile connections. Datafile connections are always returned after standard connections, regardless of sort order.
      --spaceId string    Filtering on connections by space ID
      --userId string     Filtering on userId. Requires admin role if specified userId doesn't match that is defined in JWT.
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
