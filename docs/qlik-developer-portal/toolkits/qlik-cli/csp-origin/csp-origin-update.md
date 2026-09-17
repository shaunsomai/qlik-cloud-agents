---
source: https://qlik.dev/toolkits/qlik-cli/csp-origin/csp-origin-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# csp-origin update

## qlik csp-origin update

Update a CSP

### Synopsis

Updates a content security policy.

```
qlik csp-origin update <csp-originId> [flags]
```

### Options

```
      --childSrc             Defines the valid sources for loading web workers and nested browsing contexts using elements such as frame and iFrame.
      --connectSrc           Restricts the URLs that can be loaded using script interfaces.
      --connectSrcWSS        Restricts the URLs that can be connected to websockets (all sources will be prefixed with 'wss://').
      --description string   The reason for adding this origin to the Content Security Policy.
  -f, --file file            Read request body from the specified file
      --fontSrc              Specifies valid sources for loading fonts.
      --formAction           Allow forms to be submitted to the origin.
      --frameAncestors       Specifies valid sources for embedding the resource using frame, iFrame, object, embed and applet.
      --frameSrc             Specifies valid sources for loading nested browsing contexts using elements such as frame and iFrame.
  -h, --help                 help for update
      --imgSrc               Specifies valid sources of images and favicons.
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --mediaSrc             Specifies valid sources for loading media using the audio and video elements.
      --name string          The name for this entry.
      --objectSrc            Specifies valid sources for the object, embed, and applet elements.
      --origin string        (Required) The origin that the CSP directives should be applied to.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --scriptSrc            Specifies valid sources for JavaScript.
      --styleSrc             Specifies valid sources for stylesheets.
      --workerSrc            Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts.
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
