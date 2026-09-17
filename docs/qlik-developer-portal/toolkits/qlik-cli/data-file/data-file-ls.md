---
source: https://qlik.dev/toolkits/qlik-cli/data-file/data-file-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-file ls

## qlik data-file ls

Get descriptive info for the specified data files

### Synopsis

Get descriptive info for the specified data files.

```
qlik data-file ls [flags]
```

### Options

```
      --allowInternalFiles        If set to false, do not return data files with internal extensions else return all the data files.
      --appId string              Only return files scoped to the specified app.  If this parameter is not specified, only files that are not
                                  scoped to any app are returned.  "*" implies all app-scoped files are returned.
      --baseNameWildcard string   If present, return only items whose base name matches the given wildcard.  Wildcards include '*' and '?'
                                  characters to allow for multiple matches.  The base name is the actual file or folder name without any
                                  folder pathing included.
      --connectionId string       Return files and folders that reside in the space referenced by the specified DataFiles connection.  If this
                                  parameter is not specified, the user's personal space is implied.
      --excludeFiles              If set to true, exclude files in the returned list (IE, only return folders).  If false, include files.
      --excludeSubFolders         If set to true, exclude folders and files that reside in sub-folders of the root being searched.  If false,
                                  include all items in full folder hierarchy that recursively reside under the root.  That is, setting to
                                  true results in only the direct children of the root being returned.
      --folderId string           If present, return only items which reside under the folder specified by the given ID.  If not present,
                                  items that live at the root of the space are returned.  This property is mutually exclusive with 'folderPath'.
      --folderPath string         If present, return only items which reside under the specified folder path.  If not present, items that
                                  live at the root of the space are returned.  This property is mutually exclusive with 'folderId'.
  -h, --help                      help for ls
      --includeAllSpaces          If set to true, and connectionId is not specified, return files and folders from all spaces the given user
                                  has access to (including the personal space).  If connectionId is specified, this parameter is ignored.
      --includeFolderStats        If set to true, include computed folder statistics for folders in the returned list.  If false, this information
                                  is not returned.
      --includeFolders            If set to true, include folders in the returned list.  If false, only return data files.
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                 The total number of resources to retrieve.
      --name string               Filter the list of files returned to the given file name.
      --notOwnerId string         If present, fetch the data files whose owner is not the specified owner.  If a connectionId is specified in
                                  this case, the returned list is constrained to the specified space.  If connectionId is not specified, then
                                  the returned list is constrained to the calling user's personal space.  If includeAllSpaces is set to true,
                                  and connectionId is not specified, the returned list is from all spaces the given user
                                  has access to (including the personal space).
      --ownerId string            If present, fetch the data files for the specified owner.  If a connectionId is specified in this case, the
                                  returned list is constrained to the specified space.  If connectionId is not specified, then all files owned
                                  by the specified user are returned regardless of the personal space that a given file resides in.
      --page string               If present, the cursor that starts the page of data that is returned.
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --retry int                 Number of retries to do before failing, max 10
      --sort string               The name of the field used to sort the result.  By default, the sort order is ascending.  Putting a '+' prefix on
                                  the sort field name explicitly indicates ascending sort order.  A '-' prefix indicates a descending sort order.
                                  Allowed values: "name", "+name", "-name", "size", "+size", "-size", "modifiedDate", "+modifiedDate", "-modifiedDate", "folder", "+folder", "-folder", "baseName", "+baseName", "-baseName"
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
