---
source: https://qlik.dev/toolkits/qlik-cli/api-key/api-key-create/
last_updated: 2025-06-18T09:34:47+02:00
---

# api-key create

## qlik api-key create

Create API key

### Synopsis

Creates an API key, either for a user, or for configuring SCIM for a compatible Identity Provider.
Sending `sub` and `subType` is required only for creating SCIM keys.

```
qlik api-key create [flags]
```

### Options

```
      --description string   (Required) Text that describes the API key.
      --expiry string        The expiry of the API key, in ISO8601 duration format. For example, ˋP7Dˋ sets expiry after 7 days. If not provided, defaults to the maximum API key or SCIM key expiry configured in the tenant.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for create
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --sub string           The ID of the subject for the API key. For SCIM the format is ˋSCIM\\{{IDP-ID}}ˋ, where ˋ{{IDP-ID}}ˋ is the ID of the IDP in Qlik. When creating an API key for a user, this is their user ID, e.g. ˋ64ef645a3b7009d55dee5a2bˋ, and will default to the requesting user if not provided. User must be assigned the ˋDeveloperˋ role.
      --subType string       Type of the subject. For SCIM, it should be ˋexternalClientˋ. If not specified, defaults to ˋuserˋ.
                             Allowed values: "user", "externalClient"
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
