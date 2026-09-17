---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-export/
last_updated: 2026-06-03T09:30:31+02:00
---

# di-project export

## qlik di-project export

Export a project

### Synopsis

Exports the specified data integration project.

```
qlik di-project export <di-projectId> [flags]
```

### Options

```
  -f, --file file            Read request body from the specified file
  -h, --help                 help for export
      --includeBindings      Include bindings in the exported zip file (optional, default is false)
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --mode string          Defines the export format for the project files.
                             - 'LEGACY': Exports a ZIP of the previous JSON files. Deprecated and will be removed in a future release.
                             - 'MINIMAL': Exports a ZIP of the new YAML files, including only non-default attribute values.
                             - 'ALL': Exports a ZIP of the new YAML files, including all attributes.
                             Allowed values: "MINIMAL", "ALL", "LEGACY"
      --output-file string   Filepath specifying where to write the response body.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
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
