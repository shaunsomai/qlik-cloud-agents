---
source: https://qlik.dev/apis/javascript/sn-mekko-chart/
last_updated: 2026-01-19T15:48:02Z
---

# Nebula Mekko chart

`Version: 1.4.7` | _stable_

Mekko chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [legendConfig](#legendconfig-object)
- [byDimensionConfig](#bydimensionconfig-object)

## Entries

### properties `object`

extends `EngineAPI.GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `title` | string \| EngineAPI.StringExpression | No | "" | Visualization title. |
| `subtitle` | string \| EngineAPI.StringExpression | No | "" | Visualization subtitle. |
| `footnote` | string \| EngineAPI.StringExpression | No | "" | Visualization footnote. |
| `cellColor` | object | Yes | - |  |

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qSuppressZero` | boolean | Yes | true |  |
| `qSuppressMissing` | boolean | Yes | true |  |

</details>

<details>
<summary>Properties of `cellColor`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `byDimension` | [byDimensionConfig](#bydimensionconfig-object) | No | "byDimensionConfig" |  |
| `mode` | 'auto' \| 'byDimension' | Yes | "auto" |  |
| `legend` | [legendConfig](#legendconfig-object) | Yes | - |  |

</details>

---

## Definitions

### legendConfig `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `show` | boolean \| 'auto' | Yes | "auto" |  |
| `showTitle` | boolean | Yes | true |  |

---

### byDimensionConfig `object`

Configuration object for when mode is set to `byDimension`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'index' \| 'libraryId' \| 'expression' | Yes | - |  |
| `typeValue` | number \| string | Yes | - |  |
| `label` | string \| EngineAPI.StringExpression | No | - |  |
| `persistent` | boolean | No | false |  |
| `scheme` | string | No | "" |  |

---
