---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task

## qlik scheduling task

Manage scheduling tasks

### Synopsis

Scheduling tasks define event-driven or manually started workflows for tenant resources. Use this group to create, inspect, start, update, and monitor tasks together with their run history and dependency graph.

```
qlik scheduling task [flags]
```

### Options

```
  -h, --help   help for task
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
