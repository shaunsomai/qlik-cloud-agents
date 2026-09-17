---
source: https://qlik.dev/toolkits/qlik-cli/context/context-init/
last_updated: 2025-06-18T09:34:47+02:00
---

# context init

## qlik context init

Set up access to Qlik Cloud

### Synopsis

Set up access to Qlik Cloud by entering the domain name and the api key of the Qlik Sense instance. If no context name is supplied the domain name is used as context name

```
qlik context init <context name> [flags]
```

### Options

```
  -h, --help   help for init
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
