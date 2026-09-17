---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-thread-invoke/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant thread invoke

## qlik assistant thread invoke

Execute synchronous prompt

### Synopsis

Execute prompt in synchronous non-streaming mode.

```
qlik assistant thread invoke [flags]
```

### Options

```
      --assistantId string        (Required) The ID of the Assistant containing requested Thread
  -f, --file file                 Read request body from the specified file
  -h, --help                      help for invoke
      --input-includeText         Returns text from chunks in sources output. Default value is false.
      --input-prompt string       Input prompt string for the Assistant to respond to.
      --input-promptType string   Sets the prompt type to thread.
                                  Allowed values: "thread"
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --retry int                 Number of retries to do before failing, max 10
      --threadId string           (Required) The ID of the Thread to retrieve
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
