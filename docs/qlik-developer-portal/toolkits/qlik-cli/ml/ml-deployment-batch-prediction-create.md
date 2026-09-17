---
source: https://qlik.dev/toolkits/qlik-cli/ml/ml-deployment-batch-prediction-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# ml deployment batch-prediction create

## qlik ml deployment batch-prediction create

Create a prediction configuration

### Synopsis

Create a prediction configuration

```
qlik ml deployment batch-prediction create [flags]
```

### Options

```
      --data-attributes-aliasId string                         ID of an alias
      --data-attributes-dataSetId string                       The Qlik catalog dataset ID
      --data-attributes-deploymentId string                    ID of a model deployment
      --data-attributes-description string                     
      --data-attributes-indexColumn string                     A optional column name upon which to create an index. Must be unique for
                                                               every row. If not included, Qlik will create a unique index column.
      --data-attributes-name string                            Name of this entity
      --data-attributes-schedule-applyDatasetChangeOnly        If true, only run prediction if dataset has changed to avoid
                                                               duplicates. If set to false, re-runs predictions on unchanged
                                                               datasets.
      --data-attributes-schedule-endDateTime string            When the job is scheduled to finish
      --data-attributes-schedule-recurrence strings            Recurrence rules. Maximum is DAILY but you can specify the
                                                               hour, minute, and second it runs each day.
                                                               One string per rule.
      --data-attributes-schedule-startDateTime string          (Required) When the job is scheduled to start
      --data-attributes-schedule-timezone string               (Required) Timezone used for the date-time fields
      --data-attributes-writeback-dstCoordShapName string      Sets which files, file names, and spaces are used to write results of
                                                               batch predictions (output files) to the catalog.
                                                               
                                                               Note that for predictions based on time series models, ˋdstShapNameˋ
                                                               and ˋdstCoordShapNameˋ do not apply and will be ignored if set.
      --data-attributes-writeback-dstName string               (Required) Sets which files, file names, and spaces are used to write results of
                                                               batch predictions (output files) to the catalog.
                                                               
                                                               Note that for predictions based on time series models, ˋdstShapNameˋ
                                                               and ˋdstCoordShapNameˋ do not apply and will be ignored if set.
      --data-attributes-writeback-dstNotPredictedName string   Sets which files, file names, and spaces are used to write results of
                                                               batch predictions (output files) to the catalog.
                                                               
                                                               Note that for predictions based on time series models, ˋdstShapNameˋ
                                                               and ˋdstCoordShapNameˋ do not apply and will be ignored if set.
      --data-attributes-writeback-dstShapName string           Sets which files, file names, and spaces are used to write results of
                                                               batch predictions (output files) to the catalog.
                                                               
                                                               Note that for predictions based on time series models, ˋdstShapNameˋ
                                                               and ˋdstCoordShapNameˋ do not apply and will be ignored if set.
      --data-attributes-writeback-dstSourceName string         Sets which files, file names, and spaces are used to write results of
                                                               batch predictions (output files) to the catalog.
                                                               
                                                               Note that for predictions based on time series models, ˋdstShapNameˋ
                                                               and ˋdstCoordShapNameˋ do not apply and will be ignored if set.
      --data-attributes-writeback-format string                (Required) File format for write back files (this applies to all)
                                                               Allowed values: "qvd", "parquet", "csv"
      --data-attributes-writeback-spaceId string               (Required) Space ID where you want to save batch prediction writebacks or
                                                               empty string ('') save them to your personal space.
      --data-type string                                       
                                                               Allowed values: "batch-prediction"
      --deploymentId string                                    (Required) ID of the deployment
  -f, --file file                                              Read request body from the specified file
  -h, --help                                                   help for create
      --interval int                                           Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                                  Return only IDs from the command
      --raw                                                    Return original response from server without any processing
      --retry int                                              Number of retries to do before failing, max 10
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
