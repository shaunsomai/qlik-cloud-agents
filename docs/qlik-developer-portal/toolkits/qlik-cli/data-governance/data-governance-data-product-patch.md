---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-product-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-product patch

## qlik data-governance data-product patch

Update a data product

### Synopsis

Partially updates an existing data product using JSON Patch operations.
Use this endpoint to modify properties such as name, description, datasets, tags, or key contacts.
Changes are tracked in the data product changelog.

```
qlik data-governance data-product patch <data-productId> [flags]
```

### Options

```
  -f, --file file                     Read request body from the specified file
  -h, --help                          help for patch
      --interval int                  Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                     
                                      Allowed values: "replace"
      --path string                   
                                      Allowed values: "/name", "/description", "/datasetIds", "/glossaryIds", "/readMe", "/keyContacts", "/tags", "/apiConsumableDatasetIds"
  -q, --quiet                         Return only IDs from the command
      --raw                           Return original response from server without any processing
      --retry int                     Number of retries to do before failing, max 10
      --value string|string|unknown   
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
