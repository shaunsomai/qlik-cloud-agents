---
source: https://qlik.dev/apis/javascript/sn-org-chart/
last_updated: 2026-05-28T16:30:08+01:00
---

# Nebula Org chart

`Version: 1.7.0` | _experimental_

Org chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [Style](#style-object)
- [FontColor](#fontcolor-object)
- [Background](#background-object)
- [Border](#border-object)
- [PaletteColor](#palettecolor-object)
- [ColorExpression](#colorexpression-object)

## Entries

### properties `object`

extends `EngineAPI.GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `showTitles` | boolean | Yes | true | Show title for the visualization |
| `title` | string | Yes | "" | Visualization title |
| `subtitle` | string | Yes | "" | Visualization subtitle |
| `footnote` | string | Yes | "" | Visualization footnote |
| `navigationMode` | 'expandAll' \| 'free' | Yes | "free" | How the org chart is navigated |
| `resizeOnExpand` | boolean | Yes | false | Resize and pan chart when a node's list of children is expanded |
| `style` | [Style](#style-object) | Yes | - | Holds chart styling |

---

## Definitions

### Style `object`

Holds styling options

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontColor` | [FontColor](#fontcolor-object) | No | - | Color of the text, by default #484848 |
| `backgroundColor` | [Background](#background-object) | No | - | Color of the background, by default #ffffff |
| `border` | [Border](#border-object) | No | - | Styling for border, by default #737373 |

---

### FontColor `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `colorType` | 'auto' \| 'colorPicker' \| 'byExpression' | No | "auto" | How the font color is defined |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if colorType is colorPicker |
| `colorExpression` | [ColorExpression](#colorexpression-object) | No | - | Color defined by expression, needed if colorType is byExpression |

---

### Background `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `colorType` | 'auto' \| 'colorPicker' \| 'byExpression' | No | "colorPicker" | How the background color is defined |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if colorType is colorPicker |
| `colorExpression` | [ColorExpression](#colorexpression-object) | No | - | Color defined by expression, needed if colorType is byExpression |

---

### Border `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `top` | boolean | No | true | Set to true to show thicker top border |
| `fullBorder` | boolean | No | true | Set to true to show full border |
| `colorType` | 'auto' \| 'colorPicker' \| 'byExpression' | No | "auto" | How the border color is defined |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if colorType is colorPicker |
| `colorExpression` | [ColorExpression](#colorexpression-object) | No | - | Color defined by expression, needed if colorType is byExpression |

---

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | No | - | Color as hex string (only used if index: -1) |
| `index` | number | No | - | Index in palette |

---

### ColorExpression `object`

Format for using color expressions

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStringExpression` | object | Yes | - |  |

<details>
<summary>Properties of `qStringExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - | expression that resolves to a supported color format |

</details>

---
