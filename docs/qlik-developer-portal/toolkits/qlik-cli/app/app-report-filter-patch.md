---
source: https://qlik.dev/toolkits/qlik-cli/app/app-report-filter-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# app report-filter patch

## qlik app report-filter patch

Update a filter

### Synopsis

Update a filter

```
qlik app report-filter patch <report-filterId> [flags]
```

### Options

```
      --appId string                                                           (Required) Qlik Sense app identifier
  -f, --file file                                                              Read request body from the specified file
  -h, --help                                                                   help for patch
      --interval int                                                           Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                                                              operation (replace).
                                                                               Allowed values: "replace"
      --path string                                                            A JSON Pointer path (/).
                                                                               Allowed values: "/filter"
  -q, --quiet                                                                  Return only IDs from the command
      --raw                                                                    Return original response from server without any processing
      --retry int                                                              Number of retries to do before failing, max 10
      --value-Filter-description string                                        The filter description.
      --value-Filter-filterV1_0-fieldsByState-description key:string           Gets the resource description.
      --value-Filter-filterV1_0-fieldsByState-name key:string                  Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --value-Filter-filterV1_0-fieldsByState-overrideValues key:bool[=true]   Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --value-Filter-filterV1_0-fieldsByState-selectExcluded key:bool[=true]   Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --value-Filter-filterV1_0-fieldsByState-values-valueAsNumber key:int     The filter values.
      --value-Filter-filterV1_0-fieldsByState-values-valueAsText key:string    The filter values.
      --value-Filter-filterV1_0-fieldsByState-values-valueType key:string      The filter values.
                                                                               Allowed values: "string", "number", "evaluate", "search"
      --value-Filter-filterV1_0-variables-evaluate                             The filter variables.
      --value-Filter-filterV1_0-variables-name string                          The filter variables.
      --value-Filter-filterV1_0-variables-value string                         The filter variables.
      --value-Filter-filterVersion string                                      The value to be used for this operation. The properties that cannot be patched include id, filterType, appId
                                                                               Allowed values: "filter-1.0", "filter-2.0"
      --value-Filter-name string                                               The filter name.
      --value-Filter-ownerId string                                            The user that owns the filter, if missing the same as the request user.
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
