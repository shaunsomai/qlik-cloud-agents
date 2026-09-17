---
source: https://qlik.dev/toolkits/qlik-cli/automl-deployment/automl-deployment-create-realtime-prediction/
last_updated: 2026-06-03T09:30:31+02:00
---

# automl-deployment create-realtime-prediction

## qlik automl-deployment create-realtime-prediction

(Deprecated) Generate predictions

### Synopsis

(Deprecated) Generates predictions in a synchronous request and response.

```
qlik automl-deployment create-realtime-prediction <automl-deploymentId> [flags]
```

### Options

```
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create-realtime-prediction
      --includeNotPredictedReason   If true, will include a column with the reason why a prediction was not produced.
      --includeShap                 If true, the shapley values will be included in the response.
      --includeSource               If true, the source data will be included in the response
      --index string                The name of the feature in the source data to use as an index in the response data. The column will be included with its original name and values. This is intended to allow the caller to join results with source data.
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --rows strings                The rows of the dataset to produce predictions from. Date features must be in ISO 8601 format.
      --schema-name string          The name of a feature in the dataset.
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
