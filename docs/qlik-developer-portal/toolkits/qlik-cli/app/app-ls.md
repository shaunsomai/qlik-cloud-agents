---
source: https://qlik.dev/toolkits/qlik-cli/app/app-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# app ls

## qlik app ls

List the apps the user has access to

### Synopsis

List the apps the user has access to

```
qlik app ls [flags]
```

### Options

```
      --collectionId string         The collection's unique identifier. Used to filter for items with a specific tag (collection type ˋpublicˋ), or collection.
      --createdByUserId string      User's unique identifier.
  -h, --help                        help for ls
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                   The total number of resources to retrieve.
      --name string                 The case-insensitive string used to search for a resource by name.
      --next string                 The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --noActions                   If set to true, the user's available actions for each item will not be evaluated meaning the actions-array will be omitted from the response (reduces response time).
      --notCreatedByUserId string   User's unique identifier.
      --notOwnerId string           Owner identifier.
      --ownerId string              Owner identifier.
      --prev string                 The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
      --query string                The case-insensitive string used to search for a resource by name or description.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --shared                      (Deprecated) Whether or not to return items in a shared space.
      --sort string                 The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, recentlyUsed and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively.
                                    Allowed values: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt", "+recentlyUsed", "-recentlyUsed"
      --spaceId string              The space's unique identifier (supports \'personal\' as spaceId).
      --spaceType string            The case-sensitive string used to filter items on space type(s). For example '?spaceType=shared,personal'.
                                    Allowed values: "shared", "managed", "personal", "data"
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
