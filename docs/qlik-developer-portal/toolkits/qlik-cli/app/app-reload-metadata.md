---
source: https://qlik.dev/toolkits/qlik-cli/app/app-reload-metadata/
last_updated: 2026-06-03T09:30:31+02:00
---

# app reload-metadata

## qlik app reload-metadata

Retrieves the app reload metadata list

### Synopsis

Retrieves the app reload metadata list.
Reload metadata contains reload information, including reload id, duration, endtime and lineage load info. Data is available for the last 10 reloads of an application.

```
qlik app reload-metadata <metadataId> [flags]
```

### Options

```
      --appId string              (Required) Identifier of the app
  -h, --help                      help for reload-metadata
      --includeSkipStoreReloads   Include metadata for reloads ran with SkipStore flag set to true. Default: false
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                 Maximum number of records to return from this request. Default: 100
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --reloadId string           Identifier of the reload. Use empty reloadId to get all reloads.
      --retry int                 Number of retries to do before failing, max 10
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
