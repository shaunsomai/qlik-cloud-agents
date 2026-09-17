---
source: https://qlik.dev/apis/javascript/app-integration/
last_updated: 2026-01-19T15:48:02Z
---

# App Integration

`Version: 1.1.1` | _stable_

The App Integration API provides parameters that can be used to create a URL that returns a complete HTML page containing the embedded app. This URL can be embedded in a web page, for example by including it in an iFrame. Consider using the qlik-embed toolkit with the classic/app or analytics/sheet UI instead to mitigate for third-party cookie blocking issues in modern browsers.

## Table of Contents

### Definitions

- [URL](#url-interface)

## Definitions

### URL `interface`

#### Returns

`string` - HTML page rendering a Qlik Sense visualization or a sheet.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appid` | string | Yes | - | App ID of the referenced app. |
| `sheetid` | string | Yes | - | Sheet ID of the referenced sheet. |
| `bookmark` | string | No | - | You add a bookmark definition by stating the bookmark ID in addition to the Base URL. |
| `options` | object | No | - | Add option definitions in addition to the Base URL. |
| `select` | string | No | - | Selection definitions can be added to the Base URL. Selections can be made in a single field or in multiple fields. Multiple values are separated by a semicolon. |
| `theme` | string | No | - | Add a theme definition by stating the theme ID in addition to the Base URL. Introduced in Qlik Sense 4.0 |
| `language` | string | No | - | Override default language settings by defining the language. |

<details>
<summary>Properties of `options`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `clearselections` | string | No | - | clearselections - Clears all selections made in the app before applying bookmarks and selections. |
| `developer` | string | No | - | **[experimental]** developer - enables developer mode in qlik-sense. |

</details>

<details>
<summary>Examples</summary>

**Add a bookmark definition by stating the bookmark ID in addition to the Base URL**
```
http[s]://<machinename | servername>/{virtual proxy}/sense/app/{appid}/sheet/{sheetid}/state/analysis/bookmark/{bookmarkid}
```

**Add option definitions in addition to the Base URL**
```
http[s]://<machinename | servername>/{virtual proxy}/sense/app/{appid}/sheet/{sheetid}/state/analysis/options/{option}
```

**Selection in single field that has text representation of numeric values:**
```
http[s]://<machinename | servername>/{virtual proxy}/sense/app/{appid}/sheet/{sheetid}/state/analysis/select/{field}/{[value1];[value2]}
```

**Selections in multiple fields:**
```
http[s]://<machinename | servername>/{virtual proxy}/sense/app/{appid}/sheet/{sheetid}/state/analysis/select/{field}/{value1;value2}/select/{field2}/{value1;value2}
```

**Applying a theme:**
```
http[s]://<machinename | servername>/{virtual proxy}/sense/app/{appid}/sheet/{sheetid}/theme/{themeid}
```

</details>

---
