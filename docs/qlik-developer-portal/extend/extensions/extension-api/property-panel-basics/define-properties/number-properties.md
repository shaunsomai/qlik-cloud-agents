---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/number-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Number properties

The number definition property template can be used to add a custom property of
number type. When defining a number property, the following fields can be used:

Definition properties

| Field          | Description                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | Used for all custom property type definitions. Can be either string, integer, number, array, or boolean.This field is mandatory and should always be "number" for a number property type definition. |
| `component`    | Used for defining how the property is visualized in the property panel. Used to override the default component that comes with the type setting.                                                     |
| `label`        | Used for defining the label that is displayed in the property panel.                                                                                                                                 |
| `ref`          | Name or ID used to reference a property.                                                                                                                                                             |
| `defaultValue` | Used for defining the default value of your custom property.                                                                                                                                         |
| `min`          | Used for defining the minimum value of the property.                                                                                                                                                 |
| `max`          | Used for defining the maximum value of the property.                                                                                                                                                 |

## Examples

Defining a custom property of number type can look like below.

### Example: Add custom number property to Appearance accordion

> **Note:** Customization of properties always starts with `items`.

```json
return {
  definition:{
     "items",
    component: "accordion",
    items: {
      settings: {
        uses: "settings",
        items: {
          MyNumProp: {
             "number",
            label: "Maximum",
            ref: "myproperties.max",
            defaultValue: "10.5"
          }
        }
      }
    }
  }
}
```

This is what it looks like in the property panel:

![Custom number entry field object
in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomNumProp.-MReD8x4.png)

You can also define a new accordion item as a number property.

### Example: Add custom number property as a new accordion item

```json
return {
  definition:{
     "items",
    component: "accordion",
    items: {
      MyAccordion: {
         "number",
        label: "Maximum value",
        ref: "myproperties.max",
        defaultValue: "10",
        max: "20"
      }
    }
  }
}
```

This is what it looks like in the property panel:

![Custom number entry field object
in extension as an accordion item](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomNumProp2.QkGgLmHd.png)
