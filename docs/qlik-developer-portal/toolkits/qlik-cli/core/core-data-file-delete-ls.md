---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-delete-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file delete ls

## qlik core data-file delete ls

List deleted data files

### Synopsis

Use this operation to retrieve records of data files and folders deleted within a given
time range, across all spaces in the tenant. Use `deleteStartDate` and `deleteEndDate`
to constrain the results to a specific window. This operation requires elevated
service-to-service privileges.

```
qlik core data-file delete ls [flags]
```

### Options

```
      --allowInternalFiles       If set to false, do not return data files with internal extensions else return all the data files.
      --deleteEndDate string     If specified, the returned list will only include data files and folders that have been deleted prior to the
                                 specified date (inclusive).
      --deleteStartDate string   If specified, the returned list will only include data files and folders that have been deleted since the
                                 specified date (inclusive).
  -h, --help                     help for ls
      --includeFolders           If set to true, include deleted folders in the result.  If false, only return data files.
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                The total number of resources to retrieve.
      --page string              If present, the cursor that starts the page of data that is returned.
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
      --sort string              The name of the field used to sort the result.  By default, the sort order is ascending.  Putting a '+' prefix on
                                 the sort field name explicitly indicates ascending sort order.  A '-' prefix indicates a descending sort order.
                                 Allowed values: "deletedDate", "+deletedDate", "-deletedDate"
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
