---
source: https://qlik.dev/toolkits/qlik-cli/space/space-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# space update

## qlik space update

Update a space

### Synopsis

Updates a space. To update specific properties, use `PATCH /spaces/{spaceId}`.

```
qlik space update <spaceId> [flags]
```

### Options

```
      --description string   The description of the space. Personal spaces do not have a description.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for update
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          The name of the space.
      --ownerId string       The user ID of the space owner.
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
