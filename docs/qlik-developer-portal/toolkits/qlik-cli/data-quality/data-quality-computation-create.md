---
source: https://qlik.dev/toolkits/qlik-cli/data-quality/data-quality-computation-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-quality computation create

## qlik data-quality computation create

(Deprecated) Trigger data quality computation

### Synopsis

(Deprecated) Triggers a full data quality computation for a dataset, running profile calculation followed by data quality
assessment. Returns a `computationId` that can be used to track progress via the computation status endpoint
(`GET /data-qualities/computations/{computationId}`). The computation runs asynchronously.
Poll the status endpoint until `status` is `SUCCEEDED` or `FAILED`.

```
qlik data-quality computation create [flags]
```

### Options

```
      --connectionId string    The ID of the connection
      --datasetId string       The ID of the dataset
      --executionMode string   Specifies where the data quality computation takes place. In ˋPUSHDOWNˋ mode, it runs within the Cloud Data Warehouse (e.g., Snowflake, Databricks), whereas in ˋPULLUPˋ mode, it runs in Qlik Cloud.
                               Allowed values: "PUSHDOWN", "PULLUP"
  -f, --file file              Read request body from the specified file
  -h, --help                   help for create
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --retry int              Number of retries to do before failing, max 10
      --sampleMode string      Specifies how the dataset is sampled. ˋABSOLUTEˋ represents a fixed number of rows, while ˋRELATIVEˋ refers to a percentage of the total dataset rows.
                               Allowed values: "ABSOLUTE", "RELATIVE"
      --sampleSize int         The actual value of the selected sampling method size (either a fixed number for ˋABSOLUTEˋ mode or a percentage for ˋRELATIVEˋ mode). Maximum allowed value for ˋABSOLUTEˋ mode is ˋ100000ˋ.
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
