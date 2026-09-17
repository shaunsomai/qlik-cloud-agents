---
source: https://qlik.dev/toolkits/qlik-cli/core/core-ip-policy-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# core ip-policy ls

## qlik core ip-policy ls

List IP policies

### Synopsis

Returns a list of IP policies present in the tenant. The user must be assigned the `TenantAdmin` role.

```
qlik core ip-policy ls [flags]
```

### Options

```
      --fields string   A comma-separated list of fields to limit in the response.
      --filter string   The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. All conditional statements within this query parameter are case insensitive.
                        
                        field "enabled" supports following operators: eq
                        
                        field "id" supports following operators: eq, ne
                        
                        field "name" supports following operators: eq, co
                        
                        field "tenantId" supports following operators: eq
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --page string     The page cursor. Takes precedence over other parameters.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Optional resource field name to sort on, eg. name. Can be prefixed with +/- to determine order, defaults to (+) ascending.
                        Allowed values: "enabled", "+enabled", "-enabled", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt", "name", "+name", "-name"
      --totalResults    Determines whether to return a count of the total records matched in the query. Defaults to false.
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
