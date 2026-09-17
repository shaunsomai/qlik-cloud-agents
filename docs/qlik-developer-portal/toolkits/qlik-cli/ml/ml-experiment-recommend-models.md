---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-experiment-recommend-models/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml experiment recommend-models

## qlik ml experiment recommend-models

Request model recommendations for an experiment

### Synopsis

Returns model recommendations for a specified experiment, including the best-performing, fastest, and most accurate models based on evaluation metrics.

```
qlik ml experiment recommend-models <experimentId> [flags]
```

### Options

```
      --algorithms strings    The model algorithms to consider
                              Allowed values: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression"
      --deployed              Whether to only consider models that are already deployed
  -f, --file file             Read request body from the specified file
      --fullSampling          Whether to only consider models with 100% sampling
  -h, --help                  help for recommend-models
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --versionNumbers ints   The versionNumbers of the experiment versions to consider models from
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
