---
source: https://qlik.dev/toolkits/qlik-cli/app/app-build/
last_updated: 2025-06-18T09:34:47+02:00
---

# app build

## qlik app build

Reload and save the app after updating connections, dimensions, measures, objects and the script

```
qlik app build [flags]
```

### Examples

```
qlik app build
qlik app build --connections ./myconnections.yml --script ./myscript.qvs
```

### Options

```
  -a, --app string              Name or identifier of the app
      --app-properties string   Path to a json file containing the app properties
      --bookmarks string        A list of generic bookmark json paths
      --connections string      Path to a yml file containing the data connection definitions
      --dimensions string       A list of generic dimension json paths
  -h, --help                    help for build
      --limit int               Limit the number of rows to load
      --measures string         A list of generic measures json paths
      --no-data                 Open app without data
      --no-reload               Do not run the reload script
      --no-save                 Do not save the app
      --objects string          A list of generic object json paths
      --script string           Path to a qvs file containing the app data reload script
      --silent                  Do not log reload output
  -t, --traffic                 Log JSON websocket traffic to stderr
      --ttl string              The Engine session's time to live in seconds (default "0")
      --variables string        A list of generic variable json paths
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
