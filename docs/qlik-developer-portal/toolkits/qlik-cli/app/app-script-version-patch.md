---
source: https://qlik.dev/toolkits/qlik-cli/app/app-script-version-patch/
last_updated: 2025-06-18T09:34:47+02:00
---

# app script version patch

## qlik app script version patch

Updates a specific version of the script for an app

### Synopsis

Updates a specific version of the script for an app.

```
qlik app script version patch <scriptId> [flags]
```

### Options

```
      --appId string    (Required) Identifier of the app.
      --body unknowns   (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file       Read request body from the specified file
  -h, --help            help for patch
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string       
                        Allowed values: "add", "remove", "replace"
      --path string     Path to the property to add, remove or replace.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --value string    This parameter is not used in a remove operation.
                        Corresponds to the value of the property to add or to the new value of the property to update.
                        Examples:
                        "false", "2", "\"New title\""
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
