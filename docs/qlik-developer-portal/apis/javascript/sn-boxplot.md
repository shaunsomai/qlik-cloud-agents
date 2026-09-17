---
source: https://qlik.dev/apis/javascript/sn-boxplot/
last_updated: 2026-01-19T15:48:02Z
---

# Nebula Box plot chart

`Version: 1.0.6` | _experimental_

Boxplot generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [paletteColor](#palettecolor-object)
- [refLine](#refline-object)
- [refLineStyle](#reflinestyle-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `boxplotDef` | object | Yes | - | Settings specific to the boxplot |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridlines` | object | Yes | - | Grid lines settings. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `orientation` | 'vertical' \| 'horizontal' | Yes | "vertical" | Orientation setting. If vertical, the dimension axis can only be docked on bottom or top and measure axis on left or right. |
| `refLine` | object | Yes | - | Reference lines settings |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `sorting` | object | Yes | - | Wrapper for sorting properties which will be set on the outer dimension. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition. |

<details>
<summary>Properties of `boxplotDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `calculations` | object | Yes | - | Box plot calculation settings. |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `elements` | object | Yes | - | Box plot elements settings. |
| `presentation` | object | Yes | - | Presentation settings for the boxplots |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `sorting` | object | Yes | - | Wrapper for sorting properties which will be set on the outer dimension. |

<details>
<summary>Properties of `calculations`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Use automatic calculations |
| `mode` | 'tukey' \| 'fractiles' \| 'stdDev' | Yes | "tukey" | Auto calculation modes |
| `parameters` | object | Yes | - | Box plot calculation settings |

<details>
<summary>Properties of `parameters`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fractiles` | number | Yes | 0.01 | A number representing the two whisker fractiles as N and 1-N |
| `stdDev` | number | Yes | 3 | Standard deviation spread for whiskers |
| `tukey` | number | Yes | 1.5 | Number of interquartile ranges for whiskers. |

</details>

</details>

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Set to use automatic coloring. When `"auto": true`, color settings are based on the visualization used and the number of dimensions and measures, that is, the settings are not fixed, but are dependent on the data input. |
| `box` | object | Yes | - |  |
| `expressionIsColor` | true | Yes | - | Should be true |
| `expressionLabel` | string | Yes | "" | Label to be defined on tool tips when using a coloring expression. Only used if `'expressionIsColor': false`. |
| `mode` | 'primary' \| 'byExpression' \| 'byMultiple' | Yes | "primary" | Sets the coloring mode for the visualization when auto-coloring has been switched off (`"auto": false`). Can be one of: * `primary`: a single color (by default blue) is used for all items in the chart. In visualizations that do not benefit from multiple colors (bar charts with one dimension and scatter plots), single color is the default setting. * `byExpression`: coloring is based on an expression, which in most cases is a color code. Details are set in the `"expressionIsColor"`, `"expressionLabel`" and `"colorExpression"` properties. * `byMultiple`: can be used when more than one measure is used. By default, 12 colors are used for the dimensions. The colors are reused when there are more than 12 dimension values. |
| `point` | object | Yes | - |  |
| `useBaseColors` | 'off' \| 'dimension' \| 'measure' | Yes | "off" | Use colors encoded in master items. Only applicable when `"mode": "primary"` has been defined. |

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
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the point color when you color by single color `("mode": "primary")`. |

</details>

</details>

<details>
<summary>Properties of `elements`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `firstWhisker` | object | Yes | - | Box plot element settings |
| `outliers` | object | Yes | - | Box plot outliers element |

<details>
<summary>Properties of `firstWhisker`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string \| StringExpression | No | "" | Label for the boxplot element |

</details>

<details>
<summary>Properties of `outliers`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `include` | boolean | Yes | true | Show the outliers. |
| `sortOutliers` | boolean | Yes | true |  |

</details>

</details>

<details>
<summary>Properties of `presentation`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `whiskers` | object | Yes | - | Settings for the boxplot whiskers |

<details>
<summary>Properties of `whiskers`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean | Yes | true | Show whiskers. |

</details>

</details>

<details>
<summary>Properties of `sorting`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoSort` | boolean | Yes | true | Sort automatically |

</details>

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
| `elementId` | 'firstWhisker' \| 'boxStart' \| 'boxMiddle' \| 'boxEnd' \| 'lastWhisker' | Yes | "firstWhisker" | Sorting preset |
| `expression` | ValueExpression | Yes | - | Expression for the sorting. Requires sortByExpression to be -1 or 1. |
| `sortCriteria` | object | Yes | - |  |

<details>
<summary>Properties of `sortCriteria`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sortByAscii` | number | Yes | 0 | Sort by alphabetic |
| `sortByExpression` | number | Yes | 0 | Sort by expression |
| `sortByNumeric` | number | Yes | 0 | Sort by numeric |

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
