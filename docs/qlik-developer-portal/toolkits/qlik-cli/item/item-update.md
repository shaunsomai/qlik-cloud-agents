---
source: https://qlik.dev/toolkits/qlik-cli/item/item-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# item update

## qlik item update

Update an item

### Synopsis

Updates an item. Omitted and unsupported fields are ignored. To unset a field, provide the field's zero value.

```
qlik item update <itemId> [flags]
```

### Options

```
      --description string                 
  -f, --file file                          Read request body from the specified file
  -h, --help                               help for update
      --interval int                       Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                        
  -q, --quiet                              Return only IDs from the command
      --raw                                Return original response from server without any processing
      --resourceAttributes unknown         
      --resourceCustomAttributes unknown   
      --resourceId string                  The case-sensitive string used to search for an item by resourceId. If resourceId is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceLink string                The case-sensitive string used to search for an item by resourceLink. If resourceLink is provided, then resourceType must be provided. Provide either the resourceId or resourceLink, but not both.
      --resourceSubType string             Optional field defining the item's subtype, if any.
      --resourceType string                (Required) The case-sensitive string defining the item's type.
                                           Allowed values: "app", "qlikview", "qvapp", "genericlink", "sharingservicetask", "note", "dataasset", "dataset", "automation", "automl-experiment", "automl-deployment", "assistant", "dataproduct", "dataqualityrule", "glossary", "knowledgebase", "script", "semantictype", "page"
      --resourceUpdatedAt string           The RFC3339 datetime when the resource that the item references was last updated.
      --retry int                          Number of retries to do before failing, max 10
      --spaceId string                     The space's unique identifier.
      --thumbnailId string                 The item thumbnail's unique identifier. This is optional for internal resources.
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
