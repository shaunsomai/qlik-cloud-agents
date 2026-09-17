---
source: https://qlik.dev/toolkits/qlik-cli/theme/theme-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# theme create

## qlik theme create

Create a new theme

### Synopsis

Creates a new theme. Accepts either provided file or data object. The name of the new theme must be different to any existing themes.

```
qlik theme create [flags]
```

### Options

```
      --author string          Author of the theme.
      --dependencies unknown   Map of dependencies describing version of the component it requires.
      --description string     Description of the theme.
      --file file              Theme archive.
  -h, --help                   help for create
      --homepage string        Home page of the theme.
      --icon string            Icon to show in the client.
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
      --keywords string        Keywords for the theme.
      --license string         Under which license this theme is published.
      --name string            The display name of this theme.
      --qextFilename string    The name of the qext file that was uploaded with this theme.
      --qextVersion string     The version from the qext file that was uploaded with this extension.
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --repository string      Link to the theme source code.
      --retry int              Number of retries to do before failing, max 10
      --supplier string        Supplier of the theme.
      --tags strings           List of tags.
      --type string            The type of this theme (visualization, etc.).
      --version string         Version of the theme.
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
