---
source: https://qlik.dev/apis/javascript/sn-scatter-plot/
last_updated: 2026-05-11T18:20:22+01:00
---

# Nebula Scatter plot

`Version: 3.60.1` | _stable_

Scatter plot generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [AttributeDimensionProperties](#attributedimensionproperties-object)
- [AttributeExpressionProperties](#attributeexpressionproperties-union)
- [axisStyle](#axisstyle-object)
- [byDimDef](#bydimdef-object)
- [byMeasureDef](#bymeasuredef-object)
- [ColorAttributes](#colorattributes-object)
- [CustomTooltipAttributes](#customtooltipattributes-object)
- [DimensionProperties](#dimensionproperties-object)
- [fontStyle](#fontstyle-object)
- [ImageComponent](#imagecomponent-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [labelNameStyle](#labelnamestyle-object)
- [labelStyle](#labelstyle-object)
- [legendStyle](#legendstyle-object)
- [MasterVisualizationChart](#mastervisualizationchart-object)
- [MasterVisualizationChartObject](#mastervisualizationchartobject-object)
- [MasterVisualizationChartStyle](#mastervisualizationchartstyle-object)
- [MeasureProperties](#measureproperties-object)
- [MediaLibraryRef](#medialibraryref-object)
- [paletteColor](#palettecolor-object)
- [referenceLineStyle](#referencelinestyle-object)
- [refLine](#refline-object)
- [refLineStyle](#reflinestyle-object)
- [scatterPlotStyle](#scatterplotstyle-object)
- [trendLine](#trendline-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `components` | [scatterPlotStyle](#scatterplotstyle-object)[] | Yes | - | Styling of chart components. |
| `dataPoint` | object | Yes | - | Data points settings. |
| `disableNavMenu` | boolean | Yes | false | Set to enable or disable navigation menu. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridLine` | object | Yes | - | Grid lines settings. |
| `labels` | object | Yes | "{\"mode\":1}" | Label mode settings. |
| `legend` | object | Yes | - | Legend settings. |
| `maxVisibleBubbles` | number | Yes | 2500 | Set the maximum number of visible bubbles for the chart. Max is 50000 and min is 1000. |
| `navigation` | boolean | Yes | false | Show navigation UI. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `refLine` | object | Yes | - | Reference lines settings |
| `showDetails` | boolean | No | false | Show visualization details toggle |
| `showDisclaimer` | boolean | Yes | true | Show visualization disclaimer toggle |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `tooltip` | object | Yes | - | Custom tooltip properties |
| `trendLines` | [trendLine](#trendline-object)[] | Yes | - | Array of trend lines |
| `version` | string | Yes | - | Current version of this generic object definition |
| `xAxis` | object | Yes | - | X-axis settings. |
| `yAxis` | object | Yes | - | Y-axis settings. |

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Set to use automatic coloring. When `"auto": true`, color settings are based on the visualization used and the number of dimensions and measures, that is, the settings are not fixed, but are dependent on the data input. |
| `autoMinMax` | boolean | Yes | true | Set to false to define custom color range. Custom color range is only applicable when coloring is by measure (`"mode": "byMeasure"`) or by expression (`"mode": "byExpression"`). When coloring is by expression, `"expressionIsColor": "false"` must be set for custom color range to work. |
| `byDimDef` | [byDimDef](#bydimdef-object) | No | "undefined" |  |
| `byMeasureDef` | [byMeasureDef](#bymeasuredef-object) | No | "undefined" |  |
| `colorExpression` | string | No | "undefined" | Sets the color expression to be used when `"mode": "byExpression"` is defined. Expression can evaluate either to a numerical value or a color code if `"expressionIsColor": true`. Supported formats are: `RGB`, `ARGB` and `HSL` |
| `dimensionScheme` | '12' \| '100' | Yes | "12" | Color scheme when `"mode": "byDimension"` or `"mode": "byMultiple"` (`"12"` or `"100"` for most themes). |
| `expressionIsColor` | boolean | Yes | true | Set to define whether the result of the expression is a valid CSS3 color. Only applicable when `"mode": "byExpression"`. |
| `expressionLabel` | string | Yes | "" | Label to be defined on tool tips when using a coloring expression. Only used if `'expressionIsColor': false`. |
| `formatting` | object | Yes | - | Color by measure number formatting options |
| `measureMax` | number \| ValueExpression | Yes | 10 | Set the max value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureMin` | number \| ValueExpression | Yes | 0 | Set the min value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureScheme` | 'sg' \| 'sc' \| 'dg' \| 'dc' | Yes | "sg" | Color scheme when `"mode": "byMeasure"`. Can be one of: * `sg`: (sequential gradient) the transition between the different color groups is made using different shades of colors. High measure values have darker hues * `sc`: (sequential classes) the transition between the different color groups is made using distinctly different colors. * `dg`: (diverging gradient) used when working with data that is ordered from low to high, for instance, to show the relationship between different areas on a map. Low and high values have dark colors, mid-range colors are light. * `dc`: (diverging classes) can be seen as two sequential classes combined, with the mid-range shared. The two extremes, high and low, are emphasized with dark colors with contrasting hues, and the mid-range critical values are emphasized with light colors. |
| `mode` | 'primary' \| 'byDimension' \| 'byExpression' \| 'byMeasure' \| 'byMultiple' | Yes | "primary" | Sets the coloring mode for the visualization when auto-coloring has been switched off (`"auto": false`). Can be one of: * `primary`: a single color (by default blue) is used for all items in the chart. In visualizations that do not benefit from multiple colors (bar charts with one dimension and scatter plots), single color is the default setting. * `byDimension`: coloring is based upon the amount of dimension values. Details are set in the `"byDimDef"` property. !Note: `byDimension` can only be used in conjunction with an attribute dimension on the dimension to color by, as shown in the example below. ```json {     "qDef": {       "qFieldDefs": [         "NetScoreName"       ]     },     "qAttributeDimensions": [       {         "qDef": "NetScoreName",         "id": "colorByAlternative",         "label": "Year"       }     ] } ``` * `byExpression`: coloring is based on an expression, which in most cases is a color code. Details are set in the `"expressionIsColor"`, `"expressionLabel`" and `"colorExpression"` properties. * `byMeasure`: coloring is based on the measure value. Details are set in the `"byMeasureDef"` property. * `byMultiple`: can be used when more than one measure is used. By default, 12 colors are used for the dimensions. The colors are reused when there are more than 12 dimension values. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the color when you color by single color `("mode": "primary")`. |
| `persistent` | boolean | Yes | false | Set to use persistent colors on data points between selections. Only applicable when using one dimension and when `"mode": "byDimension"` or when `"mode": "byMultiple"`. |
| `reverseScheme` | boolean | Yes | false | Set to reverse the color scheme. |
| `useBaseColors` | 'off' \| 'dimension' \| 'measure' | Yes | "off" | Use colors encoded in master items. Only applicable when `"mode": "primary"` or `"mode": "byMultiple"` has been defined. |
| `useDimColVal` | boolean | Yes | true | Set to true if you want to apply the colors defined for library dimensions when used. Only applicable if `'colorMode': 'byDimension'`. |
| `useMeasureGradient` | true | Yes | - | Set to true if you want to apply the colors defined for library measures when used. Only applicable if `"mode": "byMeasure"`. |

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `numFormatFromTemplate` | boolean | No | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |

</details>

</details>

<details>
<summary>Properties of `dataPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bubbleSizes` | number | Yes | 5 | Set bubble size when there is no measure for size. |
| `compressionResolution` | number | Yes | 5 | Resolution settings for compressed data. |
| `rangeBubbleSizes` | array | Yes | "5" | Bubble sizes. Represented as an array of two integers where the first index is the from-size and the second the to-size. From-size needs to be smaller. Only applicable when there is a third neasure. |

</details>

<details>
<summary>Properties of `gridLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Automatic grid line spacing. |
| `spacing` | 0 \| 1 \| 2 \| 3 | Yes | 2 | Grid line spacing. Used only when auto is set to false. |

</details>

<details>
<summary>Properties of `labels`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mode` | 0 \| 1 \| 2 | Yes | 1 | Show labels. 1 for auto, 2 for show all and 0 for hiding labels. |

</details>

<details>
<summary>Properties of `legend`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'auto' \| 'right' \| 'left' \| 'bottom' \| 'top' | Yes | "auto" | Sets the legend position. |
| `show` | boolean | Yes | true | Set to show the legend. |
| `showTitle` | boolean | Yes | true | Show the legend title. |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - |  |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressMissing` | boolean | Yes | true |  |

</details>

<details>
<summary>Properties of `refLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `refLinesX` | [refLine](#refline-object)[] | Yes | - | Array of x-axis reference line definitions |
| `refLinesY` | [refLine](#refline-object)[] | Yes | - | Array of y-axis reference line definitions |

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

<details>
<summary>Properties of `xAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoMinMax` | boolean | Yes | true | Automatic max/min |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `max` | number \| ValueExpression | Yes | 10 | Axis max value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"max"` or `"minMax"` to use this property |
| `min` | number \| ValueExpression | Yes | 0 | Axis min value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"min"` or `"minMax"` to use this property |
| `minMax` | 'min' \| 'max' \| 'minMax' | Yes | "min" | Set custom max/min |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |
| `spacing` | number | Yes | 1 | Axis scale |

</details>

<details>
<summary>Properties of `yAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoMinMax` | boolean | Yes | true | Automatic max/min |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `max` | number \| ValueExpression | Yes | 10 | Axis max value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"max"` or `"minMax"` to use this property |
| `min` | number \| ValueExpression | Yes | 0 | Axis min value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"min"` or `"minMax"` to use this property |
| `minMax` | 'min' \| 'max' \| 'minMax' | Yes | "min" | Set custom max/min |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |
| `spacing` | number | Yes | 1 | Axis scale |

</details>

---

## Definitions

### AttributeDimensionProperties `object`

extends `NxAttrDimDef`

Extends `NxAttrDimDef`, see Engine API: `NxAttrDimDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | One of: `colorByAlternative`: colors the chart using different dimensions (can be used together with color.mode="byDimension") or `colorByExpression` together with color.mode="byExpression". |

---

### AttributeExpressionProperties `union`

---

### axisStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [labelNameStyle](#labelnamestyle-object) | Yes | - |  |
| `title` | [fontStyle](#fontstyle-object) | Yes | - |  |

---

### byDimDef `object`

Settings when coloring by dimension (`"mode": "byDimension"`)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | libraryId if `"type": "libraryItem"`, dimension expression if `"type": "expression"` |
| `label` | string | Yes | - | Label displayed for coloring (in legend and tooltip for instance). String or expression. Not used when coloring by library items. |
| `type` | 'expression' \| 'libraryItem' | Yes | - |  |

---

### byMeasureDef `object`

Settings when coloring by measure (`"mode": "byMeasure"`)

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | libraryId if `"type": "libraryItem"`, measure expression if `"type": "expression"` |
| `label` | string | Yes | - | Label displayed for coloring (in legend and tooltip for instance). String or expression. Not used when coloring by library items. |
| `type` | 'expression' \| 'libraryItem' | Yes | - |  |

---

### ColorAttributes `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | One of: `colorByAlternative`: colors the chart using different dimensions (can be used together with color.mode="byDimension") or `colorByExpression` together with color.mode="byExpression". |

---

### CustomTooltipAttributes `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | 'customTooltipTitle' \| 'customTooltipDescription' \| 'customTooltipExpression' \| 'customTooltipImages' | Yes | - | Indicates how the attribute expression will be interpreted by the chart. `customTooltipTitle`: additional title displayed on the custom tooltip `customTooltipDescription`: description displayed on the custom tooltip `customTooltipExpression`: measures displayed on the custom tooltip |

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
| `qAttributeDimensions` | [AttributeDimensionProperties](#attributedimensionproperties-object)[] | Yes | - |  |
| `qDef` | [InlineDimensionDef](#inlinedimensiondef-object) | Yes | - |  |

---

### fontStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `fontFamily` | string | Yes | - |  |
| `fontSize` | string | Yes | - |  |

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
| `isCustomFormatted` | boolean | Yes | - | Set to true to toggle off the default client formatting. |
| `numFormatFromTemplate` | boolean | Yes | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |
| `othersLabel` | string \| StringExpression | Yes | - |  |
| `autoSort` | boolean | No | - | Set to automatically sort the measure. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |

---

### labelNameStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | [fontStyle](#fontstyle-object) | Yes | - |  |

---

### labelStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | [fontStyle](#fontstyle-object) | Yes | - |  |

---

### legendStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [fontStyle](#fontstyle-object) | Yes | - |  |
| `title` | [fontStyle](#fontstyle-object) | Yes | - |  |

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

### referenceLineStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [labelNameStyle](#labelnamestyle-object) | Yes | - |  |

---

### refLine `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | Yes | - | Reference line label. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `refLineExpr` | object | Yes | - |  |
| `show` | boolean \| ValueExpression | Yes | true | Set to true to display this reference line. |
| `coloredBackground` | boolean | No | false | Set to true to fill the label and/or value of this reference line with this color |
| `showLabel` | boolean | No | true | Set to true to show the label of this reference line. |
| `showValue` | boolean | No | true | Set to true to show the value of this reference line. |
| `style` | [refLineStyle](#reflinestyle-object) | No | - | Styling settings for reference line |

<details>
<summary>Properties of `refLineExpr`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | number \| ValueExpression | Yes | - |  |
| `label` | string \| StringExpression | No | - |  |

</details>

---

### refLineStyle `object`

Styling settings for reference line

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lineThickness` | number | No | 2 | Set the thickness for this reference line. |
| `lineType` | string | No | "" | Set the dash type for this reference line. |

---

### scatterPlotStyle `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axis` | [axisStyle](#axisstyle-object) | Yes | - |  |
| `key` | string | Yes | - | Determines which component the settings apply to. |
| `label` | [labelStyle](#labelstyle-object) | Yes | - |  |
| `legendStyle` | [legendStyle](#legendstyle-object) | Yes | - |  |
| `referenceLine` | [referenceLineStyle](#referencelinestyle-object) | Yes | - |  |

---

### trendLine `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `flipXY` | boolean | Yes | false | Set to true if the first measure should be the dependent variable |
| `label` | string | Yes | - | Trend line label |
| `qMultiDimMode` | string | Yes | "Sum" | Not applicable for scatter plot since it has only one dimension |
| `qType` | string | Yes | - | Trend line type, for example LINEAR or EXPONENTIAL |
| `qXColIx` | number | Yes | - | The column in the hypercube to be used as x axis. Related to flipXY. |
| `style` | object | Yes | - |  |

<details>
<summary>Properties of `style`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoColor` | boolean | Yes | true |  |
| `dashed` | boolean | Yes | true |  |
| `lineDash` | string | Yes | - | Represents the lengths of the dashes and the breaks |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |

</details>

---
