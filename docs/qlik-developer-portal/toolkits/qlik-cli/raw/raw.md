---
source: https://qlik.dev/toolkits/qlik-cli/raw/raw/
last_updated: 2025-06-18T09:34:47+02:00
---

# raw

## qlik raw

Send HTTP Request to Qlik Cloud

### Synopsis

Send HTTP Request to Qlik Cloud. Query parameters are specified using the --query flag, a body can be specified using one of the body flags (body, body-file or body-values)

```
qlik raw <get|put|patch|post|delete> <path> [flags]
```

### Examples

```
qlik raw get v1/items --query name=ImportantApp
```

### Options

```
      --body string                  The content of the body as a string
      --body-file string             A file path pointing to a file containing the body of the http request
      --body-values stringToString   A set of key=value pairs that well be compiled into a json object. A dot (.) inside the key is used to traverse into nested objects. The key suffixes :bool or :number can be appended to the key to inject the value into the json structure as boolean or number respectively. (default [])
  -h, --help                         help for raw
      --human                        Prints IDs and names only
      --interval int                 Duration in seconds to wait between retries, at least 1 (default 1)
      --output-file string           A file path pointing to where the response body should be written
      --query stringToString         Query parameters specified as key=value pairs separated by comma (default [])
  -q, --quiet                        Return only IDs from the command
      --raw                          Return original response from server without any processing
      --retry int                    Number of retries to do before failing, max 10
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
