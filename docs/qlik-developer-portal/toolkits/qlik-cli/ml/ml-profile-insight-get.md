---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-profile-insight-get/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml profile-insight get

## qlik ml profile-insight get

Get profile insights

### Synopsis

Retrieves profile insights for the specified dataset. If you received a
`202 Accepted` response from `POST /ml/profile-insights`, poll this
endpoint until a `200 OK` response with `ready` status is returned.

```
qlik ml profile-insight get <profile-insightId> [flags]
```

### Options

```
      --experimentType string        The optional experiment type for profile-insights GET requests after
                                     this is known.
                                     Allowed values: "binary", "multiclass", "regression"
      --experimentVersionId string   The optional experimentVersionId query parameter for profile-insights
                                     GET requests. When provided after a version has been trained, it gets
                                     the profile insights snapshot used in previous versions rather than
                                     new results.
  -h, --help                         help for get
      --interval int                 Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                        Return only IDs from the command
      --raw                          Return original response from server without any processing
      --retry int                    Number of retries to do before failing, max 10
      --target string                The optional target feature for profile-insights GET requests after this
                                     is known.
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
