---
source: https://qlik.dev/toolkits/qlik-cli/webhook/webhook-delivery-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# webhook delivery ls

## qlik webhook delivery ls

Return deliveries for a webhook

### Synopsis

Returns deliveries for a specific webhook. Delivery history is stored for 1 week.

```
qlik webhook delivery ls [flags]
```

### Options

```
      --eventType string   Filter resources by event-type.
  -h, --help               help for ls
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int          The total number of resources to retrieve.
      --next string        Cursor to the next page.
      --prev string        Cursor to the previous page.
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
      --sort string        Field to sort by, prefix with -/+ to indicate order.
                           Allowed values: "status", "+status", "-status", "triggeredAt", "+triggeredAt", "-triggeredAt"
      --status string      Filter resources by status (success or fail).
                           Allowed values: "success", "fail"
      --webhookId string   (Required) The webhook's unique identifier.
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
