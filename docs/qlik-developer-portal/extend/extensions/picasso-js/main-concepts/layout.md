---
source: https://qlik.dev/extend/extensions/picasso-js/main-concepts/layout/
last_updated: 2026-06-02T18:15:45+01:00
---

# Layout

The dock layout is the engine that controls how different components are
positioned and whether a component is rendered or not, depending on available
space, that is, the responsiveness.

There are 5 different layout areas, with the `center` area being the primary
one. It is typically where the visual components are positioned. On each side
of the center area, there is another area on which a component can be
positioned (docked). They are referred to as `top`, `bottom`, `left` and `right`.

![Descriptive image of dock area](data:image/png;base64,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)

Most components should handle any of the 5 different areas, but it may make more
sense for certain components to be primarily either in the center or at the sides.

## Scaling

### Size (physical size)

The default physical size is equal to that of the container (element) for the chart.

By explicitly setting a size, it is possible to override both width and height
of the container. Either width or height, or both can be specified.

The input value is specified as a number and represents the size in pixels.

Example:

```js
strategy: {
  size: {
    width: 100,
    height: 100
  }
}
```

### Logical size

Logical size represents the size given to the dock layout to work with. If the
logical size is different than the physical size (size of the container or the
size property), then scaling is applied to the components to fit into
the physical size.

The default logical size is equal to the physical size.

The input value is specified as a number and represents the size in pixels.

Example:

```js
strategy: {
  logicalSize: {
    width: 150,
    height: 150,
    preserveAspectRatio: false,
    align: 0.5
  }
}
```

## Responsiveness

Each component can tell the layout engine that they require a certain amount of
space, where the direction of the space required is the perpendicular axis of
the dock area, given that `left`/ `right` area has a main axis of Y and
`top`/`bottom` main axis is X.

The arrow demonstrates the direction in which a component requests space for
each dock area. Note that components docked in the center area have no impact
on the space available, which is instead determined by the amount of space
occupied by components docked at the sides.

![Descriptive image of dock area direction](data:image/png;base64,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)

The responsive engine has two ways to determine if a component should be rendered
or not. The first way is to compare the space required by a component to the
logical space available. If not enough space is available, the component is
discarded and the engine moves on to process the next component. The second way
is to define a minimum layout mode, this is currently the only way to discard a
component docked in the center area.

### Limiting space required by the center area

Each of the side areas can take a certain amount of space from the center area.
If there is not enough space available for the center area, either in vertical
or horizontal direction, the layout engine must remove one or more of the
components docked at the side.

It is possible to control the amount of space required by the center area with
properties. By setting `minWidthRatio` and/or `minHeightRatio` to a value
between 0 and 1, the available size is set as a ratio of the logical size. With
1 meaning all logical size goes to the center area, as such no components docked
at the side are rendered. 0 means that components docked at the side take as
much space as needed from the center area.

When configured with either `minWidth/minHeight` or `minWidthRatio/minHeightRatio`,
the minimum required space of the center area is set to that size. However the
center area can never be larger than logical size and clamps to the logical size.
If `minWidth` and `minWidthRatio` are set, the absolute size from `minWidth`
has precedence over `minWidthRatio`.

Example:

```js
strategy: {
  center: {
    minWidthRatio: 0.5,
    minHeightRatio: 0.5,
    minWidth: 10,
    minHeight: 10
  }
}
```

### Minimum layout mode

The minimum layout mode is a way to tell the layout engine that a component
should be discarded if the logical size is below a certain threshold in
width or height.

Example:

```js
strategy: {
  layoutModes: {
    S: { width: 150, height: 150 }
    L: { width: 300, height: 300 }
  }
}

// in the component definition
{
  type: 'my-component',
  minimumLayoutMode: 'S',
  settings...
}
```

## Component instance configuration

The following dock properties are available in the component definition:

- `show` *boolean*. True if component should be rendered.
- `layout`*object*. Layout settings
- `layout.dock` *string*. Dock setting. Any of `top` | `right` | `bottom` | `left`
- `layout.displayOrder` *number*. The order in which components are rendered
  (similar to CSS z-index).
- `layout.prioOrder` *number*. The order in which components are docked from
  the center area.
- `layout.minimumLayoutMode` *string*.

Example:

```js
components: [
  {
    type: "my-component",
    layout: {
      show: true,
      dock: "left",
      displayOrder: 0,
      prioOrder: 0,
      minimumLayoutMode: "S",
    },
  },
];
```

### Working with `displayOrder`

The `displayOrder` property is used by the layout engine to lay out components.
Components are interpreted in the ascending order of the `displayOrder` value.
The layout engine applies the value in two ways: the first is the order in which
components are rendered, and the second is the area components are laid out in
when they have a direction, that is, docked to either top, bottom, left, or right.

If docked at the same area, the component with a higher `displayOrder` is
rendered on top of the component with a lower `displayOrder`. It can be seen as
defining a z-index. A lower `displayOrder` also means that a component is
laid out first in a given direction, that is, laid out closer to the central
area (non-directional area) than a component with a higher `displayOrder`.
It can, in this case, be seen as the x-index or y-index.

In the example below, all docking areas have two components with a `displayOrder`
of 0 and 1. Notice how the center area only displays the component with
`displayOrder` 1, which is the z-index in action.

![Descriptive image of display order](https://qlik.dev/_astro/display-order.66xb6LCn.png)

### Working with `prioOrder`

The `prioOrder` property is used to define the order in which components are
added to the layout engine; this is done before any components are laid out.
When there is not enough space to add any more components to a given area,
all components not already added are then discarded. The value of `prioOrder`
is in ascending order, such that a lower value is added to the layout engine first.

## Component flowchart

The following diagram shows the order in which components flow through the
layout engine.

![Flowchart of how dock properties are resolved by the
layout engine](https://qlik.dev/_astro/dock-process-flow.DzkJ_kVQ.png)
