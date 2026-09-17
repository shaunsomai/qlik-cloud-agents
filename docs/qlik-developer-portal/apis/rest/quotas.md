# Quotas

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Quotas returns entitled attributes based on your license.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/quotas`](#get-apiv1quotas) |  |
| `GET` | [`/api/v1/quotas/{id}`](#get-apiv1quotasid) |  |

## API Reference

### GET /api/v1/quotas

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reportUsage` | boolean | No | The Boolean flag indicating whether quota usage shall be part of the response. The default value is false (only limits returned). |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Array of quota items. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the quota item. For example, "app_mem_size", "app_upload_disk_size", or "shared_spaces". |
| `type` | string | Yes | The resource type of the quota item. Always equal to "quotas". |
| `attributes` | object | Yes | The attributes of the quota. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | string | Yes | The unit of the quota limit. For memory quotas, the unit is always "bytes". For other discrete units, the item counted is used as unit, for example "spaces". |
| `quota` | number | Yes | The quota limit. If there is no quota limit, -1 is returned. |
| `usage` | number | No | The current quota usage, if applicable. This attribute is only present if it is requested using the reportUsage query parameter. |
| `warningThresholds` | number[] | No | The warning thresholds at which "close to quota" warnings can be issued when exceeded. If omitted, no warning threshold shall be used. Currently, the array will contain only one threshold value. In the future, this may be extended. The threshold is a number between 0 and 1, relating to the quota limit. For example, a value of 0.9 means that a warning should be issued when exceeding 90% of the quota limit. |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A specific error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A specific error. |

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
// qlik-api has not implemented support for `GET /api/v1/quotas` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/quotas', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/v1/quotas yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/quotas" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "type": "string",
      "attributes": {
        "unit": "string",
        "quota": 42,
        "usage": 42,
        "warningThresholds": [
          0.9
        ]
      }
    }
  ]
}
```

---

### GET /api/v1/quotas/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the quota item. For example, "app_mem_size", "app_upload_disk_size", or "shared_spaces". |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reportUsage` | boolean | No | The Boolean flag indicating whether quota usage shall be part of the response. The default value is false (usage not included). |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Quota item. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the quota item. For example, "app_mem_size", "app_upload_disk_size", or "shared_spaces". |
| `type` | string | Yes | The resource type of the quota item. Always equal to "quotas". |
| `attributes` | object | Yes | The attributes of the quota. |

<details>
<summary>Properties of `attributes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `unit` | string | Yes | The unit of the quota limit. For memory quotas, the unit is always "bytes". For other discrete units, the item counted is used as unit, for example "spaces". |
| `quota` | number | Yes | The quota limit. If there is no quota limit, -1 is returned. |
| `usage` | number | No | The current quota usage, if applicable. This attribute is only present if it is requested using the reportUsage query parameter. |
| `warningThresholds` | number[] | No | The warning thresholds at which "close to quota" warnings can be issued when exceeded. If omitted, no warning threshold shall be used. Currently, the array will contain only one threshold value. In the future, this may be extended. The threshold is a number between 0 and 1, relating to the quota limit. For example, a value of 0.9 means that a warning should be issued when exceeding 90% of the quota limit. |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A specific error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

##### 404

Not Found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A specific error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A specific error. |

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
// qlik-api has not implemented support for `GET /api/v1/quotas/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/quotas/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/quotas/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/quotas/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "type": "string",
      "attributes": {
        "unit": "string",
        "quota": 42,
        "usage": 42,
        "warningThresholds": [
          0.9
        ]
      }
    }
  ]
}
```

---
