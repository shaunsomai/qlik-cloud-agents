---
source: https://qlik.dev/toolkits/qlik-cli/completion/completion-fish/
last_updated: 2025-06-18T09:34:47+02:00
---

# completion fish

## qlik completion fish

Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

```bash
qlik completion fish | source
```

To load completions for every new session, execute once:

```bash
qlik completion fish > ~/.config/fish/completions/qlik.fish
```

You will need to start a new shell for this setup to take effect.

### Synopsis

Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

```bash
qlik completion fish | source
```

To load completions for every new session, execute once:

```bash
qlik completion fish > ~/.config/fish/completions/qlik.fish
```

You will need to start a new shell for this setup to take effect.

```
qlik completion fish [flags]
```

### Options

```
  -h, --help              help for fish
      --no-descriptions   disable completion descriptions
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
