---
source: https://qlik.dev/apis/javascript/single-integration/
last_updated: 2026-09-11T16:13:57Z
---

# Single Integrations

`Version: 1.2.2` | _stable_

The Single Integration API provides parameters that can be used to create a URL that returns a complete HTML page containing, for example, an embedded Qlik Sense visualization. This URL can be embedded in a web page by including it in an iFrame. Consider using the qlik-embed toolkit with the classic/chart or analytics/chart UI instead to mitigate for third-party cookie blocking issues in modern browsers.

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
| `appid` | string | Yes | - | ID of a Qlik Sense app. If no `appid` is available, the file name will be listed. |
| `obj` | string | Yes | - | ID of a Qlik Sense visualization. |
| `sheet` | string | Yes | - | ID of a sheet in a Qlik Sense app. |
| `snapshot` | string | Yes | - | ID of a snapshot in a Qlik Sense app. Introduced in Qlik Sense 1.1. |
| `identity` | string | No | - | Session identity. If no identity is defined, the session and selection state will be shared with the client. If an identity is defined, a separate session is created and any selections made in the single feature do not affect a concurrent session in the Qlik Sense client. |
| `lang` | string | No | - | Override default language settings by defining the language for the specific object. Accepts a short or long locale code (case-insensitive). If omitted or unsupported, falls back to English (`en`/`en-US`). Supported languages: German (`de`/`de-DE`), English (`en`/`en-US`), Spanish (`es`/`es-ES`), French (`fr`/`fr-FR`), Italian (`it`/`it-IT`), Japanese (`ja`/`ja-JP`), Korean (`ko`/`ko-KR`), Dutch (`nl`/`nl-NL`), Polish (`pl`/`pl-PL`), Brazilian Portuguese (`pt`/`pt-BR`), Russian (`ru`/`ru-RU`), Swedish (`sv`/`sv-SE`), Turkish (`tr`/`tr-TR`), Simplified Chinese (`zh-CN`), Traditional Chinese (`zh-TW`). |
| `opt` | object | No | - | Defining options. Multiple options can be combined in a single comma-separated value. Supported options are: |
| `callback` | string | No | - | Registers a JavaScript callback object exposed on `window` under the name given by `callback`. The object can define: `onValid(objectId)`, called when the object becomes valid; `onRendered(objectId)`, called after the object has rendered; and `onError(code, message)`, called if an error occurs. |
| `bookmark` | string | No | - | ID of a bookmark in a Qlik Sense app. Introduced in Qlik Sense 1.1. |
| `select` | string | No | - | Field name and values to select, or a clear-selection instruction. Introduced in Qlik Sense 1.1. Multiple `select` parameters can be defined, one per field. To select in a specific alternate state, prefix the field name with the state name and `::`. To clear every selection in all states, use `select=clearall`. To clear selections in a single state, use `select=<state>::clearall` (the default state is named `$`). |
| `theme` | string | No | - | Add a theme definition by stating the theme ID in addition to the Base URL. Introduced in Qlik Sense 4.0. |

<details>
<summary>Properties of `opt`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `currsel` | string | No | - | displays the Selection bar. |
| `currsel-dark` | string | No | - | displays the Selection bar dark mode. |
| `debug` | string | No | - | starts a JavaScript debugger. The debug option can only be defined in the URL. |
| `noanimate` | string | No | - | turns off animations. |
| `noselections` | string | No | - | turns off selections. |
| `nointeraction` | string | No | - | turns off interaction. |
| `ctxmenu` | string | No | - | enables the context menu. |

</details>

<details>
<summary>Examples</summary>

**Defining multiple preselected values:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&select=Priority,High,Medium&select=Year,2012' frameborder='0'>
```

**Defining preselected values and bookmarks:**
```
http[s]://<machinename | servername>/{virtual proxy}/single?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&
```

**Overriding the display language:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&lang=fr-FR' frameborder='0'>
```

**Combining display options:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&opt=currsel,noanimate' frameborder='0'>
```

**Selecting in a specific alternate state:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&select=MyState::Region,North' frameborder='0'>
```

**Clearing all selections:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&select=clearall' frameborder='0'>
```

**Clearing selections in the default state:**
```html
<iframe src='https://sense-demo.qlik.com/single/?appid=133dab5d-8f56-4d40-b3e0-a6b401391bde&obj=298bbd6d-f23d-4469-94a2-df243d680e0c&select=$::clearall' frameborder='0'>
```

</details>

---
