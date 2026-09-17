---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-execution-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert execution ls

## qlik data-alert execution ls

List data alert task executions

### Synopsis

Lists executions for the specified data alerting task.

```
qlik data-alert execution ls [flags]
```

### Options

```
      --conditionId string       Filter by condition id related to the executions.
      --conditionStatus string   Filter by whether the alerting task execution status is FINISHED or FAILED.
                                 Allowed values: "FINISHED", "FAILED", "ALL"
      --data-alertId string      (Required) The alerting task identifier.
      --daysOfMonth ints         Specifies required days of the month that the execution was created in
      --daysOfWeek strings       Specifies a filter for custom handled periods of time in which the executions were handled
                                 Allowed values: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
      --fields strings           Specifies specific properties to be populated
                                 Allowed values: "evaluationId", "triggerTime", "conditionStatus", "executionEvaluationStatus", "evaluation", "evaluation.endTime", "evaluation.resultData", "evaluation.resultData.count", "evaluation.resultData.headers", "evaluation.resultData.positive", "evaluation.resultData.negative", "evaluation.resultData.dimensions", "evaluation.resultData.measures"
  -h, --help                     help for ls
      --includeEvaluation        Specifies whether to include evaluation details
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --lastEachDay              Specifies whether to only show the last execution in each day
      --limit int                Limit the returned result set
      --minimumGapDays int       Specifies the number of days required between each entry. This should require a sort by triggertime
      --next string              The cursor to the next page of data. Only one of next or previous may be specified.
      --offset int               Offset for pagination - how many elements to skip
      --prev string              The cursor to the previous page of data. Only one of next or previous may be specified.
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
      --searchResultsLimit int   Specifies a limit number for the search query, affects total count and is not related to pagination
      --since string             Specifies a date that executions should have been created after. Date in RFC3339Nano format, such as 2020-01-01T00:00:00.000Z
      --sort strings             Sort the returned result set by the specified field
                                 Allowed values: "triggertime", "-triggertime", "+triggertime"
      --timezone string          Specifies a timezone the other time-based filters in this query should consider. Expecting a momentjs format, such as America/Los_Angeles
      --triggered                Filter by whether the alerting task is triggered.
      --until string             Specifies a date that executions should have been created before. Date in RFC3339Nano format, such as 2020-01-01T00:00:00.000Z
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
