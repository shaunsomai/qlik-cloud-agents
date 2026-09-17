---
source: https://qlik.dev/toolkits/qlik-cli/web-notification/web-notification-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# web-notification ls

## qlik web-notification ls

Retrieve notifications matching the query

### Synopsis

Retrieve notifications matching the query.

```
qlik web-notification ls [flags]
```

### Options

```
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --page int              Page number
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --read                  Read status of the notification
      --resourceType string   Filter by resource types. If passing more than 1 resource type, use comma seperated string.
      --retry int             Number of retries to do before failing, max 10
      --sort string           The field to sort by, with +/- prefix indicating sort order
                              Allowed values: "+createdAt", "-createdAt", "+updatedAt", "-updatedAt"
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
