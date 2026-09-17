---
source: https://qlik.dev/extend/extensions/picasso-js/main-concepts/brushing/
last_updated: 2026-06-02T18:15:45+01:00
---

# Brushing

Brushing in a component is handled in two ways: *trigger* and *consume*.

## Observe actions on the component

`trigger` controls how the component reacts to various user actions like
'tapping on a shape':

- `on`: type of interaction to react to
- `action`: type of action to respond with. *Optional*
- `contexts`: name of the brushing contexts to affect
- `data`: the mapped data properties to add to the brush. *Optional*
- `propagation`: control the event propagation when multiple shapes are tapped.
  Disabled by default. *Optional*
- `globalPropagation`: control the event propagation between components.
  Disabled by default. *Optional*
- `touchRadius`: extend contact area for tap events. Disabled by default. *Optional*
- `mouseRadius`: extend contact area for regular mouse events.
  Disabled by default. *Optional*

```js
trigger: [{
  on: 'tap',
  action: 'toggle',
  contexts: ['selection', 'tooltip'],
  data: ['x'],
  propagation: 'stop', // 'stop' => prevent trigger from propagating further than the first shape
  globalPropagation: 'stop', // 'stop' => prevent trigger of same type to be triggered on other components
  touchRadius: 24,
  mouseRadius: 10
}],
```

## Observe changes of a brush context

`consume` controls how the component uses active brushes.

- `context`: name of the brush context to observe
- `data`: the mapped data properties to observe. *Optional*
- `mode`: data properties operator: `and`, `or`, `xor`. *Optional*
- `filter`: a filtering function. *Optional*
- `style`: the style to apply to the shapes of the component
  - `active`: the style of *active* data points
  - `inactive`: the style of *inactive* data points

```js
consume: [
  {
    context: "selection",
    data: ["x"],
    filter: (shape) => shape.type === "circle",
    style: {
      active: {
        fill: "red",
        stroke: "#333",
        strokeWidth: (shape) => shape.strokeWidth * 2,
      },
      inactive: {},
    },
  },
];
```

## Programmatic changes

Brushes can be controlled programmatically by accessing a certain brush from
the picasso instance:

```js
const pic = picasso.chart(...);
const highlighter = pic.brush('highlight'); // get brush instance
highlighter.addValue('products', 'Bike'); // highlight 'Bike'
```

when `addValue` is called, components that are *consuming* the *highlight*
brushing context reacts automatically and apply the specified style.

## Brushing and linking

All components using a *trigger* or *consume* configuration is automatically
linked within the same chart. To link brushes from two different
chart instances, use `link`:

```js
const scatter = picasso.chart(/* */);
const bars = picasso.chart(/* */);
scatter.brush("select").link(bars.brush("highlight"));
```

Now, whenever a value is brushed in the `scatter` instance, the same values is
also brushed in the `bars` instance:

![animation of brushing and linking between two
charts](https://qlik.dev/_astro/brush-link.sTSg8auy.gif)

## Examples

**Scenario**: tapping on a data point in a component should activate a brush
called *highlight*, add the relevant data to the brush, and finally
highlight the point in the component.

```js
{
  type: 'point',
  data: {...},
  settings: {...},
  brush: {
    trigger: [{
      on: 'tap',
      contexts: ['highlight']
    }],
    consume: [{
      context: 'highlight',
      style: {
        inactive: {
          opacity: 0.3
        }
      }
    }]
  }
}

```

To make the component react to a *tap*, a `trigger` is added with an `on` of
type `'tap'`, and `'highlight'` as brush `contexts` that should be affected.

To have the component listen to brush changes and update itself, a `consume`
object is added with the name of the `context` to observe.
