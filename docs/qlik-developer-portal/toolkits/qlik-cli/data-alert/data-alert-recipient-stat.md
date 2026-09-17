---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-recipient-stat/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert recipient-stat

## qlik data-alert recipient-stat

Get data alert task recipient stats

### Synopsis

Retrieve the recipient stats for a data alerting task.

```
qlik data-alert recipient-stat <data-alertId> [flags]
```

### Options

```
      --groups strings   The name of the groups you would like to filter by
  -h, --help             help for recipient-stat
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --sort strings     Sort the returned result set by the specified field
                         Allowed values: "+userID", "-userID", "subscribed", "+subscribed"
      --subscribed       Subscribed property you would like to filter by
      --userID string    The recipients ID you would like to filter by
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
