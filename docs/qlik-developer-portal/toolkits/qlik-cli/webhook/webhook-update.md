---
source: https://qlik.dev/toolkits/qlik-cli/webhook/webhook-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# webhook update

## qlik webhook update

Update all webhook properties

### Synopsis

Updates a webhook, any omitted fields will be cleared, returns updated webhook.

```
qlik webhook update <webhookId> [flags]
```

### Options

```
      --checkCertificateRevocation    If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook.
      --description string            The reason for creating the webhook.
      --enableCloudEventDelivery      If enabled the webhook will be sent as a CloudEvent, once enabled for a webhook it cannot be disabled.
      --enabled                       Whether the webhook is active and sending requests.
      --encryptedHeaders key:string   These headers are persisted encrypted and decrypted to be sent as normal headers in post request (webhook delivery), in case of URL change these headers will need to be re-entered. Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for encrypted headers.
      --eventTypes strings            Types of events for which the webhook should trigger. Retrieve available types from ˋ/v1/webhooks/event-typesˋ.
  -f, --file file                     Read request body from the specified file
      --filter string                 Filter that should match for a webhook to be triggered.
                                      Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId', beside the common attributes the "com.qlik.v1.app.reload.finished" event also supports "data.status" that could be either "ok" or "error" but can't be used together with other event types.
                                      Supported attribute operators are 'eq' and 'ne'.
                                      Supported logical operators are 'and' and 'or'.
                                      Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes.
                                      For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation.
  -h, --help                          help for update
      --interval int                  Duration in seconds to wait between retries, at least 1 (default 1)
      --level string                  Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator.
                                      Allowed values: "tenant", "user"
      --name string                   (Required) The name for the webhook.
      --ownerId string                The id of the user that owns the webhook, only applicable for user level webhooks.
  -q, --quiet                         Return only IDs from the command
      --raw                           Return original response from server without any processing
      --retry int                     Number of retries to do before failing, max 10
      --secret string                 String used as secret for calculating HMAC hash sent as header.
      --url string                    (Required) Target URL for webhook HTTPS requests.
      --webhook-headers key:string    Additional headers in the post request (webhook delivery). Note: duplicate headers are not allowed and are case-insensitive. Maximum size: 2048 bytes for non-encrypted headers.
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
