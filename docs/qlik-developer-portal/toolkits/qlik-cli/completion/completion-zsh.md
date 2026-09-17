---
source: https://qlik.dev/toolkits/qlik-cli/completion/completion-zsh/
last_updated: 2025-06-18T09:34:47+02:00
---

# completion zsh

## qlik completion zsh

Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

```bash
echo "autoload -U compinit; compinit" >> ~/.zshrc
```

To load completions in your current shell session:

```bash
source <(qlik completion zsh)
```

To load completions for every new session, execute once:

#### Linux:

```bash
qlik completion zsh > "${fpath[1]}/_qlik"
```

#### macOS:

```bash
qlik completion zsh > $(brew --prefix)/share/zsh/site-functions/_qlik
```

You will need to start a new shell for this setup to take effect.

### Synopsis

Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

```bash
echo "autoload -U compinit; compinit" >> ~/.zshrc
```

To load completions in your current shell session:

```bash
source <(qlik completion zsh)
```

To load completions for every new session, execute once:

#### Linux:

```bash
qlik completion zsh > "${fpath[1]}/_qlik"
```

#### macOS:

```bash
qlik completion zsh > $(brew --prefix)/share/zsh/site-functions/_qlik
```

You will need to start a new shell for this setup to take effect.

```
qlik completion zsh [flags]
```

### Options

```
  -h, --help              help for zsh
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
