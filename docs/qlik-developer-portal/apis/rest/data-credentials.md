# Data credentials

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data credentials are the stored credentials leveraged by the data-connections service to connect to external data sources.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-credentials/{qID}`](#get-apiv1data-credentialsqid) |  |
| `PATCH` | [`/api/v1/data-credentials/{qID}`](#patch-apiv1data-credentialsqid) |  |
| `PUT` | [`/api/v1/data-credentials/{qID}`](#put-apiv1data-credentialsqid) |  |
| `DELETE` | [`/api/v1/data-credentials/{qID}`](#delete-apiv1data-credentialsqid) |  |
| `POST` | [`/api/v1/data-credentials/actions/filter-orphan`](#post-apiv1data-credentialsactionsfilter-orphan) |  |

## API Reference

### GET /api/v1/data-credentials/{qID}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Credential ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `byCredentialName` | boolean | No | If set to true, credentialId in the query will be interpreted as credential's name |

#### Responses

##### 200

Credential retrieved

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | UUID of the credential |
| `links` | object | No |  |
| `qName` | string | Yes | Name of the credential |
| `qType` | string | Yes | Type of credential |
| `created` | string | No | Datetime when the credential was created |
| `updated` | string | No | Datetime when the credential was last updated |
| `qConnCount` | integer | Yes | Number of linked connections |
| `datasourceID` | string | No | ID datasource that the credential is created for |
| `qReferenceKey` | string | No | Reference key of credential in redis |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | Link to current query |

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL pointing to the resource |

</details>

</details>

##### 400

Empty value not permitted for dataName

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 404

Credential not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-credentials/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-credentials/{qID}',
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
# qlik-cli has not implemented support for GET /api/v1/data-credentials/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/{qID}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "qID": "065f977e-6eca-408c-b78b-ecded823712c",
  "links": {
    "self": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    }
  },
  "qName": "MyCredential for REST datasource",
  "qType": "QvWebStorageProviderConnectorPackage.exe",
  "created": "2022-04-08T10:00:28.287Z",
  "updated": "2022-04-09T10:00:28.287Z",
  "qConnCount": 1,
  "datasourceID": "rest",
  "qReferenceKey": "credential:key"
}
```

---

### PATCH /api/v1/data-credentials/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Credential ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `byCredentialName` | boolean | No | If set to true, credentialId in the query will be interpreted as credential's name |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | Operation type Enum: "add", "replace", "remove" |
| `path` | string | Yes | Path to the target field to be patched |
| `value` | string \| boolean \| integer \| array | No | Value used for the patch. Required only for `add` or `replace` operations. The value type should match the type of the target field. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | integer | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | array | No |  |

</details>

#### Responses

##### 204

Credential updated successfully

##### 400

Connection ID changed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 404

Credential not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 409

Credential already exists (when updated name conflicts with existing record)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/data-credentials/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-credentials/{qID}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: '/qName',
        value: 'New value',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/data-credentials/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/{qID}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/qName","value":"New value"}]'
```

---

### PUT /api/v1/data-credentials/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Credential ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `byCredentialName` | boolean | No | If set to true, credentialId in the query will be interpreted as credential's name |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | No | UUID of the credential |
| `qName` | string | Yes | Name of the credential |
| `qType` | string | Yes | Type of credential (i.e. connector provider of the corresponding connection) |
| `qPassword` | string | Yes | Password |
| `qUsername` | string | Yes | User name |
| `connectionId` | string | No | ID of connection that will be associated with the credential |
| `datasourceID` | string | No | ID datasource that the credential is created for |

#### Responses

##### 204

Credential updated successfully

##### 400

Connection ID changed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 404

Credential not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 409

Credential already exists (when updated name conflicts with existing record)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/data-credentials/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-credentials/{qID}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      qID: 'c2dd20e3-1842-42d0-81fe-1ecf08e6abde',
      qName: 'MyCredential for REST datasource',
      qType:
        'QvWebStorageProviderConnectorPackage.exe',
      qPassword: 'MyPassword',
      qUsername: 'MyUsername',
      connectionId:
        '2eb98dea-5e3b-4f50-9967-841cec04b72f',
      datasourceID: 'rest',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-credentials/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/{qID}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"qID":"c2dd20e3-1842-42d0-81fe-1ecf08e6abde","qName":"MyCredential for REST datasource","qType":"QvWebStorageProviderConnectorPackage.exe","qPassword":"MyPassword","qUsername":"MyUsername","connectionId":"2eb98dea-5e3b-4f50-9967-841cec04b72f","datasourceID":"rest"}'
```

---

### DELETE /api/v1/data-credentials/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Credential ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `byCredentialName` | boolean | No | If set to true, credentialId in the query will be interpreted as credential's name |

#### Responses

##### 204

Credential deleted successfully

##### 404

Credential not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-credentials/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-credentials/{qID}',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-credentials/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/{qID}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/data-credentials/actions/filter-orphan

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qType` | string | No | Filtering on type of credentials |
| `qSeparated` | integer | No | Filtering on separate status of credentials: * 0 - embedded credential * 1 - separated credential  Enum: 0, 1 |
| `datasourceID` | string | No | Filtering on datasource ID of credentials |

#### Responses

##### 200

Orphan credentials returned

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Orphan credential |
| `count` | integer | Yes | Number of orphan credentials found |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | UUID of the credential |
| `user` | string | No | User ID of the credential's owner |
| `qName` | string | Yes | Name of the credential |
| `qType` | string | Yes | Type of credential (i.e. connector provider of the corresponding connection) |
| `tenant` | string | No | Tenant ID of the credential's owner |
| `created` | string | Yes | Datetime when the credential was created |
| `updated` | string | Yes | Datetime when the credential was last updated |
| `datasourceID` | string | No | ID datasource that the credential is created for |

</details>

##### 400

Bad request (Missing required field in request body)

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 403

User has no access to credentials

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-credentials/actions/filter-orphan` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-credentials/actions/filter-orphan',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      qType: 'QvOdbcConnectorPackage.exe',
      qSeparated: 0,
      datasourceID: 'snowflake',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-credentials/actions/filter-orphan yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/actions/filter-orphan" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"qType":"QvOdbcConnectorPackage.exe","qSeparated":0,"datasourceID":"snowflake"}'
```

**Example Response:**

```json
{
  "data": [
    {
      "qID": "c2dd20e3-1842-42d0-81fe-1ecf08e6abde",
      "user": "rFdHeUOiVYgPX5iTbvL0x0Cs6F62QI",
      "qName": "MyCredential for REST datasource",
      "qType": "QvWebStorageProviderConnectorPackage.exe",
      "tenant": "xqFQ0k34vSR0d9G7J-vZtHZQkiYrCqc8",
      "created": "2022-04-08T10:00:28.287Z",
      "updated": "2022-04-09T10:00:28.287Z",
      "datasourceID": "rest"
    }
  ],
  "count": 1
}
```

---
