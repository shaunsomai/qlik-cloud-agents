---
source: https://qlik.dev/extend/create-custom-themes/custom-themes-objects-extended-examples/
last_updated: 2026-06-02T18:15:45+01:00
---

# Extended object styling

These examples show how to apply extended styling to the individual Qlik Sense
chart types using custom themes. All properties referenced in the following example
are described in detail in [Custom theme JSON properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/themes-properties/).

## Object type specific styling overview

In addition to the chart type specific properties presented in Custom theme
JSON properties, you can also style titles and labels for the individual chart
types. If you do this, the chart type styling will override the styling
defined for all objects.

This example shows how the title object has been defined on object level and
also on chart type level for bar charts.

Example:

```json
"object" : {
  "title": {
    "main": {
      "color" : "@grayscale-40",
      "fontSize" : "20px"
    },
    "subTitle" : {
      "color" : "@grayscale-40",
      "fontSize" : "16px"
    },
    "footer" : {
      "color" : "@grayscale-15",
      "fontSize" : "@text",
      "backgroundColor" : "@grayscale-85"
    }
  },
  "barChart": {
    "title": {
      "main": {
        "color" : "@grayscale-35",
        "fontSize" : "22px"
      },
      "subTitle" : {
        "color" : "@grayscale-35",
        "fontSize" : "18px"
      },
      "footer" : {
        "color" : "@grayscale-35",
        "fontSize" : "14px",
        "backgroundColor" : "@grayscale-80"
      }
    },
    "outOfRange": {
      "color": "@grayscale-40"
    }
  }
}
```

## Bar chart specific styling

In this example, you'll define the out of range color for bar charts.

Example:

```json
"barChart": {
  "outOfRange": {
    "color": "@grayscale-40"
  }
}
```

## Boxplot specific styling

For boxplot charts, you can style the stroke colors for the whiskers, lines,
and boxes. In addition, you can also style the fill color for the boxes.

Example:

```json
"boxPlot": {
  "box": {
    "whisker": {
      "stroke": "@grayscale-35"
    },
    "line": {
      "stroke": "@grayscale-35"
    },
    "box": {
      "fill": "@grayscale-35",
      "stroke": "@grayscale-35"
    }
  }
}
```

## Distribution plot specific styling

You can style the fill color of the box for distribution plots.

Example:

```json
"distributionPlot": {
  "box": {
    "fill": "@grayscale-35"
  }
}
```

## Filter pane specific styling

The title is the only filterpane specific styling you can apply. Filterpanes
consist of list boxes, and the content of a filterpane is controlled by the
styling in the listBox object.

Example:

```json
"filterpane": {
  "title": {
    "main": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    }
  }
}
```

## KPI specific styling

There are no KPI specific properties for styling. This example shows how to
style the title of KPIs.

Example:

```json
"kpi": {
  "title": {
    "main": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    }
  }
}
```

## Gauge specific styling

There are no gauge specific properties for styling. This example shows how to
style the labels of gauges.

Example:

```json
"gauge": {
  "label": {
    "value": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    }
  }
}
```

## Histogram specific styling

There are no histogram specific properties for styling. This example shows how
to style the labels of histograms.

Example:

```json
"histogram": {
  "label": {
    "value": {
      "color": "@grayscale-35",
      "fontSize": "20px"
    }
  }
}
```

## Line chart specific styling

You can style the out of range colors for line charts.

Example:

```json
"lineChart": {
  "outOfRange": {
    "color": "@grayscale-40"
  }
}
```

## List box specific styling

You can style the title, content, and data colors of list boxes. This styling also controls the appearance of:

- Filter panes.
- List boxes in the selections tool.
- Searches of values in charts.

Example:

```json
"listBox": {
  "title": {
    "main": {
      "color": "@grayscale-40",
      "fontSize": "@text"
    }
  },
  "content": {
    "color": "@grayscale-35",
    "fontSize": "@text"
  },
  "dataColors": {
    "selected": "#0363ff",
    "alternative": "#a8c9ff",
    "excluded": "#ffaf03",
    "selectedExcluded": "#ffe58f",
    "possible": "#ffffff"
  }
}
```

## Map chart specific styling

For map charts, you can style the background color, labels, and legends.

Example:

```json
"mapChart": {
  "backgroundColor": "@light",
  "legend": {
    "title": {
      "color": "@grayscale-35"
    },
    "label": {
      "color": "@grayscale-35"
    }
  },
  "label": {
    "value": {
      "dark": {
        "color": "@grayscale-20"
      },
      "light": {
        "color": "@grayscale-70"
      },
      "fontSize": "@text"
    }
  }
}
```

## Pie chart specific styling

You can style the axis title and the labels for pie charts.

Example:

```json
"pieChart": {
  "axis": {
    "title": {
      "fontSize": "@text"
    }
  },
  "label": {
    "name": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    },
    "value": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    }
  }
}
```

## Pivot table specific styling

For pivot tables, you can style the headers and the content.

Example:

```json
"pivotTable": {
  "header" : {
    "fontSize" : "@text",
    "color": "@grayscale-35"
  },
  "content": {
    "fontSize": "@text",
    "color": "@grayscale-35"
  }
}
```

## Scatter plot specific styling

You can style the labels for scatter plots.

Example:

```json
"scatterPlot": {
  "label": {
    "value": {
      "color": "@grayscale-40",
      "fontSize": "@14px"
    }
  }
}
```

## Straight table specific styling

For the straight table object, you can customize styling at the dimension and measure levels.
You can also customize elements such as totals, null values, grid, and the hover menu.

The theme reference for `sn-table` visualizations is `straightTableV2`. Use this when
defining your theme.

Example:

```json
{
  "object": {
    "straightTableV2": {
      "dimension": {
        "label": {
          "name": {
            "fontFamily": "Verdana",
            "fontSize": "18px",
            "color": "#ccc",
            "backgroundColor": "#ff0000"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#000000",
            "backgroundColor": "orangered"
          }
        }
      },
      "measure": {
        "label": {
          "value": {
            "fontFamily": "Arial",
            "fontSize": "14px",
            "color": "#ccc",
            "backgroundColor": "#ff0099"
          }
        }
      },
      "total": {
        "label": {
          "value": {
            "fontFamily": "Tahoma",
            "fontSize": "24px",
            "color": "#fff",
            "backgroundColor": "#3399aa"
          }
        }
      },
      "null": {
        "label": {
          "value": {
            "color": "red",
            "backgroundColor": "#ccc"
          }
        }
      },
      "grid": {
        "borderColor": "purple",
        "divider": {
          "borderColor": "lime"
        },
        "hover": {
          "color": "orange",
          "backgroundColor": "black"
        }
      }
    }
  }
}
```

## Table specific styling

> **Note:** The straight table has replaced the table as the default table visualization.
> Consider upgrading existing tables to straight tables for improved capabilities
> and performance. For information about the straight table, see [straight table](embed/foundational-knowledge/visualizations/straight-table).

For the table, you can style the headers and the content.

Example:

```json
"table" : {
  "header" : {
    "fontSize" : "@text",
    "color": "@grayscale-60"
  },
  "content": {
    "fontSize": "@text",
    "color": "@grayscale-35"
  }
}
```

## Treemap specific styling

You can style the branches and the leaves for treemaps.

Example:

```json
"treemap": {
  "branch": {
    "backgroundColor": "@grayscale-70",
    "label": {
      "color": "@grayscale-35",
      "fontSize": "@text"
    }
  },
  "leaf": {
    "label": {
      "fontSize": "@text"
    }
  }
}
```

## Waterfall chart specific styling

For a waterfall chart, you can style labels, values, and shapes.

Example:

```json
"waterfallChart": {
  "label": {
    "value": {
      "fontSize": "20px"
    }
  },
  "value": {
    "color": {
      "default": "@grayscale-45",
      "dark": "@grayscale-20",
      "light": "@grayscale-70"
    }
  },
  "shape": {
    "positiveValue": {
      "fill": "@grayscale-70"
    },
    "negativeValue": {
      "fill": "@grayscale-45"
    },
    "subtotal": {
      "fill": "@grayscale-20"
    },
    "bridge": {
      "stroke": "@grayscale-35"
    }
  }
}
```

## Write table specific styling

For the write table, you can customize styling at the dimension and measure levels.
You can also customize elements such as editable columns, totals, null values, grid, and the hover menu.

> **Limitations:** The write table cannot be embedded using qlik-embed.
>
> The write table supports custom themes, but you cannot use custom themes to
> change colors that define cell statuses (orange, green, and blue).

Example:

```json
"writeTable": {
      "dimension": {
        "label": {
          "name": {
            "fontFamily": "Verdana",
            "fontSize": "18px",
            "color": "#ccc",
            "backgroundColor": "#ff0000"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#000000",
            "backgroundColor": "orangered"
          }
        }
      },
      "measure": {
        "label": {
          "value": {
            "fontFamily": "Arial",
            "fontSize": "14px",
            "color": "#ccc",
            "backgroundColor": "#ff0099"
          }
        }
      },
      "total": {
        "label": {
          "value": {
            "fontFamily": "Tahoma",
            "fontSize": "24px",
            "color": "#fff",
            "backgroundColor": "#3399aa"
          }
        }
      },
      "null": {
        "label": {
          "value": {
            "color": "red",
            "backgroundColor": "#ccc"
          }
        }
      },
      "grid": {
        "borderColor": "purple",
        "divider": {
          "borderColor": "lime"
        },
        "hover": {
          "color": "orange",
          "backgroundColor": "black"
        }
      },
      "editableColumn": {
        "label": {
          "value": {
            "color": "#5c4a00",
            "backgroundColor": "#fffbe6"
          }
        },
        "inputFieldBackground": "#fffbe6",
        "inputFieldHoverColor": "#fff3cc"
      }
    }
```

## Full code example

<details>
  <summary>Full example of theme.json</summary>

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
  "object" : {
    "title": {
      "main": {
        "color" : "@grayscale-40",
        "fontSize" : "20px"
      },
      "subTitle" : {
        "color" : "@grayscale-40",
        "fontSize" : "16px"
      },
      "footer" : {
        "color" : "@grayscale-15",
        "fontSize" : "@text",
        "backgroundColor" : "@grayscale-85"
      }
    },
    "label" : {
      "name" : {
        "color" : "@grayscale-35",
        "fontSize" : "@text"
      },
      "value" : {
        "color" : "@grayscale-35",
        "fontSize" : "@text"
      }
    },
    "axis" : {
      "title" : {
        "color" : "@grayscale-35",
        "fontSize" : "@text"
      },
      "label" : {
        "color" : "@grayscale-35",
        "fontSize" : "@text"
      },
      "line" : {
        "major" : {
          "color" : "@grayscale-20"
        },
        "minor" : {
          "color" : "@grayscale-40"
        }
      }
    },
    "grid" : {
      "line": {
        "highContrast": {
          "color": "#999999"
        },
        "major": {
          "color": "#CCCCCC"
        },
        "minor": {
          "color": "#E6E6E6"
        }
      }
    },
    "referenceLine": {
      "label": {
        "name": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      },
      "outOfBounds": {
        "color": "@grayscale-35",
        "backgroundColor": "@grayscale-35",
        "fontSize": "@text"
      }
    },
    "legend": {
      "title": {
        "fontSize": "@text",
        "color": "@grayscale-35"
      },
      "label": {
        "fontSize": "@text",
        "color": "@grayscale-35"
      }
    },
    "barChart": {
      "outOfRange": {
        "color": "@grayscale-40"
      }
    },
    "boxPlot": {
      "box": {
        "whisker": {
          "stroke": "@grayscale-35"
        },
        "line": {
          "stroke": "@grayscale-35"
        },
        "box": {
          "fill": "@grayscale-35",
          "stroke": "@grayscale-35"
        }
      }
    },
    "distributionPlot": {
      "box": {
        "fill": "@grayscale-35"
      }
    },
    "filterpane": {
      "title": {
        "main": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      }
    },
    "kpi": {
      "title": {
        "main": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      }
    },
    "gauge": {
      "label": {
        "value": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      }
    },
    "histogram": {
      "label": {
        "value": {
          "color": "@grayscale-35",
          "fontSize": "20px"
        }
      }
    },
    "lineChart": {
      "outOfRange": {
        "color": "@grayscale-40"
      }
    },
    "listBox": {
      "title": {
        "main": {
          "color": "@grayscale-40",
          "fontSize": "@text"
        }
      },
      "content": {
        "color": "@grayscale-35",
        "fontSize": "@text"
      },
      "dataColors": {
        "selected": "#0363ff",
        "alternative": "#a8c9ff",
        "excluded": "#ffaf03",
        "selectedExcluded": "#ffe58f",
        "possible": "#ffffff"
      }
    },
    "mapChart": {
      "backgroundColor": "@grayscale-95",
      "label": {
        "value": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      },
      "legend": {
        "title": {
          "color": "@grayscale-35"
        },
        "label": {
          "color": "@grayscale-35"
        }
      }
    },
    "pieChart": {
      "axis": {
        "title": {
          "fontSize": "@text"
        }
      },
      "label": {
        "name": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        },
        "value": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      }
    },
    "pivotTable": {
      "header" : {
        "fontSize" : "@text",
        "color": "@grayscale-35"
      },
      "content": {
        "fontSize": "@text",
        "color": "@grayscale-35"
      }
    },
    "scatterPlot": {
      "label": {
        "value": {
          "color": "@grayscale-40",
          "fontSize": "@14px"
        }
      }
    },
    "straightTable" : {
      "header" : {
        "fontSize" : "@text",
        "color": "@grayscale-35"
      },
      "content": {
        "fontSize": "@text",
        "color": "@grayscale-35"
      }
    },
  "straightTableV2": {
      "dimension": {
        "label": {
          "name": {
            "fontFamily": "Verdana",
            "fontSize": "18px",
            "color": "#ccc",
            "backgroundColor": "#ff0000"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#000000",
            "backgroundColor": "orangered"
          }
        }
      },
      "measure": {
        "label": {
          "value": {
            "fontFamily": "Arial",
            "fontSize": "14px",
            "color": "#ccc",
            "backgroundColor": "#ff0099"
          }
        }
      },
      "total": {
        "label": {
          "value": {
            "fontFamily": "Tahoma",
            "fontSize": "24px",
            "color": "#fff",
            "backgroundColor": "#3399aa"
          }
        }
      },
      "null": {
        "label": {
          "value": {
            "color": "red",
            "backgroundColor": "#ccc"
          }
        }
      },
      "grid": {
        "borderColor": "purple",
        "divider": {
          "borderColor": "lime"
        },
        "hover": {
          "color": "orange",
          "backgroundColor": "black"
        }
      }
    },
    "writeTable": {
      "dimension": {
        "label": {
          "name": {
            "fontFamily": "Verdana",
            "fontSize": "18px",
            "color": "#ccc",
            "backgroundColor": "#ff0000"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#000000",
            "backgroundColor": "orangered"
          }
        }
      },
      "measure": {
        "label": {
          "value": {
            "fontFamily": "Arial",
            "fontSize": "14px",
            "color": "#ccc",
            "backgroundColor": "#ff0099"
          }
        }
      },
      "total": {
        "label": {
          "value": {
            "fontFamily": "Tahoma",
            "fontSize": "24px",
            "color": "#fff",
            "backgroundColor": "#3399aa"
          }
        }
      },
      "null": {
        "label": {
          "value": {
            "color": "red",
            "backgroundColor": "#ccc"
          }
        }
      },
      "grid": {
        "borderColor": "purple",
        "divider": {
          "borderColor": "lime"
        },
        "hover": {
          "color": "orange",
          "backgroundColor": "black"
        }
      },
      "editableColumn": {
        "label": {
          "value": {
            "color": "#5c4a00",
            "backgroundColor": "#fffbe6"
          }
        },
        "inputFieldBackground": "#fffbe6",
        "inputFieldHoverColor": "#fff3cc"
      }
    },
    "treemap": {
      "branch": {
        "backgroundColor": "@grayscale-70",
        "label": {
          "color": "@grayscale-35",
          "fontSize": "@text"
        }
      },
      "leaf": {
        "label": {
          "fontSize": "@text"
        }
      }
    },
    "waterfallChart": {
      "label": {
        "value": {
          "fontSize": "20px"
        }
      },
      "value": {
        "color": {
          "default": "@grayscale-45",
          "dark": "@grayscale-20",
          "light": "@grayscale-70"
        }
      },
      "shape": {
        "positiveValue": {
          "fill": "@grayscale-70"
        },
        "negativeValue": {
          "fill": "@grayscale-45"
        },
        "subtotal": {
          "fill": "@grayscale-20"
        },
        "bridge": {
          "stroke": "@grayscale-35"
        }
      }
    }
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
          "none",
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
