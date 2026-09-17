---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-starter-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant starter update

## qlik assistant starter update

Update a starter

### Synopsis

Updates the specified starter.

```
qlik assistant starter update <starterId> [flags]
```

### Options

```
      --additionalContext string                         (Required) Optional context collected from curated meant to be leveraged by LLM-based question recommendation system.
      --assistantId string                               (Required) The ID of the assistant containing the requested starter.
  -f, --file file                                        Read request body from the specified file
      --followups-additionalContext string               Optional context collected from curated meant to be leveraged by LLM-based question recommendation system.
      --followups-id string                              Unique identifier of the Followup.
      --followups-question string                        Starter sample question.
      --followups-recommendedAnswer-content string       Starter answer content.
      --followups-recommendedAnswer-contentType string   Answer type of content.
  -h, --help                                             help for update
      --id string                                        (Required) Unique identifier of the starter.
      --interval int                                     Duration in seconds to wait between retries, at least 1 (default 1)
      --question string                                  (Required) Starter sample question.
  -q, --quiet                                            Return only IDs from the command
      --raw                                              Return original response from server without any processing
      --recommendedAnswer-content string                 (Required) Starter answer content.
      --recommendedAnswer-contentType string             (Required) Answer type of content.
      --retry int                                        Number of retries to do before failing, max 10
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
