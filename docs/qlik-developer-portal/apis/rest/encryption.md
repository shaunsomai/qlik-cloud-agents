# Encryption

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Tenants in Qlik Cloud can be encrypted with a key you provide via a supported KMS. This API allows you to configure and manage encryption keys.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/encryption/keyproviders`](#get-apiv1encryptionkeyproviders) | Returns a list of AWS key providers in the tenant. Use /actions/list to return all key providers. |
| `POST` | [`/api/v1/encryption/keyproviders`](#post-apiv1encryptionkeyproviders) | The AWS-KMS key configuration must match the Qlik Cloud region configuration requirements. Most regions should have a key deployed to the same AWS region as the Qlik Cloud tenant, with a replica key in the relevant Qlik Cloud DR region. Consult the documentation for DR region mappings. |
| `GET` | [`/api/v1/encryption/keyproviders/{arnFingerPrint}`](#get-apiv1encryptionkeyprovidersarnfingerprint) | Retrieve key provider detail by passing the ARN fingerprint as parameter. |
| `PATCH` | [`/api/v1/encryption/keyproviders/{arnFingerPrint}`](#patch-apiv1encryptionkeyprovidersarnfingerprint) | Update the name and/or description of a key provider. |
| `DELETE` | [`/api/v1/encryption/keyproviders/{arnFingerPrint}`](#delete-apiv1encryptionkeyprovidersarnfingerprint) | Delete a key configuration from the tenant. Not supported for the default Qlik managed key provider. Key must not be in use. |
| `POST` | [`/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate`](#post-apiv1encryptionkeyprovidersarnfingerprintactionsmigrate) | Migrate the active key from one provider to another. The migration process may take some time to complete, however this process will not impact users, and the tenant will continue to function normally during the migration. Use the migration details endpoint to monitor migration progress. |
| `POST` | [`/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test`](#post-apiv1encryptionkeyprovidersarnfingerprintactionstest) | Validate a key to check if Qlik Cloud has required access to your AWS account and key policy, and the key configuration. If the key policy or configuration are changed from the required configuration, this may impact your ability to access your tenant. |
| `GET` | [`/api/v1/encryption/keyproviders/actions/list`](#get-apiv1encryptionkeyprovidersactionslist) | Returns a list of all key providers in the tenant, including the default Qlik key provider. |
| `POST` | [`/api/v1/encryption/keyproviders/actions/reset-to-default-provider`](#post-apiv1encryptionkeyprovidersactionsreset-to-default-provider) | Reset the encryption key back to the default Qlik managed provider. No action will be taken if tenant is already using the Qlik provider. |
| `GET` | [`/api/v1/encryption/keyproviders/migration/actions/details`](#get-apiv1encryptionkeyprovidersmigrationactionsdetails) | Retrieve details for the ongoing or last completed migration for the tenant. |

## API Reference

### GET /api/v1/encryption/keyproviders

Returns a list of AWS key providers in the tenant. Use /actions/list to return all key providers.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Successfully retrieved list of key providers

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `current` | boolean | No | Indicates whether the key is being used to encrypt/decrypt secrets. |
| `tenantId` | string | No | Tenant ID. |
| `createdAt` | string | No | When key entry was created. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |
| `multiRegion` | boolean | No | Indicates whether the key has multi-region configurations and has replica key in qcs secondary region. |
| `replicaKeys` | object[] | No |  |
| `arnFingerPrint` | string | No | The ARN fingerprint. |
| `promotedToCurrentAt` | string | No | When the key was promoted to being the current active one. |
| `demotedFromCurrentAt` | string | No | When the key was demoted from being current to non active. |

<details>
<summary>Properties of `replicaKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | No | Replica key keeps list of backup keys from the supported qcs secondary region. |
| `region` | string | No | Region indicates the backup qcs-region link to the primary region. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to load list of key providers

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/encryption/keyproviders` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders',
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
# qlik-cli has not implemented support for GET /api/v1/encryption/keyproviders yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
    "name": "test name",
    "current": true,
    "description": "test description",
    "drCompliant": true,
    "keyprovider": "AWS-KMS",
    "multiRegion": true,
    "replicaKeys": [
      {
        "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
        "region": "eu-west-3"
      }
    ],
    "complianceError": {
      "code": "",
      "region": "",
      "message": ""
    }
  }
]
```

---

### POST /api/v1/encryption/keyproviders

The AWS-KMS key configuration must match the Qlik Cloud region configuration requirements. Most regions should have a key deployed to the same AWS region as the Qlik Cloud tenant, with a replica key in the relevant Qlik Cloud DR region. Consult the documentation for DR region mappings.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |

#### Responses

##### 201

Successfully registered the provided AWS-KMS key

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `current` | boolean | No | Indicates whether the key is being used to encrypt/decrypt secrets. |
| `tenantId` | string | No | Tenant ID. |
| `createdAt` | string | No | When key entry was created. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |
| `multiRegion` | boolean | No | Indicates whether the key has multi-region configurations and has replica key in qcs secondary region. |
| `replicaKeys` | object[] | No |  |
| `arnFingerPrint` | string | No | The ARN fingerprint. |
| `promotedToCurrentAt` | string | No | When the key was promoted to being the current active one. |
| `demotedFromCurrentAt` | string | No | When the key was demoted from being current to non active. |

<details>
<summary>Properties of `replicaKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | No | Replica key keeps list of backup keys from the supported qcs secondary region. |
| `region` | string | No | Region indicates the backup qcs-region link to the primary region. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 403

Unable to access the provided AWS-KMS key, access is forbidden. Check if AWS key policy allows access from Qlik Cloud.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 406

Failed to register the provided AWS-KMS key

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 408

Failed to return a response within the timeout window. The key provider (QlikVault, AWS-KMS) might be unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 409

The provided key is already registered

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to validate AWS-KMS ARN structure

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/encryption/keyproviders` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      arn: 'arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456',
      name: 'test name',
      current: false,
      description: 'test description',
      drCompliant: true,
      keyprovider: 'AWS-KMS',
      multiRegion: true,
      replicaKeys: [
        {
          arn: 'arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456',
          region: 'eu-west-3',
        },
      ],
      complianceError: [
        { code: '', region: '', message: '' },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/encryption/keyproviders yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders" \
-X POST \
-H "Authorization: Bearer <access_token>" \
-H "Content-type: application/json" \
-d '{"arn":"arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456","name":"test name","current":false,"description":"test description","drCompliant":true,"keyprovider":"AWS-KMS","multiRegion":true,"replicaKeys":[{"arn":"arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456","region":"eu-west-3"}],"complianceError":[{"code":"","region":"","message":""}]}'
```

**Example Response:**

```json
{
  "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
  "name": "test name",
  "current": false,
  "description": "test description",
  "drCompliant": true,
  "keyprovider": "AWS-KMS",
  "multiRegion": true,
  "replicaKeys": [
    {
      "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
      "region": "eu-west-3"
    }
  ],
  "complianceError": [
    {
      "code": "",
      "region": "",
      "message": ""
    }
  ]
}
```

---

### GET /api/v1/encryption/keyproviders/{arnFingerPrint}

Retrieve key provider detail by passing the ARN fingerprint as parameter.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arnFingerPrint` | string | Yes | The fingerprint of the requested provider key. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Successfully fetched key provider information

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `current` | boolean | No | Indicates whether the key is being used to encrypt/decrypt secrets. |
| `tenantId` | string | No | Tenant ID. |
| `createdAt` | string | No | When key entry was created. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |
| `multiRegion` | boolean | No | Indicates whether the key has multi-region configurations and has replica key in qcs secondary region. |
| `replicaKeys` | object[] | No |  |
| `arnFingerPrint` | string | No | The ARN fingerprint. |
| `promotedToCurrentAt` | string | No | When the key was promoted to being the current active one. |
| `demotedFromCurrentAt` | string | No | When the key was demoted from being current to non active. |

<details>
<summary>Properties of `replicaKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | No | Replica key keeps list of backup keys from the supported qcs secondary region. |
| `region` | string | No | Region indicates the backup qcs-region link to the primary region. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

No entry match for the fingerprint was found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 414

Requested fingerprint length is too large

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/encryption/keyproviders/{arnFingerPrint}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/{arnFingerPrint}',
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
# qlik-cli has not implemented support for GET /api/v1/encryption/keyproviders/{arnFingerPrint} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/{arnFingerPrint}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
  "name": "test name",
  "current": false,
  "description": "test description",
  "drCompliant": true,
  "keyprovider": "AWS-KMS",
  "multiRegion": true,
  "replicaKeys": [
    {
      "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
      "region": "eu-west-3"
    }
  ],
  "complianceError": [
    {
      "code": "",
      "region": "",
      "message": ""
    }
  ]
}
```

---

### PATCH /api/v1/encryption/keyproviders/{arnFingerPrint}

Update the name and/or description of a key provider.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arnFingerPrint` | string | Yes | The ARN fingerprint of an existing key provider key. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace" |
| `path` | string | Yes | The property path. |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 204

Successfully patched key provider information

##### 400

Failed to decode key provider patch request payload

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

No entry match for the fingerprint was found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to patch key provider information

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/encryption/keyproviders/{arnFingerPrint}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/{arnFingerPrint}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/name',
        value: 'New Encryption Key',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/encryption/keyproviders/{arnFingerPrint} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/{arnFingerPrint}" \
-X PATCH \
-H "Authorization: Bearer <access_token>" \
-H "Content-type: application/json" \
-d '[{"op":"replace","path":"/name","value":"New Encryption Key"}]'
```

---

### DELETE /api/v1/encryption/keyproviders/{arnFingerPrint}

Delete a key configuration from the tenant. Not supported for the default Qlik managed key provider. Key must not be in use.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arnFingerPrint` | string | Yes | The fingerprint of the key provider you wish to delete. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 204

Successfully deleted key

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `response` | string | No | Successful response message. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

No entry match for the fingerprint was found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to delete key provider information

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 424

The requested key is being used and cannot be deleted

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/encryption/keyproviders/{arnFingerPrint}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/{arnFingerPrint}',
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
# qlik-cli has not implemented support for DELETE /api/v1/encryption/keyproviders/{arnFingerPrint} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/{arnFingerPrint}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "Key provider metadata deleted successfully"
}
```

---

### POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate

Migrate the active key from one provider to another. The migration process may take some time to complete, however this process will not impact users, and the tenant will continue to function normally during the migration. Use the migration details endpoint to monitor migration progress.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arnFingerPrint` | string | Yes | The fingerprint of an existing key provider key. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Successfully initiated cipherkeys migration

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Migration operation ID. |
| `state` | string | No | Migration operation state. Enum: "New", "InProgress", "Completed" |
| `progress` | number | No | Progress in percentage. |
| `tenantId` | string | No | Tenant ID. |
| `completedAt` | string | No |  |
| `initiatedAt` | string | No |  |
| `migratingTo` | string | No | The new key ARN that keys should be migrated to. |
| `migratingFrom` | string | No | The key ARN being migrated from (in case of QlikVault, could be a short name only). |
| `migratingToPrefix` | string | No | The new key prefix (to help services know which prefix should NOT be migrated). |
| `migratingToFingerprint` | string | No | The new key ARN fingerprint. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

No entry match for the fingerprint was found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 412

Failed to initiate migration

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 424

Failed to prepare migration

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 428

There is already an ongoing migration for the tenant

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate',
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
# qlik-cli has not implemented support for POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/migrate" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "state": "New",
  "progress": 42,
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "completedAt": "2018-10-30T07:06:22Z",
  "initiatedAt": "2018-10-30T07:06:22Z",
  "migratingTo": "string",
  "migratingFrom": "string",
  "migratingToPrefix": "string",
  "migratingToFingerprint": "string"
}
```

---

### POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test

Validate a key to check if Qlik Cloud has required access to your AWS account and key policy, and the key configuration. If the key policy or configuration are changed from the required configuration, this may impact your ability to access your tenant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arnFingerPrint` | string | Yes | The fingerprint of an existing key provider key. |

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 201

Successfully validated key

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `current` | boolean | No | Indicates whether the key is being used to encrypt/decrypt secrets. |
| `tenantId` | string | No | Tenant ID. |
| `createdAt` | string | No | When key entry was created. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |
| `multiRegion` | boolean | No | Indicates whether the key has multi-region configurations and has replica key in qcs secondary region. |
| `replicaKeys` | object[] | No |  |
| `arnFingerPrint` | string | No | The ARN fingerprint. |
| `promotedToCurrentAt` | string | No | When the key was promoted to being the current active one. |
| `demotedFromCurrentAt` | string | No | When the key was demoted from being current to non active. |

<details>
<summary>Properties of `replicaKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | No | Replica key keeps list of backup keys from the supported qcs secondary region. |
| `region` | string | No | Region indicates the backup qcs-region link to the primary region. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

No entry match for the fingerprint was found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 408

Failed to return a response within the timeout window. The key provider (QlikVault, AWS-KMS) might be unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test',
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
# qlik-cli has not implemented support for POST /api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/{arnFingerPrint}/actions/test" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
  "name": "test name",
  "current": false,
  "description": "test description",
  "drCompliant": true,
  "keyprovider": "AWS-KMS",
  "multiRegion": true,
  "replicaKeys": [
    {
      "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
      "region": "eu-west-3"
    }
  ],
  "complianceError": [
    {
      "code": "",
      "region": "",
      "message": ""
    }
  ]
}
```

---

### GET /api/v1/encryption/keyproviders/actions/list

Returns a list of all key providers in the tenant, including the default Qlik key provider.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Successfully retrieved list of key providers

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | Yes | The provider resource notation for the key. |
| `name` | string | Yes | Name of key provider entry. |
| `current` | boolean | No | Indicates whether the key is being used to encrypt/decrypt secrets. |
| `tenantId` | string | No | Tenant ID. |
| `createdAt` | string | No | When key entry was created. |
| `description` | string | No | Description of key provider entry. |
| `keyprovider` | string | Yes | Key Provider type. Enum: "AWS-KMS" |
| `multiRegion` | boolean | No | Indicates whether the key has multi-region configurations and has replica key in qcs secondary region. |
| `replicaKeys` | object[] | No |  |
| `arnFingerPrint` | string | No | The ARN fingerprint. |
| `promotedToCurrentAt` | string | No | When the key was promoted to being the current active one. |
| `demotedFromCurrentAt` | string | No | When the key was demoted from being current to non active. |

<details>
<summary>Properties of `replicaKeys`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `arn` | string | No | Replica key keeps list of backup keys from the supported qcs secondary region. |
| `region` | string | No | Region indicates the backup qcs-region link to the primary region. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to load list of key providers

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/encryption/keyproviders/actions/list` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/actions/list',
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
# qlik-cli has not implemented support for GET /api/v1/encryption/keyproviders/actions/list yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/actions/list" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "arn": "#QLIK_MANAGED_KEY_PROVIDER#",
    "name": "Qlik Internal Kms",
    "tenantId": "ImTRa-bkJTD-NZRYjNBa_rDhwSVA6Qo8",
    "createdAt": "Qlik managed",
    "description": "Default key management service",
    "keyprovider": "Qlik",
    "arnFingerPrint": "ImTRa-bkJTD-NZRYjNBa_rDhwSVA6Qo8",
    "promotedToCurrentAt": "2023-06-21T18:45:57Z",
    "demotedFromCurrentAt": "0001-01-01T00:00:00Z"
  },
  {
    "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
    "name": "CMK - 01",
    "tenantId": "ImTRa-bkJTD-NZRYjNBa_rDhwSVA6Qo8",
    "createdAt": "2023-06-21T18:43:49Z",
    "drCompliant": true,
    "keyprovider": "AWS-KMS",
    "multiRegion": true,
    "replicaKeys": [
      {
        "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-1237c011a37erft67ei987c7612q456",
        "region": "eu-west-3"
      }
    ],
    "arnFingerPrint": "9f352c5a9c1618485051892cb57467e4",
    "complianceError": {
      "code": "",
      "region": "",
      "message": ""
    },
    "promotedToCurrentAt": "2023-06-21T18:43:54Z",
    "demotedFromCurrentAt": "2023-06-21T18:45:57Z"
  },
  {
    "arn": "arn:aws:kms:eu-west-1:111222334455:key/mrk-2678f8123w236c3123469387dc2ce561",
    "name": "CMK - 02",
    "current": true,
    "tenantId": "ImTRa-bkJTD-NZRYjNBa_rDhwSVA6Qo8",
    "createdAt": "2023-06-21T18:59:17Z",
    "description": "CMK migration test",
    "drCompliant": false,
    "keyprovider": "AWS-KMS",
    "multiRegion": true,
    "replicaKeys": [
      {
        "arn": "arn:aws:kms:eu-west-3:111222334455:key/mrk-2678f8123w236c3123469387dc2ce561",
        "region": "eu-west-3"
      }
    ],
    "arnFingerPrint": "12342c83b25f9e36543bca28f69e4210",
    "complianceError": {
      "code": "Encryption-88",
      "region": "eu-west-3",
      "message": "The policy of the provided key does not allow the required action [eu-west-3] [GenerateDataKey]."
    },
    "promotedToCurrentAt": "2023-06-21T18:59:18Z",
    "demotedFromCurrentAt": "0001-01-01T00:00:00Z"
  }
]
```

---

### POST /api/v1/encryption/keyproviders/actions/reset-to-default-provider

Reset the encryption key back to the default Qlik managed provider. No action will be taken if tenant is already using the Qlik provider.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Tenant is already using Qlik Managed provider, no action taken

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No | Tenant is already using Qlik KMS, no migration is required. |

##### 205

Successfully initiated key migration to Qlik managed provider

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Migration operation ID. |
| `state` | string | No | Migration operation state. Enum: "New", "InProgress", "Completed" |
| `progress` | number | No | Progress in percentage. |
| `tenantId` | string | No | Tenant ID. |
| `completedAt` | string | No |  |
| `initiatedAt` | string | No |  |
| `migratingTo` | string | No | The new key ARN that keys should be migrated to. |
| `migratingFrom` | string | No | The key ARN being migrated from (in case of QlikVault, could be a short name only). |
| `migratingToPrefix` | string | No | The new key prefix (to help services know which prefix should NOT be migrated). |
| `migratingToFingerprint` | string | No | The new key ARN fingerprint. |

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 406

There is already an ongoing migration in progress for this tenant, this must complete before a new migration can be started

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 412

Failed to initiate migration to Qlik managed provider

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 424

Tenant is already using Qlik Managed provider

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/encryption/keyproviders/actions/reset-to-default-provider` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/actions/reset-to-default-provider',
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
# qlik-cli has not implemented support for POST /api/v1/encryption/keyproviders/actions/reset-to-default-provider yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/actions/reset-to-default-provider" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "Tenant is already using Qlik KMS, no migration is required."
}
```

---

### GET /api/v1/encryption/keyproviders/migration/actions/details

Retrieve details for the ongoing or last completed migration for the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | string | Yes | The JWT used for authentication. Send the JWT in the request header using the Bearer schema. |

#### Responses

##### 200

Successfully fetched migration information

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | Migration operation ID. |
| `state` | string | No | Migration operation state. Enum: "New", "InProgress", "Completed" |
| `progress` | number | No | Progress in percentage. |
| `tenantId` | string | No | Tenant ID. |
| `completedAt` | string | No |  |
| `initiatedAt` | string | No |  |
| `migratingTo` | string | No | The new key ARN that keys should be migrated to. |
| `migratingFrom` | string | No | The key ARN being migrated from (in case of QlikVault, could be a short name only). |
| `migratingToPrefix` | string | No | The new key prefix (to help services know which prefix should NOT be migrated). |
| `migratingToFingerprint` | string | No | The new key ARN fingerprint. |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 401

Unauthorized, invalid JWT

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 404

There is no ongoing migration for this tenant

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

##### 417

Failed to get ongoing migration information

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `meta` | object | No | Additional error object metadata. |
| `title` | string | Yes | Description of the error. |
| `detail` | string | No | Extra information about the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/encryption/keyproviders/migration/actions/details` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/encryption/keyproviders/migration/actions/details',
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
# qlik-cli has not implemented support for GET /api/v1/encryption/keyproviders/migration/actions/details yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders/migration/actions/details" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "state": "New",
  "progress": 42,
  "tenantId": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "completedAt": "2018-10-30T07:06:22Z",
  "initiatedAt": "2018-10-30T07:06:22Z",
  "migratingTo": "string",
  "migratingFrom": "string",
  "migratingToPrefix": "string",
  "migratingToFingerprint": "string"
}
```

---
