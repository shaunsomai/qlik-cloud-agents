---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant create

## qlik assistant create

Create an assistant

### Synopsis

Creates a new assistant.

```
qlik assistant create [flags]
```

### Options

```
      --customProperties unknown    (Required) freeform JSON to allow custom customization options.
      --defaultPromptType string    Default prompt type for the assistant.
                                    Allowed values: "thread", "oneshot"
      --description string          (Required) The description of the assistant.
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --knowledgeBases strings      List of knowledgebases the assistant is using.
      --name string                 (Required) The name of the assistant.
      --orderedStarterIds strings   List of starter IDs in the order they will be sorted.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --spaceId string              (Required) Unique identifier of the space to contain the assistant.
      --systemMessage string        (Deprecated) System prompt setting up conversation context.
      --tags strings                The list of tags for the assistant.
      --title string                (Required) The title of the assistant.
      --welcomeMessage string       (Required) Initial message in the chat conversation.
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
