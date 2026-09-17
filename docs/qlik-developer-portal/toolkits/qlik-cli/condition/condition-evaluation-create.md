---
source: https://qlik.dev/toolkits/qlik-cli/condition/condition-evaluation-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# condition evaluation create

## qlik condition evaluation create

Executes the condition

### Synopsis

Executes the condition

```
qlik condition evaluation create [flags]
```

### Options

```
      --alertId string                            The id of the alerting task the condition and evaluation is part of
      --causalEvent-data-eventID string           (Required) the event id from eventing service.
      --causalEvent-data-lastReloadTime string    (Required) The time of the last reload
      --causalEvent-eventID string                (Required) the event id from eventing
      --causalEvent-extensions-sessionID string   (Required) 
      --causalEvent-extensions-tenantID string    (Required) 
      --causalEvent-extensions-userID string      (Required) 
      --causalEvent-manualTrigger                 (Required) 
      --causalEvent-manualTriggerID string        (Required) the manual trigger id from eventing if present
      --conditionId string                        (Required) The id of the condition
      --contextId string                          (Required) Extra context information to carry through to the result if any
  -f, --file file                                 Read request body from the specified file
  -h, --help                                      help for create
      --interval int                              Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                     Return only IDs from the command
      --raw                                       Return original response from server without any processing
      --retry int                                 Number of retries to do before failing, max 10
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
