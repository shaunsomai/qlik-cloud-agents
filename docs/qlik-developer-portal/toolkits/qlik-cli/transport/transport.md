---
source: https://qlik.dev/toolkits/qlik-cli/transport/transport/
last_updated: 2025-07-08T16:09:30Z
---

# transport

## qlik transport

Manage configuration for email and notification

### Synopsis

Transports supports configuration of the tenant-level SMTP service. For the SMTP service in Qlik Automate, review the automation-connections API.

```
qlik transport [flags]
```

### Options

```
  -h, --help   help for transport
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
