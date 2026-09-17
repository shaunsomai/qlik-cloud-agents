---
source: https://qlik.dev/toolkits/qlik-cli/app/app-report-filter-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# app report-filter ls

## qlik app report-filter ls

Get the filter list

### Synopsis

List all filters that are present in the given app. Filters allow to reduce the app data visible in a report output. Each filter can contain definitions on one or multiple fields.

```
qlik app report-filter ls [flags]
```

### Options

```
      --appId string          (Required) Qlik Sense app identifier
      --filter string         The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive.
                              The following fields support the ˋcoˋ (contains) operator: ˋnameˋ, ˋdescriptionˋ
                              The following fields support the ˋeqˋ (equals) operator: ˋownerIdˋ
                              Example:
                              (name co "query1" or description co "query2") and ownerId eq "123"
      --filterTypes strings   The filter type (REP, SUB). REP stands for report bookmark, SUB for subscription bookmark.
                              Allowed values: "REP", "SUB"
  -h, --help                  help for ls
      --interval int          Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int             The total number of resources to retrieve.
      --loadType string       Load type expressing the kind of request, eg. interactive for report requests from the Web UI, batch for scheduled report generation.
                              Allowed values: "interactive", "batch"
      --page string           If present, the cursor that starts the page of data that is returned.
  -q, --quiet                 Return only IDs from the command
      --raw                   Return original response from server without any processing
      --retry int             Number of retries to do before failing, max 10
      --sort strings          Sorting parameters.
                              Allowed values: "+ownerId", "-ownerId", "-name", "+name", "+description", "-description", "+createdAt", "-createdAt", "+updatedAt", "-updatedAt"
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
