---
source: https://qlik.dev/toolkits/qlik-cli/item/item-collections/
last_updated: 2025-06-18T09:34:47+02:00
---

# item collections

## qlik item collections

List collections of an item

### Synopsis

Finds and returns the collections (and tags) of an item. This endpoint does not return the user's favorites collection.

```
qlik item collections <itemId> [flags]
```

### Options

```
  -h, --help           help for collections
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --name string    The case-sensitive string used to search for a collection by name.
      --next string    The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --prev string    The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
      --query string   The case-insensitive string used to search for a resource by name or description.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --sort string    The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively.
                       Allowed values: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt"
      --type string    The case-sensitive string used to search for a collection by type.
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
