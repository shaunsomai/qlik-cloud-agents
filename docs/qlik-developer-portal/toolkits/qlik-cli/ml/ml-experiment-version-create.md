---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-experiment-version-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml experiment version create

## qlik ml experiment version create

Create an experiment version

### Synopsis

Creates an experiment version.
Poll this version and check its `status` field to determine when models
are finished training.

```
qlik ml experiment version create [flags]
```

### Options

```
      --data-attributes-algorithms strings                             Algorithms used for model training in this version. See
                                                                       documentation for valid algorithms for each
                                                                       ˋexperimentTypeˋ.
                                                                       
                                                                       If not provided, defaults to all valid algorithms for your
                                                                       experimentType.
                                                                       Allowed values: "catboost_classifier", "catboost_regression", "elasticnet_regression", "gaussian_nb", "kneighbors_classifier", "lasso_regression", "lasso", "lgbm_classifier", "lgbm_regression", "linear_regression", "logistic_regression", "random_forest_classifier", "random_forest_regression", "sgd_regression", "xgb_classifier", "xgb_regression"
      --data-attributes-dataSetId string                               (Required) The Qlik catalog dataset ID
      --data-attributes-datasetOrigin string                           (Required) Whether this is a new or other dataset
                                                                       Allowed values: "new", "changed", "refreshed", "same"
      --data-attributes-dateIndexes strings                            A optional date column name to index
      --data-attributes-experimentMode string                          (Required) The model training mode for the experiment version
                                                                       Allowed values: "intelligent", "manual", "manual_hpo"
      --data-attributes-experimentType string                          (Required) Experiment type
                                                                       Allowed values: "binary", "multiclass", "regression"
      --data-attributes-featuresList-changeType string                 Indicates if you want to change the featureType for this
                                                                       feature within the experiment version
                                                                       Allowed values: "categorical", "numeric", "date", "freetext"
      --data-attributes-featuresList-dataType string                   The data type of this feature in your dataset
                                                                       Allowed values: "DATE", "TIME", "DATETIME", "TIMESTAMP", "STRING", "DOUBLE", "DECIMAL", "INTEGER", "BOOLEAN", "BINARY", "CUSTOM", "FLOAT", "OBJECT"
      --data-attributes-featuresList-featureType string                The default feature type based on the feature's data type.
                                                                       If you want a value to be interpreted differently (e.g. 0/1
                                                                       as categorical/boolean instead of numeric), use ˋchangeTypeˋ.
                                                                       Allowed values: "categorical", "numeric", "date", "freetext"
      --data-attributes-featuresList-include                           Include this feature in your experiment version? Default
                                                                       here is based on insights for this feature
                                                                       (e.g. willBeDropped).
      --data-attributes-featuresList-name string                       Name of the feature column
      --data-attributes-featuresList-parentFeature string              The parent feature name for engineered features. e.g. ˋOrderDateˋ may be the parent of its engineered features (features extracted from parent) like ˋOrderDate.YEARˋ, ˋOrderDate.MONTHˋ, etc.
      --data-attributes-name string                                    (Required) 
      --data-attributes-pipeline-transforms-column-changeType string   Pipeline metadata including transformations to apply to columns and
                                                                       specific schema configuration data
      --data-attributes-pipeline-transforms-column-name string         Pipeline metadata including transformations to apply to columns and
                                                                       specific schema configuration data
      --data-attributes-target string                                  (Required) The target field in the dataset. Set in first experiment
                                                                       version and can't be changed in subsequent versions.
      --data-attributes-trainingDuration int                           (Required) Optional training duration in seconds. If not provided, max value used.
                                                                       If provided, min 900 (15m) and max 21600 (6h).
      --data-type string                                               (Required) 
                                                                       Allowed values: "experiment-version"
      --experimentId string                                            (Required) ID of the experiment
  -f, --file file                                                      Read request body from the specified file
  -h, --help                                                           help for create
      --interval int                                                   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                                          Return only IDs from the command
      --raw                                                            Return original response from server without any processing
      --retry int                                                      Number of retries to do before failing, max 10
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
