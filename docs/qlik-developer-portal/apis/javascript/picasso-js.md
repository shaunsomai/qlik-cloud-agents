---
source: https://qlik.dev/apis/javascript/picasso-js/
last_updated: 2026-08-25T10:14:37+01:00
---

# picasso.js

`Version: 2.11.7` | _stable_

A charting library streamlined for building visualizations for the Qlik Sense Analytics platform.

## Table of Contents

### Entries

- [picassojs](#picassojscfg-function)

### Definitions

- [ArcSettings](#arcsettings-object)
- [Brush](#brush-interface)
- [BrushConfig](#brushconfig-object)
- [BrushConsumeSettings](#brushconsumesettings-object)
- [BrushTargetConfig](#brushtargetconfig-object)
- [BrushTriggerSettings](#brushtriggersettings-object)
- [canvasRendererFactory](#canvasrendererfactoryscenefn-function)
- [Chart](#chart-interface)
- [ChartDefinition](#chartdefinition-object)
- [ChartSettings](#chartsettings-object)
- [Circle](#circle-object)
- [CollectionSettings](#collectionsettings-interface)
- [Component](#component-object)
- [ComponentAxis](#componentaxis-object)
- [ComponentBox](#componentbox-object)
- [ComponentBrushArea](#componentbrusharea-object)
- [ComponentBrushAreaDir](#componentbrushareadir-object)
- [ComponentBrushLasso](#componentbrushlasso-object)
- [ComponentBrushRange](#componentbrushrange-object)
- [ComponentContainer](#componentcontainer-object-experimental)
- [ComponentGridLine](#componentgridline-object)
- [ComponentLabels](#componentlabels-object)
- [ComponentLegendCat](#componentlegendcat-object)
- [ComponentLegendSeq](#componentlegendseq-object)
- [ComponentLine](#componentline-object)
- [ComponentPie](#componentpie-object)
- [ComponentPoint](#componentpoint-object)
- [ComponentRefLine](#componentrefline-object)
- [ComponentSettings](#componentsettings-interface)
- [ComponentText](#componenttext-object)
- [ComponentTooltip](#componenttooltip-object)
- [ComponentTypes](#componenttypes-union)
- [customLayoutFunction](#customlayoutfunctionrect-components-function)
- [DataExtraction](#dataextraction-object)
- [DataFieldExtraction](#datafieldextraction-object)
- [Dataset](#dataset-interface)
- [DataSource](#datasource-object)
- [datumAccessor](#datumaccessord-function)
- [DatumBoolean](#datumboolean-union)
- [DatumConfig](#datumconfig-object)
- [DatumExtract](#datumextract-object)
- [DatumNumber](#datumnumber-union)
- [DatumString](#datumstring-union)
- [DockLayoutSettings](#docklayoutsettings-object)
- [Field](#field-object)
- [formatter](#formatter-function)
- [FormatterDefinition](#formatterdefinition-object)
- [Geopolygon](#geopolygon-object)
- [Interaction](#interaction-object)
- [InteractionSettings](#interactionsettings-interface)
- [Line](#line-object)
- [Path](#path-object)
- [plugin](#pluginregistries-options-function)
- [Point](#point-object)
- [Polygon](#polygon-object)
- [Polyline](#polyline-object)
- [ProgressiveObject](#progressiveobject-object-experimental)
- [Rect](#rect-object)
- [Registries](#registries-object)
- [registry](#registrykey-value-function)
- [Renderer](#renderer-interface)
- [RendererSettings](#renderersettings-object-experimental)
- [Scale](#scale-interface)
- [ScaleBand](#scaleband-object)
- [ScaleCategoricalColor](#scalecategoricalcolor-object)
- [ScaleDefinition](#scaledefinition-object)
- [ScaleLinear](#scalelinear-object)
- [ScaleSequentialColor](#scalesequentialcolor-object)
- [ScaleThresholdColor](#scalethresholdcolor-object)
- [SceneNode](#scenenode-class)
- [svgRendererFactory](#svgrendererfactorytreefactory-ns-scenefn-function)
- [TransformObject](#transformobject-object)
- [Ranges](#ranges-object)
- [beforeDestroy](#beforedestroy-function)
- [beforeMount](#beforemount-function)
- [beforeRender](#beforerender-function)
- [beforeUpdate](#beforeupdate-function)
- [created](#created-function)
- [destroyed](#destroyed-function)
- [mounted](#mountedelement-function)
- [updated](#updated-function)
- [ContinuousSettings](#continuoussettings-object)
- [DiscreteSettings](#discretesettings-object)
- [MajorReference](#majorreference-object)
- [BarsLabelStrategy](#barslabelstrategy-object)
- [RowsLabelStrategy](#rowslabelstrategy-object)
- [SlicesLabelStrategy](#sliceslabelstrategy-object)
- [Source](#source-object)
- [LayerSort](#layersorta-b-function)
- [GenericObject](#genericobject-object)
- [GenericText](#generictext-object)
- [Line](#line-object)
- [LineLabel](#linelabel-object)
- [LineLabelBackground](#linelabelbackground-object)
- [Extract](#extract-object)
- [FilterCallback](#filtercallbackdatum-function)
- [SortCallback](#sortcallbacka-b-function)
- [StackKeyCallback](#stackkeycallbackdatum-function)
- [StackValueCallback](#stackvaluecallbackdatum-function)
- [FilterFn](#filterfncell-function)
- [LabelFn](#labelfncell-function)
- [Props](#props-object)
- [ReduceFn](#reducefnvalues-function)
- [ReduceLabelFn](#reducelabelfnlabels-value-function)
- [TrackByFn](#trackbyfncell-function)
- [ValueFn](#valuefncell-function)
- [LayoutMode](#layoutmode-object)
- [SizeDefinition](#sizedefinition-object)
- [CanvasBufferSize](#canvasbuffersize-union-experimental)
- [Progressive](#progressive-function-experimental)
- [TransformFunction](#transformfunction-function-experimental)

## Entries

### picassojs(cfg?) `function`

picasso.js entry point

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cfg` | object | No | - |  |

#### Returns

[picassojs](#picassojscfg-function)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | [registry](#registrykey-value-function) | Yes | - | Component registry |
| `data` | [registry](#registrykey-value-function) | Yes | - | Data registry |
| `formatter` | [registry](#registrykey-value-function) | Yes | - | Formatter registry |
| `interaction` | [registry](#registrykey-value-function) | Yes | - | Interaction registry |
| `renderer` | [registry](#registrykey-value-function) | Yes | - | Renderer registry |
| `scale` | [registry](#registrykey-value-function) | Yes | - | Scale registry |
| `version` | string | Yes | - | picasso.js version |

<details>
<summary>Examples</summary>

```javascript
import picasso from 'picasso.js';

const configuredPicasso = picasso({ renderer: { prio: ['canvas'] } }) // All components will render using the canvas renderer
```

</details>

---

#### chart(definition) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `definition` | [ChartDefinition](#chartdefinition-object) | Yes | - |  |

##### Returns

[Chart](#chart-interface)

<details>
<summary>Examples</summary>

```javascript
picasso.chart({
    element: document.querySelector('#container'), // This is the element to render the chart in
    data: [
      {
        type: 'matrix',
        data: [
          ['Month', 'Sales', 'Margin'],
          ['Jan', 1106, 7],
          ['Feb', 5444, 53],
          ['Mar', 147, 64],
          ['Apr', 7499, 47],
          ['May', 430, 62],
          ['June', 9735, 13],
          ['July', 5832, 13],
          ['Aug', 7435, 15],
          ['Sep', 3467, 35],
          ['Oct', 3554, 78],
          ['Nov', 5633, 23],
          ['Dec', 6354, 63],
        ],
      },
    ],
    settings: {
      scales: {
        x: { data: { field: 'Margin' } },
        y: { data: { field: 'Sales' } },
      },
      components: [
        {
          // specify how to render the chart
          type: 'axis',
          scale: 'y',
          layout: {
            dock: 'left',
          },
        },
        {
          type: 'axis',
          scale: 'x',
          layout: {
            dock: 'bottom',
          },
        },
        {
          type: 'point',
          data: {
            extract: {
              field: 'Month',
              props: {
                x: { field: 'Margin' },
                y: { field: 'Sales' },
              },
            },
          },
          settings: {
            x: { scale: 'x' },
            y: { scale: 'y' },
            size: function () {
              return Math.random();
            },
          },
        },
      ],
    },
  });
```

</details>

---

#### use(plugin, options?) `function`

Plugin registry

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `plugin` | [plugin](#pluginregistries-options-function) | Yes | - |  |
| `options` | object | No | - |  |

---

## Definitions

### ArcSettings `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `startAngle` | number | Yes | - | Start of arc line, in radians |
| `endAngle` | number | Yes | - | End of arc line, in radians |
| `radius` | number | Yes | - | Radius of arc line |

---

### Brush `interface`

A brush context

---

#### addAndRemoveValues(addItems, removeItems) `function`

Add and remove values in a single operation
almost the same as calling addValues and removeValues but only triggers one 'update' event

If the state of the brush changes, an 'update' event is emitted.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `addItems` | object[] | Yes | - | Items to add |
| `removeItems` | object[] | Yes | - | Items to remove |

---

#### addKeyAlias(key, alias) `function`

Adds an alias to the given key

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Value to be replaced |
| `alias` | string | Yes | - | Value to replace key with |

<details>
<summary>Examples</summary>

```javascript
brush.addKeyAlias('BadFieldName', 'Region');
brush.addValue('BadFieldName', 'Sweden'); // 'BadFieldName' will be stored as 'Region'
brush.containsValue('Region', 'Sweden'); // true
brush.containsValue('BadFieldName', 'Sweden'); // true
```

</details>

---

#### addRange(key, range) `function`

Adds a numeric range to this brush context

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the range |
| `range` | object | Yes | - | The range to add to this brush |

<details>
<summary>Examples</summary>

```javascript
brush.addRange('Sales', { min: 20, max: 50 });
```

</details>

---

#### addRanges(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items containing the ranges to remove |

---

#### addValue(key, value) `function`

emits [start](#start-event), [update](#updateadded-removed-event)

Adds a primitive value to this brush context

If this brush context is not started, a 'start' event is emitted.
If the state of the brush changes, ie. if the added value does not already exist, an 'update' event is emitted.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `value` | string \| number | Yes | - | The value to add |

<details>
<summary>Examples</summary>

```javascript
brush.addValue('countries', 'Sweden');
brush.addValue('/qHyperCube/qDimensionInfo/0', 3);
```

</details>

---

#### addValues(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items to add |

---

#### brushes() `function`

Returns all brushes within this context

##### Returns

`object`

---

#### clear() `function`

Clears this brush context

---

#### configure(config) `function`

Configure the brush instance.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | [BrushConfig](#brushconfig-object) | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
brushInstance.configure({
  ranges: [
    { key: 'some key', includeMax: false },
    { includeMax: true, includeMin: true },
  ]
})
```

</details>

---

#### containsRange(key, range) `function`

Checks if a range segment is contained within this brush context

Returns true if the range segment exists for the provided key, returns false otherwise.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `range` | object | Yes | - | The range to check for |

##### Returns

`boolean`

<details>
<summary>Examples</summary>

```javascript
brush.addRange('Sales', { min: 10, max: 50 });
brush.containsRange('Sales', { min: 15, max: 20 }); // true - the range segment is fully contained within [10, 50]
brush.containsRange('Sales', { min: 5, max: 20 }); // false - part of the range segment is outside [10, 50]
brush.containsRange('Sales', { min: 30, max: 80 }); // false - part of the range segment is outside [10, 50]
```

</details>

---

#### containsRangeValue(key, value) `function`

Checks if a value is contained within a range in this brush context

Returns true if the values exists for the provided key, returns false otherwise.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `value` | number | Yes | - | The value to check for |

##### Returns

`boolean`

<details>
<summary>Examples</summary>

```javascript
brush.addRange('Sales', { min: 10, max: 50 });
brush.containsRangeValue('Sales', 30); // true
brush.containsRangeValue('Sales', 5); // false
```

</details>

---

#### containsValue(key, value) `function`

Checks if a certain value exists in this brush context

Returns true if the values exists for the provided key, returns false otherwise.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `value` | string \| number | Yes | - | The value to check for |

##### Returns

`boolean`

<details>
<summary>Examples</summary>

```javascript
brush.addValue('countries', 'Sweden');
brush.containsValue('countries', 'Sweden'); // true
brush.toggleValue('countries', 'Sweden'); // remove 'Sweden'
brush.containsValue('countries', 'Sweden'); // false
```

</details>

---

#### end(args) `function`

emits [end](#end-event)

Ends this brush context

Ends this brush context and emits an 'end' event if it is not already ended.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `args` | any | Yes | - | arguments to be passed to 'end' listeners |

---

#### intercept(name, ic) `function`

Adds an event interceptor

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | Name of the event to intercept |
| `ic` | function | Yes | - | Handler to call before event is triggered |

<details>
<summary>Examples</summary>

```javascript
brush.intercept('add-values', items => {
 console.log('about to add the following items', items);
 return items;
});
```

</details>

---

#### isActive() `function`

Checks if this brush is activated

Returns true if started, false otherwise

##### Returns

`boolean`

---

#### link(target) `function`

Link this brush to another brush instance.

When linked, the `target` will receive updates whenever this brush changes.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | [Brush](#brush-interface) | Yes | - | The brush instance to link to |

---

#### removeAllInterceptors(name?) `function`

Removes all interceptors

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | No | - | Name of the event to remove interceptors for. If not provided, removes all interceptors. |

---

#### removeInterceptor(name, ic) `function`

Removes an interceptor

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | Name of the event to intercept |
| `ic` | function | Yes | - | Handler to remove |

---

#### removeKeyAlias(key) `function`

Removes an alias

This will only remove the key to alias mapping for new manipulations of the brush,
no changes will be made to the current state of this brush.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Value to remove as alias |

<details>
<summary>Examples</summary>

```javascript
brush.removeKeyAlias('BadFieldName');
```

</details>

---

#### removeRange(key, range) `function`

Removes a numeric range from this brush context

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the range |
| `range` | object | Yes | - | The range to remove from this brush |

---

#### removeRanges(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items containing the ranges to remove |

---

#### removeValue(key, value) `function`

Removes a primitive values from this brush context

If the state of the brush changes, ie. if the removed value does exist, an 'update' event is emitted.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `value` | string \| number | Yes | - | The value to remove |

<details>
<summary>Examples</summary>

```javascript
brush.removeValue('countries', 'Sweden');
```

</details>

---

#### removeValues(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items to remove |

---

#### setRange(key, range) `function`

Sets a numeric range to this brush context

Overwrites any active ranges identified by `key`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the range |
| `range` | object | Yes | - | The range to set on this brush |

---

#### setRanges(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items containing the ranges to set |

---

#### setValues(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items to set |

---

#### start(args) `function`

emits [start](#start-event)

Starts this brush context

Starts this brush context and emits a 'start' event if it is not already started.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `args` | any | Yes | - | arguments to be passed to 'start' listeners |

---

#### toggleRange(key, range) `function`

Toggles a numeric range in this brush context

Removes the range if it's already contained within the given identifier,
otherwise the given range is added to the brush.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the range |
| `range` | object | Yes | - | The range to toggle in this brush |

---

#### toggleRanges(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items containing the ranges to toggle |

---

#### toggleValue(key, value) `function`

Toggles a primitive value in this brush context

If the given value exists in this brush context, it will be removed. If it does not exist it will be added.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | An identifier that represents the data source of the value |
| `value` | string \| number | Yes | - | The value to toggle |

<details>
<summary>Examples</summary>

```javascript
brush.toggleValue('countries', 'Sweden');
```

</details>

---

#### toggleValues(items) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `items` | object[] | Yes | - | Items to toggle |

---

#### end() `event`

Triggered when this brush is deactivated

---

#### start() `event`

Triggered when this brush is activated

---

#### update(added, removed) `event`

Triggered when this brush is updated

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `added` | object[] | Yes | - | The added items |
| `removed` | object[] | Yes | - | The removed items |

---

### BrushConfig `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ranges` | [Ranges](#ranges-object)[] | No | - | Range configurations |

---

### BrushConsumeSettings `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `context` | string | No | - | Name of the brush context to observe |
| `data` | string[] | No | - | The mapped data properties to observe |
| `mode` | string | No | - | Data properties operator: and, or, xor. |
| `filter` | function | No | - | Filtering function |
| `style` | object | No | - | The style to apply to the shapes of the component |

<details>
<summary>Properties of `style`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `active` | object<string, any> | No | - | The style of active data points |
| `inactive` | object<string, any> | No | - | The style of inactive data points |

</details>

<details>
<summary>Examples</summary>

```javascript
{
   context: 'selection',
   data: ['x'],
   filter: (shape) => shape.type === 'circle',
   style: {
     active: {
       fill: 'red',
       stroke: '#333',
       strokeWidth: (shape) => shape.strokeWidth * 2,
     },
     inactive: {},
   },
}
```

</details>

---

### BrushTargetConfig `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Component key |
| `contexts` | string[] | No | - | Name of the brushing contexts to affect |
| `data` | string[] | No | - | The mapped data properties to add to the brush |
| `action` | string | No | "set" | Type of action to respond with |

---

### BrushTriggerSettings `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `on` | string | No | - | Type of interaction to trigger brush on |
| `action` | string | No | - | Type of interaction to respond with |
| `contexts` | string[] | No | - | Name of the brushing contexts to affect |
| `data` | string[] | No | - | The mapped data properties to add to the brush |
| `propagation` | string | No | - | Control the event propagation when multiple shapes are tapped. Disabled by default |
| `globalPropagation` | string | No | - | Control the event propagation between components. Disabled by default |
| `touchRadius` | number | No | - | Extend contact area for touch events. Disabled by default |
| `mouseRadius` | number | No | - | Extend contact area for regular mouse events. Disabled by default |

<details>
<summary>Examples</summary>

```javascript
{
   on: 'tap',
   action: 'toggle',
   contexts: ['selection', 'tooltip'],
   data: ['x'],
   propagation: 'stop', // 'stop' => prevent trigger from propagating further than the first shape
   globalPropagation: 'stop', // 'stop' => prevent trigger of same type to be triggered on other components
   touchRadius: 24,
   mouseRadius: 10
 }
```

</details>

---

### canvasRendererFactory(sceneFn?) `function`

Create a new canvas renderer

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sceneFn` | function | No | - | Scene factory |

#### Returns

[Renderer](#renderer-interface) - A canvas renderer instance

---

### Chart `interface`

Chart instance

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `interactions` | object | Yes | - | Get all interaction instances |

<details>
<summary>Properties of `interactions`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `instances` | [Interaction](#interaction-object)[] | Yes | - |  |

</details>

---

#### brush(name) `function`

Get or create brush context for this chart

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | Name of the brush context. If no match is found, a new brush context is created and returned. |

##### Returns

[Brush](#brush-interface)

---

#### brushFromShapes(shapes, config) `function`

Brush data by providing a collection of data bound shapes.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `shapes` | [SceneNode](#scenenode-class)[] | Yes | - | An array of data bound shapes. |
| `config` | object | Yes | - | Options |

<details>
<summary>Examples</summary>

```javascript
const shapes = chartInstance.shapesAt(...);
const config = {
 components:[
   {
     key: 'key1',
     contexts: ['myContext'],
     data: [''],
     action: 'add'
   }
 ]
};
chartInstance.brushFromShapes(shapes, config);
```

</details>

---

#### component(key) `function`

Get a component context

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Component key |

##### Returns

[Component](#component-object) - Component context

---

#### componentsFromPoint(p) `function`

Get components overlapping a point.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `p` | [Point](#point-object) | Yes | - | Point with x- and y-coordinate. The coordinate is relative to the browser viewport. |

##### Returns

[Component](#component-object)[] - Array of component contexts

---

#### dataset(key) `function`

Get

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Get the dataset identified by `key` |

##### Returns

[Dataset](#dataset-interface)

---

#### destroy() `function`

Destroy the chart instance.

---

#### findShapes(selector) `function`

Get all nodes matching the provided selector

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `selector` | string | Yes | - | CSS selector [type, attribute, universal, class] |

##### Returns

[SceneNode](#scenenode-class)[] - Array of objects containing matching nodes

<details>
<summary>Examples</summary>

```javascript
chart.findShapes('Circle') // [<CircleNode>, <CircleNode>]
chart.findShapes('Circle[fill="red"][stroke!="black"]') // [CircleNode, CircleNode]
chart.findShapes('Container Rect') // [Rect, Rect]
```

</details>

---

#### formatter(v) `function`

Get or create a formatter for this chart

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `v` | string \| object | Yes | - | Formatter reference or formatter options |

##### Returns

[formatter](#formatter-function)

<details>
<summary>Examples</summary>

```javascript
instance.formatter('nameOfMyFormatter'); // Fetch an existing formatter by name
instance.formatter({ formatter: 'nameOfMyFormatter' }); // Fetch an existing formatter by name
instance.formatter({ type: 'q' }); // Fetch an existing formatter by type
instance.formatter({
 formatter: 'd3',
 type: 'number',
 format: '1.0.%'
}); // Create a new formatter
```

</details>

---

#### formatters() `function`

Get all registered formatters

##### Returns

object<string, [formatter](#formatter-function)>

---

#### getAffectedShapes(context, mode, props, key) `function`

Get all shapes associated with the provided context

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `context` | string | Yes | - | The brush context |
| `mode` | string | Yes | - | Property comparison mode. |
| `props` | string[] | Yes | - | Which specific data properties to compare |
| `key` | string | Yes | - | Which component to get shapes from. Default gives shapes from all components. |

##### Returns

`object[]` - Array of objects containing shape and parent element

---

#### layoutComponents(def?) `function`  **[experimental]**

Layout the chart with new settings and / or data

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `def` | object | No | - | New chart definition |

---

#### scale(v) `function`

Get or create a scale for this chart

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `v` | string \| object | Yes | - | Scale reference or scale options |

##### Returns

[Scale](#scale-interface)

<details>
<summary>Examples</summary>

```javascript
instance.scale('nameOfMyScale'); // Fetch an existing scale by name
instance.scale({ scale: 'nameOfMyScale' }); // Fetch an existing scale by name
instance.scale({ source: '0/1', type: 'linear' }); // Create a new scale
```

</details>

---

#### scales() `function`

Get all registered scales

##### Returns

object<string, [Scale](#scale-interface)>

---

#### shapesAt(shape, opts) `function`

Get all nodes colliding with a geometrical shape (circle, line, rectangle, point, polygon, geopolygon).

The input shape is identified based on the geometrical attributes in the following order: circle => line => rectangle => point => polygon => geopolygon.
Note that not all nodes on a scene have collision detection enabled.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `shape` | [Line](#line-object) \| [Rect](#rect-object) \| [Point](#point-object) \| [Circle](#circle-object) | Yes | - | A geometrical shape. Coordinates are relative to the top-left corner of the chart instance container. |
| `opts` | object | Yes | - | Options |

##### Returns

[SceneNode](#scenenode-class)[] - Array of objects containing colliding nodes

<details>
<summary>Examples</summary>

```javascript
chart.shapesAt(
 {
   x: 0,
   y: 0,
   width: 100,
   height: 100
 },
 {
   components: [
     { key: 'key1', propagation: 'stop' },
     { key: 'key2' }
   ],
   propagation: 'stop'
 }
);
```

</details>

---

#### toggleBrushing(val?) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `val` | boolean | No | - | Toggle brushing on or off. If value is omitted, a toggle action is applied to the current state. |

---

#### update(def?) `function`

Update the chart with new settings and / or data

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `def` | object | No | - | New chart definition |

---

### ChartDefinition `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `beforeDestroy` | [beforeDestroy](#beforedestroy-function) | No | - |  |
| `beforeMount` | [beforeMount](#beforemount-function) | No | - |  |
| `beforeRender` | [beforeRender](#beforerender-function) | No | - |  |
| `beforeUpdate` | [beforeUpdate](#beforeupdate-function) | No | - |  |
| `created` | [created](#created-function) | No | - |  |
| `destroyed` | [destroyed](#destroyed-function) | No | - |  |
| `mounted` | [mounted](#mountedelement-function) | No | - |  |
| `updated` | [updated](#updated-function) | No | - |  |
| `data` | [DataSource](#datasource-object)[] \| [DataSource](#datasource-object) | Yes | - | Chart data |
| `element` | HTMLElement | Yes | - | Element to attach chart to |
| `settings` | [ChartSettings](#chartsettings-object) | Yes | - | Chart settings |

---

### ChartSettings `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | [ComponentTypes](#componenttypes-union)[] | No | - | Components |
| `scales` | object<string, [ScaleDefinition](#scaledefinition-object)> | No | - | Dictionary with scale definitions |
| `formatters` | object<string, [FormatterDefinition](#formatterdefinition-object)> | No | - | Dictionary with formatter definitions |
| `strategy` | [DockLayoutSettings](#docklayoutsettings-object) | No | - | Dock layout strategy |
| `interactions` | [InteractionSettings](#interactionsettings-interface)[] | No | - | Interaction handlers |
| `collections` | [CollectionSettings](#collectionsettings-interface)[] | No | - | Collections |

---

### Circle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cx` | number | Yes | - | Center x-coordinate |
| `cy` | number | Yes | - | Center y-coordinate |
| `r` | number | Yes | - | Circle radius |

---

### CollectionSettings `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Unique key for the collection |
| `data` | [DataExtraction](#dataextraction-object) | Yes | - | Data configuration |

<details>
<summary>Examples</summary>

```javascript
{
    key: 'my-collection',
    data: {
      extract: [{
        source: 'Products',
        field: 'Product',
        value: d => d.name,
        label: d => `<${d.name}>`
        props: {
          year: { field: 'Year' }
          num: { field: 'Sales' }
        }
      }],
      filter: d => d.label !== 'Sneakers', // extract everything except Sneakers
      sort: (a, b) => a.label > b.label ? -1 : 1, // sort descending
    }
}
```

</details>

---

### Component `object`

Component instance

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Type of component |
| `key` | string | Yes | - | Key of the component |

---

### ComponentAxis `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'axis' | Yes | - | component type |
| `scale` | string | Yes | - | reference to band or linear scale |
| `settings` | [DiscreteSettings](#discretesettings-object) \| [ContinuousSettings](#continuoussettings-object) | No | - | discrete or continuous axis settings |

<details>
<summary>Examples</summary>

```javascript
{
 type: 'axis',
 scale: '<name-of-scale>'
}
```

</details>

---

### ComponentBox `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'box' | Yes | - | component type |
| `data` | object | Yes | - |  |
| `settings` | object | Yes | - |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `min` | number | No | - | Min |
| `max` | number | No | - | Max |
| `start` | number | No | - | Start of box |
| `end` | number | No | - | End of box |
| `med` | number | No | - | Median |

</details>

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `major` | object | Yes | - |  |
| `minor` | object | Yes | - |  |
| `orientation` | string | No | "vertical" | Which orientation to use (vertical or horizontal) |
| `box` | object | No | - | Visual properties for the box shape in the box marker |
| `line` | object | No | - | Visual properties for lines between min-start, end-max. |
| `whisker` | object | No | - | All the visual properties for whiskers at min and max. |
| `median` | object | No | - | Visual properties for the median |
| `oob` | object | No | - | EXPERIMENTAL: Out of bounds symbol utilizing the symbol API |

<details>
<summary>Properties of `major`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scale` | string | Yes | - | The scale to use along the major (dimension) axis |
| `ref` | string \| [MajorReference](#majorreference-object) | No | "self" | Reference to the data property along the major axis |

</details>

<details>
<summary>Properties of `minor`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scale` | string | Yes | - | The scale to use along the minor (measure) axis |

</details>

<details>
<summary>Properties of `box`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true | Boolean for showing the box shape |
| `fill` | string | No | "#fff" |  |
| `stroke` | string | No | "#000" |  |
| `strokeWidth` | number | No | 1 |  |
| `strokeLinejoin` | string | No | "miter" |  |
| `width` | number | No | 1 |  |
| `maxWidthPx` | number | No | 100 | Maximum width of the box in pixels (not applicable when using major start and end) |
| `minWidthPx` | number | No | 1 | Minimum width of the box in pixels (not applicable when using major start and end) |
| `minHeightPx` | number | No | 1 | Minimum height of the box shape |

</details>

<details>
<summary>Properties of `line`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `stroke` | string | No | "#000" |  |
| `strokeWidth` | number | No | 1 |  |

</details>

<details>
<summary>Properties of `whisker`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `stroke` | string | No | "#000" |  |
| `strokeWidth` | number | No | 1 |  |
| `width` | number | No | 1 |  |

</details>

<details>
<summary>Properties of `median`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `stroke` | string | No | "#000" |  |
| `strokeWidth` | number | No | 1 |  |

</details>

<details>
<summary>Properties of `oob`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `type` | string | No | "n-polygon" | Type of the symbol to be used |
| `fill` | string | No | "#999" | Fill color of the symbol |
| `stroke` | string | No | "#000" | Stroke color |
| `strokeWidth` | number | No | 0 | Stroke width |
| `size` | number | No | 10 | Size/width of the symbol in pixels |
| `sides` | number | No | 3 | Number of sides for a n-polygon (3 for triangle) |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: "box",
  data: {
   mapTo: {
     min: { source: "/qHyperCube/qMeasureInfo/0" },
     start: { source: "/qHyperCube/qMeasureInfo/1" },
     med: { source: "/qHyperCube/qMeasureInfo/2" },
     end: { source: "/qHyperCube/qMeasureInfo/3" },
     max: { source: "/qHyperCube/qMeasureInfo/4" },
   },
   groupBy: {
     source: "/qHyperCube/qDimensionInfo/0"
   }
 },
 settings: {
   major: {
     scale: { source: "/qHyperCube/qDimensionInfo/0" }
   },
   minor: {
     scale: { source: ["/qHyperCube/qMeasureInfo/0",
              "/qHyperCube/qMeasureInfo/1",
              "/qHyperCube/qMeasureInfo/2",
              "/qHyperCube/qMeasureInfo/3",
              "/qHyperCube/qMeasureInfo/4"] }
   }
 }
}
```

</details>

---

### ComponentBrushArea `object`

extends [ComponentSettings](#componentsettings-interface)

A component that can brush a rectangular area

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'brush-area' | Yes | - | component type |
| `settings` | object | Yes | - |  |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `brush` | object | Yes | - |  |

<details>
<summary>Properties of `brush`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | [BrushTargetConfig](#brushtargetconfig-object)[] | Yes | - |  |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'brush-area',
 brush: {
   components: [{ key: '<target-component>', contexts: ['highlight'] }]
 }
}
```

</details>

---

### ComponentBrushAreaDir `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'brush-area-dir' | Yes | - | component type |
| `settings` | object | Yes | - |  |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `brush` | object | Yes | - |  |
| `direction` | string | No | "vertical" | Rendering direction [horizontal\|vertical] |
| `bubbles` | object | No | - |  |
| `target` | object | No | - |  |

<details>
<summary>Properties of `brush`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | [BrushTargetConfig](#brushtargetconfig-object)[] | Yes | - |  |

</details>

<details>
<summary>Properties of `bubbles`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true | True to show label bubble, false otherwise |
| `align` | string | No | "start" | Where to anchor bubble [start\|end] |
| `label` | function | No | - | Callback function for the labels |

</details>

<details>
<summary>Properties of `target`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | string[] | No | - | Render matching overlay on target components |

</details>

</details>

---

### ComponentBrushLasso `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'brush-lasso' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lasso` | object | No | - | Lasso style settings |
| `snapIndicator` | object | No | - | Snap indicator settings |
| `startPoint` | object | No | - | Start point style settings |
| `brush` | object | No | - |  |

<details>
<summary>Properties of `lasso`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | string | No | "transparent" |  |
| `stroke` | string | No | "black" |  |
| `strokeWidth` | number | No | 2 |  |
| `opacity` | number | No | 0.7 |  |
| `strokeDasharray` | number | No | - |  |

</details>

<details>
<summary>Properties of `snapIndicator`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `threshold` | number | No | 75 | The distance in pixel to show the snap indicator, if less then threshold the indicator is dispalyed |
| `strokeDasharray` | string | No | "5, 5" |  |
| `stroke` | string | No | "black" |  |
| `strokeWidth` | number | No | 2 |  |
| `opacity` | number | No | 0.5 |  |

</details>

<details>
<summary>Properties of `startPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `r` | number | No | 10 | Circle radius |
| `stroke` | string | No | "green" |  |
| `strokeWidth` | number | No | 1 |  |
| `opacity` | number | No | 1 |  |

</details>

<details>
<summary>Properties of `brush`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | object[] | Yes | - | Array of components to brush on. |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'brush-lasso',
 settings: {
   brush: {
     components: [{ key: '<target-component>', contexts: ['<brush-context>'] }]
   }
 },
}
```

</details>

---

### ComponentBrushRange `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'brush-range' | Yes | - | component type |
| `settings` | object | Yes | - |  |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `brush` | string \| object | Yes | - | Brush context to apply changes to |
| `scale` | string | Yes | - | Scale to extract data from |
| `direction` | string | No | "vertical" | Rendering direction [horizontal\|vertical] |
| `bubbles` | object | No | - |  |
| `target` | object | No | - |  |

<details>
<summary>Properties of `bubbles`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true | True to show label bubble, false otherwise |
| `align` | string | No | "start" | Where to anchor bubble [start\|end] |
| `label` | function | No | - | Callback function for the labels |

</details>

<details>
<summary>Properties of `target`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | string[] | No | - | Render matching overlay on target components |
| `selector` | string | No | - | Instead of targeting a component, target one or more shapes |
| `fillSelector` | string | No | - | Target a subset of the selector as fill area. Only applicable if `selector` property is set |

</details>

</details>

---

### ComponentContainer `object`  **[experimental]**

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'container' | Yes | - | component type |

<details>
<summary>Examples</summary>

```javascript
{
 type: 'container',
 preferredSize: ({ inner, outer, dock, children }) => {
   const sizes = children.map(c => c.preferredSize({ inner, outer }));
   return Math.max(...sizes);
 },
 strategy: (rect, components) => {
   const height = rect.height / components.length;
   components.forEach((c, i) => {
     c.resize({ ...rect, height, y: rect.y + i * height })
   });
   return { visible: components, hidden: [], order: components };
 },
 components: [
    ...
 ],
}
```

</details>

---

### ComponentGridLine `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'grid-line' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | object | Yes | - |  |
| `y` | object | Yes | - |  |
| `ticks` | object | No | - |  |
| `minorTicks` | object | No | - |  |

<details>
<summary>Properties of `x`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scale` | string | Yes | - | The scale to use along x |

</details>

<details>
<summary>Properties of `y`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scale` | string | Yes | - | The scale to use along y |

</details>

<details>
<summary>Properties of `ticks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `stroke` | string | No | "black" |  |
| `strokeWidth` | number | No | "1" |  |
| `strokeDasharray` | string | No | - |  |

</details>

<details>
<summary>Properties of `minorTicks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true |  |
| `stroke` | string | No | "black" |  |
| `strokeWidth` | number | No | "1" |  |
| `strokeDasharray` | string | No | - |  |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'grid-line',
 settings: {
   x: {
     scale: '<name-of-scale>',
   },
   y: {
     scale: '<name-of-scale>',
   },
 },
}
```

</details>

---

### ComponentLabels `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'labels' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sources` | [Source](#source-object)[] | Yes | - | Source settings |

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: 'labels',
  settings: {
    sources: [
      {
        component: 'bars',
        selector: 'rect', // select all 'rect' shapes from the 'bars' component
        strategy: {
          type: 'bar', // the strategy type
          settings: {
            labels: [
              {
                label({ data }) {
                  return data ? data.end.label : '';
                },
                placements: [
                  // label placements in prio order. Label will be placed in the first place it fits into
                  { position: 'inside', fill: '#fff' },
                  { position: 'outside', fill: '#666' },
                ],
              },
            ],
          },
        },
      },
    ],
  },
}
```

</details>

---

### ComponentLegendCat `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'legend-cat' | Yes | - | component type |
| `scale` | string | Yes | - | Reference to categorical color scale |
| `settings` | object | No | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `item` | object | No | - | Settings applied per item |
| `layout` | object | No | - |  |
| `navigation` | object | No | - |  |
| `title` | object | No | - |  |

<details>
<summary>Properties of `item`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `align` | number | No | 0.5 | Align item |
| `justify` | number | No | 0.5 | Justify item |
| `label` | object | No | - |  |
| `shape` | object | No | - |  |
| `show` | boolean | No | true | Whether to show the current item |

<details>
<summary>Properties of `label`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontFamily` | string | No | "Arial" | Font family |
| `fontSize` | string | No | "12px" | Font size in pixels |
| `lineHeight` | number | No | 1.2 | Line height as a multiple of the font size |
| `maxLines` | number | No | 2 | Max number of lines allowed if label is broken into multiple lines (only applicable with wordBreak) |
| `maxWidth` | number | No | 136 | Maximum width of label, in px |
| `wordBreak` | string | No | "none" | Word break rule, how to apply line break if label text overflows its maxWidth property. Either `'break-word'` or `'break-all'` |

</details>

<details>
<summary>Properties of `shape`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `size` | number | No | 12 | Size of shape in pixels |
| `type` | string | No | "square" | Type of shape |

</details>

</details>

<details>
<summary>Properties of `layout`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `direction` | string | No | "ltr" | Layout direction. Either `'ltr'` or `'rtl'` |
| `scrollOffset` | number | No | 0 | Initial scroll offset |
| `size` | number | No | 1 | Maximum number of columns (vertical) or rows (horizontal) |

</details>

<details>
<summary>Properties of `navigation`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `button` | object | No | - |  |
| `disabled` | boolean | No | false | Whether the button should be disabled or not |

<details>
<summary>Properties of `button`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `class` | object<string, boolean> | No | - |  |
| `content` | function | Yes | - |  |
| `tabIndex` | number | No | - |  |

</details>

</details>

<details>
<summary>Properties of `title`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `anchor` | string | Yes | "start" | Horizontal alignment of the text. Allowed values are `'start'`, `'middle'` and `'end'` |
| `fill` | string | No | "#595959" | Title color |
| `fontFamily` | string | No | "Arial" | Font family |
| `fontSize` | string | No | "16px" | Font size in pixels |
| `lineHeight` | number | No | 1.25 | Line height as a multiple of the font size |
| `maxLines` | number | No | 2 | Max number of lines allowed if label is broken into multiple lines, is only appled when `wordBreak` is not set to `'none'` |
| `maxWidth` | number | No | 156 | Maximum width of title, in px |
| `show` | boolean | No | true | Whether to show the title |
| `text` | string | No | - | Title text. Defaults to the title of the provided data field |
| `wordBreak` | string | No | "none" | Word break rule, how to apply line break if label text overflows its maxWidth property. Either `'break-word'` or `'break-all'` |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: 'legend-cat',
  scale: '<categorical-color-scale>',
}
```

</details>

---

### ComponentLegendSeq `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'legend-seq' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | string | Yes | - | Reference to definition of sequential color scale |
| `major` | string | Yes | - | Reference to definition of linear scale |
| `size` | number | No | 15 | Size in pixels of the legend, if vertical is the width and height otherwise |
| `length` | number | No | 1 | A value in the range 0-1 indicating the length of the legend node |
| `maxLengthPx` | number | No | 250 | Max length in pixels |
| `align` | number | No | 0.5 | A value in the range 0-1 indicating horizontal alignment of the legend's content. 0 aligns to the left, 1 to the right. |
| `justify` | number | No | 0 | A value in the range 0-1 indicating vertical alignment of the legend's content. 0 aligns to the top, 1 to the bottom. |
| `padding` | object | No | - |  |
| `tick` | object | No | - |  |
| `title` | object | No | - | Title settings |

<details>
<summary>Properties of `padding`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `left` | number | No | 5 | Size in pixels |
| `right` | number | No | 5 | Size in pixels |
| `top` | number | No | 5 | Size in pixels |
| `bottom` | number | No | 5 | Size in pixels |

</details>

<details>
<summary>Properties of `tick`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | function | No | - | Function applied to all tick values. Return value should be a string and is used as label |
| `fill` | string | No | "#595959" | Tick color |
| `fontSize` | string | No | "12px" | Font size in pixels |
| `fontFamily` | string | No | "Arial" | Font family |
| `maxLengthPx` | number | No | 150 | Max length in pixels |
| `anchor` | string | No | "" | Where to anchor the tick in relation to the legend node, supported values are [top, bottom, left and right] or empty string to auto anchor |
| `padding` | number | No | 5 | padding in pixels to the legend node |

</details>

<details>
<summary>Properties of `title`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true | Toggle title on/off |
| `text` | string | No | "" | Title text. Defaults to the title of the provided data field |
| `fill` | string | No | "#595959" | Title color |
| `fontSize` | string | No | "12px" | Font size in pixels |
| `fontFamily` | string | No | "Arial" | Font family |
| `maxLengthPx` | number | No | 100 | Max length in pixels |
| `padding` | number | No | 5 | padding in pixels to the legend node |
| `anchor` | string | No | "" | Where to anchor the title in relation to the legend node, supported values are [top, left and right] or empty string to auto anchor |
| `wordBreak` | string | No | "none" | How overflowing title is handled, if it should insert line breaks at word boundries (break-word) or character boundries (break-all) |
| `hyphens` | string | No | "auto" | How words should be hyphenated when text wraps across multiple lines (only applicable with wordBreak) |
| `maxLines` | number | No | 2 | Number of allowed lines if title contains line breaks (only applicable with wordBreak) |
| `lineHeight` | number | No | 1.2 | A multiplier defining the distance between lines (only applicable with wordBreak) |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: 'legend-seq',
  settings: {
    fill: '<sequential-color-scale>',
    major: '<linear-scale>',
  }
}
```

</details>

---

### ComponentLine `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'line' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connect` | boolean | No | false |  |
| `coordinates` | object | Yes | - |  |
| `layers` | object | Yes | - |  |
| `orientation` | string | No | "horizontal" |  |

<details>
<summary>Properties of `coordinates`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `defined` | [DatumBoolean](#datumboolean-union) | No | true |  |
| `layerId` | number | No | 0 |  |
| `major` | number | Yes | 0.5 |  |
| `minor` | number | Yes | 0.5 |  |

</details>

<details>
<summary>Properties of `layers`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `area` | object | Yes | - |  |
| `curve` | string | No | "linear" |  |
| `line` | object | Yes | - |  |
| `show` | boolean | No | true |  |
| `sort` | [LayerSort](#layersorta-b-function) | No | - |  |

<details>
<summary>Properties of `area`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | string | No | "#ccc" |  |
| `opacity` | number | No | 0.8 |  |
| `show` | boolean | No | true |  |

</details>

<details>
<summary>Properties of `line`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `opacity` | number | No | 1 |  |
| `show` | boolean | No | true |  |
| `showMinor0` | boolean | No | true |  |
| `stroke` | string | No | "#ccc" |  |
| `strokeDasharray` | string | No | - |  |
| `strokeLinejoin` | string | No | "miter" |  |
| `strokeWidth` | number | No | 1 |  |

</details>

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: "line",
  data: {
    extract: {
      field: "Year",
      props: {
        sales: { field: "Sales" },
      },
    },
  },
  settings: {
    coordinates: {
      major: { scale: "t" },
      minor: { scale: "y", ref: "sales" },
    },
  },
}
```

</details>

---

### ComponentPie `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'pie' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `endAngle` | number | No | - | End angle of the pie, in radians |
| `slice` | object | Yes | - |  |
| `startAngle` | number | No | 0 | Start angle of the pie, in radians |

<details>
<summary>Properties of `slice`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `arc` | number | No | 1 | Absolute value of the slice's arc length |
| `cornerRadius` | number | No | 0 | Corner radius of the slice, in pixels |
| `fill` | string | No | "#333" | Fill color of the slice |
| `innerRadius` | number | No | 0 | Inner radius of the slice |
| `offset` | number | No | 0 | Radial offset of the slice |
| `opacity` | number | No | 1 | Opacity of the slice |
| `outerRadius` | number | No | 0.8 | Outer radius of the slice |
| `show` | boolean | No | true | Visibility of the slice |
| `stroke` | string | No | "#ccc" | Stroke color of the slice |
| `strokeLinejoin` | string | No | "round" | Stroke line join |
| `strokeWidth` | number | No | 1 | Stroke width of the slice |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: 'pie',
  data: {
    extract: {
      field: 'Region',
      props: {
        num: { field: 'Population' }
      }
    }
  },
  settings: {
    startAngle: Math.PI / 2,
    endAngle: -Math.PI / 2,
    slice: {
      arc: { ref: 'num' },
      fill: 'green',
      stroke: 'red',
      strokeWidth: 2,
      strokeLinejoin: 'round',
      innerRadius: 0.6,
      outerRadius 0.8,
      opacity: 0.8,
      offset: 0.2
    }
  }
}
```

</details>

---

### ComponentPoint `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'point' | Yes | - | component type |
| `settings` | object | No | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | [DatumString](#datumstring-union) | No | "#333" | Fill color |
| `imageSettings` | object | No | - | Image settings. Applies only when point shape is set to 'image'. |
| `label` | [DatumString](#datumstring-union) | No | "" | Label |
| `opacity` | [DatumNumber](#datumnumber-union) | No | 1 | Opacity of shape |
| `shape` | [DatumString](#datumstring-union) | No | "circle" | Type of shape |
| `show` | [DatumBoolean](#datumboolean-union) | No | true | Whether or not to show the point |
| `size` | [DatumNumber](#datumnumber-union) | No | 1 | Normalized size of shape |
| `sizeLimits` | object | No | - |  |
| `stroke` | [DatumString](#datumstring-union) | No | "#ccc" | Stroke color |
| `strokeDasharray` | [DatumString](#datumstring-union) | No | "" | Stroke dash array |
| `strokeLinejoin` | [DatumString](#datumstring-union) | No | "miter" | Stroke line join |
| `strokeWidth` | [DatumNumber](#datumnumber-union) | No | 0 | Stroke width |
| `x` | [DatumNumber](#datumnumber-union) | No | 0.5 | Normalized x coordinate |
| `y` | [DatumNumber](#datumnumber-union) | No | 0.5 | Normalized y coordinate |

<details>
<summary>Properties of `imageSettings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `height` | number | No | - | Image height. If not set, the image's natural height is used |
| `imageScalingFactor` | number | No | - | Image scaling factor |
| `imageSrc` | string | No | - | Image source |
| `position` | string | No | "center-center" | Position of image |
| `symbol` | string | No | "rectangle" | Shape of image: 'rectangle' or 'circle' |
| `width` | number | No | - | Image width. If not set, the image's natural width is used |

</details>

<details>
<summary>Properties of `sizeLimits`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `maxPx` | number | No | 10000 | Maximum size of shape, in pixels |
| `maxRelDiscrete` | number | No | 1 | Maximum size relative discrete scale banwidth |
| `maxRelExtent` | number | No | 0.1 | Maximum size relative linear scale extent |
| `minPx` | number | No | 1 | Minimum size of shape, in pixels |
| `minRelDiscrete` | number | No | 0.1 | Minimum size relative discrete scale banwidth |
| `minRelExtent` | number | No | 0.01 | Minimum size relative linear scale extent |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
  type: 'point',
  data: {
    extract: {
      field: 'Month',
      props: {
        x: { field: 'Margin' },
        y: { field: 'Year' }
      }
    }
  },
  settings: {
    x: { scale: 'm' },
    y: { scale: 'y' },
  }
}
```

</details>

---

### ComponentRefLine `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'ref-line' | Yes | - | component type |
| `settings` | object | Yes | - | Component settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lines` | object | Yes | - | X & Y Lines |

<details>
<summary>Properties of `lines`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | [Line](#line-object)[] | No | "[]" | Reference lines along X axis |
| `y` | [Line](#line-object)[] | No | "[]" | Reference lines along Y axis |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'ref-line',
 lines: {
   y: [{
     scale: 'y',
     value: 5000,
     label: {
       text: 'value label'
     }
     slope: 0.5,
   }]
 }
}
```

</details>

---

### ComponentSettings `interface`

Generic settings available to all components

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Component type (ex: axis, point, ...) |
| `preferredSize` | function | No | - | Function returning the preferred size |
| `created` | function | No | - | Called when the component has been created |
| `beforeMount` | function | No | - | Called before the component has been mounted |
| `mounted` | function | No | - | Called after the component has been mounted |
| `beforeUpdate` | function | No | - | Called before the component has been updated |
| `updated` | function | No | - | Called after the component has been updated |
| `beforeRender` | function | No | - | Called before the component has been rendered |
| `beforeDestroy` | function | No | - | Called before the component has been destroyed |
| `destroyed` | function | No | - | Called after the component has been destroyed |
| `brush` | object | No | - | Brush settings |
| `layout` | object | No | - | Layout settings |
| `show` | boolean | No | true | If the component should be rendered |
| `scale` | string | No | - | Named scale. Will be provided to the component if it asks for it. |
| `formatter` | string | No | - | Named formatter. Fallback to create formatter from scale. Will be provided to the component if it asks for it. |
| `components` | [ComponentSettings](#componentsettings-interface)[] | No | - | **[experimental]** Optional list of child components |
| `strategy` | [DockLayoutSettings](#docklayoutsettings-object) \| [customLayoutFunction](#customlayoutfunctionrect-components-function) | No | - | **[experimental]** Layout strategy used for child components. |
| `data` | [DataExtraction](#dataextraction-object) \| [DataFieldExtraction](#datafieldextraction-object) | No | - | Extracted data that should be available to the component |
| `rendererSettings` | [RendererSettings](#renderersettings-object-experimental) | No | - | Settings for the renderer used to render the component |
| `key` | string | No | - | Component key |

<details>
<summary>Properties of `brush`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `trigger` | [BrushTriggerSettings](#brushtriggersettings-object)[] | No | - | Trigger settings |
| `consume` | [BrushConsumeSettings](#brushconsumesettings-object)[] | No | - | Consume settings |
| `sortNodes` | function | No | - | Sorting function for nodes. Should return sorted nodes. |

</details>

<details>
<summary>Properties of `layout`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `displayOrder` | number | No | 0 |  |
| `prioOrder` | number | No | 0 |  |
| `minimumLayoutMode` | string \| Object | No | - | Refer to layout sizes defined by layoutModes in `strategy` |
| `dock` | string | No | - | left, right, top or bottom |

</details>

---

### ComponentText `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'text' | Yes | - | component type |
| `text` | string \| function | Yes | - | Text to display |
| `settings` | object | Yes | - |  |
| `style` | object | Yes | - |  |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paddingStart` | number | No | 5 | Start padding in pixels |
| `paddingEnd` | number | No | 5 | End padding in pixels |
| `paddingLeft` | number | No | 0 | Left padding in pixels |
| `paddingRight` | number | No | 0 | Right padding in pixels |
| `anchor` | string | No | "center" | Where to v- or h-align the text. Supports `left`, `right`, `top`, `bottom` and `center` |
| `join` | string | No | ", " | String to add when joining titles from multiple sources |
| `maxLengthPx` | number | No | - | Limit the text length |

</details>

<details>
<summary>Properties of `style`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `text` | object | No | - |  |

<details>
<summary>Properties of `text`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontSize` | string | No | "12px" | Font size of text |
| `fontFamily` | string | No | "Source Sans Pro" | Font family of text |
| `fontWeight` | string | No | "normal" | Font weight of text |
| `fill` | string | No | "#ffffff" | Fill color of text |
| `stroke` | string | No | "transparent" | Stroke of text |
| `strokeWidth` | number | No | 0 | Stroke width of text |
| `opacity` | number | No | 1 | Opacity of text |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'text',
 text: 'my title',
 dock: 'left',
 settings: {
   anchor: 'left',
 }
}
```

</details>

---

### ComponentTooltip `object`

extends [ComponentSettings](#componentsettings-interface)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'tooltip' | Yes | - | component type |
| `settings` | object | Yes | - |  |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appendTo` | HTMLElement | No | - | Explicitly set a target element. This allows the tooltip to attach itself outside the picasso container. |
| `arrowClass` | object<string, boolean> | No | - | Set arrow class. |
| `contentClass` | object<string, boolean> | No | - | Set content class. |
| `delay` | number | No | 500 | Delay before the tooltip is rendered, in milliseconds |
| `direction` | string | No | "ltr" | Content direction [ltr \| rtl] |
| `duration` | number | No | 8000 | How long the tooltip is visible, in milliseconds |
| `placement` | object | No | - |  |
| `tooltipClass` | object<string, boolean> | No | - | Set tooltip class. |

<details>
<summary>Properties of `placement`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `area` | number | No | "viewport" | Specify the limiting area, where target is the component area unless the appendTo property is set, in which case it referes to the appendTo element. Viewport is the browser viewport.  Available options are: [viewport \| target] |
| `dock` | string | No | "auto" | Docking position of the tooltip. Available positions: [left \| right \| top \| bottom \| auto] |
| `offset` | number | No | 8 | Distance from the content area to the tooltip position, in px. |
| `type` | string | No | "pointer" | Available types: [pointer \| bounds \| slice] |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
picasso.chart({
  settings: {
    interactions: [{
      type: 'native',
      events: {
        mousemove(e) {
          const tooltip = this.chart.component('<tooltip-key>');
          tooltip.emit('show', e);
        },
        mouseleave(e) {
          const tooltip = this.chart.component('<tooltip-key>');
          tooltip.emit('hide');
        }
      }
    }],
    components: [
      {
        key: '<tooltip-key>',
        type: 'tooltip'
      }
    ]
  },
  ...
});
```

</details>

---

### ComponentTypes `union`

---

### customLayoutFunction(rect, components) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rect` | [Rect](#rect-object) | Yes | - |  |
| `components` | object[] | Yes | - |  |

---

### DataExtraction `object`

Used to extract data from a `DataSource`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `extract` | [Extract](#extract-object) \| [Extract](#extract-object)[] | Yes | - | Extract definition |
| `stack` | object | No | - | If provided, defines how the data should be stacked |
| `filter` | [FilterCallback](#filtercallbackdatum-function) | No | - | Callback function to filter the extracted data items |
| `sort` | [SortCallback](#sortcallbacka-b-function) | No | - | Callback function to sort the extracted data items |

<details>
<summary>Properties of `stack`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `stackKey` | [StackKeyCallback](#stackkeycallbackdatum-function) | Yes | - | Callback function. Should return the key to stack by |
| `value` | [StackValueCallback](#stackvaluecallbackdatum-function) | Yes | - | Callback function. Should return the data value to stack with |
| `stackByKey` | string[] | No | - | Optional list of keys to stack by |

</details>

<details>
<summary>Examples</summary>

```javascript
{
  extract: [{
    source: 'Products',
    field: 'Product',
    value: d => d.name,
    label: d => `<${d.name}>`
    props: {
      year: { field: 'Year' }
      num: { field: 'Sales' }
    }
  }],
  filter: d => d.label !== 'Sneakers', // extract everything except Sneakers
  sort: (a, b) => a.label > b.label ? -1 : 1, // sort descending
}
```

</details>

---

### DataFieldExtraction `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `source` | string | Yes | - | Which data source to extract from |
| `field` | string | Yes | - | The field to extract data from |
| `value` | [ValueFn](#valuefncell-function) \| string \| number \| boolean | No | - | The field value accessor |
| `label` | [LabelFn](#labelfncell-function) \| string \| number \| boolean | No | - | The field label accessor |

<details>
<summary>Examples</summary>

```javascript
{
 source: 'Products',
 field: 'Sales',
 value: (val) => Math.round(val),
 label: (val) => `<${val}>`
}
```

</details>

---

### Dataset `interface`

---

#### extract(config) `function`

Extract data items from this dataset

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | [Extract](#extract-object) \| [DataFieldExtraction](#datafieldextraction-object) | Yes | - |  |

##### Returns

[DatumExtract](#datumextract-object)[]

---

#### field(query) `function`

Find a field within this dataset

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | Yes | - | The field to find |

##### Returns

[Field](#field-object)

---

#### fields() `function`

Get all fields within this dataset

##### Returns

[Field](#field-object)[]

---

#### hierarchy() `function`

##### Returns

`null`

---

#### key() `function`

Get the key identifying this dataset

##### Returns

`string`

---

#### raw() `function`

Get the raw data

##### Returns

`any`

---

### DataSource `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | No | - | Unique identifier for this data source |
| `type` | string | Yes | - | The dataset type |
| `data` | any | Yes | - | Data |

---

### datumAccessor(d) `function`

Callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `d` | [DatumExtract](#datumextract-object) | Yes | - | datum |

<details>
<summary>Examples</summary>

```javascript
(d) => Math.min(0, d.value);
```

</details>

---

### DatumBoolean `union`

Custom type that is either a boolean, DatumConfig or a datumAccessor

---

### DatumConfig `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scale` | string | No | - | Name of a scale |
| `fn` | [datumAccessor](#datumaccessord-function) | No | - |  |
| `ref` | string | No | - | A reference to a DatumExtract property |

<details>
<summary>Examples</summary>

```javascript
// Implicitly resolve the datum by passing a referenced data through the scale
{
 scale: '<name-of-scale>',
 ref: '<data-property>'
}

// or explicitly resolve the datum using callback function
{
 fn: (d) => Math.min(0, d.datum.x.value);
}
```

</details>

---

### DatumExtract `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | any | Yes | - | The extracted value |
| `label` | string | Yes | - | The extracted value as a string |
| `source` | object | Yes | - | The data source of the extracted data |

<details>
<summary>Properties of `source`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | The data-source key |
| `field` | string | Yes | - | The source field |

</details>

---

### DatumNumber `union`

Custom type that is either a number, DatumConfig or a datumAccessor

---

### DatumString `union`

Custom type that is either a string, DatumConfig or a datumAccessor

---

### DockLayoutSettings `object`

Dock layout settings

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `logicalSize` | object | No | - | Logical size |
| `center` | object | No | - | Define how much space the center dock area requires |
| `layoutModes` | object<string, [LayoutMode](#layoutmode-object)> | No | - | Dictionary with named sizes |
| `size` | object | No | - | Size is equal to that of the container (element) of the chart by default. It's possible to overwrite it by explicitly setting width or height |

<details>
<summary>Properties of `logicalSize`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `width` | number | No | - | Width in pixels |
| `height` | number | No | - | Height in pixels |
| `preserveAspectRatio` | boolean | No | false | If true, takes the smallest ratio of width/height between logical and physical size ( physical / logical ) |
| `align` | number | No | 0.5 | Normalized value between 0-1. Defines how the space around the scaled axis is spread in the container, with 0.5 meaning the spread is equal on both sides. Only applicable if preserveAspectRatio is set to true |

</details>

<details>
<summary>Properties of `center`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `minWidthRatio` | number | No | 0.5 | Value between 0 and 1 |
| `minHeightRatio` | number | No | 0.5 | Value between 0 and 1 |
| `minWidth` | number | No | - | Width in pixels |
| `minHeight` | number | No | - | Height in pixels |

</details>

<details>
<summary>Properties of `size`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `width` | number | No | - | Width in pixels |
| `height` | number | No | - | Height in pixels |

</details>

---

### Field `object`

---

#### formatter() `function`

Returns a formatter adapted to the content of this field.

---

#### id() `function`

Returns this field's id

##### Returns

`string`

---

#### items() `function`

Returns the values of this field.

##### Returns

[DatumExtract](#datumextract-object)[]

---

#### key() `function`

Returns this field's key

##### Returns

`string`

---

#### max() `function`

Returns the max value of this field.

##### Returns

`number`

---

#### min() `function`

Returns the min value of this field.

##### Returns

`number`

---

#### raw() `function`

Returns the input data

##### Returns

`any`

---

#### tags() `function`

Returns the tags.

##### Returns

`string[]`

---

#### title() `function`

Returns this field's title.

##### Returns

`string`

---

#### type() `function`

Returns this field's type: 'dimension' or 'measure'.

##### Returns

`string`

---

### formatter() `function`

#### Returns

`any` - Returns a formatted value

---

### FormatterDefinition `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `formatter` | string | No | - | Name of the formatter |
| `type` | string | No | - | Type of formatter |
| `format` | string | No | - | Format string |
| `data` | [DataExtraction](#dataextraction-object) \| [DataFieldExtraction](#datafieldextraction-object) | No | - | The data to create formatter from |

---

### Geopolygon `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `polygons` | [Polygon](#polygon-object)[] | Yes | - | Array of polygons |

---

### Interaction `object`

Interaction instance

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `on` | function | Yes | - | Enable interaction |
| `off` | function | Yes | - | Disable interaction |
| `destroy` | function | Yes | - | Destroy interaction |
| `key` | string | Yes | - | Interaction identifier |

---

### InteractionSettings `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Type of interaction handler |
| `key` | string | No | - | Unique key identifying the handler |
| `enable` | function \| boolean | Yes | - | Enable or disable the interaction handler. If a callback function is provided, it must return either true or false |

<details>
<summary>Examples</summary>

```javascript
{
 type: 'native',
 key: 'nativeHandler',
 enable: () => true,
 events: { // "events" is a property specific to the native handler
   mousemove: (e) => console.log('mousemove', e),
 }
}
```

</details>

---

### Line `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x1` | number | Yes | - | Start x-coordinate |
| `y1` | number | Yes | - | Start y-coordinate |
| `x2` | number | Yes | - | End x-coordinate |
| `y2` | number | Yes | - | End y-coordinate |

---

### Path `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `d` | string | Yes | - | Path definition |

---

### plugin(registries, options) `function`

Callback function to register a plugin

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `registries` | [Registries](#registries-object) | Yes | - |  |
| `options` | object | Yes | - |  |

---

### Point `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | number | Yes | - | X-coordinate |
| `y` | number | Yes | - | Y-coordinate |

---

### Polygon `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `points` | [Point](#point-object)[] | Yes | - | Array of connected points |

---

### Polyline `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `points` | [Point](#point-object)[] | Yes | - | Array of connected points |

---

### ProgressiveObject `object`  **[experimental]**

A format to represent a data chunk to be rendered.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `start` | number | Yes | - | Start index of a data chunk. |
| `end` | number | Yes | - | End index of a data chunk. |
| `isFirst` | boolean | Yes | - | If it is the first data chunk rendered. This helps to clear a canvas before rendering. |
| `isLast` | boolean | Yes | - | If it is the last data chunk rendered. This helps to update other components depending on a component with progressive rendering. |

---

### Rect `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | number | Yes | - | X-coordinate |
| `y` | number | Yes | - | Y-coordinate |
| `width` | number | Yes | - | Width |
| `height` | number | Yes | - | Height |

---

### Registries `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | [registry](#registrykey-value-function) | Yes | - | Component registry |
| `data` | [registry](#registrykey-value-function) | Yes | - | Data registry |
| `formatter` | [registry](#registrykey-value-function) | Yes | - | Formatter registry |
| `interaction` | [registry](#registrykey-value-function) | Yes | - | Interaction registry |
| `renderer` | [registry](#registrykey-value-function) | Yes | - | Renderer registry |
| `scale` | [registry](#registrykey-value-function) | Yes | - | Scale registry |

---

### registry(key, value?) `function`

Register a `value` with the given `key`. If `value` is omitted, returns the `value` of `key`.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | Name of the type to register |
| `value` | any | No | - | Value to store in the registry. |

#### Returns

`any` - Registered value

---

### Renderer `interface`

---

#### appendTo(element) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement | Yes | - | Element to attach renderer to |

##### Returns

`HTMLElement` - Root element of the renderer

---

#### clear() `function`

Clear all child elements from the renderer root element

##### Returns

[Renderer](#renderer-interface) - The renderer instance

---

#### destory() `function`

Remove the renderer root element from its parent element

---

#### element() `function`

Get the element this renderer is attached to

##### Returns

`HTMLElement`

---

#### findShapes(selector) `function`

Get all nodes matching the provided selector

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `selector` | string | Yes | - | CSS selector [type, attribute, universal, class] |

##### Returns

[SceneNode](#scenenode-class)[] - Array of objects containing matching nodes

---

#### itemsAt(geometry) `function`

Get nodes renderer at area

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `geometry` | [Point](#point-object) \| [Circle](#circle-object) \| [Rect](#rect-object) \| [Line](#line-object) \| [Polygon](#polygon-object) \| [Geopolygon](#geopolygon-object) | Yes | - | Get nodes that intersects with geometry |

##### Returns

[SceneNode](#scenenode-class)[]

---

#### measureText(opts) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `opts` | object | Yes | - |  |

##### Returns

`object` - Width and height of text

<details>
<summary>Examples</summary>

```javascript
measureText({
 text: 'my text',
 fontSize: '12px',
 fontFamily: 'Arial'
}); // returns { width: 20, height: 12 }
```

</details>

---

#### render(nodes) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `nodes` | object[] | Yes | - | Nodes to render |

##### Returns

`boolean` - True if the nodes were rendered, otherwise false

---

#### root() `function`

Get the root element of the renderer

##### Returns

`HTMLElement`

---

#### settings(settings?) `function`

Set or Get renderer settings

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `settings` | object | No | - | Settings for the renderer |

---

#### size(opts?) `function`

Set or Get the size definition of the renderer container.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `opts` | [SizeDefinition](#sizedefinition-object) | No | - | Size definition |

##### Returns

[SizeDefinition](#sizedefinition-object) - The current size definition

---

### RendererSettings `object`  **[experimental]**

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `transform` | [TransformFunction](#transformfunction-function-experimental) | No | - | Setting for applying transform without re-rendering the whole component completely. |
| `canvasBufferSize` | [CanvasBufferSize](#canvasbuffersize-union-experimental) | No | - | Specifies the size of buffer canvas (used together with transform setting). |
| `progressive` | [Progressive](#progressive-function-experimental) | No | - | Setting for applying progressive rendering to a canvas renderer |
| `disableScreenReader` | boolean | No | false | Setting to disable the screen reader for the component. If set to true, screen reader support will be disabled. This setting is not relevant when using the canvas renderer. |

---

### Scale `interface`

Scale instance

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Type of scale |

---

### ScaleBand `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "band" |  |
| `padding` | number | No | 0 | Sets both inner and outer padding to the same value |
| `paddingInner` | number | No | 0 | Inner padding |
| `paddingOuter` | number | No | 0 | Outer padding |
| `align` | number | No | 0.5 | Control how the outer padding should be distributed, where 0.5 would distribute the padding equally on both sides |
| `invert` | boolean | No | false | Invert the output range |
| `maxPxStep` | number | No | - | Explicitly limit the bandwidth to a pixel value |
| `label` | function | No | - | Callback label function, applied on each datum |
| `value` | function | No | - | Callback value function, applied on each datum |
| `range` | number[] \| function | No | "[0, 1]" | Set range explicitly (ignored when maxPxStep takes effect) |

---

### ScaleCategoricalColor `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "categorical-color" |  |
| `range` | string[] | No | false | CSS color values of the output range |
| `unknown` | string | No | - | Value to return when input value is unknown |
| `explicit` | object | No | - | Explicitly bind values to an output |

<details>
<summary>Properties of `explicit`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain[]` | object[] | No | - | Values to bind |
| `range[]` | string[] | No | - | Output range |

</details>

---

### ScaleDefinition `object`

Definition for creating a scale. Additional properties, specific for a type of scale, can be added as key/value pairs

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | - | Type of scale |
| `data` | [DataExtraction](#dataextraction-object) \| [DataFieldExtraction](#datafieldextraction-object) | No | - | Data configuration |

---

### ScaleLinear `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "linear" |  |
| `expand` | number | No | - | Expand the output range |
| `invert` | boolean | No | false | Invert the output range |
| `include` | number[] | No | - | Include specified numbers in the output range |
| `ticks` | object | No | - |  |
| `minorTicks` | object | No | - |  |
| `min` | number | No | - | Set an explicit minimum value |
| `max` | number | No | - | Set an explicit maximum value |

<details>
<summary>Properties of `ticks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tight` | boolean | No | false |  |
| `forceBounds` | boolean | No | false |  |
| `distance` | number | No | 100 | Approximate distance between each tick |
| `values` | number[] \| object[] | No | - | If set, ticks are no longer generated but instead equal to this set |
| `count` | number | No | - |  |

</details>

<details>
<summary>Properties of `minorTicks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `count` | number | No | 3 |  |

</details>

---

### ScaleSequentialColor `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "sequential-color" |  |
| `range` | string[] | No | - | CSS color values of the output range |
| `invert` | boolean | No | false | Invert range |
| `min` | number | No | - | Set an explicit minimum value |
| `max` | number | No | - | Set an explicit maximum value |

---

### ScaleThresholdColor `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "threshold-color" |  |
| `domain` | number[] | No | - | Values defining the thresholds |
| `range` | string[] | No | - | CSS color values of the output range |
| `invert` | boolean | No | false | Invert range |
| `min` | number | No | - | Set an explicit minimum value |
| `max` | number | No | - | Set an explicit maximum value |
| `nice` | boolean | No | false | If set to true, will generate 'nice' domain values. Ignored if domain is set. |

---

### SceneNode() `class`

Read-only object representing a node on the scene.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `attrs` | object | Yes | - | Node attributes |
| `bounds` | [Rect](#rect-object) | Yes | - | Bounding rectangle of the node. After any transform has been applied, if any, but excluding scaling transform related to devicePixelRatio. Origin is in the top-left corner of the scene element. |
| `children` | [SceneNode](#scenenode-class)[] | Yes | - | Get child nodes |
| `collider` | [Line](#line-object) \| [Rect](#rect-object) \| [Circle](#circle-object) \| [Path](#path-object) | Yes | - | Collider of the node. Transform on the node has been applied to the collider shape, if any, but excluding scaling transform related to devicePixelRatio. Origin is in the top-left corner of the scene element.  If node has no collider, null is returned. |
| `data` | any | Yes | - | Get the associated data |
| `desc` | object | Yes | - | Node description |
| `element` | HTMLElement | Yes | - | Element the scene is attached to |
| `key` | string | Yes | - | Key of the component this shape belongs to |
| `localBounds` | [Rect](#rect-object) | Yes | - | Bounding rectangle of the node within its local coordinate system. Origin is in the top-left corner of the scene element. |
| `parent` | [SceneNode](#scenenode-class) | Yes | - | Get parent node |
| `tag` | string | Yes | - | Node tag |
| `type` | string | Yes | - | Node type |

---

#### boundsRelativeTo(target, includeTransform) `function`

Bounding rectangle of the node, relative a target.

If target is an HTMLElement, the bounds are relative to the HTMLElement.
Any other target type will return the bounds relative to the viewport of the browser.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | HTMLElement \| any | Yes | - |  |
| `includeTransform` | boolean | Yes | true | Whether to include any applied transforms on the node |

##### Returns

[Rect](#rect-object)

<details>
<summary>Examples</summary>

```javascript
node.boundsRelativeTo($('div'));
node.boundsRelativeTo('viewport');
```

</details>

---

### svgRendererFactory(treeFactory?, ns?, sceneFn?) `function`

Create a new svg renderer

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `treeFactory` | function | No | - | Node tree factory |
| `ns` | string | No | - | Namespace definition |
| `sceneFn` | function | No | - | Scene factory |

#### Returns

[Renderer](#renderer-interface) - A svg renderer instance

---

### TransformObject `object`

A format to represent a transformation.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `horizontalScaling` | number | Yes | - |  |
| `horizontalSkewing` | number | Yes | - |  |
| `verticalSkewing` | number | Yes | - |  |
| `verticalScaling` | number | Yes | - |  |
| `horizontalMoving` | number | Yes | - |  |
| `verticalMoving` | number | Yes | - |  |

---

### Ranges `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `includeMax` | boolean | No | true | Whether or not the maximum value of a range should be included when determining if a value is brushed. |
| `includeMin` | boolean | No | true | Whether or not the minimum value of a range should be included when determining if a value is brushed. |
| `key` | string | No | - | An identifier that represents the data source of the value |

---

### beforeDestroy() `function`

Called before the chart has been destroyed

---

### beforeMount() `function`

Called before the chart has been mounted

---

### beforeRender() `function`

Called before the chart has been rendered

---

### beforeUpdate() `function`

Called before the chart has been updated

---

### created() `function`

Called when the chart has been created

---

### destroyed() `function`

Called after the chart has been destroyed

---

### mounted(element) `function`

Called after the chart has been mounted

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement | Yes | - | The element the chart been mounted to |

---

### updated() `function`

Called after the chart has been updated

---

### ContinuousSettings `object`

Continuous axis settings

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `arc` | [ArcSettings](#arcsettings-object) | No | - | Optional arc settings |
| `align` | string | No | "auto" | Set the anchoring point of the axis. Available options are `auto/left/right/bottom/top`. In `auto` the axis determines the best option. The options are restricted based on the axis orientation, a vertical axis may only anchor on `left` or `right` |
| `labels` | object | Yes | - |  |
| `line` | object | Yes | - |  |
| `minorTicks` | object | Yes | - |  |
| `paddingEnd` | number | No | 10 | Padding in direction perpendicular to the axis |
| `paddingStart` | number | No | 0 | Padding in direction perpendicular to the axis |
| `ticks` | object | Yes | - |  |

<details>
<summary>Properties of `labels`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `align` | number | No | 0.5 | Align act as a slider for the text bounding rect over the item bandwidth, given that the item have a bandwidth. |
| `centerEndLabels` | boolean | No | false | Center the labels at the end of the axis. Only applicable for vertical continuous axes. |
| `filterOverlapping` | boolean | No | true | Toggle whether labels should be filtered if they are overlapping. Filtering may be applied in a non-sequential order. If labels are overlapping and this setting is toggled off, the axis will automatically hide. |
| `margin` | number | No | 4 | Space in pixels between the tick and label. |
| `maxLengthPx` | number | No | 150 | Max length of labels in pixels |
| `minLengthPx` | number | No | 0 | Min length of labels in pixels. Labels will always at least require this much space |
| `offset` | number | No | 0 | Offset in pixels along the axis direction. |
| `show` | boolean | No | true | Toggle labels on/off |

</details>

<details>
<summary>Properties of `line`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | true | Toggle line on/off |

</details>

<details>
<summary>Properties of `minorTicks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `margin` | number | No | 0 | Space in pixels between the ticks and the line. |
| `show` | boolean | No | false | Toggle minor-ticks on/off |
| `tickSize` | number | No | 3 | Size of the ticks in pixels. |

</details>

<details>
<summary>Properties of `ticks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `margin` | number | No | 0 | Space in pixels between the ticks and the line. |
| `show` | boolean | No | true | Toggle ticks on/off |
| `tickSize` | number | No | 8 | Size of the ticks in pixels. |

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'axis',
 scale: '<name-of-linear-scale>',
 settings: {
   minorTicks: {
     show: false,
   },
 },
}
```

</details>

---

### DiscreteSettings `object`

Discrete axis settings

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `align` | string | No | "auto" | Set the anchoring point of the axis. Available options are `auto/left/right/bottom/top`. In `auto` the axis determines the best option. The options are restricted based on the axis orientation, a vertical axis may only anchor on `left` or `right` |
| `labels` | object | Yes | - |  |
| `line` | object | Yes | - |  |
| `paddingEnd` | number | No | 10 | Padding in direction perpendicular to the axis |
| `paddingStart` | number | No | 0 | Padding in direction perpendicular to the axis |
| `ticks` | object | Yes | - |  |

<details>
<summary>Properties of `labels`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `align` | number | No | 0.5 | Align act as a slider for the text bounding rect over the item bandwidth, given that the item have a bandwidth. Except when labels are tilted, then the align is a pure align that shifts the position of the label anchoring point. |
| `filterOverlapping` | boolean | No | false | Toggle whether labels should be filtered if they are overlapping. Filtering may be applied in a non-sequential order. If labels are overlapping and this setting is toggled off, the axis will automatically hide. |
| `margin` | number | No | 4 | Space in pixels between the tick and label. |
| `maxEdgeBleed` | number | No | - | Control the amount of space (in pixels) that labes can occupy outside their docking area. Only applicable when labels are in `tilted` mode. |
| `maxGlyphCount` | number | No | - | When only a sub-set of data is available, ex. when paging. This property can be used to let the axis estimate how much space the labels will consume, allowing it to give a consistent space estimate over the entire dataset when paging. |
| `maxLengthPx` | number | No | 150 | Max length of labels in pixels |
| `minLengthPx` | number | No | 0 | Min length of labels in pixels. Labels will always at least require this much space |
| `mode` | string | No | "auto" | Control how labels arrange themself. Availabe modes are `auto`, `horizontal`, `layered` and `tilted`. When set to `auto` the axis determines the best possible layout in the current context. |
| `offset` | number | No | 0 | Offset in pixels along the axis direction. |
| `show` | boolean | No | true | Toggle labels on/off |
| `tiltAngle` | number | No | 40 | Tilting angle in degrees. Capped between -90 and 90. Only applicable when labels are in `tilted` mode. |
| `tiltThreshold` | number | No | 0.7 | Threshold for toggle of tilted labels. Capped between 0 and 1. For example, if it is set to 0.7, then tilted labels will be toggled if less than 70% of the labels are visible. |

</details>

<details>
<summary>Properties of `line`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | No | false | Toggle line on/off |

</details>

<details>
<summary>Properties of `ticks`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `margin` | number | No | 0 | Space in pixels between the ticks and the line. |
| `show` | boolean | No | false | Toggle ticks on/off |
| `tickSize` | number | No | 4 | Size of the ticks in pixels. |

</details>

<details>
<summary>Examples</summary>

```javascript
{
 type: 'axis',
 scale: '<name-of-band-scale>',
 settings: {
   labels: {
     mode: 'tilted',
     tiltAngle: 40,
   },
 },
}
```

</details>

---

### MajorReference `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `start` | string | Yes | - | Reference to the data property of the start value along the major axis |
| `end` | string | Yes | - | Reference to the data property of the end value along the major axis |

---

### BarsLabelStrategy `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'bar' | Yes | - | Name of strategy |
| `settings` | object | Yes | - | Bars strategy settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `direction` | string \| function | No | "up" | The direction in which the bars are growing: 'up', 'down', 'right' or 'left'. |
| `orientation` | string | No | "auto" | Orientation of text: 'auto', 'horizontal' or 'vertical' |
| `fontFamily` | string | No | "Arial" |  |
| `fontSize` | number | No | 12 |  |
| `labels` | object[] | Yes | - |  |

</details>

---

### RowsLabelStrategy `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'rows' | Yes | - | Name of strategy |
| `settings` | object | Yes | - | Rows strategy settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontFamily` | string | No | "Arial" |  |
| `fontSize` | number | No | 12 |  |
| `justify` | number | No | 0.5 |  |
| `padding` | number | No | 4 |  |
| `labels` | object[] | Yes | - |  |

</details>

---

### SlicesLabelStrategy `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'slice' | Yes | - | Name of strategy |
| `settings` | object | Yes | - | Slices strategy settings |

<details>
<summary>Properties of `settings`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `direction` | string \| function | No | "horizontal" | The direction of the text: 'horizontal' or 'rotate'. |
| `fontFamily` | string | No | "Arial" |  |
| `fontSize` | number | No | 12 |  |
| `labels` | object[] | Yes | - |  |

</details>

---

### Source `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | string | Yes | - | Key of target component |
| `selector` | string | Yes | - | Shape selector |
| `strategy` | [BarsLabelStrategy](#barslabelstrategy-object) \| [RowsLabelStrategy](#rowslabelstrategy-object) \| [SlicesLabelStrategy](#sliceslabelstrategy-object) | Yes | - | Strategy settings |

---

### LayerSort(a, b) `function`

Callback function for layer sort

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `a` | object | Yes | - |  |
| `b` | object | Yes | - |  |

---

### GenericObject `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | string | No | "#fff" | Fill color |
| `stroke` | string | No | "transparent" | Stroke |
| `strokeWidth` | number | No | 0 | Stroke width |
| `opacity` | number | No | 1 | Opacity |

---

### GenericText `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `text` | string | No | "" | Text (if applicable) |
| `fontSize` | string | No | "12px" | Font size (if applicable) |
| `fontFamily` | string | No | "Arial" | Font family |
| `fill` | string | No | "#fff" | Fill color |
| `stroke` | string | No | "transparent" | Stroke |
| `strokeWidth` | number | No | 0 | Stroke width |
| `strokeDasharray` | string | No | - | Stroke dash array |
| `opacity` | number | No | 1 | Opacity |

---

### Line `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | number \| function | Yes | - | The value of the reference line. If a scale is specified, it is applied. |
| `scale` | string | No | - | Scale to use (if undefined will use normalized value 0-1) |
| `line` | [GenericObject](#genericobject-object) | No | "ComponentRefLine~GenericObject" | The style of the line |
| `label` | [LineLabel](#linelabel-object) | No | "ComponentRefLine~LineLabel" | The label style of the line |
| `slope` | number | No | 0 | The slope for the reference line |

---

### LineLabel `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `padding` | number | Yes | 5 | Padding inside the label |
| `text` | string | No | "" | Text |
| `fontSize` | string | No | "12px" | Font size |
| `fontFamily` | string | No | "Arial" | Font family |
| `stroke` | string | No | "transparent" | Stroke |
| `strokeWidth` | number | No | 0 | Stroke width |
| `opacity` | number | No | 1 | Opacity |
| `align` | number \| string | No | 0 | Alignment property left to right (0 = left, 1 = right). Also supports string ('left', 'center', 'middle', 'right') |
| `vAlign` | number \| string | No | 0 | Alignment property top to bottom (0 = top, 1 = bottom). Also supports string ('top', 'center', 'middle', 'bottom') |
| `maxWidth` | number | No | 1 | The maximum relative width to the width of the rendering area (see maxWidthPx as well) |
| `maxWidthPx` | number | No | 9999 | The maximum width in pixels. Labels will be rendered with the maximum size of the smallest value of maxWidth and maxWidthPx size, so you may specify maxWidth 0.8 but maxWidthPx 100 and will never be over 100px and never over 80% of the renderable area |
| `background` | [LineLabelBackground](#linelabelbackground-object) | No | "ComponentRefLine~LineLabelBackground" | The background style (rect behind text) |
| `show` | boolean | No | true | Show label |
| `showValue` | boolean | No | true | Show value label |

---

### LineLabelBackground `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | string | No | "#fff" | Fill color |
| `stroke` | string | No | "transparent" | Stroke |
| `strokeWidth` | number | No | 0 | Stroke width |
| `opacity` | number | No | 0.5 | Opacity |

---

### Extract `object`

Data extraction definition. Define how and what kind of data should be extracted from a `DataSource`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `source` | string | Yes | - | Which data source to extract from |
| `field` | string | Yes | - | The field to extract data from |
| `value` | [ValueFn](#valuefncell-function) \| string \| number \| boolean | No | - | The field value accessor |
| `label` | [LabelFn](#labelfncell-function) \| string \| number \| boolean | No | - | The field label accessor |
| `trackBy` | [TrackByFn](#trackbyfncell-function) | No | - | Track by value accessor |
| `reduce` | [ReduceFn](#reducefnvalues-function) \| string | No | - | Reducer function |
| `reduceLabel` | [ReduceLabelFn](#reducelabelfnlabels-value-function) \| string | No | - | Label reducer function |
| `filter` | [FilterFn](#filterfncell-function) | No | - | Filter function |
| `props` | object<string, [Props](#props-object)> | No | - | Additional properties to add to the extracted item |

<details>
<summary>Examples</summary>

```javascript
{
    source: 'Products',
    field: 'Product',
    value: (val) => val,
    label: (val) => `<${val}>`
    props: {
      year: { field: 'Year' }
      num: { field: 'Sales' }
    }
  }
```

</details>

---

### FilterCallback(datum) `function`

Callback function to filter the extracted data items

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `datum` | [DatumExtract](#datumextract-object) | Yes | - | The extracted datum |

#### Returns

`boolean` - Return true if the datum should be included in the final data set

---

### SortCallback(a, b) `function`

Callback function to sort the extracted data items

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `a` | [DatumExtract](#datumextract-object) | Yes | - | The extracted datum |
| `b` | [DatumExtract](#datumextract-object) | Yes | - | The extracted datum |

#### Returns

`number` - If less than 0, sort a before b. If greater than 0, sort b before a

---

### StackKeyCallback(datum) `function`

Callback function. Should return the key to stack by

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `datum` | [DatumExtract](#datumextract-object) | Yes | - | The extracted datum |

#### Returns

`any` - The data value to stack by

---

### StackValueCallback(datum) `function`

Callback function. Should return the data value to stack with

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `datum` | [DatumExtract](#datumextract-object) | Yes | - | The extracted datum |

#### Returns

`any` - The data value to stack with

---

### FilterFn(cell) `function`

Filter callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cell` | any | Yes | - | The field cell |

#### Returns

`boolean`

---

### LabelFn(cell) `function`

Label callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cell` | any | Yes | - | The field cell |

#### Returns

`string`

---

### Props `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `field` | string | Yes | - | The field to extract data from |
| `value` | [ValueFn](#valuefncell-function) \| string \| number \| boolean | No | - | The field value accessor |
| `label` | [LabelFn](#labelfncell-function) \| string \| number \| boolean | No | - | The field label accessor |

<details>
<summary>Examples</summary>

```javascript
{
 field: 'Sales',
 value: (val) => Math.round(val),
 label: (val) => `<${val}>`
}
```

</details>

---

### ReduceFn(values) `function`

Reduce callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `values` | any[] | Yes | - | The collected values to reduce |

#### Returns

`any`

---

### ReduceLabelFn(labels, value) `function`

ReduceLabel callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `labels` | any[] | Yes | - | The collected labels to reduce |
| `value` | any | Yes | - | Reduced value |

#### Returns

`string`

---

### TrackByFn(cell) `function`

TrackBy callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cell` | any | Yes | - | The field cell |

#### Returns

`any`

---

### ValueFn(cell) `function`

Value callback function

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cell` | any | Yes | - | The field cell |

#### Returns

`any`

---

### LayoutMode `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `width` | number | Yes | - |  |
| `height` | number | Yes | - |  |

---

### SizeDefinition `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | number | No | - | x-coordinate |
| `y` | number | No | - | y-coordinate |
| `width` | number | No | - | Width |
| `height` | number | No | - | Height |
| `scaleRatio` | object | No | - |  |
| `margin` | object | No | - |  |

<details>
<summary>Properties of `scaleRatio`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `x` | number | No | - | Scale ratio on x-axis |
| `y` | number | No | - | Scale ratio on y-axis |

</details>

<details>
<summary>Properties of `margin`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `left` | number | No | - | Left margin |
| `top` | number | No | - | Top margin |

</details>

---

### CanvasBufferSize `union`  **[experimental]**

An object containing width and height of the canvas buffer or a function returning an object on that format.
Gets a rect object as input parameter.

---

### Progressive() `function`  **[experimental]**

A function which returns either (1) false (to specify no progressive rendering used) or an object specifing the data chunk rendered.
 This is only applied to a canvas renderer.

#### Returns

[ProgressiveObject](#progressiveobject-object-experimental) | boolean

---

### TransformFunction() `function`  **[experimental]**

Should return a transform object if transformation should be applied, otherwise undefined or a falsy value.
Transforms can be applied with the canvas, svg and dom renderer.
Transform is applied when running chart.update, see example.
!Important: When a transform is applied to a component, the underlaying node representations are not updated with the new positions/sizes, which
can cause problems for operations that relies on the positioning of the shapes/nodes (such as tooltips, selections etc). An extra chart update
without a transform is therefore needed to make sure the node position information is in sync with the visual representation again.

#### Returns

[TransformObject](#transformobject-object)

<details>
<summary>Examples</summary>

```javascript
const pointComponentDef = {
  type: 'point',
  rendererSettings: {
    tranform() {
      if(shouldApplyTransform) {
        return {
          horizontalScaling: 1,
          horizontalSkewing: 0,
          verticalSkewing: 0,
          verticalScaling: 1,
          horizontalMoving: x,
          verticalMoving: y
        };
      }
    }
  }
  data: {
// ............

chart.update({ partialData: true });
```

</details>

---
