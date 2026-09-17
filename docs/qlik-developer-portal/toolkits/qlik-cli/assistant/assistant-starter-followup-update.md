---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-starter-followup-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# assistant starter followup update

## qlik assistant starter followup update

Update a Followup

### Synopsis

Updates the specified Followup.

```
qlik assistant starter followup update <followupId> [flags]
```

### Options

```
      --additionalContext string               (Required) Optional context collected from curated meant to be leveraged by LLM-based question recommendation system.
      --assistantId string                     (Required) The ID of the assistant containing the requested Followup.
  -f, --file file                              Read request body from the specified file
  -h, --help                                   help for update
      --id string                              (Required) Unique identifier of the Followup.
      --interval int                           Duration in seconds to wait between retries, at least 1 (default 1)
      --question string                        (Required) Starter sample question.
  -q, --quiet                                  Return only IDs from the command
      --raw                                    Return original response from server without any processing
      --recommendedAnswer-content string       (Required) Starter answer content.
      --recommendedAnswer-contentType string   (Required) Answer type of content.
      --retry int                              Number of retries to do before failing, max 10
      --starterId string                       (Required) The ID of the starter containing the requested Followup.
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
