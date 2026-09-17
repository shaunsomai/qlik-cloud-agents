---
source: https://qlik.dev/toolkits/qlik-cli/app/app-media-list-get/
last_updated: 2025-06-18T09:34:47+02:00
---

# app media list get

## qlik app media list get

Lists media content

### Synopsis

Lists media content.
Returns a JSON formatted array of strings describing the available media content or error if the optional path supplied is not found.

```
qlik app media list get <path> [flags]
```

### Options

```
      --appId string   (Required) Unique application identifier.
  -h, --help           help for get
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --show string    Optional. List output can include files and folders in different ways:
                       * Not recursive, default if show option is not supplied or incorrectly specified, results in output with files and empty directories for the path specified only.
                       * Recursive(r), use ?show=r or ?show=recursive, results in a recursive output with files, all empty folders are excluded.
                       * All(a), use ?show=a or ?show=all, results in a recursive output with files and empty directories.
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
