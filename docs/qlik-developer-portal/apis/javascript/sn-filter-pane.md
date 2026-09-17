---
source: https://qlik.dev/apis/javascript/sn-filter-pane/
last_updated: 2026-08-25T10:14:37+01:00
---

# Nebula Filter Pane

`Version: 1.4.0` | _stable_

Filter pane generic object definition

## Table of Contents

### Entries

- [properties](#properties-namespace)

### Definitions

- [ChildListDef](#childlistdef)

## Entries

### properties `namespace`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote. |
| `qChildListDef` | [ChildListDef](#childlistdef) | Yes | "{}" | A list definition for listing child objects. The child object should contain listbox properties. See https://qlik.dev/apis/javascript/nebula-listbox-properties |
| `showTitles` | boolean | No | false | Show title for the visualization. |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle. |
| `title` | string \| StringExpression | No | "" | Visualization title. |
| `version` | string | Yes | - | Current version of this generic object definition |

---

## Definitions

### ChildListDef

---
