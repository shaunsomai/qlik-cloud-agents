---
source: https://qlik.dev/toolkits/qlik-cli/app/app-unbuild/
last_updated: 2025-06-18T09:34:47+02:00
---

# app unbuild

## qlik app unbuild

Split up an existing app into separate json and yaml files

### Synopsis

Extracts generic objects, dimensions, measures, variables, reload script and connections from an app in an engine into separate json and yaml files.
In addition to the resources from the app a config.yml configuration file is generated that binds them all together.
Passwords in the connection definitions can not be exported from the app and hence need to be handled manually.
Generic Object trees (e.g. Qlik Sense sheets) are exported as a full property tree which means that child objects are found inside the parent´s json (the qChildren array).

```
qlik app unbuild [flags]
```

### Examples

```
qlik app unbuild
qlik app unbuild --app APP-ID
```

### Options

```
  -a, --app string   Name or identifier of the app
      --dir string   Path to a the folder where the unbuilt app is exported (default "./<app name>-unbuild")
  -h, --help         help for unbuild
      --no-data      Open app without data
  -t, --traffic      Log JSON websocket traffic to stderr
      --ttl string   The Engine session's time to live in seconds (default "0")
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
