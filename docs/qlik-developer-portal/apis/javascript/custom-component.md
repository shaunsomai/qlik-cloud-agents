---
source: https://qlik.dev/apis/javascript/custom-component/
last_updated: 2026-01-19T15:48:02Z
---

# CustomComponentAPI

`Version: 1.0.0` | _stable_

Custom components are small, self-contained elements of code that can be used and re-used when building widgets. Custom components contains the following elements: definition (QEXT) file, main JavaScript file and optional assets such as JavaScript libraries, images, and fonts.

## Table of Contents

### Definitions

- [link](#linkscope-element-attrs-function)
- [component](#component-interface)
- [qext](#qext-interface)

## Definitions

### link(scope, element, attrs) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | object | Yes | - |  |
| `element` | $Element | Yes | - |  |
| `attrs` | object | Yes | - |  |

---

### component `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `componentName` | string | Yes | - | The name of the component |
| `restrict` | string | Yes | - |  |
| `link` | [link](#linkscope-element-attrs-function) | Yes | - |  |

---

### qext `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | The name of the custom component. |
| `description` | string | Yes | - | Provides a meaningful description of your custom component. |
| `type` | string | Yes | - | Extension type. Should always be `'component'` for custom components. |
| `version` | string | Yes | - | Version of your custom component. Uses the semantic version concept. |
| `author` | string | No | - | Author of the custom component. |

---
