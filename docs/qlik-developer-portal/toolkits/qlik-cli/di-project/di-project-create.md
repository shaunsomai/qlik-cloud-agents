---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# di-project create

## qlik di-project create

Create a new project

### Synopsis

Creates a new data integration project in the specified space.

```
qlik di-project create [flags]
```

### Options

```
      --cloudStagingConnection string   The cloud staging connection string
      --description string              A description of the project
  -f, --file file                       Read request body from the specified file
  -h, --help                            help for create
      --interval int                    Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                     The name of the project
      --platformConnection string       The platform connection string
      --platformType string             The platform type of the project. Supported values: - SNOWFLAKE: Snowflake - BIGQUERY: Google BigQuery - SYNAPSE: Azure Synapse - DATABRICKS: Databricks - REDSHIFT: Amazon Redshift - MSSQL: Microsoft SQL Server - FABRIC: Microsoft Fabric (OneLake) - QLIK_QVD: Qlik-managed QVD - QLIK_QVD_CUSTOMER_MANAGED: Customer-managed QVD
                                        Allowed values: "SNOWFLAKE", "BIGQUERY", "SYNAPSE", "DATABRICKS", "REDSHIFT", "MSSQL", "FABRIC", "QLIK_QVD", "QLIK_QVD_CUSTOMER_MANAGED"
  -q, --quiet                           Return only IDs from the command
      --raw                             Return original response from server without any processing
      --retry int                       Number of retries to do before failing, max 10
      --space string                    The ID of the space where the project will be created
      --type string                     The type of the project
                                        Allowed values: "DATA_PIPELINE", "DATA_MOVEMENT"
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
