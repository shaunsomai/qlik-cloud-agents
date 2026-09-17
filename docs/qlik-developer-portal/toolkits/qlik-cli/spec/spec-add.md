---
source: https://qlik.dev/toolkits/qlik-cli/spec/spec-add/
last_updated: 2025-06-18T09:34:47+02:00
---

# spec add

## qlik spec add

Add a specification to be used for command generation

### Synopsis

The name specified using name flag overrides the extracted name of specification'.
Note: When multiple specifications are added, the names are specified in the same order.
Format: qlik spec add spec\_one.json spec\_two.json --name "spec-1","spec-2".
If the names aren't specified or left blank they are extracted from the specification

```
qlik spec add <path-to-spec>... [flags]
```

### Examples

```
qlik spec add ./my-spec.json --name foo
```

### Options

```
  -h, --help           help for add
      --name strings   Override the extracted name of specification
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
