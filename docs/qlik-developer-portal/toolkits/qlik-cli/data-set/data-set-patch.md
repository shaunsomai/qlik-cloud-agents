---
source: https://qlik.dev/toolkits/qlik-cli/data-set/data-set-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-set patch

## qlik data-set patch

Patch data set

### Synopsis

Partially updates an existing DataSet by ID using JSON Patch operations (RFC 6902), including ownership attributes.

A user can update any DataSet within a space if they fulfill **one** of the following conditions:

- Has **Can edit** permission in a **data space**.
- Is a **Professional** user with the **Editor** or **Operator** role in a **shared space**.
- Is a **Professional** user with the **Facilitator** or **Operator** role in a **managed space**.

```
qlik data-set patch <data-setId> [flags]
```

### Options

```
  -f, --file file       Read request body from the specified file
      --from string     A JSON Pointer path pointing to the location to move/copy from.
  -h, --help            help for patch
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --op string       The operation to be performed.
                        Allowed values: "add", "remove", "replace", "move", "copy", "test"
      --path string     A JSON pointer to the property being affected.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --value unknown   The value to add, replace or test.
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
