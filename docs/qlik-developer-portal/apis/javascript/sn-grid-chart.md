---
source: https://qlik.dev/apis/javascript/sn-grid-chart/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Grid chart

`Version: 2.14.0` | _stable_

Grid chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [byDimDef](#bydimdef-object)
- [byMeasureDef](#bymeasuredef-object)
- [paletteColor](#palettecolor-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `dataPoint` | object | Yes | - | Data point settings. |
| `footnote` | string \| StringExpression | Yes | "" | Visualization footnote. |
| `mode` | 'default' \| 'heatmap' | Yes | "default" | Chart mode. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `showDetails` | boolean | Yes | true | Show visualization details toggle |
| `showTitles` | boolean | No | true | Show title for the visualization |
| `subtitle` | string \| StringExpression | Yes | "" | Visualization subtitle. |
| `title` | string \| StringExpression | Yes | "" | Visualization title. |
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
| `dimensionScheme` | string | Yes | "12" | Color scheme when `"mode": "byDimension"` or `"mode": "byMultiple"` (`"12"` or `"100"` for most themes). |
| `expressionIsColor` | boolean | Yes | true | Set to define whether the result of the expression is a valid CSS3 color. Only applicable when `"mode": "byExpression"`. |
| `expressionLabel` | string | Yes | "" | Label to be defined on tool tips when using a coloring expression. Only used if `"expressionIsColor": false`. |
| `measureMax` | ValueExpression | No | "undefined" | Set the max value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureMin` | ValueExpression | No | "undefined" | Set the min value for the color range. Only applicable if `"autoMinMax": false`. |
| `measureScheme` | 'sg' \| 'sc' \| 'dg' \| 'dc' | Yes | "sg" | Color scheme when `"mode": "byMeasure"`. Can be one of: * `sg`: (sequential gradient) the transition between the different color groups is made using different shades of colors. High measure values have darker hues * `sc`: (sequential classes) the transition between the different color groups is made using distinctly different colors. * `dg`: (diverging gradient) used when working with data that is ordered from low to high, for instance, to show the relationship between different areas on a map. Low and high values have dark colors, mid-range colors are light. * `dc`: (diverging classes) can be seen as two sequential classes combined, with the mid-range shared. The two extremes, high and low, are emphasized with dark colors with contrasting hues, and the mid-range critical values are emphasized with light colors. |
| `mode` | 'primary' \| 'byDimension' \| 'byExpression' \| 'byMeasure' \| 'byMultiple' | Yes | "primary" | Sets the coloring mode for the visualization when auto-coloring has been switched off (`"auto": false`). Can be one of: * `primary`: a single color (by default blue) is used for all items in the chart. In visualizations that do not benefit from multiple colors (bar charts with one dimension and scatter plots), single color is the default setting. * `byDimension`: coloring is based upon the amount of dimension values. Details are set in the `"byDimDef"` property. !Note: `byDimension` can only be used in conjunction with an attribute dimension on the dimension to color by, as shown in the example below. ```json {     "qDef": {       "qFieldDefs": [         "NetScoreName"       ]     },     "qAttributeDimensions": [       {         "qDef": "NetScoreName",         "id": "colorByAlternative",         "label": "Year"       }     ] } ``` * `byExpression`: coloring is based on an expression, which in most cases is a color code. Details are set in the `"expressionIsColor"`, `"expressionLabel`" and `"colorExpression"` properties. * `byMeasure`: coloring is based on the measure value. Details are set in the `"byMeasureDef"` property. * `byMultiple`: can be used when more than one measure is used. By default, 12 colors are used for the dimensions. The colors are reused when there are more than 12 dimension values. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the color when you color by single color `("mode": "primary")`. |
| `reverseScheme` | boolean | Yes | false | Set to reverse the color scheme. |
| `singleColor` | number | Yes | - | _(deprecated)_ |
| `useBaseColors` | 'off' \| 'dimension' \| 'measure' | Yes | "off" | Use colors encoded in master items. Only applicable when `"mode": "primary"` or `"mode": "byMultiple"` has been defined. |
| `useDimColVal` | boolean | Yes | true | Set to true if you want to apply the colors defined for library dimensions when used. Only applicable if `'colorMode': 'byDimension'`. |
| `useMeasureGradient` | boolean | Yes | true | Set to true if you want to apply the colors defined for library measures when used. Only applicable if `"mode": "byMeasure"`. |

</details>

<details>
<summary>Properties of `dataPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rangeBubbleSizes` | array | Yes | "[0.1, 0.4]" | Symbol size setting. Can be a value between 0.1 and 1. |
| `showLabels` | 'auto' \| 'off' | Yes | "off" | Show labels for data points. |
| `symbol` | 'circle' \| 'cross' \| 'diamond' \| 'line' \| 'saltire' \| 'square' \| 'star' \| 'triangle' | Yes | "circle" | Symbol used for representation in grid. |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAlwaysFullyExpanded` | boolean | Yes | true |  |
| `qDimensions` | NxDimension[] | Yes | - |  |
| `qMeasures` | NxMeasure[] | Yes | - |  |
| `qMode` | string | Yes | "T" | Needs to be "T" in order for grid-chart to work properly |
| `qSuppressMissing` | boolean | Yes | true |  |
| `qSuppressZero` | boolean | Yes | false |  |

</details>

<details>
<summary>Properties of `xAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axisDisplayMode` | 'auto' \| 'custom' \| 'max' | Yes | "auto" | Set to specify axis display mode (number of items). |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `gridLines` | boolean | Yes | false | Vertical grid lines |
| `label` | 'auto' \| 'horizontal' \| 'tilted' | Yes | "auto" | Label orientation |
| `maxVisibleItems` | number \| ValueExpression | Yes | 10 | Only applied when axisDisplayMode is custom. Max is 55 for performance reasons. |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |

</details>

<details>
<summary>Properties of `yAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axisDisplayMode` | 'auto' \| 'custom' \| 'max' | Yes | "auto" | Set to specify axis display mode (number of items). |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `gridLines` | boolean | Yes | false | Horizontal grid lines |
| `maxVisibleItems` | number \| ValueExpression | Yes | 10 | Only applied when axisDisplayMode is custom. Max is 55 for performance reasons. |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |

</details>

---

## Definitions

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

### paletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---
