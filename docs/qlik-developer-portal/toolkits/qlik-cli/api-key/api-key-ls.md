---
source: https://qlik.dev/toolkits/qlik-cli/api-key/api-key-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# api-key ls

## qlik api-key ls

List API keys

### Synopsis

Lists API keys for the tenant. To list API keys owned by other users, requesting user must be assigned the `TenantAdmin` role.

```
qlik api-key ls [flags]
```

### Options

```
      --createdByUser string   The user ID that created the API key.
      --endingBefore string    Get resources with IDs that are lower than the target resource ID. Cannot be used in conjunction with startingAfter.
  -h, --help                   help for ls
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int              The total number of resources to retrieve.
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --retry int              Number of retries to do before failing, max 10
      --sort string            The field to sort by, with +/- prefix indicating sort order
                               Allowed values: "createdByUser", "+createdByUser", "-createdByUser", "sub", "+sub", "-sub", "status", "+status", "-status", "description", "+description", "-description", "created", "+created", "-created"
      --startingAfter string   Get resources with IDs that are higher than the target resource ID. Cannot be used in conjunction with endingBefore.
      --status string          The status of the API key.
                               Allowed values: "active", "expired", "revoked"
      --sub string             The ID of the subject. For SCIM the format is ˋSCIM\\{{IDP-ID}}ˋ, where ˋ{{IDP-ID}}ˋ is the ID of the IDP in Qlik. For users, use their user ID, e.g. ˋ64ef645a3b7009d55dee5a2bˋ.
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
