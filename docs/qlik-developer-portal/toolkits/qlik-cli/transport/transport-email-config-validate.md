---
source: https://qlik.dev/toolkits/qlik-cli/transport/transport-email-config-validate/
last_updated: 2026-06-03T09:30:31+02:00
---

# transport email-config validate

## qlik transport email-config validate

Get configuration status

### Synopsis

Returns the current isValid value for the email configuration for the tenant. Does not attempt to connect to a server to verify the connection or send a test email. Will return false if no email configuration exists.

```
qlik transport email-config validate [flags]
```

### Options

```
  -h, --help           help for validate
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
