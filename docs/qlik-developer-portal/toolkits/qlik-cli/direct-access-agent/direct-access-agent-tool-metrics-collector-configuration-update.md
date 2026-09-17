---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-tool-metrics-collector-configuration-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# direct-access-agent tool metrics-collector configuration update

## qlik direct-access-agent tool metrics-collector configuration update

Set metrics collector settings

### Synopsis

Completely replaces the contents of the metrics collector settings configuration file. Partial updates are not supported.  Requestor must be assigned the `TenantAdmin` role. Available in Direct Access Gateway V1.7.9+.

```
qlik direct-access-agent tool metrics-collector configuration update <direct-access-agentId> [flags]
```

### Options

```
      --connectorConfigurations-connectorAgent-metricsCollectionEnabled         (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-connectorAgent-scrapeIntervalSeconds int        (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-fileConnector-metricsCollectionEnabled          (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-fileConnector-scrapeIntervalSeconds int         (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-odbcConnector-metricsCollectionEnabled          (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-odbcConnector-scrapeIntervalSeconds int         (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-restConnector-metricsCollectionEnabled          (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-restConnector-scrapeIntervalSeconds int         (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-sapBwConnector-metricsCollectionEnabled         (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-sapBwConnector-scrapeIntervalSeconds int        (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-sapPackageConnector-metricsCollectionEnabled    (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-sapPackageConnector-scrapeIntervalSeconds int   (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-sapSqlConnector-metricsCollectionEnabled        (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-sapSqlConnector-scrapeIntervalSeconds int       (Required) Frequency in seconds at which metrics are collected from this connector.
      --connectorConfigurations-systemMetrics-metricsCollectionEnabled          (Required) Indicates whether metrics collection is enabled for this connector.
      --connectorConfigurations-systemMetrics-scrapeIntervalSeconds int         (Required) Frequency in seconds at which metrics are collected from this connector.
  -f, --file file                                                               Read request body from the specified file
  -h, --help                                                                    help for update
      --interval int                                                            Duration in seconds to wait between retries, at least 1 (default 1)
      --metricsCollectorSettings-baseScrapeIntervalSeconds int                  (Required) The base interval in seconds for the metrics collection loop.
                                                                                This defines how frequently the collector checks whether to scrape each connector, not the interval at which each connector is scraped. Must be equal to or less than the lowest individual connector scrape interval.
      --metricsCollectorSettings-dataRetentionCheckIntervalMinutes int          (Required) The interval in minutes the metrics collector checks for and deletes old data.
      --metricsCollectorSettings-enabled                                        (Required) Indicates whether the metrics collector is enabled.
      --metricsCollectorSettings-localDataRetentionDays int                     (Required) The number of days to retain local data.
      --metricsCollectorSettings-localDatabaseFileLocation string               (Required) The file location for the local metrics database. If not specified, defaults to ˋC:\ProgramData\Qlik\Gateway\tmpˋ.
      --metricsCollectorSettings-port int                                       (Required) The port number that the metrics collector API will run on.
                                                                                This must match the port that the SYSTEM connector runs on to enable network metrics collection.
  -q, --quiet                                                                   Return only IDs from the command
      --raw                                                                     Return original response from server without any processing
      --retry int                                                               Number of retries to do before failing, max 10
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
