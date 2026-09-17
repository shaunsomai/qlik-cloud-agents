---
source: https://qlik.dev/toolkits/qlik-cli/collection/collection-item-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# collection item ls

## qlik collection item ls

List items in a collection

### Synopsis

Retrieves items from a collection that the user has access to.

```
qlik collection item ls [flags]
```

### Options

```
      --collectionId string   (Required) The collection's unique identifier. (This query also supports 'favorites' as the collectionID).
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --name string           The case-insensitive string used to search for a resource by name.
      --next string           The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --noActions             If set to true, the user's available actions for each item will not be evaluated meaning the actions-array will be omitted from the response (reduces response time).
      --prev string           The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
      --query string          The case-insensitive string used to search for a resource by name or description.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --resourceId string     The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceLink string   The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceType string   The case-sensitive string used to search for an item by resourceType.
                              Allowed values: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page"
      --retry int             Number of retries to do before failing, max 10
      --shared                (Deprecated) Whether or not to return items in a shared space.
      --sort string           The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively.
                              Allowed values: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt"
      --spaceId string        The space's unique identifier (supports \'personal\' as spaceId).
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
