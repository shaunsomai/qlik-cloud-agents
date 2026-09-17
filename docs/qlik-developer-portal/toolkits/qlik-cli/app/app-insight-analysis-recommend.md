---
source: https://qlik.dev/toolkits/qlik-cli/app/app-insight-analysis-recommend/
last_updated: 2026-06-03T09:30:31+02:00
---

# app insight-analysis recommend

## qlik app insight-analysis recommend

Returns analysis recommendations in response to a natural language question, a set of fields and master items, or a set of fields and master items with an optional target analysis

### Synopsis

Returns analysis recommendations in response to a natural language question, a set of fields and master items, or a set of fields and master items with an optional target analysis.

```
qlik app insight-analysis recommend <appId> [flags]
```

### Options

```
      --fields unknowns                              (Deprecated) Array of JSON-objects to send as the property fields.
      --fields-name string                           
      --fields-overrides-classifications strings     
      --fields-overrides-defaultAggregation string   
  -f, --file file                                    Read request body from the specified file
  -h, --help                                         help for recommend
      --interval int                                 Duration in seconds to wait between retries, at least 1 (default 1)
      --libItems unknowns                            (Deprecated) Array of JSON-objects to send as the property libItems.
      --libItems-libId string                        
      --libItems-overrides-format-qDec string        
      --libItems-overrides-format-qFmt string        
      --libItems-overrides-format-qThou string       
      --libItems-overrides-format-qType string       
      --libItems-overrides-format-qUseThou int       
      --libItems-overrides-format-qnDec int          
  -q, --quiet                                        Return only IDs from the command
      --raw                                          Return original response from server without any processing
      --retry int                                    Number of retries to do before failing, max 10
      --targetAnalysis-id string                     id of the target analysis, returned by the GET insight-analyses endpoint
      --text string                                  The NL query.
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
