---
source: https://qlik.dev/toolkits/qlik-cli/data-asset/data-asset-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# data-asset update

## qlik data-asset update

Update data asset

### Synopsis

Update data asset.

```
qlik data-asset update <data-assetId> [flags]
```

### Options

```
      --appId string                  
      --appType string                (Required) 
      --dataFreshness string          The date-time when the source data was last changed
      --dataStoreInfo-id string       (Required) 
      --description string            
  -f, --file file                     Read request body from the specified file
  -h, --help                          help for update
      --id string                     Only required when updating the resource. Must be null for new resources.
      --interval int                  Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                   
      --ownerId string                The value is automatically set by the application.
      --properties key:unknown        A Map of name-value pairs.
  -q, --quiet                         Return only IDs from the command
      --raw                           Return original response from server without any processing
      --retry int                     Number of retries to do before failing, max 10
      --spaceId string                
      --tags strings                  
      --technicalDescription string   
      --technicalName string          (Required) 
      --version int                   Only required when updating the resource. Must be null for new resources.
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
