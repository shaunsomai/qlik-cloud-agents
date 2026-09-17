---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-alert

## qlik data-alert

Manage data alerts - notifications based on data

### Synopsis

Supports chart sharing, chart monitoring and alerting features. The legacy sharing APIs refer to chart sharing and chart monitoring, which is a feature that allows the user to send an e-mail with an embedded chart either manually (chart sharing) or in a recurring manner (chart monitoring). It also stores the history related to these actions. The alerting/ data-alerts APIs support the alerting feature, where a user is able to create alerts that trigger notifications in case a condition in the dataset of an app is fulfilled.

```
qlik data-alert [flags]
```

### Options

```
  -h, --help   help for data-alert
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
