---
source: https://qlik.dev/toolkits/qlik-cli/space/space-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# space patch

## qlik space patch

Update a space's properties

### Synopsis

Updates one or more properties of a space. To update all properties at once, use `PUT /spaces/{spaceId}`.

```
qlik space patch <spaceId> [flags]
```

### Options

```
      --body unknowns   (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file       Read request body from the specified file
  -h, --help            help for patch
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string       The operation to be performed.
                        Allowed values: "replace"
      --path string     Field of space to be patched (updated).
                        Allowed values: "/name", "/ownerId", "/description"
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --value string    The value to be used within the operations.
                        - name: The name (string) of space of maxLength 256 of pattern: ^[^\"\*\?\<\>\/\|\\\:]+$
                        - description: The description (string) of the space. Personal spaces do not have a description.
                        - ownerId: The user ID in uid format (string) of the space owner.
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
