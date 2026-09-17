---
source: https://qlik.dev/manage/data-governance/create-data-product/
last_updated: 2026-04-20T13:34:03+01:00
---

# Create and activate a data product

In this tutorial, you'll learn how to create and activate a data product using the [Data Products API](https://qlik.dev/apis/rest/data-governance/data-products).
You'll configure datasets, metadata, and governance contacts to make it consumable by business users.

A data product is a curated collection of datasets, metadata, and governance information that makes data discoverable
and consumable for business users. By grouping related datasets with clear ownership and documentation, data products
simplify data discovery and ensure consistent, high-quality information across your organization.

## Overview

The example scenario is a Sales data product that groups datasets related to customer transactions, revenue, and
performance metrics:

- You create the data product in your space as an empty container.
- You add datasets to the product using the update endpoint.
- You configure product metadata (name, description, tags, and key contacts).
- You activate the product, making it discoverable in the data marketplace.

## What you'll learn

In this tutorial, you'll learn:

- How to create an empty data product in a space
- How to add datasets to your data product
- How to configure product metadata and governance details
- How to activate a data product for consumption
- How to verify the activation status
- How to activate API endpoints for OData consumption
- How to export product documentation

## Prerequisites

- You have access to a Qlik Cloud tenant with at least one managed space.
  You can only activate data products in managed spaces.
- You have created and published datasets that you want to group into a data product.
- An access token or API key with sufficient [data product management permissions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes-capacity-model.htm),
  see [Authentication](https://qlik.dev/authenticate).
- You know the IDs of the datasets you want to add to your data product.

> **Note:** Replace everything in `<angle brackets>` or `{curly braces}` with your own values.
> For example, replace `<TENANT>` with your tenant name.

## Before you begin

You need the space ID and user IDs for key contacts before creating your data product.

### Get the space ID

First, identify the personal, shared, or data space where you want to create the data product:

```bash
curl -X GET "https://<TENANT>/api/v1/spaces" \
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
[
    {
        "id": "a1b2c3d4e5f6g7h8i9j0k1l2",
        "name": "Sales Analytics - Development",
        "description": "Space for developing sales data products and analytics",
        "type": "shared",
        "createdAt": "2025-01-15T10:30:00Z",
        "updatedAt": "2025-01-15T10:30:00Z"
    },
    {
        "id": "693c3b29ddb4de1c3954133d",
        "name": "Sales Analytics",
        "description": "Sales data products and analytics",
        "type": "managed",
        "createdAt": "2025-01-15T10:30:00Z",
        "updatedAt": "2025-01-15T10:30:00Z"
    },
    ...
]
```

Copy the `id` of the personal, shared, or data space where you want to create your data product.
You will need a managed space for the activation step later.

### Get user IDs for key contacts

Before configuring governance contacts, retrieve the user IDs for the users you want to assign as key contacts:

```bash
curl -X GET "https://<TENANT>/api/v1/users" \
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
[
    {
        "id": "6909d8524392dbbab822c7f7",
        "name": "John Smith",
        "email": "john.smith@example.com",
        "status": "active",
        "tenantId": "uYP0lh4-BlTdFa3QoJ2JN5vzXmNbkQSu"
    },
    {
        "id": "6b7c8d9e0f1a2b3c4d5e6f7g",
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "status": "active",
        "tenantId": "uYP0lh4-BlTdFa3QoJ2JN5vzXmNbkQSu"
    },
    ...
]
```

Copy the `id` values for the users you want to assign as key contacts.

> **Note:** Each user can only be assigned once as a key contact in a data product (one role per user).

## Step 1: Create an empty data product

Initialize a new data product as a container for datasets in the desired space:

```bash
curl -X POST "https://<TENANT>/api/data-governance/data-products" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"<DATA_PRODUCT_NAME>\",
    \"description\": \"<DATA_PRODUCT_DESCRIPTION>\",
    \"spaceId\": \"<SPACE_ID>\",
    \"readMe\": \"<README_CONTENT>\"
  }"
```

Example request for a Sales data product:

```bash
curl -X POST "https://<TENANT>/api/data-governance/data-products" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"Sales Analytics Data Product\",
    \"description\": \"Comprehensive sales data product grouping customer transactions, revenue metrics, and performance analytics\",
    \"spaceId\": \"a1b2c3d4e5f6g7h8i9j0k1l2\",
    \"readMe\": \"The Sales Analytics Data Product contains curated sales datasets for analysis and reporting.\"
  }"
```

Example response:

```json
{
    "id": "p1q2r3s4t5u6v7w8x9y0z1a2",
    "tenantId": "uYP0lh4-BlTdFa3QoJ2JN5vzXmNbkQSu",
    "spaceId": "a1b2c3d4e5f6g7h8i9j0k1l2",
    "name": "Sales Analytics Data Product",
    "description": "Comprehensive sales data product grouping customer transactions, revenue metrics, and performance analytics",
    "datasetIds": [],
    "apiConsumableDatasetIds": [],
    "glossaryIds": [],
    "createdAt": "2025-12-26T14:25:00Z",
    "createdBy": "6909d8524392dbbab822c7f7",
    "updatedAt": "2025-12-26T14:25:00Z",
    "updatedBy": "6909d8524392dbbab822c7f7",
    "ownerId": "6909d8524392dbbab822c7f7",
    "readMe": "The Sales Analytics Data Product contains curated sales datasets for analysis and reporting.",
    "qri": "qri:data-product://p1q2r3s4t5u6v7w8x9y0z1a2",
    "keyContacts": [],
    "tags": [],
    "activated": false,
    "activatedOn": []
}
```

Copy the `id` field from the response. You will use this ID in the remaining steps.

> **Tip:** The `readMe` field supports Markdown format. Use it to provide comprehensive documentation about your data product's purpose, contents, and usage guidelines.

## Step 2: Add datasets to your data product

Update the data product to add datasets using a replace operation.
This operation replaces the entire dataset list, so you must include all datasets you want the data product to contain,
not just the new ones.

```bash
curl -X PATCH "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "[
    {
      \"op\": \"replace\",
      \"path\": \"/datasetIds\",
      \"value\": [\"<DATASET_ID_1>\", \"<DATASET_ID_2>\", \"<DATASET_ID_3>\"]
    }
  ]"
```

Example request adding sales datasets:

```bash
curl -X PATCH "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "[
    {
      \"op\": \"replace\",
      \"path\": \"/datasetIds\",
      \"value\": [\"6672d8b7a182224cbb3f1c26\", \"6689g7h8i9j0k1l2m3n4o5p6\", \"6a7b8c9d0e1f2g3h4i5j6k7l\"]
    }
  ]"
```

If successful, you receive a `204 No Content` response.

> **Note:** Pass all datasets you want to include as an array in the value field.\
> The replace operation sets the complete dataset list for the product.

## Step 3: (Optional) Configure key contacts and quality metadata

Add key contacts to your data product for governance and support using a replace operation.
Include all key contacts you want assigned, as this operation replaces the entire contact list.

> **Warning:** Each user ID can only appear once in the keyContacts array.
> You cannot assign multiple roles to the same user.

```bash
curl -X PATCH "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "[
    {
      \"op\": \"replace\",
      \"path\": \"/keyContacts\",
      \"value\": [
        {
          \"userId\": \"<USER_ID_1>\",
          \"role\": \"owner\"
        },
        {
          \"userId\": \"<USER_ID_2>\",
          \"role\": \"steward\"
        }
      ]
    }
  ]"
```

Example request:

```bash
curl -X PATCH "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "[
    {
      \"op\": \"replace\",
      \"path\": \"/keyContacts\",
      \"value\": [
        {
          \"userId\": \"6909d8524392dbbab822c7f7\",
          \"role\": \"owner\"
        },
        {
          \"userId\": \"6b7c8d9e0f1a2b3c4d5e6f7g\",
          \"role\": \"steward\"
        }
      ]
    }
  ]"
```

If successful, you receive a `204 No Content` response.

> **Tip:** Key contacts clarify ownership and support responsibilities.
> Use the owner role for primary contact and steward role for data governance leads.

## Step 4: Verify the product configuration

Retrieve your data product to verify all configuration changes:

```bash
curl -X GET "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>" \
  -H "Authorization: Bearer <API_KEY>"
```

Example response:

```json
{
    "id": "p1q2r3s4t5u6v7w8x9y0z1a2",
    "name": "Sales Analytics Data Product",
    "description": "Comprehensive sales data product grouping customer transactions, revenue metrics, and performance analytics",
    "spaceId": "a1b2c3d4e5f6g7h8i9j0k1l2",
    "tags": ["sales", "analytics", "revenue"],
    "readMe": "# Sales Analytics Data Product\n\nThis product contains curated sales datasets for analysis and reporting.",
    "ownerId": "6909d8524392dbbab822c7f7",
    "tenantId": "uYP0lh4-BlTdFa3QoJ2JN5vzXmNbkQSu",
    "activated": false,
    "createdAt": "2025-12-26T14:25:00Z",
    "createdBy": "6909d8524392dbbab822c7f7",
    "updatedAt": "2025-12-26T14:35:00Z",
    "updatedBy": "6909d8524392dbbab822c7f7",
    "datasetIds": [
        "6672d8b7a182224cbb3f1c26",
        "6689g7h8i9j0k1l2m3n4o5p6",
        "6a7b8c9d0e1f2g3h4i5j6k7l"
    ],
    "keyContacts": [
        {
            "userId": "6909d8524392dbbab822c7f7",
            "role": "owner"
        },
        {
            "userId": "6b7c8d9e0f1a2b3c4d5e6f7g",
            "role": "steward"
        }
    ]
}
```

Verify that `datasetIds` contains all the datasets you added and `keyContacts` includes your governance team.

## Step 5: Activate the data product

To make the certified and trusted data products available more widely to your organization, including analytics
consumers, they need to be activated on the Data marketplace.

Activate your data product to deploy it to a managed space and make it discoverable and consumable
by users with the `Can consume data product` permission and at least `View` role in the managed space:

> **Warning:** Data products can only be activated in managed spaces.

```bash
curl -X POST "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>/actions/activate" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"<DATA_PRODUCT_NAME>\",
    \"spaceId\": \"<SPACE_ID>\"
  }"
```

Example request:

```bash
curl -X POST "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2/actions/activate" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"Sales Analytics\",
    \"spaceId\": \"693c3b29ddb4de1c3954133d\"
  }"
```

<details>
  <summary>
    Example response:
  </summary>

  ```json
  {
      "id": "p1q2r3s4t5u6v7w8x9y0z1a2",
      "tenantId": "uYP0lh4-BlTdFa3QoJ2JN5vzXmNbkQSu",
      "spaceId": "693c3b29ddb4de1c3954133d",
      "name": "Sales Analytics Data Product",
      "datasetIds": [
          "6672d8b7a182224cbb3f1c26",
          "6689g7h8i9j0k1l2m3n4o5p6",
          "6a7b8c9d0e1f2g3h4i5j6k7l"
      ],
      "apiConsumableDatasetIds": [],
      "glossaryIds": [],
      "createdAt": "2025-12-26T14:25:00Z",
      "createdBy": "6909d8524392dbbab822c7f7",
      "updatedAt": "2025-12-26T14:35:00Z",
      "updatedBy": "6909d8524392dbbab822c7f7",
      "ownerId": "6909d8524392dbbab822c7f7",
      "qri": "qri:data-product://p1q2r3s4t5u6v7w8x9y0z1a2",
      "keyContacts": [
          {
              "userId": "6909d8524392dbbab822c7f7",
              "role": "owner"
          },
          {
              "userId": "6b7c8d9e0f1a2b3c4d5e6f7g",
              "role": "steward"
          }
      ],
      "tags": [],
      "activated": true,
      "activatedOn": [
          "693c3b29ddb4de1c3954133d"
      ],
      "activatedAt": "2025-12-26T14:35:00Z",
      "quality": {
          "validity": 100.0,
          "completeness": 100.0
      },
      "trustScore": {
          "score": 85.29412,
          "applicableDatasets": 1,
          "dimensions": [
              {
                  "id": "USAGE",
                  "score": 0.0,
                  "applicableDatasets": 1
              },
              {
                  "id": "DIVERSITY",
                  "score": 50.0,
                  "applicableDatasets": 1
              },
              {
                  "id": "COMPLETENESS",
                  "score": 100.0,
                  "applicableDatasets": 1
              },
              {
                  "id": "VALIDITY",
                  "score": 100.0,
                  "applicableDatasets": 1
              },
              {
                  "id": "DISCOVERABILITY",
                  "score": 0.0,
                  "applicableDatasets": 1
              },
              {
                  "id": "TIMELINESS",
                  "applicableDatasets": 0
              },
              {
                  "id": "ACCURACY",
                  "applicableDatasets": 0
              }
          ]
      }
  }
  ```
</details>

Notice that `activated` is now `true` and `activatedAt` shows the activation timestamp.

The response also includes a `trustScore` object that evaluates data quality across multiple dimensions.
For more information about trust scores and data quality metrics, see [Understanding Qlik Trust Score](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Qlik-Trust-score.htm)
on Qlik Help.

> **Warning:** Once activated, your data product is visible in the data marketplace.\
> Only activate products that are fully configured and ready for consumption by business users.

## Step 6: (Optional) Activate the API endpoints

You can activate API endpoints to query, filter, and consume data from your data products across tools and ecosystems.
Once the endpoints are activated, you can access your data through OData-compliant APIs.

Update the data product to mark datasets as queryable via OData-compliant APIs, using a replace operation.
In the replace operation, specify all datasets you want to make API-consumable.

> **Note:** You can only designate datasets that are already included in your data product's `datasetIds` array as API-consumable.

Example request:

```bash
curl -X PATCH "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "[
    {
      \"op\": \"replace\",
      \"path\": \"/apiConsumableDatasetIds\",
      \"value\": [\"<DATASET_ID_1>\", \"<DATASET_ID_2>\", \"<DATASET_ID_3>\"]
    }
  ]"
```

If successful, you receive a `204 No Content` response.

API endpoints are enabled for the datasets you designate in this step. These endpoints become available in the active
marketplace version once the [data product is activated](#step-5-activate-the-data-product).

For more information about OData, see the [Microsoft documentation](https://learn.microsoft.com/en-us/odata/).

## Step 7: (Optional) Export product documentation

You can export documentation of your activated product for sharing or archiving:

```bash
curl -X GET "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>/actions/export-documentation" \
  -H "Authorization: Bearer <API_KEY>" \
  -o "<FILE_NAME>.md"
```

<details>
  <summary>
    Example response:
  </summary>

  ```md
  # Sales Analytics Data Product
  ## Readme
  The Sales Analytics Data Product contains curated sales datasets for analysis and reporting.

  ## Key contacts
  | Name | Role |
  |------|------|
  | John Smith | owner |
  | Jane Doe | steward |

  ## Metadata
  Modified: 2025-12-26T14:40:00Z  
  Created: 2025-12-26T14:25:00Z  
  Space: Sales Analytics  
  Modified by: John Smith  
  Creator: John Smith  
  Owner: John Smith  

  ## Data Quality
  Validity: 100%  
  Completeness: 100%

  ## Datasets (3)
  ## Customer Transactions

  ### Metadata
  Profile refreshed: 2025-12-26T14:32:00Z  
  Modified: 2025-12-26T14:32:00Z  
  Created: 2025-06-19T13:10:14Z  
  Number of rows: 52,847  
  Number of fields: 8  
  Size: 12.4 MiB  

  ### Data quality
  Trust score: 4.3/5  
  Valid: 100%  
  Invalid: 0%  
  Empty: 0%  

  ## Revenue Metrics

  ### Metadata
  Profile refreshed: 2025-12-26T14:32:00Z  
  Modified: 2025-12-26T14:32:00Z  
  Created: 2025-06-20T10:15:30Z  
  Number of rows: 18,392  
  Number of fields: 6  
  Size: 5.8 MiB  

  ### Data quality
  Trust score: 4.2/5  
  Valid: 100%  
  Invalid: 0%  
  Empty: 0%  

  ## Performance Analytics

  ### Metadata
  Profile refreshed: 2025-12-26T14:32:00Z  
  Modified: 2025-12-26T14:32:00Z  
  Created: 2025-06-21T09:45:20Z  
  Number of rows: 31,256  
  Number of fields: 12  
  Size: 8.9 MiB  

  ### Data quality
  Trust score: 4.4/5  
  Valid: 100%  
  Invalid: 0%  
  Empty: 0%  
  ```
</details>

This Markdown file contains your data product's complete documentation, metadata, key contacts, and dataset information
that can be shared with stakeholders or archived for compliance.

## Step 8: (Optional) Monitor changes with changelog

Track all changes made to your data product:

```bash
curl -X GET "https://<TENANT>/api/data-governance/data-products/<DATA_PRODUCT_ID>/changelogs" \
  -H "Authorization: Bearer <API_KEY>"
```

<details>
  <summary>
    Example response:
  </summary>

  ```json
  {
      "data": [
          {
              "id": "694e8c78cb095e700317789d",
              "changes": [
                  {
                      "path": "/name",
                      "operator": "replace",
                      "value": "Sales Analytics Data Product"
                  },
                  {
                      "path": "/description",
                      "operator": "remove",
                      "value": null
                  },
                  {
                      "path": "/activatedOn",
                      "operator": "add",
                      "value": [
                          "693c3b29ddb4de1c3954133d"
                      ]
                  }
              ],
              "createdAt": "2025-12-26T14:40:00Z",
              "createdBy": "6909d8524392dbbab822c7f7"
          },

          {
              "id": "694e6b98717625a4a940645b",
              "changes": [
                  {
                      "path": "/keyContacts",
                      "operator": "add",
                      "value": [
                          {
                              "userId": "6909d8524392dbbab822c7f7",
                              "role": "owner"
                          },
                          {
                              "userId": "6b7c8d9e0f1a2b3c4d5e6f7g",
                              "role": "steward"
                          }
                      ]
                  }
              ],
              "createdAt": "2025-12-26T14:35:30Z",
              "createdBy": "6909d8524392dbbab822c7f7"
          },
          {
              "id": "694e6854cb095e700317784d",
              "changes": [
                  {
                      "path": "/datasetIds",
                      "operator": "add",
                      "value": [
                          "6672d8b7a182224cbb3f1c26",
                          "6689g7h8i9j0k1l2m3n4o5p6",
                          "6a7b8c9d0e1f2g3h4i5j6k7l"
                      ]
                  }
              ],
              "createdAt": "2025-12-26T14:32:00Z",
              "createdBy": "6909d8524392dbbab822c7f7"
          },
          {
              "id": "694e88df717625a4a940649c",
              "changes": [
                  {
                      "path": "/name",
                      "operator": "add",
                      "value": "Sales Analytics Data Product"
                  },
                  {
                      "path": "/description",
                      "operator": "add",
                      "value": "Comprehensive sales data product grouping customer transactions, revenue metrics, and performance analytics"
                  },
                  {
                      "path": "/readMe",
                      "operator": "add",
                      "value": "The Sales Analytics Data Product contains curated sales datasets for analysis and reporting."
                  },
                  {
                      "path": "/spaceId",
                      "operator": "add",
                      "value": "a1b2c3d4e5f6g7h8i9j0k1l2"
                  }
              ],
              "createdAt": "2025-12-26T14:25:00Z",
              "createdBy": "6909d8524392dbbab822c7f7"
          }
      ],
      "page": 1,
      "limit": 10,
      "total": 4,
      "pages": 1,
      "links": {
          "self": {
              "href": "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2/changelogs"
          },
          "first": {
              "href": "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2/changelogs?page=1"
          },
          "last": {
              "href": "https://<TENANT>/api/data-governance/data-products/p1q2r3s4t5u6v7w8x9y0z1a2/changelogs?page=1"
          }
      }
  }
  ```
</details>

The changelog helps you audit governance updates and track data product evolution over time.

## Summary

You've successfully created and activated a data product that:

- Groups related datasets within a single curated package
- Includes comprehensive metadata
- Assigns governance ownership through key contacts
- Is now discoverable and consumable by business users

Your data product is now ready for use in the data marketplace.

## Next steps

- [Learn more about the Data Products API](https://qlik.dev/apis/rest/data-governance/data-products)
