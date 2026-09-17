---
source: https://qlik.dev/extend/extensions/nebula-js/nebula-stardust-core-principles/
last_updated: 2026-09-03T10:42:49Z
---

# Core principles

`nebula.js` is the framework for building custom visualization extensions on top of Qlik's Associative
Engine. The primary package, `@nebula.js/stardust`, exposes a hook-based component API that covers
data bindings, environment and selections. Understanding a handful of core concepts unlocks the entire
framework.

## The extension structure

Every extension is a function that returns an object with three top-level keys: `qae`, `component` and `ext`.

```js
import { useElement, useLayout, useEffect } from "@nebula.js/stardust";

export default function (env) {
  return {
    qae: {
      properties: {
        qHyperCubeDef: {
          qInitialDataFetch: [
            {
              qWidth: 2,
              qHeight: 500,
            },
          ],
        },
      },
      data: {
        targets: [
          {
            path: "/qHyperCubeDef",
            dimensions: {
              min: 1,
              max: 1,
              description: () => "Bar",
            },
            measures: {
              min: 1,
              max: 1,
              description: (properties) =>
                properties?.orientation === "vertical" ? "Height" : "Width",
            },
          },
        ],
      },
    },
    component() {
      const element = useElement();
      const layout = useLayout();
      if (layout && element) {
        const data = layout.qHyperCube.qDataPages[0].qMatrix;
        const measure = layout.qHyperCube.qMeasureInfo[0];
        const isVertical = layout.orientation === "vertical";
        element.innerHTML = `<div style="writing-mode: ${isVertical ? "vertical-rl" : "horizontal-tb"}">${measure.qFallbackTitle}: ${data[0][0].qText}</div>`;
      }
    },
    ext: {
      definition: {
        type: "items",
        component: "accordion",
        items: {
          data: {
            uses: "data",
          },
          settings: {
            uses: "settings",
          },
          presentation: {
            uses: "presentation",
            items: {
              orientation: {
                ref: "orientation",
                type: "string",
                label: "Orientation",
                component: "dropdown",
                options: [
                  { value: "vertical", label: "Vertical" },
                  { value: "horizontal", label: "Horizontal" },
                ],
              },
            },
          },
        },
      },
      support: {
        snapshot: false,
        export: true,
        exportData: true,
        viewData: true,
      },
    },
  };
}
```

`qae` is the backend definition: it contains information that tells Qlik's
Associative Engine what properties and data the visualization needs.

`component` is the frontend: it runs in a hook-aware context and is responsible
for rendering the DOM.

`ext` is the extension settings, it tells the Qlik frontend how to display
the property panel (`definition`) and what additional
features this particular extension supports.

## The Generic Object: Properties, layout and model

The Generic Object is the bridge between your extension and Qlik's Associative Engine.

- *properties* you declare as the input, which engine evaluates to produce a *layout*
- *model*: created by nebula, representation of the engines generic object API, for
  example contains functions like setProperties and beginSelections that affects the objects state.

### Static and dynamic properties

Properties come in two kinds:

- **Static properties** pass through the engine unchanged. Use them for settings like colors,
  toggle states, or configuration your visualization needs to persist.
- **Dynamic properties** are evaluated by the engine before being returned in the layout. You
  identify them by the `q` prefix followed by a capital letter, for example `qHyperCubeDef` or
  `qValueExpression`.

```js
// properties (input)
{
  isStacked: true,              // static — passes through as-is
  simpleMath: {
    qValueExpression: {         // dynamic — evaluated by the engine
      qExpr: '1+1',
    },
  },
  qHyperCubeDef: {},            // dynamic — produces a HyperCube in the layout
}

// layout (output)
{
  isStacked: true,
  simpleMath: 2,                // evaluated result
  qHyperCube: { /* ... */ },   // HyperCube data
}
```

The layout is what `useLayout()` returns inside `component`. Your rendering code reads from the
layout, never directly from the properties.

For more information, see [Configure data](https://qlik.dev/extend/extensions/extension-api/build-extension/configuring-data/).

## Stardust hooks

The `component` function runs inside a hook-aware context. Stardust hooks follow the same rules as
React hooks: call them at the top level of `component`, never inside conditions or loops.

### Core hooks

| Hook                   | Returns                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| `useElement()`         | The DOM element stardust has reserved for your visualization                             |
| `useLayout()`          | The evaluated Generic Object layout                                                      |
| `useStaleLayout()`     | Same as useLayout, but will not trigger if the object is in selections                   |
| `useModel()`           | The object model [Generic Object](https://qlik.dev/apis/json-rpc/qix/genericobject/) API |
| `useApp()`             | The object model [Doc](https://qlik.dev/apis/json-rpc/qix/doc/) API                      |
| `useAppLayout()`       | The evaluated app layout, including locale information                                   |
| `useSelections()`      | The selection API for the current object                                                 |
| `useTheme()`           | The currently active theme                                                               |
| `useState(initial)`    | Local reactive state, scoped to this object instance                                     |
| `useEffect(fn, deps)`  | Runs a side effect when any dependency changes                                           |
| `usePromise(fn, deps)` | Wraps an async function and returns `[result, error]`                                    |

### The rendering cycle

The `component` function runs every time Stardust needs to re-render, starting with object creation.
Inside it, you call hooks like `useElement()` and `useLayout()`.
Stardust tracks the dependencies listed in each `useEffect` hook.
When a dependency changes, for example `layout` updates because a user made a selection, Stardust re-runs
the `component` function, but only the hooks that depend on that value.

```js
// Runs on each render, likely multiple times
component() {
  const element = useElement();
  const layout = useLayout();

  useEffect(() => {
    // Runs on mount and whenever `element` or `layout` changes.
    element.innerHTML = `<h1>${layout.title}</h1>`;
  }, [element, layout]);
}
```

`useElement` and `useLayout` rarely change independently, but listing both in the dependency array
is correct: if either changes, the effect must re-run to keep the DOM consistent.

For a full list of available hooks and their signatures, see the
[nebula.js API reference](https://qlik.dev/apis/javascript/nebula-js/).

## Data targets and HyperCubeDef

A `qHyperCubeDef` in your properties declares that you want data from the engine. A *data target*
tells stardust which of those definitions should be user-configurable, meaning Qlik's property panel
shows drag-and-drop fields for dimensions and measures.

```js
qae: {
  properties: {
    qHyperCubeDef: {},
  },
  data: {
    targets: [
      {
        path: '/qHyperCubeDef',
        dimensions: { min: 1, max: 2 },
        measures: { min: 1, max: 1 },
      },
    ],
  },
},
```

`path` is the JSON path from the root of the properties object. When the limits you declare are not
met, for example the user hasn't added a required dimension, stardust shows a placeholder instead
of calling `component`. This saves you from writing defensive checks inside `component`.

You can modify a dimension or measure at the moment it is added:

```js
dimensions: {
  min: 1,
  max: 2,
  added(dimension) {
    dimension.qNullSuppression = true;
  },
},
```

For more information, see [Configure data](https://qlik.dev/extend/extensions/extension-api/build-extension/configuring-data/) and
[HyperCube introduction](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/).

## The HyperCube and data pages

The `qHyperCube` in the layout is the result of evaluating `qHyperCubeDef`. Think of it as a table:
`qDimensionInfo` and `qMeasureInfo` describe the columns, and `qDataPages` contains the rows.

Because the engine can hold billions of rows, data is never transferred all at once. You control the
initial fetch with `qInitialDataFetch`:

```js
qHyperCubeDef: {
  qInitialDataFetch: [{ qLeft: 0, qTop: 0, qWidth: 2, qHeight: 100 }],
},
```

The maximum per request is 10 000 cells (rows × columns). If you need more data after the initial
load, call `model.getHyperCubeData` directly:

```js
const model = useModel();
model.getHyperCubeData("/qHyperCubeDef", [
  { qLeft: 0, qTop: 100, qWidth: 2, qHeight: 100 },
]);
```

For more information, see [HyperCube introduction](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/).

## The Associative Engine and selections

Qlik's Associative Engine maintains a single in-memory data model where every field and its
associations are tracked together. When a user selects a value in one chart, the engine propagates
the filter across all associated fields in every other chart simultaneously. Your extension does not
need to coordinate with other visualizations: the engine handles it automatically.

### Instant selections

For immediate filtering, call `selectHyperCubeCells` directly on the model:

```js
import { useModel, useEffect } from '@nebula.js/stardust';

component() {
  const model = useModel();

  useEffect(() => {
    model.selectHyperCubeCells('/qHyperCubeDef', [rowIndex], [0]);
  }, [model]);
}
```

The selection is applied and all charts update in one step.

### Modal selections

Modal selections let a user accumulate choices before confirming. While active, the source chart
retains its full dataset so the user can keep selecting:

```js
import { useSelections, useElement, useLayout, useEffect } from '@nebula.js/stardust';

component() {
  const element = useElement();
  const layout = useLayout();
  const selections = useSelections();

  useEffect(() => {
    // Setup the click event(s)
    const onClick = (e) => {
      if (!selections.isActive()) {
        selections.begin(['/qHyperCubeDef']);
      }
      const rowIndex = e.data.row; // Find out what was clicked in some manner
      selections.select({
        method: 'selectHyperCubeCells',
        params: ['/qHyperCubeDef', [rowIndex], [0]],
      });
    };

    element.addEventListener('click', onClick);
    return () => element.removeEventListener('click', onClick);
  }, [element, selections]);

  useEffect(() => {
    // Update visual feedback based on whether the object is in selection mode.
    if (layout.qSelectionInfo.qInSelections) {
      // highlight selected rows
    } else {
      // reset highlights
    }
  }, [layout]);
}
```

The user confirms or cancels through the standard Qlik toolbar. Use `layout.qSelectionInfo.qInSelections`
to know when modal mode is active so you can update visual feedback in your chart.

For more information, see [Select data](https://qlik.dev/extend/extensions/extension-api/build-extension/selecting-data/).

## Theming

The `useTheme()` hook returns the currently active Qlik theme. Use it to read colors, fonts, and
other design tokens so your visualization respects the theme applied to the app:

```js
import { useTheme, useEffect } from '@nebula.js/stardust';

component() {
  const theme = useTheme();

  useEffect(() => {
    const background = theme.getColorPickerColor({ color: theme.getDataColorSpecials().primary });
    // use background in your rendering
  }, [theme]);
}
```

For more information, see [Get started with the Theme API](https://qlik.dev/extend/extensions/extension-api/build-extension/theme-getting-started/).

## What to read next

With these core principles in place, you are ready to move into the detailed guides:

- [Build a HelloWorld extension using nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension/):
  a step-by-step tutorial that applies all these concepts together
- [Configure data](https://qlik.dev/extend/extensions/extension-api/build-extension/configuring-data/):
  deep dive on properties, layout, and data targets
- [Consume data](https://qlik.dev/extend/extensions/extension-api/build-extension/consuming-data/):
  reference for all data and model hooks
- [HyperCube introduction](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/):
  complete guide to HyperCubeDef and data pages
- [Select data](https://qlik.dev/extend/extensions/extension-api/build-extension/selecting-data/):
  instant and modal selection patterns in detail
- [nebula.js API reference](https://qlik.dev/apis/javascript/nebula-js/): complete hook and type reference
