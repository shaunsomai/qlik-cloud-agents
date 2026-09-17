---
source: https://qlik.dev/apis/javascript/sn-bullet-chart/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Bullet chart

`Version: 2.14.0` | _stable_

Bullet chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [AttributeExpressionProperties](#attributeexpressionproperties-union)
- [AttributeExpressions](#attributeexpressions-object)
- [conditionalColoringProperties](#conditionalcoloringproperties-object)
- [CustomTooltipAttributes](#customtooltipattributes-object)
- [DimensionProperties](#dimensionproperties-object)
- [ImageComponent](#imagecomponent-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [limitsProperties](#limitsproperties-object)
- [MasterVisualizationChart](#mastervisualizationchart-object)
- [MasterVisualizationChartObject](#mastervisualizationchartobject-object)
- [MasterVisualizationChartStyle](#mastervisualizationchartstyle-object)
- [MeasureProperties](#measureproperties-object)
- [MediaLibraryRef](#medialibraryref-object)
- [paletteColor](#palettecolor-object)
- [paletteColorsProperties](#palettecolorsproperties-object)
- [properties.dataPoint.showLabels](#propertiesdatapointshowlabels)
- [properties.dataPoint.showSegmentLabels](#propertiesdatapointshowsegmentlabels)
- [properties.dataPoint.showTotalLabels](#propertiesdatapointshowtotallabels)
- [qStaticContentUrlDef](#qstaticcontenturldef-object)
- [segmentsProperties](#segmentsproperties-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridLine` | object | Yes | - | Grid lines settings. Used only when using commom axis. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `orientation` | 'vertical' \| 'horizontal' | Yes | "vertical" | Orientation setting. If vertical, the dimension axis can only be docked on bottom or top and measure axis on left or right. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `scrollbar` | 'bar' \| 'none' | Yes | "bar" | Sets the style of the scroll bar |
| `scrollStartPos` | number | Yes | 0 | Scroll Alignment. If 0, then the scrollbar will start at the left/top of the chart, if 1 it starts at the right/bottom of the chart. Generally decides if the scroll starts at the beginning or end of the data |
| `showDetails` | boolean | No | true | Show visualization details toggle |
| `showTitles` | boolean | No | true | Show title for the visualization |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `tooltip` | object | Yes | - | Custom tooltip properties |
| `version` | string | Yes | - | Current version of this generic object definition |

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Set to use automatic coloring. When `"auto": true`, color settings are based on the visualization used. |
| `bar` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the color of bar. |
| `mode` | primary | Yes | - | `primary`: a single color (by default blue) for all bar items and (by default black) for all target items in the bullet chart. |
| `target` | [paletteColor](#palettecolor-object) | Yes | "{ index: -1, color: '#000000' }" | The target object is used to define the color of target. |

</details>

<details>
<summary>Properties of `dimensionAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `label` | 'auto' \| 'horizontal' \| 'tilted' | Yes | "auto" | Label orientation |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |

</details>

<details>
<summary>Properties of `gridLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Automatic grid line spacing. |
| `spacing` | 0 \| 1 \| 2 \| 3 | Yes | 2 | Grid line spacing. Used only when auto is set to false. |

</details>

<details>
<summary>Properties of `measureAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `commonAxis` | boolean | Yes | false | When set to true, use common axis. |
| `commonRange` | boolean | Yes | false | When set to true, use common range. |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |
| `spacing` | number | Yes | 1 | Axis scale |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - |  |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressMissing` | boolean | Yes | true |  |
| `qSuppressZero` | boolean | Yes | false |  |

</details>

<details>
<summary>Properties of `tooltip`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Toggle for using custom tooltip or regular tooltip |
| `chart` | [MasterVisualizationChart](#mastervisualizationchart-object) | Yes | "undefined" | The chart object is used to define the chart displayed by the custom tooltip. |
| `description` | string \| StringExpression | No | "" | Custom tooltip description. |
| `hideBasic` | boolean | Yes | false | Toggle for hiding basic information from custom tooltip |
| `imageComponents` | [ImageComponent](#imagecomponent-object)[] | Yes | "undefined" | The imageComponents objects are used to define the images displayed by the custom tooltip. |
| `title` | string \| StringExpression | No | "" | Custom tooltip title. |

</details>

---

## Definitions

### AttributeExpressionProperties `union`

---

### AttributeExpressions `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | If set to `"bullet-target"` the expression will be interpreted as the target for the specific measure. If set to `"bullet-segment"` the expression will be interpreted as a segment limit. |

<details>
<summary>Examples</summary>

```json
"qAttributeExpressions": [{
  "qExpression": "Avg(Sales)",
  "qLibraryId: "",
  "qAttribute: true,
  "id": "bullet-target"
},
{
  "qExpression: "Avg(Sales)/2",
  "qLibraryId: "",
  "qAttribute: true,
  "id: "bullet-segment"
}]
```

</details>

---

### conditionalColoringProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `segments` | [segmentsProperties](#segmentsproperties-object) | Yes | - |  |

<details>
<summary>Examples</summary>

```json
"segments": {
  "limits": [
    {
      "gradient": false
    }
  ],
  "paletteColors": [
    {
      "color": "#bfbfbf",
      "index": -1
    },
    {
      "color": "#a5a5a5",
      "index": -1
    }
  ]
}
```

</details>

---

### CustomTooltipAttributes `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | 'customTooltipTitle' \| 'customTooltipDescription' \| 'customTooltipExpression' | Yes | - | Indicates how the attribute expression will be interpreted by the chart. `customTooltipTitle`: additional title displayed on the custom tooltip `customTooltipDescription`: description displayed on the custom tooltip `customTooltipExpression`: measures displayed on the custom tooltip |

<details>
<summary>Examples</summary>

```json
"qAttributeExpressions": [{
  "qExpression": "",
  "qLibraryId": "",
  "qAttribute": true,
  "qNumFormat": {
     "qType": "U",
     "qnDec": 10,
     "qUseThou": 0,
     "qFmt": "",
     "qDec": "",
     "qThou": "",
   }
  "qLabel": "custom title",
  "qLabelExpression": "",
  "id": "customTooltipTitle"
},
{
  "qExpression": "avg(population)",
  "qLibraryId": "",
  "qAttribute": true,
  "qNumFormat": {
     "qType": "U",
     "qnDec": 10,
     "qUseThou": 0,
     "qFmt": "",
     "qDec": "",
     "qThou": "",
   }
  "qLabel": "",
  "qLabelExpression": "",
  "id": "customTooltipDescription"
},
{
  "qExpression": "",
  "qLibraryId": "zpDNMcg",
  "qAttribute": true,
  "qNumFormat": {
     "qType": "U",
     "qnDec": 10,
     "qUseThou": 0,
     "qFmt": "",
     "qDec": "",
     "qThou": "",
   }
  "qLabel": "",
  "qLabelExpression": "",
  "id": "customTooltipExpression"
},
{
  "qExpression": "sum(population)",
  "qLibraryId": "",
  "qAttribute": true,
  "qNumFormat": {
     "qType": "M",
     "qnDec": 2,
     "qUseThou": 0,
     "qFmt": "$#,##0.00;-$#,##0.00",
     "qDec": ".",
     "qThou": ",",
   }
  "qLabel": "",
  "qLabelExpression": "=avg(population)",
  "id": "customTooltipExpression"
},
{
  "qExpression": "'https://my_url/'+sum(population)",
  "qLibraryId": "",
  "qAttribute": true,
  "qNumFormat": null,
  "qLabel": "",
  "qLabelExpression": "",
  "cId": "generatedUniqueId",
  "id": "customTooltipImages"
}]
```

</details>

---

### DimensionProperties `object`

extends `NxDimension`

Extends `NxDimension`, see Engine API: `NxDimension`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDef` | [InlineDimensionDef](#inlinedimensiondef-object) | Yes | - |  |

---

### ImageComponent `object`

Image component information structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cId` | string | Yes | - | Identifier of the image component - used as a link with an attribute expression |
| `ref` | string \| StringExpression \| [MediaLibraryRef](#medialibraryref-object) | Yes | - | The reference value of the image |
| `size` | string | Yes | - | Size as 'small','medium','large' or 'original' |
| `type` | string | Yes | - | Input type as 'url' or 'media library' |

---

### InlineDimensionDef `object`

extends `NxInlineDimensionDef`

Extends `NxInlineDimensionDef`, see Engine API: `NxInlineDimensionDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `othersLabel` | string \| StringExpression | Yes | - |  |
| `autoSort` | boolean | No | - | Set to automatically sort the dimension. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |

---

### InlineMeasureDef `object`

extends `NxInlineMeasureDef`

Extends `NxInlineMeasureDef`, see Engine API: `NxInlineMeasureDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoMinMax` | boolean | Yes | - | Default false. Set to true to custmize the ranges of measure. |
| `conditionalColoring` | [conditionalColoringProperties](#conditionalcoloringproperties-object) | Yes | - | Information of how the segments |
| `isCustomFormatted` | boolean | Yes | - | Set to true to toggle off the default client formatting. |
| `max` | number \| ValueExpression | Yes | - | Set the max value of the range. |
| `min` | string | Yes | - | Set the min value of the range. |
| `minMax` | string | Yes | - | Set custom max/min. Default "min". Supported type are: 'min'\|'max'\|'minMax'. |
| `numFormatFromTemplate` | boolean | Yes | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |
| `othersLabel` | string \| StringExpression | Yes | - |  |
| `useSegments` | boolean | Yes | - | Default false. Set to true to customize segment colors. |
| `autoSort` | boolean | No | - | Set to automatically sort the measure. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |

---

### limitsProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `gradient` | boolean | No | - | Set gradient of the color. |

---

### MasterVisualizationChart `object`

Chart component information structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `object` | [MasterVisualizationChartObject](#mastervisualizationchartobject-object) | Yes | - | Object containing the information fo the visualization, such as refId in case of master visualization |
| `style` | [MasterVisualizationChartStyle](#mastervisualizationchartstyle-object) | Yes | - | Object containing the styles of the chart such as 'size' |

---

### MasterVisualizationChartObject `object`

Chart component information structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `refId` | string | Yes | - | Input field containing the qExtendsId of the visualization, where qExtendsId is the unique id of the master visualization |

---

### MasterVisualizationChartStyle `object`

Chart component information structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `size` | string | Yes | - | Input type as 'small' or 'medium' or 'large' |

---

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAttributeExpressions` | [AttributeExpressionProperties](#attributeexpressionproperties-union)[] | Yes | - |  |
| `qDef` | [InlineMeasureDef](#inlinemeasuredef-object) | Yes | - |  |

---

### MediaLibraryRef `object`

Media Library Reference structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStaticContentUrlDef` | object | Yes | - | Media library structure |

---

### paletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---

### paletteColorsProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |

---

### properties.dataPoint.showLabels

Show labels on data points

---

### properties.dataPoint.showSegmentLabels

Show segment labels

---

### properties.dataPoint.showTotalLabels

Show total labels

---

### qStaticContentUrlDef `object`

Media Library structure that will be evaluated by the engine.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | Yes | - | Value of media library image |

---

### segmentsProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `limits` | [limitsProperties](#limitsproperties-object)[] | Yes | - |  |
| `paletteColors` | [paletteColorsProperties](#palettecolorsproperties-object)[] | Yes | - |  |

---
