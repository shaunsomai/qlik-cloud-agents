---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/qlistobjectdef/
last_updated: 2026-06-29T09:07:47+02:00
---

# qListObjectDef

A list object is a visualization that contains one dimension. When getting the
layout of a list object (`qListObjectDef`), all values are rendered. If
selections are applied to a list object, the selected values are displayed
along with the excluded and the optional values.

Just like you can have multiple hypercubes in your properties, you can also
have multiple list objects. If you have multiple list objects, you need to
place them at different paths in your property structure.

## Examples

Example: List object definition in List template

```json
initialProperties: {
    version: 1.0,
    qListObjectDef: {
        qShowAlternatives: true,
        qFrequencyMode: "V",
        qInitialDataFetch: [{
            qWidth: 2,
            qHeight: 50
        }]
    }
},
```

## Properties

For a complete description of the `qListObjectDef` properties,
see the [Qlik Sense Engine API documentation](https://qlik.dev/apis/json-rpc/qix/schemas/#listobjectdef).

## Learn more

- [Generic object in visualization extensions](https://qlik.dev/extend/extensions/extension-api/build-extension/generic-object-viz-extension/)
