---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/working-with-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Work with properties

## Working with properties

The property panel of a visualization will render itself using a property
definition. This definition describes what the property panel should look like
and how it is connected to the data.

Some parts of the properties are reusable but you can also define your own
properties for your visualization.

### Reusable properties

The following accordion items on the property panel can be reused when creating
a property panel for your visualization:

- Dimensions
- Measures
- Sorting
- Add-ons
- Appearance

### Examples

This is the most basic example of a properties JavaScript file containing all
reusable property panel accordion items.

The Appearance accordion item in the property panel is named settings in the
code. See the example below.

```js
define( [], ( )=> {

  return {
     "items",
    component: "accordion",
    items: {
      dimensions: {
        uses: "dimensions"
      },
      measures: {
        uses: "measures"
      },
      sorting: {
        uses: "sorting"
      },
      addons: {
        uses: "addons"
      },
      settings: {
        uses: "settings"
      }
    }
  };
});
```

Example extension property panel

![Example of extension property panel](https://qlik.dev/_astro/ex_ExtensionPropertiesReuseAll.C9phUaF6.png)

## Custom properties

You can define your own properties for your visualization. Qlik Cloud
automatically adds them to the property panel and takes care of persistence. You
then find the selected values in the layout parameter. For every property, you
define a JavaScript object.

## Learn more

- [Reusing existing properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-reusing-properties/)
- [Adding custom properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-add-custom-properties/)
