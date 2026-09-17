# Lineage graphs

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Lineage-graphs represents the lineage information for a specific Qlik item.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/lineage-graphs/impact/{id}/actions/expand`](#get-apiv1lineage-graphsimpactidactionsexpand) | Returns next-level nodes inside a specified node on an impact analysis graph retrieved using a base node. |
| `GET` | [`/api/v1/lineage-graphs/impact/{id}/actions/search`](#get-apiv1lineage-graphsimpactidactionssearch) | Searchs all labels within a impact graph on all available levels. Returns result per level. |
| `GET` | [`/api/v1/lineage-graphs/impact/{id}/overview`](#get-apiv1lineage-graphsimpactidoverview) | Returns all RESOURCE level nodes that are impacted by a change in the source node. The number of tables and fields that are impacted for each resource are included as metadata. The id (QRI) can be on any level (FIELD, TABLE or RESOURCE) and the impact will be collected based on the starting QRI. |
| `GET` | [`/api/v1/lineage-graphs/impact/{id}/source`](#get-apiv1lineage-graphsimpactidsource) | Returns all levels of the requested root node. Only node information will be returned. |
| `GET` | [`/api/v1/lineage-graphs/nodes/{id}`](#get-apiv1lineage-graphsnodesid) | Returns lineage graphs of a source node. The id (QRI) can point to an item on the field, table and resource level. |
| `GET` | [`/api/v1/lineage-graphs/nodes/{id}/actions/expand`](#get-apiv1lineage-graphsnodesidactionsexpand) | Returns the expanded node and its edges. Up and downstream nodes are not part of the response, edges are. The id is the root node that lineage is requested for. The QRI of the node to expand is sent as the query parameter "node" for expansion. |
| `GET` | [`/api/v1/lineage-graphs/nodes/{id}/actions/search`](#get-apiv1lineage-graphsnodesidactionssearch) | Returns result per level by searching all labels within a lineage graph on all available levels. |
| `POST` | [`/api/v1/lineage-graphs/nodes/{id}/overview`](#post-apiv1lineage-graphsnodesidoverview) | Returns the first generation upstream direct lineage. For each field QRI, will find any direct linege dataset or application. |

## API Reference

### GET /api/v1/lineage-graphs/impact/{id}/actions/expand

Returns next-level nodes inside a specified node on an impact analysis graph retrieved using a base node.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The QRI for base node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `level` | string | Yes | The level to get the nodes on. Enum: "field", "table" |
| `node` | string | Yes | The node in the downstream graph to get next-level nodes for. For instance, to get the TABLE level nodes inside a RESOURCE level node, use the RESOURCE level QRI for the node. Similarly, use the TABLE level QRI to get the FIELD level nodes. If a TABLE level QRI is used with `level` parameter being `TABLE`, only the RESOURCE level of the node will be taken into consideration. |
| `down` | integer | No | The number of downstream resource levels nodes to retrieve. (5 if not provided, -1 means unlimited and 1 means direct lineage) |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graph` | object | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graph`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The index of edges. This is only used in the POST request. |
| `source` | string | No | The id (QRI) of the source node on this edge. |
| `target` | string | No | The id (QRI) of the target node on this edge. |
| `metadata` | object | No |  |
| `relation` | string | No |  |

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | No | The total number of nodes retrieved in this graph. |
| `createdAt` | string | No | The date and time when the graph is created. |
| `producerId` | string | No | The id (QRI) of the graph producer. |
| `specVersion` | string | No |  |
| `producerType` | string | No | The type of the graph producer. |

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/impact/{id}/actions/expand` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/impact/{id}/actions/expand',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/impact/{id}/actions/expand yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/actions/expand" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graph": {
    "type": "RESOURCE",
    "edges": [
      {
        "id": "1",
        "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "metadata": {
          "type": "string"
        },
        "relation": [
          "LOAD",
          "STORE",
          "READ",
          "FROM"
        ]
      }
    ],
    "label": "Sales Data",
    "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
    "directed": true,
    "metadata": {
      "total": 1,
      "createdAt": "2023-10-05T14:48:00.000Z",
      "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
      "specVersion": 1,
      "producerType": [
        "QDA",
        "EXTERNAL"
      ]
    }
  }
}
```

---

### GET /api/v1/lineage-graphs/impact/{id}/actions/search

Searchs all labels within a impact graph on all available levels. Returns result per level.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The qri for root node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | Yes | The expression that matches the SCIM filter format. The filter has to be encoded. The currently supported attribute is "label", attribute operator "co" (contains), and grouping operator "or". Example: 'label co "label1" or label co "label2"'. The search queries are case insensetive. |
| `down` | integer | No | The number of downstream resource levels nodes to search. (5 if not provided, -1 means unlimited) and 1 means direct lineage. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object | No | The list of lineage graphs. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object[] | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/impact/{id}/actions/search` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/impact/{id}/actions/search',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/impact/{id}/actions/search yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/actions/search" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graphs": {
    "graphs": [
      {
        "type": "RESOURCE",
        "edges": [
          {
            "id": "1",
            "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "metadata": {
              "type": "string"
            },
            "relation": [
              "LOAD",
              "STORE",
              "READ",
              "FROM"
            ]
          }
        ],
        "label": "Sales Data",
        "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
        "directed": true,
        "metadata": {
          "total": 1,
          "createdAt": "2023-10-05T14:48:00.000Z",
          "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
          "specVersion": 1,
          "producerType": [
            "QDA",
            "EXTERNAL"
          ]
        }
      }
    ]
  }
}
```

---

### GET /api/v1/lineage-graphs/impact/{id}/overview

Returns all RESOURCE level nodes that are impacted by a change in the source node. The number of tables and fields that are impacted for each resource are included as metadata. The id (QRI) can be on any level (FIELD, TABLE or RESOURCE) and the impact will be collected based on the starting QRI.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The qri for root node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `down` | integer | No | The number of downstream resource levels nodes to retrieve. (5 if not provided, -1 means unlimited and 1 means direct lineage) |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graph` | object | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graph`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The index of edges. This is only used in the POST request. |
| `source` | string | No | The id (QRI) of the source node on this edge. |
| `target` | string | No | The id (QRI) of the target node on this edge. |
| `metadata` | object | No |  |
| `relation` | string | No |  |

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | No | The total number of nodes retrieved in this graph. |
| `createdAt` | string | No | The date and time when the graph is created. |
| `producerId` | string | No | The id (QRI) of the graph producer. |
| `specVersion` | string | No |  |
| `producerType` | string | No | The type of the graph producer. |

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/impact/{id}/overview` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/impact/{id}/overview',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/impact/{id}/overview yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/overview" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graph": {
    "type": "RESOURCE",
    "edges": [
      {
        "id": "1",
        "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "metadata": {
          "type": "string"
        },
        "relation": [
          "LOAD",
          "STORE",
          "READ",
          "FROM"
        ]
      }
    ],
    "label": "Sales Data",
    "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
    "directed": true,
    "metadata": {
      "total": 1,
      "createdAt": "2023-10-05T14:48:00.000Z",
      "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
      "specVersion": 1,
      "producerType": [
        "QDA",
        "EXTERNAL"
      ]
    }
  }
}
```

---

### GET /api/v1/lineage-graphs/impact/{id}/source

Returns all levels of the requested root node. Only node information will be returned.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id (QRI) for root node. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object | No | The list of lineage graphs. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object[] | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/impact/{id}/source` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/impact/{id}/source',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/impact/{id}/source yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/source" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graphs": {
    "graphs": [
      {
        "type": "RESOURCE",
        "edges": [
          {
            "id": "1",
            "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "metadata": {
              "type": "string"
            },
            "relation": [
              "LOAD",
              "STORE",
              "READ",
              "FROM"
            ]
          }
        ],
        "label": "Sales Data",
        "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
        "directed": true,
        "metadata": {
          "total": 1,
          "createdAt": "2023-10-05T14:48:00.000Z",
          "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
          "specVersion": 1,
          "producerType": [
            "QDA",
            "EXTERNAL"
          ]
        }
      }
    ]
  }
}
```

---

### GET /api/v1/lineage-graphs/nodes/{id}

Returns lineage graphs of a source node. The id (QRI) can point to an item on the field, table and resource level.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id (QRI) for the source node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collapse` | boolean | No | To collapse internal nodes, set to true, false otherwise. |
| `level` | string | No | The graph level to retrieve. Enum: "field", "table", "resource", "all" |
| `up` | integer | No | The number of upstream levels of nodes to retrieve. (5 if not provided, -1 means unlimited) |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graph` | object | No | The lineage graph containing the node. |
| `graphs` | object | No | The list of lineage graphs. |

<details>
<summary>Properties of `graph`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The index of edges. This is only used in the POST request. |
| `source` | string | No | The id (QRI) of the source node on this edge. |
| `target` | string | No | The id (QRI) of the target node on this edge. |
| `metadata` | object | No |  |
| `relation` | string | No |  |

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | No | The total number of nodes retrieved in this graph. |
| `createdAt` | string | No | The date and time when the graph is created. |
| `producerId` | string | No | The id (QRI) of the graph producer. |
| `specVersion` | string | No |  |
| `producerType` | string | No | The type of the graph producer. |

</details>

</details>

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object[] | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Internal server error

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/nodes/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/nodes/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/nodes/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graph": {
    "type": "RESOURCE",
    "edges": [
      {
        "id": "1",
        "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "metadata": {
          "type": "string"
        },
        "relation": [
          "LOAD",
          "STORE",
          "READ",
          "FROM"
        ]
      }
    ],
    "label": "Sales Data",
    "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
    "directed": true,
    "metadata": {
      "total": 1,
      "createdAt": "2023-10-05T14:48:00.000Z",
      "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
      "specVersion": 1,
      "producerType": [
        "QDA",
        "EXTERNAL"
      ]
    }
  },
  "graphs": {
    "graphs": [
      {
        "type": "RESOURCE",
        "edges": [
          {
            "id": "1",
            "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "metadata": {
              "type": "string"
            },
            "relation": [
              "LOAD",
              "STORE",
              "READ",
              "FROM"
            ]
          }
        ],
        "label": "Sales Data",
        "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
        "directed": true,
        "metadata": {
          "total": 1,
          "createdAt": "2023-10-05T14:48:00.000Z",
          "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
          "specVersion": 1,
          "producerType": [
            "QDA",
            "EXTERNAL"
          ]
        }
      }
    ]
  }
}
```

---

### GET /api/v1/lineage-graphs/nodes/{id}/actions/expand

Returns the expanded node and its edges. Up and downstream nodes are not part of the response, edges are. The id is the root node that lineage is requested for. The QRI of the node to expand is sent as the query parameter "node" for expansion.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id (QRI) for the source node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `level` | string | Yes | The level to expand to. Enum: "field", "table" |
| `node` | string | Yes | The QRI of the node in the upstream graph for expansion. |
| `collapse` | boolean | No | To collapse internal nodes, set to true, false otherwise. |
| `up` | integer | No | The number of upstream levels of nodes retrieved to expand. (5 if not provided, -1 means unlimited) |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graph` | object | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graph`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The index of edges. This is only used in the POST request. |
| `source` | string | No | The id (QRI) of the source node on this edge. |
| `target` | string | No | The id (QRI) of the target node on this edge. |
| `metadata` | object | No |  |
| `relation` | string | No |  |

<details>
<summary>Properties of `metadata`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metadata`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | No | The total number of nodes retrieved in this graph. |
| `createdAt` | string | No | The date and time when the graph is created. |
| `producerId` | string | No | The id (QRI) of the graph producer. |
| `specVersion` | string | No |  |
| `producerType` | string | No | The type of the graph producer. |

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 500

Internal server error

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/nodes/{id}/actions/expand` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/nodes/{id}/actions/expand',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/nodes/{id}/actions/expand yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/actions/expand" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graph": {
    "type": "RESOURCE",
    "edges": [
      {
        "id": "1",
        "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
        "metadata": {
          "type": "string"
        },
        "relation": [
          "LOAD",
          "STORE",
          "READ",
          "FROM"
        ]
      }
    ],
    "label": "Sales Data",
    "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
    "directed": true,
    "metadata": {
      "total": 1,
      "createdAt": "2023-10-05T14:48:00.000Z",
      "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
      "specVersion": 1,
      "producerType": [
        "QDA",
        "EXTERNAL"
      ]
    }
  }
}
```

---

### GET /api/v1/lineage-graphs/nodes/{id}/actions/search

Returns result per level by searching all labels within a lineage graph on all available levels.

- **Rate Limit:** Special (20 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The qri for root node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | Yes | The expression that matches the SCIM filter format. The filter has to be encoded. The currently supported attribute is "label", attribute operator "co" (contains), and grouping operator "or". Example: 'label co "label1" or label co "label2"'. The search queries are case insensitive. |
| `collapse` | boolean | No | To collapse internal nodes, set to true, false otherwise. |
| `up` | integer | No | The number of upstream levels of nodes retrieved to search. (5 if not provided, -1 means unlimited) |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object | No | The list of lineage graphs. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `graphs` | object[] | No | The lineage graph containing the node. |

<details>
<summary>Properties of `graphs`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | No |  |
| `edges` | object[] | No |  |
| `label` | string | No | Label string for this graph. |
| `nodes` | object | No | All the nodes contained in a graph. |
| `directed` | boolean | No | Returns true if the graph is directed. |
| `metadata` | object | No |  |

<details>
<summary>Properties of `edges`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `metadata`</summary>

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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

</details>

##### 429

Too many requests

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `errors` | object[] | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/lineage-graphs/nodes/{id}/actions/search` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/nodes/{id}/actions/search',
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
# qlik-cli has not implemented support for GET /api/v1/lineage-graphs/nodes/{id}/actions/search yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/actions/search" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "graphs": {
    "graphs": [
      {
        "type": "RESOURCE",
        "edges": [
          {
            "id": "1",
            "source": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "target": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
            "metadata": {
              "type": "string"
            },
            "relation": [
              "LOAD",
              "STORE",
              "READ",
              "FROM"
            ]
          }
        ],
        "label": "Sales Data",
        "nodes": "{\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\":{\"label\":\"a\",\"metadata\":{\"id\":\"qri:app:sense://3634fc0d-273d-429e-8d0b-1b4b1b66a1f2\",\"subtype\":\"PROCESSOR\",\"type\":\"DA_APP\",\"filePath\":\"example.qvd\"}}}",
        "directed": true,
        "metadata": {
          "total": 1,
          "createdAt": "2023-10-05T14:48:00.000Z",
          "producerId": "qri:db:oracle://LfxVj_3du3GYdWdNaa721lOWvbhENXEArBpl58h96YE#ZfH0lkXnTTGu7QGnIvKZpIxFNagQivBtnbC_cAoCPOs",
          "specVersion": 1,
          "producerType": [
            "QDA",
            "EXTERNAL"
          ]
        }
      }
    ]
  }
}
```

---

### POST /api/v1/lineage-graphs/nodes/{id}/overview

Returns the first generation upstream direct lineage. For each field QRI, will find any direct linege dataset or application.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The qri for root node. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `collapse` | boolean | No | To collapse internal nodes, set to true, false otherwise. |
| `up` | integer | No | The number of upstream levels of nodes retrieved to get overview from. (5 if not provided, -1 means unlimited) |

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `application/json` | string[] | No | List of qri to find direct lineage for. |

#### Responses

##### 200

Successful Operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resources` | object[] | No |  |

<details>
<summary>Properties of `resources`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qri` | string | No | Input QRI that we are getting the overview for. |
| `lineage` | object[] | No |  |

<details>
<summary>Properties of `lineage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tableQRI` | string | No | Table level QRI that the field belongs to. |
| `tableLabel` | string | No | Table level label |
| `resourceQRI` | string | No | Resource level QRI |
| `resourceLabel` | string | No | Resource level label |

</details>

</details>

##### 201

Successfully created new resource.

**Content-Type:** `application/json`


##### 207

Request partially succeeded.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `status` | integer | No |  |
| `resource` | object | No |  |

<details>
<summary>Properties of `resource`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qri` | string | No | Input QRI that we are getting the overview for. |
| `lineage` | object[] | No |  |

<details>
<summary>Properties of `lineage`</summary>

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

</details>

##### 403

User does not have access to the node.

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

</details>

##### 404

The record is not found.

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
| `meta` | object | No | The meta contains additional information when requests fail due to internal errors. |
| `title` | string | No |  |
| `detail` | string | No |  |

</details>

##### 503

Service unavailable

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

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/lineage-graphs/nodes/{id}/overview` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/lineage-graphs/nodes/{id}/overview',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      'qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5',
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/lineage-graphs/nodes/{id}/overview yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/overview" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '["qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5"]'
```

**Example Response:**

```json
{
  "resources": [
    {
      "qri": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
      "lineage": [
        {
          "tableQRI": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
          "tableLabel": "Sales Table",
          "resourceQRI": "qri:app:sense://e5c651d5-1198-45a2-be5d-f016cee0baf5",
          "resourceLabel": "Sales Data"
        }
      ]
    }
  ]
}
```

---
