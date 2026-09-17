---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/generic-object-viz-extension/
last_updated: 2026-06-02T18:15:45+01:00
---

# Generic object in visualization extensions

The generic object is underlying all visualizations in Qlik Sense. This allows
you to use the Qlik associative engine capability. A generic object is
created when your custom visualization extension is added to an app. It contains
the initial properties specified and it is persisted in the app.

## Properties and layout

The generic object has properties in a structure that you define. There are
two kinds of properties:

- User defined: Qlik Sense only persists the properties and includes them in the
  layout as-is. Their usage is then defined in the code.

- Qlik associative engine defined: The Qlik associative engine validates the
  properties and replaces them in the output - the layout - by the calculated
  counterparts. A `qHyperCubeDef` containing the dimension and measure
  definitions is replaced by a `qHyperCube` containing the calculated values.

Qlik Engine JSON API: [qHyperCubeDef](https://qlik.dev/apis/json-rpc/qix/schemas/#hypercubedef)

Qlik Engine JSON API: [qHyperCube](https://qlik.dev/apis/json-rpc/qix/schemas/#hypercube)

> **Tip:** All properties defined by the Qlik associative engine start with the letter `"q"`.
> To avoid conflicts, it's good practice to start your own custom properties with a different letter.

The properties of a visualization extension are set up in `initialProperties`.

Example: People chart `initialProperties`

```json
initialProperties : {
  version: 1.0,
  qHyperCubeDef : {
    qDimensions : [],
    qMeasures : [],
    qInitialDataFetch : [{
      qWidth : 2,
      qHeight : 50
    }]
  }
}
```

This creates a hypercube at root level so you know where to find your data when
you define the paint method. The preceding example also creates a user defined
property called `version`. The Qlik associative engine only persists user defined
properties so you can view the version history by using `layout.version`.

You can create visualization extensions with multiple hypercubes or
visualization extensions without properties, hence without any hypercube at
all. The Hello world visualization extension is an example of a visualization
extension with no hypercube.

You can also create visualization extensions with other predefined properties:

- `qListObject`
- `qStringExpression`
- `qValueExpression`

## Using qListObject

qListObject is underlying list boxes and is suitable if you want to create a
list of all values from a field. The Horizontal listbox visualization extension
exemplifies the `qListObject` together with some user defined properties.

A list object is a visualization that contains one dimension. When getting the
layout of a list object (`qListObjectDef`), all values are rendered. If
selections are applied to a list object, the selected values are displayed
along with the excluded and the optional values.

Just like you can have multiple hypercubes in your properties, you can also
have multiple list objects. If you have multiple list objects, you need to
place them at different paths in your property structure

Example: Horizontal listbox `initialProperties`

```json
initialProperties : {
  version : 1.0,
  qListObjectDef : {
    qShowAlternatives : true,
    qFrequencyMode : "V",
    qSortCriterias : {
      qSortByState : 1
    },
    qInitialDataFetch : [{
      qWidth : 2,
      qHeight : 50
    }]
  },
  fixed: true,
  width: 25,
  percent: true,
  selectionMode: "CONFIRM"
}
```

Qlik Engine JSON API: [qListObjectDef](https://qlik.dev/apis/json-rpc/qix/schemas/#listobjectdef)

## Using multiple hypercubes

When creating visualization extensions with multiple hypercubes to combine
several data sets, you need to place the hypercubes at different paths in your
property structure.

Example: Multiple hypercubes defined in `initialProperties`

```json
initialProperties : {
  qHyperCubeDef : {
    qDimensions : [],
    qMeasures : [],
    qInitialDataFetch : [{
      qWidth : 10,
      qHeight : 50
    }]
  },
  second:{
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

## Using qStringExpression and qValueExpression

You can use `qStringExpression` or `qValueExpression` if you want an expression to
be evaluated. A string expression is an expression that returns a single string
value. An expression value is an expression that returns a single numeric value.

Example: qStringExpression and qValueExpression

```json
version : {
  qStringExpression : "=QlikViewVersion ()"
},
fields : {
  qValueExpression : "=Count(DISTINCT $Field)"
}
```

Qlik Engine JSON API: [qStringExpression](https://qlik.dev/apis/json-rpc/qix/schemas/#stringexpression)

Qlik Engine JSON API: [qValueExpression](https://qlik.dev/apis/json-rpc/qix/schemas/#valueexpression)

## Learn more

- [Extension API: initialProperties property](https://help.qlik.com/en-US/sense-developer/Subsystems/APIs/Content/Sense_ClientAPIs/ExtensionAPI/initialproperties-property.htm)
  on Qlik Help.
