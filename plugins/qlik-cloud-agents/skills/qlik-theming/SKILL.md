---
name: qlik-theming
version: "1.1.0"
description: Build, install and apply a custom Qlik Sense theme — the theme.json schema, data palettes and colour scales, chart chrome, where theme folders go on Desktop and Cloud, and the registration step that silently stops a theme applying. Load this whenever choosing chart colours for a Qlik app, creating or editing a theme, copying a built-in theme to customise, or when an applied theme has no visible effect. External palette validators are optional.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, ToolSearch
license: MIT
---

# Qlik theming

A Qlik theme is an extension: a folder holding a `.qext` manifest and a `theme.json`. It sets the data palettes, the colour scales, and the chart chrome — fonts, axis, gridlines, legend, per-chart-type label colours.

## Palette and platform procedure

Choose categorical colours for entities, sequential lightness for magnitudes, and diverging scales around meaningful midpoints. Check contrast, distinguishability and colour-vision simulations on the actual chart background. Pair status colours with labels or symbols. External validators are optional and not bundled; do not claim automated validation without running it.

Write the theme and matching .qext, install/register it and verify visually. Applying it changes an app and requires the existing APPROVED: protocol. Assets are bundled in assets/themes. Tool examples below describe Desktop only; on Cloud discover actual connector capabilities or use the supported management UI. Inspect server-qualified names and confirm the target app when both plugins are installed.

## theme.json schema

```json
{
  "_variables": { "@ink-primary": "#0b0b0b", "@gridline": "#e1e0d9" },
  "backgroundColor": "#ffffff",
  "fontFamily": "Source Sans Pro, system-ui, sans-serif",
  "fontSize": "13px",
  "color": "@ink-primary",

  "dataColors": {
    "primaryColor": "#2a78d6",
    "othersColor":  "#898781",
    "nullColor":    "#e1e0d9",
    "errorColor":   "#d03b3b"
  },

  "palettes": {
    "data": [
      { "name": "My 8", "type": "row", "scale": ["#2a78d6", "#eb6834", "..."] }
    ],
    "ui": [ { "name": "Palette", "colors": ["#ffffff", "#2a78d6", "..."] } ]
  },

  "scales": [
    { "name": "Magnitude", "type": "gradient", "propertyValue": "magnitude",
      "scale": ["#cde2fb", "#3987e5", "#0d366b"] },
    { "name": "Variance",  "type": "class",    "propertyValue": "variance",
      "scale": ["#d03b3b", "#f0efec", "#2a78d6"] }
  ],

  "object": {
    "axis":   { "label": { "name": { "color": "@ink-primary" } },
                "line": { "major": { "color": "@gridline" } } },
    "grid":   { "line": { "major": { "color": "@gridline" } } },
    "legend": { "label": { "color": "@ink-primary" } },
    "title":  { "main": { "color": "@ink-primary", "fontSize": "15px" } }
  }
}
```

| Section | Notes |
|---|---|
| `_variables` | Named tokens usable anywhere a value goes — the theme equivalent of CSS custom properties. Define ink, surface and gridline once. |
| `palettes.data` | Categorical palettes in the colour picker. **Use `type: "row"`.** |
| `palettes.ui` | Swatches in the manual colour picker. |
| `scales` | `type: "gradient"` interpolates; `type: "class"` gives discrete bands. Give each a unique `propertyValue`. |
| `dataColors.primaryColor` | The single-series default — what a one-measure bar chart uses. Set it to categorical slot 1. |
| `dataColors.othersColor` | The colour of the folded tail. Make it a neutral grey so "Other" never looks like a category. |
| `object` | Per-chart chrome. Keys include `axis`, `grid`, `legend`, `label`, `title`, `referenceLine`, plus `barChart`, `lineChart`, `comboChart`, `scatterPlot`, `treemap`, `pieChart`, `gauge`, `kpi`, `straightTable`, `pivotTable`, `listBox`, `boxPlot`, `histogram`, `waterfallChart`, `distributionPlot`, `bulletChart`, `mapChart`. |

### `row` versus `pyramid` — this one matters

Qlik's built-in "12 Colors" is `type: "pyramid"`: a nested list indexed by series count, so three series get one set of hues and four get a *different* set. A filter that drops a series therefore repaints the survivors, and colour stops identifying an entity.

**Always use `type: "row"`** in a custom theme — a flat list assigned in fixed order.

## Installing

**Desktop.** Copy the folder into an Extensions directory:

```
C:\Qlik\Sense\Extensions\<theme-id>\
%USERPROFILE%\Documents\Qlik\Sense\Extensions\<theme-id>\
```

The folder name, the `.qext` filename and the theme id must all match: `my-theme/my-theme.qext`.

**Then restart Qlik Sense Desktop.** This is not optional and it is the single most common reason a theme "doesn't work". Desktop builds its extension registry when the Web Extension Service starts. A folder dropped in afterwards is served over HTTP — `/extensions/my-theme/theme.json` returns 200 — but it is not registered, so the client silently falls back to the default. Check with:

```bash
curl http://localhost:4848/api/wes/v1/extensions      # "data": [] means nothing registered
```

`qlik_list_themes` reports this per theme as `registered: true/false` and warns when a theme is installed but unregistered. Check it before concluding a theme is broken.

**Qlik Cloud.** Zip the folder and upload under Management Console → Themes.

## Applying a theme

```
qlik_list_themes(app?)            # built-ins + custom, with registration status
qlik_set_app_theme(app, theme)    # sets the app's theme property and saves
```

`qlik_set_app_theme` refuses an unknown id unless you pass `confirm: true`, and warns when the target is unregistered or missing `theme.json`. Pass an empty theme to clear back to the client default. `qlik_describe_app` reports the current theme.

After applying, **refresh the browser (F5)** — the client caches theme properties.

Built-in ids: `sense`, `card`, `breeze`, `horizon`.

## Copying a built-in to customise

The four shipped themes are readable on disk and are the best starting point:

```
%LOCALAPPDATA%\Programs\Qlik\Sense\Client\assets\external\sense-themes-default\
    sense\  card\  breeze\  horizon\
```

`sense/theme.json` is the most complete example of the `object` section. Copy one, rename the folder, write a matching `.qext`, then replace the palette and scales.

Do not assume a built-in is a good colour source. Measured against white, Qlik's default (the Paul Tol scheme) fails the lightness band and chroma floor and has one pair below the normal-vision separation floor; `horizon` has seven of eight hues below the chroma floor. They are brand palettes, not working data palettes. Validate before adopting.

## The `.qext` manifest

```json
{
  "name": "My Theme",
  "description": "What it is for.",
  "type": "theme",
  "version": "1.0.0",
  "author": "You"
}
```

`"type": "theme"` is what makes it a theme rather than a visualisation extension.

## Limits worth stating rather than discovering

- **Dark mode.** All four built-ins are light and Desktop renders on white. A dark theme needs its own steps validated against a dark surface — never an automatic inversion of light values.
- **Status colours.** There is no theme slot for good/warning/critical; those live in per-chart colour expressions. Keep them distinct from the series hues so a status colour never impersonates a series, and always pair them with an icon or label.
- **A theme cannot fix a chart.** It sets colours, not encodings. A combo chart with a currency and a percentage on one axis is broken whatever palette it wears — that is a second axis or a second chart, not a colour problem.
