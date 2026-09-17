---
source: https://qlik.dev/toolkits/qlik-cli/item/item-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# item ls

## qlik item ls

List items

### Synopsis

Lists items that the user has access to.

```
qlik item ls [flags]
```

### Options

```
      --collectionId string         The collection's unique identifier. Used to filter for items with a specific tag (collection type ˋpublicˋ), or collection.
      --createdByUserId string      User's unique identifier.
  -h, --help                        help for ls
      --id string                   The item's unique identifier.
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
      --resourceId string           The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceIds string          The case-sensitive strings used to search for an item by resourceIds. The maximum number of resourceIds it supports is 100. If resourceIds is provided, then resourceType must be provided. For example '?resourceIds=appId1,appId2'
      --resourceLink string         The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceSubType string      the case-sensitive string used to filter items by resourceSubType(s). For example '?resourceSubType=chart-monitoring,qix-df,qvd'. Will return a 400 error if used in conjuction with the square bracket syntax for resourceSubType filtering in the 'resourceType' query parameter.
      --resourceType string         The case-sensitive string used to filter items by resourceType(s). For example '?resourceType=app,qvapp'. Additionally, a optional resourceSubType filter can be added to each resourceType. For example '?resourceType=app[qvd,chart-monitoring],qvapp'. An trailing comma can be used to include the empty resourceSubType, e.g. '?resourceType=app[qvd,chart-monitoring,]', or, to include only empty resourceSubTypes, '?resourceType=app[]' This syntax replaces the 'resourceSubType' query param, and using both in the same query will result in a 400 error.
                                    Allowed values: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page"
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
