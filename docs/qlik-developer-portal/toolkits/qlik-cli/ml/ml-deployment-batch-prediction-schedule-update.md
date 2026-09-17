---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-batch-prediction-schedule-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml deployment batch-prediction schedule update

## qlik ml deployment batch-prediction schedule update

Update a batch prediction schedule

### Synopsis

Updates the schedule for a batch prediction.

```
qlik ml deployment batch-prediction schedule update [flags]
```

### Options

```
      --batch-predictionId string   (Required) ID of the batch prediction
      --deploymentId string         (Required) ID of the deployment
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for update
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                   All patch requests use the replace operation
                                    Allowed values: "replace"
      --path string                 Path for the property you want to update
                                    Allowed values: "/startDateTime", "/endDateTime", "/timezone", "/recurrence", "/applyDatasetChangeOnly"
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --value unknown               Use for fields that can be ˋanyˋ type (string, number, etc.)
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
