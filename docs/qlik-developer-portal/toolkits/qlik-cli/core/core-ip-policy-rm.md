---
source: https://qlik.dev/toolkits/qlik-cli/core/core-ip-policy-rm/
last_updated: 2026-06-03T09:30:31+02:00
---

# core ip-policy rm

## qlik core ip-policy rm

Delete an IP policy

### Synopsis

Deletes an IP policy by ID. If this is the last enabled policy in the tenant, IP allowlisting will be disabled and access will be permitted via all IP addresses. The user's IP address must be present in at least one other policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role.

```
qlik core ip-policy rm <ip-policyId> [flags]
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
