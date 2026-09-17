---
source: https://qlik.dev/extend/extensions/picasso-js/scales/scale-threshold-color/
last_updated: 2026-06-02T18:15:45+01:00
---

# Color - Threshold

In the `Color Threshold` scale, the colors present in the range property array are
applied among the domain values from start to end, blending them in the values between
edges if needed.

## Usage

```js
picasso.chart({
  data,
  element,
  settings: {
    scales: {
      myScale: {
        type: "threshold-color",
        domain: [69, 2260, 4460],
        range: ["#9bcd25", "rgb(57, 174, 86)", "mediumturquoise"],
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

![Example rendering of a bar chart with color
threshold scale](https://qlik.dev/_astro/scale-color-threshold.DOVX2ChL.png)

### Settings

The property `nice` can be specified to generate "nice" domain values but it is
ignored if domain is set.

`range` property supports `RGB` and `RGBA`, `HEX` and `HTML Color names`.

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalethresholdcolor).
