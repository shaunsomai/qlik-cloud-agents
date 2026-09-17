---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-product-activate/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-governance data-product activate

## qlik data-governance data-product activate

Activate a data product

### Synopsis

Activates a data product for publishing and consumption.
Once activated, the data product becomes discoverable and accessible to authorized users.
Requires publish permissions and valid data product configuration.

```
qlik data-governance data-product activate <data-productId> [flags]
```

### Options

```
      --description string   A description of the data product.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for activate
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          (Required) Name of the data product to activate.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --spaceId string       Unique identifier of the space.
      --tags strings         
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
