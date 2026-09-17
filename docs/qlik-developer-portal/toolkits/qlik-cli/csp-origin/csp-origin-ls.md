---
source: https://qlik.dev/toolkits/qlik-cli/csp-origin/csp-origin-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# csp-origin ls

## qlik csp-origin ls

List CSPs

### Synopsis

Retrieves all content security policies for a tenant.

```
qlik csp-origin ls [flags]
```

### Options

```
      --childSrc         Filter resources by directive 'childSrc', true/false.
      --connectSrc       Filter resources by directive 'connectSrc', true/false.
      --connectSrcWSS    Filter resources by directive 'connectSrcWSS', true/false.
      --fontSrc          Filter resources by directive 'fontSrc', true/false.
      --formAction       Filter resources by directive 'formAction', true/false.
      --frameAncestors   Filter resources by directive 'frameAncestors', true/false.
      --frameSrc         Filter resources by directive 'frameSrc', true/false.
  -h, --help             help for ls
      --imgSrc           Filter resources by directive 'imgSrc', true/false.
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int        The total number of resources to retrieve.
      --mediaSrc         Filter resources by directive 'mediaSrc', true/false.
      --name string      Filter resources by name (wildcard and case insensitive).
      --next string      Cursor to the next page.
      --objectSrc        Filter resources by directive 'objectSrc', true/false.
      --origin string    Filter resources by origin (wildcard and case insensitive).
      --prev string      Cursor to previous next page.
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --scriptSrc        Filter resources by directive 'scriptSrc', true/false.
      --sort string      Field to sort by, prefix with -/+ to indicate order.
                         Allowed values: "name", "-name", "origin", "-origin", "createdDate", "-createdDate", "modifiedDate", "-modifiedDate"
      --styleSrc         Filter resources by directive 'styleSrc', true/false.
      --workerSrc        Filter resources by directive 'workerSrc', true/false.
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
