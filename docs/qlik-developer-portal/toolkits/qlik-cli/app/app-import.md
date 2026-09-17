---
source: https://qlik.dev/toolkits/qlik-cli/app/app-import/
last_updated: 2025-06-18T09:34:47+02:00
---

# app import

## qlik app import

Imports an app into the system

### Synopsis

Imports an app into the system.

```
qlik app import [flags]
```

### Options

```
      --NoData                If NoData is true, the data of the existing app will be kept as is, otherwise it will be replaced by the new incoming data.
      --appId string          The app ID of the target app when source is qvw file.
      --fallbackName string   The name of the target app when source does not have a specified name, applicable if source is qvw file.
      --file file             
      --fileId string         The file ID to be downloaded from Temporary Content Service (TCS) and used during import.
  -h, --help                  help for import
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --mode string           The import mode. In ˋnewˋ mode (default), the source app will be imported as a new app.
                              
                              One of:
                              * NEW
                              * AUTOREPLACE
                              Note: The ˋautoreplaceˋ mode is an internal mode only and is not permitted for external use.
      --name string           The name of the target app.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --resumable             Make a resumable request, recommended for large payloads.
                              The request is split into chunks and if the request is interrupted, it can be resumed by repeating the same command.
                              Note: Only works with files, not piped input.
      --retry int             Number of retries to do before failing, max 10
      --spaceId string        The space ID of the target app.
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
