---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/themes-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Theme JSON properties

> **Notes:**
>
> - This topic does not include all possible properties, and all properties listed in this topic are not mandatory.
> - Colors should be defined using hexadecimal values.
> - Visualization IDs do not always match theme IDs, for example, the straight table
>   has a visualization ID of `sn-table`, but a theme ID of `straightTableV2`.

These are common properties of the JSON file top level structure.

Common properties

- \_inherit: Defines if the custom theme inherits style properties from the Sense
  Classic theme. Properties defined in the JSON file override the inherited properties.

  Default or undefined: `true`.

  Example:

  `"_inherit": false,`|

- \_cards: Optional.

  Defines if the custom theme should style the objects on the sheets as cards.

  Default or undefined: `false`.

  Example:`"_cards": false,`

- \_variables: Optional.

  Variables that can be referenced within the JSON file.

  > **Note:** Variable names must be prefixed with @.

  Example:

  ```json
  "_variables": {
    "@default": "#555555",
    "@dark": "#333333",
    "@light": "#eeeeee",
    "@H1": "24px",
    "@H2": "18px",
    "@H3": "14px",
    "@H4": "13px",
    "@H5": "12px",
    "@font-normal": "12px"
  }
  ```

- custom\_styles: Optional.

  Reference to a custom style sheet that will be inserted when theme is applied.

  > **Note:** Although adding custom CSS files is possible, not all CSS rules
  > work at all times in Qlik Sense. For greater stability, use a JSON file instead.

  Example:

  ```json
  "customStyles": [{
    "cssRef": "theme.css",
    "classRef": "my-theme"
  }]
  ```

- color: Font color.

  This setting can be overridden by defining the color property on any level
  that supports color.

  Example:

  ```json
  "color": "@default"
  ```

- fontSize: Font size.

  This setting can be overridden by defining the fontSize property on any level
  that supports fontSize.

  Example:

  ```json
  "fontSize":"@font-normal"
  ```

- fontFamily: Font (typeface)

  Can be specified as a list of prioritized fonts and generic family names,
  separated by a comma. This setting can be overridden by defining the
  fontFamily property on any level that supports `fontFamily`.

  Example:

  ```json
  "fontFamily": "Arial, Helvetica, sans-serif"
  ```

- backgroundColor: Background color of charts.

  This setting can be overridden by defining the background color property on
  chart-type level.

  Example:

  ```json
  "backgroundColor": "@light"
  ```

- object: Object styling.

  See [object](#object) for more details.

  Example:

  ```json
  "object": {
    "line": {
      ...
    },
    "title": {
      ...
    },
    "label": {
      ...
    },
    "axis": {
      ...
    },
    "grid": {
      ...
    },
    "referenceLine": {
      ...
    },
    "legend": {
      ...
    },
    "barChart": {
      ...
    },
    "boxPlot": {
      ...
    },
    "bulletChart": {
      ...
    },
    "comboChart": {
      ...
    },
    "distributionPlot": {
      ...
    },
    "filterpane": {
      ...
    },
    "kpi": {
      ...
    },
    "gauge": {
      ...
    },
    "histogram": {
      ...
    },
    "lineChart": {
      ...
    },
    "listBox": {
      ...
    },
    "mapChart": {
      ...
    },
    "pieChart": {
      ...
    },
    "pivotTable": {
      ...
    },
    "pivotTableV2": {
      ...
    },
    "scatterPlot": {
      ...
    },
    "straightTable" : {
      ...
    },
    "straightTableV2": {
      ...
    },
    "tabContainer": {
      ...
    },
    "textImage": {
      ...
    },
    "treemap": {
      ...
    },
    "waterfallChart" : {
      ...
    },
    "writeTable": {
      ...
    }
  }
  ```

- dataColors: Data color properties.

  - primaryColor: Primary color property.
  - othersColor: Others color property.
  - errorColor: Error color property.
  - nullColor: Null color property.
  - selected: Color property for selected values. This property appears in the selection bar and all listboxes.
    It also appears when making selections in the Straight table and Pivot table charts in the Visualization bundle.
  - alternative: Color property for alternative values. This property appears in the selection bar and all listboxes.
  - excluded: Color property for excluded values. This property appears in the selection bar and all listboxes.
  - selectedExcluded: Color property for selected excluded values.
    This property appears in the selection bar and all listboxes.
  - possible: Color property for possible values. This property appears in the selection bar and all listboxes.

  Example:

  ```json
  "dataColors": {
    "primaryColor": "#0000FF",
    "othersColor": "#808080",
    "errorColor": "#FF0000",
    "nullColor": "#FFFF00",
    "selected": "#ff9900",
    "alternative": "#D9D9D9",
    "excluded": "#4B4B4B",
    "selectedExcluded": "#888888",
    "possible": "#ffffff"
  }
  ```

- palettes: Customized color palette properties.
  See [palettes](#palettes) for more details.

- scales: Color scheme properties.
  See [scales](#scales) for more details.

- sheet: Properties for the background color of the sheet title.
  See [sheet](#sheet) for more details.

## object

These are the common properties of the `object` structure.

### title

Title properties. This setting can be overridden by defining the `title`
property on chart-type level.

Title properties

- main: Main title properties.
  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- subTitle: Subtitle properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- footer: Footer properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

  - backgroundColor: Background color.

    Example:

    ```json
    "backgroundColor": "@light"
    ```

Example:

```json
"title": {
  "main": {
    "color": "@default",
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif"
  },
  "subTitle": {
    "color": "@default",
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif"
  },
  "footer": {
    "color": "@default",
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif",
    "backgroundColor": "@light"
  }
}
```

### label

Label properties. This setting can be overridden by defining the `label`
property on chart-type level for charts that have labels.

Label properties are supported for the following chart types.

Chart types and label support

| Chart type       | label.name.color | label.name.fontSize | label.value.color | label.value.fontSize |
| ---------------- | ---------------- | ------------------- | ----------------- | -------------------- |
| barChart         | -                | -                   | ✓                 | ✓                    |
| bulletChart      | -                | -                   | ✓                 | ✓                    |
| comboChart       | -                | -                   | ✓                 | ✓                    |
| gauge            | -                | -                   | ✓                 | -(calculated)        |
| histogram        | -                | -                   | ✓                 | ✓                    |
| kpi              | ✓                | -(calculated)       | -                 | -(calculated)        |
| lineChart        | -                | -                   | ✓                 | ✓                    |
| mapChart         | -                | -                   | -                 | ✓                    |
| pieChart         | ✓                | ✓                   | -(calculated)     | ✓                    |
| pieChart (donut) | ✓                | ✓                   | ✓                 | ✓                    |
| scatterPlot      | -                | -                   | ✓                 | ✓                    |
| waterfallChart   | -                | -                   | -                 | ✓                    |

> **Note:** `label.name.fontFamily` and `label.value.fontFamily` are supported by all chart types.

label properties

- name: Label name properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- value: Label value properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

Example:

```json
"label": {
  "name": {
    "color": "@default",
    "fontSize": "10px",
    "fontFamily": "sans-serif"
  },
  "value": {
    "color": "@default",
    "fontSize": "10px",
    "fontFamily": "sans-serif"
  }
}
```

### axis

Axis properties. This setting can be overridden by defining the `axis` property on
chart-type level for charts with axes (bar charts, box plots, combo charts,
distribution plots, gauges, histograms, line charts, scatter plots, and
waterfall charts).

For pie charts, `axis.title` can be overridden and is used for styling the
dimension label.

axis properties

- title: Axis title properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- label: Axis label properties.

  - name: Properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

    - fontFamily: Font (typeface).

      Example:

      ```json
      "fontFamily": "sans-serif"
      ```

- line: Axis line properties.

  - major: Axis title properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

  - minor: Axis label properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

Example:

```json
"axis": {
  "title": {
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif",
    "color": "@default"
  },
  "label": {
    "name": {
      "color": "@default",
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif"
    }
  },
  "line": {
    "major": {
      "color": "@default"
    },
    "minor": {
      "color": "@default"
    }
  }
}
```

### grid

Grid properties. This setting cannot be overridden on chart-type level.

grid properties

- line: line properties.

  - highContrast: High contrast property.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

  - major: Major property.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

  - minor: Minor property.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

Example:

```json
"grid": {
  "line": {
    "highContrast": {
      "color": "@default"
    },
    "major": {
      "color": "@default"
    },
    "minor": {
      "color": "@default"
    }
  }
}
```

### referenceLine

Reference line properties. This setting cannot be overridden on chart-type level.

referenceLine properties

- label: Label properties.

  - name: Name Properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

    - fontFamily: Font (typeface).

      Example:

      ```json
      "fontFamily": "sans-serif"
      ```

- outOfBounds: Out of bounds properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - backgroundColor: Background color.

    Example:

    ```json
    "backgroundColor": "@light"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```javascript
    "fontFamily": "sans-serif"
    ```

Example:

```json
"referenceLine": {
  "label": {
    "name": {
      "color": "@default",
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif"
    }
  },
  "outOfBounds": {
    "color": "@default",
    "backgroundColor": "@default",
    "fontSize": "@H6",
    "fontFamily": "sans-serif"
  }
}
```

### legend

Legend properties. This setting can be overridden by defining the `legend` property
on chart-type level for charts with legends (bar charts, combo charts, line
charts, map charts, pie charts, scatter plots, treemaps, waterfall charts).

legend properties

- title: Legend title properties.

  - color: Font color.

    Example:

  ```json
  "color": "@default"
  ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- label: Legend label properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

Example

```json
"legend": {
  "title": {
    "color": "@default",
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif"
  },
  "label": {
    "color": "@default",
    "fontSize": "@font-normal",
    "fontFamily": "sans-serif"
  }
}
```

### `{chart-type}`

See [Chart types](#chart-types) for more details.

Chart type can be:

- barChart
- boxPlot
- bulletChart
- comboChart
- distributionPlot
- filterpane
- gauge
- histogram
- kpi
- layoutContainer
- lineChart
- listBox
- mapChart
- pieChart
- pivotTable
- pivotTableV2
- scatterPlot
- straightTable
- straightTableV2
- tabContainer
- textImage
- treemap
- waterfallChart
- writeTable

> **Note:** Most global `object` properties can also be defined on chart-type level.
> If done, this overrides the properties set on the global `object` level.

## Chart types

These are the common chart type properties that can exist within the `object`
structure. The properties listed for each chart are specific to them.

> **Note:** Most global `object` properties can also be defined on chart-type level.
> If done, this overrides the properties set on the global `object` level.

### barChart

barChart properties

- outOfRange: Out of range properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "barChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "label": {
      "value": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "outOfRange": {
      "color": "@default"
    }
  }
  ```
</details>

### boxPlot

boxPlot properties

- box: Box properties.

  - whisker: Properties.

    - stroke: Stroke color.

      Example:

      ```json
      "stroke": "@default"
      ```

  - line: Properties.

    - stroke: Stroke color.

      Example:

      ```json
      "stroke": "@default"
      ```

  - box: Properties.

    - fill: Fill color.

      Example:

      ```json
      "fill": "@default"
      ```

    - stroke: Stroke color.

      Example:

      ```json
      "stroke": "@default"
      ```

<details>
  <summary>Example</summary>

  ```json
  "boxPlot": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "box": {
      "whisker": {
        "stroke": "@default"
      },
      "line": {
        "stroke": "@default"
      },
      "box": {
        "fill": "@default",
        "stroke": "@default"
      }
    }
  }
  ```
</details>

### bulletChart

bulletChart properties

- outOfRange: Out of range properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "bulletChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "label": {
      "value": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "outOfRange": {
      "color": "@default"
    }
  }
  ```
</details>

### comboChart

Combo chart properties

- outOfRange: Out of range properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "comboChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    }
  }
  ```
</details>

### distributionPlot

distributionPlot properties

- box: Box properties.

  - fill: Fill color.

    Example:

    ```javascript
    "fill": "@default"
    ```

<details>
  <summary>Example</summary>

  ```json
  "distributionPlot": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "box": {
      "fill": "@default"
    }
  }
  ```
</details>

### filterpane

Filter pane properties

<details>
  <summary>Example</summary>

  ```json
  "filterpane": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    }
  }
  ```
</details>

### gauge

Gauge properties

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "gauge": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "label": {
      "value": {
        "color": "@default",
        "fontSize": "42px"
      }
    }
  }
  ```
</details>

### histogram

Histogram properties

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "histogram": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "label": {
      "value": {
        "color": "@default",
        "fontSize": "40px",
        "fontFamily": "sans-serif"
      }
    }
  }
  ```
</details>

### kpi

KPI properties

- label: Label properties.

  - name: Label name properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

<details>
  <summary>Example</summary>

  ```json
  "kpi": {
      "backgroundColor": "@light",
      "title": {
          "main": {
              "color": "@default",
              "fontSize": "@font-normal",
              "fontFamily": "@font-family"
          },
          "subTitle": {
              "color": "@default",
              "fontSize": "@font-normal",
              "fontFamily": "@font-family"
          },
          "footer": {
              "color": "@default",
              "fontSize": "@font-normal",
              "fontFamily": "@font-family",
              "backgroundColor": "@light"
          }
      },
      "label": {
          "name": {
              "color": "@default",
              "fontFamily": "@font-family"
          },
          "value": {
              "fontFamily": "@font-family"
          }
      }
  }
  ```
</details>

### lineChart

lineChart properties

- outOfRange: Out of range properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "lineChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "outOfRange": {
      "color": "@default"
    },
    "label": {
      "value": {
        "color": "@dark",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    }
  }
  ```
</details>

### listBox

List properties. Used to style filter panes and the list boxes in the
selections tool.

listBox properties

- content: List box content properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- dataColors: Data color properties for list boxes.

  - selected: Color property for selected values. This color property appears in all listboxes,
    including in filter panes, the selection tool, and when searching values in charts.

    Example:

    ```json
    "selected": "#ff9900"
    ```

  - alternative: Color property for alternative values. This color property appears in all listboxes,
    including in filter panes, the selection tool, and when searching values in charts.

    Example:

    ```json
    "alternative": "#D9D9D9"
    ```

  - excluded: Color property for excluded values. This color property appears in all listboxes,
    including in filter panes, the selection tool, and when searching values in charts.

    Example:

    ```json
    "excluded": "#4B4B4B"
    ```

  - selectedExcluded: Color property for selected excluded values.
    This color property appears in all listboxes, including in filter panes, the selection tool, and when searching
    values in charts.

    Example:

    ```json
    "selectedExcluded": "#888888"
    ```

  - possible: Color property for possible values. This color property appears in all listboxes,
    including in filter panes, the selection tool, and when searching values in charts.

    Example:

    ```json
    "possible": "#ffffff"
    ```

  - fontSize: Font size.

<details>
  <summary>Example</summary>

  ```json
  "listBox": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "content": {
      "color": "@default",
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif"
    },
    "dataColors": {
      "color": "@default",
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif",
      "selected": "#0000ff",
      "alternative": "#D9D9D9",
      "excluded": "#4B4B4B",
      "selectedExcluded": "#888888",
      "possible": "#ffffff"
  }
  }
  ```
</details>

### mapChart

mapChart properties

- label: Map chart label properties.

  - value: Properties.

    - dark.color: Dark font color.

    - light.color: Light font color.

    - fontSize: Font size.

      Example:

      ```json
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
      ```

<details>
  <summary>Example</summary>

  ```json
  "mapChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
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
</details>

### pieChart

pieChart properties

- axis: Pie chart axis properties.

  - title: Properties. Used to style the pie chart dimension label.

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

- label: Pie chart label properties.

  - name: Slice label name properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

  - value: Slice value label properties.

    > **Note:** `label.value.color` is only applicable for pie charts presented as a donut.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "pieChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "label": {
      "name": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "value": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    }
  }
  ```
</details>

### pivotTable

pivotTable properties

- header: Pivot table header properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

    - fontFamily: Font (typeface).

      Example:

      ```json
      "fontFamily": "sans-serif"
      ```

- content: Pivot table content properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

  - hover: Properties.

    - backgroundColor: Background color when hovering.

      Example:

      ```json
      "backgroundColor": "@light"
      ```

    - color: Font color when hovering.

      Example:

      ```json
      "color": "@default"
      ```

- scrollbar: Pivot table scroll bar properties.

  - size: Scroll bar width.

  Example:

  ```json
  "size": "small"
  ```

<details>
  <summary>Example</summary>

  ```json
  "pivotTable": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "header": {
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif",
      "color": "@default"
    },
    "content": {
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif",
      "color": "@default"
    }
    "scrollbar": {
      "size": "small"
    }
  }
  ```
</details>

### pivotTableV2

pivotTableV2 properties

- dimension: Dimension properties.
  - label: Dimension label properties.
    - name: Dimension label name properties.
      - `fontFamily`: Font family property for the dimension label names.
      - `fontSize`: Font size property for the dimension label names.
      - `color`: Font color property for the dimension label names.
      - `backgroundColor`: Background color property for the dimension label names.
    - value: Dimension label value properties.
      - `fontFamily`: Font family property for the dimension label values.
      - `fontSize`: Font size property for the dimension label values.
      - `color`: Font color properties for the dimension label values.
      - `backgroundColor`: Background color property for the dimension label values.
- measure: Measure properties.
  - label: Measure label properties.
    - name: Measure label name properties.
      - `color`: Font color property for the measure label names.
      - `backgroundColor`: Background color property for the measure label names.
    - value: Measure label value properties.
      - `fontFamily`: Font family property for the measure label values.
      - `fontSize`: Font size property for the measure label values.
      - `color`: Font color properties for the measure label values.
      - `backgroundColor`: Background color property for the measure label values.
- total: Totals row properties.
  - label: Totals row label properties.
    - value: Totals row label value properties.
      - `color`: Font color properties for the totals row label values.
      - `backgroundColor`: Background color property for the totals row label values.
- null: Null value properties.
  - label: Null value label properties.
    - value: Null value label properties for value labels.
      - `color`: Null value color properties for value labels.
      - `backgroundColor`: Null value background color properties for value labels.
- grid: Grid properties.
  - `lineClamp`: Maximum number of lines for cell content before truncation.
  - `backgroundColor`: Grid background color properties.
  - `borderColor`: Grid border color properties.
  - divider: Grid divider properties.
    - `borderColor`: Grid divider border color properties.

<details>
  <summary>Example</summary>

  ```json
  { 
  "object": { 
  "pivotTableV2": { 
        "dimension": { 
          "label": { 
            "name": { 
              "fontFamily": "sans-serif", 
              "fontSize": "18px", 
              "color": "#333333", 
              "backgroundColor": "transparent" 
            }, 
            "value": { 
              "fontFamily": "sans-serif", 
              "fontSize": "12px", 
              "color": "#333333", 
              "backgroundColor": "transparent" 
            } 
          } 
        }, 
        "measure": { 
          "label": { 
            "name": { 
              "color": "#737373", 
              "backgroundColor": "transparent" 
            }, 
            "value": { 
              "fontFamily": "sans-serif", 
              "fontSize": "12px", 
              "color": "#737373", 
              "backgroundColor": "transparent" 
            } 
          } 
        }, 
        "total": { 
          "label": { 
            "value": { 
              "color": "#333333", 
              "backgroundColor": "transparent" 
            } 
          } 
        }, 
        "null": { 
          "label": { 
            "value": { 
              "color": "#333333", 
              "backgroundColor": "#F2F2F2" 
            } 
          } 
        }, 
        "grid": { 
          "lineClamp": 1, 
          "backgroundColor": "transparent", 
          "borderColor": "#D9D9D9", 
          "divider": { 
            "borderColor": "#B3B3B3" 
          } 
        } 
      } 
  } 
  } 
  ```
</details>

### scatterPlot

Scatterplot properties

- label: Label properties.

  - value: Label value properties.

    - color: Font color.

      Example:

      ```json
      "color": "@default"
      ```

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "scatterPlot": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "label": {
      "value": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    }
  }
  ```
</details>

### straightTable

> **Note:** straightTableV2 has replaced straightTable as the default table visualization.
> Consider upgrading existing tables to straight tables for improved capabilities
> and performance.

straightTable properties

- header: Straight table header properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

- content: Straight table content properties.

  - color: Font color.

    Example:

    ```json
    "color": "@default"
    ```

  - fontSize: Font size.

    Example:

    ```json
    "fontSize": "@font-normal"
    ```

  - fontFamily: Font (typeface).

    Example:

    ```json
    "fontFamily": "sans-serif"
    ```

  - hover: Properties.

    - backgroundColor: Background color when hovering.

      Example:

      ```json
      "backgroundColor": "@light"
      ```

    - color: Font color when hovering.

      Example:

      ```javascript
      "color": "@default"
      ```

- scrollbar: Straight table scroll bar properties.

  - size: Scroll bar width.

    Example:

    ```json
    "size": "small"
    ```

<details>
  <summary>Example</summary>

  ```json
  "straightTable": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "header": {
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif",
      "color": "@default"
    },
    "content": {
      "fontSize": "@font-normal",
      "fontFamily": "sans-serif",
      "color": "@default"
    }
    "scrollbar": {
      "size": "small"
    }
  }
  ```
</details>

### straightTableV2

straightTableV2 properties

- dimension: Dimension properties.
  - label: Dimension label properties.
    - name: Dimension label name properties.
      - `fontFamily`: Font family property for the dimension label names.
      - `fontSize`: Font size property for the dimension label names.
      - `color`: Font color property for the dimension label names.
      - `backgroundColor`: Background color property for the dimension label names.
    - value: Dimension label value properties.
      - `fontFamily`: Font family property for the dimension label values.
      - `fontSize`: Font size property for the dimension label values.
      - `color`: Font color properties for the dimension label values.
      - `backgroundColor`: Background color property for the dimension label values.
- measure: Measure properties.
  - label: Measure label properties.
    - value: Measure label value properties.
      - `fontFamily`: Font family property for the measure label values.
      - `fontSize`: Font size property for the measure label values.
      - `color`: Font color properties for the measure label values.
      - `backgroundColor`: Background color property for the measure label values.
- total: Totals row properties.
  - label: Totals row label properties.
    - value: Totals row label value properties.
      - `fontFamily`: Font family property for the totals row label values.
      - `fontSize`: Font size property for the totals row label values.
      - `color`: Font color properties for the totals row label values.
      - `backgroundColor`: Background color property for the totals row label values.
- null: Null value properties.
  - label: Null value label properties.
    - value: Null value label properties for value labels.
      - `color`: Null value color properties for value labels.
      - `backgroundColor`: Null value background color properties for value labels.
- grid: Grid properties.
  - `lineClamp`: Maximum number of lines for cell content before truncation.
  - `borderColor`: Grid border color.
  - `backgroundColor`: Grid background color.
  - divider: Grid divider properties.
    - `borderColor`: Grid divider border color.
  - hover: Hover row properties.
    - `color`: Text color when hovering over a row.
    - `backgroundColor`: Background color when hovering over a row.

<details>
  <summary>Example</summary>

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
          "lineClamp": 2, 
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
</details>

### tabContainer

tabContainer properties

- label: Tab label properties.
  - value: Tab label value properties.
    - `fontSize`: Tab label font size.
    - `fontFamily`: Tab label font family.
    - `color`: Tab label color.
  - `textAlignment`: Tab label text alignment.
- icon: Tab icon properties.
  - value: Tab icon value properties.
    - `color`: Tab icon color.
    - `fontSize`: Tab icon size.
- indicator: Active tab indicator properties.
  - selected: Selected tab indicator properties.
    - `color`: Selected tab indicator color.
  - hover: Hover tab indicator properties.
    - `color`: Hover tab indicator color.
- background: Tab background properties.
  - hover: Hover background properties.
    - `color`: Hover background color.

<details>
  <summary>Example</summary>

  ```json
  "tabContainer": {
    "label": {
      "value": {
        "fontSize": "13px",
        "fontFamily": "sans-serif",
        "color": "#333333"
      },
      "textAlignment": "left"
    },
    "icon": {
      "value": {
        "color": "#333333",
        "fontSize": "13px"
      }
    },
    "indicator": {
      "selected": {
        "color": "#00873D"
      },
      "hover": {
        "color": "#B3B3B3"
      }
    },
    "background": {
      "hover": {
        "color": "rgba(0,0,0,0.03)"
      }
    }
  }
  ```
</details>

### textImage

Text & image properties

<details>
  <summary>Example</summary>

  ```json
  "textImage": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    }
  }
  ```
</details>

### treemap

treemap properties

- branch: Branch properties.

  - backgroundColor: Background color.

  - label: Branch label properties.

    - fontSize: Font size.

      Example:

      ```javascript
      "fontSize": "@font-normal"
      ```

- leaf: Leaf properties.

  - label: Leaf label properties.

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

<details>
  <summary>Example</summary>

  ```json
  "treemap": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "legend": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "branch": {
      "backgroundColor": "@default",
      "label": {
        "color": "@light",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "leaf": {
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    }
  }
  ```
</details>

### waterfallChart

waterfallChart properties

- label: Label properties.

  - value: Label value properties.

    - fontSize: Font size.

      Example:

      ```json
      "fontSize": "@font-normal"
      ```

- value: Value properties.

  - color: Properties.

    - default: Default color.

    - Example:

      ```json
      "default": "@default"
      ```

    - dark: Dark color.

      Example:

      ```json
      "dark": "@dark"
      ```

    - light: Light color.

      Example:

      ```json
      "light": "@light"
      ```

- shape: Line chart label properties.

  - positiveValue: Properties.

    - fill: Fill color.

      Example:

      ```json
      "fill": "@default"
      ```

  - negativeValue: Properties.

    - fill: Fill color.

      Example:

      ```json
      "fill": "@default"
      ```

  - subtotal: Properties.

    - fill: Fill color.

      Example:

      ```json
      "fill": "@default"
      ```

  - bridge: Properties.

    - stroke: Stroke color.

      Example:

      ```javascript
      "stroke": "@default"
      ```

<details>
  <summary>Example</summary>

  ```json
  "waterfallChart": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    },
    "axis": {
      "title": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      },
      "label": {
        "name": {
          "color": "@default",
          "fontSize": "@font-normal",
          "fontFamily": "sans-serif"
        }
      },
      "line": {
        "major": {
          "color": "@default"
        },
        "minor": {
          "color": "@default"
        }
      }
    },
    "legend": {
      "label": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "color": "@default"
      }
    },
    "label": {
      "value": {
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      }
    },
    "value": {
      "color": {
        "default": "@default",
        "dark": "@dark",
        "light": "@light"
      }
    },
    "shape": {
      "positiveValue": {
        "fill": "white"
      },
      "negativeValue": {
        "fill": "#ccccc"
      },
      "subtotal": {
        "fill": "#000000"
      },
      "bridge": {
        "stroke": "#333333"
      }
    }
  }
  ```
</details>

### writeTable

writeTable properties

- dimension: Dimension properties.
  - label: Dimension label properties.
    - name: Dimension label name properties.
      - `fontFamily`: Font family property for the dimension label names.
      - `fontSize`: Font size property for the dimension label names.
      - `color`: Font color property for the dimension label names.
      - `backgroundColor`: Background color property for the dimension label names.
    - value: Dimension label value properties.
      - `fontFamily`: Font family property for the dimension label values.
      - `fontSize`: Font size property for the dimension label values.
      - `color`: Font color properties for the dimension label values.
      - `backgroundColor`: Background color property for the dimension label values.
- measure: Measure properties.
  - label: Measure label properties.
    - value: Measure label value properties.
      - `fontFamily`: Font family property for the measure label values.
      - `fontSize`: Font size property for the measure label values.
      - `color`: Font color properties for the measure label values.
      - `backgroundColor`: Background color property for the measure label values.
- total: Totals row properties.
  - label: Totals row label properties.
    - value: Totals row label value properties.
      - `fontFamily`: Font family property for the totals row label values.
      - `fontSize`: Font size property for the totals row label values.
      - `color`: Font color properties for the totals row label values.
      - `backgroundColor`: Background color property for the totals row label values.
- null: Null value properties.
  - label: Null value label properties.
    - value: Null value label properties for value labels.
      - `color`: Null value color properties for value labels.
      - `backgroundColor`: Null value background color properties for value labels.
- grid: Grid properties.
  - `backgroundColor`: Grid background color properties.
  - divider: Grid divider properties.
    - `borderColor`: Grid border color properties.
- hover: Hover menu properties.
  - `color`: Hover menu text color properties.
  - `backgroundColor`: Hover menu background color properties.
- editableColumn: Editable column properties.
  - label: Editable column label properties.
    - value: Editable column label value properties.
      - `fontFamily`: Font family property for the editable column label values.
      - `fontSize`: Font size property for the editable column label values.
      - `color`: Font color property for editable column label values.
      - `backgroundColor`: Background color property for editable column label values.
  - `inputFieldBackground`: Input field background color property.
  - `inputFieldHoverColor`: Input field hover color property.

<details>
  <summary>Example</summary>

  ```json
  { 
  "object": { 
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
              "fontFamily": "Arial", 
              "fontSize": "14px", 
              "color": "#FFFF00", 
              "backgroundColor": "#b2a938" 
            } 
          }, 
          "inputFieldBackground": "#ffffff", 
          "inputFieldHoverColor": "#f0f0f0" 
        } 
      } 
  } 
  } 
  ```
</details>

### `{extension-name}`

Extension properties for this specific extension.

<details>
  <summary>Example</summary>

  ```json
  "MyVizExtension": {
    "backgroundColor": "@light",
    "title": {
      "main": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "subTitle": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif"
      },
      "footer": {
        "color": "@default",
        "fontSize": "@font-normal",
        "fontFamily": "sans-serif",
        "backgroundColor": "@light"
      }
    }
  }
  ```
</details>

## palettes

These are the common color palette properties.

palettes properties

- data: Properties for data palette. These are used for Color by dimension in
  the properties panel.

  - name: Name of the palette. Optional.

  - othersColor: Display name for the color palette in the UI.

    Example:

    "translation": "12 colors"

  - propertyValue: Identifier of the palette. Must be unique in the system.

  - type: Type of color palette.

    - pyramid
    - row

  - scale: Definition of all colors used in the palette. Scales from top to
    bottom, and left to right.

- ui: Properties for the UI palette. You can define several palettes but the
  first palette defined in ui is used in the color picker, for example when
  coloring by single color.

  - name: Name of the palette.

  - colors: Colors used in the UI palette. Should always be unique colors defined.

## scales

These are the common color scheme properties. The scales are used for
Color by measure in the properties panel.

scales properties

- name: Name of the color scheme.

  Example

  ```json
  "name": "Custom Sequential Gradient"
  ```

- translation: Display name for the color scheme in the UI.

  Example

  ```json
  "translation": "Custom Sequential Gradient"
  ```

- type: Type of the color scheme.

  - gradient

  - class

    Example

    ```json
    "type": "gradient"
    ```

- propertyValue: Property value of the color scheme

  - sg for Sequential Gradient

  - sc for Sequential Classes

  - dg for Diverging gradient

  - dc for Diverging Classes

    Example

    ```json
    "propertyValue": "sg"
    ```

- scale: Colors included in the color scheme, scaled from left to right.

  Example

  ```json
  "scale": [ "#1A2980", "#26D0CE" ]
  ```

## sheet

These are the sheet title background color properties.

sheet properties

- title: Properties for sheet title background color.

  - private: Private sheets that have not been shared.

    - titleBackgroundColor: Defines the background color of the sheet title.

    - titleBackgroundGradientColor: Defines the color of the gradient within the
      sheet title.

- approved: Published and approved sheets.

  - titleBackgroundColor: Defines the background color of the sheet title.

  - titleBackgroundGradientColor: Defines the color of the gradient within the
    sheet title.

- published: Published by you or others and not approved.

  - titleBackgroundColor: Defines the background color of the sheet title.

  - titleBackgroundGradientColor: Defines the color of the gradient within the
    sheet title.

## Example

<details>
  <summary> Full example of theme.json </summary>

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
        "lineClamp": 2,
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
    "tabContainer": {
      "label": {
        "value": {
          "fontSize": "13px",
          "fontFamily": "sans-serif",
          "color": "#333333"
        },
        "textAlignment": "left"
      },
      "icon": {
        "value": {
          "color": "#333333",
          "fontSize": "13px"
        }
      },
      "indicator": {
        "selected": {
          "color": "#00873D"
        },
        "hover": {
          "color": "#B3B3B3"
        }
      },
      "background": {
        "hover": {
          "color": "rgba(0,0,0,0.03)"
        }
      }
    },
    "pivotTableV2": {
      "dimension": {
        "label": {
          "name": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#333333",
            "backgroundColor": "transparent"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#333333",
            "backgroundColor": "transparent"
          }
        }
      },
      "measure": {
        "label": {
          "name": {
            "color": "#737373",
            "backgroundColor": "transparent"
          },
          "value": {
            "fontFamily": "sans-serif",
            "fontSize": "12px",
            "color": "#737373",
            "backgroundColor": "transparent"
          }
        }
      },
      "total": {
        "label": {
          "value": {
            "color": "#333333",
            "backgroundColor": "transparent"
          }
        }
      },
      "null": {
        "label": {
          "value": {
            "color": "#333333",
            "backgroundColor": "#F2F2F2"
          }
        }
      },
      "grid": {
        "lineClamp": 1,
        "backgroundColor": "transparent",
        "borderColor": "#D9D9D9",
        "divider": {
          "borderColor": "#B3B3B3"
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
