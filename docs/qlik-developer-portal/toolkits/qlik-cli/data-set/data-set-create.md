---
source: https://qlik.dev/toolkits/qlik-cli/data-set/data-set-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-set create

## qlik data-set create

Save new data set

### Synopsis

Save new data set

```
qlik data-set create [flags]
```

### Options

```
      --additionalSchemas-anomalies strings                               Anomalies associated with this schema. Example: $warning-unknown-headers
      --additionalSchemas-dataFields-alias string                         Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-dataType-originalType string         Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-dataType-properties key:unknown      The properties map key is string and the value is of type object. Please note, Datatype DECIMAL requires two mandatory properties to be defined; these properties must be named: precision and scale, each of these property accepts integer value.  All other datatypes does not require any manadatory properties to be defined.
      --additionalSchemas-dataFields-dataType-type string                 Each datatype may vary in terms of required properties. Example: Datatype DECIMAL requires two mandatory properties to be defined - precision and scale, each one accepts integer value. All other datatypes does not have any required properties.
                                                                          Allowed values: "DATE", "TIME", "DATETIME", "TIMESTAMP", "STRING", "DOUBLE", "DECIMAL", "INTEGER", "BOOLEAN", "BINARY", "CUSTOM"
      --additionalSchemas-dataFields-description string                   Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-encrypted                            Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-name string                          Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-nullable                             Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-ordinalPositionInKey int             Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-orphan                               Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-primaryKey                           Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-properties key:unknown               Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-sensitive                            Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-dataFields-tags strings                         An array of system tags
      --additionalSchemas-dataFields-userTags-id string                   The id of the tag in Collections
      --additionalSchemas-dataFields-userTags-name string                 An array of user-supplied tags
      --additionalSchemas-loadOptions key:unknown                         Options for loading files. Example: "qLabel": "embedded labels"
      --additionalSchemas-overrideSchemaAnomalies                         Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --additionalSchemas-schemaName string                               Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --appTypeOverride string                                            Optional override of DataAsset appType.
      --createdByConnectionId string                                      The connectionId that created the Dataset. Optional.
      --dataAssetInfo-dataStoreInfo-id string                             (Required) 
      --dataAssetInfo-id string                                           (Required) 
      --description string                                                
  -f, --file file                                                         Read request body from the specified file
  -h, --help                                                              help for create
      --id string                                                         Only required when updating the resource. Must be null for new resources.
      --interval int                                                      Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                                                       
      --operational-contentUpdated                                        
      --operational-endDate string                                        
      --operational-lastLoadTime string                                   
      --operational-lastUpdateTime string                                 
      --operational-location string                                       
      --operational-logMessage string                                     
      --operational-rowCount int                                          
      --operational-size int                                              
      --operational-startDate string                                      
      --operational-status string                                         
      --operational-tableConnectionInfo-additionalProperties key:string   
      --operational-tableConnectionInfo-selectionScript string            
      --operational-tableConnectionInfo-tableName string                  
      --operational-tableOwner string                                     
      --ownerId string                                                    The value is automatically set by the application.
      --properties key:unknown                                            A Map of name-value pairs.
      --qri string                                                        (Required) NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles.
  -q, --quiet                                                             Return only IDs from the command
      --raw                                                               Return original response from server without any processing
      --retry int                                                         Number of retries to do before failing, max 10
      --schema-anomalies strings                                          Anomalies associated with this schema. Example: $warning-unknown-headers
      --schema-dataFields-alias string                                    Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-dataType-originalType string                    Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-dataType-properties key:unknown                 The properties map key is string and the value is of type object. Please note, Datatype DECIMAL requires two mandatory properties to be defined; these properties must be named: precision and scale, each of these property accepts integer value.  All other datatypes does not require any manadatory properties to be defined.
      --schema-dataFields-dataType-type string                            Each datatype may vary in terms of required properties. Example: Datatype DECIMAL requires two mandatory properties to be defined - precision and scale, each one accepts integer value. All other datatypes does not have any required properties.
                                                                          Allowed values: "DATE", "TIME", "DATETIME", "TIMESTAMP", "STRING", "DOUBLE", "DECIMAL", "INTEGER", "BOOLEAN", "BINARY", "CUSTOM"
      --schema-dataFields-description string                              Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-encrypted                                       Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-name string                                     Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-nullable                                        Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-ordinalPositionInKey int                        Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-orphan                                          Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-primaryKey                                      Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-properties key:unknown                          Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-sensitive                                       Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-dataFields-tags strings                                    An array of system tags
      --schema-dataFields-userTags-id string                              The id of the tag in Collections
      --schema-dataFields-userTags-name string                            An array of user-supplied tags
      --schema-loadOptions key:unknown                                    Options for loading files. Example: "qLabel": "embedded labels"
      --schema-overrideSchemaAnomalies                                    Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --schema-schemaName string                                          Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema
      --secureQri string                                                  (Required) 
      --spaceId string                                                    
      --tags strings                                                      
      --technicalDescription string                                       
      --technicalName string                                              (Required) 
      --type string                                                       
      --version int                                                       Only required when updating the resource. Must be null for new resources.
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
