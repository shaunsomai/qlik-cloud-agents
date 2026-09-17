---
source: https://qlik.dev/toolkits/qlik-cli/transport/transport-email-config-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# transport email-config update

## qlik transport email-config update

Update email configuration

### Synopsis

Creates or replaces the email configuration for the tenant. Validation of the configuration is done as part of the request.

```
qlik transport email-config update [flags]
```

### Options

```
  -f, --file file                                Read request body from the specified file
  -h, --help                                     help for update
      --interval int                             Duration in seconds to wait between retries, at least 1 (default 1)
      --providerConfig-clientId string           Microsoft365 client identifier
      --providerConfig-clientSecret string       secret to authenticate the Microsoft365 account
      --providerConfig-emailAddress string       
      --providerConfig-emailPassword string      password for SMTP basic authentication
      --providerConfig-providerTenantId string   Microsoft365 tenant identifier
      --providerConfig-securityType string       SMTP security mechanism to use. Could be either 'none', 'StartTLS' or 'SSL/TLS'
      --providerConfig-senderName string         The name that should appear in From field when sending emails with this account
      --providerConfig-serverAddress string      domain name or IP address of SMTP server
      --providerConfig-serverPort int            smtp server port
      --providerConfig-username string           user name used for SMTP login
  -q, --quiet                                    Return only IDs from the command
      --raw                                      Return original response from server without any processing
      --retry int                                Number of retries to do before failing, max 10
      --serviceProvider string                   Name of the service provider for authentication
                                                 Allowed values: "Microsoft365", "BasicAuth"
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
