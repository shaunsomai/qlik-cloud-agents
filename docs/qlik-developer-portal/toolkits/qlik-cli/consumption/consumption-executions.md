---
source: https://qlik.dev/toolkits/qlik-cli/consumption/consumption-executions/
last_updated: 2025-06-18T09:34:47+02:00
---

# consumption executions

## qlik consumption executions

Retrieves the list of executions on an specific tenant

### Synopsis

Retrieves the list of executions on an specific tenant

```
qlik consumption executions [flags]
```

### Options

```
      --actionToBlock string       
      --filter string              The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax.
                                   
                                   example ˋtaskName eq "automation_run_ended" or taskName eq "report_triggered" or or taskName eq "dataVolumeAggregated"ˋ
                                   
                                   The following fields are supported: ˋscopeˋ, ˋresourcetypeˋ, ˋresourceactionˋ, ˋresourceidˋ, ˋcapacitylimitˋ,
                                   ˋlocalusageˋ, ˋglobalusageˋ, ˋoverageˋ, ˋblockedˋ, ˋperiodstartˋ, ˋperiodendˋ, ˋconsumptionreportidˋ, ˋblockedeventtimeˋ,
                                   ˋoverageeventtimeˋ, ˋtasknameˋ, ˋtaskdescriptionˋ, ˋuseridˋ, ˋtenantidˋ, ˋcustomerfacingˋ, ˋactiontoblockˋ
  -h, --help                       help for executions
      --interval int               Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                  Limit the returned result set
      --offset int                 Offset for pagination - how many elements to skip
      --page string                The cursor to the page of data.
      --periodsToInclude strings   Specifies which periods to include regardless of the period type, start and end specified
                                   Allowed values: "current", "previous"
  -q, --quiet                      Return only IDs from the command
      --raw                        Return original response from server without any processing
      --retry int                  Number of retries to do before failing, max 10
      --sort strings               
                                   Allowed values: "periodstart", "-periodstart", "+periodstart", "periodend", "-periodend", "+periodend"
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
