---
source: https://qlik.dev/toolkits/qlik-cli/collection/collection-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# collection patch

## qlik collection patch

Update collection

### Synopsis

Updates the name, description, or type fields provided in the patch body. Can be used to publish a `private` collection as a `publicgoverned` collection by patching `/type` with `publicgoverned` once the collection contains at least 1 item. Can also be used to return a `publicgoverned` collection to `private`. Cannot be used to change between `public` (tag) and `private / publicgoverned` (collection).

```
qlik collection patch <collectionId> [flags]
```

### Options

```
      --body unknowns   (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file       Read request body from the specified file
  -h, --help            help for patch
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string       The operation to be performed.
                        Allowed values: "replace"
      --path string     Field of collection to be patched.
                        Allowed values: "/name", "/description", "/type"
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --value string    The value to be used within the operations.
                        - name: The name of the collection. Must not be "".
                        - description: The description of the collection. Empty string "" is allowed.
                        - type: The type of the collection. Via this path the collection type can be toggled between "private" and "publicgoverned".
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
