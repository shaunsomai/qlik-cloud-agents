---
source: https://qlik.dev/toolkits/qlik-cli/webhook/webhook-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# webhook ls

## qlik webhook ls

List webhooks

### Synopsis

Retrieves all webhooks entries for a tenant that the user has access to. Users assigned the `TenantAdmin` role can retrieve all webhooks. A user can have up to 150 webhooks at one time.

```
qlik webhook ls [flags]
```

### Options

```
      --createdByUserId string   Filter resources by user that created it.
      --enabled                  Filter resources by enabled true/false.
      --eventTypes string        Filter resources by event-type/types, a single webhook item can have multiple event-types.
  -h, --help                     help for ls
      --interval int             Duration in seconds to wait between retries, at least 1 (default 1)
      --level string             Filter resources by level that user has access to (either user or level).
      --limit int                The total number of resources to retrieve.
      --name string              Filter resources by name (wildcard and case insensitive).
      --next string              Cursor to the next page.
      --origins string           Filter resources by origins, supports multiorigin.
                                 Allowed values: "api", "automations", "management-console"
      --ownerId string           Filter resources by user that owns it, only applicable for user level webhooks.
      --prev string              Cursor to the previous page.
  -q, --quiet                    Return only IDs from the command
      --raw                      Return original response from server without any processing
      --retry int                Number of retries to do before failing, max 10
      --sort string              Field to sort by, prefix with -/+ to indicate order.
                                 Allowed values: "name", "+name", "-name", "url", "+url", "-url", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt"
      --updatedByUserId string   Filter resources by user that last updated the webhook.
      --url string               Filter resources by URL (wildcard and case insensitive).
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
