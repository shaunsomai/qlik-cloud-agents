---
source: https://qlik.dev/toolkits/qlik-cli/app/app-script-version-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# app script version ls

## qlik app script version ls

Retrieves the script history for an app

### Synopsis

Retrieves the script history for an app.
Returns information about the saved versions of the script in a list sorted with latest first.

```
qlik app script version ls [flags]
```

### Options

```
      --appId string    (Required) Identifier of the app.
      --filter string   A scim filter expression defining which script versions should be retrieved. Filterable fields are:
                        * ScriptId
                        * ModifiedTime
                        * ModifierId
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       Maximum number of records to return from this request.
      --page string     Opaque definition of which page of the result set to return. Returned from a previous call using the same filter. Not yet supported.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
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
