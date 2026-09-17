---
source: https://qlik.dev/toolkits/qlik-cli/collection/collection-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# collection ls

## qlik collection ls

List collections

### Synopsis

Retrieves the collections that the user has access to. This endpoint does not return the user's favorites collection, which can be retrieved with `/v1/collections/favorites`.

```
qlik collection ls [flags]
```

### Options

```
      --creatorId string      The case-sensitive string used to search for a resource by creatorId.
  -h, --help                  help for ls
      --id string             The collection's unique identifier.
      --includeItems string   Includes the list of items belonging to the collections. Supported parameters are 'limit', 'sort' and 'resourceType'. Supported formats are json formatted string or deep object style using square brackets.
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --name string           The case-sensitive string used to search for a collection by name.
      --next string           The cursor to the next page of resources. Provide either the
                              next or prev cursor, but not both.
      --prev string           The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
      --query string          The case-insensitive string used to search for a resource by name or description.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort string           The property of a resource to sort on (default sort is +createdAt).
                              The supported properties are createdAt, updatedAt, and name. A property
                              must be prefixed by + or - to indicate ascending or descending sort order
                              respectively.
                              Allowed values: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt"
      --type string           The case-sensitive string used to filter for a collection by type. Retrieve private collections with ˋprivateˋ, public collections with ˋpublicgovernedˋ, and tags with ˋpublicˋ.
                              Allowed values: "private", "public", "publicgoverned"
      --types strings         A comma-separated case-sensitive string used to filter by multiple types.
                              Allowed values: "private", "public", "publicgoverned"
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
