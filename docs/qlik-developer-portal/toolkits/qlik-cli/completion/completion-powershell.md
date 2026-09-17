---
source: https://qlik.dev/toolkits/qlik-cli/completion/completion-powershell/
last_updated: 2025-06-18T09:34:47+02:00
---

# completion powershell

## qlik completion powershell

Generate the autocompletion script for powershell.

To load completions in your current shell session:

```bash
qlik completion powershell | Out-String | Invoke-Expression
```

To load completions for every new session, add the output of the above command
to your powershell profile.

### Synopsis

Generate the autocompletion script for powershell.

To load completions in your current shell session:

```bash
qlik completion powershell | Out-String | Invoke-Expression
```

To load completions for every new session, add the output of the above command
to your powershell profile.

```
qlik completion powershell [flags]
```

### Options

```
  -h, --help              help for powershell
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
