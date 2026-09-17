---
source: https://qlik.dev/toolkits/qlik-cli/item/item-publisheditems/
last_updated: 2026-06-03T09:30:31+02:00
---

# item publisheditems

## qlik item publisheditems

List published items

### Synopsis

Finds and returns the published items for a given item. This endpoint is particularly useful for finding the published copies of an app or a qvapp when you want to replace the content of a published copy with new information from the source item.

```
qlik item publisheditems <itemId> [flags]
```

### Options

```
  -h, --help                  help for publisheditems
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --next string           The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --prev string           The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --resourceType string   The case-sensitive string used to search for an item by resourceType.
                              Allowed values: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page"
      --retry int             Number of retries to do before failing, max 10
      --sort string           The property of a resource to sort on (default sort is +createdAt). The supported properties are createdAt, updatedAt, and name. A property must be prefixed by + or   - to indicate ascending or descending sort order respectively.
                              Allowed values: "+createdAt", "-createdAt", "+name", "-name", "+updatedAt", "-updatedAt"
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
