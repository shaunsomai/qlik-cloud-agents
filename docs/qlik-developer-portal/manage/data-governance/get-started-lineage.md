---
source: https://qlik.dev/manage/data-governance/get-started-lineage/
last_updated: 2026-04-20T13:34:03+01:00
---

# Get started with Lineage integration

## Introduction

This tutorial is going to show how to use the Lineage API
to retrieve lineage and impact analysis information for the selected
objects in Qlik Sense.

The Lineage API enables users to keep track of the origins
and impacted content of the base objects on resource, table,
and field levels.

In addition to displaying the input graphs and output content for
the base nodes, the Lineage API also supports search, expansion,
and overview on the nodes within input and output graphs.

## Prerequisites

1. An access token or API key. For more information, see [Authentication](https://qlik.dev/authenticate).

2. [Upload an app](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/create-app-cloud-hub.htm)
   If you don't have an app or data already prepared, you can
   [download the movies dataset](https://github.com/qlik-oss/nebula.js/blob/main/data/apps/the_movies.qvf)
   from the GitHub repository and upload it to the cloud.

3. A Qlik Resource identifier (QRI). In the Lineage service,
   the QRIs are served as the node IDs in the graphs.
   They are also used as query parameters in the API.
   Here is how you can get the QRIs for applications and datasets:
   1. An app QRI is based on its global unique identifier (GUID).
      The GUID can be extracted from the URL and is the part
      that follows `/app`. For example, if the URL is `https://your-tenant.us.qlikcloud.com/sense/app/7fc4d85c-0e07-4160-90a9-c2ca4a45fd81`,
      then the GUID of the app is `7fc4d85c-0e07-4160-90a9-c2ca4a45fd81`,
      and the QRI is a string composed of the GUID and
      the prefix `qri:app:sense://`.
      Therefore in this example, the QRI will be `qri:app:sense://7fc4d85c-0e07-4160-90a9-c2ca4a45fd81`.
   2. To retrieve the QRI of a dataset, you can use
      the Items API [`GET /items/{itemId}`](https://qlik.dev/apis/rest/items/#%23%2Fentries%2Fitems%2F-itemId-get).
      The `itemId` used in the API is the unique identifier of the item.
      It can be extracted from the dataset URL. For example,
      if the URL is `https://your-tenant.us.qlikcloud.com/dataset/6269671709cdb300381e80d2`,
      the unique identifier of the item is `6269671709cdb300381e80d2`.
      The dataset QRI is the value of `secureQri` under the `resourceAttributes`
      section in the API response. It looks approximately like this, `qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8`.

## Lineage API Usage

### Lineage Endpoints

#### **Retrieve lineage graphs for a base node**

```http
GET /api/v1/lineage-graphs/nodes/{id} HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

To retrieve the lineage graph with different options,
you can add the following optional parameters in the request:

- `level` to return a graph on resource, table, field level.
  By default, the resource level is returned.
  Example of the request URL with `level` being used:
  `https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}?level=field`
- `up` to return a graph based on different numbers of upstream layers of nodes.
  For instance, if an app has only one input data source and nothing
  preceding, the upstream layers of the app is one in total. By default,
  the `up` parameter is set to `5`.
  To return all layers of upstream nodes, you can use `up=-1`.
- `collapse` to collapse internal nodes. By default, `collapse` is true.
  To expand internal nodes in the returned graph, you can use `collapse=false`.

Here is an example of the returned graph in the response:

```json
{
  "graph": {
    "directed": true,
    "type": "RESOURCE",
    "label": "Resource Level Lineage for qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9",
    "nodes": {
      "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9": {
        "label": "app",
        "metadata": {
          "subtype": "APPLICATION",
          "type": "DA_APP"
        }
      },
      "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8": {
        "label": "test.csv",
        "metadata": {
          "subtype": "FILE",
          "type": "DATASET"
        }
      }
    },
    "edges": [
      {
        "metadata": {},
        "relation": "LOAD",
        "source": "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8",
        "target": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
      }
    ],
    "metadata": {
      "id": "RESOURCE::qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9",
      "total": 2
    }
  }
}
```

#### **Expand a node in a lineage graph**

With this endpoint, the user can expand a node to the next level in a lineage graph
retrieved using the base node QRI. In the response, the expanded node
and its edges are returned, whereas the up and downstream nodes are not included.

```http
GET /api/v1/lineage-graphs/nodes/{id}/actions/expand?node={node_qri}&level=TABLE HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`{node_qri}` is the QRI of the node to expand. It's used in the
`node` as a required parameter. In order to get the TABLE level
nodes inside a RESOURCE level node, a RESOURCE level QRI should
be used. Similarly, use the TABLE level QRI to get the FIELD
level nodes. If a TABLE level QRI is used with `level` parameter
being `TABLE`, only the RESOURCE level QRI of the node will be
taken into consideration.

`level` is another required parameter to determine what level to expand to.
The default value is `table`. It can also be `field`.

`up` and `collapse` can be used as optional parameters in the request.
They work in the same way as they do in the `GET /lineage-graphs/nodes/{id}`.

Here is an example of the returned graph of the expanded node and its edges:

```json
{
  "graph": {
    "directed": true,
    "type": "TABLE",
    "label": "Expansion for qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9",
    "nodes": {
      "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
        "label": "c1",
        "metadata": {
          "type": "TABLE"
        }
      }
    },
    "edges": [
      {
        "relation": "from",
        "source": "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8#A7TgITl2fGTo0ZuwU8PWXIAC4ot2TdsMMkLL7-4hSWA",
        "target": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI"
      }
    ],
    "metadata": {}
  }
}
```

#### **Retrieve the overview for a list of field level nodes**

This endpoint first retrieves a lineage graph using a base node QRI,
and then returns the first generation upstream direct lineage for
each provided field level node QRI in the request body.

```http
POST /api/v1/lineage-graphs/nodes/{id}/overview HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

[
   "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI",
   "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk#4O6LtQaF4F-g9H7QQgOulT_f0FX1vSiS6hhlBCVPjDo#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI"
]
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`up` and `collapse` can be used as optional parameters in the request.
They work in the same way as they do in the `GET /lineage-graphs/nodes/{id}`.

Here is an example of the response:

```json
{
  "resources": [
    {
      "qri": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI",
      "lineage": [
        {
          "resourceLabel": "c1_1.csv",
          "resourceQRI": "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8",
          "tableQRI": "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8#A7TgITl2fGTo0ZuwU8PWXIAC4ot2TdsMMkLL7-4hSWA",
          "tableLabel": "c1_1"
        }
      ]
    },
    {
      "qri": "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk#4O6LtQaF4F-g9H7QQgOulT_f0FX1vSiS6hhlBCVPjDo#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI",
      "lineage": [
        {
          "resourceLabel": "app",
          "resourceQRI": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9",
          "tableQRI": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI",
          "tableLabel": "c1"
        }
      ]
    }
  ]
}
```

#### **Search for nodes in a lineage graph**

This will search for all the nodes in the lineage graphs of all available levels
where the labels of the nodes match the search filter. The lineage graphs
are retrieved with a base node QRI provided in the request URL.

```http
GET /api/v1/lineage-graphs/nodes/{id}/actions/search HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`filter` is a required parameter in this request that follows [RFC 7644](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2).
The currently supported attribute is `label`, attribute operator `co` (contains),
and grouping operator `or`. The search queries are case insensitive.
Here is an example of the request URL with filter `label co "label1" or label co "label2"`:
`https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/search?filter=label%20co%20%22label1%22%20or%20label%20co%20%22label2%22`

`up` and `collapse` can be used as optional parameters in the request.
They work in the same way as they do in the `GET /lineage-graphs/nodes/{id}`.

The search response is a list of graphs on all available levels containing
the nodes that match the search filter.

Here is an example of the search response:

```json
{
  "graphs": [
    {
      "directed": false,
      "type": "RESOURCE",
      "label": "",
      "nodes": {
        "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8": {
          "label": "c1_1.csv",
          "metadata": {
            "subtype": "FILE",
            "type": "DATASET"
          }
        }
      },
      "edges": null,
      "metadata": null
    },
    {
      "directed": false,
      "type": "TABLE",
      "label": "",
      "nodes": {
        "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "TABLE"
          }
        },
        "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8#A7TgITl2fGTo0ZuwU8PWXIAC4ot2TdsMMkLL7-4hSWA": {
          "label": "c1_1",
          "metadata": {
            "type": "TABLE"
          }
        }
      },
      "edges": null,
      "metadata": null
    },
    {
      "directed": false,
      "type": "FIELD",
      "label": "",
      "nodes": {
        "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "FIELD"
          }
        },
        "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#b7lP72MUZw8o-iS6deFptraRKOv-EGzFRkQ5gdAzAh8#A7TgITl2fGTo0ZuwU8PWXIAC4ot2TdsMMkLL7-4hSWA#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "FIELD"
          }
        },
        "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk#4O6LtQaF4F-g9H7QQgOulT_f0FX1vSiS6hhlBCVPjDo#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "FIELD"
          }
        }
      },
      "edges": null,
      "metadata": null
    }
  ]
}
```

### Impact Analysis Endpoints

Only users with Tenant Admin role have access to these endpoints.

#### **Retrieve the source information of an impact graph**

This endpoint retrieves the node information of the base node
on all levels.

```http
GET /api/v1/lineage-graphs/impact/{id}/source HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

Here is an example of the response:

```json
{
  "graphs": [
    {
      "directed": true,
      "type": "RESOURCE",
      "label": "",
      "nodes": {
        "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9": {
          "label": "app",
          "metadata": {
            "subtype": "PROCESSOR",
            "type": "DA_APP"
          }
        }
      },
      "edges": [],
      "metadata": {
        "id": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
      }
    },
    {
      "directed": true,
      "type": "TABLE",
      "label": "",
      "nodes": {
        "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "TABLE"
          }
        }
      },
      "edges": [],
      "metadata": {
        "id": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
      }
    },
    {
      "directed": true,
      "type": "FIELD",
      "label": "",
      "nodes": {
        "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
          "label": "c1",
          "metadata": {
            "type": "FIELD"
          }
        }
      },
      "edges": [],
      "metadata": {
        "id": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
      }
    }
  ]
}
```

#### **Retrieve the impact overview for a base node**

This returns all the nodes that are impacted by the base node
on the resource level. The response graph includes the number of
table and field level nodes of each resource level node in the metadata.

```http
GET /api/v1/lineage-graphs/impact/{id}/overview HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`down` can be used as an optional parameter in the request.
It returns a different number of downstream layers of nodes
in the impact graph. By default, the `down` parameter is set to `5`.
To get all layers of nodes, you can use `down=-1`.

Here is an example of the response:

```json
{
  "graph": {
    "directed": true,
    "type": "RESOURCE",
    "label": "",
    "nodes": {
      "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#R2nrC7G3EU5LxIBnXten-xk7FIsLMRenDro3ieVoTRA": {
        "label": "output.qvd",
        "metadata": {
          "fields": 1,
          "tables": 1
        }
      },
      "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk": {
        "label": "output.csv",
        "metadata": {
          "fields": 1,
          "tables": 1
        }
      }
    },
    "edges": [],
    "metadata": {
      "id": "OVERVIEW:qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
    }
  }
}
```

#### **Expand a node impacted by the base node**

With this endpoint, the user can expand a node in an impact graph
retrieved using the base node QRI. In the response, the expanded node
and its edges are returned, whereas the up and downstream nodes are not included.

```http
GET /api/v1/lineage-graphs/nodes/{id}/actions/expand?node={node_qri}&level=TABLE HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`{node_qri}` is the QRI of the node to expand. It's used in the
`node` as a required parameter.

`level` is another required parameter to determine to what level to expand.
The default value is `table`. It can also be `field`.

`down` can be used as an optional parameter in the request.
It returns different number of downstream layers of nodes
in the impact graph. By default, the `down` parameter is set to `5`.
To get all layers of nodes, you can use `down=-1`.

Here is an example of the response:

```json
{
  "graph": {
    "directed": true,
    "type": "TABLE",
    "label": "test",
    "nodes": {
      "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI": {
        "label": "c1",
        "metadata": {
          "fields": 1,
          "type": "TABLE"
        }
      }
    },
    "edges": [],
    "metadata": {
      "id": "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9"
    }
  }
}
```

#### **Search for nodes impacted by the base node**

This will search for all the nodes in the impact graphs of all available levels
where the labels of the nodes match the search filter. The impact graphs
are retrieved with a base node QRI provided in the request URL.

```http
GET /api/v1/lineage-graphs/impact/{id}/actions/search HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>
```

`<API_KEY>` is your API key.

`{id}` is the QRI of the base node.

`filter` is a required parameter in this request that follows [RFC 7644](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2).
The currently supported attribute is `label`, attribute operator `co` (contains),
and grouping operator `or`. The search queries are case insensitive.
Here is an example of the request URL with filter `label co "label1" or label co "label2"`:
`https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/search?filter=label%20co%20%22label1%22%20or%20label%20co%20%22label2%22`

`down` can be used as an optional parameter in the request.
It works in the same way as it does in the `GET /lineage-graphs/impact/{id}/overview`.

The search response is a list of graphs on all available levels containing
the nodes that match the search filter.

Here is an example of the response:

```json
{
    "graphs": [
        {
            "directed": false,
            "type": "RESOURCE",
            "label": "",
            "nodes": {
                "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk": {
                    "label": "output.csv",
                    "metadata": {
                        "subtype": "FILE",
                        "type": "DATASET"
                    }
                }
            },
            "edges": null,
            "metadata": null
        },
        {
            "directed": false,
            "type": "TABLE",
            "label": "",
            "nodes": {
                "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v0": {
                    "label": "c1",
                    "metadata": {
                        "type": "TABLE"
                    }
                },
                "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v1": {
                    "label": "c1",
                    "metadata": {
                        "stored": true,
                        "type": "TABLE"
                    }
                },
                "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#R2nrC7G3EU5LxIBnXten-xk7FIsLMRenDro3ieVoTRA#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v0": {
                    "label": "c1",
                    "metadata": {
                        "type": "TABLE"
                    }
                }
            },
            "edges": null,
            "metadata": null
        },
        {
            "directed": false,
            "type": "FIELD",
            "label": "",
            "nodes": {
                "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v0": {
                    "label": "c1",
                    "metadata": {
                        "type": "FIELD"
                    }
                },
                "qri:app:sense://d941992a-11b3-42f7-853d-b61274add8b9#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v1": {
                    "label": "c1",
                    "metadata": {
                        "type": "FIELD"
                    }
                },
                "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#R2nrC7G3EU5LxIBnXten-xk7FIsLMRenDro3ieVoTRA#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v0": {
                    "label": "c1",
                    "metadata": {
                        "type": "FIELD"
                    }
                },
                "qri:qdf:user://g_T6cPqyb7PDRwWKUeLLyx6W85HwvPvgO4cSNod5mLA#fbZ_6xbtUgP2_yRC1BND3FKCemE7pWolHOCPQgTALQk#4O6LtQaF4F-g9H7QQgOulT_f0FX1vSiS6hhlBCVPjDo#0PYxyh3bqNs7z8ueBXzcmNA3nxvuAOdaVFFHon2t2YI-v0": {
                    "label": "c1",
                    "metadata": {
                        "type": "FIELD"
                    }
                }
            },
            "edges": null,
            "metadata": null
        }
    ]
```
