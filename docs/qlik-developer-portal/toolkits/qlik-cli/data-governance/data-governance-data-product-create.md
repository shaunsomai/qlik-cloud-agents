---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-product-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-product create

## qlik data-governance data-product create

Create a data product

### Synopsis

Creates a new data product with specified metadata, datasets, and governance information.
Use this endpoint to package related datasets into a governed, discoverable asset.
Requires create permissions in the target space.

```
qlik data-governance data-product create [flags]
```

### Options

```
      --apiConsumableDatasetIds strings   List of dataset IDs for which API consumption is enabled. Must be a subset of datasetIds.
      --datasetIds strings                List of dataset IDs associated with the Data Product. Maximum of 100 items.
      --description string                A description of the Data Product.
  -f, --file file                         Read request body from the specified file
      --glossaryIds strings               List of glossary IDs linked to the Data Product. Each entry must be a valid UUIDv4 (maximum 36 characters). Maximum of 100 items.
  -h, --help                              help for create
      --interval int                      Duration in seconds to wait between retries, at least 1 (default 1)
      --keyContacts-role string           Role of the key contact in the Data Product.
      --keyContacts-userId string         Unique identifier of the user.
      --name string                       (Required) Display name of the data product.
  -q, --quiet                             Return only IDs from the command
      --raw                               Return original response from server without any processing
      --readMe string                     A readme of the Data Product.
      --retry int                         Number of retries to do before failing, max 10
      --spaceId string                    Unique identifier of the space.
      --tags strings                      List of tags for the data product.
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
