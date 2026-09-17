---
source: https://qlik.dev/toolkits/qlik-cli/space/space-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# space create

## qlik space create

Create a space

### Synopsis

Creates a space. Spaces names must be unique. Spaces of type `data` should only be used for Qlik Talend Data Integration projects.

```
qlik space create [flags]
```

### Options

```
      --description string   The description of the space. Personal spaces do not have a description.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for create
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          (Required) The name of the space. Personal spaces do not have a name.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --type string          (Required) The type of space such as shared, managed, and so on.
                             Allowed values: "shared", "managed", "data"
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
