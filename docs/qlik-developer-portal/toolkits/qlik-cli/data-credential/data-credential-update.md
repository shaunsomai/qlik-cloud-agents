---
source: https://qlik.dev/toolkits/qlik-cli/data-credential/data-credential-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-credential update

## qlik data-credential update

Updates a credential specified by ID (or by name when bycredentialname=true is set in query)

### Synopsis

Updates a credential specified by ID (or by name when bycredentialname=true is set in query)

```
qlik data-credential update <qID> [flags]
```

### Options

```
      --byCredentialName      If set to true, credentialId in the query will be interpreted as credential's name
      --connectionId string   ID of connection that will be associated with the credential
      --datasourceID string   ID datasource that the credential is created for
  -f, --file file             Read request body from the specified file
  -h, --help                  help for update
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --qID string            UUID of the credential
      --qName string          (Required) Name of the credential
      --qPassword string      (Required) Password
      --qType string          (Required) Type of credential (i.e. connector provider of the corresponding connection)
      --qUsername string      (Required) User name
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
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
