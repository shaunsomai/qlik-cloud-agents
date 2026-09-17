---
source: https://qlik.dev/toolkits/qlik-cli/app/app-media-thumbnail/
last_updated: 2025-06-18T09:34:47+02:00
---

# app media thumbnail

## qlik app media thumbnail

Gets media content from file currently used as application thumbnail

### Synopsis

Gets media content from file currently used as application thumbnail.
Returns a stream of bytes containing the media file content on success, or error if file is not found.
The image selected as thumbnail is only updated when application is saved.

```
qlik app media thumbnail [flags]
```

### Options

```
      --appId string         (Required) Unique application identifier.
  -h, --help                 help for thumbnail
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --output-file string   Filepath specifying where to write the response body.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
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
