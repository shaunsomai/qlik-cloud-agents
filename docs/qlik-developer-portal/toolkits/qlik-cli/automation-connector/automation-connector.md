---
source: https://qlik.dev/toolkits/qlik-cli/automation-connector/automation-connector/
last_updated: 2026-06-03T09:30:31+02:00
---

# automation-connector

## qlik automation-connector

List automation connectors

### Synopsis

Automation connectors let you integrate third-party services and applications into your data analytics workflows. Use this API to discover available connectors and understand billing characteristics.

```
qlik automation-connector [flags]
```

### Options

```
  -h, --help   help for automation-connector
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
