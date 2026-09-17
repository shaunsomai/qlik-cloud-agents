---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-batch-prediction-schedule-set/
last_updated: 2025-06-18T09:34:47+02:00
---

# ml deployment batch-prediction schedule set

## qlik ml deployment batch-prediction schedule set

Add a batch prediction schedule

### Synopsis

Adds a schedule to a batch prediction.

```
qlik ml deployment batch-prediction schedule set [flags]
```

### Options

```
      --batch-predictionId string                (Required) ID of the batch prediction
      --data-attributes-applyDatasetChangeOnly   If true, only run prediction if dataset has changed to avoid
                                                 duplicates. If set to false, re-runs predictions on unchanged
                                                 datasets.
      --data-attributes-endDateTime string       When the job is scheduled to finish
      --data-attributes-recurrence strings       Recurrence rules. Maximum is DAILY but you can specify the
                                                 hour, minute, and second it runs each day.
                                                 One string per rule.
      --data-attributes-startDateTime string     (Required) When the job is scheduled to start
      --data-attributes-timezone string          (Required) Timezone used for the date-time fields
      --data-type string                         
                                                 Allowed values: "batch-prediction-schedule"
      --deploymentId string                      (Required) ID of the deployment
  -f, --file file                                Read request body from the specified file
  -h, --help                                     help for set
      --interval int                             Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                    Return only IDs from the command
      --raw                                      Return original response from server without any processing
      --retry int                                Number of retries to do before failing, max 10
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
