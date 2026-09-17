---
source: https://qlik.dev/toolkits/qlik-cli/audit/audit-ls/
last_updated: 2025-06-18T09:34:47+02:00
---

# audit ls

## qlik audit ls

List recent audit events

### Synopsis

Retrieves list of events for subscribed services for your tenant. Stores events for 90 days, after which they can be accessed via `/v1/audits/archive`.

```
qlik audit ls [flags]
```

### Options

```
      --eventTime string   The start/end time interval formatted in ISO 8601 to search by eventTime. For example, "?eventTime=2021-07-14T18:41:15.00Z/2021-07-14T18:41:15.99Z".
      --eventType string   The case-sensitive string used to search by eventType. Retrieve a list of possible eventTypes with ˋ/v1/audits/typesˋ.
  -h, --help               help for ls
      --id string          The comma separated list of audit unique identifiers.
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int          The total number of resources to retrieve.
      --next string        The cursor to the next page of resources. Provide either the next or prev cursor, but not both.
      --prev string        The cursor to the previous page of resources. Provide either the next or prev cursor, but not both.
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
      --sort string        The property of a resource to sort on (default sort is -eventTime). The supported properties are source, eventType, and eventTime. A property must be prefixed by + or - to indicate ascending or descending sort order respectively.
      --source string      The case-sensitive string used to search by source. Retrieve a list of possible sources with ˋ/v1/audits/sourcesˋ.
      --userId string      The case-sensitive string used to search by userId.
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
