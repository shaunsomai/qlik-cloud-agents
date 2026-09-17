---
source: https://qlik.dev/apis/javascript/sn-histogram/
last_updated: 2026-01-19T15:48:02Z
---

# Nebula Histogram chart

`Version: 1.0.6` | _experimental_

Histogram generic object definition

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
| `bins` | object | Yes | - | Bin settings. |
| `color` | object | Yes | - | Color settings. |
| `dataPoint` | object | Yes | - | Data points |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridlines` | object | Yes | - | Grid lines settings. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `refLine` | object | Yes | - | Reference lines settings |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `sorting` | object | Yes | - | Wrapper for sorting properties which will be set on the outer dimension. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition. |

<details>
<summary>Properties of `bins`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | - | Auto mode generates a nice looking histogram without special parameters. |
| `binCount` | number | Yes | "" | Number of bars to be displayed, used when binMode is set to 'maxCount'. |
| `binMode` | string | Yes | - | MaxCount - Able to adjust the maximum number of bars to be displayed. size - Able to adjust size of bars and offset from x-axis. |
| `binSize` | number | Yes | - | The width of the bars, used when binMode is set to 'size'. |
| `countDistinct` | boolean | Yes | - | Shows unique values. |
| `offset` | number | Yes | - | Used to know where to start displaying bars on x-axis. |

</details>

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bar` | object | Yes | - |  |

<details>
<summary>Properties of `bar`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6 }" | The paletteColor object is used to define the bar color. |

</details>

</details>

<details>
<summary>Properties of `dataPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `showLabels` | boolean | Yes | false | Show labels on bars |

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
| `label` | string \| StringExpression | No | "" | Label to show on the measure axis, if left empty it defaults to 'Frequency' |
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
| `autoSort` | true | Yes | - | Sort automatically |

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
