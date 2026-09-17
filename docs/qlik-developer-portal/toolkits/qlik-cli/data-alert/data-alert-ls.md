---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert ls

## qlik data-alert ls

List data alert tasks

### Synopsis

Retrieves all data alert tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks.

```
qlik data-alert ls [flags]
```

### Options

```
      --appID string         The app ID you would like to filter by
      --conditionId string   The conditionId you would like to filter by
  -h, --help                 help for ls
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int            Limit the returned result set
      --next string          The cursor to the next page of data. Only one of next or previous may be specified.
      --offset int           Offset for finding a list of entities - used for pagination
      --ownerId string       The id of the owner you would like to filter by
      --ownerName string     The name of the owner you would like to filter by
      --prev string          The cursor to the previous page of data. Only one of next or previous may be specified.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --role strings         The role you would like to filter by
                             Allowed values: "owner", "recipient", "notowner"
      --sort strings         Sort the returned result set by the specified field
                             Allowed values: "-datecreated", "datecreated", "+datecreated", "-ownername", "ownername", "+ownername", "lasttrigger", "-lasttrigger", "+lasttrigger", "lastscan", "-lastscan", "+lastscan", "name", "-name", "+name", "enabled", "-enabled", "+enabled", "status", "-status", "+status", "nextexecutiontime", "-nextexecutiontime", "+nextexecutiontime"
      --status strings       The status you would like to filter by
                             Allowed values: "INVALID_RECIPIENT", "INVALID_OWNER", "DISABLED", "VALID"
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
