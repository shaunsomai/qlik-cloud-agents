---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml deployment ls

## qlik ml deployment ls

List deployments

### Synopsis

List deployments

```
qlik ml deployment ls [flags]
```

### Options

```
      --filter string   Deployment fields by which you can filter responses.<br><br>
                        - ˋspaceIdˋ ID string (or empty string for personal space) - ID of space in which deployment(s) exist
                        - ˋmodelIdˋ UUID string - By model ID
                        - ˋcreatedByˋ ID string
                        - ˋownerIdˋ ID string
                        - ˋexperimentIdˋ UUID string - ID of experiment in which model(s) exist
                        - ˋexperimentVersionIdˋ UUID string - ID of experiment version in which model(s) exist
                        - ˋpredictionIdˋ UUID string - ID of prediction which exists on deployment
                        - ˋpredictionEnabledˋ boolean - Are predictions enabled
                        - ˋexactNameˋ string - Deployments with exact name. Names may not be unique.
                        - ˋnameContainsˋ string - Deployments where name includes this. Names may not be unique
                        - ˋexperimentTypeˋ string - Deployments that have models of the experiment type
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --offset int      Number of rows to skip before getting page[size]
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Field(s) by which to sort response
                        Allowed values: "createdAt", "+createdAt", "-createdAt", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt"
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
