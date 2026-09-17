---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/custom-integer-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Integer properties

The integer definition property template can be used to add a custom property of
integer type. When defining an integer property, the following fields can be used:

Definition properties

| Field          | Description                                                                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | Used for all custom property type definitions. Can be either string, integer, number, array, or boolean.This field is mandatory and should always be "integer" for an integer property type definition. |
| `component`    | Used for defining how the property is visualized in the property panel. Used to override the default component that comes with the type setting.                                                        |
| `label`        | Used for defining the label that is displayed in the property panel.                                                                                                                                    |
| `ref`          | Name or ID used to reference a property.                                                                                                                                                                |
| `defaultValue` | Used for defining the default value of your custom property.                                                                                                                                            |
| `min`          | Used for defining the minimum value of the property.                                                                                                                                                    |
| `max`          | Used for defining the maximum value of the property.                                                                                                                                                    |

## Examples

Defining a custom property of integer type can look like below.

### Example: Add custom integer property to Appearance accordion

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
          MyIntProp: {
             "integer",
            label: "Minimum",
            ref: "myproperties.min",
            defaultValue: "10"
          }
        }
      }
    }
  }
}
```

This is what it looks like in the property panel:

![Custom integer field with title in
extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomIntProp.DwWOYXGC.png)

You can also define a new accordion item as an integer property

### Example: Add custom integer property as a new accordion item

```json
return {
  definition:{  
     "items",
    component: "accordion",
    items: {
      MyAccordion: {
         "integer",
        label: "Min/Max",
        ref: "myproperties.min",
        defaultValue: "15",
        min: "10",
        max: "20"
      }
    }
  }
}
```

This is what it looks like in the property panel:

![Custom integer field with title
in extension as accordion object](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomIntProp2.DT4WxvWi.png)
