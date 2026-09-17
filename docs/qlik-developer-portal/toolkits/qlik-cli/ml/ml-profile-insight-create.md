---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-profile-insight-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml profile-insight create

## qlik ml profile-insight create

Start profile insights creation

### Synopsis

Starts creating profile insights for an experiment dataset.
This is an asynchronous operation. A `202 Accepted` response indicates
that the process has started successfully. Use the link in the response
to check the status.

```
qlik ml profile-insight create [flags]
```

### Options

```
      --data-attributes-dataSetId string        The Qlik catalog dataset ID
      --data-attributes-experimentType string   Experiment type
                                                Allowed values: "binary", "multiclass", "regression"
      --data-attributes-shouldWait              Whether the server should or client should manage polling/waiting
      --data-attributes-target string           Optional selected target provided on subsequent requests
      --data-type string                        Data wrapper for request input
                                                Allowed values: "profile-insights"
  -f, --file file                               Read request body from the specified file
  -h, --help                                    help for create
      --interval int                            Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                   Return only IDs from the command
      --raw                                     Return original response from server without any processing
      --retry int                               Number of retries to do before failing, max 10
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
