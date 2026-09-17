---
source: https://qlik.dev/toolkits/qlik-cli/report/report-output-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# report output ls

## qlik report output ls

Get report request outputs

### Synopsis

Get the list of the outputs produced so far for the given report request. The outputs are generated asynchronously
and are complete only when the status of the report request is 'done' or 'failed' or 'aborted'.

```
qlik report output ls <reportId> [flags]
```

### Options

```
      --filter string   The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive.
                        The following fields support the ˋeqˋ (equals) operator: ˋoutputIdˋ
                        Example:
                        outputId eq "123" or outputId eq "321"
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --page string     If present, the cursor that starts the page of data that is returned.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort strings    Sorting parameters
                        Allowed values: "+outputId", "-outputId", "+sizeBytes", "-sizeBytes"
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
