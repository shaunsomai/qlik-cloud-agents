---
source: https://qlik.dev/apis/javascript/sn-sankey-chart/
last_updated: 2026-09-11T16:13:57Z
---

# Nebula Sankey chart

`Version: 1.25.0` | _stable_

Sankey chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [AttributeExpressionProperties](#attributeexpressionproperties-interface)
- [DimensionProperties](#dimensionproperties-object)
- [InlineDimensionDef](#inlinedimensiondef-object)
- [InlineMeasureDef](#inlinemeasuredef-object)
- [MeasureProperties](#measureproperties-object)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `link` | object | Yes | - | Link style settings. |
| `node` | object | Yes | - | Node settings. |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `showTitles` | boolean | No | true | Show title for the visualization. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition |

<details>
<summary>Properties of `link`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `opacity` | number | Yes | 0.5 | Opacity of the links in the chart. Between 0 and 1. |

</details>

<details>
<summary>Properties of `node`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `padding` | number | Yes | 0.2 | Padding between the nodes. Between 0 and 1. |
| `sort` | 'valueA' \| 'valueD' \| 'data' | No | - | Sorting mode for nodes.  - `undefined` - Prioritize sorting for optimal layout. - `'valueA'` - Sort according to value of each node, in ascending order. - `'valueD'` - Sort according to value of each node, in descending order. - `'data` - Sort according to the order of the data. |
| `width` | number | Yes | 0.2 | Width of the nodes. Can be a value between 0 and 1. |

</details>

<details>
<summary>Properties of `qHyperCubeDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimensions` | [DimensionProperties](#dimensionproperties-object)[] | Yes | - |  |
| `qMeasures` | [MeasureProperties](#measureproperties-object)[] | Yes | - |  |
| `qSuppressMissing` | boolean | Yes | true |  |
| `qSuppressZero` | boolean | Yes | false |  |

</details>

---

## Definitions

### AttributeExpressionProperties `interface`

extends `NxAttrExprDef`

Extends `NxAttrExprDef`, see Engine API: `NxAttrExprDef`.
Can be used to color nodes (specified under dimension) or a links (specified under measure) (CSS color).
See example below on how to specify custom color for links in the chart.

<details>
<summary>Examples</summary>

Set color of links to be "green"

```json
"qAttributeExpressions": [
    {
      "qExpression": "'green'",
      "qLibraryId": "",
      "qAttribute": true
    }
]
```

</details>

---

### DimensionProperties `object`

extends `NxDimension`

Extends `NxDimension`, see Engine API: `NxDimension`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAttributeExpressions` | [AttributeExpressionProperties](#attributeexpressionproperties-interface)[] | Yes | - |  |
| `qDef` | [InlineDimensionDef](#inlinedimensiondef-object) | Yes | - |  |

---

### InlineDimensionDef `object`

extends `NxInlineDimensionDef`

Extends `NxInlineDimensionDef`, see Engine API: `NxInlineDimensionDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `othersLabel` | string \| StringExpression | Yes | - |  |
| `autoSort` | boolean | No | - | Set to automatically sort the dimension. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |

---

### InlineMeasureDef `object`

extends `NxInlineMeasureDef`

Extends `NxInlineMeasureDef`, see Engine API: `NxInlineMeasureDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isCustomFormatted` | boolean | Yes | - | Set to true to toggle off the default client formatting. |
| `numFormatFromTemplate` | boolean | Yes | true | When enabled, the number format to use can be selected from multiple predefined formats based on the desired type (number, date). |
| `autoSort` | boolean | No | - | Set to automatically sort the measure. |
| `cId` | string | No | - | ID used by the Qlik Sense. Must be unique within the current chart. |

---

### MeasureProperties `object`

extends `NxMeasure`

Extends `NxMeasure`, see Engine API: `NxMeasure`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAttributeExpressions` | [AttributeExpressionProperties](#attributeexpressionproperties-interface)[] | Yes | - |  |
| `qDef` | [InlineMeasureDef](#inlinemeasuredef-object) | Yes | - |  |

---
