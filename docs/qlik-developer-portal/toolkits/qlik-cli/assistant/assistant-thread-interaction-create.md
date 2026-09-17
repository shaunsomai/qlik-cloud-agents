---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-thread-interaction-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant thread interaction create

## qlik assistant thread interaction create

Create an interaction

### Synopsis

Creates a new interaction for the thread.

```
qlik assistant thread interaction create [flags]
```

### Options

```
      --assistantId string               (Required) The ID of the assistant in which to create the interaction.
  -f, --file file                        Read request body from the specified file
  -h, --help                             help for create
      --interval int                     Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                            Return only IDs from the command
      --raw                              Return original response from server without any processing
      --rejected                         Indicator the system marked request as suspicious.
      --rejectionReason int              Rejection reason for a question:
                                           * 1 - PROMPT_INJECTION
                                           * 2 - OUT_OF_CONTEXT
                                           * 3 - TOO_COMPLEX
                                         Allowed values: "1", "2", "3"
      --request string                   (Required) Interaction request content.
      --response string                  (Required) Interaction response content.
      --retry int                        Number of retries to do before failing, max 10
      --sources-chunks-chunkId string    Chunk unique identifier for "AI" generated message source.
      --sources-chunks-text string       Chunk text for "AI" generated message source.
      --sources-datasourceId string      Reference to DataSource used for "AI" generated messages.
      --sources-documentId string        Reference to Document used for "AI" generated messages.
      --sources-knowledgebaseId string   Reference to KnowledgeBase used for "AI" generated messages.
      --sources-lastIndexedAt string     Datetime when the knowledgebase was last indexed.
      --sources-source string            Path to the document used.
      --threadId string                  (Required) The ID of the thread in which to create the interaction.
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
