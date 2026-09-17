---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-graph-children-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task graph children ls

## qlik scheduling task graph children ls

List child tasks

### Synopsis

Retrieves a paginated list of tasks that are direct children of the specified task in the dependency graph. A child task is one that is triggered when the parent task completes successfully.

```
qlik scheduling task graph children ls <taskId> [flags]
```

### Options

```
      --filter string   Advanced filter expression using RFC 7644 SCIM syntax. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for syntax details. All comparisons are case-insensitive. Supported fields: ˋnameˋ, ˋenabledˋ, ˋresourceIdˋ, ˋownerIdˋ, ˋspaceIdˋ, ˋcreatedAtˋ, ˋupdatedAtˋ, ˋupdatedByˋ, ˋlastStatusˋ, ˋlastTriggeredByˋ, ˋlastStartedAtˋ, ˋlastEndedAtˋ, ˋlastExecutedAsˋ, and ˋtriggerTypeˋ.
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --page string     Cursor token for fetching the next page of results.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     Field and direction to sort results by. Prefix the field name with
                        ˋ+ˋ for ascending or ˋ-ˋ for descending order. Defaults to ˋ-updatedAtˋ.
                        Allowed values: "+createdAt", "-createdAt", "+enabled", "-enabled", "+name", "-name", "+ownerId", "-ownerId", "+resourceId", "-resourceId", "+spaceId", "-spaceId", "+updatedAt", "-updatedAt", "+updatedBy", "-updatedBy", "+lastStatus", "-lastStatus", "+lastTriggeredBy", "-lastTriggeredBy", "+lastStartedAt", "-lastStartedAt", "+lastEndedAt", "-lastEndedAt", "+lastExecutedAs", "-lastExecutedAs", "+triggerType", "-triggerType"
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
