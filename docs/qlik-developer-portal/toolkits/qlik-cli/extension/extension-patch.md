---
source: https://qlik.dev/toolkits/qlik-cli/extension/extension-patch/
last_updated: 2025-06-18T09:34:47+02:00
---

# extension patch

## qlik extension patch

Update a specific extension

### Synopsis

Updates a specific extension matching either extension ID or extension name. Accepts either provided file or data object.

```
qlik extension patch <extensionId> [flags]
```

### Options

```
      --author string               Author of the extension.
      --bundle-description string   Description of the bundle.
      --bundle-id string            Unique identifier of the bundle.
      --bundle-name string          Name of the bundle.
      --bundled                     If the extension is part of an extension bundle.
      --checksum string             Checksum of the extension contents.
      --dependencies unknown        Map of dependencies describing version of the component it requires.
      --deprecated string           A date noting when the extension was deprecated.
      --description string          Description of the extension.
      --file file                   Extension archive.
  -h, --help                        help for patch
      --homepage string             Home page of the extension.
      --icon string                 Icon to show in the client.
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --keywords string             Keywords for the extension.
      --license string              Under which license this extension is published.
      --loadpath string             Relative path to the extension's entry file, defaults to ˋfilenameˋ from the qext file.
      --name string                 The display name of this extension.
      --preview string              Path to an image that enables users to preview the extension.
      --qextFilename string         The name of the qext file that was uploaded with this extension.
      --qextVersion string          The version from the qext file that was uploaded with this extension.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --repository string           Link to the extension source code.
      --retry int                   Number of retries to do before failing, max 10
      --supernova                   If the extension is a supernova extension or not.
      --supplier string             Supplier of the extension.
      --tags strings                List of tags.
      --type string                 The type of this extension (visualization, etc.).
      --version string              Version of the extension.
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
