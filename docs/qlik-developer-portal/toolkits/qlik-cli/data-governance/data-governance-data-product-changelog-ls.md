---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-product-changelog-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-product changelog ls

## qlik data-governance data-product changelog ls

Get data product changelogs

### Synopsis

Retrieves a paginated history of all notable changes made to a data product.
Each changelog entry captures the operation type, affected property, and timestamp.
Use this endpoint to track the history of changes or data product evolution over time.

```
qlik data-governance data-product changelog ls <data-productId> [flags]
```

### Options

```
  -h, --help           help for ls
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --page int       Page number.
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --sort string    Sort order for changelog entries. Use ˋ+createdAtˋ for oldest first or ˋ-createdAtˋ for newest first.
                       Prefix with ˋ+ˋ for ascending or ˋ-ˋ for descending order. Default: -createdAt.
                       Allowed values: "+createdAt", "-createdAt"
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
