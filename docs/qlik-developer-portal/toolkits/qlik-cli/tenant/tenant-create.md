---
source: https://qlik.dev/toolkits/qlik-cli/tenant/tenant-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# tenant create

## qlik tenant create

Create a tenant

### Synopsis

Creates a tenant in the requested region, linked to the provided license key. You must use a regional OAuth client generated via the [My Qlik portal](https://account.myqlik.qlik.com/account) to call this endpoint. Tenant creation, deactivation, and reactivation requests must be sent to the register endpoint in the relevant Qlik Cloud region, e.g. `https://register.us.qlikcloud.com/api/v1/tenants` if interacting with tenants in the `us` region.

```
qlik tenant create [flags]
```

### Options

```
      --datacenter string   The datacenter where the tenant is located.
                            
                            Supported locations for commercial licenses:
                            - ˋap-northeast-1ˋ: Japan (jp)
                            - ˋap-southeast-1ˋ: Australia (ap)
                            - ˋap-southeast-2ˋ: Singapore (sg)
                            - ˋeu-central-1ˋ: Germany (de)
                            - ˋeu-west-1ˋ: Ireland (eu)
                            - ˋeu-west-2ˋ: United Kingdom (uk)
                            - ˋus-east-1ˋ: United States of America (us)
  -f, --file file           Read request body from the specified file
  -h, --help                help for create
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --licenseKey string   The signed license key of the license that will be associated with the created tenant.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
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
