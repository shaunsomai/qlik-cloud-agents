---
source: https://qlik.dev/toolkits/qlik-cli/sharing-task/sharing-task-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# sharing-task ls

## qlik sharing-task ls

List sharing tasks

### Synopsis

Retrieves all sharing tasks accessible to the user. Users assigned the `TenantAdmin` or `AnalyticsAdmin` role can view all tasks.

```
qlik sharing-task ls [flags]
```

### Options

```
      --appid string         the filter by sharing task resource app id. TenantAdmin users may omit this parameter to list all sharing-tasks in the tenant.
      --excludeDeleting      Indicates if task with the status DELETING should be excluded from the list
  -h, --help                 help for ls
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int            Limit the returned result set
      --next string          (Deprecated) The cursor to the next page of data. Only one of next or previous may be specified.
      --offset int           Offset for finding a list of entities - used for pagination
      --owner string         the filter by sharing task resource owner id.
      --ownername string     the filter by sharing task resource owner name.
      --page string          The cursor to the page of data.
      --prev string          (Deprecated) The cursor to the previous page of data. Only one of next or previous may be specified.
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --retry int            Number of retries to do before failing, max 10
      --role strings         the filter by sharing task resource role.
                             Allowed values: "owner", "recipient"
      --sort strings         Sort the returned result set by the specified field
                             Allowed values: "-datecreated", "datecreated", "+datecreated", "-name", "name", "+name", "-ownername", "ownername", "+ownername", "-enabled", "enabled", "+enabled", "-status", "status", "+status", "-type", "type", "+type", "-sent", "sent", "+sent", "-scheduled", "scheduled", "+scheduled", "-appname", "appname", "+appname", "-appid", "appid", "+appid"
      --templateId strings   array of template ids to filter by
      --type strings         the filter by sharing task resource type. If type is template-sharing only and user is not tenant admin, appid is also required.
                             Allowed values: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing"
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
