---
source: https://qlik.dev/toolkits/qlik-cli/user/user-invite/
last_updated: 2026-06-03T09:30:31+02:00
---

# user invite

## qlik user invite

Invite one or more users by email address

### Synopsis

Invite one or more users by email address.

```
qlik user invite [flags]
```

### Options

```
  -f, --file file                  Read request body from the specified file
  -h, --help                       help for invite
      --interval int               Duration in seconds to wait between retries, at least 1 (default 1)
      --invitees-email string      Email address for this invitee. Example - "foo@qlik.com".
      --invitees-language string   Optional ISO 639-1 2 letter code for invite language. Defaults to 'en' when missing or not found.
      --invitees-name string       Optional display name for this invitee. Example - "Elvis Presley".
      --invitees-resend            Flag - when true invite message is sent to inactive or invited users. Typically used to force email resend to users who are not yet active.
  -q, --quiet                      Return only IDs from the command
      --raw                        Return original response from server without any processing
      --retry int                  Number of retries to do before failing, max 10
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
