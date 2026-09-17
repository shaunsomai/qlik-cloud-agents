---
source: https://qlik.dev/apis/javascript/sn-table/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Table

`Version: 6.55.0` | _stable_

Table generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [DimensionProperties](#dimensionproperties-object)
- [MeasureProperties](#measureproperties-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [AttributeExpressionProperties](#attributeexpressionproperties-object)
- [TextAlign](#textalign-object)
- [ColumnWidth](#columnwidth-object)
- [Component](#component-object)
- [ContentStyling](#contentstyling-object)
- [HeaderStyling](#headerstyling-object)
- [PaletteColor](#palettecolor-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `qHyperCubeDef` | object | Yes | - | Extends HyperCubeDef, see Engine API: HyperCubeDef |
| `showTitles` | boolean | No | true | Show title for the visualization |
| `enableChartExploration` | boolean | No | false | Show chart exploration option in context menu |
| `title` | string \| StringExpression | No | "" | Visualization title |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote |
| `totals` | object | No | - | totals settings |
| `usePagination` | boolean | No | false | Use pagination or continuous scroll. If undefined, defaults to using pagination |
| `components` | [Component](#component-object)[] | Yes | - | Holds general styling |

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - | The maximum amount of dimensions is 1000 |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - | The maximum amount of measures is 1000 |
| `qColumnOrder` | number[] | Yes | - |  |

</details>

<details>
<summary>Properties of `totals`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | No | "Totals" | The label of the totals row, shown in the leftmost column |
| `show` | boolean | No | true | If set to true, the display of the totals row will be handled automatically, and the `position` prop will be ignored. |
| `position` | 'top' \| 'bottom' \| 'noTotals' | No | "noTotals" | The position of the totals row, hiding it if set to `noTotals` |

</details>

---

## Definitions

### DimensionProperties `object`

extends `NxDimension`

Extends `NxDimension`, see Engine API: `NxDimension`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDef` | [InlineDimensionDef](#inlinedimensiondef-object) | Yes | - |  |
| `qAttributeExpressions` | [AttributeExpressionProperties](#attributeexpressionproperties-object)[] | Yes | - |  |

---

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDef` | [InlineMeasureDef](#inlinemeasuredef-object) | Yes | - |  |
| `qAttributeExpressions` | [AttributeExpressionProperties](#attributeexpressionproperties-object)[] | Yes | - |  |

---

### InlineDimensionDef `object`

extends `NxInlineDimensionDef`

Extends `NxInlineDimensionDef`, see Engine API: `NxInlineDimensionDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `textAlign` | [TextAlign](#textalign-object) | No | - |  |
| `columnWidth` | [ColumnWidth](#columnwidth-object) | No | - |  |

---

### InlineMeasureDef `object`

extends `NxInlineMeasureDef`

Extends `NxInlineMeasureDef`, see Engine API: `NxInlineMeasureDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `textAlign` | [TextAlign](#textalign-object) | No | - |  |
| `columnWidth` | [ColumnWidth](#columnwidth-object) | No | - |  |

---

### AttributeExpressionProperties `object`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.
Column specific styling overrides general styling, that is defined in `components`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | 'cellForegroundColor' \| 'cellBackgroundColor' \| 'textStyleExpression' | Yes | - | specifying what the style applies to |

---

### TextAlign `object`

extends `NxInlineDimensionDef`

Holds text alignment for a specific column.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | - | If true, sets the alignment based on the type of column (left for dimension, right for measure) |
| `align` | 'left' \| 'center' \| 'right' | Yes | - | Is used (and mandatory) if `auto` is false |

---

### ColumnWidth `object`

Column width info

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'auto' \| 'FitToContent' \| 'pixels' \| 'percentage' | Yes | - | Defines how the column width is set. `auto` calculates the width(s) so the total table width equals the chart width. `fitToContent` calculates a width based on the cells' content. `pixels` uses a specified pixel value. `percentage` sets the column width to specified percentage of the chart width |
| `pixels` | number | No | - | Is used (and mandatory) if type is `pixels` |
| `percentage` | number | No | - | Is used (and mandatory) if type is `percentage` |

---

### Component `object`

General styling for all columns.
Split up into header and content (body) styling.
If any property is not set, default values specific for each property is used.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `theme` |
| `content` | [ContentStyling](#contentstyling-object) | No | - |  |
| `header` | [HeaderStyling](#headerstyling-object) | No | - |  |

---

### ContentStyling `object`

Holds properties for font size, font color and hover styling.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontSize` | number | No | - | Defaults to `14` |
| `fontColor` | [PaletteColor](#palettecolor-object) | No | - | Defaults to `#404040` |
| `hoverEffect` | boolean | No | - | Toggles hover effect |
| `hoverColor` | [PaletteColor](#palettecolor-object) | No | - | Background hover color. Uses `#f4f4f4` if no hover colors are set, is transparent if only `hoverFontColor` is set |
| `hoverFontColor` | [PaletteColor](#palettecolor-object) | No | - | When only `hoverColor` is set, this is adjusted to either `#f4f4f4` or `#ffffff` for optimal contrast |
| `padding` | string | No | - | Css setting for the cell padding, defaults to `4px 12px` |

---

### HeaderStyling `object`

Holds properties for font size and color.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontSize` | number | No | - | Defaults to `14` |
| `fontColor` | [PaletteColor](#palettecolor-object) | No | - | Defaults to `#404040` |

---

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---
