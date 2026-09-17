---
source: https://qlik.dev/toolkits/qlik-cli/web-integration/web-integration-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# web-integration ls

## qlik web-integration ls

List web integrations

### Synopsis

Retrieves web integrations matching the query.

```
qlik web-integration ls [flags]
```

### Options

```
      --endingBefore string    The target web integration ID to start looking before for web integrations. Cannot be used in conjunction with startingAfter.
  -h, --help                   help for ls
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int              The total number of resources to retrieve.
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --retry int              Number of retries to do before failing, max 10
      --sort string            The field to sort by. Prefix with +/- to indicate ascending/descending order.
                               Allowed values: "name", "+name", "-name"
      --startingAfter string   The target web integration ID to start looking after for web integrations. Cannot be used in conjunction with endingBefore.
      --tenantId string        The tenant ID to filter by.
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
