---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-change-owner/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file change-owner

## qlik core data-file change-owner

Change data file or folder owner

### Synopsis

Use this operation to transfer ownership of a data file or folder to a different user.
When the item is in a personal space, changing the owner moves it to the new owner's
personal space. The item must be in the root of its current space for this operation to
succeed. Items nested inside subfolders cannot be moved this way. Changing the owner
of a root-level folder also recursively updates the owner for all files and subfolders
within it.

```
qlik core data-file change-owner <data-fileId> [flags]
```

### Options

```
  -f, --file file        Read request body from the specified file
  -h, --help             help for change-owner
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
      --ownerId string   (Required) The ID of the new owner.
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
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
