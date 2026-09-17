---
source: https://qlik.dev/apis/javascript/sn-line-chart/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Line chart

`Version: 2.14.0` | _stable_

Line chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [Accumulation](#accumulation-object)
- [AttributeDimensionProperties](#attributedimensionproperties-object)
- [AttributeExpressionProperties](#attributeexpressionproperties-union)
- [Axis](#axis-object)
- [AxisStyling](#axisstyling-object)
- [byDimDef](#bydimdef-object)
- [byMeasureDef](#bymeasuredef-object)
- [ColorAttributes](#colorattributes-object)
- [Component](#component-union)
- [CustomTooltipAttributes](#customtooltipattributes-object)
- [Difference](#difference-object)
- [DimensionForecast](#dimensionforecast-object)
- [DimensionProperties](#dimensionproperties-object)
- [dimRefLine](#dimrefline-object)
- [FontStyling](#fontstyling-object)
- [ForecastAttributes](#forecastattributes-object)
- [ImageComponent](#imagecomponent-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [Label](#label-object)
- [LabelNameStyling](#labelnamestyling-object)
- [LabelValueStyling](#labelvaluestyling-object)
- [Legend](#legend-object)
- [LegendStyling](#legendstyling-object)
- [Line](#line-object)
- [LineStyling](#linestyling-object)
- [MasterVisualizationChart](#mastervisualizationchart-object)
- [MasterVisualizationChartObject](#mastervisualizationchartobject-object)
- [MasterVisualizationChartStyle](#mastervisualizationchartstyle-object)
- [MeasureForecast](#measureforecast-object)
- [MeasureProperties](#measureproperties-object)
- [MediaLibraryRef](#medialibraryref-object)
- [Modifier](#modifier-union)
- [MovingAverage](#movingaverage-object)
- [paletteColor](#palettecolor-object)
- [qStaticContentUrlDef](#qstaticcontenturldef-object)
- [refLine](#refline-object)
- [refLineStyle](#reflinestyle-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `components` | [Component](#component-union)[] | Yes | - | Styling of chart components. |
| `dataPoint` | object | Yes | - | Data point settings. |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridLine` | object | Yes | - | Grid lines settings. |
| `legend` | object | Yes | - | Legend settings. |
| `lineType` | 'line' \| 'area' | Yes | "line" | Type of line chart. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `nullMode` | 'gap' \| 'connect' \| 'zero' | No | "gap" | Null value presentation |
| `orientation` | 'vertical' \| 'horizontal' | Yes | "horizontal" | Orientation setting. If horizontal, the dimension axis can only be docked on bottom or top and measure axis on left or right. |
| `preferContinuousAxis` | boolean | Yes | true | Chart axis setting to control preference of scale on a dimensional axis. If true, the scale along the dimensional axis will be continuous if the data supports it, discrete otherwise. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `refLine` | object | Yes | - | Reference lines settings |
| `scrollbar` | 'bar' \| 'miniChart' \| 'none' | Yes | "miniChart" | Sets the style of the scroll bar |
| `scrollStartPos` | number | Yes | 0 | Scroll Alignment. If 0, then the scrollbar will start at the left/top of the chart, if 1 it starts at the right/bottom of the chart. Generally decides if the scroll starts at the beginning or end of the data |
| `separateStacking` | boolean | Yes | true | Stack positive and negative values separately. Dependent of lineType property. |
| `showDetails` | boolean | No | true | Show visualization details toggle |
| `showDisclaimer` | boolean | Yes | true | Show visualization disclaimer toggle |
| `showMiniChartForContinuousAxis` | boolean | Yes | true | Chart axis setting to turn on/off the mini chart for continuous axis. |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `stackedArea` | boolean | Yes | false | Stack areas. Dependent of lineType property. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `tooltip` | object | Yes | - | Custom tooltip properties |
| `version` | string | Yes | - | Current version of this generic object definition |

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
| `measureMax` | ValueExpression | No | "undefined" | Set the max value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureMin` | ValueExpression | No | "undefined" | Set the min value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureScheme` | 'sg' \| 'sc' \| 'dg' \| 'dc' | Yes | "sg" | Color scheme when `"mode": "byMeasure"`. Can be one of: * `sg`: (sequential gradient) the transition between the different color groups is made using different shades of colors. High measure values have darker hues * `sc`: (sequential classes) the transition between the different color groups is made using distinctly different colors. * `dg`: (diverging gradient) used when working with data that is ordered from low to high, for instance, to show the relationship between different areas on a map. Low and high values have dark colors, mid-range colors are light. * `dc`: (diverging classes) can be seen as two sequential classes combined, with the mid-range shared. The two extremes, high and low, are emphasized with dark colors with contrasting hues, and the mid-range critical values are emphasized with light colors. |
| `mode` | 'primary' \| 'byDimension' \| 'byExpression' \| 'byMeasure' \| 'byMultiple' | Yes | "primary" | Sets the coloring mode for the visualization when auto-coloring has been switched off (`"auto": false`). Can be one of: * `primary`: a single color (by default blue) is used for all items in the chart. In visualizations that do not benefit from multiple colors (bar charts with one dimension and scatter plots), single color is the default setting. * `byDimension`: coloring is based upon the amount of dimension values. Details are set in the `"byDimDef"` property. !Note: `byDimension` can only be used in conjunction with an attribute dimension on the dimension to color by, as shown in the example below. ```json {     "qDef": {       "qFieldDefs": [         "NetScoreName"       ]     },     "qAttributeDimensions": [       {         "qDef": "NetScoreName",         "id": "colorByAlternative",         "label": "Year"       }     ] } ``` * `byExpression`: coloring is based on an expression, which in most cases is a color code. Details are set in the `"expressionIsColor"`, `"expressionLabel`" and `"colorExpression"` properties. * `byMeasure`: coloring is based on the measure value. Details are set in the `"byMeasureDef"` property. * `byMultiple`: can be used when more than one measure is used. By default, 12 colors are used for the dimensions. The colors are reused when there are more than 12 dimension values. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the color when you color by single color `("mode": "primary")`. |
| `persistent` | boolean | Yes | false | Set to use persistent colors on data points between selections. Only applicable when using one dimension and when `"mode": "byDimension"` or when `"mode": "byMultiple"`. |
| `reverseScheme` | boolean | Yes | false | Set to reverse the color scheme. |
| `singleColor` | number | Yes | - | _(deprecated)_ |
| `useBaseColors` | 'off' \| 'dimension' \| 'measure' | Yes | "off" | Use colors encoded in master items. Only applicable when `"mode": "primary"` or `"mode": "byMultiple"` has been defined. |
| `useDimColVal` | boolean | Yes | true | Set to true if you want to apply the colors defined for library dimensions when used. Only applicable if `'colorMode': 'byDimension'`. |
| `useMeasureGradient` | boolean | Yes | true | Set to true if you want to apply the colors defined for library measures when used. Only applicable if `"mode": "byMeasure"`. |

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isCustomFormatted` | boolean | No | false | If true, the client formatting will be toggled off |
| `numFormatFromTemplate` | boolean | No | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |

</details>

</details>

<details>
<summary>Properties of `dataPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | Yes | false | Show data points. |
| `showLabels` | boolean | Yes | false | Show labels on data points. |

</details>

<details>
<summary>Properties of `dimensionAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axisDisplayMode` | 'auto' \| 'custom' \| 'max' | Yes | "auto" | Set to specify axis display mode (number of axis values). |
| `continuousAuto` | boolean | Yes | true | Continuous setting used for toggling between auto and custom setting |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `label` | 'auto' \| 'horizontal' \| 'tilted' | Yes | "auto" | Label orientation |
| `maxVisibleItems` | number \| ValueExpression | Yes | 10 | Only visible when axisDisplayMode is custom. Max = 10000 / (numDims+numMeasures) |
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
<summary>Properties of `legend`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'auto' \| 'right' \| 'left' \| 'bottom' \| 'top' | Yes | "auto" | Sets the legend position. |
| `show` | boolean | Yes | true | Set to show the legend. |
| `showTitle` | boolean | Yes | true | Show the legend title. |

</details>

<details>
<summary>Properties of `measureAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoMinMax` | boolean | Yes | true | Automatic max/min |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `logarithmic` | boolean | Yes | false | Logarithmic scale |
| `max` | number \| ValueExpression | Yes | 10 | Axis max value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"max"` or `"minMax"` to use this property |
| `min` | number \| ValueExpression | Yes | 0 | Axis min value. `"autoMinMax"` must be set to false and `"minMax"` must be set to `"min"` or `"minMax"` to use this property |
| `minMax` | 'min' \| 'max' \| 'minMax' | Yes | "min" | Set custom max/min |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |
| `spacing` | number | Yes | 1 | Axis scale |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAlwaysFullyExpanded` | boolean | Yes | true |  |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - |  |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressMissing` | boolean | Yes | true |  |
| `qSuppressZero` | boolean | Yes | false |  |

</details>

<details>
<summary>Properties of `refLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dimRefLines` | [dimRefLine](#dimrefline-object)[] | Yes | - | Array of dimension based reference line definitions |
| `refLines` | [refLine](#refline-object)[] | Yes | - | Array of measure based reference line definitions |

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

### Accumulation `object`

It allows you to accumulate values of your measure over one or two dimensions.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fullAccumulation` | boolean | Yes | - | Select whether the accumulation will happen on the Full range or Custom range. |
| `showExcludedValues` | boolean | Yes | - | Shows the excluded values (values not in the current selection) in the accumulation. |
| `type` | string | Yes | - | This should be set to `"accumulation"`. |
| `accumulationDimension:` | number | No | - | Only applicable when there are two dimensions. Selects the dimension on which the accumulation will take place. If the accumulation is made across multiple dimensions, this will be the first dimension. |
| `crossAllDimensions` | boolean | No | - | Only applicable when there are two dimensions. Continues accumulation across both dimensions. |
| `disabled` | boolean | No | - |  |
| `steps` | number | No | - | Only applicable when `fullAccumulation` is set to `false`. The number of steps in the dimensions which form an accumulation range. Only zero and positive integers are accepted. Note: Sorting order of dimension values (or step order) is important and affects results. |

---

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

### Axis `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axis` | [AxisStyling](#axisstyling-object) | Yes | - |  |
| `key` | string | Yes | - | This should be set to `"axis"` (Determines which component the settings apply to). |

---

### AxisStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [LabelNameStyling](#labelnamestyling-object) | Yes | - |  |
| `title` | [FontStyling](#fontstyling-object) | Yes | - |  |

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

### Component `union`

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

### Difference `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `showExcludedValues` | boolean | Yes | - | Shows the excluded values (values not in the current selection) in the difference. |
| `type` | string | Yes | - | This should be set to `"difference"`. |
| `accumulationDimension:` | number | No | - | Only applicable when there are two dimensions. Selects the dimension on which the difference will take place. If the difference is made across multiple dimensions, this will be the first dimension. |
| `crossAllDimensions` | boolean | No | - | Only applicable when there are two dimensions. Continues the difference across both dimensions. |
| `disabled` | boolean | No | - |  |

---

### DimensionForecast `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `steps` | number | Yes | 3 | Number of forecast steps |
| `stepSize` | number | Yes | "days" |  |
| `stepSizeMultiplier` | number | Yes | 1 |  |

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

### dimRefLine `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | Yes | - | Reference line label. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `refLineExpr` | object | Yes | - |  |
| `show` | boolean \| ValueExpression | Yes | true | Set to true to display this reference line. |
| `align` | 'start' \| 'center' \| 'end' | No | "center" | Set alignment for this reference line |
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
| `stringValue` | string \| StringExpression | Yes | - |  |

</details>

---

### FontStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `fontFamily` | string | Yes | - |  |
| `fontSize` | string | Yes | - |  |

---

### ForecastAttributes `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | 'forecast' \| 'forecast_lower' \| 'forecast_lower' | Yes | - | Indicates how the attribute expression will be interpreted by the chart. `forecast`: forecast line `forecast_lower`: lower edge of forecast confidence interval `forecast_upper`: upper edge of forecast confidence interval |

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
| `forecast` | [DimensionForecast](#dimensionforecast-object) | Yes | - |  |
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
| `forecast` | [MeasureForecast](#measureforecast-object) | Yes | - |  |
| `isCustomFormatted` | boolean | Yes | - | Set to true to toggle off the default client formatting. |
| `numFormatFromTemplate` | boolean | Yes | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |
| `othersLabel` | string \| StringExpression | Yes | - |  |
| `autoSort` | boolean | No | - | Set to automatically sort the measure. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |
| `modifiers` | [Modifier](#modifier-union)[] | No | - | Set to apply a modifier to a measure. |
| `style` | [LineStyling](#linestyling-object) | No | - | Can be used to change the line thickness, line type, and line curve for one of the lines. These style settings will override the components styling settings. |

---

### Label `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `"label"` (Determines which component the settings apply to). |
| `label` | [LabelValueStyling](#labelvaluestyling-object) | Yes | - |  |

---

### LabelNameStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | [FontStyling](#fontstyling-object) | Yes | - |  |

---

### LabelValueStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | [FontStyling](#fontstyling-object) | Yes | - | Data points labels |

---

### Legend `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `"legend"` (Determines which component the settings apply to). |
| `legend` | [LegendStyling](#legendstyling-object) | Yes | - |  |

---

### LegendStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [LabelNameStyling](#labelnamestyling-object) | Yes | - |  |
| `title` | [FontStyling](#fontstyling-object) | Yes | - |  |

---

### Line `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `"line"` (Determines which component the settings apply to). |
| `style` | [LineStyling](#linestyling-object) | Yes | - |  |

---

### LineStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dataPointSize` | number | Yes | 6 | Set to specify the size of the data point. |
| `lineCurve` | 'linear' \| 'monotone' | Yes | "linear" |  |
| `lineThickness` | number | Yes | 1 | Set to specify line thickness. Can be set from 1 to 5. |
| `lineType` | 'solid' \| 'dashed' | Yes | "solid" |  |

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

### MeasureForecast `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `confidence` | number | Yes | 0.95 | Only relevant when method is 'SSA' and showConfidence is true. should be between 0 and 1 (exclusive) |
| `enabled` | boolean | Yes | false |  |
| `lineCurve` | 'linear' \| 'monotone' | Yes | "linear" |  |
| `lineThickness` | number | Yes | 1 | Set to specify line thickness. Can be set from 1 to 5. |
| `lineType` | 'solid' \| 'dashed' | Yes | "dashed" |  |
| `method` | 'ssa_forecast' \| 'ols_forecast' | Yes | "ssa_forecast" | Forecast method |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `showConfidence` | boolean | Yes | true | Only used when method is 'SSA' |

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

### Modifier `union`

---

### MovingAverage `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fullRange` | boolean | Yes | - | Select whether the moving average will happen on the Full range or Custom range. |
| `nullSuppression` | boolean | Yes | - | Choose to have null values calculated by the moving average modifier. |
| `showExcludedValues` | boolean | Yes | - | Shows the excluded values (values not in the current selection) in the moving average. |
| `type` | string | Yes | - | This should be set to `"movingAverage"`. |
| `accumulationDimension:` | number | No | - | Only applicable when there are two dimensions. Selects the dimension on which the moving average will take place. If the moving average is made across multiple dimensions, this will be the first dimension. |
| `crossAllDimensions` | boolean | No | - | Only applicable when there are two dimensions. Continues the moving average across both dimensions. |
| `disabled` | boolean | No | - |  |
| `steps` | number | No | - | Only applicable when `fullRange` is set to `false`. The number of steps in the dimension which form a moving average. Only zero and positive integers are accepted. Note: Sorting order of dimension values (or step order) is important and affects results. |

---

### paletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---

### qStaticContentUrlDef `object`

Media Library structure that will be evaluated by the engine.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | Yes | - | Value of media library image |

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
