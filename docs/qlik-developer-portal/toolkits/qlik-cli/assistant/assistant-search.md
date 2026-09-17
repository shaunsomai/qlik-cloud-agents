---
source: https://qlik.dev/toolkits/qlik-cli/assistant/assistant-search/
last_updated: 2026-06-03T09:30:31+02:00
---

# assistant search

## qlik assistant search

Perform search on an assistant

### Synopsis

Perform search with either `SIMPLE` or `FULL` mode. SIMPLE does semantic search while FULL does semantic search, reranking and hybrid search. Use topN to control number of chunks in response, max limit is 50. Default to 5.

```
qlik assistant search <assistantId> [flags]
```

### Options

```
  -f, --file file           Read request body from the specified file
  -h, --help                help for search
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --prompt string       (Required) Query text or question to search.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --searchMode string   Search mode to use.   Allowed values: ˋSIMPLEˋ and ˋFULLˋ.   Default: ˋSIMPLEˋ.
                            Allowed values: "SIMPLE", "FULL"
      --topN int            Number of chunks to return in results.
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
