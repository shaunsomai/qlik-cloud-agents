---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-data-credential-rm/
last_updated: 2026-06-03T09:30:31+02:00
---

# connectivity data-credential rm

## qlik connectivity data-credential rm

Delete a credential

### Synopsis

Use this operation to delete a data credential by its unique identifier. To delete a credential by name instead of ID, set the `byCredentialName` query parameter to `true`.

```
qlik connectivity data-credential rm <qID> [flags]
```

### Options

```
      --byCredentialName   When ˋtrueˋ, the value of the ˋcredentialIdˋ in the query is interpreted as the credential's name rather than its unique identifier.
  -h, --help               help for rm
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
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
