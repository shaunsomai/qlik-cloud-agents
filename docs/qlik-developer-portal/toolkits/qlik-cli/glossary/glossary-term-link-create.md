---
source: https://qlik.dev/toolkits/qlik-cli/glossary/glossary-term-link-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# glossary term link create

## qlik glossary term link create

Creates a new link to a term

### Synopsis

Links to resources are not considered term properties but external relations. Links can be created for terms in any status. Permissions on term and resource determine if the link can be created.

```
qlik glossary term link create [flags]
```

### Options

```
  -f, --file file                Read request body from the specified file
      --glossaryId string        (Required) The glossary id.
  -h, --help                     help for create
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --resourceId string        (Required) The unique identifier of the resource (app or dataset) to link to the term.
      --resourceType string      (Required) The type of resource being linked to the term.
                                 Allowed values: "app", "dataset"
      --retry int                Number of retries to do before failing, max 10
      --subResourceId string     Required when subResourceType or subResourceName is provided. The unique identifier of the subresource.
      --subResourceName string   Required when subResourceType or subResourceId is provided. The display name of the subresource.
      --subResourceType string   Required when subResourceId or subResourceName is provided. The type of the subresource.
                                 Allowed values: "master_dimension", "master_measure", "field"
      --termId string            (Required) The term id.
      --type string              The type of relationship between the term and the linked resource:
                                 - ˋdefinitionˋ: Use when the term provides the formal definition for the linked resource (e.g., a term defines what a master measure or dimension means)
                                 - ˋrelatedˋ: Use when the term is generally related to the resource but doesn't formally define it
                                 Allowed values: "definition", "related"
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
