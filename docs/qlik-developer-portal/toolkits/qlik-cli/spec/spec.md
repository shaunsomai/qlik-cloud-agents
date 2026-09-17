---
source: https://qlik.dev/toolkits/qlik-cli/spec/spec/
last_updated: 2025-06-18T09:34:47+02:00
---

# spec

## qlik spec

Handle inclusion of external specifications

### Synopsis

Add, remove, get or list external specifications to be used for command generation.

The added specifications will overwrite bundled specifications in case of
path collisions, e.g. if you are supplying a newer version of an API spec.
Also note that commands will be generated for both public and private endpoints,
which is not the case for the bundled specifications.

Note that adding or removing external will probably change the command
structure which means that you might want to re-source the completion afterwards.

```
qlik spec [flags]
```

### Options

```
  -h, --help   help for spec
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
