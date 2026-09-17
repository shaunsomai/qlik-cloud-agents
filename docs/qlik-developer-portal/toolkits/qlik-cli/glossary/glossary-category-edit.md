---
source: https://qlik.dev/toolkits/qlik-cli/glossary/glossary-category-edit/
last_updated: 2025-06-18T09:34:47+02:00
---

# glossary category edit

## qlik glossary category edit

Modify a glossary category interactively in a text-editor

### Synopsis

Modify a glossary category interactively in a text-editor

This command will fetch a glossary category and open it in the editor 'vi'.
You can change the default editor by setting the 'EDITOR' environment variable.
Default editors are 'vi' for Linux/Darwin and 'notepad' for Windows.
The resource will be updated according to the changes made in the editor upon save.

```
qlik glossary category edit <categoryId> [flags]
```

### Options

```
      --glossaryId string   (Required) The glossary id.
  -h, --help                help for edit
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
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
