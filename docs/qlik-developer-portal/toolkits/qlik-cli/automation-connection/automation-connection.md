---
source: https://qlik.dev/toolkits/qlik-cli/automation-connection/automation-connection/
last_updated: 2025-06-19T11:53:14Z
---

# automation-connection

## qlik automation-connection

Manage automation-connections

### Synopsis

Automation connections are data sources utilized by automations in Qlik Automate.

```
qlik automation-connection [flags]
```

### Options

```
  -h, --help   help for automation-connection
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
