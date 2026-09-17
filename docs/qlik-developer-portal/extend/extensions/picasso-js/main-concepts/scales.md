---
source: https://qlik.dev/extend/extensions/picasso-js/main-concepts/scales/
last_updated: 2026-06-02T18:15:45+01:00
---

# Scales

Scales are an essential part of most visualizations and picasso.js comes bundled
with a couple of them.

The scales in picasso.js are augmented [d3 scales](https://github.com/d3/d3-scale),
where the main difference is tighter integration with [data](https://qlik.dev/extend/extensions/picasso-js/main-concepts/data/).

## Using scales

Scales are used indirectly via the `picasso.chart` API. Where the `chart` API
instantiate the scales.
This approach allows the `components` object to use a scale instances by
reference. It's also possible to access via the chart instance API.

```js
const chartInstance = picasso.chart({
  data,
  element,
  settings: {
    scales: {
      nameOfMyScale: {
        type: 'type-of-scale',
        data,
        aScaleProperty: true, // Add scale setting properties here
      },
    },
    components: [
      {
        type: 'some-component',
        scale: 'nameOfMyScale', // Pass the scale instance to the component
      },
    ],
  },
});

chartInstance.scales('nameOfMyScale'); // Returns a scale instance
```

### Scale type deduction from data

If `type` property is omitted then it's deducted depending on
the [data](https://qlik.dev/extend/extensions/picasso-js/main-concepts/data/).

- If there are extracted fields in data and all of them are set to type `dimension`
  then the type is set to `band` otherwise it's set to `linear` as default

### How can a scale be consumed

Depending on the context there are little variations, some components
consume scales or data differently and some are dependent on scales,
here are some examples:

- [Axis](https://qlik.dev/apis/javascript/picasso-js/#definitions-componentaxis)
  component doesn't take any data as input directly, instead the data is
  implicitly fetched from the referenced scale.
- [Box](https://qlik.dev/apis/javascript/picassojs#%23%2Fdefinitions%2FComponentBox)
  component requires a “major” and “minor” scale.

## API Reference

- [Band](https://qlik.dev/apis/javascript/picasso-js/#definitions-scaleband) - [Linear](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalelinear)
- [Color - Categorical](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalecategoricalcolor)
- [Color - Sequential](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalesequentialcolor)
- [Color - Threshold](https://qlik.dev/apis/javascript/picasso-js/#definitions-scalethresholdcolor)
