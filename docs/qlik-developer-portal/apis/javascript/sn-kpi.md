---
source: https://qlik.dev/apis/javascript/sn-kpi/
last_updated: 2026-03-09T12:29:42Z
---

# Nebula KPI

`Version: 2.4.0` | _stable_

KPI generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [MeasureProperties](#measureproperties-object)
- [Coloring](#coloring-object)
- [MeasureAxis](#measureaxis-object)
- [ConditionalColoring](#conditionalcoloring-object)
- [Gradient](#gradient-object)
- [Segments](#segments-object)
- [Limit](#limit-object)
- [PaletteColor](#palettecolor-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `qHyperCubeDef` | object | Yes | - | Extends HyperCubeDef, see Engine API: HyperCubeDef |
| `showTitles` | boolean | No | false |  |
| `title` | string | No | "" |  |
| `subtitle` | string | No | "" |  |
| `footnote` | string | No | "" |  |
| `showDetails` | boolean | No | true |  |
| `showMeasureTitle` | boolean | Yes | true |  |
| `showSecondMeasureTitle` | boolean | Yes | true |  |
| `textAlign` | 'left' \| 'center' \| 'right' | No | "center" |  |
| `layoutBehavior` | 'responsive' \| 'fixed' \| 'relative' | No | "relative" |  |
| `disableNavMenu` | boolean | Yes | false |  |
| `fontSize` | 'S' \| 'M' \| 'L' | Yes | "M" |  |
| `useLink` | boolean | Yes | false |  |
| `sheetLink` | string | No | "" |  |
| `openUrlInNewTab` | boolean | No | true |  |
| `components` | array | Yes | - |  |

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressZero` | boolean | Yes | false |  |
| `qSuppressMissing` | boolean | Yes | true |  |

</details>

---

## Definitions

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `coloring` | [Coloring](#coloring-object) | No | - |  |
| `conditionalColoring` | [ConditionalColoring](#conditionalcoloring-object) | Yes | - |  |
| `measureAxis` | [MeasureAxis](#measureaxis-object) | Yes | - | _(deprecated)_ |

---

### Coloring `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `baseColor` | [PaletteColor](#palettecolor-object) | No | - |  |
| `gradient` | [Gradient](#gradient-object) | No | - |  |

---

### MeasureAxis `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `min` | number | Yes | - |  |
| `max` | number | Yes | - |  |

---

### ConditionalColoring `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useConditionalColoring` | boolean | Yes | - |  |
| `useBaseColors` | boolean | Yes | - |  |
| `paletteSingleColor` | [PaletteColor](#palettecolor-object) | Yes | - |  |
| `segments` | [Segments](#segments-object) | Yes | - |  |

---

### Gradient `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `colors` | [PaletteColor](#palettecolor-object)[] | Yes | - |  |
| `breakTypes` | boolean[] | Yes | - |  |
| `limits` | number[] | Yes | - |  |
| `limitType` | 'percent' \| 'absolute' | Yes | - |  |

---

### Segments `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `limits` | [Limit](#limit-object)[] | Yes | - |  |
| `paletteColors` | [PaletteColor](#palettecolor-object)[] | Yes | - |  |

---

### Limit `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | number | Yes | - |  |
| `gradient` | boolean | Yes | - |  |

---

### PaletteColor `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `index` | number | Yes | - |  |
| `color` | string | Yes | - |  |

---
