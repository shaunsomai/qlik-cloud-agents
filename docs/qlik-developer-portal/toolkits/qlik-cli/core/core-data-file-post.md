---
source: https://qlik.dev/toolkits/qlik-cli/core/core-data-file-post/
last_updated: 2026-06-03T09:30:31+02:00
---

# core data-file post

## qlik core data-file post

Batch upload files or create folders

### Synopsis

Use this operation to perform multiple upload (`POST`) operations on data files and folders
in a single request. The response includes the individual result status for each
specified item.

```
qlik core data-file post [flags]
```

### Options

```
  -f, --file file                               Read request body from the specified file
  -h, --help                                    help for post
      --interval int                            Duration in seconds to wait between retries, at least 1 (default 1)
      --post-request-appId string               If this file should be bound to the lifecycle of a specific app, this is the ID of this app.  If this
                                                request is creating a folder, the specification of an app ID is not allowed.
      --post-request-connectionId string        If present, this is the DataFiles connection that the upload should occur in the context of.  If absent,
                                                the default is that the upload will occur in the context of the Personal Space DataFiles connection.  If the
                                                DataFiles connection is different from the one specified when the file or folder was last POSTed or PUT, this
                                                will result in a logical move of this file or folder into the new space.
      --post-request-folder                     If true, a folder will be created.  If false, a file is created.
      --post-request-folderId string            If the specified file or folder should be moved to become a a sub-item of an existing folder, this is the ID
                                                of this parent folder.  Any additional folder path that is present on the Name property will be created
                                                as a subfolder hierarchy of this folder.  If the FolderID is null, the file or folder specified in the
                                                Name property (including any folder prefix on that name), will be created in the root of the space.
      --post-request-name string                Name that will be given to the file or folder.  It should be noted that the '/' character
                                                in the name indicates a 'path' separator in a logical folder hierarchy for the name.  Names that
                                                contain '/'s should be used with the assumption that a logical 'folder hierarchy' is being defined for the
                                                full pathname of that file or folder.  IE, a '/' is a significant character in the name.
      --post-request-sourceId string            If a SourceId is specified, this is the ID of the existing data file or folder whose content should be copied
                                                into the specified data file or folder.  That is, for a file instead of the file content being specified in
                                                the Data element, it is effectively copied from an existing, previously uploaded file.  For a folder, rather
                                                than the new folder being empty, it's contents are copied from an existing, previously created folder.
      --post-request-tempContentFileId string   If a TempContentFileId is specified, this is the ID of a previously uploaded temporary content file whose
                                                content should be copied into the specified data file.  That is, instead of the file content being specified
                                                in the Data element, it is effectively copied from an existing, previously uploaded file.  The expectation
                                                is that this file was previously uploaded to the temporary content service, and the ID specified here is
                                                the one returned from the temp content upload request.  This option does not apply when POSTing a folder.
  -q, --quiet                                   Return only IDs from the command
      --raw                                     Return original response from server without any processing
      --retry int                               Number of retries to do before failing, max 10
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
