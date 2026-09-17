---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-configuration-patch/
last_updated: 2026-06-03T09:30:31+02:00
---

# direct-access-agent configuration patch

## qlik direct-access-agent configuration patch

Update agent configuration

### Synopsis

Makes changes to the local agent configuration using JSON Patch. Requestor must be assigned the `TenantAdmin` role and needs to be either a Gateway's space owner or a member in the Gateway's space with `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

```
qlik direct-access-agent configuration patch <direct-access-agentId> [flags]
```

### Options

```
  -f, --file file      Read request body from the specified file
  -h, --help           help for patch
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --op string      
                       Allowed values: "add", "replace", "remove"
      --path string    
                       Allowed values: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES"
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --value string   
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
