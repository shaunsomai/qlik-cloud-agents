---
source: https://qlik.dev/manage/data-governance/get-started-catalog/
last_updated: 2026-08-19T17:28:45+02:00
---

# Get started with Catalog integration

## Introduction

This tutorial is going to teach you how to use the Catalog API to create properties,
data stores, data assets and data sets to store metadata information for Qlik Sense.

The Catalog API allows Qlik Sense to keep track of various Qlik Sense applications.
The Catalog API works with the profile service, the lineage service, the qix-datafiles service
and the apps service. Support for more Qlik Sense applications is currently under development.

This tutorial shows you how to converse with the API through a series of requests.
Postman is used to send the API requests.

## Prerequisites

1. Download and install [Postman](https://getpostman.com).

2. An access token or API key. For more information, see [Authentication](https://qlik.dev/authenticate).

## Catalog API endpoint

Connections to the Catalog API endpoint are made using
HTTPS by default. When communicating with the Catalog API, the URL has
the following form:
`{URL}/api/v1/data-sets`
where \{URL} is your tenant URL.

The following API endpoints are also available:
`{URL}/api/v1/data-stores`
`{URL}/api/v1/data-assets`
`{URL}/api/v1/properties`

For the sake of this tutorial, the data-sets endpoint will be used as an example.

## API usage examples

### Set up Postman

1. Start Postman.

2. Set the HTTP method to POST.

3. Enter the following path in the URL area:
   `{URL}/api/v1/data-sets`
   The full URL should look something like: `https://your-tenant.us.qlikcloud.com/api/v1/data-sets`.

4. Select `Headers` and add `Content-Type` as the key with `application/json`
   as the value. The following examples show how to access the Catalog API
   using Postman. Before making API requests, add your access token as a Bearer Token to
   Postman.

### Explaining the relationship between data sets, data assets and data stores

Catalog stores metadata and the capabilities built around it continue to expand.
One of its main features is a way to store metadata in multiple different levels.
The way it is organized is that you can have multiple data assets within a data store.
You can have multiple data sets within a data asset. And having it organized this way
allows flexibility on how you define your metadata.

### Creating a data set

This example shows how to engage the API create a new data-set

1. In the body of the request, set the expected value for the POST request.
   Here is an example of the bare minimum requirement for the data-sets API endpoint:

```json
{
  "technicalName": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "dataAssetInfo": {
    "id": "620fa314b6348d39e499d3bf",
    "name": "Personal"
  },
  "qri": "qdf:qix-datafiles:gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa:uid@620f9fda2174e7ce4588894d:qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "secureQri": "qri:qdf:user://4TEVh68AnPt7GTfK2wy0Nsk7O074qk4z99PzfU0Gu54#OniPiaVLeXxqodbC_SBYngr_HdDVfABvg2vUafGtYwA"
}
```

1. Here is another example with other fields that you might want to include:

```json
{
  "name": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "description": "",
  "technicalDescription": "",
  "technicalName": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "spaceId": "620ff5558666515313e6570d",
  "dataAssetInfo": {
    "id": "620fa314b6348d39e499d3bf",
    "name": "Personal",
    "dataStoreInfo": {
      "id": "620fa314b6348d39e499d3b8",
      "name": "DataFilesStore",
      "type": "qix-datafiles"
    }
  },
  "qri": "qdf:qix-datafiles:gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa:uid@620f9fda2174e7ce4588894d:qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "secureQri": "qri:qdf:user://4TEVh68AnPt7GTfK2wy0Nsk7O074qk4z99PzfU0Gu54#OniPiaVLeXxqodbC_SBYngr_HdDVfABvg2vUafGtYwA",
  "type": "xlsx"
}
```

It is important to note that when entering the `spaceId`, it must refer to an existing
space or it can be removed to default to your personal space. If you want to find the
space ID of other existing spaces, you can call the spaces API.

1. Click `Send`. The JSON response from the API should look something like this for the second example:

   ```json
   {
     "id": "620ff588c4eef203278dce16",
     "name": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
     "description": "",
     "tenantId": "gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa",
     "spaceId": "620ff5558666515313e6570d",
     "ownerId": "620f9fda2174e7ce4588894d",
     "createdTime": "2022-02-18T19:37:44.855Z",
     "createdBy": "620f9fda2174e7ce4588894d",
     "lastModifiedTime": "2022-02-18T19:37:44.855Z",
     "lastModifiedBy": "620f9fda2174e7ce4588894d",
     "version": 0,
     "technicalDescription": "",
     "technicalName": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
     "dataAssetInfo": {
       "id": "620fa314b6348d39e499d3bf",
       "name": "Personal",
       "dataStoreInfo": {
         "id": "620fa314b6348d39e499d3b8",
         "name": "DataFilesStore",
         "type": "qix-datafiles"
       }
     },
     "qri": "qdf:qix-datafiles:gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa:uid@620f9fda2174e7ce4588894d:qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
     "secureQri": "qri:qdf:user://4TEVh68AnPt7GTfK2wy0Nsk7O074qk4z99PzfU0Gu54#OniPiaVLeXxqodbC_SBYngr_HdDVfABvg2vUafGtYwA",
     "type": "xlsx"
   }
   ```

   Using this response, you can keep track of the ID to be reused for executing PUT & PATCH requests.

### Updating a data set

This example shows how to engage the API to update an existing data set.

1. Here is an example of a PUT request:

```json
{
  "id": "620ff588c4eef203278dce16",
  "name": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "description": "",
  "tenantId": "gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa",
  "spaceId": "620ff5558666515313e6570d",
  "createdTime": "2022-02-18T19:37:44.855Z",
  "createdBy": "620f9fda2174e7ce4588894d",
  "lastModifiedTime": "2022-02-18T19:37:44.855Z",
  "lastModifiedBy": "620f9fda2174e7ce4588894d",
  "version": 0,
  "technicalDescription": "",
  "technicalName": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "dataAssetInfo": {
    "id": "620fa314b6348d39e499d3bf",
    "name": "Personal",
    "dataStoreInfo": {
      "id": "620fa314b6348d39e499d3b8",
      "name": "DataFilesStore",
      "type": "qix-datafiles"
    }
  },
  "qri": "qdf:qix-datafiles:gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa:uid@620f9fda2174e7ce4588894d:qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "secureQri": "qri:qdf:user://4TEVh68AnPt7GTfK2wy0Nsk7O074qk4z99PzfU0Gu54#OniPiaVLeXxqodbC_SBYngr_HdDVfABvg2vUafGtYwA",
  "type": "xlsx"
}
```

Similarly to the POST request, it is important to note that when entering the `spaceId`,
it must refer to an existing space or it can be removed to default to your personal
space. If you want to find the space ID of other existing spaces, you can call the spaces API.
You can also do the same with the `ownerId`. You can use the users API to get any `userId` if
there is a need to change the `ownerId` of a data set.

1. Click `Send`. The JSON response from the API should look something like this:

```json
{
  "id": "620ff588c4eef203278dce16",
  "name": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "description": "",
  "tenantId": "gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa",
  "spaceId": "620ff5558666515313e6570d",
  "createdTime": "2022-02-18T19:37:44.855Z",
  "createdBy": "620f9fda2174e7ce4588894d",
  "lastModifiedTime": "2022-02-18T20:35:14.394Z",
  "lastModifiedBy": "620f9fda2174e7ce4588894d",
  "version": 1,
  "technicalDescription": "",
  "technicalName": "qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "dataAssetInfo": {
    "id": "620fa314b6348d39e499d3bf",
    "name": "Personal",
    "dataStoreInfo": {
      "id": "620fa314b6348d39e499d3b8",
      "name": "DataFilesStore",
      "type": "qix-datafiles"
    }
  },
  "qri": "qdf:qix-datafiles:gOeaTFZJ0HghbJ7NqK6pyaM_aQ9JlwLa:uid@620f9fda2174e7ce4588894d:qix- xlsx-2022-02-18-kzsgt9z1.xlsx",
  "secureQri": "qri:qdf:user://4TEVh68AnPt7GTfK2wy0Nsk7O074qk4z99PzfU0Gu54#OniPiaVLeXxqodbC_SBYngr_HdDVfABvg2vUafGtYwA",
  "type": "xlsx"
}
```

### Patching a data-set

1. Here is an example of a PATCH request:

```json
[
  {
    "op": "add",
    "path": "/field",
    "value": "value"
  }
]
```

With the Patch request, you can decide to add or replace fields and set their values without
passing the entire body of the catalog.

You can find all the different ways to use the Patch request in the link below
[Using JSON Patch in Spring REST](https://www.baeldung.com/spring-rest-json-patch)

### Field alias uniqueness validation

A data set schema contains a `dataFields` array. Each field has a `name` and can define an optional `alias`, for
example:

```json
{
  "schema": {
    "dataFields": [{ "name": "CustomerEmail", "alias": "Email" }]
  }
}
```

When you create a data set with `POST /data-sets`, or update one with
`PUT /data-sets/{data-set-id}` or `PATCH /data-sets/{data-set-id}`,
the API validates the aliases within each schema.
The same validation applies to schemas in `additionalSchemas`.

The following rules apply:

- An alias can't be the same as the name of another field in the same schema.
- An alias must be unique among the aliases in the same schema.

If either rule is violated, the request returns a `400 Bad Request` response.

For example, the following `PATCH` request fails if `Email` is already used as another field's name or alias in the same
schema:

```json
[
  {
    "op": "add",
    "path": "/schema/dataFields/2/alias",
    "value": "Email"
  }
]
```

> **Tip:** Validate alias values against the other field names and aliases in the same schema before sending the request.

### Deleting data-set, data-asset and data-stores

1. Here is an example of a batch DELETE request:

```json
{
  "ids": ["ids"]
}
```

There are considerable differences between deleting a data set, data asset and data store.
When deleting a data asset, it will delete all child data sets that are linked to the data asset.
When attempting to delete a data store, it will first verify that there is no existing data asset
for that data store. There is no special behavior for deleting data sets; they can be deleted and
won't have any unexpected results.

## Conclusion

All of the previous actions can be done with data sets, data assets and data stores.
You can refer to the API reference to see what fields are accepted.
