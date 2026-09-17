---
source: https://qlik.dev/apis/javascript/sn-gauge/
last_updated: 2026-08-25T10:14:37+01:00
---

# Nebula Gauge

`Version: 0.11.0` | _stable_

Gauge generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [Axis](#axis-object)
- [AxisStyling](#axisstyling-object)
- [Component](#component-union)
- [Expr](#expr-object)
- [FontStyling](#fontstyling-object)
- [Label](#label-object)
- [LabelNameStyling](#labelnamestyling-object)
- [LabelValueStyling](#labelvaluestyling-object)
- [Limits](#limits-object)
- [PaletteColor](#palettecolor-object)
- [RefLine](#refline-object)
- [RefLineStyle](#reflinestyle-object)
- [StringExpression](#stringexpression-object)
- [ValueExpression](#valueexpression-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoOrientation` | boolean | Yes | true | Auto orientation, only applicable to bar gauge. If true, the orientation of the bar gauge is adaptive to the aspect ratio of the chart. |
| `color` | object | Yes | - | Color settings. |
| `components` | [Component](#component-union)[] | Yes | - | Styling of chart components. |
| `disableNavMenu` | boolean | Yes | false |  |
| `footnote` | string \| [StringExpression](#stringexpression-object) | No | "" | Footnote of the visualization. |
| `gaugetype` | 'radial' \| 'bar' | Yes | "radial" | Gauge type |
| `measureAxis` | object | Yes | - | Measure axis configuration. |
| `orientation` | 'horizontal' \| 'vertical' | Yes | "horizontal" | Orientation of the bar gauge. Only applicable when autoOrientation is false. |
| `paletteProgressColor` | [PaletteColor](#palettecolor-object) | Yes | - | Define the progress color. Applicable when useSegment is 'off' and useBaseColors is also 'off' |
| `qHyperCubeDef` | object | Yes | - | Hypercube definition for the visualization. |
| `refLine` | object | Yes | - | Reference lines settings |
| `segmentInfo` | object | Yes | - | Segment information for the gauge. |
| `showDetails` | boolean | Yes | true | Show visualization details toggle |
| `showTitles` | boolean | Yes | true | Whether to show titles for the visualization. |
| `subtitle` | string \| [StringExpression](#stringexpression-object) | No | "" | Subtitle of the visualization. |
| `title` | string \| [StringExpression](#stringexpression-object) | No | "" | Title of the visualization. |
| `useSegments` | boolean | Yes | false | Decide if segments coloring or progress coloring is used. If true, the segments are colored according to the segmentInfo.paletteColors. |
| `version` | string | Yes | - | Current version of this generic object definition |

<details>
<summary>Properties of `color`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useBaseColors` | 'measure' \| 'off' | Yes | "measure" | If should use colors encoded in master items |

</details>

<details>
<summary>Properties of `measureAxis`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `max` | number \| [ValueExpression](#valueexpression-object) | Yes | 100 | Maximum value for the measure axis. |
| `min` | number \| [ValueExpression](#valueexpression-object) | Yes | 0 | Minimum value for the measure axis. |
| `show` | 'all' \| 'labels' \| 'title' \| 'none' | Yes | "all" | Labels and title |
| `spacing` | 1 \| 0.5 \| 2 | Yes | 1 | Axis scale |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qInitialDataFetch` | object[] | Yes | - | Initial data fetch configuration. |
| `qMeasures` | Array | Yes | - | Array of measures for the hypercube. |
| `qSuppressMissing` | boolean | Yes | true | Whether to suppress missing values. |
| `qSuppressZero` | boolean | Yes | false | Whether to suppress zero values. |

</details>

<details>
<summary>Properties of `refLine`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `refLines` | [RefLine](#refline-object)[] | Yes | - | Array of measure based reference line definitions |

</details>

<details>
<summary>Properties of `segmentInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `limits` | [Limits](#limits-object)[] | Yes | - | Array of segment limits. |
| `paletteColors` | [PaletteColor](#palettecolor-object)[] | Yes | - | Array of segment colors. |

</details>

---

## Definitions

### Axis `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `axis` | [AxisStyling](#axisstyling-object) | Yes | - |  |
| `key` | string | Yes | - | This should be set to `"axis"` |

---

### AxisStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | [LabelNameStyling](#labelnamestyling-object) | Yes | - |  |
| `title` | [FontStyling](#fontstyling-object) | Yes | - |  |

---

### Component `union`

---

### Expr `object`

Expression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - | expression as a string, e.g. '=Sum([Actual Amount])', note that the equal sign is optional |

---

### FontStyling `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | [PaletteColor](#palettecolor-object) | Yes | - |  |
| `fontFamily` | string | Yes | - |  |

---

### Label `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `"value"` |
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
| `value` | [FontStyling](#fontstyling-object) | Yes | - | Gauge value label |

---

### Limits `object`

The limits between segments colors.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `gradient` | boolean | Yes | - | Gradient color (i.e. gradually changing color) or solid color |
| `value` | number \| [ValueExpression](#valueexpression-object) | Yes | - | Value of the limit |

---

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---

### RefLine `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string \| [StringExpression](#stringexpression-object) | Yes | - | Reference line label. |
| `paletteColor` | [PaletteColor](#palettecolor-object) | Yes | - | Color of the reference line and label. |
| `refLineExpr` | object | Yes | - |  |
| `show` | boolean \| [ValueExpression](#valueexpression-object) | Yes | true | Set to true to display this reference line. |
| `showLabel` | boolean | No | true | Set to true to show the label of this reference line. |
| `showValue` | boolean | No | true | Set to true to show the value of this reference line. |
| `style` | [RefLineStyle](#reflinestyle-object) | No | - | Styling settings for reference line |

<details>
<summary>Properties of `refLineExpr`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | number \| [ValueExpression](#valueexpression-object) | Yes | - |  |
| `label` | string \| [StringExpression](#stringexpression-object) | No | - |  |

</details>

---

### RefLineStyle `object`

Styling settings for reference line

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lineThickness` | number | No | 2 | Set the thickness for this reference line. |
| `lineType` | string | No | "" | Set the dash type for this reference line. |

---

### StringExpression `object`

String expression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStringExpression` | [Expr](#expr-object) | Yes | - |  |

---

### ValueExpression `object`

Value expression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qValueExpression` | [Expr](#expr-object) | Yes | - |  |

---
