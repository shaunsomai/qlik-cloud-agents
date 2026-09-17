---
source: https://qlik.dev/manage/data-files/
last_updated: 2026-04-20T13:34:03+01:00
---

# Overview

In this tutorial series, you are going to learn about data files, how to create
them, update them, and delete them in bulk. You'll also learn how they relate to
other assets in Qlik Cloud, such as Analytics apps, data connections, data stores,
data assets, and data sets.

## What is a data file?

Qlik Cloud allows you to upload or create certain file types for storing data within
spaces. These files will appear in the `DataFiles` data connection when using the
data load editor or data manager, and will also appear in the Cloud Hub catalog.
For more information on data files, see [Adding data from uploaded data files](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data-datafiles.htm)
on Qlik Help.

Data files can be loaded into Analytics apps within Qlik Cloud via the `DataFiles`
data connection in a space.

## What is a data connection?

Data connections are assets that you can create in spaces to provide connectivity
to data sources. With respect to data files, each space is automatically provisioned
with a data connection called `DataFiles`, which is the sole repository in that
space for uploading data in file format. All other types of data source
connectivity can be created when required. For more information,
see [Data sources in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm)
on Qlik Help.

## Data stores, data assets, data sets, and data files

Data files are flat files (with formats such as CSV, QVD, TXT, XLSX) that are
uploaded or created within Qlik Cloud. When a data file is created or updated,
several other pieces of metadata are created in other Qlik Cloud services to
help catalog and make this data more accessible to users.

- **Data stores** - by default, a single data store is provisioned on a tenant, which
  contains all data files in all spaces, with the name `DataFilesStore`
  - **Data assets** - each space creates a corresponding data asset under the
    `DataFilesStore` data store. A data store can have multiple data assets.
    - **Data sets** - each data file uploaded or created on the tenant creates a
      corresponding data set. If the data file is a supported format, this data
      set will contain metadata about the fields and properties from the data file.
      A data asset can have multiple data sets.

To learn more about interacting with data in the Qlik Cloud Catalog, review
the [Get started with Catalog integration guide](https://qlik.dev/manage/data-governance/get-started-catalog).

## What happens when you upload a data file?

Uploading a new data file results in the creation of a new data file resource,
either in a shared or managed space if a valid connection ID is provided, or in
your personal space if not.

The system will also create a data set resource, linked to the corresponding
data asset and data store. For compatible file sources, the catalog stores
the field and object metadata in the data set, and this will be visible in the
catalog in the Qlik Cloud Hub.

When you delete a data file, the corresponding data set is also removed. If you
delete a data set, it does not delete the corresponding data file.

## Supported data file formats

Most common flat file formats such as CSV, XLSX, TXT, and QVD are supported. For
the full list of supported file formats, see [Adding and managing your analytics data](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-data-resources-spaces.htm)
on Qlik Help.

## Get started

- [Create data files](https://qlik.dev/manage/data-files/create-datafiles) - Learn how to upload, create, and copy data files
- [Update data files](https://qlik.dev/manage/data-files/update-datafiles) - Learn how to update data files, owners, connections & space metadata
- [Delete data files](https://qlik.dev/manage/data-files/delete-datafiles) - Learn how to delete data files from Qlik Cloud
