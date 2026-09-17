---
source: https://qlik.dev/toolkits/qlik-cli/tenant/tenant-reactivate/
last_updated: 2025-06-18T09:34:47+02:00
---

# tenant reactivate

## qlik tenant reactivate

Reactivate a tenant

### Synopsis

Reactivates a deactivated tenant. Tenants can be reactivated until the `estimatedPurgeDate` provided at time of deactivation. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants/{tenantId}/actions/reactivate` if interacting with tenants in the `us` region.

```
qlik tenant reactivate <tenantId> [flags]
```

### Options

```
  -h, --help           help for reactivate
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
