# Data products

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data products are packages that group related datasets within a single, curated offering. Use the Data products API to create, manage, and activate data products for consumption by business users.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/data-governance/data-products`](#post-apidata-governancedata-products) | Creates a new data product with specified metadata, datasets, and governance information. |
| `GET` | [`/api/data-governance/data-products/{dataProductId}`](#get-apidata-governancedata-productsdataproductid) | Retrieves the details of the specified data product, including name, description, associated datasets, key contacts, and activation status. |
| `PATCH` | [`/api/data-governance/data-products/{dataProductId}`](#patch-apidata-governancedata-productsdataproductid) | Partially updates an existing data product using JSON Patch operations. |
| `DELETE` | [`/api/data-governance/data-products/{dataProductId}`](#delete-apidata-governancedata-productsdataproductid) | Permanently removes a data product from the tenant. |
| `POST` | [`/api/data-governance/data-products/{dataProductId}/actions/activate`](#post-apidata-governancedata-productsdataproductidactionsactivate) | Activates a data product for publishing and consumption. |
| `POST` | [`/api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality`](#post-apidata-governancedata-productsdataproductidactionscompute-datasets-data-quality) | Triggers a full data quality computation for all datasets in the data product, running profile calculation followed by data quality |
| `POST` | [`/api/data-governance/data-products/{dataProductId}/actions/deactivate`](#post-apidata-governancedata-productsdataproductidactionsdeactivate) | Deactivates a data product, preventing it from being consumed by other services or users. |
| `GET` | [`/api/data-governance/data-products/{dataProductId}/actions/export-documentation`](#get-apidata-governancedata-productsdataproductidactionsexport-documentation) | Exports data product documentation in Markdown format. |
| `POST` | [`/api/data-governance/data-products/{dataProductId}/actions/move`](#post-apidata-governancedata-productsdataproductidactionsmove) | Moves a data product from its current space to a different space. |
| `GET` | [`/api/data-governance/data-products/{dataProductId}/changelogs`](#get-apidata-governancedata-productsdataproductidchangelogs) | Retrieves a paginated history of all notable changes made to a data product. |
| `POST` | [`/api/data-governance/data-products/actions/generate-provider-url`](#post-apidata-governancedata-productsactionsgenerate-provider-url) | Generates a URL to access a third-party provider's user interface. |

## API Reference

### POST /api/data-governance/data-products

Creates a new data product with specified metadata, datasets, and governance information.
Use this endpoint to package related datasets into a governed, discoverable asset.
Requires create permissions in the target space.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Display name of the data product. |
| `tags` | string[] | No | List of tags for the data product. |
| `readMe` | string | No | A readme of the Data Product. |
| `spaceId` | string | No | Unique identifier of the space. |
| `datasetIds` | string[] | No | List of dataset IDs associated with the Data Product. Maximum of 100 items. |
| `description` | string | No | A description of the Data Product. |
| `glossaryIds` | string[] | No | List of glossary IDs linked to the Data Product. Each entry must be a valid UUIDv4 (maximum 36 characters). Maximum of 100 items. |
| `keyContacts` | object[] | No | List of key contacts for the data product. |
| `apiConsumableDatasetIds` | string[] | No | List of dataset IDs for which API consumption is enabled. Must be a subset of datasetIds. |

<details>
<summary>Properties of `keyContacts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the key contact in the Data Product. |
| `userId` | string | Yes | Unique identifier of the user. |

</details>

#### Responses

##### 201

Data product created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `qri` | string | Yes | Qlik Resource Identifier (QRI) uniquely identifying the data product across the platform. |
| `name` | string | Yes |  |
| `tags` | string[] | Yes |  |
| `mainId` | string | No | Primary identifier used for main data product reference. |
| `readMe` | string | No | Documentation in Markdown format providing detailed information about the data product. |
| `ownerId` | string | Yes | Identifier of the user who owns the data product and is responsible for governance. |
| `quality` | object | No |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `activated` | boolean | No | Indicates whether the data product is currently activated for consumption. |
| `createdAt` | string | Yes | Timestamp when the data product was created in ISO 8601 format. |
| `createdBy` | string | Yes | Identifier of the user who created the data product. |
| `updatedAt` | string | Yes | Timestamp of the most recent update in ISO 8601 format. |
| `updatedBy` | string | Yes | Identifier of the user who last updated the data product. |
| `datasetIds` | string[] | Yes |  |
| `trustScore` | object | No |  |
| `activatedAt` | string | No | Timestamp when the data product was most recently activated in ISO 8601 format. |
| `activatedOn` | string[] | Yes | List of target environments or platforms where the data product is activated. |
| `description` | string | No |  |
| `glossaryIds` | string[] | Yes |  |
| `keyContacts` | object[] | Yes | Represents a designated contact person for a data product, optionally with their role. |
| `pendingChangesCount` | integer | No | Number of pending changes that are not yet activated. |
| `apiConsumableDatasetIds` | string[] | Yes | List of dataset IDs for which API consumption is enabled |

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `validity` | number | Yes |  |
| `completeness` | number | Yes |  |

</details>

<details>
<summary>Properties of `trustScore`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `score` | number | Yes |  |
| `dimensions` | object[] | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `score` | number | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

</details>

</details>

<details>
<summary>Properties of `keyContacts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the key contact in the Data Product. |
| `userId` | string | Yes | Unique identifier of the user. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 422

The data product limit has been exceeded for this tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'ExampleDataProductName',
      tags: ['exampleTag1', 'exampleTag2'],
      readMe:
        'This is an example readme for the Data Product.',
      spaceId: 'ExampleSpaceId',
      datasetIds: ['string'],
      description:
        'This is an example Data Product.',
      glossaryIds: ['string'],
      keyContacts: [
        {
          role: 'Data Steward',
          userId: 'exampleUserId',
        },
      ],
      apiConsumableDatasetIds: ['string'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"ExampleDataProductName","tags":["exampleTag1","exampleTag2"],"readMe":"This is an example readme for the Data Product.","spaceId":"ExampleSpaceId","datasetIds":["string"],"description":"This is an example Data Product.","glossaryIds":["string"],"keyContacts":[{"role":"Data Steward","userId":"exampleUserId"}],"apiConsumableDatasetIds":["string"]}'
```

**Example Response:**

```json
{
  "id": "string",
  "qri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "mainId": "string",
  "readMe": "string",
  "ownerId": "string",
  "quality": {
    "validity": 42,
    "completeness": 42
  },
  "spaceId": "string",
  "tenantId": "string",
  "activated": true,
  "createdAt": "2018-03-20T09:12:28Z",
  "createdBy": "string",
  "updatedAt": "2018-03-20T09:12:28Z",
  "updatedBy": "string",
  "datasetIds": [
    "string"
  ],
  "trustScore": {
    "score": 42,
    "dimensions": [
      {
        "id": "string",
        "score": 42,
        "previousScore": 42,
        "applicableDatasets": 42
      }
    ],
    "previousScore": 42,
    "applicableDatasets": 42
  },
  "activatedAt": "2018-03-20T09:12:28Z",
  "activatedOn": [
    "string"
  ],
  "description": "string",
  "glossaryIds": [
    "string"
  ],
  "keyContacts": [
    {
      "role": "Data Steward",
      "userId": "exampleUserId"
    }
  ],
  "pendingChangesCount": 42,
  "apiConsumableDatasetIds": [
    "string"
  ]
}
```

---

### GET /api/data-governance/data-products/{dataProductId}

Retrieves the details of the specified data product, including name, description, associated datasets, key contacts, and activation status.
Requires read access to the Data Product.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Responses

##### 200

Data product details retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `qri` | string | Yes | Qlik Resource Identifier (QRI) uniquely identifying the data product across the platform. |
| `name` | string | Yes |  |
| `tags` | string[] | Yes |  |
| `mainId` | string | No | Primary identifier used for main data product reference. |
| `readMe` | string | No | Documentation in Markdown format providing detailed information about the data product. |
| `ownerId` | string | Yes | Identifier of the user who owns the data product and is responsible for governance. |
| `quality` | object | No |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `activated` | boolean | No | Indicates whether the data product is currently activated for consumption. |
| `createdAt` | string | Yes | Timestamp when the data product was created in ISO 8601 format. |
| `createdBy` | string | Yes | Identifier of the user who created the data product. |
| `updatedAt` | string | Yes | Timestamp of the most recent update in ISO 8601 format. |
| `updatedBy` | string | Yes | Identifier of the user who last updated the data product. |
| `datasetIds` | string[] | Yes |  |
| `trustScore` | object | No |  |
| `activatedAt` | string | No | Timestamp when the data product was most recently activated in ISO 8601 format. |
| `activatedOn` | string[] | Yes | List of target environments or platforms where the data product is activated. |
| `description` | string | No |  |
| `glossaryIds` | string[] | Yes |  |
| `keyContacts` | object[] | Yes | Represents a designated contact person for a data product, optionally with their role. |
| `pendingChangesCount` | integer | No | Number of pending changes that are not yet activated. |
| `apiConsumableDatasetIds` | string[] | Yes | List of dataset IDs for which API consumption is enabled |

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `validity` | number | Yes |  |
| `completeness` | number | Yes |  |

</details>

<details>
<summary>Properties of `trustScore`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `score` | number | Yes |  |
| `dimensions` | object[] | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `score` | number | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

</details>

</details>

<details>
<summary>Properties of `keyContacts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the key contact in the Data Product. |
| `userId` | string | Yes | Unique identifier of the user. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-products/{dataProductId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/data-governance/data-products/{dataProductId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "qri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "mainId": "string",
  "readMe": "string",
  "ownerId": "string",
  "quality": {
    "validity": 42,
    "completeness": 42
  },
  "spaceId": "string",
  "tenantId": "string",
  "activated": true,
  "createdAt": "2018-03-20T09:12:28Z",
  "createdBy": "string",
  "updatedAt": "2018-03-20T09:12:28Z",
  "updatedBy": "string",
  "datasetIds": [
    "string"
  ],
  "trustScore": {
    "score": 42,
    "dimensions": [
      {
        "id": "string",
        "score": 42,
        "previousScore": 42,
        "applicableDatasets": 42
      }
    ],
    "previousScore": 42,
    "applicableDatasets": 42
  },
  "activatedAt": "2018-03-20T09:12:28Z",
  "activatedOn": [
    "string"
  ],
  "description": "string",
  "glossaryIds": [
    "string"
  ],
  "keyContacts": [
    {
      "role": "Data Steward",
      "userId": "exampleUserId"
    }
  ],
  "pendingChangesCount": 42,
  "apiConsumableDatasetIds": [
    "string"
  ]
}
```

---

### PATCH /api/data-governance/data-products/{dataProductId}

Partially updates an existing data product using JSON Patch operations.
Use this endpoint to modify properties such as name, description, datasets, tags, or key contacts.
Changes are tracked in the data product changelog.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Enum: "replace" |
| `path` | string | Yes | Enum: "/name", "/description", "/datasetIds", "/glossaryIds", "/readMe", "/keyContacts", "/tags", "/apiConsumableDatasetIds" |
| `value` | string \| array | No |  |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No | Value is expected to be null or a string if the path is either /name, /description, or /readMe |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ArrayOfUniqueStrings` | string[] | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object[] | No | Value is expected to be null or an array of object if the path is /keyContacts |

</details>

#### Responses

##### 204

Data product updated successfully.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/data-governance/data-products/{dataProductId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/data-governance/data-products/{dataProductId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/name","value":"string"}]'
```

---

### DELETE /api/data-governance/data-products/{dataProductId}

Permanently removes a data product from the tenant.
This action cannot be undone and does not affect the underlying datasets.
Requires delete permissions for the data product.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Responses

##### 204

Data product deleted successfully.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/data-governance/data-products/{dataProductId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/data-governance/data-products/{dataProductId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/data-governance/data-products/{dataProductId}/actions/activate

Activates a data product for publishing and consumption.
Once activated, the data product becomes discoverable and accessible to authorized users.
Requires publish permissions and valid data product configuration.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the data product to activate. |
| `tags` | string[] | No | List of tags for the data product. |
| `spaceId` | string | No | Unique identifier of the space. |
| `description` | string | No | A description of the data product. |

#### Responses

##### 201

Created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `qri` | string | Yes | Qlik Resource Identifier (QRI) uniquely identifying the data product across the platform. |
| `name` | string | Yes |  |
| `tags` | string[] | Yes |  |
| `mainId` | string | No | Primary identifier used for main data product reference. |
| `readMe` | string | No | Documentation in Markdown format providing detailed information about the data product. |
| `ownerId` | string | Yes | Identifier of the user who owns the data product and is responsible for governance. |
| `quality` | object | No |  |
| `spaceId` | string | No |  |
| `tenantId` | string | Yes |  |
| `activated` | boolean | No | Indicates whether the data product is currently activated for consumption. |
| `createdAt` | string | Yes | Timestamp when the data product was created in ISO 8601 format. |
| `createdBy` | string | Yes | Identifier of the user who created the data product. |
| `updatedAt` | string | Yes | Timestamp of the most recent update in ISO 8601 format. |
| `updatedBy` | string | Yes | Identifier of the user who last updated the data product. |
| `datasetIds` | string[] | Yes |  |
| `trustScore` | object | No |  |
| `activatedAt` | string | No | Timestamp when the data product was most recently activated in ISO 8601 format. |
| `activatedOn` | string[] | Yes | List of target environments or platforms where the data product is activated. |
| `description` | string | No |  |
| `glossaryIds` | string[] | Yes |  |
| `keyContacts` | object[] | Yes | Represents a designated contact person for a data product, optionally with their role. |
| `pendingChangesCount` | integer | No | Number of pending changes that are not yet activated. |
| `apiConsumableDatasetIds` | string[] | Yes | List of dataset IDs for which API consumption is enabled |

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `validity` | number | Yes |  |
| `completeness` | number | Yes |  |

</details>

<details>
<summary>Properties of `trustScore`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `score` | number | Yes |  |
| `dimensions` | object[] | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

<details>
<summary>Properties of `dimensions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `score` | number | No |  |
| `previousScore` | number | No |  |
| `applicableDatasets` | number | Yes |  |

</details>

</details>

<details>
<summary>Properties of `keyContacts`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | string | No | Role of the key contact in the Data Product. |
| `userId` | string | Yes | Unique identifier of the user. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products/{dataProductId}/actions/activate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/actions/activate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'ExampleDataProductName',
      tags: ['example'],
      spaceId: 'ExampleSpaceId',
      description:
        'This is an example data product.',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products/{dataProductId}/actions/activate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/actions/activate" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"ExampleDataProductName","tags":["example"],"spaceId":"ExampleSpaceId","description":"This is an example data product."}'
```

**Example Response:**

```json
{
  "id": "string",
  "qri": "string",
  "name": "string",
  "tags": [
    "string"
  ],
  "mainId": "string",
  "readMe": "string",
  "ownerId": "string",
  "quality": {
    "validity": 42,
    "completeness": 42
  },
  "spaceId": "string",
  "tenantId": "string",
  "activated": true,
  "createdAt": "2018-03-20T09:12:28Z",
  "createdBy": "string",
  "updatedAt": "2018-03-20T09:12:28Z",
  "updatedBy": "string",
  "datasetIds": [
    "string"
  ],
  "trustScore": {
    "score": 42,
    "dimensions": [
      {
        "id": "string",
        "score": 42,
        "previousScore": 42,
        "applicableDatasets": 42
      }
    ],
    "previousScore": 42,
    "applicableDatasets": 42
  },
  "activatedAt": "2018-03-20T09:12:28Z",
  "activatedOn": [
    "string"
  ],
  "description": "string",
  "glossaryIds": [
    "string"
  ],
  "keyContacts": [
    {
      "role": "Data Steward",
      "userId": "exampleUserId"
    }
  ],
  "pendingChangesCount": 42,
  "apiConsumableDatasetIds": [
    "string"
  ]
}
```

---

### POST /api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality

Triggers a full data quality computation for all datasets in the data product, running profile calculation followed by data quality
assessment. Returns a `batchComputationId` that can be used to track overall progress via the batch computation status endpoint
(`GET /api/data-governance/data-qualities/batch-computations/{batchComputationId}`). The computation runs asynchronously.
Poll the status endpoint until `status` is `FINISHED`.


- **Rate Limit:** Special (10 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Responses

##### 202

Data quality computation triggered successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetResponses` | object[] | Yes | List of computation results, one entry per dataset in the data product. |
| `batchComputationId` | string | Yes | Unique identifier for the data quality batch computation job. |

<details>
<summary>Properties of `datasetResponses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | string | No | Error message if the computation failed; absent on success. |
| `status` | string | Yes | Current execution status of the computation (REQUESTED or FAILED). Enum: "REQUESTED", "FAILED" |
| `datasetId` | string | Yes | The ID of the dataset |
| `computationId` | string | Yes | Unique identifier for this individual data quality computation job. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "datasetResponses": [
    {
      "error": "string",
      "status": "REQUESTED",
      "datasetId": "669144f5aa2d642638ef1dd0",
      "computationId": "string"
    }
  ],
  "batchComputationId": "string"
}
```

---

### POST /api/data-governance/data-products/{dataProductId}/actions/deactivate

Deactivates a data product, preventing it from being consumed by other services or users.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Responses

##### 204

No content

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products/{dataProductId}/actions/deactivate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/actions/deactivate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products/{dataProductId}/actions/deactivate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/actions/deactivate" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/data-governance/data-products/{dataProductId}/actions/export-documentation

Exports data product documentation in Markdown format.
Use this endpoint to generate documentation for sharing or archiving.
Requires read access to the data product.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Responses

##### 200

Documentation exported successfully in Markdown format.

**Content-Type:** `text/markdown`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `text/markdown` | string | No |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 406

MIME type isn't supported.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 415

Unsupported output format requested.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-products/{dataProductId}/actions/export-documentation` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/actions/export-documentation',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/data-governance/data-products/{dataProductId}/actions/export-documentation yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/actions/export-documentation" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
"string"
```

---

### POST /api/data-governance/data-products/{dataProductId}/actions/move

Moves a data product from its current space to a different space.
Use this endpoint to reorganize data products across workspaces or governance domains.
Requires delete permissions in the source space and create permissions in the target space.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | Yes | Unique identifier of the space. |

#### Responses

##### 204

No content

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products/{dataProductId}/actions/move` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/actions/move',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      spaceId: 'exampleSpaceId',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products/{dataProductId}/actions/move yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/actions/move" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"spaceId":"exampleSpaceId"}'
```

---

### GET /api/data-governance/data-products/{dataProductId}/changelogs

Retrieves a paginated history of all notable changes made to a data product.
Each changelog entry captures the operation type, affected property, and timestamp.
Use this endpoint to track the history of changes or data product evolution over time.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataProductId` | string | Yes | Unique identifier of the data product. Must be a valid GUID assigned when the data product was created. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | integer | No | Page number. |
| `limit` | integer | No | Maximum number of items to return per page. |
| `sort` | string | No | Sort order for changelog entries. Use `+createdAt` for oldest first or `-createdAt` for newest first. Prefix with `+` for ascending or `-` for descending order. Default: -createdAt.  Enum: "+createdAt", "-createdAt" |

#### Responses

##### 200

OK response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `page` | integer | No |  |
| `limit` | integer | No |  |
| `links` | object | No |  |
| `pages` | integer | No |  |
| `total` | integer | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No |  |
| `changes` | object[] | No |  |
| `createdAt` | string | No | Timestamp when this changelog entry was created in ISO 8601 format. |
| `createdBy` | string | No | Identifier of the user who made these changes. |

<details>
<summary>Properties of `changes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | No | Enum: "/name", "/description", "/spaceId", "/datasetIds", "/glossaryIds", "/readMe", "/keyContacts", "/tags", "/activatedOn", "/apiConsumableDatasetIds", "/semanticModel" |
| `value` | string \| array | No |  |
| `operator` | string | No | Enum: "replace", "add", "remove" |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

_Properties truncated due to depth limit._

**Option 2:**

_Properties truncated due to depth limit._

**Option 3:**

_Properties truncated due to depth limit._

**Option 4:**

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `last` | object | No |  |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |
| `first` | object | No |  |

<details>
<summary>Properties of `last`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `first`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 409

The input request conflicts with the current state of the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-products/{dataProductId}/changelogs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/{dataProductId}/changelogs',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/data-governance/data-products/{dataProductId}/changelogs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/{dataProductId}/changelogs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "changes": [
        {
          "path": "/name",
          "value": "string",
          "operator": "replace"
        }
      ],
      "createdAt": "2018-03-20T09:12:28Z",
      "createdBy": "string"
    }
  ],
  "page": 42,
  "limit": 42,
  "links": {
    "last": {
      "href": "string"
    },
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    },
    "first": {
      "href": "string"
    }
  },
  "pages": 42,
  "total": 42
}
```

---

### POST /api/data-governance/data-products/actions/generate-provider-url

Generates a URL to access a third-party provider's user interface.
Use this endpoint to integrate external services with your data product.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSetId` | string | Yes | Unique identifier of the dataset. |

#### Responses

##### 200

OK response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes |  |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Service temporarily unavailable. Retry the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-products/actions/generate-provider-url` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-products/actions/generate-provider-url',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-products/actions/generate-provider-url yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products/actions/generate-provider-url" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "url": "string"
}
```

---
