---
source: https://qlik.dev/extend/extensions/picasso-js/components/tooltip/
last_updated: 2026-06-02T18:15:45+01:00
---

# Tooltip

A customizable tooltip component that can display complementary information.
Typically used when moving the mouse cursor over a node or selecting a node.

![Example rendering of a tooltip component](https://qlik.dev/_astro/tooltip.D7T3n2AE.png)

## Layout

There is only one use case for docking the tooltip component
and that is docking at the center area, which is the default value.

### `appendTo` setting

The `appendTo` setting allows the tooltip to be decoupled from the chart
container by creating the tooltip DOM element as child of the `appendTo`
element instead.

## Events

There is no need to configure [data](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/data)
or [scales](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/scales), as they are
not directly consumed by the component. Instead, it reacts to events that are
triggered from interactions.

### `show` event

The event takes two parameters, the first is the pointer event and the second is
an optional object which may contain specific nodes to use when rendering the
tooltip. If the second parameter is omitted, the pointer event is used to
perform a node lookup on the chart instance.

With a single event parameter:

```js
picassoInstance.component("<key value of tooltip>").emit("show", event);
```

With optional parameters:

```js
const nodes = picassoInstance.shapesAt({ x: 1, y: 2, width: 3, height: 4 }); // An array of nodes
picassoInstance.component("<key value of tooltip>").emit("show", event, {
  nodes,
  delay: 50, // Optional, the component setting value is used as default
  duration: 2000, // Optional, the component setting value is used as default
}); // The event is dispatched and if no new events are triggered until the delay has passed, a tooltip is displayed
```

### `hide` event

Hide the tooltip hides the tooltip if it's currently displayed, if not
the event is ignored.

```js
picassoInstance.component("<key value of tooltip>").emit("hide");
```

## Extracting data and generating custom content

As the main purpose of a tooltip is often to displayed complementary data when
hovering or selecting a node, controlling which data to displayed is crucial.
Luckily there are two settings available to ensure that correct data is
displayed in the tooltip.

### Extracting data

The `extract` setting is executed for each node and is expected to return a data
representation. By default the extracted data is a string with the value of the
node. But could be any data structure, such as an object or an array of objects.

```js
const extract = ({ node }) => node.data.value;
```

### Generating content

The `content` setting is responsible for generating virtual nodes using the
HyperScript API and is expected to return an array of virtual nodes.

```js
{
  settings: {
    content: ({ h, data }) => data.map((datum) => h("div", {}, datum));
  }
}
```

### Example - Formatting values

Here the value is passed through a formatter and returns the output as extracted
data.

```js
{
  settings: {
    extract: ({ node, resources }) =>
      resources.formatter("<name-of-a-formatter>")(node.data.value);
  }
}
```

But sometimes you want to give the value some context, for example by labeling it.
As such you can change the data structure to an object instead to make it more clear
what the data represent. As you do, the default `content` generator function
complains because it doesn't understand the new data structure, so you must also
update the `content` setting.

```js
{
  settings: {
    extract: ({ node, resources }) => ({
      label: node.data.label,
      value: resources.formatter('<name-of-a-formatter>')(node.data.value)
    }),
    // We go from a basic content generator, to one that understand the new data structure
    content: ({ h, data }) => data.map(datum => h('div', {}, `${datum.label}: ${datum.value}`))
  }
}
```

## Placement strategies

The placement strategy defines how the tooltip is positioned in relation to a
set of nodes or a node. The built-in strategies all have a auto docking feature,
such that if the tooltip doesn't fit inside its designated area, the docking
position may be adjusted to a position where it does fit.

> Note that there may still be scenarios where the tooltip doesn't fit,
> for example when the designated area just cannot fit the tooltip at all.

### Available strategies

- `pointer` - is the default and use the current pointer position to place the tooltip.
- `bounds` - use the bounding rectangle of the first node. Note the depending on
  the type of shape, the position of the tooltip may indicate that it's not over
  the visual area of the shape.
- `slice` - is built to work together with the `pie` component, such that the
  tooltip is placed at the arc of a slice.

All strategies can be defined as a string, object, or a function.

```js
// Define as a string
{
  settings: {
    placement: 'pointer'
  }
}

// Or as an object
{
  settings: {
    placement: {
      type: 'pointer',
      dock: 'top',
      offset: 8,
      area: 'target'
    }
  }
}

// Or as a function
{
  settings: {
    placement: () => ({
      type: 'pointer',
      dock: 'top',
      offset: 8,
      area: 'target'
    })
  }
}
```

### Custom placement function

When the built in placement strategies are not sufficient, it possible to create
your own placement function.

```js
{
  settings: {
    placement: {
      fn: () => {
        // Do some magic here
        return {
          {
            computedTooltipStyle: {
              left: '10px',
              top: '20px',
              color: 'red'
            },
            computedArrowStyle: {
              left: '0px',
              top: '0px',
              color: 'red'
            },
            dock: 'top'
          }
        };
      }
    }
  }
}
```

## Example

```js
picasso.chart({
  settings: {
    interactions: [{
      type: 'native',
      events: {
        mousemove(e) {
          const tooltip = this.chart.component('<tooltip-key>');
          tooltip.emit('show', e);
        },
        mouseleave(e) {
          const tooltip = this.chart.component('<tooltip-key>');
          tooltip.emit('hide');
        }
      }
    }],
    components: [
      {
        key: '<tooltip-key>',
        type: 'tooltip'
      }
    ]
  },
  ...
});
```

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-componenttooltip).
