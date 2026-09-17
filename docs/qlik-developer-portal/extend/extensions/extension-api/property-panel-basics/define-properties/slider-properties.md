---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/slider-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Slider properties

The slider definition property template can be used to add a custom property of
slider type. When defining a slider property, the following fields can be used:

Definition properties

| Field          | Description                                                                                                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`         | Used for all custom property type definitions. Can be either `string`, `integer`, `number`, `array`, or `boolean`.This field is mandatory and should always be `"number"` for a slider property type definition.> **Note:** The slider effect is achieved by setting the component field to `"slider"`; see below. |
| `component`    | Used for defining how the property is visualized in the property panel. Used to override the default component that comes with the type setting.This field is mandatory for a slider property and should always be `"slider"`.                                                                                     |
| `label`        | Used for defining the label that is displayed in the property panel.                                                                                                                                                                                                                                               |
| `ref`          | Name or ID used to reference a property.                                                                                                                                                                                                                                                                           |
| `defaultValue` | Used for defining the default value of your custom property.                                                                                                                                                                                                                                                       |
| `min`          | Used for defining the minimum value of the property.                                                                                                                                                                                                                                                               |
| `max`          | Used for defining the maximum value of the property.                                                                                                                                                                                                                                                               |
| `step`         | Used for defining the step value of the property.                                                                                                                                                                                                                                                                  |

## Examples

Defining a custom property of slider type can look like below.

Example: Add custom slider property to Appearance accordion

> **Note:** Customization of properties always starts with `items`.

```js
return {
  type: "items",
  component: "accordion",
  items: {
    settings: {
      uses: "settings",
      items: {
        MySliderProp: {
          type: "number",
          component: "slider",
          label: "Range",
          ref: "myproperties.range",
          min: 10,
          max: 20,
          step: 0.5,
          defaultValue: 15
        }
      }
    }
```

This is what it looks like in the property panel

![Custom slider with title
object in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomSliderProp.DYjzItC_.png)

You can also define a new accordion item as a slider property.

Example: Add custom slider property as a new accordion item

```js
return {
  type: "items",
  component: "accordion",
  items: {
  MyAccordion: {
    type: "number",
    component: "slider",
    label: "My slider",
    ref: "myproperties.range",
    min: 10,
    max: 20,
    step: 0.5,
    defaultValue: 15
  }
```

This is what it looks like with the slider property defined as an
accordion item in the property panel:

![Custom slider with title
object in extension as accordion item](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomSliderProp2.EiPj3AbY.png)
