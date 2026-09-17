---
source: https://qlik.dev/apis/javascript/sn-action-button/
last_updated: 2026-04-23T17:22:43+01:00
---

# Nebula Button

`Version: 2.3.0` | _stable_

Action button generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [Action](#action-object)
- [NavigationAction](#navigationaction-object)
- [Style](#style-object)
- [Font](#font-object)
- [Background](#background-object)
- [Border](#border-object)
- [Icon](#icon-object)
- [PaletteColor](#palettecolor-object)
- [ColorExpression](#colorexpression-object)
- [EnabledExpression](#enabledexpression-object)

## Entries

### properties `object`

extends `EngineAPI.GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition. |
| `showTitles` | boolean | No | false | Show title for the visualization |
| `title` | string | No | "" | Visualization title |
| `subtitle` | string | No | "" | Visualization subtitle |
| `footnote` | string | No | "" | Visualization footnote |
| `useEnabledCondition` | boolean | Yes | false | Controlling if the button should use an expression to determine if it is enabled or not |
| `enabledCondition` | number \| [EnabledExpression](#enabledexpression-object) | Yes | 1 | Number or expression evaluating to number, 0 means disabling the button |
| `actions` | [Action](#action-object)[] | Yes | - | List of actions, performed in this order |
| `runtimeExpressionEvaluation` | false | Yes | - | Boolean to determine the parallel evaluation of expression. Set to true if you want the expression to be evaluated between the actions (instead of upfront). |
| `navigation` | [NavigationAction](#navigationaction-object) | Yes | - | Navigation action to move to new sheet/URL, performed after all other actions |
| `style` | [Style](#style-object) | Yes | - | All styling options |

---

## Definitions

### Action `object`

Defines what action to perform and options for that action type.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `actionLabel` | string | No | "" | Label for reference |
| `actionType` | 'applyBookmark' \| 'back' \| 'forward' \| 'clearAll' \| 'clearAllButThis' \| 'clearField' \| 'selectAll' \| 'selectValues' \| 'selectMatchingValues' \| 'selectAlternative' \| 'selectExcluded' \| 'selectPossible' \| 'toggleSelect' \| 'lockAll' \| 'lockField' \| 'unlockAll' \| 'unlockField' \| 'setVariable' \| 'doReload' \| 'executeAutomation' \| 'refreshDynamicViews' | No | "" | The type of action |
| `bookmark` | string | No | "" | ID of bookmark, required for type 'applyBookmark' |
| `field` | string | No | "" | Name of field. Required for types 'clearAllButThis', 'clearField', 'selectAll', 'selectValues', 'selectMatchingValues', 'selectAlternative', 'selectExcluded', 'selectPossible', 'toggleSelect', 'lockField' and 'unlockField' |
| `softLock` | string | No | "" | Set to true to ignore locked field(s). Required for types 'clearAll', 'clearAllButThis', 'clearField', 'selectAll', 'selectValues', 'selectMatchingValues', 'selectAlternative', 'selectExcluded', 'selectPossible' and 'toggleSelect' |
| `value` | string | No | "" | To select certain values in a field or set a variable. Required for types 'selectValues', 'selectMatchingValues', 'toggleSelect' and 'setVariable' |
| `variable` | string | No | "" | Name of variable. Required for type 'setVariable' |
| `partial` | boolean | No | false | Set to true if you want to do a partial reload. |
| `automation` | string | No | "" | Item ID of the automation (the id field returned from /api/v1/items?resourceType=automations) |
| `automationId` | string | No | "" | ID of the automation (the id field from /api/v1/automations OR the id field from /api/v1/automations) |
| `automationPostData` | boolean | No | false | Set to true to include the current selections in the automation. Defaults to false |
| `automationTriggered` | boolean | No | false | Set to true when the automation should use the triggered run mode. Defaults to false |
| `automationTriggeredText` | string | No | "" | Helper text when using the triggered run mode. Defaults to false |
| `automationExecutionToken` | string | No | "" | Token used when using the triggered run mode |
| `automationShowNotification` | boolean | No | false | Set to true when an automation should return a notification when finished running. Defaults to false |
| `automationNotificationDuration` | string | No | "" | The amount of time in seconds that a notification should remain visible after running an automation |
| `automationNotificationDurationHelp` | string | No | "" | Helper text when enabling notifications |
| `automationOpenLinkSameWindow` | boolean | No | false | Set to true if you want links from notifications to be opened in the same tab |

---

### NavigationAction `object`

Defines a navigation action to perform after the other actions. Note that when the sn-action-button is used outside Qlik Sense you can only use the 'openWebsite' action.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `action` | 'nextSheet' \| 'prevSheet' \| 'firstSheet' \| 'lastSheet' \| 'goToSheet' \| 'goToSheetById' \| 'goToSheetById' \| 'goToStory' \| 'openWebsite' \| 'odagLink' \| 'openChainedApp' | Yes | - | Name of navigation action |
| `appId` | string | No | - | app ID. Required for 'openChainedApp' |
| `sheet` | string | No | - | sheet ID. Required for 'goToSheet' and 'goToSheetById' |
| `chartId` | string | No | - | chart ID. Required for 'goToSheet' and highlighting the chart |
| `story` | string | No | - | Story ID. Required for 'goToStory' |
| `websiteUrl` | string | No | - | URL for website. required for 'openWebsite' |
| `sameWindow` | boolean | No | - | Set to true to open in same window/tab. Required for 'openWebsite' |
| `odagLink` | string | No | - | ODAG link name. Required for 'odagLink' |

---

### Style `object`

Holds styling options

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | No | "Button" | The text displayed on the button |
| `showLabel` | boolean | No | true | If the label should be shown or hidden |
| `font` | [Font](#font-object) | No | - | Styling for the label |
| `background` | [Background](#background-object) | No | - | Styling for background, including image |
| `border` | [Border](#border-object) | No | - | Styling for border |
| `icon` | [Icon](#icon-object) | No | - | Styling for icon |

---

### Font `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontFamily` | string | No | "Source Sans Pro" | Font Family of the label |
| `useColorExpression` | boolean | No | false | Set to true to use color expression |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if useColorExpression is false |
| `colorExpression` | [ColorExpression](#colorexpression-object) | No | - | Color defined by expression, needed if useColorExpression is true |
| `size` | number | No | 0.5 | Relative[] size of label, must be greater than 0 and 1 fills the entire button |
| `sizeFixed` | number | No | 20 | Fixed size of the label in pixels. Must be bigger than 5. Only active when sizeBehavior is fixed. |
| `align` | 'left' \| 'center' \| 'right' | No | "center" | Horizontal alignment |
| `style` | object | No | - | Additional style options |
| `sizeBehavior` | 'responsive' \| 'relative' \| 'fixed' | No | "responsive" | Setting to determine how the fontsize of the label is calculated. |

<details>
<summary>Properties of `style`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bold` | boolean | No | true | Bold text |
| `italic` | boolean | No | false | Italic text |
| `underline` | boolean | No | false | Underlined text |

</details>

---

### Background `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useColorExpression` | boolean | No | false | Set to true to use color expression |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if useColorExpression is false |
| `colorExpression` | [ColorExpression](#colorexpression-object) | No | - | Color defined by expression, needed if useColorExpression is true |
| `mode` | 'none' \| 'media' | No | "none" | Toggles the background image, set to media to show the image |
| `useImage` | boolean | No | false | Set to true to show background image |
| `url` | object | No | - | Contains the URL for the background image |
| `position` | 'topLeft' \| 'centerLeft' \| 'bottomLeft' \| 'topCenter' \| 'centerCenter' \| 'bottomCenter' \| 'topRight' \| 'centerRight' \| 'bottomRight' \| 'top-left' \| 'center-left' \| 'bottom-left' \| 'top-center' \| 'center-center' \| 'top-right' \| 'center-right' \| 'bottom-right' | No | "center-center" | Image position |
| `size` | 'auto' \| 'alwaysFit' \| 'fitWidth' \| 'fitHeight' \| 'fill' \| 'alwaysFill' \| 'stretchFit' | No | "auto" | Size of the image, relative to the button |

<details>
<summary>Properties of `url`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStaticContentUrlDef` | object | No | - |  |

<details>
<summary>Properties of `qStaticContentUrlDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | No | - | URL represented as a string |

</details>

</details>

---

### Border `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useBorder` | boolean | No | false | Set to true to use border expression |
| `width` | number | No | 0 | Relative width, 0 is no border and 1 make the border fill the entire button |
| `radius` | number | No | 0 | Relative border radius, 0 is no rounding and 1 will make the short side a half circle |
| `useColorExpression` | boolean | No | false | Set to true to use color expression |
| `color` | [PaletteColor](#palettecolor-object) | No | - | Color defined by index or hex code, needed if useColorExpression is false |
| `colorExpression` | string | No | - | Color defined by expression, needed if useColorExpression is true |

---

### Icon `object`

Icons are only available inside Qlik Sense

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `useIcon` | boolean | No | false | Set to true to show icon, default is false |
| `iconType` | object | No | - | holds the name of the icon |
| `position` | 'left' \| 'right' | No | "left" | Defines which side of the label the icon will be |

<details>
<summary>Properties of `iconType`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | string | No | "" | name of icon |

</details>

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

### EnabledExpression `object`

Format for setting if the button is enabled/disabled with an expression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStringExpression` | object | Yes | - |  |

<details>
<summary>Properties of `qStringExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - | expression that resolves to a number |

</details>

---
