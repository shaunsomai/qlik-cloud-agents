---
source: https://qlik.dev/toolkits/qlik-cli/report-template/report-template-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# report-template create

## qlik report-template create

Create a new report template

### Synopsis

Create a new report template.

```
qlik report-template create [flags]
```

### Options

```
      --description string          Template description
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for create
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                 (Required) Template name
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --sourceAppAction string      Specifies the action to perform with the given source app id. Use "validate" to verify that the template source app matches the provided value. Use "replace" to migrate the template to a different app by replacing the source app id.
                                    Allowed values: "validate", "replace"
      --sourceAppId string          The ID of the app that this template is using as data source. The id stored in the template file metadata is used if no value is specified.
      --temporaryContentId string   (Required) The ID of a previously uploaded temporary content file
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
