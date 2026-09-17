---
source: https://qlik.dev/toolkits/qlik-cli/completion/completion-bash/
last_updated: 2025-06-18T09:34:47+02:00
---

# completion bash

## qlik completion bash

Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.
If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

```bash
source <(qlik completion bash)
```

To load completions for every new session, execute once:

#### Linux:

```bash
qlik completion bash > /etc/bash_completion.d/qlik
```

#### macOS:

```bash
qlik completion bash > $(brew --prefix)/etc/bash_completion.d/qlik
```

You will need to start a new shell for this setup to take effect.

### Synopsis

Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.
If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

```bash
source <(qlik completion bash)
```

To load completions for every new session, execute once:

#### Linux:

```bash
qlik completion bash > /etc/bash_completion.d/qlik
```

#### macOS:

```bash
qlik completion bash > $(brew --prefix)/etc/bash_completion.d/qlik
```

You will need to start a new shell for this setup to take effect.

```
qlik completion bash
```

### Options

```
  -h, --help              help for bash
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
