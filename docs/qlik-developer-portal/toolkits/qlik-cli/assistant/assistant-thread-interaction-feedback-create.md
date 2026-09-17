---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-thread-interaction-feedback-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# assistant thread interaction feedback create

## qlik assistant thread interaction feedback create

Create feedback

### Synopsis

Creates feedback for the thread.

```
qlik assistant thread interaction feedback create [flags]
```

### Options

```
      --assistantId string     (Required) The ID of the assistant in which to create the feedback.
      --comment string         Optional comment for feedback.
  -f, --file file              Read request body from the specified file
  -h, --help                   help for create
      --interactionId string   (Required) The ID of the interaction in which to create the feedback.
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --reason string          (Required) Reason for feedback.
      --retry int              Number of retries to do before failing, max 10
      --threadId string        (Required) The ID of the thread in which to create the feedback.
      --vote int               (Required) Integer representation of feedback given (-1 = negative, 1 = positive).
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
