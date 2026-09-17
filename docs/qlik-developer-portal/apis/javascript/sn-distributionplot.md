---
source: https://qlik.dev/apis/javascript/sn-distributionplot/
last_updated: 2026-01-19T15:48:02Z
---

# Nebula Distribution plot chart

`Version: 1.0.6` | _experimental_

Distributionplot generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [paletteColor](#palettecolor-object)
- [properties.dataPoint.bubbleScales](#propertiesdatapointbubblescales)
- [properties.dataPoint.displacement](#propertiesdatapointdisplacement-union)
- [refLine](#refline-object)
- [refLineStyle](#reflinestyle-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridlines` | object | Yes | - | Grid lines settings. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `orientation` | 'vertical' \| 'horizontal' | Yes | "horizontal" | Orientation setting. If vertical, the dimension axis can only be docked on bottom or top and measure axis on left or right. |
| `presentation` | object | Yes | - | Presentation settings for the distributionplot |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `refLine` | object | Yes | - | Reference lines settings |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `sorting` | object | Yes | - | Wrapper for sorting properties which will be set on the outer dimension. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition. |

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `box` | object | Yes | - |  |
| `expressionLabel` | string | Yes | "" | Label to be defined on tool tips when using a coloring expression. Only used if `'expressionIsColor': false`. |
| `point` | object | Yes | - |  |

<details>
<summary>Properties of `box`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: -1, color: '#e6e6e6' }" | The paletteColor object is used to define the box color when you color by single color `("mode": "primary")`. |

</details>

<details>
<summary>Properties of `point`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Set to use automatic coloring. When `"auto": true`, color settings are based on the visualization used and the number of dimensions and measures, that is, the settings are not fixed, but are dependent on the data input. |
| `expressionIsColor` | true | Yes | - | Should be true |
| `mode` | 'primary' \| 'byExpression' \| 'byMultiple' | Yes | "primary" | Sets the coloring mode for the visualization when auto-coloring has been switched off (`"auto": false`). Can be one of: * `primary`: a single color (by default blue) is used for all items in the chart. In visualizations that do not benefit from multiple colors (bar charts with one dimension and scatter plots), single color is the default setting. * `byExpression`: coloring is based on an expression, which in most cases is a color code. Details are set in the `"expressionIsColor"`, `"expressionLabel`" and `"colorExpression"` properties. * `byMultiple`: can be used when more than one measure is used. By default, 12 colors are used for the dimensions. The colors are reused when there are more than 12 dimension values. |
| `useBaseColors` | 'off' \| 'dimension' \| 'measure' | Yes | "off" | Use colors encoded in master items. Only applicable when `"mode": "primary"` has been defined. |

</details>

</details>

<details>
<summary>Properties of `dimensionAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `label` | 'auto' | Yes | - | Label orientation |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |

</details>

<details>
<summary>Properties of `gridlines`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Automatic grid line spacing. |
| `spacing` | 0 \| 2 \| 3 | Yes | 2 | Grid line spacing. Used only when auto is set to false. |

</details>

<details>
<summary>Properties of `measureAxis`</summary>

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
<summary>Properties of `presentation`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `visibleComponents` | 'points_box' \| 'points' \| 'box' | Yes | "points_box" | Visible components of the distributionplot |

</details>

<details>
<summary>Properties of `refLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `refLines` | [refLine](#refline-object)[] | Yes | - | Array of measure based reference line definitions |

</details>

<details>
<summary>Properties of `sorting`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoSort` | boolean | Yes | true | Sort automatically |
| `elementId` | 'distplot-exp-min' \| 'distplot-exp-max' | Yes | "distplot-exp-min" | Sorting preset |
| `expression` | ValueExpression | Yes | - | Expression for the sorting. Requires sortByExpression to be -1 or 1. |
| `sortCriteria` | object | Yes | - |  |

<details>
<summary>Properties of `sortCriteria`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sortByAscii` | number | Yes | 0 | Sort by alphabetic |
| `sortByExpression` | number | Yes | 0 | Sort by expression |
| `sortByNumeric` | number | Yes | 0 | Sort by numeric |
| `sortByLoadOrder` | number | Yes | 0 | Sort by load order |

</details>

</details>

---

## Definitions

### paletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---

### properties.dataPoint.bubbleScales

Size parameter for points (20 - 100), step is 5.

---

### properties.dataPoint.displacement `union`

Property for controlling displacement of data points

---

### refLine `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | Yes | - | Reference line label. |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | - |  |
| `show` | boolean \| ValueExpression | Yes | true | Set to true to display this reference line. |
| `coloredBackground` | boolean | No | false | Set to true to fill the label and/or value of this reference line with this color |
| `showLabel` | boolean | No | true | Set to true to show the label of this reference line. |
| `showValue` | boolean | No | true | Set to true to show the value of this reference line. |
| `style` | [refLineStyle](#reflinestyle-object) | No | - | Styling settings for reference line |

---

### refLineStyle `object`

Styling settings for reference line

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lineThickness` | number | No | 2 | Set the thickness for this reference line. |
| `lineType` | string | No | "" | Set the dash type for this reference line. |

---
