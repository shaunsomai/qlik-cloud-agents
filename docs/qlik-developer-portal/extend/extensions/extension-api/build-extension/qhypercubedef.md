---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/qhypercubedef/
last_updated: 2026-06-29T09:07:47+02:00
---

# qHyperCubeDef

Most visualizations that come built-in with Qlik Sense are based on a hypercube
definition (`qHyperCubeDef`) on root level. A hypercube can contain both
dimensions and measures. If selections are applied to a hypercube, only the
selected values are displayed.

You can have multiple hypercubes in your properties (`initialProperties`). This
allows you to make advanced visualizations that combine several data sets.
If you have multiple hypercubes, you need to place them at different paths in
your property structure.

## Examples

Example: Hypercube definition in Chart template

```json
initialProperties: {
    version: 1.0,
    qHyperCubeDef: {
        qDimensions: [],
        qMeasures: [],
        qInitialDataFetch: [{
            qWidth: 2,
            qHeight: 50
        }]
    }
},
```

Example: Multiple hypercubes definition

```json
initialProperties : {
        version : 1.0,
        qHyperCubeDef : {
            qDimensions : [],
            qMeasures : [],
            qInitialDataFetch : [{
                qWidth : 10,
                qHeight : 50
            }]
        },
        second : {
            qHyperCubeDef : {
                qDimensions : [],
                qMeasures : [],
                qInitialDataFetch : [{
                    qWidth : 10,
                    qHeight : 50
            }]
        }
    }
}
```

Example: Enabling numerical sorting

By defining `qInterColumnSortOrder`, numerical sorting on the measure is enabled.
If you define `qInterColumnSortOrder` in `initialProperties`, you must also define
the `qDimensions` and `qMeasures` being used, else an error will be thrown.

```json
initialProperties : {
    qHyperCubeDef : {
        qDimensions : [{
            qDef : {
                qFieldDefs : ["Dim1"]
            }
        }
        ],
        qMeasures : [{
            qDef:{
                qDef : "=Sum(Expression1)"}
            }
        ],
        qInterColumnSortOrder : [1,0],
        qInitialDataFetch : [{
            qWidth : 10,
            qHeight : 50
        }]
    }
},
```

## Properties

For a complete description of the `qHyperCubeDef` properties,
see the [Qlik Sense Engine API documentation](https://qlik.dev/apis/json-rpc/qix/schemas/#hypercubedef)

## Learn more

- [Generic object in visualization extensions](https://qlik.dev/extend/extensions/extension-api/build-extension/generic-object-viz-extension/)
