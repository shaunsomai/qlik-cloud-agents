---
source: https://qlik.dev/toolkits/qlik-cli/app/app-object-change-owner/
last_updated: 2025-06-18T09:34:47+02:00
---

# app object change-owner

## qlik app object change-owner

Sets owner on an app object

### Synopsis

Sets owner on an app object.
The user must be the owner of the object.

```
qlik app object change-owner [flags]
```

### Options

```
      --appId string      (Required) Identifier of the app.
  -f, --file file         Read request body from the specified file
  -h, --help              help for change-owner
      --interval int      Duration in seconds to wait between retries, at least 1 (default 1)
      --objectId string   (Required) Identifier of the object.
      --ownerId string    
  -q, --quiet             Return only IDs from the command
      --raw               Return original response from server without any processing
      --retry int         Number of retries to do before failing, max 10
```

### Options inherited from parent commands

```
  -a, --app string               Name or identifier of the app
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
      --no-data                  Open app without data
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -t, --traffic                  Log JSON websocket traffic to stderr
      --ttl string               The Engine session's time to live in seconds (default "0")
  -v, --verbose                  Log extra information
```
