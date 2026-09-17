---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-experiment-model-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# ml experiment model ls

## qlik ml experiment model ls

List models

### Synopsis

List models

```
qlik ml experiment model ls [flags]
```

### Options

```
      --experimentId string   (Required) ID of the experiment
      --filter string         Model fields you can filter by:<br><br>
                              
                              - ˋexperimentVersionIdˋ UUID string - Find by experiment version ID
                              - ˋbatchNumˋ UUID string - Search by batch number
                              - ˋisHpoˋ boolean - Is hyperparameter optimization used?
                              - ˋisMetricsˋ boolean - Are metrics for regression, binary, or multiclass are used?
                              - ˋidˋ UUID string - Find by model ID
                              - ˋalgorithmˋ enum string - Find by algorithm<br><br>
                              
                                - Valid algorithms: catboost_classifier, catboost_regression,
                                  elasticnet_regression, gaussian_nb, kneighbors_classifier,
                                  lasso_regression, lasso, lgbm_classifier, lgbm_regression,
                                  linear_regression, logistic_regression, random_forest_classifier,
                                  random_forest_regression, sgd_regression, xgb_classifier,
                                  xgb_regression<br><br>
                              
                              - ˋstatusˋ enum string - find by status<br><br>
                                - Valid statuses: pending, training_requested, training_done, ready, error<br><br>
                              - ˋhasDeploymentˋ boolean - Models that are part of a deployment
                              - ˋnameContainsˋ string - Models with name includes this case-insensitive string
                              - ˋexactNameˋ string - Models with exact name. Model names may not be unique
                              - ˋsamplingRatioˋ number - Find models by sampling ratio
                              - ˋmodelStateˋ enum string - State by which to find models<br><br>
                                - Valid states: ˋpending, enabled, disabled, inactiveˋ
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --offset int            Number of rows to skip before getting page[size]
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort string           Field(s) by which to sort response
                              Allowed values: "createdAt", "+createdAt", "-createdAt", "description", "+description", "-description", "name", "+name", "-name", "updatedAt", "+updatedAt", "-updatedAt"
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
