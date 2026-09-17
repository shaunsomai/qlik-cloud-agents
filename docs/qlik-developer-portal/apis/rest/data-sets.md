# Data sets

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data sets are part of the catalog in Qlik Cloud. A data set is a member of a data asset.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/data-sets`](#post-apiv1data-sets) | Creates and saves a new data set in the catalog. |
| `DELETE` | [`/api/v1/data-sets`](#delete-apiv1data-sets) |  |
| `GET` | [`/api/v1/data-sets/{data-set-id}`](#get-apiv1data-setsdata-set-id) |  |
| `PATCH` | [`/api/v1/data-sets/{data-set-id}`](#patch-apiv1data-setsdata-set-id) | Partially updates an existing DataSet by ID using JSON Patch operations (RFC 6902), including ownership attributes. |
| `PUT` | [`/api/v1/data-sets/{data-set-id}`](#put-apiv1data-setsdata-set-id) | Fully replaces an existing DataSet by ID, including ownership attributes. |
| `GET` | [`/api/v1/data-sets/{data-set-id}/profiles`](#get-apiv1data-setsdata-set-idprofiles) |  |

## API Reference

### POST /api/v1/data-sets

Creates and saves a new data set in the catalog.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 201

Created new data set successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format. Also returned when field aliases are not unique within a schema or conflict with another field's name.

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `POST /api/v1/data-sets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      qri: 'string',
      name: 'string',
      tags: ['string'],
      type: 'string',
      schema: {
        anomalies: ['string'],
        dataFields: [
          {
            name: 'string',
            tags: ['string'],
            alias: 'string',
            orphan: true,
            dataType: {
              type: 'DATE',
              properties: {},
              originalType: 'string',
            },
            nullable: true,
            userTags: [
              { id: 'string', name: 'string' },
            ],
            encrypted: true,
            sensitive: true,
            primaryKey: true,
            properties: {},
            description: 'string',
            ordinalPositionInKey: 42,
          },
        ],
        schemaName: 'string',
        loadOptions: {},
        overrideSchemaAnomalies: true,
      },
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      secureQri: 'string',
      properties: {},
      description: 'string',
      operational: {
        size: 42,
        status: 'string',
        endDate: '2018-10-30T07:06:22Z',
        location: 'string',
        rowCount: 42,
        startDate: '2018-10-30T07:06:22Z',
        logMessage: 'string',
        tableOwner: 'string',
        lastLoadTime: '2018-10-30T07:06:22Z',
        contentUpdated: true,
        lastUpdateTime: '2018-10-30T07:06:22Z',
        tableConnectionInfo: {
          tableName: 'string',
          selectionScript: 'string',
          additionalProperties: {},
        },
      },
      dataAssetInfo: {
        id: 'string',
        dataStoreInfo: { id: 'string' },
      },
      technicalName: 'string',
      appTypeOverride: 'string',
      additionalSchemas: [
        {
          anomalies: ['string'],
          dataFields: [
            {
              name: 'string',
              tags: ['string'],
              alias: 'string',
              orphan: true,
              dataType: {
                type: 'DATE',
                properties: {},
                originalType: 'string',
              },
              nullable: true,
              userTags: [
                { id: 'string', name: 'string' },
              ],
              encrypted: true,
              sensitive: true,
              primaryKey: true,
              properties: {},
              description: 'string',
              ordinalPositionInKey: 42,
            },
          ],
          schemaName: 'string',
          loadOptions: {},
          overrideSchemaAnomalies: true,
        },
      ],
      technicalDescription: 'string',
      createdByConnectionId: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-sets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","qri":"string","name":"string","tags":["string"],"type":"string","schema":{"anomalies":["string"],"dataFields":[{"name":"string","tags":["string"],"alias":"string","orphan":true,"dataType":{"type":"DATE","properties":{},"originalType":"string"},"nullable":true,"userTags":[{"id":"string","name":"string"}],"encrypted":true,"sensitive":true,"primaryKey":true,"properties":{},"description":"string","ordinalPositionInKey":42}],"schemaName":"string","loadOptions":{},"overrideSchemaAnomalies":true},"ownerId":"string","spaceId":"string","version":42,"secureQri":"string","properties":{},"description":"string","operational":{"size":42,"status":"string","endDate":"2018-10-30T07:06:22Z","location":"string","rowCount":42,"startDate":"2018-10-30T07:06:22Z","logMessage":"string","tableOwner":"string","lastLoadTime":"2018-10-30T07:06:22Z","contentUpdated":true,"lastUpdateTime":"2018-10-30T07:06:22Z","tableConnectionInfo":{"tableName":"string","selectionScript":"string","additionalProperties":{}}},"dataAssetInfo":{"id":"string","dataStoreInfo":{"id":"string"}},"technicalName":"string","appTypeOverride":"string","additionalSchemas":[{"anomalies":["string"],"dataFields":[{"name":"string","tags":["string"],"alias":"string","orphan":true,"dataType":{"type":"DATE","properties":{},"originalType":"string"},"nullable":true,"userTags":[{"id":"string","name":"string"}],"encrypted":true,"sensitive":true,"primaryKey":true,"properties":{},"description":"string","ordinalPositionInKey":42}],"schemaName":"string","loadOptions":{},"overrideSchemaAnomalies":true}],"technicalDescription":"string","createdByConnectionId":"string"}'
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
  "type": "string",
  "schema": {
    "anomalies": [
      "string"
    ],
    "dataFields": [
      {
        "name": "string",
        "tags": [
          "string"
        ],
        "alias": "string",
        "index": 42,
        "orphan": true,
        "dataType": {
          "type": "DATE",
          "properties": {},
          "originalType": "string"
        },
        "nullable": true,
        "userTags": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "encrypted": true,
        "sensitive": true,
        "primaryKey": true,
        "properties": {},
        "description": "string",
        "ordinalPositionInKey": 42
      }
    ],
    "schemaName": "string",
    "loadOptions": {},
    "effectiveDate": "2018-10-30T07:06:22Z",
    "overrideSchemaAnomalies": true
  },
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "secureQri": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "operational": {
    "size": 42,
    "status": "string",
    "endDate": "2018-10-30T07:06:22Z",
    "location": "string",
    "rowCount": 42,
    "startDate": "2018-10-30T07:06:22Z",
    "logMessage": "string",
    "tableOwner": "string",
    "lastLoadTime": "2018-10-30T07:06:22Z",
    "contentUpdated": true,
    "lastUpdateTime": "2018-10-30T07:06:22Z",
    "tableConnectionInfo": {
      "tableName": "string",
      "selectionScript": "string",
      "additionalProperties": {}
    }
  },
  "dataAssetInfo": {
    "id": "string",
    "name": "string",
    "dataStoreInfo": {
      "id": "string",
      "name": "string",
      "type": "string"
    }
  },
  "technicalName": "string",
  "lastModifiedBy": "string",
  "appTypeOverride": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "additionalSchemas": [
    {
      "anomalies": [
        "string"
      ],
      "dataFields": [
        {
          "name": "string",
          "tags": [
            "string"
          ],
          "alias": "string",
          "index": 42,
          "orphan": true,
          "dataType": {
            "type": "DATE",
            "properties": {},
            "originalType": "string"
          },
          "nullable": true,
          "userTags": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "encrypted": true,
          "sensitive": true,
          "primaryKey": true,
          "properties": {},
          "description": "string",
          "ordinalPositionInKey": 42
        }
      ],
      "schemaName": "string",
      "loadOptions": {},
      "effectiveDate": "2018-10-30T07:06:22Z",
      "overrideSchemaAnomalies": true
    }
  ],
  "technicalDescription": "string",
  "createdByConnectionId": "string"
}
```

---

### DELETE /api/v1/data-sets

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | string[] | No |  |

#### Responses

##### 204

Deleted data sets.

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `DELETE /api/v1/data-sets` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ ids: ['string'] }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/data-sets yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets" \
-X DELETE \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ids":["string"]}'
```

---

### GET /api/v1/data-sets/{data-set-id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-set-id` | string | Yes |  |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `projections` | string[] | No | Comma-separated fields to return in the response. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `GET /api/v1/data-sets/{data-set-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets/{data-set-id}',
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
# qlik-cli has not implemented support for GET /api/v1/data-sets/{data-set-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets/{data-set-id}" \
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
  "type": "string",
  "schema": {
    "anomalies": [
      "string"
    ],
    "dataFields": [
      {
        "name": "string",
        "tags": [
          "string"
        ],
        "alias": "string",
        "index": 42,
        "orphan": true,
        "dataType": {
          "type": "DATE",
          "properties": {},
          "originalType": "string"
        },
        "nullable": true,
        "userTags": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "encrypted": true,
        "sensitive": true,
        "primaryKey": true,
        "properties": {},
        "description": "string",
        "ordinalPositionInKey": 42
      }
    ],
    "schemaName": "string",
    "loadOptions": {},
    "effectiveDate": "2018-10-30T07:06:22Z",
    "overrideSchemaAnomalies": true
  },
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "secureQri": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "operational": {
    "size": 42,
    "status": "string",
    "endDate": "2018-10-30T07:06:22Z",
    "location": "string",
    "rowCount": 42,
    "startDate": "2018-10-30T07:06:22Z",
    "logMessage": "string",
    "tableOwner": "string",
    "lastLoadTime": "2018-10-30T07:06:22Z",
    "contentUpdated": true,
    "lastUpdateTime": "2018-10-30T07:06:22Z",
    "tableConnectionInfo": {
      "tableName": "string",
      "selectionScript": "string",
      "additionalProperties": {}
    }
  },
  "dataAssetInfo": {
    "id": "string",
    "name": "string",
    "dataStoreInfo": {
      "id": "string",
      "name": "string",
      "type": "string"
    }
  },
  "technicalName": "string",
  "lastModifiedBy": "string",
  "appTypeOverride": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "additionalSchemas": [
    {
      "anomalies": [
        "string"
      ],
      "dataFields": [
        {
          "name": "string",
          "tags": [
            "string"
          ],
          "alias": "string",
          "index": 42,
          "orphan": true,
          "dataType": {
            "type": "DATE",
            "properties": {},
            "originalType": "string"
          },
          "nullable": true,
          "userTags": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "encrypted": true,
          "sensitive": true,
          "primaryKey": true,
          "properties": {},
          "description": "string",
          "ordinalPositionInKey": 42
        }
      ],
      "schemaName": "string",
      "loadOptions": {},
      "effectiveDate": "2018-10-30T07:06:22Z",
      "overrideSchemaAnomalies": true
    }
  ],
  "technicalDescription": "string",
  "createdByConnectionId": "string"
}
```

---

### PATCH /api/v1/data-sets/{data-set-id}

Partially updates an existing DataSet by ID using JSON Patch operations (RFC 6902), including ownership attributes.

A user can update any DataSet within a space if they fulfill **one** of the following conditions:

- Has **Can edit** permission in a **data space**.
- Is a **Professional** user with the **Editor** or **Operator** role in a **shared space**.
- Is a **Professional** user with the **Facilitator** or **Operator** role in a **managed space**.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-set-id` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "add", "remove", "replace", "move", "copy", "test" |
| `from` | string | No | A JSON Pointer path pointing to the location to move/copy from. |
| `path` | string | Yes | A JSON pointer to the property being affected. |
| `value` | object | No | The value to add, replace or test. |

#### Responses

##### 200

Patched data set successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 204

Patched data set successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format. Also returned when field aliases are not unique within a schema or conflict with another field's name.

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `PATCH /api/v1/data-sets/{data-set-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets/{data-set-id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        from: 'string',
        path: 'string',
        value: {},
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/data-sets/{data-set-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets/{data-set-id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","from":"string","path":"string","value":{}}]'
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
  "type": "string",
  "schema": {
    "anomalies": [
      "string"
    ],
    "dataFields": [
      {
        "name": "string",
        "tags": [
          "string"
        ],
        "alias": "string",
        "index": 42,
        "orphan": true,
        "dataType": {
          "type": "DATE",
          "properties": {},
          "originalType": "string"
        },
        "nullable": true,
        "userTags": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "encrypted": true,
        "sensitive": true,
        "primaryKey": true,
        "properties": {},
        "description": "string",
        "ordinalPositionInKey": 42
      }
    ],
    "schemaName": "string",
    "loadOptions": {},
    "effectiveDate": "2018-10-30T07:06:22Z",
    "overrideSchemaAnomalies": true
  },
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "secureQri": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "operational": {
    "size": 42,
    "status": "string",
    "endDate": "2018-10-30T07:06:22Z",
    "location": "string",
    "rowCount": 42,
    "startDate": "2018-10-30T07:06:22Z",
    "logMessage": "string",
    "tableOwner": "string",
    "lastLoadTime": "2018-10-30T07:06:22Z",
    "contentUpdated": true,
    "lastUpdateTime": "2018-10-30T07:06:22Z",
    "tableConnectionInfo": {
      "tableName": "string",
      "selectionScript": "string",
      "additionalProperties": {}
    }
  },
  "dataAssetInfo": {
    "id": "string",
    "name": "string",
    "dataStoreInfo": {
      "id": "string",
      "name": "string",
      "type": "string"
    }
  },
  "technicalName": "string",
  "lastModifiedBy": "string",
  "appTypeOverride": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "additionalSchemas": [
    {
      "anomalies": [
        "string"
      ],
      "dataFields": [
        {
          "name": "string",
          "tags": [
            "string"
          ],
          "alias": "string",
          "index": 42,
          "orphan": true,
          "dataType": {
            "type": "DATE",
            "properties": {},
            "originalType": "string"
          },
          "nullable": true,
          "userTags": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "encrypted": true,
          "sensitive": true,
          "primaryKey": true,
          "properties": {},
          "description": "string",
          "ordinalPositionInKey": 42
        }
      ],
      "schemaName": "string",
      "loadOptions": {},
      "effectiveDate": "2018-10-30T07:06:22Z",
      "overrideSchemaAnomalies": true
    }
  ],
  "technicalDescription": "string",
  "createdByConnectionId": "string"
}
```

---

### PUT /api/v1/data-sets/{data-set-id}

Fully replaces an existing DataSet by ID, including ownership attributes.

A user can update any DataSet within a space if they fulfill **one** of the following conditions:

- Has **Can edit** permission in a **data space**.
- Is a **Professional** user with the **Editor** or **Operator** role in a **shared space**.
- Is a **Professional** user with the **Facilitator** or **Operator** role in a **managed space**.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-set-id` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 200

Updated data set successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Only required when updating the resource. Must be null for new resources. |
| `qri` | string | Yes | NOTE: this will be deprecated after migration to secureQri. Required user defined field. All the parts in the format must be separated by ':'. The first part denotes the resourceType, followed by dataStoreType and tenant guid. The spaceGuid or userGuid is to be populated based on if the dataset is in shared or private space and finally the full file name. This field is auto populated for the dataSet generated for qix-datafiles. |
| `name` | string | No |  |
| `tags` | string[] | No |  |
| `type` | string | No |  |
| `schema` | object | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `ownerId` | string | No | The value is automatically set by the application. |
| `spaceId` | string | No |  |
| `version` | integer | No | Only required when updating the resource. Must be null for new resources. |
| `tenantId` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `createdBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `secureQri` | string | Yes |  |
| `properties` | object | No | A Map of name-value pairs. |
| `createdTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `description` | string | No |  |
| `operational` | object | No |  |
| `dataAssetInfo` | object | Yes |  |
| `technicalName` | string | Yes |  |
| `lastModifiedBy` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `appTypeOverride` | string | No | Optional override of DataAsset appType. |
| `lastModifiedTime` | string | No | The value is automatically set by the application. User defined value is ignored. |
| `additionalSchemas` | object[] | No | Optional field to specify additional schemas for files where multiple tables or sheets are available. User must define primary schema in 'schema' attribute and rest of the sheets/ tables can be defined using this field. This field is not populated for the dataSets with single schema |
| `technicalDescription` | string | No |  |
| `createdByConnectionId` | string | No | The connectionId that created the Dataset. Optional. |

<details>
<summary>Properties of `schema`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `operational`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | No |  |
| `status` | string | No |  |
| `endDate` | string | No |  |
| `location` | string | No |  |
| `rowCount` | integer | No |  |
| `startDate` | string | No |  |
| `logMessage` | string | No |  |
| `tableOwner` | string | No |  |
| `lastLoadTime` | string | No |  |
| `contentUpdated` | boolean | No |  |
| `lastUpdateTime` | string | No |  |
| `tableConnectionInfo` | object | No |  |

<details>
<summary>Properties of `tableConnectionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableName` | string | No |  |
| `selectionScript` | string | No |  |
| `additionalProperties` | object | No |  |

</details>

</details>

<details>
<summary>Properties of `dataAssetInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `dataStoreInfo` | object | No |  |

<details>
<summary>Properties of `dataStoreInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | No |  |
| `type` | string | No |  |

</details>

</details>

<details>
<summary>Properties of `additionalSchemas`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `anomalies` | string[] | No | Anomalies associated with this schema. Example: $warning-unknown-headers |
| `dataFields` | object[] | Yes |  |
| `schemaName` | string | No |  |
| `loadOptions` | object | No | Options for loading files. Example: "qLabel": "embedded labels" |
| `effectiveDate` | string | No |  |
| `overrideSchemaAnomalies` | boolean | No |  |

<details>
<summary>Properties of `dataFields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes |  |
| `tags` | string[] | No | An array of system tags |
| `alias` | string | No | Alias of the field. Must be unique within the schema and must not match another field's name. Returns `400` if violated. |
| `index` | integer | No |  |
| `orphan` | boolean | No |  |
| `dataType` | object | Yes |  |
| `nullable` | boolean | No |  |
| `userTags` | object[] | No | An array of user-supplied tags |
| `encrypted` | boolean | No |  |
| `sensitive` | boolean | No |  |
| `primaryKey` | boolean | No |  |
| `properties` | object | No |  |
| `description` | string | No |  |
| `ordinalPositionInKey` | integer | No |  |

<details>
<summary>Properties of `dataType`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `userTags`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format. Also returned when field aliases are not unique within a schema or conflict with another field's name.

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `PUT /api/v1/data-sets/{data-set-id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets/{data-set-id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'string',
      qri: 'string',
      name: 'string',
      tags: ['string'],
      type: 'string',
      schema: {
        anomalies: ['string'],
        dataFields: [
          {
            name: 'string',
            tags: ['string'],
            alias: 'string',
            orphan: true,
            dataType: {
              type: 'DATE',
              properties: {},
              originalType: 'string',
            },
            nullable: true,
            userTags: [
              { id: 'string', name: 'string' },
            ],
            encrypted: true,
            sensitive: true,
            primaryKey: true,
            properties: {},
            description: 'string',
            ordinalPositionInKey: 42,
          },
        ],
        schemaName: 'string',
        loadOptions: {},
        overrideSchemaAnomalies: true,
      },
      ownerId: 'string',
      spaceId: 'string',
      version: 42,
      secureQri: 'string',
      properties: {},
      description: 'string',
      operational: {
        size: 42,
        status: 'string',
        endDate: '2018-10-30T07:06:22Z',
        location: 'string',
        rowCount: 42,
        startDate: '2018-10-30T07:06:22Z',
        logMessage: 'string',
        tableOwner: 'string',
        lastLoadTime: '2018-10-30T07:06:22Z',
        contentUpdated: true,
        lastUpdateTime: '2018-10-30T07:06:22Z',
        tableConnectionInfo: {
          tableName: 'string',
          selectionScript: 'string',
          additionalProperties: {},
        },
      },
      dataAssetInfo: {
        id: 'string',
        dataStoreInfo: { id: 'string' },
      },
      technicalName: 'string',
      appTypeOverride: 'string',
      additionalSchemas: [
        {
          anomalies: ['string'],
          dataFields: [
            {
              name: 'string',
              tags: ['string'],
              alias: 'string',
              orphan: true,
              dataType: {
                type: 'DATE',
                properties: {},
                originalType: 'string',
              },
              nullable: true,
              userTags: [
                { id: 'string', name: 'string' },
              ],
              encrypted: true,
              sensitive: true,
              primaryKey: true,
              properties: {},
              description: 'string',
              ordinalPositionInKey: 42,
            },
          ],
          schemaName: 'string',
          loadOptions: {},
          overrideSchemaAnomalies: true,
        },
      ],
      technicalDescription: 'string',
      createdByConnectionId: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-sets/{data-set-id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets/{data-set-id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"string","qri":"string","name":"string","tags":["string"],"type":"string","schema":{"anomalies":["string"],"dataFields":[{"name":"string","tags":["string"],"alias":"string","orphan":true,"dataType":{"type":"DATE","properties":{},"originalType":"string"},"nullable":true,"userTags":[{"id":"string","name":"string"}],"encrypted":true,"sensitive":true,"primaryKey":true,"properties":{},"description":"string","ordinalPositionInKey":42}],"schemaName":"string","loadOptions":{},"overrideSchemaAnomalies":true},"ownerId":"string","spaceId":"string","version":42,"secureQri":"string","properties":{},"description":"string","operational":{"size":42,"status":"string","endDate":"2018-10-30T07:06:22Z","location":"string","rowCount":42,"startDate":"2018-10-30T07:06:22Z","logMessage":"string","tableOwner":"string","lastLoadTime":"2018-10-30T07:06:22Z","contentUpdated":true,"lastUpdateTime":"2018-10-30T07:06:22Z","tableConnectionInfo":{"tableName":"string","selectionScript":"string","additionalProperties":{}}},"dataAssetInfo":{"id":"string","dataStoreInfo":{"id":"string"}},"technicalName":"string","appTypeOverride":"string","additionalSchemas":[{"anomalies":["string"],"dataFields":[{"name":"string","tags":["string"],"alias":"string","orphan":true,"dataType":{"type":"DATE","properties":{},"originalType":"string"},"nullable":true,"userTags":[{"id":"string","name":"string"}],"encrypted":true,"sensitive":true,"primaryKey":true,"properties":{},"description":"string","ordinalPositionInKey":42}],"schemaName":"string","loadOptions":{},"overrideSchemaAnomalies":true}],"technicalDescription":"string","createdByConnectionId":"string"}'
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
  "type": "string",
  "schema": {
    "anomalies": [
      "string"
    ],
    "dataFields": [
      {
        "name": "string",
        "tags": [
          "string"
        ],
        "alias": "string",
        "index": 42,
        "orphan": true,
        "dataType": {
          "type": "DATE",
          "properties": {},
          "originalType": "string"
        },
        "nullable": true,
        "userTags": [
          {
            "id": "string",
            "name": "string"
          }
        ],
        "encrypted": true,
        "sensitive": true,
        "primaryKey": true,
        "properties": {},
        "description": "string",
        "ordinalPositionInKey": 42
      }
    ],
    "schemaName": "string",
    "loadOptions": {},
    "effectiveDate": "2018-10-30T07:06:22Z",
    "overrideSchemaAnomalies": true
  },
  "ownerId": "string",
  "spaceId": "string",
  "version": 42,
  "tenantId": "string",
  "createdBy": "string",
  "secureQri": "string",
  "properties": {},
  "createdTime": "2018-10-30T07:06:22Z",
  "description": "string",
  "operational": {
    "size": 42,
    "status": "string",
    "endDate": "2018-10-30T07:06:22Z",
    "location": "string",
    "rowCount": 42,
    "startDate": "2018-10-30T07:06:22Z",
    "logMessage": "string",
    "tableOwner": "string",
    "lastLoadTime": "2018-10-30T07:06:22Z",
    "contentUpdated": true,
    "lastUpdateTime": "2018-10-30T07:06:22Z",
    "tableConnectionInfo": {
      "tableName": "string",
      "selectionScript": "string",
      "additionalProperties": {}
    }
  },
  "dataAssetInfo": {
    "id": "string",
    "name": "string",
    "dataStoreInfo": {
      "id": "string",
      "name": "string",
      "type": "string"
    }
  },
  "technicalName": "string",
  "lastModifiedBy": "string",
  "appTypeOverride": "string",
  "lastModifiedTime": "2018-10-30T07:06:22Z",
  "additionalSchemas": [
    {
      "anomalies": [
        "string"
      ],
      "dataFields": [
        {
          "name": "string",
          "tags": [
            "string"
          ],
          "alias": "string",
          "index": 42,
          "orphan": true,
          "dataType": {
            "type": "DATE",
            "properties": {},
            "originalType": "string"
          },
          "nullable": true,
          "userTags": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "encrypted": true,
          "sensitive": true,
          "primaryKey": true,
          "properties": {},
          "description": "string",
          "ordinalPositionInKey": 42
        }
      ],
      "schemaName": "string",
      "loadOptions": {},
      "effectiveDate": "2018-10-30T07:06:22Z",
      "overrideSchemaAnomalies": true
    }
  ],
  "technicalDescription": "string",
  "createdByConnectionId": "string"
}
```

---

### GET /api/v1/data-sets/{data-set-id}/profiles

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data-set-id` | string | Yes |  |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataConnectionIds` | string[] | No | Comma-separated data connection IDs. |
| `limit` | integer | No | Page size limit. |
| `page` | integer | No |  |
| `projections` | string[] | No | Comma-separated fields to return in the response. |
| `sort` | string[] | No |  |

#### Responses

##### 200

Return profiles of data set.

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
| `meta` | object | No |  |
| `samples` | object[] | No |  |
| `profiles` | object[] | No |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Enum: "QUEUED", "RUNNING", "FINISHED", "FAILED", "INCOMPLETE", "CANCELLED", "STALE", "PARTIAL", "DEFERRED" |
| `messages` | string[] | No |  |
| `dataSetId` | string | No |  |
| `resultType` | string | No | Enum: "NORMAL", "BASIC" |
| `connectionId` | string | No |  |
| `lastLoadTime` | string | No |  |
| `computationEndTime` | string | No |  |
| `computationStartTime` | string | No |  |

</details>

<details>
<summary>Properties of `samples`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `records` | object[] | No |  |
| `fieldNames` | string[] | No |  |

<details>
<summary>Properties of `records`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `profiles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `sizeInBytes` | integer | No |  |
| `numberOfRows` | integer | No |  |
| `fieldProfiles` | object[] | No |  |

<details>
<summary>Properties of `fieldProfiles`</summary>

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

##### 202

The profile is currently running.

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
| `meta` | object | No |  |
| `samples` | object[] | No |  |
| `profiles` | object[] | No |  |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Enum: "QUEUED", "RUNNING", "FINISHED", "FAILED", "INCOMPLETE", "CANCELLED", "STALE", "PARTIAL", "DEFERRED" |
| `messages` | string[] | No |  |
| `dataSetId` | string | No |  |
| `resultType` | string | No | Enum: "NORMAL", "BASIC" |
| `connectionId` | string | No |  |
| `lastLoadTime` | string | No |  |
| `computationEndTime` | string | No |  |
| `computationStartTime` | string | No |  |

</details>

<details>
<summary>Properties of `samples`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `records` | object[] | No |  |
| `fieldNames` | string[] | No |  |

<details>
<summary>Properties of `records`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `profiles`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No |  |
| `sizeInBytes` | integer | No |  |
| `numberOfRows` | integer | No |  |
| `fieldProfiles` | object[] | No |  |

<details>
<summary>Properties of `fieldProfiles`</summary>

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

Internal Server Error.

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

Requested service is not available.

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
// qlik-api has not implemented support for `GET /api/v1/data-sets/{data-set-id}/profiles` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-sets/{data-set-id}/profiles',
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
# qlik-cli has not implemented support for GET /api/v1/data-sets/{data-set-id}/profiles yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets/{data-set-id}/profiles" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "meta": {
        "status": "QUEUED",
        "messages": [
          "string"
        ],
        "dataSetId": "string",
        "resultType": "NORMAL",
        "connectionId": "string",
        "lastLoadTime": "2018-10-30T07:06:22Z",
        "computationEndTime": "2018-10-30T07:06:22Z",
        "computationStartTime": "2018-10-30T07:06:22Z"
      },
      "samples": [
        {
          "name": "string",
          "records": [
            {
              "values": [
                "string"
              ]
            }
          ],
          "fieldNames": [
            "string"
          ]
        }
      ],
      "profiles": [
        {
          "name": "string",
          "sizeInBytes": 42,
          "numberOfRows": 42,
          "fieldProfiles": [
            {
              "name": "string",
              "tags": [
                "string"
              ],
              "index": 42,
              "median": 42,
              "average": 42,
              "dataType": "DATE",
              "evenness": 42,
              "kurtosis": 42,
              "skewness": 42,
              "fractiles": [
                42
              ],
              "sampleValues": [
                "string"
              ],
              "technicalName": "string",
              "classification": {
                "pii": true,
                "tags": [
                  {
                    "tag": "string",
                    "score": 42
                  }
                ],
                "sensitive": true,
                "obfuscation": "string"
              },
              "nullValueCount": 42,
              "textValueCount": 42,
              "zeroValueCount": 42,
              "maxNumericValue": 42,
              "maxStringLength": 42,
              "minNumericValue": 42,
              "minStringLength": 42,
              "sumStringLength": 42,
              "emptyStringCount": 42,
              "sumNumericValues": 42,
              "numericValueCount": 42,
              "standardDeviation": 42,
              "distinctValueCount": 42,
              "mostFrequentValues": [
                {
                  "value": "string",
                  "frequency": 42
                }
              ],
              "negativeValueCount": 42,
              "positiveValueCount": 42,
              "averageStringLength": 42,
              "frequencyDistribution": [
                {
                  "binEdge": 42,
                  "frequency": 42
                }
              ],
              "lastSortedStringValue": "string",
              "firstSortedStringValue": "string",
              "sumSquaredNumericValues": 42
            }
          ]
        }
      ]
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
