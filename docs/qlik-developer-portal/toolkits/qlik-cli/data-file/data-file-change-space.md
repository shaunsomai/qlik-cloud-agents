---
source: https://qlik.dev/toolkits/qlik-cli/data-file/data-file-change-space/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-file change-space

## qlik data-file change-space

Change the space that an existing data file or folder resides in

### Synopsis

This is to allow for a separate admin type of operation that is more global in terms of access in cases
where admin users may not explicitly have been granted full access to a given space within the declared
space-level permissions.  If the space ID is set to null, then the datafile or folder will end up residing
in the personal space of the user who is the owner of the item.  Note that, if a given file or folder is not
in the root of a given space, this operation will not succeed, since the parent folder does not reside in
the target space.  If the space of a folder in the root of the source space is changed, all subfolders and
files within those subfolders will also recursively be moved to the new space.

```
qlik data-file change-space <data-fileId> [flags]
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
