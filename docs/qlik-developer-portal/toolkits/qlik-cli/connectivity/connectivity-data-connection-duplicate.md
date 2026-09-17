---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-connection-duplicate/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-connection duplicate

## qlik connectivity data-connection duplicate

Duplicate a connection

### Synopsis

Use this operation to create a copy of an existing data connection. The duplicated connection can optionally be placed in a different space by specifying `spaceId`. You can override the credentials in the duplicate by providing `qUsername` and `qPassword` in the request body.

```
qlik connectivity data-connection duplicate [flags]
```

### Options

```
  -f, --file file          Read request body from the specified file
  -h, --help               help for duplicate
      --id string          (Required) ID of the source connection being duplicated
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
      --name string        Optional name for the duplicated connection, must be unique in the target scope. If not specified, a name will be automatically generated
      --qPassword string   Optional credential password, specify to override credential embedded (or associated) with the source connection
      --qUsername string   Optional credential username, specify to override credential embedded (or associated) with the source connection
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
      --spaceId string     Optional target space ID for the duplicated connection. If not specified, the duplicated connection will be in the same space as the source connection
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
