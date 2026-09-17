---
source: https://qlik.dev/toolkits/qlik-cli/question/question-ask/
last_updated: 2025-06-18T09:34:47+02:00
---

# question ask

## qlik question ask

Returns the generated response for parsed chat queries, if no app was specified nor present in conversation context, suggests matching apps

### Synopsis

Returns the generated response for parsed chat queries, if no app was specified nor present in conversation context, suggests matching apps.

```
qlik question ask [flags]
```

### Options

```
      --app-id string                
      --app-name string              
      --clearEntityContext           Flag that clears the entity context.
      --disableConversationContext   Flag that specifies either to enable converastion context.
      --disableFollowups             The flag specifies whether to disable follow-up recommendations.
      --disableNarrative             Flag that specifies whether the narratives should be generated for the user query or not.
      --enableVisualizations         Flag that specifies whether visualization object should be provided or not.
  -f, --file file                    Read request body from the specified file
  -h, --help                         help for ask
      --interval int                 Duration in seconds to wait between retries, at least 1 (default 1)
      --lang string                  The language to assume when parsing, specified as an ISO-639-1 code.
                                     Defaults to 'en' (English).
  -q, --quiet                        Return only IDs from the command
      --raw                          Return original response from server without any processing
      --recommendationId string      property that contains the Id of the recommendation for which the response should be generated.
      --retry int                    Number of retries to do before failing, max 10
      --text string                  (Required) The sentence that will be parsed.
      --visualizationTypes strings   Specify visualizationTypes for only which visualization object should be provided if enableVisualizations is set to true. For eg. ['linechart', 'barchart']
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
