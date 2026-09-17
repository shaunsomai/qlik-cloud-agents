---
source: https://qlik.dev/manage/di-projects/di-connectors-reference/
last_updated: 2026-02-26T11:12:20+01:00
---

# Data integration connectors reference

A Qlik Talend Data Integration data connection refers to a connection established to a source or target data service,
which can be used for building data integration projects.

You can use the Data Connections, Data Sources, and Data Credentials APIs to programmatically create and manage data
connections for data integration projects. To do this, you must reference the correct `dataSourceId` value for each
connector type.

This reference lists all supported data integration connectors and their corresponding identifiers.

## Understanding connector types

Data integration supports two types of connectors:

- **Source connectors** (`repsrc_` prefix): Extract data from source
  systems
- **Target connectors** (`reptgt_` prefix): Load data into target systems

Some systems (such as Microsoft SQL Server and MySQL) have both source
and target connector variants to support different use cases.

## Supported connectors

Use the `dataSourceId` values from this table when creating data
connections for Data Integration projects via the APIs.

### Sources

| Connector                                  | dataSourceId              | Type   |
| ------------------------------------------ | ------------------------- | ------ |
| IBM DB2 for iSeries                        | `repsrc_db2iseries`       | Source |
| IBM DB2 for LUW                            | `repsrc_db2luw`           | Source |
| IBM DB2 for z/OS                           | `repsrc_db2zos`           | Source |
| Microsoft SQL Server (log based)           | `repsrc_mssql`            | Source |
| Microsoft SQL Server (Microsoft CDC based) | `repsrc_azuresqlmscdc`    | Source |
| MySQL (source)                             | `repsrc_mysql`            | Source |
| Oracle (source)                            | `repsrc_oracle`           | Source |
| PostgreSQL (source)                        | `repsrc_postgresql`       | Source |
| SAP Application Server                     | `repsrc_sapdbapplication` | Source |
| SAP Extractor                              | `repsrc_sapextractor`     | Source |
| SAP HANA (Database)                        | `repsrc_saphana`          | Source |
| SAP ODP                                    | `repsrc_sapodp`           | Source |

### Targets

| Connector               | dataSourceId                   | Type   |
| ----------------------- | ------------------------------ | ------ |
| Amazon Redshift         | `reptgt_qdiredshift`           | Target |
| Amazon S3               | `reptgt_qdis3`                 | Target |
| Azure Data Lake Storage | `reptgt_qdiadls`               | Target |
| Azure Synapse Analytics | `reptgt_qdisynapse`            | Target |
| Databricks              | `reptgt_qdidatabricks`         | Target |
| Google BigQuery         | `reptgt_qdibigquery`           | Target |
| Google Cloud Storage    | `reptgt_qdigooglecloudstorage` | Target |
| Microsoft Fabric        | `reptgt_qdimicrosoftfabric`    | Target |
| Microsoft SQL Server    | `reptgt_mssqltarget`           | Target |
| MySQL (target)          | `reptgt_qdimysql`              | Target |
| Oracle (target)         | `reptgt_qdioracle`             | Target |
| PostgreSQL (target)     | `reptgt_qdipostgresql`         | Target |
| Snowflake               | `reptgt_qdisnowflake`          | Target |

## Using dataSourceId in API calls

When creating a data connection for a data integration project, pass
the `dataSourceId` to the Data Connections API:

```bash
curl -X POST "https://<TENANT>/api/v1/data-connections" ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"dataSourceId\": \"<DATA_SOURCE_ID>\",
    \"qName\": \"<CONNECTION_NAME>\",
    \"space\": \"<SPACE_ID>\",
    \"connectionProperties\": {
      // Connector-specific properties here
    }
  }"
```

> **Use only documented connectors:** Although other connectors may be available, only the ones documented on this page should be used with data integration
> projects.

## Related documentation

- [Deploy a data integration project](https://qlik.dev/manage/di-projects/deploy-di-project):
  Step-by-step workflow for exporting and importing projects
- [Data Connections API reference](https://qlik.dev/apis/rest/data-connections/): Full API
  documentation
- [Data Sources API reference](https://qlik.dev/apis/rest/data-sources/): List available data
  sources for your tenant
- [Data Credentials API reference](https://qlik.dev/apis/rest/data-credentials/): Manage
  credentials for connections
