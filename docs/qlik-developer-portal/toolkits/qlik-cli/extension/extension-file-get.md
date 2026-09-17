---
source: https://qlik.dev/toolkits/qlik-cli/extension/extension-file-get/
last_updated: 2025-06-18T09:34:47+02:00
---

# extension file get

## qlik extension file get

Download file from extension archive

### Synopsis

Downloads a specific file from the extension matching either extension ID or extension name, identified by the file path within the imported extension.

```
qlik extension file get <filepath> [flags]
```

### Options

```
      --extensionId string   (Required) Extension identifier or its qextFilename.
  -h, --help                 help for get
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
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
