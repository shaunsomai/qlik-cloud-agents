---
source: https://qlik.dev/toolkits/qlik-cli/context/context-login/
last_updated: 2025-06-18T09:34:47+02:00
---

# context login

## qlik context login

Login and set cookie for the named context

### Synopsis

Login and set cookie for the named context

This is only applicable when connecting to 'Qlik Sense Enterprise on Windows' through its proxy using HTTPS.
If no 'context-name' is used as argument the 'current-context' defined in the config will be used instead.

```
qlik context login <context-name> [flags]
```

### Examples

```
qlik context login
qlik context login context-name
```

### Options

```
  -h, --help              help for login
      --password string   Password to be used when logging in to Qlik Sense Enterprise (use with caution)
      --user string       Username to be used when logging in to Qlik Sense Enterprise
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
