---
source: https://qlik.dev/toolkits/qlik-cli/report-template/report-template-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# report-template ls

## qlik report-template ls

Get descriptive info for the specified templates

### Synopsis

Get descriptive info for the specified templates.

```
qlik report-template ls [flags]
```

### Options

```
  -h, --help                 help for ls
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int            The total number of resources to retrieve.
      --name string          Template name to search and filter for. Case-insensitive open search with wildcards both as prefix and suffix.
      --ownerId string       Return the templates for the specified owner.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --skip int             If present, skip this number of the returned values in the result set (facilitates paging).
      --sort strings         Field to sort by. Prefix with +/- to indicate ascending/descending. By default, the sort order is ascending.
                             Allowed values: "name", "+name", "-name", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt", "type", "+type", "-type"
      --sourceAppId string   Return the templates that are using the specified app as data source.
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
