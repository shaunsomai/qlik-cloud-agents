---
source: https://qlik.dev/toolkits/qlik-cli/data-file/data-file-change-owner/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-file change-owner

## qlik data-file change-owner

Change the owner of an existing data file or folder

### Synopsis

This is primarily an admin type of operation.  In general, the owner of a data file or folder is implicitly
set as part of a create or update operation.  For data files or folders that reside in a personal space,
changing the owner has the effect of moving the data file to the new owner's personal space.  Note that,
If a given file or folder is not in the root of a personal space, this operation will not succeed, since
the parent folder does not reside in the target owner's personal space.  If the owner of a folder in the
root of a personal space is changed, the owner of all subfolders and files within those subfolders will
also recursively change.

```
qlik data-file change-owner <data-fileId> [flags]
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
