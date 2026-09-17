---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/radiobutton-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Radio button properties

The radio button definition property template can be used to add a custom
property of radio button type. When defining a radio button property, the
following fields can be used:

Definition properties

| Field          | Description                                                                                                                                                                                                                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`         | Used for all custom property type definitions. Can be either `string`, `integer`, `number`, `array`, or `boolean`.This field is mandatory and should always be `"string"` for a radio button property type definition.> **Note:** The radio button effect is achieved by setting the component field to `"radiobuttons"`; see below. |
| `component`    | Used for defining how the property is visualized in the property panel. Used to override the default component that comes with the type setting.This field is mandatory for a radio button property and should always be `"radiobuttons"`.                                                                                           |
| `label`        | Used for defining the label that is displayed in the property panel.                                                                                                                                                                                                                                                                 |
| `ref`          | Name or ID used to reference a property.                                                                                                                                                                                                                                                                                             |
| `defaultValue` | Used for defining the default value of your custom property.                                                                                                                                                                                                                                                                         |
| options        | Array of options. Can be `value`, `label`, and `function`.Example:`options: [{``value: "v",``label: "Vertical"``}, {``value: "h",``label: "Horizontal"``}],`                                                                                                                                                                         |

## Examples

### Fetching options from an external resource

> **Note:** This example is using jQuery. Make sure to have jQuery included as a require-dependency.

```js
return {
  type: "items",
  component: "accordion",
  items: {
    settings: {
      uses: "settings",
      items: {
        MyDropdownProp: {
          type: "string",
          component: "dropdown",
          label: "Data source",
          ref: "myproperties.datasource",
          options: () => {
            return $.get("datasource.php").then((items) => {
              return items.map((item) => {
                return {
                  value:item.toLowerCase(),
                  label:item
                };
              });
            });
          }
```

> **Note:** Options will be fetched every time a property is changed.
> To avoid repeating reloads, cache the result from the web service.

### Defining custom radio buttons

Defining a custom property of radio button type can look like below.

Example: Add custom radio button property to Appearance accordion

> **Note:** Customization of properties always starts with `items`.

```js
return {
  type: "items",
  component: "accordion",
  items: {
    settings: {
    uses: "settings",
    items: {
      MyRadiobuttongroupProp: {
        type: "string",
        component: "radiobuttons",
        label: "Orientation radio-buttons",
        ref: "myproperties.orientation",
        options: [{
          value: "v",
          label: "Vertical"
        }, {
          value: "h",
          label: "Horizontal"
        }],
        defaultValue: "v"
      }
    }
  }
```

This is how it appears in the property panel.

![Custom radio buttons with
title object in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomRadiobttnProp.BQpT3zVG.png)

You can also define a new accordion item as a radio button property.

Example: Add a custom radio button property as a new accordion item

```js
return {
  type: "items",
  component: "accordion",
  items: {
    MyAccordion: {
      type: "string",
      component: "radiobuttons",
      label: "Orientation radio-buttons",
      ref: "myproperties.orientation",
      options: [{
        value: "v",
        label: "Vertical"
      }, {
        value: "h",
        label: "Horizontal"
      }],
      defaultValue: "v"
    }
```

This is how it appears in the property panel.

![Custom radio buttons with
title object in extension as an accordion item](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomRadiobttnProp2.BtD-ftfY.png)
