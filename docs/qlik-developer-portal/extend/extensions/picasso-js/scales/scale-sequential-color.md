---
source: https://qlik.dev/extend/extensions/picasso-js/scales/scale-sequential-color/
last_updated: 2026-06-02T18:15:45+01:00
---

# Color - Sequential

The `Color Sequential` scale is the default color filling method that fills in
color in a regular sequence, from start to end.

## Usage

```js
picasso.chart({
  data,
  element,
  settings: {
    scales: {
      myScale: {
        type: "sequential-color",
        min: 0,
        max: 100,
        range: ["red", "blue"],
      },
    },
    components: [
      {
        type: "some-component",
        scale: "myScale",
      },
    ],
  },
});
```

![Example of bar chart with sequential color scale](https://qlik.dev/_astro/scaleColorSequential.BLisPjw3.png)

### Settings

`range` is an optional property that supports `RGB` and `RGBA`, `HEX` and
`HTML Color names`.
`min` and `max` are optional properties that set what data value fit
at the bottom and top of your `range`. `invert` is an optional property
that is used to invert the `range`.

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalesequentialcolor).
