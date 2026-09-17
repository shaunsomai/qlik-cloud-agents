---
source: https://qlik.dev/apis/javascript/sn-pivot-table/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Pivot table

`Version: 7.54.0` | _experimental_

Pivot Table generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [DimensionProperties](#dimensionproperties-object)
- [MeasureProperties](#measureproperties-object)
- [AttributeExpressionDef](#attributeexpressiondef-union)
- [ColorByExpressionId](#colorbyexpressionid-union)
- [ColorByExpressionDef](#colorbyexpressiondef-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [ColumnWidth](#columnwidth-object)
- [TextAlignValues](#textalignvalues-union)
- [TextAlign](#textalign-object)
- [Component](#component-union)
- [GeneralStylingKey](#generalstylingkey-literal)
- [FontStyleValues](#fontstylevalues-union)
- [GeneralStyling](#generalstyling-object)
- [BackgroundColor](#backgroundcolor-object)
- [BackgroundColorExpression](#backgroundcolorexpression-object)
- [BackgroundImage](#backgroundimage-object)
- [MediaUrl](#mediaurl-object)
- [TitleOptions](#titleoptions-object)
- [TitleStyling](#titlestyling-object)
- [ChartStylingKey](#chartstylingkey-literal)
- [ChartStyling](#chartstyling-object)
- [CellStyling](#cellstyling-object)
- [PartialCellStyling](#partialcellstyling-object)
- [GridStyling](#gridstyling-object)
- [PaletteColor](#palettecolor-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `qHyperCubeDef` | object | Yes | - |  |
| `showTitles` | boolean | No | true | Show title for the visualization |
| `title` | string \| StringExpression | No | "" | Visualization title |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote |
| `nullValueRepresentation` | object | No | - | Null value properties |
| `components` | [Component](#component-union)[] | No | - | General and chart specific styling |

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAlwaysFullyExpanded` | boolean | Yes | false |  |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - |  |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressMissing` | boolean | Yes | true |  |
| `qSuppressZero` | boolean | Yes | false |  |
| `qShowTotalsAbove` | boolean | Yes | true |  |
| `qIndentMode` | boolean | Yes | false |  |

</details>

<details>
<summary>Properties of `nullValueRepresentation`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `text` | string | No | "-" | Null value text |

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
| `qAttributeExpressions` | [AttributeExpressionDef](#attributeexpressiondef-union)[] | Yes | - |  |

---

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDefs` | [InlineMeasureDef](#inlinemeasuredef-object) | Yes | - |  |
| `qAttributeExpressions` | [AttributeExpressionDef](#attributeexpressiondef-union)[] | Yes | - |  |

---

### AttributeExpressionDef `union`

---

### ColorByExpressionId `union`

Color by expression identifier

---

### ColorByExpressionDef `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpression` | StringExpression | Yes | - |  |
| `id` | [ColorByExpressionId](#colorbyexpressionid-union) | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
{ qExpression: "=if(Sum([Sales Quantity]) > 500, green(), blue())", id: "cellBackgroundColor" }
```

</details>

---

### InlineDimensionDef `object`

extends `NxInlineDimensionDef`

Extends `NxInlineDimensionDef`, see Engine API: `NxInlineDimensionDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `columnWidth` | [ColumnWidth](#columnwidth-object) | No | - |  |
| `textAlign` | [TextAlign](#textalign-object) | No | - |  |

---

### InlineMeasureDef `object`

extends `NxInlineMeasureDef`

Extends `NxInlineMeasureDef`, see Engine API: `NxInlineMeasureDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `columnWidth` | [ColumnWidth](#columnwidth-object) | No | - |  |
| `textAlign` | [TextAlign](#textalign-object) | No | - |  |

---

### ColumnWidth `object`

Column width info. For the left grid, the properties are always applied.
For the right grid, only the leaf nodes will listen to the properties, and the columns above will get the width of the leaves accumulated

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'auto' \| 'FitToContent' \| 'pixels' \| 'percentage' | Yes | - | Defines how the column width is set. For the right grid, `auto` calculates the width(s) so the total width of the columns equals the right grid width. If the width reaches a minimum value, the columns will overflow. For the left grid, `auto` is N/A and defaults to `fitToContent`. `fitToContent` calculates a width based on the column's content. `pixels` uses a specified pixel value. `percentage` sets the column width to specified percentage of the chart/grid width |
| `pixels` | number | No | - | Pixel value used if type is `pixels` |
| `percentage` | number | No | - | Percentage value used if type is `percentage`. Note that for the left grid columns, this is a percentage of the whole chart width. For the right grid columns, it is a percentage of the right grid width |

---

### TextAlignValues `union`

Text align values

---

### TextAlign `object`

Set the alignment of text in the chart.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | Yes | - | If true the chart decides text alignment, otherwise the "align" value is used. |
| `align` | [TextAlignValues](#textalignvalues-union) | No | - | Align value |

---

### Component `union`

Styling defintions

---

### GeneralStylingKey `literal`

Mandatory key for general styling

---

### FontStyleValues `union`

Font styling values

---

### GeneralStyling `object`

General chart styling

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | [GeneralStylingKey](#generalstylingkey-literal) | Yes | - |  |
| `title` | [TitleStyling](#titlestyling-object) | Yes | - |  |
| `bgColor` | [BackgroundColor](#backgroundcolor-object) \| [BackgroundColorExpression](#backgroundcolorexpression-object) | No | - |  |
| `bgImage` | [BackgroundImage](#backgroundimage-object) | No | - |  |

<details>
<summary>Examples</summary>

```javascript
{
 key: "general",
 title: {
   main: {
     fontSize: "18px",
     fontFamily: "Arial",
     fontStyle: ["bold", "italic"],
     color: { color: "orangered" },
   }
 },
 bgColor: {
   useExpression: true,
   color: {
     index: 6,
     color: "#006580"
   },
   colorExpression: {
     qStringExpression: {
       qExpr: "red()"
     }
   }
 },
 bgImage: {
   mode: "media",
   mediaUrl: {
     qStaticContentUrlDef: {
       qUrl: "<path-to-image>"
     }
   }
 }
}
```

</details>

---

### BackgroundColor `object`

Chart background color

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | [PaletteColor](#palettecolor-object) | Yes | - | Background color palette |

---

### BackgroundColorExpression `object`

Chart background color by expression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useExpression` | boolean | Yes | - | Boolean to indicate if color by expression should be used |
| `colorExpression` | StringExpression | Yes | - | Color expression, "useExpression" must also be true |

---

### BackgroundImage `object`

Chart background image.

Background image takes precedence over background color.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mode` | "media" | Yes | - | Mode |
| `mediaUrl` | [MediaUrl](#mediaurl-object) | Yes | - | Media url |

---

### MediaUrl `object`

Media url

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStaticContentUrlDef` | object | Yes | - | Background image mode |

<details>
<summary>Properties of `qStaticContentUrlDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | Yes | - | Relative path of the image |

</details>

---

### TitleOptions `object`

Title styling options

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontSize` | string | No | - | Font size in pixel value |
| `fontFamily` | string | No | - | Font family |
| `fontStyle` | [FontStyleValues](#fontstylevalues-union)[] | No | - | Font style |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Font color palette |

---

### TitleStyling `object`

Title styling

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `main` | [TitleOptions](#titleoptions-object) | No | - | Styling for chart title |
| `subTitle` | [TitleOptions](#titleoptions-object) | No | - | Styling for chart sub title |
| `footer` | [TitleOptions](#titleoptions-object) | No | - | Styling for chart footer |

---

### ChartStylingKey `literal`

Mandatory key for chart styling

---

### ChartStyling `object`

Custom styling of cells

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | [ChartStylingKey](#chartstylingkey-literal) | Yes | - |  |
| `header` | [CellStyling](#cellstyling-object) | No | - | Styling for header cells |
| `dimensionValues` | [CellStyling](#cellstyling-object) | No | - | Styling for dimension value cells |
| `measureValues` | [CellStyling](#cellstyling-object) | No | - | Styling for measure value cells |
| `measureLabels` | [PartialCellStyling](#partialcellstyling-object) | No | - | Styling for measure label cells |
| `totalValues` | [PartialCellStyling](#partialcellstyling-object) | No | - | Styling for total value cells |
| `nullValues` | [PartialCellStyling](#partialcellstyling-object) | No | - | Styling for null values cells |
| `grid` | [GridStyling](#gridstyling-object) | No | - | General grid styling |

<details>
<summary>Examples</summary>

```javascript
{
 key: "theme",
 dimensionValues: {
   fontSize: "18px",
   fontFamily: "Arial",
   fontStyle: ["bold", "italic"],
   fontColor: { color: "orangered" },
   background: { index: 2 }
 }
}
```

</details>

---

### CellStyling `object`

Properties for styling a cell

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontSize` | string | No | - | Font size in pixel value |
| `fontFamily` | string | No | - | Font family |
| `fontStyle` | [FontStyleValues](#fontstylevalues-union)[] | No | - | Font style |
| `fontColor` | [PaletteColor](#palettecolor-object) | No | - | Font color palette |
| `background` | [PaletteColor](#palettecolor-object) | No | - | Cell background color palette |

---

### PartialCellStyling `object`

Properties for styling a cell

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontStyle` | [FontStyleValues](#fontstylevalues-union)[] | No | - | Font style |
| `fontColor` | [PaletteColor](#palettecolor-object) | No | - | Font color palette |
| `background` | [PaletteColor](#palettecolor-object) | No | - | Cell background color palette |

---

### GridStyling `object`

General grid styling

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lineClamp` | number | No | - | A numerical value that represents the number of lines a text at most can be splitt into |
| `border` | [PaletteColor](#palettecolor-object) | No | - | Border color between cells |
| `divider` | [PaletteColor](#palettecolor-object) | No | - | Border color between row and column dimensions sections |
| `background` | [PaletteColor](#palettecolor-object) | No | - |  |

---

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---
