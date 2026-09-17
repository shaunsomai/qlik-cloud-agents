---
source: https://qlik.dev/extend/extensions/picasso-js/main-concepts/chart/
last_updated: 2026-06-02T18:15:45+01:00
---

# Chart

## Render a chart

The `picasso.chart` function creates and renders a chart.

### `picasso.chart(definition)`

- `definition` Object
  - `element` HTMLElement. The element to render the chart into.
  - `data` Object. The data to render. [More](https://qlik.dev/extend/extensions/picasso-js/main-concepts/data).
  - `settings` Object.
    - `components` Array. [More](https://qlik.dev/extend/extensions/picasso-js/main-concepts/components).
    - `scales` Object (optional). Scales to use when rendering. [More](https://qlik.dev/extend/extensions/picasso-js/main-concepts/scales).
    - `formatters` Object (optional). Formatters that can be referenced from
      other components. [More](https://qlik.dev/extend/extensions/picasso-js/main-concepts/formatting).
    - `strategy` Object (optional). Layout behavior and responsiveness. [More](https://qlik.dev/extend/extensions/picasso-js/main-concepts/layout).
  - `created` Function (optional). Lifecycle hook.
  - `beforeMount` Function (optional). Lifecycle hook.
  - `mounted` Function (optional). Lifecycle hook.
  - `beforeRender` Function (optional). Lifecycle hook.
  - `beforeUpdate` Function (optional). Lifecycle hook.
  - `updated` Function (optional). Lifecycle hook.
  - `beforeDestroy` Function (optional). Lifecycle hook.
  - `destroyed` Function (optional). Lifecycle hook.

## Chart lifecycle hooks

Use the lifecycle hooks to add and remove capabilities when certain events are triggered.

If you have used frameworks such as React or VueJS, you are familiar with the
lifecycle concept. There are basically three use cases:

### Rendering a chart the first time

This triggers lifecycle events in the following order:

`created -> beforeRender -> beforeMount -> mounted`

### Updating a chart

This triggers lifecycle events in the following order:

`beforeUpdate -> beforeRender -> updated`

### Tearing down a chart

This triggers lifecycle events in the following order:

`beforeDestroy -> destroyed`

### Methods

#### created()

Called when the chart has been created. Use to initialize state variables that
should be bound to the chart instance.

```js
picasso.chart({
  created() {
    this.dataPage = 1;
  },
});
```

#### beforeMount()

Called before the chart has been mounted. Use to set initial state that server
rendered charts may not need. *This hook is client-side only.*

```js
picasso.chart({
  beforeMount() {
    this.clickCount = 0;
  },
});
```

#### mounted(element)

- `element` HTMLElement - The element the chart was rendered in.

Called after the chart has been mounted. Use to bind custom event handlers or
other operations requiring the element. *This hook is client-side only.*

```js
picasso.chart({
  mounted(element) {
    // Bind a tap listener using the Touche library (https://github.com/stoffeastrom/touche)
    Touche(element).tap({
      options: {
        areaThreshold: 5,
      },
      end: function (e, data) {
        console.log('tap');
      },
    });
  },
});
```

#### beforeRender()

Called before the chart has been rendered. Use to initialize state variables
that should be bound to the chart instance.

```js
picasso.chart({
  beforeRender() {
    this.dataPage = 1;
  },
});
```

#### beforeUpdate()

Called before the chart is updated. Use to initialize state variables that
should be bound to the chart instance.

```js
picasso.chart({
  beforeUpdate() {
    this.dataPage = 1;
  },
});
```

#### updated()

Called when the chart has been updated. Use to initialize state variables that
should be bound to the chart instance.

```js
picasso.chart({
  updated() {
    this.dataPage = 1;
  },
});
```

#### beforeDestroy()

Called before the chart has been destroyed. Use to unbind custom event listeners
and do cleanup work requiring the element. *This hook is client-side only.*

```js
picasso.chart({
  beforeDestroy() {
    this.dataPage = 1;
  },
});
```

#### destroyed()

Called when the chart has been destroyed. At this point all event handlers have
been unbound and references to elements are not available. *This hook is*
*client-side only.*

```js
chart({
  destroyed() {
    this. = 1;
  }
});
```

## Chart instance functions

### update()

Update a chart with new `data` and/or `settings`. Triggers updates of all
chart components.

```js
const chartInstance = picasso.chart({
  /* ... */
});
chartInstance.update({
  settings: newSettings,
  data: newData,
});
```

## Example

```js
const chartInstance = picasso.chart({
  element: document.getElementById('chart-container'),
  data: { ... },
  settings: {
    scales: {
      x: {
        data: { extract: { field: "Products" } }
      },
      y: {
        data: { extract: { field: "Year" } }
      }
    },
    components: [{
      type: "point",
      settings: {
        fill: 'red'
      }
    }]
  },
  created: function() {
    console.log('Chart was created');
  },
  mounted: function() {
    console.log('Chart was mounted');
  }
});

chartInstance.update({
  data: { /* . */ }
});
```

> Note that you should not use arrow functions to let the `this` context inside
> methods to be bound to the instance
