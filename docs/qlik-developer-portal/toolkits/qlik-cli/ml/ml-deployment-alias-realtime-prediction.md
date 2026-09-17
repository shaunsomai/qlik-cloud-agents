---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-alias-realtime-prediction/
last_updated: 2025-06-18T09:34:47+02:00
---

# ml deployment alias realtime-prediction

## qlik ml deployment alias realtime-prediction

Generate predictions in a synchronous request/response

### Synopsis

Generate predictions in a synchronous request/response

```
qlik ml deployment alias realtime-prediction [flags]
```

### Options

```
      --aliasName string            (Required) The name of the ML Deployment Alias that will be used to determine which model should be used to produce predictions
      --deploymentId string         (Required) ID of the deployment
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for realtime-prediction
      --includeNotPredictedReason   If true, reason why a prediction was not produced included response
      --includeShap                 If true, shap values included in response
      --includeSource               If true, source data included in response
      --index string                The name of the feature in the source data to use as an index in the
                                    response data. The column will be included with its original name
                                    and values. This is intended to allow the caller to join results
                                    with source data.
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --rows strings                Rows of the dataset from which to produce predictions.
                                    Date features must be in ISO 8601 format.
      --schema-name string          The name of a feature in the dataset
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
