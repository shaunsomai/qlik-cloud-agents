---
source: https://qlik.dev/toolkits/qlik-cli/ui-config/ui-config-pinned-link-bulk-create-pinned-links/
last_updated: 2026-06-03T09:30:31+02:00
---

# ui-config pinned-link bulk-create-pinned-links

## qlik ui-config pinned-link bulk-create-pinned-links

Create multiple pinned links

### Synopsis

Creates one or more pinned links for navigation, an alternative method to multiple calls to `/ui-config/pinned-links`. Links are displayed below any existing pinned links, and will be added in the order sent in the request. Requires calling user to be assigned the `TenantAdmin` role. A tenant can have a maximum of 50 pinned links.

```
qlik ui-config pinned-link bulk-create-pinned-links [flags]
```

### Options

```
  -f, --file file           Read request body from the specified file
  -h, --help                help for bulk-create-pinned-links
      --interval int        Duration in seconds to wait between retries, at least 1 (default 1)
      --links-link string   The URL the user will be taken to when they click on the custom link. Must be https.
      --links-name string   The title of the link, which will be shown in the navigation bar. Max length 50 characters.
  -q, --quiet               Return only IDs from the command
      --raw                 Return original response from server without any processing
      --retry int           Number of retries to do before failing, max 10
      --scope string        (Required) Specifies the scope of the link. Only supports ˋtenantˋ.
                            Allowed values: "tenant"
      --type string         (Required) Specifies the type of the link. Only supports ˋcustom-linkˋ.
                            Allowed values: "custom-link"
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
