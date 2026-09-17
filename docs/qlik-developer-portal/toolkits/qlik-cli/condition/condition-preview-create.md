---
source: https://qlik.dev/toolkits/qlik-cli/condition/condition-preview-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# condition preview create

## qlik condition preview create

Create condition preview request\\

### Synopsis

Create condition preview request.

```
qlik condition preview create [flags]
```

### Options

```
      --compoundCondition-conditionBase-appId string         The id of the app the condition is evaluated against
      --compoundCondition-conditionBase-bookmarkId string    The bookmark corresponding to the selection state to apply to the app at evaluation time
      --compoundCondition-conditionBase-description string   Description of the condition
      --compoundCondition-conditionBase-type string          Indicates the condition type
                                                             Allowed values: "compound", "data"
      --compoundCondition-data-conditions strings            Array of condition ids
      --compoundCondition-data-expression string             Boolean expression made up of variable names defined from the conditions section
      --compoundCondition-data-history-enabled               Is history enabled
      --dataCondition-conditionBase-appId string             The id of the app the condition is evaluated against
      --dataCondition-conditionBase-bookmarkId string        The bookmark corresponding to the selection state to apply to the app at evaluation time
      --dataCondition-conditionBase-description string       Description of the condition
      --dataCondition-conditionBase-type string              Indicates the condition type
                                                             Allowed values: "compound", "data"
      --dataCondition-conditionData unknown                  List of parameters specific to data condition are available in DCE and will be passed as is to DCE as per the API docs of data-condition-evaluator
      --dataCondition-dimensions-field string                Field referred to the dimension where the selection is made. This may be used to generate deep links.
      --dataCondition-dimensions-qLibraryId string           Refers to a dimension stored in the library
      --dataCondition-dimensions-title string                Dimension title
      --dataCondition-headers strings                        List of header labels
      --dataCondition-history-enabled                        Is history enabled
      --dataCondition-measures-qLibraryId string             Refers to a measure stored in the library
      --dataCondition-measures-qNumFormat unknown            Format of the field
      --dataCondition-measures-title string                  Measure title
      --dataCondition-selections-count int                   The count
      --dataCondition-selections-field string                Field name
      --dataCondition-selections-selectedSummary strings     Array of selected
  -f, --file file                                            Read request body from the specified file
  -h, --help                                                 help for create
      --interval int                                         Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                                Return only IDs from the command
      --raw                                                  Return original response from server without any processing
      --retry int                                            Number of retries to do before failing, max 10
      --type string                                          (Required) Indicates the condition type
                                                             Allowed values: "compound", "data"
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
