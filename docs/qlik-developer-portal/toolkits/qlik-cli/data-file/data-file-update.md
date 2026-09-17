---
source: https://qlik.dev/toolkits/qlik-cli/data-file/data-file-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-file update

## qlik data-file update

Re-upload an existing data file or update an existing folder

### Synopsis

Re-upload an existing data file or update an existing folder.

```
qlik data-file update <data-fileId> [flags]
```

### Options

```
      --appId string                 If this file should be bound to the lifecycle of a specific app, this is the ID of this app.  If this
                                     request is creating a folder, the specification of an app ID is not allowed.
      --connectionId string          If present, this is the DataFiles connection points to the space that the file or folder should reside in.
                                     If absent, the default is that the file or folder will reside in the Personal SPce.  If the DataFiles
                                     connection is different from the one specified when the file or folder was last POSTed or PUT, this will
                                     result in a logical move of this file or folder into the new space.
      --file file                    IFormFile form multipart/form-data
      --folderId string              If the specified file or folder should be created as a sub-item of an existing folder, this is the ID
                                     of this parent folder.  Any additional folder path that is present on the Name property will be created
                                     as a subfolder hierarchy of this folder.  If the FolderID is null, the file or folder specified in the
                                     Name property (including any folder prefix on that name), will be created in the root of the space.
      --folderMergeBehavior string   If a SourceId is specified, and a folder is being updated by this PUT operation, this specifies how the
                                     source folder contents should be applied to the target folder, if the target folder is not empty.  'merge'
                                     implies the contents of the source folder should be merged with the existing target contents.  That is, all
                                     existing direct or indirect child items in the target folder are replaced by the same items in the source folder.
                                     All existing items in the target folder that are not present in the source folder are left, as is, in the target.
                                     'replace' implies the contents of the source folder should replace the contents of the target folder.  That is,
                                     all direct or indirect items in the target folder are removed before the items from the source folder are copied
                                     over.  The resulting target folder only contains the items from the source folder.  If not specified, the default
                                     behavior is 'merge'.<p>Members:</p><ul></ul>
                                     Allowed values: "merge", "replace"
  -h, --help                         help for update
      --interval int                 Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                  Name that will be given to the file or folder.  If this name is different than the name used when the file
                                     or folder was last POSTed or PUT, this will result in a rename of the file or folder.  It should be noted
                                     that the '/' character in a data file name indicates a 'path' separator in a logical folder hierarchy for
                                     the name.  Names that contain '/'s should be used with the assumption that a logical 'folder hierarchy' is
                                     being defined for the full pathname of that file or folder..  '/' is a significant character in the data file
                                     or folder name.
  -q, --quiet                        Return only IDs from the command
      --raw                          Return original response from server without any processing
      --resumable                    Make a resumable request, recommended for large payloads.
                                     The request is split into chunks and if the request is interrupted, it can be resumed by repeating the same command.
                                     Note: Only works with files, not piped input.
      --retry int                    Number of retries to do before failing, max 10
      --sourceId string              If a SourceId is specified, this is the ID of the existing data file or folder whose content should be copied
                                     into the specified data file or folder.  That is, for a file instead of the file content being specified in
                                     the Data element, it is effectively copied from an existing, previously uploaded file.  For a folder, it's
                                     contents are copied from an existing, previously created folder.  If there it existing content in the target
                                     folder, then how the source and target folder contents are merged together is specified in the
                                     FolderMergeBehavior option.
      --tempContentFileId string     If a TempContentFileId is specified, this is the ID of a previously uploaded temporary content file whose
                                     content should be copied into the specified data file.  That is, instead of the file content being specified
                                     in the Data element, it is effectively copied from an existing, previously uploaded file.  The expectation
                                     is that this file was previously uploaded to the temporary content service, and the ID specified here is
                                     the one returned from the temp content upload request.
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
