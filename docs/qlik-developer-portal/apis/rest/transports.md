# Email configuration

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Transports supports configuration of the tenant-level SMTP service. For the SMTP service in Qlik Automate, review the automation-connections API.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/transports/email-config`](#get-apiv1transportsemail-config) | Returns the current email configuration and configuration status for the tenant. |
| `PATCH` | [`/api/v1/transports/email-config`](#patch-apiv1transportsemail-config) | Patches the email configuration for the tenant. This endpoint is deprecated, use `PUT /transports/email-config` to replace the entire configuration instead. |
| `PUT` | [`/api/v1/transports/email-config`](#put-apiv1transportsemail-config) | Creates or replaces the email configuration for the tenant. Validation of the configuration is done as part of the request. |
| `DELETE` | [`/api/v1/transports/email-config`](#delete-apiv1transportsemail-config) | Deletes the email configuration for the tenant. |
| `POST` | [`/api/v1/transports/email-config/actions/send-test-email`](#post-apiv1transportsemail-configactionssend-test-email) | Attempts to sends a test email using the active configuration, with the supplied email info (subject, body, recipient). |
| `POST` | [`/api/v1/transports/email-config/actions/validate`](#post-apiv1transportsemail-configactionsvalidate) | Returns the current isValid value for the email configuration for the tenant. Does not attempt to connect to a server to verify the connection or send a test email. Will return false if no email configuration exists. |
| `POST` | [`/api/v1/transports/email-config/actions/verify-connection`](#post-apiv1transportsemail-configactionsverify-connection) | Attempts to verify connection to email server using a low-level protocol handshake to confirm the server is reachable and the credentials are valid, without sending a test email. |

## API Reference

### GET /api/v1/transports/email-config

Returns the current email configuration and configuration status for the tenant.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

Email configuration. If configuration does not exist in database then { isValid false, passwordExists false} is returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | object | No | Contains statusCode and statusReason |
| `isValid` | boolean | No | Is the configuration valid |
| `tenantId` | string | No | The tenant Id |
| `username` | string | No | user name |
| `errorCode` | string | No | Indicates error with this email configuration. OK means that no error is indicated. Possible values are OK, CONFIG_NOT_SET, INCOMPLETE_CONFIG, INVALID_CREDENTIALS, PROVIDER_ERROR |
| `serverPort` | number | No | smtp server listening port |
| `lastUpdated` | string | No |  |
| `authFailures` | number | No | Number of authentication failures |
| `emailAddress` | string | No | used for SMTP authentication |
| `securityType` | string | No | one of none, StartTLS or SSL/TLS |
| `serverAddress` | string | No | domain name or IP address of SMTP server |
| `passwordExists` | boolean | No | Indicates if password is defined for this smtp config. The password itself is not returned! |
| `providerConfig` | object | No |  |
| `serviceProvider` | string | No | Name of the service provider for authentication Enum: "Microsoft365", "BasicAuth" |
| `modificationTime` | string | No | Last modification time. Formatted as a ISO 8601 string. |

<details>
<summary>Properties of `status`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | number | No | Status code |
| `statusReason` | string | No | Status reason |

</details>

<details>
<summary>Properties of `providerConfig`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `getMicrosoft365Config` | object | No |  |

<details>
<summary>Properties of `getMicrosoft365Config`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | No | Microsoft365 client identifier |
| `emailAddress` | string | No | The email address that should appear in From field when sending emails with this account |
| `providerTenantId` | string | No | Microsoft365 tenant identifier |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `getBasicAuthConfig` | object | No |  |

<details>
<summary>Properties of `getBasicAuthConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `username` | string | No | user name used for SMTP login |
| `senderName` | string | No | The name that should appear in From field when sending emails with this account |
| `serverPort` | number | No | smtp server port |
| `emailAddress` | string | No | The email address that should appear in From field when sending emails with this account |
| `securityType` | string | No | The selected SMTP security mechanism. Could be either 'none', 'StartTLS' or 'SSL/TLS' |
| `serverAddress` | string | No | domain name or IP address of SMTP server |

</details>

</details>

##### 403

Must be a tenant admin.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/transports/email-config` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config',
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
# qlik-cli has not implemented support for GET /api/v1/transports/email-config yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": {
    "statusCode": 0,
    "statusReason": "OK"
  },
  "isValid": true,
  "tenantId": "mcdd-mkw_Ebo0fR2vLl8_YsQYFsYrTdP",
  "username": "john.smith@company.com",
  "errorCode": "INVALID_CREDENTIALS",
  "serverPort": 587,
  "lastUpdated": "string",
  "authFailures": 0,
  "emailAddress": "john.smith@company.com",
  "securityType": "StartTLS",
  "serverAddress": "smtp.company.com",
  "passwordExists": true,
  "providerConfig": {
    "clientId": "12345678-1234-1234-1234-123456789012",
    "emailAddress": "abc@example.com",
    "providerTenantId": "12345678-1234-1234-1234-123456789012"
  },
  "serviceProvider": "Microsoft365",
  "modificationTime": "2022-06-30T09:57:40.954Z"
}
```

---

### PATCH /api/v1/transports/email-config _(deprecated)_

Patches the email configuration for the tenant. This endpoint is deprecated, use `PUT /transports/email-config` to replace the entire configuration instead.

- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2026-11. Migrating to PUT /email-config

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed. Enum: "replace, remove, add" |
| `path` | string | Yes | The path for the given resource field to patch. Enum: "/username", "/serverAddress", "/serverPort", "/securityType", "/emailAddress", "/emailPassword" |
| `value` | string | Yes | The value to be used for this operation. |

#### Responses

##### 204

Success.

##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### 403

Must be a tenant admin.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/transports/email-config` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'replace',
        path: '/username',
        value: 'New name',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/transports/email-config yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"replace","path":"/username","value":"New name"}]'
```

---

### PUT /api/v1/transports/email-config

Creates or replaces the email configuration for the tenant. Validation of the configuration is done as part of the request.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `providerConfig` | object | No |  |
| `serviceProvider` | string | No | Name of the service provider for authentication Enum: "Microsoft365", "BasicAuth" |

<details>
<summary>Properties of `providerConfig`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `putMicrosoft365Config` | object | No | Microsoft 365 authentication configuration. Provides OAuth credentials and tenant information for Microsoft 365 email delivery. |

<details>
<summary>Properties of `putMicrosoft365Config`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | No | Microsoft365 client identifier |
| `clientSecret` | string | No | secret to authenticate the Microsoft365 account |
| `emailAddress` | string | No | The email address that should appear in From field when sending emails with this account |
| `providerTenantId` | string | No | Microsoft365 tenant identifier |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `putBasicAuthConfig` | object | No | SMTP basic authentication configuration. Provides server address, credentials, and sender information for standard SMTP email delivery. |

<details>
<summary>Properties of `putBasicAuthConfig`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `username` | string | No | user name used for SMTP login |
| `senderName` | string | No | The name that should appear in From field when sending emails with this account |
| `serverPort` | number | No | smtp server port |
| `emailAddress` | string | No | The email address that should appear in From field when sending emails with this account |
| `securityType` | string | No | SMTP security mechanism to use. Could be either 'none', 'StartTLS' or 'SSL/TLS' |
| `emailPassword` | string | No | password for SMTP basic authentication |
| `serverAddress` | string | No | domain name or IP address of SMTP server |

</details>

</details>

#### Responses

##### 204

Email configuration validated and saved successfully.
- For "BasicAuth": Connection to the email server verified with provided credentials.
- For "Microsoft365": Authentication token successfully retrieved with provided credentials.


##### 400

Bad request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### 403

Must be a tenant admin.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/transports/email-config` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      providerConfig: {
        clientId:
          '12345678-1234-1234-1234-123456789012',
        clientSecret:
          '-123a5678_1234/1234*1234-123b567b12',
        emailAddress: 'abc@example.com',
        providerTenantId:
          '12345678-1234-1234-1234-123456789012',
      },
      serviceProvider: 'Microsoft365',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/transports/email-config yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"providerConfig":{"clientId":"12345678-1234-1234-1234-123456789012","clientSecret":"-123a5678_1234/1234*1234-123b567b12","emailAddress":"abc@example.com","providerTenantId":"12345678-1234-1234-1234-123456789012"},"serviceProvider":"Microsoft365"}'
```

---

### DELETE /api/v1/transports/email-config

Deletes the email configuration for the tenant.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 204

Success.

##### 403

Must be a tenant admin.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/transports/email-config` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config',
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
# qlik-cli has not implemented support for DELETE /api/v1/transports/email-config yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/transports/email-config/actions/send-test-email

Attempts to sends a test email using the active configuration, with the supplied email info (subject, body, recipient).

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | email body |
| `subject` | string | No | email subject |
| `recipient` | string | No | email recipient (email address) |

#### Responses

##### 200

Attempted send request. Response body indicates success/failure

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No | error message from SMTP middleware .. a bit technical but could be useful to administrator |
| `success` | boolean | No | was SMTP operation successful or not. Other fields herein provide more detail |
| `connectionFailed` | boolean | No | could not resolve domain name, connection refused, connection timed out, SSL mismatch |
| `smtpResponseCode` | integer | No | smtp result code string from the SMTP server. eg. "250 2.6.0" |

##### 403

Must be a tenant admin.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### 404

No email config exists for tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/transports/email-config/actions/send-test-email` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config/actions/send-test-email',
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
# qlik-cli has not implemented support for POST /api/v1/transports/email-config/actions/send-test-email yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config/actions/send-test-email" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "string",
  "success": true,
  "connectionFailed": true,
  "smtpResponseCode": 42
}
```

---

### POST /api/v1/transports/email-config/actions/validate

Returns the current isValid value for the email configuration for the tenant. Does not attempt to connect to a server to verify the connection or send a test email. Will return false if no email configuration exists.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 200

Returns boolean isValid for the email config.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isValid` | boolean | No | true if smtp config is correct and complete. Will return false if smtp-config does not exist at all |
| `errorCode` | string | No | Indicates error with this email configuration. OK means that no error is indicated. Possible values are OK, CONFIG_NOT_SET, INCOMPLETE_CONFIG, INVALID_CREDENTIALS, PROVIDER_ERROR |

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/transports/email-config/actions/validate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config/actions/validate',
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
# qlik-cli has not implemented support for POST /api/v1/transports/email-config/actions/validate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config/actions/validate" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "isValid": true,
  "errorCode": "INVALID_CREDENTIALS"
}
```

---

### POST /api/v1/transports/email-config/actions/verify-connection

Attempts to verify connection to email server using a low-level protocol handshake to confirm the server is reachable and the credentials are valid, without sending a test email.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Responses

##### 200

Performed email connection. Response body indicates success/failure

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No | error message from SMTP middleware .. a bit technical but could be useful to administrator |
| `success` | boolean | No | was SMTP operation successful or not. Other fields herein provide more detail |
| `connectionFailed` | boolean | No | could not resolve domain name, connection refused, connection timed out, SSL mismatch |
| `smtpResponseCode` | integer | No | smtp result code string from the SMTP server. eg. "250 2.6.0" |

##### 404

No email config exists for tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem |

</details>

##### default

Unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | An error object. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/transports/email-config/actions/verify-connection` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/transports/email-config/actions/verify-connection',
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
# qlik-cli has not implemented support for POST /api/v1/transports/email-config/actions/verify-connection yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config/actions/verify-connection" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "string",
  "success": true,
  "connectionFailed": true,
  "smtpResponseCode": 42
}
```

---
