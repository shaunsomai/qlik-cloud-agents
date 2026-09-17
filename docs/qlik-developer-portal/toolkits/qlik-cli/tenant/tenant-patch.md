---
source: https://qlik.dev/toolkits/qlik-cli/tenant/tenant-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# tenant patch

## qlik tenant patch

Update a tenant

### Synopsis

Updates properties of a specific tenant by ID.

```
qlik tenant patch <tenantId> [flags]
```

### Options

```
      --body unknowns       (Deprecated) Array of JSON-objects to send as the request body.
  -f, --file file           Read request body from the specified file
  -h, --help                help for patch
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --op string           The operation to be performed.
                            Allowed values: "replace"
      --path string         A JSON Pointer value that references a location within the target document where the operation is performed.
                            Allowed values: "/name", "/hostnames/1", "/autoAssignCreateSharedSpacesRoleToProfessionals", "/autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals", "/autoAssignDataServicesContributorRoleToProfessionals", "/enableAnalyticCreation", "/enableAppOpeningFeedback"
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --value string|bool   The value to be used for this operation.
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
