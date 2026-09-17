---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-experiment-version-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# ml experiment version ls

## qlik ml experiment version ls

List experiment versions

### Synopsis

List experiment versions

```
qlik ml experiment version ls [flags]
```

### Options

```
      --experimentId string   (Required) ID of the experiment
      --filter string         Experiment version filter options
                              - ˋisRunningˋ boolean - Is the experiment version running (training models)?
                              - ˋisSettledˋ boolean - Is the experiment version settled?
                              - ˋstatusˋ enum string - Status to filter by. Omit to get models of any status.
                                - Valid statuses: pending, ready, error, cancelled
                              - ˋmodelIdˋ UUID string - ID of a model associated with the experiment
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --offset int            Number of rows to skip before getting page[size]
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort string           Field(s) by which to sort response
                              Allowed values: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "experimentMode", "+experimentMode", "-experimentMode", "experimentType", "+experimentType", "-experimentType", "name", "+name", "-name", "status", "+status", "-status", "updatedAt", "+updatedAt", "-updatedAt", "versionNumber", "+versionNumber", "-versionNumber"
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
