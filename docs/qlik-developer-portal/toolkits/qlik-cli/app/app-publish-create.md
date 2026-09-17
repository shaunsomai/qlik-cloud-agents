---
source: https://qlik.dev/toolkits/qlik-cli/app/app-publish-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# app publish create

## qlik app publish create

Publishes a specific app to a managed space

### Synopsis

Publishes a specific app to a managed space.

```
qlik app publish create <appId> [flags]
```

### Options

```
      --attributes-description string   The description of the application.
      --attributes-name string          The name (title) of the application.
      --data string                     
                                        Allowed values: "source", "target"
  -f, --file file                       Read request body from the specified file
  -h, --help                            help for create
      --interval int                    Duration in seconds to wait between retries, at least 1 (default 1)
      --moveApp                         The original is moved instead of copied. The current published state of all objects is kept.
      --originAppId string              If app is moved, originAppId needs to be provided.
  -q, --quiet                           Return only IDs from the command
      --raw                             Return original response from server without any processing
      --retry int                       Number of retries to do before failing, max 10
      --spaceId string                  The managed space ID where the app will be published.
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
