---
source: https://qlik.dev/toolkits/qlik-cli/core/core-auth-settings-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# core auth-settings patch

## qlik core auth-settings patch

Update authentication settings

### Synopsis

Updates one or more authentication settings for the tenant using JSON Patch (RFC 6902). Supports `replace` operations on `/userSessionInactivityTimeoutMinutes`, `/maxUserSessionLifespanMinutes`, and `/dynamicClientRegistrationEnabled`. The value for `maxUserSessionLifespanMinutes` must be a whole number of hours (divisible by 60). The user must be assigned the `TenantAdmin` role.

```
qlik core auth-settings patch [flags]
```

### Options

```
  -f, --file file               Read request body from the specified file
  -h, --help                    help for patch
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
      --op string               The operation to be performed.
                                Allowed values: "replace"
      --path string             A JSON Pointer to the authentication settings field. Use ˋ/dynamicClientRegistrationEnabledˋ only with a boolean ˋvalueˋ. Fields ˋ/dcrDefaultConsentMethodˋ and ˋ/dcrAllowedAuthenticationMethodsˋ are only available when dynamic client registration is enabled.
                                Allowed values: "/userSessionInactivityTimeoutMinutes", "/maxUserSessionLifespanMinutes", "/dynamicClientRegistrationEnabled", "/dcrDefaultConsentMethod", "/dcrAllowedAuthenticationMethods"
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
      --value int|bool|string   Value to set for the targeted authentication settings field. Timeout fields accept only integer values, ˋ/dynamicClientRegistrationEnabledˋ accepts only boolean values, ˋ/dcrDefaultConsentMethodˋ accepts a string value, and ˋ/dcrAllowedAuthenticationMethodsˋ accepts an array of strings.
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
