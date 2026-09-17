---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-change-space/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file change-space

## qlik core data-file change-space

Change data file or folder space

### Synopsis

Use this operation to move a data file or folder to a different space. Set `spaceId` to
`null` to move the item to the personal space of its owner. The item must be in the root
of its current space for this operation to succeed. Moving a root-level folder also
recursively moves all files and subfolders within it to the new space. This is an
administrative operation that bypasses explicit space-level permission requirements.

```
qlik core data-file change-space <data-fileId> [flags]
```

### Options

```
  -f, --file file        Read request body from the specified file
  -h, --help             help for change-space
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --spaceId string   The ID of the space.  If null, this data file will be moved to the user's personal space.
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
