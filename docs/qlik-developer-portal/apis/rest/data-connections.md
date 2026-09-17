# Data connections

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data connections are used by Qlik Cloud Analytics apps and Data Integration projects to connect to external data sources. Credentials are stored in data-credentials.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-connections`](#get-apiv1data-connections) |  |
| `POST` | [`/api/v1/data-connections`](#post-apiv1data-connections) |  |
| `GET` | [`/api/v1/data-connections/{qID}`](#get-apiv1data-connectionsqid) |  |
| `PATCH` | [`/api/v1/data-connections/{qID}`](#patch-apiv1data-connectionsqid) |  |
| `PUT` | [`/api/v1/data-connections/{qID}`](#put-apiv1data-connectionsqid) |  |
| `DELETE` | [`/api/v1/data-connections/{qID}`](#delete-apiv1data-connectionsqid) |  |
| `POST` | [`/api/v1/data-connections/actions/delete`](#post-apiv1data-connectionsactionsdelete) |  |
| `POST` | [`/api/v1/data-connections/actions/duplicate`](#post-apiv1data-connectionsactionsduplicate) |  |
| `POST` | [`/api/v1/data-connections/actions/update`](#post-apiv1data-connectionsactionsupdate) |  |

## API Reference

### GET /api/v1/data-connections

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataName` | string | No | Provides an alternate name to be used for data[] element in GET response. |
| `extended` | boolean | No | Returns extended list of properties (e.g. encrypted credential string) when set to true. |
| `spaceId` | string | No | Filtering on connections by space ID |
| `personal` | boolean | No | Filtering on personal connections, ignored if spaceId is defined in same request |
| `owner` | string | No | Filtering on datafile connections by owner (i.e. app) ID. |
| `ownedByMe` | boolean | No | Filtering on connections, return connections owned by the caller if set to true (doesn't apply to datafiles connections) |
| `limit` | integer | No | Number of resources to be returned (between 1 and 100) |
| `sort` | string | No | Name of field sort on for pagination, with prefix with + or - indicating ascending or descending order. When used for data-connections, sort field only applies to non-datafiles connections. Whatever sorting order is, datafiles connections will be returned after all regular connections being returned. |
| `page` | string | No | Pagination cursor string, which is generated automatically in previous pagination query. |
| `noDatafiles` | boolean | No | Datafiles connections will not be returned if set to true |
| `userId` | string | No | Filtering on userId. Requires admin role if specified userId doesn't match that is defined in JWT. |
| `caseinsensitive` | boolean | No | Sort results will be returned in case insensitive order if set to true (Only used along with sort query) |
| `locale` | string | No | ICU locale ID, used only when caseinsensitive is set to true, default to 'en' if undefined |
| `includeQris` | boolean | No | Base Qri (encrypted) will be returned when the query is set to true, default is false |
| `filter` | string | No | Filtering resources by properties (filterable properties only) using SCIM filter string. Note the filter string only applies to connections managed by data-connections service, i.e. filtering doesn't apply to DataFile connections. When filtering on datetime property (e.g. created, updated), datetime should be in RFC3339 format. |
| `includeDisabled` | boolean | No | Includes connections that uses disabled datasources |

#### Responses

##### 200

List connections with optional filter queries. Connections will be filtered internally based on the space access rules applicable to the caller. When some of connections are not returned due to errors, errors array in the response will be set.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | Essential fields of a connection |
| `meta` | object | No |  |
| `links` | object | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qEngineObjectID |
| `qri` | string | No | Encrypted base Qri string (filterable using SCIM filter, e.g. filter='qri co "snowflake"') |
| `tags` | string[] | No | List of tags attached to the connection |
| `user` | string | No | User ID of the connection's creator |
| `links` | object | Yes |  |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection, i.e. provider type of underlying connector |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | integer | Yes | Indicates the type of user associated with the data connection Enum: 0, 1 |
| `tenant` | string | Yes | Tenant ID of the connection's creator |
| `created` | string | No | Datetime when the connection was created |
| `updated` | string | No | Datetime when the connection was last updated |
| `privileges` | string[] | Yes | Array of string (i.e. update, delete, read) indicating the user's privileges on the associated connection Enum: "list", "update", "delete", "read", "change_owner", "change_space" |
| `datasourceID` | string | No | Data source ID |
| `qArchitecture` | integer | Yes | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qID |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qConnectionSecret` | string | No | String that contains connection specific secret (or password). This field will not be included in response of GET /data-connections, will only be included in the response of GET /data-connections/{qID} |
| `connectionProperties` | object | No | List of connection parsed from connection string (only available when query parseConnection=true is set) |
| `qSeparateCredentials` | boolean | No | Indicates whether or not this is a credential-less connection |

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `self` | object | Yes | Link to current query |

<details>
<summary>Properties of `self`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | No | Total count of resources being requested. |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No | URL link to next page of requested resources (available to paged request only) |
| `prev` | object | No | URL link to previous page of requested resources (available to paged request only) |
| `self` | object | Yes | Link to current query |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL pointing to the next page of resources |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL pointing to the previous page of resources |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL pointing to the resource |

</details>

</details>

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

##### 400

Bad request, typically when dataName is empty

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

##### 500

Internal error, this happens when the service fails to make requests to dependency services

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

##### 502

Bad gateway, this happens when requests to required (dependent) services time out

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
// qlik-api has not implemented support for `GET /api/v1/data-connections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections',
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
# qlik-cli has not implemented support for GET /api/v1/data-connections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "qID": "a7eb530e-475a-4864-bc12-dacf4b081e72",
      "qri": "qri:db:snowflake://BQ1-3F_BvWfxxCDDiz9vQepqHLAcHWqacoqwLq4wxWM",
      "tags": "[\"tag1, \"tag2\"]",
      "user": "rFdHeUOiVYgPX5iTbvL0x0Cs6F62QI",
      "links": {
        "self": {
          "href": "https://mytenant.us.qlikcloud.com/..."
        }
      },
      "qName": "MyConnection",
      "qType": "QvOdbcConnectorPackage.exe",
      "space": "6226583d53a69876774d4f96",
      "qLogOn": 1,
      "tenant": "xqFQ0k34vSR0d9G7J-vZtHZQkiYrCqc8",
      "created": "2022-04-08T10:00:28.287Z",
      "updated": "2022-04-09T10:00:28.287Z",
      "privileges": "[update, delete, read]",
      "datasourceID": "sfdc",
      "qArchitecture": 0,
      "qCredentialsID": "a4e00184-8743-4a44-a1a8-07bba573afea",
      "qEngineObjectID": "a7eb530e-475a-4864-bc12-dacf4b081e72",
      "qConnectStatement": "CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"",
      "qConnectionSecret": "Connection_Specific_Secret",
      "connectionProperties": "{\"property1\": \"value\", \"property2\": \"value\"}",
      "qSeparateCredentials": true
    }
  ],
  "meta": {
    "count": 12
  },
  "links": {
    "next": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    },
    "prev": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    },
    "self": {
      "href": "https://mytenant.us.qlikcloud.com/.../0e445014-a564-496a-9a8d-28baadcc3ef9"
    }
  },
  "errors": [
    {
      "code": "DCERROR-0010",
      "title": "Bad or invalid request",
      "detail": "Field xxx is missing in the request",
      "status": 400
    }
  ]
}
```

---

### POST /api/v1/data-connections

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConnectionCreate` | object | No | Schema used to create a connection with given connection string (i.e. qConnectStatement) along with other metadata |

<details>
<summary>Properties of `ConnectionCreate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | No | Unique identifier (UUID) for the data connection. A UUID will be generated automatically if qID is not specified or empty |
| `tags` | string[] | No | List of tags attached to the connection (allow max 32 tags) |
| `owner` | string | No | App ID |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection - indicates connection provider type |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | string | No | Indicates the type of user associated with the data connection. Enum: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER" |
| `qPassword` | string | No | Any logon password associated with the data connection (connector encoded) |
| `qUsername` | string | No | Any logon username associated with the data connection |
| `datasourceID` | string | Yes | ID of the datasource associated with this connection |
| `qriInRequest` | string | No | QRI string of the connection. The string will be persisted to mongo when the request is originated from trusted client (i.e. dcaas) to avoid invalid QRi string. |
| `qArchitecture` | integer | No | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | No | Unique identifier (UUID) for the data connection as specified by the Sense engine. A UUID will be generated automatically if this field is not specified or empty |
| `qCredentialsName` | string | No | Name of the credential associated with the connection |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qConnectionSecret` | string | No | String that contains connection specific secret (or password) that requires encryption before persist to database. This field is connection level secret |
| `qSeparateCredentials` | boolean | No | Indicates whether or not to create a credential-less connection |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DcaasConnectionCreate` | object | No | Schema used to create a connection using a list of connection properties for given datasource |

<details>
<summary>Properties of `DcaasConnectionCreate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tags` | string[] | No | List of tags attached to the connection (allow max 31 tags) |
| `qName` | string | Yes | Descriptive name of the data connection |
| `space` | string | No | ID of the space in which the connection shall be created. Connection will be created in user's personal space if undefined |
| `authUrlOnly` | boolean | No | When set to true, only authentication URL will be returned (i.e. no connection will be created) if datasource supports OAuth, and other properties set in the request will ignored. This property will be ignored if the request is not OAuth or datasource doesn't support OAuth |
| `datasourceID` | string | Yes | ID of the datasource of the connection |
| `connectionProperties` | object | Yes | Connection properties required to create dataconnection for the given datasource, which is defined by the response of 'GET /v1/data-sources/:{datasourceId}/api-specs' |

</details>

</details>

#### Responses

##### 201

Data connection created

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | object | No |  |

<details>
<summary>Properties of `application/json`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConnectionCreateResponse` | object | No | Essential fields of a connection |

<details>
<summary>Properties of `ConnectionCreateResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qEngineObjectID |
| `user` | string | No | User ID of the connection's creator |
| `links` | object | No |  |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection - indicates connection provider type |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | string | Yes | Indicates the type of user associated with the data connection. Enum: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER" |
| `created` | string | No | Datetime when the connection was created |
| `updated` | string | No | Datetime when the connection was last updated |
| `privileges` | string[] | Yes | Array of string (i.e. update, delete, read) indicating the user's privileges on the associated connection Enum: "list", "update", "delete", "read", "change_owner", "change_space" |
| `qArchitecture` | integer | Yes | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qReferenceKey` | string | No | Reference key of credential in redis |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qID |
| `qCredentialsName` | string | No | Name of the credential associated with the connection |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qSeparateCredentials` | boolean | Yes | Indicates whether or not this is a credential-less connection |

<details>
<summary>Properties of `links`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `DcaasConnectionCreateAuthResponse` | object | No | Authentication URL response for OAuth datasources (when authUrlOnly is set to true in request) |

<details>
<summary>Properties of `DcaasConnectionCreateAuthResponse`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `authUrl` | string | Yes | Authentication URL used to generate authentication code for datasources supporting OAuth |

</details>

</details>

##### 400

Invalid data connection specified

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

User has no access to the connection or space

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

Credentials referenced by qCredentialsID in the request body could not be found

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

Data connection already exists

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
// qlik-api has not implemented support for `POST /api/v1/data-connections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      qID: 'b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28',
      tags: '["tag1, "tag2"]',
      owner:
        '928e2a66-01ba-4678-aa32-e74c213896fa',
      qName: 'MyConnection',
      qType: 'QvOdbcConnectorPackage.exe',
      space: '611bcebaeec1203d88211ac4',
      qLogOn: '1',
      qPassword: 'Connector encoded password',
      qUsername: 'MyUsername',
      datasourceID: 'snowflake',
      qriInRequest:
        'qri:db:snowflake://BQ1-3F_BvWfxxCDDiz9vQepqHLAcHWqacoqwLq4wxWM',
      qArchitecture: 0,
      qCredentialsID:
        '935ec250-65bc-47c0-965b-53554f3f87d8',
      qEngineObjectID:
        'b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28',
      qCredentialsName: 'MyCredential',
      qConnectStatement:
        'CUSTOM CONNECT TO \\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\"',
      qConnectionSecret:
        'Any connection specific secret string',
      qSeparateCredentials: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-connections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"qID":"b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28","tags":"[\"tag1, \"tag2\"]","owner":"928e2a66-01ba-4678-aa32-e74c213896fa","qName":"MyConnection","qType":"QvOdbcConnectorPackage.exe","space":"611bcebaeec1203d88211ac4","qLogOn":"1","qPassword":"Connector encoded password","qUsername":"MyUsername","datasourceID":"snowflake","qriInRequest":"qri:db:snowflake://BQ1-3F_BvWfxxCDDiz9vQepqHLAcHWqacoqwLq4wxWM","qArchitecture":0,"qCredentialsID":"935ec250-65bc-47c0-965b-53554f3f87d8","qEngineObjectID":"b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28","qCredentialsName":"MyCredential","qConnectStatement":"CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"","qConnectionSecret":"Any connection specific secret string","qSeparateCredentials":false}'
```

**Example Response:**

```json
{
  "qID": "b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28",
  "user": "rFdHeUOiVYgPX5iTbvL0x0Cs6F62QI",
  "links": {
    "self": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    }
  },
  "qName": "MyConnection",
  "qType": "QvOdbcConnectorPackage.exe",
  "space": "611bcebaeec1203d88211ac4",
  "qLogOn": "1",
  "created": "2022-04-09T10:00:28.287Z",
  "updated": "2022-04-09T10:00:28.287Z",
  "privileges": "[update, delete, read]",
  "qArchitecture": 0,
  "qReferenceKey": "credential:key",
  "qCredentialsID": "7b475581-2f68-4c81-ac52-25705b8229fb",
  "qEngineObjectID": "b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28",
  "qCredentialsName": "MyCredential",
  "qConnectStatement": "CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"",
  "qSeparateCredentials": true
}
```

---

### GET /api/v1/data-connections/{qID}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Connection ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `extended` | boolean | No | Returns extended list of properties (e.g. encrypted credential string) when set to true. |
| `type` | string | No | The connection ID in the path becomes a connection name when this query parameter is set. Enum: "connectionname" |
| `credentialId` | string | No | Credential ID |
| `byCredentialName` | boolean | No | If set to true, credentialId in the query will be interpreted as credential's name |
| `spaceId` | string | No | Filtering on connections by space ID |
| `noCache` | boolean | No | datafiles connections will be returned from cache by default (if data-connections is configured to use cache), this query parameter is used disable this default behavior, e.g. return an update-to-date datafiles connection if the query is set to true |
| `parseConnection` | boolean | No | List of connection properties shall be returned when the query is set to true, default is false |

#### Responses

##### 200

Data connection retrieved

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qEngineObjectID |
| `qri` | string | No | Encrypted base Qri string (filterable using SCIM filter, e.g. filter='qri co "snowflake"') |
| `tags` | string[] | No | List of tags attached to the connection |
| `user` | string | No | User ID of the connection's creator |
| `links` | object | Yes |  |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection, i.e. provider type of underlying connector |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | integer | Yes | Indicates the type of user associated with the data connection Enum: 0, 1 |
| `tenant` | string | Yes | Tenant ID of the connection's creator |
| `created` | string | No | Datetime when the connection was created |
| `updated` | string | No | Datetime when the connection was last updated |
| `privileges` | string[] | Yes | Array of string (i.e. update, delete, read) indicating the user's privileges on the associated connection Enum: "list", "update", "delete", "read", "change_owner", "change_space" |
| `datasourceID` | string | No | Data source ID |
| `qArchitecture` | integer | Yes | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qID |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qConnectionSecret` | string | No | String that contains connection specific secret (or password). This field will not be included in response of GET /data-connections, will only be included in the response of GET /data-connections/{qID} |
| `connectionProperties` | object | No | List of connection parsed from connection string (only available when query parseConnection=true is set) |
| `qSeparateCredentials` | boolean | No | Indicates whether or not this is a credential-less connection |

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

The qID is not a valid UUID

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

User has no access to the connection or space

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

Data connection not found

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

##### 500

Credential decryption failed, likely due to invalid credentials

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
// qlik-api has not implemented support for `GET /api/v1/data-connections/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/{qID}',
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
# qlik-cli has not implemented support for GET /api/v1/data-connections/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/{qID}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "qID": "a7eb530e-475a-4864-bc12-dacf4b081e72",
  "qri": "qri:db:snowflake://BQ1-3F_BvWfxxCDDiz9vQepqHLAcHWqacoqwLq4wxWM",
  "tags": "[\"tag1, \"tag2\"]",
  "user": "rFdHeUOiVYgPX5iTbvL0x0Cs6F62QI",
  "links": {
    "self": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    }
  },
  "qName": "MyConnection",
  "qType": "QvOdbcConnectorPackage.exe",
  "space": "6226583d53a69876774d4f96",
  "qLogOn": 1,
  "tenant": "xqFQ0k34vSR0d9G7J-vZtHZQkiYrCqc8",
  "created": "2022-04-08T10:00:28.287Z",
  "updated": "2022-04-09T10:00:28.287Z",
  "privileges": "[update, delete, read]",
  "datasourceID": "sfdc",
  "qArchitecture": 0,
  "qCredentialsID": "a4e00184-8743-4a44-a1a8-07bba573afea",
  "qEngineObjectID": "a7eb530e-475a-4864-bc12-dacf4b081e72",
  "qConnectStatement": "CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"",
  "qConnectionSecret": "Connection_Specific_Secret",
  "connectionProperties": "{\"property1\": \"value\", \"property2\": \"value\"}",
  "qSeparateCredentials": true
}
```

---

### PATCH /api/v1/data-connections/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Connection ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | The connection ID in the path becomes a connection name when this query parameter is set. Enum: "connectionname" |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qlik-auth-code` | string | No | OAuth authentication code. This header is required by certain datasources when patching a data connection. |

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

Data connection updated successfully

##### 400

Bad request due to invalid data in body

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

User has no access to the connection or space

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

Data connection not found

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

Data connection already exists (when updated name conflicts with existing record)

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
// qlik-api has not implemented support for `PATCH /api/v1/data-connections/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/{qID}',
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
# qlik-cli has not implemented support for PATCH /api/v1/data-connections/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/{qID}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/qName","value":"New value"}]'
```

---

### PUT /api/v1/data-connections/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Connection ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | The connection ID in the path becomes a connection name when this query parameter is set. Enum: "connectionname" |
| `spaceId` | string | No | Filtering on connections by space ID |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Unique identifier for the data connection |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection - indicates connection provider type |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | string | No | Indicates the type of user associated with the data connection. Enum: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER" |
| `qPassword` | string | No | Any logon password associated with the data connection |
| `qUsername` | string | No | Any logon username associated with the data connection |
| `datasourceID` | string | No | ID of the datasource associated with this connection |
| `qArchitecture` | integer | No | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | Yes | Unique identifier for the data connection as specified by the Sense engine |
| `qCredentialsName` | string | No | Name of the credential associated with the connection |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qConnectionSecret` | string | No | String that contains connection level secret (or password). If this field presents in request, then existing connection secret will be updated to its value. If is an empty string, then existing connection secret will be cleared. If this field is missing, existing secret will not be updated. |
| `qSeparateCredentials` | boolean | No | Indicates whether or not this is a credential-less connection |

#### Responses

##### 204

Data connection updated successfully

##### 400

Bad request due to invalid data in body

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

User has no access to the connection or space

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

Data connection not found

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

Data connection already exists (when updated name conflicts with existing record)

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
// qlik-api has not implemented support for `PUT /api/v1/data-connections/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/{qID}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      qID: '55e13286-fbd8-4a59-a10d-807937a97443',
      qName: 'MyConnection',
      qType: 'snowflake',
      space: '611bcebaeec1203d88211ac4',
      qLogOn: '1',
      qPassword: 'password',
      qUsername: 'MyUsername',
      datasourceID: 'snowflake',
      qArchitecture: 1,
      qCredentialsID:
        'cea94172-fa83-47c8-8171-b6f151918ad0',
      qEngineObjectID:
        '55e13286-fbd8-4a59-a10d-807937a97443',
      qCredentialsName: 'CredentialName',
      qConnectStatement:
        'CUSTOM CONNECT TO \\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\"',
      qConnectionSecret:
        'connection specific secret string',
      qSeparateCredentials: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-connections/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/{qID}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"qID":"55e13286-fbd8-4a59-a10d-807937a97443","qName":"MyConnection","qType":"snowflake","space":"611bcebaeec1203d88211ac4","qLogOn":"1","qPassword":"password","qUsername":"MyUsername","datasourceID":"snowflake","qArchitecture":1,"qCredentialsID":"cea94172-fa83-47c8-8171-b6f151918ad0","qEngineObjectID":"55e13286-fbd8-4a59-a10d-807937a97443","qCredentialsName":"CredentialName","qConnectStatement":"CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"","qConnectionSecret":"connection specific secret string","qSeparateCredentials":true}'
```

---

### DELETE /api/v1/data-connections/{qID}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Connection ID |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No | The connection ID in the path becomes a connection name when this query parameter is set. Enum: "connectionname" |
| `spaceId` | string | No | Filtering on connections by space ID |

#### Responses

##### 204

Data connection deleted successfully

##### 403

User has no access to the connection or space

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

Data connection not found

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
// qlik-api has not implemented support for `DELETE /api/v1/data-connections/{qID}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/{qID}',
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
# qlik-cli has not implemented support for DELETE /api/v1/data-connections/{qID} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/{qID}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/data-connections/actions/delete

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connections` | object[] | Yes |  |

<details>
<summary>Properties of `connections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of connection |
| `name` | string | No | Connection name |

</details>

#### Responses

##### 207

Bulk delete completed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of the resource |
| `error` | object | No |  |
| `status` | integer | Yes | Status code of operation on resource identified by ID |

<details>
<summary>Properties of `error`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

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

User has no access to the endpoint. The endpoint requires Admin role

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
// qlik-api has not implemented support for `POST /api/v1/data-connections/actions/delete` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/actions/delete',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      connections: [
        {
          id: 'b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd',
          name: 'MyConnection',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-connections/actions/delete yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/actions/delete" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"connections":[{"id":"b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd","name":"MyConnection"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd",
      "error": {
        "code": "DCERROR-0010",
        "title": "Bad or invalid request",
        "detail": "Field xxx is missing in the request",
        "status": 400
      },
      "status": 204
    }
  ]
}
```

---

### POST /api/v1/data-connections/actions/duplicate

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of the source connection being duplicated |
| `name` | string | No | Optional name for the duplicated connection, must be unique in the target scope. If not specified, a name will be automatically generated |
| `spaceId` | string | No | Optional target space ID for the duplicated connection. If not specified, the duplicated connection will be in the same space as the source connection |
| `qPassword` | string | No | Optional credential password, specify to override credential embedded (or associated) with the source connection |
| `qUsername` | string | No | Optional credential username, specify to override credential embedded (or associated) with the source connection |

#### Responses

##### 201

Duplicate completed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qEngineObjectID |
| `user` | string | No | User ID of the connection's creator |
| `links` | object | No |  |
| `qName` | string | Yes | Descriptive name of the data connection |
| `qType` | string | Yes | Type of connection - indicates connection provider type |
| `space` | string | No | ID of the space to which the connection belongs |
| `qLogOn` | string | Yes | Indicates the type of user associated with the data connection. Enum: "0", "1", "LOG_ON_SERVICE_USER", "LOG_ON_CURRENT_USER" |
| `created` | string | No | Datetime when the connection was created |
| `updated` | string | No | Datetime when the connection was last updated |
| `privileges` | string[] | Yes | Array of string (i.e. update, delete, read) indicating the user's privileges on the associated connection Enum: "list", "update", "delete", "read", "change_owner", "change_space" |
| `qArchitecture` | integer | Yes | 0 or 1 value indicating whether the data connector is 64-bit (0) or 32-bit (1). Defaults to 0 if not specified. Enum: 0, 1 |
| `qReferenceKey` | string | No | Reference key of credential in redis |
| `qCredentialsID` | string | No | ID of the credential associated with the connection |
| `qEngineObjectID` | string | Yes | Unique identifier (UUID) for the data connection, must be same as qID |
| `qCredentialsName` | string | No | Name of the credential associated with the connection |
| `qConnectStatement` | string | Yes | Connection string for the data connection |
| `qSeparateCredentials` | boolean | Yes | Indicates whether or not this is a credential-less connection |

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

Bad request (Missing required field in request body, or duplicate from / to a reserved connection)

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

User has no access to the source connection or no access to target space

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

Connection defined by id not found

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

Duplicated connection would result in a name conflict with the connections in the scope

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
// qlik-api has not implemented support for `POST /api/v1/data-connections/actions/duplicate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/actions/duplicate',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 'b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd',
      name: 'ResourceName',
      spaceId: '611bcebaeec1203d88211ac4',
      qPassword: 'Password',
      qUsername: 'UserName',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-connections/actions/duplicate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/actions/duplicate" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"id":"b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd","name":"ResourceName","spaceId":"611bcebaeec1203d88211ac4","qPassword":"Password","qUsername":"UserName"}'
```

**Example Response:**

```json
{
  "qID": "b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28",
  "user": "rFdHeUOiVYgPX5iTbvL0x0Cs6F62QI",
  "links": {
    "self": {
      "href": "https://mytenant.us.qlikcloud.com/..."
    }
  },
  "qName": "MyConnection",
  "qType": "QvOdbcConnectorPackage.exe",
  "space": "611bcebaeec1203d88211ac4",
  "qLogOn": "1",
  "created": "2022-04-09T10:00:28.287Z",
  "updated": "2022-04-09T10:00:28.287Z",
  "privileges": "[update, delete, read]",
  "qArchitecture": 0,
  "qReferenceKey": "credential:key",
  "qCredentialsID": "7b475581-2f68-4c81-ac52-25705b8229fb",
  "qEngineObjectID": "b4a949cb-3aaf-4cd5-a140-dd3ea34f0d28",
  "qCredentialsName": "MyCredential",
  "qConnectStatement": "CUSTOM CONNECT TO \\\"provider=QvOdbcConnectorPackage.exe;driver=snowflake;server=...\\\"",
  "qSeparateCredentials": true
}
```

---

### POST /api/v1/data-connections/actions/update

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connections` | object[] | Yes |  |

<details>
<summary>Properties of `connections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Connection ID |
| `name` | string | No | Connection name |
| `ownerId` | string | No | User ID to which the connection will be updated. If not present, the connection's owner wont be changed |
| `spaceId` | string | No | Space ID to which the connection will be updated. If not present, the connection's space wont be changed. If it is empty string, then the connection will be moved to the personal space of the user identified by ownerId (If ownerId is undefined, then the connection will be in oroginal owner's personal space) |
| `spaceType` | string | No | Space type. Required when spaceId is specified Enum: "personal", "shared", "managed", "data" |

</details>

#### Responses

##### 207

Bulk update completed

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | ID of the resource |
| `error` | object | No |  |
| `status` | integer | Yes | Status code of operation on resource identified by ID |

<details>
<summary>Properties of `error`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Unique internal error code |
| `title` | string | No | A summary in english explaining what went wrong |
| `detail` | string | No | More concrete details |
| `status` | integer | No | HTTP status code |

</details>

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

User has no access to the endpoint. The endpoint requires Admin role

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
// qlik-api has not implemented support for `POST /api/v1/data-connections/actions/update` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-connections/actions/update',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      connections: [
        {
          id: 'b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd',
          name: 'MyConnection',
          ownerId:
            '6K9xjsItDexffSlu5vg1oWYkY8x7f-06',
          spaceId: '611bcebaeec1203d88211ac4',
          spaceType: 'personal',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-connections/actions/update yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections/actions/update" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"connections":[{"id":"b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd","name":"MyConnection","ownerId":"6K9xjsItDexffSlu5vg1oWYkY8x7f-06","spaceId":"611bcebaeec1203d88211ac4","spaceType":"personal"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "b2c1ab1f-392c-4cd1-87bd-4c3cd256f5fd",
      "error": {
        "code": "DCERROR-0010",
        "title": "Bad or invalid request",
        "detail": "Field xxx is missing in the request",
        "status": 400
      },
      "status": 204
    }
  ]
}
```

---
