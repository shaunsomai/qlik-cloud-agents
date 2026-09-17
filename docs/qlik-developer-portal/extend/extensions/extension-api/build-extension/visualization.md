---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/visualization/
last_updated: 2026-06-02T18:15:45+01:00
---

# Visualization

## What's a visualization

A visualization in the context of this API represents the visual output of some
underlying data stored in Qlik's Associative Data Model. It could be almost
anything you want it to be and is traditionally developed to show the data in
the shape of a chart, table, KPI, etc.

## Composition

A visualization has two main parts: a backend *Generic Object* that describes
the *properties* of the visualization and is persisted in the data model, and a
frontend visual part that renders the *layout* of the *Generic Object*.

## Definition

The minimal visualization that doesn't contain any data nor renders anything
looks like this:

```js
export default function () {
  return {
    qae: {
      /* */
    },
    component() {},
  };
}
```

The `component()` is where you render the visual part, while `qae` is where you
define the properties and data handled by Qlik's Associative Engine (QAE).
