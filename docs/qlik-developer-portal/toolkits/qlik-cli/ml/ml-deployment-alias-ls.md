---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-alias-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml deployment alias ls

## qlik ml deployment alias ls

List aliases

### Synopsis

Retrieves a list of aliases based on filter parameters for a deployment.

```
qlik ml deployment alias ls [flags]
```

### Options

```
      --deploymentId string   (Required) ID of the deployment
      --filter string         Alias fields by which you can filter responses
                              - ˋnameˋ string - Aliases with exact name
                              - ˋmodelIdˋ UUID string - By model ID
                              - ˋmodeˋ enum string - Mode by which alias is set to
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --offset int            Number of rows to skip before getting page[size]
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort string           Field(s) by which to sort response
                              Allowed values: "name", "+name", "-name"
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
