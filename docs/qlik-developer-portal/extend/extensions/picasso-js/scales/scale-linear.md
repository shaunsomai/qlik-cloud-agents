---
source: https://qlik.dev/extend/extensions/picasso-js/scales/scale-linear/
last_updated: 2026-06-02T18:15:45+01:00
---

# Linear

The linear scale is used to represent numerical data over a continuous range
and is typically used as part of
a [continuous axis](https://qlik.dev/extend/extensions/picasso-js/scales/components/axis#continuous).
It is used to show sampled values from the scales domain, configured as ticks
and minorTicks, or it is consumed by a component to map data points along an axis.

## Usage

You can create a linear scale bound to data, however it is also possible to have
the scale independent of data points.

### Data bound

To connect a linear scale to data points, you need to specify the field name.
The following example creates a linear scale (myScale) based on the data points
for the field Sales and a domain of `[1106,5444]`. Note that specifying the type
linear is optional since it is the default option for a scale.

```js
picasso.chart({
  data: [
    {
      type: 'matrix',
      data: [
        ['Year', 'Month', 'Sales', 'Margin'],
        ['2010', 'Jan', 1106, 7],
        ['2010', 'Feb', 5444, 53],
      ],
    },
  ],
  element,
  settings: {
    scales: {
      myScale: {
        type: 'linear',
        data: {
          field: 'Sales',
        },
      },
    },
    components: [
      {
        type: 'some-component',
        scale: 'myScale',
      },
    ],
  },
});
```

### Independent

An independent linear scale is not bound to data points. It defaults to a range
of 0 to 1. However, it is possible to set your own limits to the scale. Here the
linear scale is set using the `min`/`max` properties instead of binding it via
data. Using the `min/max` properties on a data bound scale overrides
the range specified by the data points.

```js
myScale: {
  min: 0,
  max: 100,
}
```

### Expand

You can expand the scale by using the expand property (this only works when
the scale is bound to data points). Be aware that it sets the factor by which the
scale is expanded. In the example below, the scale containing domain `[0,5]`
expands with a factor 1 in both directions creating a domain of `[-5,10]`

```js
picasso.chart({
  data: [
    {
      type: 'matrix',
      data: [
        ['x', 'y'],
        [0, 0],
        [5, 5],
      ],
    },
  ],
  element,
  settings: {
    scales: {
      myScale: {
        data: {
          field: 'x',
        },
        expand: 1,
      },
    },
  },
});
```

### Invert

You can invert the scale by setting the invert property to true.

```js
myScale: {
  min: 0,
  max: 100,
  invert: true
}
```

### Include

To include specific values in the scale, you can use specify an array of values in
include.

```js
myScale: {
  data: {
    field: 'fieldNmae'
  },
  include: [-100, 236]
}
```

### Adding custom ticks

It is possible to configure custom ranges in the linear scale when making use
of ticks. To have a tick representing a range, you need to define a set of
custom ticks with a value (the tick) and its start and end values.

```js
{ // scale settings
  domain: [0, 10],
  ticks: {
    values: [
      { value: 3, start: 2, end: 4, label: '$3', isMinor: false },
      { value: 6, start: 5, end: 7, label: '$6', isMinor: false }
    ]
  }
}
```

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalelinear).
