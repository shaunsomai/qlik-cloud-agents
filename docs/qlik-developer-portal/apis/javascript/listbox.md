---
source: https://qlik.dev/apis/javascript/listbox/
last_updated: 2026-08-25T10:14:37+01:00
---

# Nebula Listbox properties

`Version: 7.4.0` | _stable_

nebula listbox properties definition

## Table of Contents

### Definitions

- [ListboxProperties](#listboxproperties-object)
- [ListObjectDef](#listobjectdef-interface)
- [ValueExpression](#valueexpression-object)

## Definitions

### ListboxProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoConfirm` | boolean | No | false | Automatically confirm selections when clicking outside a listbox, without showing the selections toolbar. |
| `checkboxes` | boolean | No | false | Show values as checkboxes instead of as fields. |
| `frequencyMax` | 'fetch' \| [ValueExpression](#valueexpression-object) | No | - | frequencyMax calculation needed for histogram when not using qListObjectDef.qFrequencyMode: 'P' use an expression in the form `Max(AGGR(Count([field]), [field]))` (when needed) or 'fetch' that triggers an extra engine call but needed for library dimension that could change field when using the object |
| `histogram` | boolean | No | false | Show histogram bar. also requires (qListObjectDef.qFrequencyMode 'V' and frequencyMax) or qListObjectDef.qFrequencyMode 'P' |
| `layoutOptions` | object | No | - | Layout settings. |
| `qListObjectDef` | [ListObjectDef](#listobjectdef-interface) | Yes | - |  |
| `searchEnabled` | boolean | No | true | Enables search. |
| `showTitle` | boolean | No | true | Show title. |
| `title` | string | No | "" | Listbox title |
| `wildCardSearch` | boolean | No | false | Pre-fill search input field with wildcard characters. |

<details>
<summary>Properties of `layoutOptions`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dataLayout` | 'singleColumn' \| 'grid' | No | "singleColumn" | Layout mode. |
| `dense` | boolean | No | false | Dense mode. |
| `layoutOrder` | 'row' \| 'column' | No | "row" | Layout order. Only used when dataLayout is 'grid' |
| `maxVisibleColumns` | object | No | - | Max visible columns. Only used when dataLayout is 'grid' and layoutOrder is 'row' |
| `maxVisibleRows` | object | No | - | Max visible rows. Only used when dataLayout is 'grid' and layoutOrder is 'column' |

<details>
<summary>Properties of `maxVisibleColumns`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | No | true | Automatically fit as many columns as possible. Only used when dataLayout is 'grid' and layoutOrder is 'row' |
| `maxColumns` | number | No | 3 | Fixed number of max visible columns. Only used when dataLayout is 'grid' layoutOrder is 'row' and auto is false |

</details>

<details>
<summary>Properties of `maxVisibleRows`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | No | true | Automatically fits as many rows as possible. Only used when dataLayout is 'grid' and layoutOrder is 'column' |
| `maxRows` | number | No | 3 | Fixed number of max visible rows. Only used when dataLayout is 'grid' layoutOrder is 'column' and auto is false |

</details>

</details>

---

### ListObjectDef `interface`

extends `qix.ListObjectDef`

Extends `ListObjectDef`, see Engine API: `ListObjectDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `frequencyEnabled` | boolean | No | false | Show frequency count. also requires qListObjectDef.qFrequencyMode to be set |

---

### ValueExpression `object`

see: https://qlik.dev/apis/json-rpc/qix/schemas#%23%2Fdefinitions%2Fschemas%2Fentries%2FValueExpression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qValueExpression` | object | Yes | - |  |

<details>
<summary>Properties of `qValueExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - |  |

</details>

---
