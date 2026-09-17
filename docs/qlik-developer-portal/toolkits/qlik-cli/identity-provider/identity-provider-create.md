---
source: https://qlik.dev/toolkits/qlik-cli/identity-provider/identity-provider-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# identity-provider create

## qlik identity-provider create

Create identity providers of type OIDC or JWTAuth

### Synopsis

Creates a new IdP on a tenant. Requesting user must be assigned the `TenantAdmin` role. For non-interactive IdPs (e.g. JWT), IdP must be created by sending `options` payload. For interactive IdPs (e.g. SAML or OIDC), send `pendingOptions` payload to require the interactive verification step; or send `options` payload with `skipVerify` set to `true` to skip validation step and make IdP immediately available.

```
qlik identity-provider create [flags]
```

### Options

```
      --clockToleranceSec int                                               
      --createNewUsersOnLogin                                               
      --description string                                                  
  -f, --file file                                                           Read request body from the specified file
  -h, --help                                                                help for create
      --interactive                                                         
      --interval int                                                        Duration in seconds to wait between retries, at least 1 (default 1)
      --options-allowIdpInitiatedLogin                                      Toggle to allow IdP initated login by the SAML IdP.
      --options-allowedClientIds strings                                    Only clients with IDs in this list will be allowed API access. A blank list or empty value means any client IDs authenticated against the IdP will be allowed access.
      --options-audience string                                             Allows for setting audience in access tokens.
      --options-certificates unknowns                                       (Deprecated) Array of JSON-objects to send as the property options-certificates.
      --options-certificates-certificate string                             The X.509 certificate for validating signed SAML responses.
      --options-certificates-encryption                                     Indicates whether the certificate is used for encryption.
      --options-certificates-name string                                    Given name for this certificate.
      --options-certificates-signature                                      Indicates whether the certificate is used for the signature.
      --options-claimsMapping-client_id strings                             A list of JSON pointers used to map the user's client ID.
      --options-claimsMapping-email strings                                 A list of SAML attributes used to map the user's email.
      --options-claimsMapping-groups strings                                A list of SAML attributes used to map the user's groups.
      --options-claimsMapping-name strings                                  A list of SAML attributes used to map the user's name.
      --options-claimsMapping-picture strings                               A list of SAML attributes used to map the user's picture.
      --options-claimsMapping-sub strings                                   
      --options-discoveryUrl string                                         The OpenID configuration endpoint. (Ex: https://<domain>/.well-known/openid-configuration). Required if openid_configuration is not given.
      --options-entityId string                                             The entity ID for the SAML IdP. Required if metadata is not provided.
      --options-issuer string                                               The JWT issuer.
      --options-metadata-raw string                                         The IDP metadata XML in base64-encoded format.
      --options-nameIdFormat string                                         The name identifier format that will be requested from the identity provider.
                                                                            Allowed values: "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress", "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent", "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
      --options-openid_configuration-authorization_endpoint string          OAuth 2.0 Authorization Endpoint
      --options-openid_configuration-end_session_endpoint string            URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.
      --options-openid_configuration-introspection_endpoint string          The introspection endpoint is an OAuth 2.0 endpoint that takes a parameter representing an OAuth 2.0 token and returns a JSON [RFC7159] document representing the meta information.
      --options-openid_configuration-issuer string                          OpenID Provider issuer
      --options-openid_configuration-jwks_uri string                        URL of the OP's JSON Web Key Set [JWK] document
      --options-openid_configuration-token_endpoint string                  OAuth 2.0 Token Endpoint
      --options-openid_configuration-userinfo_endpoint string               URL of the OP's UserInfo Endpoint
      --options-realm string                                                The realm identifier for the IdP.
      --options-signOnUrl string                                            The sign on URL for the SAML IdP. Required if metadata is not provided.
      --options-staticKeys unknowns                                         (Deprecated) Array of JSON-objects to send as the property options-staticKeys.
      --options-staticKeys-kid string                                       Key ID used to sign the JWTs.
      --options-staticKeys-pem string                                       Pem-encoded public key for verifying the JWTs.
      --pendingOptions-allowIdpInitiatedLogin                               Toggle to allow IdP initated login by the SAML IdP.
      --pendingOptions-blockOfflineAccessScope                              When true, the ˋoffline_accessˋ scope will not be requested from the IdP where applicable.
      --pendingOptions-certificates unknowns                                (Deprecated) Array of JSON-objects to send as the property pendingOptions-certificates.
      --pendingOptions-certificates-certificate string                      The X.509 certificate for validating signed SAML responses.
      --pendingOptions-certificates-encryption                              Indicates whether the certificate is used for encryption.
      --pendingOptions-certificates-name string                             Given name for this certificate.
      --pendingOptions-certificates-signature                               Indicates whether the certificate is used for the signature.
      --pendingOptions-claimsMapping-client_id strings                      A list of JSON pointers used to map the user's client ID.
      --pendingOptions-claimsMapping-email strings                          
      --pendingOptions-claimsMapping-email_verified strings                 A list of JSON pointers used to map the user's email_verified claim.
      --pendingOptions-claimsMapping-groups strings                         
      --pendingOptions-claimsMapping-locale strings                         A list of JSON pointers used to map the user's locale.
      --pendingOptions-claimsMapping-name strings                           
      --pendingOptions-claimsMapping-picture strings                        
      --pendingOptions-claimsMapping-sub strings                            
      --pendingOptions-claimsMapping-zoneinfo strings                       A list of JSON pointers used to map the user's zoneinfo.
      --pendingOptions-clientId string                                      The client identifier used as part of authenticating an interactive identity provider.
      --pendingOptions-clientSecret string                                  The client secret used as part of authenticating an interactive identity provider.
      --pendingOptions-decryptingKey-certificate string                     The key's certificate in pem format
      --pendingOptions-decryptingKey-createdAt string                       The timestamp for when the decrypting key was created.
      --pendingOptions-decryptingKey-createdBy string                       The user id of the user who created the decrypting key
      --pendingOptions-decryptingKey-jwks string                            The public key in jwk format
      --pendingOptions-decryptingKey-keyId string                           The id of the decrypting key
      --pendingOptions-decryptingKey-keySize int                            The algorithm size of the decrypting key
      --pendingOptions-decryptingKey-keyType string                         The algorithm type of the decrypting key
      --pendingOptions-decryptingKey-publicKey string                       The public key in pem format
      --pendingOptions-discoveryUrl string                                  The OpenID configuration endpoint. (Ex: https://<domain>/.well-known/openid-configuration). Required if openid_configuration is not given.
      --pendingOptions-emailVerifiedAlwaysTrue                              Only ADFS and AzureAD IdPs can set this property. For ADFS and AzureAD, it defaults to false. For other IdPs, it defaults to undefined.
      --pendingOptions-entityId string                                      The entity ID for the SAML IdP. Required if metadata is not provided.
      --pendingOptions-idTokenSignatureAlg string                           The algorithm used to sign the ID token. The default algorithm is RS256.
                                                                            Allowed values: "RS256", "RS512"
      --pendingOptions-metadata-raw string                                  The IDP metadata XML in base64-encoded format.
      --pendingOptions-nameIdFormat string                                  The name identifier format that will be requested from the identity provider.
                                                                            Allowed values: "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress", "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent", "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
      --pendingOptions-openid_configuration-authorization_endpoint string   OAuth 2.0 Authorization Endpoint
      --pendingOptions-openid_configuration-end_session_endpoint string     URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.
      --pendingOptions-openid_configuration-introspection_endpoint string   The introspection endpoint is an OAuth 2.0 endpoint that takes a parameter representing an OAuth 2.0 token and returns a JSON [RFC7159] document representing the meta information.
      --pendingOptions-openid_configuration-issuer string                   OpenID Provider issuer
      --pendingOptions-openid_configuration-jwks_uri string                 URL of the OP's JSON Web Key Set [JWK] document
      --pendingOptions-openid_configuration-token_endpoint string           OAuth 2.0 Token Endpoint
      --pendingOptions-openid_configuration-userinfo_endpoint string        URL of the OP's UserInfo Endpoint
      --pendingOptions-realm string                                         The realm identifier for the IdP.
      --pendingOptions-scope string                                         Scope which will be sent along with token requests to the IdP. Scopes should be space delimited. Will default to certain values depending on the IdP provider.
      --pendingOptions-signOnUrl string                                     The sign on URL for the SAML IdP. Required if metadata is not provided.
      --pendingOptions-useClaimsFromIdToken                                 If true, will use the claims from the ID token. By default it is set to true for ADFS and AzureAD.
      --postLogoutRedirectUri string                                        
      --protocol string                                                     
      --provider string                                                     
  -q, --quiet                                                               Return only IDs from the command
      --raw                                                                 Return original response from server without any processing
      --retry int                                                           Number of retries to do before failing, max 10
      --skipVerify                                                          
      --tenantIds strings                                                   
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
