---
source: https://qlik.dev/apis/javascript/sn-nav-menu/
last_updated: 2026-02-20T08:58:43Z
---

# Nebula Navigation menu

`Version: 0.14.1` | _stable_

Navigation menu generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [Component](#component-object)
- [ContentStyling](#contentstyling-object)
- [DrawerButtonStyling](#drawerbuttonstyling-object)
- [FontStyle](#fontstyle-object)
- [PaletteColor](#palettecolor-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `components` | [Component](#component-object)[] | Yes | - | Holds general styling |
| `disableNavMenu` | boolean | No | true | Disable hover menu toggle |
| `footnote` | string \| StringExpression | No | "" | Visualization footnote |
| `layoutOptions` | object | Yes | - | Layout settings. |
| `showDetails` | boolean | No | false | Show visualization details toggle |
| `showTitles` | boolean | No | false | Show title for the visualization |
| `subtitle` | string \| StringExpression | No | "" | Visualization subtitle |
| `title` | string \| StringExpression | No | "" | Visualization title |
| `version` | string | Yes | - | Current version of this generic object definition |

<details>
<summary>Properties of `layoutOptions`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `alignment` | 'top-left' \| 'top-center' \| 'top-right' \| 'center-left' \| 'center-center' \| 'center-right' \| 'bottom-left' \| 'bottom-center' \| 'bottom-right' | No | - | The alignment of the menu in the object viewport in both directions(horizontal and vertical) |
| `dividerColor` | [PaletteColor](#palettecolor-object) | No | - | Divider color settings. |
| `drawerMode` | boolean | No | false | If set to true, the navigation menu is displayed as a button, and the `orientation` and `layout` properties will be ignored. If set to false, the navigation menu is displayed as a menu, and the `showDrawerIcon` property will be ignored. |
| `drawerPanelPosition` | 'left' \| 'right' | No | "left" | The position of the drawer panel. If set to `left`, the drawer panel is anchored to the left, if set to `right`, the drawer panel is anchored to the right |
| `largeItems` | boolean | No | false | If set to true, menu items have a bigger padding top and bottom. |
| `layout` | 'fill' \| 'minimal' | No | - | The space layout of the menu. If set to `fill`, menu items use all space in horizontal direction, if set to `minimal`, menu items use minimum space in horizontal direction. |
| `orientation` | 'vertical' \| 'horizontal' | No | - | The orientation of the menu. If set to `vertical`, menu items are displayed vertically, if set to `horizontal`, menu items are displayed horizontally |
| `sameItemWidth` | boolean | No | true | This is only valid if `orientation` property is set to `horizontal`. If set to true, all items have the same width. |
| `separateItems` | boolean | No | false | If set to true, a space of 8px is displayed between two menu items. |
| `showDrawerIcon` | boolean | No | true | If set to true, the drawer icon is displayed. |
| `showItemIcons` | boolean | No | false | If set to true, an icon is displayed to the left of a menu item. |
| `useDivider` | boolean | No | false | If set to true, a divider is displayed between two menu items. |

</details>

---

## Definitions

### Component `object`

General styling for navigation menu.
If any property is not set, default values specific for each property is used.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | This should be set to `theme` |
| `content` | [ContentStyling](#contentstyling-object) | No | - |  |

---

### ContentStyling `object`

Holds properties for font family, font size, font color and hover styling.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fontFamily` | string | Yes | - | Defaults to `Source Sans Pro, sans serif` |
| `fontSize` | string | Yes | - | Defaults to `12px` |
| `fontStyle` | [FontStyle](#fontstyle-object) | Yes | - |  |
| `borderColor` | [PaletteColor](#palettecolor-object) | No | - |  |
| `borderRadius` | string | No | - |  |
| `borderWidth` | string | No | - |  |
| `boxShadow` | string | No | - |  |
| `boxShadowColor` | [PaletteColor](#palettecolor-object) | No | - |  |
| `defaultColor` | [PaletteColor](#palettecolor-object) | No | - | Menu item color, defaults to `white` |
| `defaultFontColor` | [PaletteColor](#palettecolor-object) | No | - | Defaults to `#404040` |
| `drawerButton` | [DrawerButtonStyling](#drawerbuttonstyling-object) | No | - |  |
| `highlightColor` | [PaletteColor](#palettecolor-object) | No | - | Color when a menu item is highlighted, defaults to `white` |
| `highlightFontColor` | [PaletteColor](#palettecolor-object) | No | - | Defaults to `#404040` |
| `hoverColor` | [PaletteColor](#palettecolor-object) | No | - | Color when a menu item is hovered, defaults to `#d3d3d3` |
| `hoverFontColor` | [PaletteColor](#palettecolor-object) | No | - | Defaults to `#404040` |

---

### DrawerButtonStyling `object`

Holds properties for drawer button styling.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `defaultColor` | [PaletteColor](#palettecolor-object) | No | - | Drawer button color, defaults to `white` |
| `hoverColor` | [PaletteColor](#palettecolor-object) | No | - | Color when a drawer button is hovered, defaults to `white` |

---

### FontStyle `object`

Font style

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bold` | boolean | Yes | - | Default to false |
| `italic` | boolean | Yes | - | Default to false |
| `normal` | boolean | Yes | - | Default to true |
| `underline` | boolean | Yes | - | Default to false |

---

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |
| `alpha` | number | No | - | Transparency value, default to 1 |

---
