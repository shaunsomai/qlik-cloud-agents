---
source: https://qlik.dev/toolkits/qlik-cli/sharing-task/sharing-task/
last_updated: 2025-06-18T09:34:47+02:00
---

# sharing-task

## qlik sharing-task

Manage and schedule when tasks execute

### Synopsis

For scheduled capabilities such as reports, data alerts, subscriptions, and more, sharing tasks defines when these tasks execute, and tie together the resource definition with any conditions on execution.

```
qlik sharing-task [flags]
```

### Options

```
  -h, --help   help for sharing-task
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
