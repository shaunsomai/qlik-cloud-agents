---
source: https://qlik.dev/toolkits/qlik-cli/api-key/api-key-rm/
last_updated: 2025-06-18T09:34:47+02:00
---

# api-key rm

## qlik api-key rm

Delete or revoke an API key

### Synopsis

Deletes or revokes an API key for a given API key ID. When the owner of the API key sends the request, the key will be deleted and removed from the tenant. When a user assigned the `TenantAdmin` role sends the request, the key will be disabled and marked as revoked.

```
qlik api-key rm <api-keyId> [flags]
```

### Options

```
  -h, --help           help for rm
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
