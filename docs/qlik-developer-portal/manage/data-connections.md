---
source: https://qlik.dev/manage/data-connections/
last_updated: 2026-05-05T09:59:43+01:00
---

# Overview

In this tutorial series, you are going to learn about data connections, how to create
them, update them, and delete them. You'll also learn how they relate to
other assets in Qlik Cloud, such as Analytics apps, data files, data stores,
data assets, data sets, automation connections and data integration sources
and targets.

## Connections in Qlik Cloud

It is important to know that Qlik Cloud supports multiple types of
connections to data sources, including:

- Qlik Cloud Analytics data connections - used for building Qlik Cloud Analytics apps
- Qlik Talend Data Integration data connections - used for building Qlik Talend Data Integration projects
- Qlik Automate automation connections - used for building Qlik Automate workflows

This tutorial series covers analytics and data integration data connections, which share the same API endpoints for most
connector types.
Because the consumers differ, the examples and follow-on tutorials should be
chosen based on whether you are building analytics apps or data integration
projects.

## Analytics data connections

A Qlik Cloud Analytics data connection refers to a connection established between
your Qlik Cloud tenant and a data source, which can be directly used for sourcing
data for loading into Qlik Sense applications.

Data connections in Qlik Cloud enable the integration of data from a wide range
of systems and databases, such as relational databases, spreadsheets, cloud-based
data sources, web services, [and more](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm).
These connections provide a bridge for
bringing data into Qlik Cloud applications, allowing users to build data models,
create visualizations, and perform data analysis.

Each connection requires connection parameters such as server addresses,
authentication credentials, and other relevant configuration details specific to
the data source. Once configured, these connections can be shared as assets within
spaces, and leveraged by users with appropriate access rights.

To learn more about connectivity to analytics data sources in Qlik Cloud, review
the [Getting started with loading your data guide](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Workflow/workflow.htm)
on Qlik Help.

To learn more about the available connectivity to web-based, web storage, JDBC, ODBC,
REST, Salesforce, and SAP sources, review the full list
at [Qlik Cloud Analytics data sources](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm)
on Qlik Help.

## Data integration data connections

A Qlik Talend Data Integration data connection refers to a connection established to a source or target data service,
which can be used for building data integration projects.

To learn more about the range of data sources and targets available, review the
[Qlik Cloud Data Integration connection help page](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Sources-and-targets.htm).

## API support for data connections

There are several APIs in Qlik Cloud which support the creation and management
of data connections. These are:

- [Data connections](https://qlik.dev/apis/rest/data-connections) - manages
  data connections.
- [Data credentials](https://qlik.dev/apis/rest/data-credentials) - manages
  credentials for data connections.
- [Data sources](https://qlik.dev/apis/rest/data-sources) - provides information
  on the data sources to which data connections can be created.

Data connections and data credentials APIs provide full manageability of
data connections in Qlik Cloud.

## Get started

- [Create data connections](https://qlik.dev/manage/data-connections/create-data-connections) - Learn how to create a new data connection
- [Use interactive auth or separated credentials](https://qlik.dev/manage/data-connections/auth-data-connections) - Learn about the different authentication patterns available when creating connections
- [Leverage Qlik Data Gateway direct access to connect to data](https://qlik.dev/manage/data-connections/gateway-data-connections) - Learn how to connect to data behind your firewall via the direct access gateway
- [Update data connections](https://qlik.dev/manage/data-connections/update-data-connections) - Learn how to update data connections, owners, connections, and space metadata
- [Delete data connections](https://qlik.dev/manage/data-connections/delete-data-connections) - Learn how to delete data connections from Qlik Cloud
