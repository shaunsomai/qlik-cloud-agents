---
source: https://qlik.dev/toolkits/qlik-cli/oauth-client/oauth-client-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# oauth-client create

## qlik oauth-client create

Create an OAuth client

### Synopsis

Create a new OAuth client. Requires `TenantAdmin` role when created in-tenant. `appType` cannot be changed after creation. Consent method and published state can be changed after creation. For supported `appType`, use `PATCH /oauth-clients/{id}/connection-configs/me` to change consent method, and `POST /oauth-clients/{id}/actions/publish` to change the client to published after creation.

```
qlik oauth-client create [flags]
```

### Options

```
      --allowedAuthMethods strings              List of allowed authentication methods for the client
                                                Allowed values: "client_secret", "private_key_jwt"
      --allowedGrantTypes strings               Allowed grant types, only for use with appType: 'web'
                                                Allowed values: "client_credentials", "urn:qlik:oauth:user-impersonation"
      --allowedOrigins strings                  List of allowed origins for this client, only available with SPA application type
      --allowedScopes strings                   List of allowed scopes for this client. For a full list of scopes see [qlik.dev/authenticate/oauth/scopes/](https://qlik.dev/authenticate/oauth/scopes/).
      --appType string                          (Required) Application type
                                                Allowed values: "web", "native", "spa", "anonymous-embed"
      --clientName string                       (Required) Client application name
      --clientUri string                        URI for homepage of client
      --connectionConfig-consentMethod string   Specifies the consent method for the connection. The only allowed value is "trusted."
                                                Allowed values: "trusted"
      --description string                      Client description
  -f, --file file                               Read request body from the specified file
  -h, --help                                    help for create
      --interval int                            Duration in seconds to wait between retries, at least 1 (default 1)
      --logoUri string                          URI for logo of client
      --publicKeys-alg string                   Algorithm intended for use with the key
                                                Allowed values: "RS256", "RS512", "ES384"
      --publicKeys-crv string                   Curve for EC keys
      --publicKeys-e string                     Exponent for RSA keys
      --publicKeys-kid string                   Key ID
      --publicKeys-kty string                   Key type (e.g., RSA, EC)
                                                Allowed values: "RSA", "EC"
      --publicKeys-n string                     Modulus for RSA keys
      --publicKeys-use string                   Intended use of the key (typically "sig" for signature)
                                                Allowed values: "sig"
      --publicKeys-x string                     X coordinate for EC keys
      --publicKeys-y string                     Y coordinate for EC keys
  -q, --quiet                                   Return only IDs from the command
      --raw                                     Return original response from server without any processing
      --redirectUris strings                    List of allowed redirect URIs for login
      --retry int                               Number of retries to do before failing, max 10
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
