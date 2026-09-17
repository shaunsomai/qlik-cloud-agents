---
source: https://qlik.dev/extend/extensions/picasso-js/components/legend-seq/
last_updated: 2026-06-02T18:15:45+01:00
---

# Legend - Sequential

The Sequential legend can represent sequential data mapped to a color range.

## Data and scales

The legend component doesn't take any [data](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/data) as input
directly, instead the data is implicitly fetched from the referenced [scales](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/scales).

There are two required scales, a `fill` scale and a `major` scale. The `fill`
scale represent the color range, via a sequential color scale, and `major` is
the numerical representation, via a linear scale.

## Layout

The legend can be laid out in two directions; horizontal and vertical.
The direction is dependent on the docking area, `top` and `bottom` are
horizontal and `left` and `right` are vertical.

Horizontal layout:

![Example of a legend with horizontal layout](data:image/png;base64,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)

Vertical layout:

![Example of a legend with vertical layout](data:image/png;base64,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)

### Custom labels

Custom labels can be configured using a ticks function. The ticks function is
evaluated for each tick (start and stop) and expects a string value to be returned.

```js
{
  type: 'legend-seq',
  settings: {
    fill: 'sequential-color-scale',
    major: 'linear-scale',
    tick: {
      label: (tickValue, index) => {
        const temp = ['Hot', 'Cold'];
        return temp[index % 2];
      },
    }
  }
}
```

![Example of a legend with custom labels](data:image/png;base64,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)

## Formatting

Label formatting is derived from the `major` scale and the data itself. But as
with any component, it is possible to reference a [custom formatter](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/formatting)
using the `formatter` property.

```js
{
  type: 'legend-seq',
  formatter: {
    formatter: 'd3', // The type of formatter to use
    type: 'number', // The type of data to format
    format: '-1.0%' // Format pattern
  }
}
```

## Interaction

There is no direct way to configure interactions, instead it is done via other
components, such as the [brush-range](https://qlik.dev/extend/extensions/picasso-js/components/brush-range/).

### Enable range selection

To enable range selection, two scene nodes are exposed that can be referenced,
via a CSS selector, by
the [brush-range](https://qlik.dev/extend/extensions/picasso-js/components/brush-range/) component as a target.

This reference enables
the [brush-range](https://qlik.dev/extend/extensions/picasso-js/components/brush-range/)
component to limit the
target area to a sub-area of the legends dock area.

```js
chartSettings = {
  interactions: [
    ... // Setup required brush-range interactions here.
  ],
  scales: {
    'sequential-color-scale': { source: '0/1', type: 'color' },
    'linear-scale': { source: '0/1', type: 'linear' },
  },
  components: [
    {
      type: 'legend-seq',
      layout: {
        dock: 'right',
      },
      key: 'myLegend' // Reference by the brush-range component,
      settings: {
        fill: 'sequential-color-scale',
        major: 'linear-scale'
      }
    },
    {
      type: 'brush-range',
      key: 'myBrushRange',
      layout: {
        dock: '@myLegend', // Legend reference
      },
      settings: {
        brush: 'highlight',
        scale: 'linear-scale',
        direction: 'vertical',
        bubbles: {
          align: 'start',
          placement: 'outside' // Render bubbles outside the legends dock area
        },
        target: {
          selector: '[id="legend-seq-target"]', // Define the target area. Must reference a node from @myLegend
          fillSelector: '[id="legend-seq-ticks"]', // Define the target fill area. Must reference a node from @myLegend
          fill: 'rgba(82,204,82,0.3)',
        }
      },
  }]
}
```

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-componentlegendseq).
