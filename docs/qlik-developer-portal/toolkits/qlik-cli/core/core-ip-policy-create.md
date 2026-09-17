---
source: https://qlik.dev/toolkits/qlik-cli/core/core-ip-policy-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# core ip-policy create

## qlik core ip-policy create

Create an IP policy

### Synopsis

Creates a new IPv4 IP policy in the tenant. If this is the first enabled policy, IP allowlisting will be enabled and access via other IP addresses will be blocked. The user's IP address must be present in at least one policy if allowlisting is enabled. The user must be assigned the `TenantAdmin` role. IPv6 IP addresses are not currently supported.

```
qlik core ip-policy create [flags]
```

### Options

```
      --allowedIps strings   An array of allowed IP IPv4 addresses, either as plain IP addresses, or as CIDR ranges.
      --enabled              Indicates whether the IP policy is enabled.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for create
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string          The descriptive name for the IP policy.
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
