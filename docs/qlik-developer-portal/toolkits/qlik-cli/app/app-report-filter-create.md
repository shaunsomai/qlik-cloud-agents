---
source: https://qlik.dev/toolkits/qlik-cli/app/app-report-filter-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# app report-filter create

## qlik app report-filter create

Create a new filter

### Synopsis

Creates a new report filter which is used to re-apply selections, variables, patches to an engine session.

```
qlik app report-filter create [flags]
```

### Options

```
      --appId string                                              (Required) Qlik Sense app identifier
      --appId-in-body string                                      The App ID.
      --description string                                        The filter description.
  -f, --file file                                                 Read request body from the specified file
      --filterType string                                         (Required) 
                                                                  Allowed values: "REP", "SUB"
      --filterV1_0-fieldsByState-description key:string           Gets the resource description.
      --filterV1_0-fieldsByState-name key:string                  Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --filterV1_0-fieldsByState-overrideValues key:bool[=true]   Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --filterV1_0-fieldsByState-selectExcluded key:bool[=true]   Map of fields to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000.
      --filterV1_0-fieldsByState-values-valueAsNumber key:int     The filter values.
      --filterV1_0-fieldsByState-values-valueAsText key:string    The filter values.
      --filterV1_0-fieldsByState-values-valueType key:string      The filter values.
                                                                  Allowed values: "string", "number", "evaluate", "search"
      --filterV1_0-variables-evaluate                             The filter variables.
      --filterV1_0-variables-name string                          The filter variables.
      --filterV1_0-variables-value string                         The filter variables.
      --filterVersion string                                      (Required) 
                                                                  Allowed values: "filter-1.0", "filter-2.0"
  -h, --help                                                      help for create
      --interval int                                              Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                                               (Required) The filter name.
      --ownerId string                                            The user that owns the filter, if missing the same as the request user.
  -q, --quiet                                                     Return only IDs from the command
      --raw                                                       Return original response from server without any processing
      --retry int                                                 Number of retries to do before failing, max 10
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
