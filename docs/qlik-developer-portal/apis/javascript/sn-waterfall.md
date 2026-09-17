---
source: https://qlik.dev/apis/javascript/sn-waterfall/
last_updated: 2026-01-19T15:48:02Z
---

# Nebula Waterfall chart

`Version: 1.0.6` | _experimental_

Waterfall chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [FieldAttributes](#fieldattributes-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [MeasureProperties](#measureproperties-object)
- [paletteColor](#palettecolor-object)
- [properties.qDef.isCustomFormatted](#propertiesqdefiscustomformatted)
- [properties.qDef.numFormatFromTemplate](#propertiesqdefnumformatfromtemplate)
- [properties.qDef.qNumFormat](#propertiesqdefqnumformat)
- [refLine](#refline-object)
- [refLineStyle](#reflinestyle-object)
- [subtotalProperties](#subtotalproperties-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | object | Yes | - | Color settings. Most color options for visualizations are set in the color object in the options. You activate custom coloring by setting `"auto": false` which turns off auto-coloring. If `"auto": true`, no other properties need to be defined in the color object. Note: Some of the color properties are depending on which theme is currently being used. |
| `dataPoint` | object | Yes | - | Data point. |
| `dimensionAxis` | object | Yes | - | Dimension axis settings. |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `gridlines` | object | Yes | - | Grid lines settings. |
| `legend` | object | Yes | - | Legend settings. |
| `measureAxis` | object | Yes | - | Measure axis settings. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `refLine` | object | Yes | - | Reference lines settings |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition. |

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Set to use automatic coloring. When `"auto": true`, color settings are based on the visualization used and the number of dimensions and measures, that is, the settings are not fixed, but are dependent on the data input. |
| `negativeValue` | object | Yes | - | Negative value color. |
| `positiveValue` | object | Yes | - | Positive value color. |
| `subtotal` | object | Yes | - | Subtotal value color. |

<details>
<summary>Properties of `negativeValue`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: -1, color: '#cc6677' }" | paletteColor |

</details>

<details>
<summary>Properties of `positiveValue`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: 6, color: null }" | paletteColor |

</details>

<details>
<summary>Properties of `subtotal`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paletteColor` | [paletteColor](#palettecolor-object) | Yes | "{ index: -1, color: '#c3c3c3' }" | paletteColor |

</details>

</details>

<details>
<summary>Properties of `dataPoint`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `showLabels` | boolean | Yes | true | Show labels. |

</details>

<details>
<summary>Properties of `dimensionAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'near' \| 'far' | Yes | "near" | Axis docking position |
| `label` | 'auto' \| 'horizontal' \| 'tilted' | Yes | "auto" | Label orientation |
| `show` | 'labels' \| 'none' | Yes | "labels" | Labels and title |

</details>

<details>
<summary>Properties of `gridlines`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | true | Automatic grid line spacing. |
| `spacing` | 0 \| 2 \| 3 | Yes | 2 | Grid line spacing. Used only when auto is set to false. |

</details>

<details>
<summary>Properties of `legend`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dock` | 'auto' \| 'right' \| 'left' \| 'bottom' \| 'top' | Yes | "auto" | Sets the legend position. |
| `show` | boolean | Yes | true | Set to show the legend. |

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
| `show` | 'labels' \| 'none' | Yes | "labels" | Labels and title |
| `spacing` | number | Yes | 1 | Axis scale |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |

</details>

<details>
<summary>Properties of `refLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `refLines` | [refLine](#refline-object)[] | Yes | - | Array of measure based reference line definitions |

</details>

---

## Definitions

### FieldAttributes `object`

Field attributes structure.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dec` | string | Yes | - | Defines the decimal separator. |
| `Fmt` | string | Yes | - | Defines the format pattern that applies to qText. |
| `nDec` | number | Yes | - | Number of decimals. |
| `Thou` | string | Yes | - | Defines the thousand separator (if any). |
| `Type` | string | Yes | - | Type of the field. |
| `UseThou` | number | Yes | - | Defines whether or not a thousands separator must be used. |

---

### InlineMeasureDef `object`

extends `NxInlineMeasureDef`

Extends `NxInlineMeasureDef`, see Engine API: `NxInlineMeasureDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `subtotal` | [subtotalProperties](#subtotalproperties-object) | Yes | - | subtotal settings. |
| `valueType` | 'NORMAL' \| 'INVERSE' \| 'SUBTOTAL' | Yes | "NORMAL" | Measure operation. |

---

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDef` | [InlineMeasureDef](#inlinemeasuredef-object) | Yes | - |  |

---

### paletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---

### properties.qDef.isCustomFormatted

If true, the client formatting will be toggled off.

---

### properties.qDef.numFormatFromTemplate

When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date).

---

### properties.qDef.qNumFormat

see Engine API: `FieldAttributes`.

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

### subtotalProperties `object`

Settings for subtotal

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `enable` | boolean | Yes | false | Option to add a subtotal after a measure. |
| `label` | string | Yes | "Subtotal" | Label of the subtotal added after a measure. |

---
