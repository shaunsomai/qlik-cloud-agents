---
source: https://qlik.dev/toolkits/qlik-cli/core/core-auth-settings/
last_updated: 2026-06-03T09:30:31+02:00
---

# core auth-settings

## qlik core auth-settings

Manage core authentication settings

### Synopsis

Authentication settings control tenant session limits and related authentication behaviour in the core platform. Use this group to review the current values and patch the settings that govern user sessions.

```
qlik core auth-settings [flags]
```

### Options

```
  -h, --help   help for auth-settings
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
