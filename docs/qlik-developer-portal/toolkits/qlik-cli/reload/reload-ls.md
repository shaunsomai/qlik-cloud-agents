---
source: https://qlik.dev/toolkits/qlik-cli/reload/reload-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# reload ls

## qlik reload ls

Find and return reloads

### Synopsis

Finds and returns the reloads that the user has access to.

```
qlik reload ls [flags]
```

### Options

```
      --appId string    (Required) The UUID formatted string used to search for an app's reload history entries. TenantAdmin users may omit this parameter to list all reload history in the tenant.
      --filter string   SCIM filter expression used to search for reloads.
                        The filter syntax is defined in RFC 7644 section 3.4.2.2
                        
                        Supported attributes:
                        - status: see #schemas/Status
                        - partial: see #schemas/Partial
                        - type: see #schemas/Type
                        
                        Supported operators:
                        - eq
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --log             The boolean value used to include the log field or not, set log=true to include the log field.
      --next string     The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --partial         The boolean value used to search for a reload is partial or not.
      --prev string     The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort by, with +/- prefix indicating sort order
                        Allowed values: "creationTime", "+creationTime", "-creationTime", "status", "+status", "-status", "startTime", "+startTime", "-startTime", "endTime", "+endTime", "-endTime"
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
