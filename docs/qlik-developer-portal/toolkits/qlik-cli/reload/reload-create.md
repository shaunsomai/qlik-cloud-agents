---
source: https://qlik.dev/toolkits/qlik-cli/reload/reload-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# reload create

## qlik reload create

Reload an app

### Synopsis

Reloads an app specified by an app ID.

```
qlik reload create [flags]
```

### Options

```
      --appId string           (Required) The ID of the app to be reloaded.
  -f, --file file              Read request body from the specified file
  -h, --help                   help for create
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
      --partial                The boolean value used to present the reload is partial or not
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --retry int              Number of retries to do before failing, max 10
      --variables key:string   The variables to be used in the load script. Maximum of 20 variables allowed with a maximum length of 256 characters for each name/value.
      --weight int             The weight of the reload for the same tenant. The higher the weight, the sooner the reload will be scheduled relative to other reloads for the same tenant. The personal app will be always set as 1.
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
