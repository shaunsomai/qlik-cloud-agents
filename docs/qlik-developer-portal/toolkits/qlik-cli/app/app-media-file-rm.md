---
source: https://qlik.dev/toolkits/qlik-cli/app/app-media-file-rm/
last_updated: 2025-06-18T09:34:47+02:00
---

# app media file rm

## qlik app media file rm

Deletes a media content file or complete directory

### Synopsis

Deletes a media content file or complete directory.
Returns OK if the bytes containing the media file (or the complete content of a directory) were successfully deleted, or error in case of failure or lack of permission.

```
qlik app media file rm <path> [flags]
```

### Options

```
      --appId string   (Required) Unique application identifier.
  -h, --help           help for rm
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
