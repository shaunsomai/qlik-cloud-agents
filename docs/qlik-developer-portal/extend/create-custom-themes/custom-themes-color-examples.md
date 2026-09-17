---
source: https://qlik.dev/extend/create-custom-themes/custom-themes-color-examples/
last_updated: 2026-06-02T18:15:45+01:00
---

# Create custom color palettes and color scales

These examples show how to create color palettes and color scales for your custom
themes. All properties referenced in the examples below are described in detail in
[Custom theme JSON properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/themes-properties/).

## What is being used where?

The color palettes and color scales you define are being used in different
places in Qlik Sense.

### Sheet title styling

Sheet title styling objects

| Object           | Colors defined in         |
| ---------------- | ------------------------- |
| Background color | `"palettes": {"ui": [0]}` |
| Font color       | `"palettes": {"ui": [0]}` |

### Properties panel

Properties panel objects

| Object       | Colors defined in                                                                                                                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto         | `"palettes": {"data": [ 0 ]}`That is, the first palette defined in data.> **Note:** Charts set to `color="auto"` use the `primaryColor` when only one color is used, for example, in one-dimensional bar charts. Charts with more colors use the first palette defined in data, for example, in pie charts or multi-dimensional bar charts. |
| Single color | `"palettes": {"ui": [ 0 ]}`                                                                                                                                                                                                                                                                                                                 |
| By Dimension | `"palettes": {"data": [...]}`                                                                                                                                                                                                                                                                                                               |
| By Measure   | `"scales": [{...}]`                                                                                                                                                                                                                                                                                                                         |

### Master items

Master item objects

| Object                 | Colors defined in         |
| ---------------------- | ------------------------- |
| Measure color          | `"palettes": {"ui": [0]}` |
| Dimension color        | `"palettes": {"ui": [0]}` |
| Dimension value colors | `"palettes": {"ui": [0]}` |

### Storytelling

Storytelling objects

| Object                 | Colors defined in         |
| ---------------------- | ------------------------- |
| Shape background color | `"palettes": {"ui": [0]}` |

## Defining the color palettes (data, ui)

The colors defined in the `data` palette are used for `Color by dimension` in the
properties panel.

Though you can define several palettes in `ui`, the first palette defined here is
used in the color picker for example when coloring by single color.

> **Note:** Colors should be defined using hexadecimal values.

```json
"palettes" : {
  "data" : [
    {
      "name": "Dark colors",
      "translation": "Dark colors",
      "propertyValue": "12",
      "type": "row",
      "scale": [
        "#808080",
        "#737373",
        "#666666",
        "#595959",
        "#4D4D4D",
        "#474747",
        "#404040",
        "#333333",
        "#262626",
        "#1A1A1A",
        "#0D0D0D",
        "#000000"
      ]
    },
    {
      "name": "Light colors",
      "translation": "Light colors",
      "propertyValue": "11",
      "type": "row",
      "scale": [
        "#FFFFFF",
        "#FBFBFB",
        "#F2F2F2",
        "#E6E6E6",
        "#D9D9D9",
        "#CCCCCC",
        "#BFBFBF",
        "#B3B3B3",
        "#A6A6A6",
        "#999999",
        "#8C8C8C"
      ]
    }
  ],
  "ui": [
    {
      "name": "Palette",
      "colors": [
        "#FFFFFF",
        "#FBFBFB",
        "#F2F2F2",
        "#D9D9D9",
        "#BFBFBF",
        "#A6A6A6",
        "#8C8C8C",
        "#808080",
        "#737373",
        "#595959",
        "#474747",
        "#404040",
        "#262626",
        "#0D0D0D",
        "#000000"
      ]
    }
  ]
}
```

## Defining the color scales

The color defined in the `scales` are used for `Color by measure` in the
properties panel.

If you define two colors in the scale property, Qlik Sense generates a color
scale between those colors.

> **Note:** Colors should be defined using hexadecimal values.

```json
"scales": [
  {
    "name": "Light colors sequential gradient",
    "translation": "Light colors sequential gradient",
    "type": "gradient",
    "propertyValue": "sg",
    "scale": [ "#8C8C8C", "#FBFBFB" ]
  },
  {
    "name": "Light colors sequential classes",
    "translation": "Light colors sequential classes",
    "propertyValue": "sc",
    "type": "class",
    "scale": [ "#8C8C8C", "#FBFBFB" ]
  },
  {
    "name": "Dark colors diverging gradient",
    "translation": "Dark colors diverging gradient",
    "propertyValue": "dg",
    "type": "gradient",
    "scale": [ "#737373", "#0D0D0D" ]
  },
  {
    "name": "Dark colors diverging classes",
    "translation": "Dark colors diverging classes",
    "propertyValue": "dc",
    "type": "class",
    "scale": [ "#737373", "#0D0D0D" ]
  }
]
```

## Full code example

<details>
  <summary>theme.json</summary>

  ```json
  {
    "_inherit": false,
    "_variables" : {
      "@grayscale-100" : "#FFFFFF",
      "@grayscale-98" : "#FBFBFB",
      "@grayscale-95" : "#F2F2F2",
      "@grayscale-90" : "#E6E6E6",
      "@grayscale-85" : "#D9D9D9",
      "@grayscale-80" : "#CCCCCC",
      "@grayscale-75" : "#BFBFBF",
      "@grayscale-70" : "#B3B3B3",
      "@grayscale-65" : "#A6A6A6",
      "@grayscale-60" : "#999999",
      "@grayscale-55" : "#8C8C8C",
      "@grayscale-50" : "#808080",
      "@grayscale-45" : "#737373",
      "@grayscale-40" : "#666666",
      "@grayscale-35" : "#595959",
      "@grayscale-30" : "#4D4D4D",
      "@grayscale-28" : "#474747",
      "@grayscale-25" : "#404040",
      "@grayscale-20" : "#333333",
      "@grayscale-15" : "#262626",
      "@grayscale-10" : "#1A1A1A",
      "@grayscale-5" : "#0D0D0D",
      "@grayscale-0" : "#000000",
      "@text" : "13px"
    },
    "color": "@grayscale-20",
    "fontSize": "@text",
    "backgroundColor": "@grayscale-95",
    "dataColors": {
      "primaryColor": "@grayscale-28",
      "othersColor": "@grayscale-55",
      "errorColor": "@grayscale-90",
      "nullColor": "@grayscale-85"
    },
    "palettes" : {
      "data" : [
        {
          "name": "Dark colors",
          "translation": "Dark colors",
          "propertyValue": "12",
          "type": "row",
          "scale": [
            "#808080",
            "#737373",
            "#666666",
            "#595959",
            "#4D4D4D",
            "#474747",
            "#404040",
            "#333333",
            "#262626",
            "#1A1A1A",
            "#0D0D0D",
            "#000000"
          ]
        },
        {
          "name": "Light colors",
          "translation": "Light colors",
          "propertyValue": "11",
          "type": "row",
          "scale": [
            "#FFFFFF",
            "#FBFBFB",
            "#F2F2F2",
            "#E6E6E6",
            "#D9D9D9",
            "#CCCCCC",
            "#BFBFBF",
            "#B3B3B3",
            "#A6A6A6",
            "#999999",
            "#8C8C8C"
          ]
        }
      ],
      "ui": [
        {
          "name": "Palette",
          "colors": [
            "#FFFFFF",
            "#FBFBFB",
            "#F2F2F2",
            "#D9D9D9",
            "#BFBFBF",
            "#A6A6A6",
            "#8C8C8C",
            "#808080",
            "#737373",
            "#595959",
            "#474747",
            "#404040",
            "#262626",
            "#0D0D0D",
            "#000000"
          ]
        }
      ]
    },
    "scales": [
      {
        "name": "Light colors sequential gradient",
        "translation": "Light colors sequential gradient",
        "type": "gradient",
        "propertyValue": "sg",
        "scale": [ "#8C8C8C", "#FBFBFB" ]
      },
      {
        "name": "Light colors sequential classes",
        "translation": "Light colors sequential classes",
        "propertyValue": "sc",
        "type": "class",
        "scale": [ "#8C8C8C", "#FBFBFB" ]
      },
      {
        "name": "Dark colors diverging gradient",
        "translation": "Dark colors diverging gradient",
        "propertyValue": "dg",
        "type": "gradient",
        "scale": [ "#737373", "#0D0D0D" ]
      },
      {
        "name": "Dark colors diverging classes",
        "translation": "Dark colors diverging classes",
        "propertyValue": "dc",
        "type": "class",
        "scale": [ "#737373", "#0D0D0D" ]
      }
    ]
  }
  ```
</details>
