# Themes

Qlik Sense themes are extensions: a folder holding a `.qext` manifest (`"type": "theme"`) and a `theme.json`. They control the data palettes, the colour scales, and the chart chrome — fonts, axis, gridlines, legend, per-chart-type label colours.

## Installing

**Desktop** — copy the theme folder into your Extensions directory (`C:\Qlik\Sense\Extensions\` or `%USERPROFILE%\Documents\Qlik\Sense\Extensions\`), then **restart Qlik Sense Desktop**. The restart is not optional: Desktop builds its extension registry when the Web Extension Service starts, so a folder dropped in afterwards serves over HTTP but never appears in the theme list. You can confirm registration with:

```
curl http://localhost:4848/api/wes/v1/extensions
```

An empty `"data": []` means nothing is registered yet.

**Qlik Cloud** — zip the folder and upload it under Management Console → Themes.

Then pick it per app in *App options → Appearance → App theme*, or set the app's `theme` property to the folder name via the Engine API.

## What Qlik gives you

| Section | Purpose |
|---|---|
| `palettes.data` | Categorical palettes offered in the colour picker. `type: "row"` is a fixed list; `type: "pyramid"` is a nested list indexed by series count. |
| `palettes.ui` | The swatches in the manual colour picker. |
| `scales` | Named sequential/diverging scales. `type: "gradient"` interpolates; `type: "class"` gives discrete bands. |
| `dataColors` | `primaryColor` (single-series default), `othersColor`, `nullColor`, `errorColor`. |
| `object` | Per-chart-type chrome: `axis`, `grid`, `legend`, `label`, `title`, plus `barChart`, `lineChart`, `treemap`, `pivotTable`, `listBox` and the rest. |
| `_variables` | Named tokens (`@ink-primary`) reusable anywhere a value is expected — the theme equivalent of CSS custom properties. |

**Use `row`, not `pyramid`.** Qlik's built-in "12 Colors" is a pyramid: with three series you get one set of hues, with four you get a different set. That means a filter which changes the series count repaints the survivors, so a colour stops identifying an entity. A `row` palette assigns hues in fixed order and never re-assigns them.

## Copying and customising a built-in

The four shipped themes are readable on disk — a good starting point:

```
%LOCALAPPDATA%\Programs\Qlik\Sense\Client\assets\external\sense-themes-default\
    sense\    card\    breeze\    horizon\
```

Copy one to your Extensions folder, rename the folder, add a matching `.qext`, and edit. `sense/theme.json` is the most complete reference for the `object` section.

## sales-demo-theme

Built for the Sales Demo app and validated rather than eyeballed. See [THEME-NOTES.md](THEME-NOTES.md) for the validator output, the reasoning, and the documented limits — in particular the three-slot cap for treemaps and scatter plots.
