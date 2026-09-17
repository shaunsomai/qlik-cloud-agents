---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/string-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# String properties

The string definition property template can be used to add a custom property of
string type. When defining a string property, the following fields can be used:

Definition properties

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | Used for all custom property type definitions. Can be either string, integer, number, array, or boolean.This field is mandatory and should always be "string" for a string property type definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `label`        | Used for defining the label that is displayed in the property panel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ref`          | Name or ID used to reference a property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `defaultValue` | Used for defining the default value of your custom property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `expression`   | Used for defining if values starting with = will be treated as expressions which are evaluated by the Qlik associative engine. Can be either `"always"`, `"optional"` or `""` (empty).`"always"`: the property will always be evaluated as an expression meaning that the property will be the value of for example `"Avg(Sales)"`.`"optional"`: the property will only be evaluated as an expression if an = sign is leading the expression. For example `"Avg(Sales)"` will be presented as the string "Avg(Sales)" while `"=Avg(Sales)"` will be evaluated as an expression and presented as either 5 or "5" depending on if it is used in a Number/Integer component or in a String component.`""`: If the setting is left empty or not defined at all, the property will not be evaluated as an expression meaning that the property will be the string `"Avg(Sales)"`.> |
| `show`         | Function returning true if property should be displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `maxlength`    | The maximum number of characters the string can consist of.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Examples

Defining a custom property of string type can look like below.

![Custom string property entry
object in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomStringProp.DUMlbN9H.png)

#### Example: Add custom string property to Appearance accordion

> **Note:** Customization of properties always starts with `items`.

```json
return {
  definition:{
    type: "items",
    component: "accordion",
    items: {
      settings: {
        uses: "settings",
        items: {
          MyStringProp: {
            ref: "title",
            label: "My string property",
            type: "string",
            defaultValue: "MyNewExtension"
          }
        }
      }
    }
  }
};
```

This is what it looks like in the property panel

![Custom string property entry
object in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomStringProp.DUMlbN9H.png)

You can also define a new accordion item as a string property.

#### Example: Add custom string property as a new accordion item

```json
MyAccordion: {
  type: "string",
  label: "Description",
  ref: "description",
  defaultValue: "This is my description"
}  
```

![Custom string property entry object
in extension as accordion item](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomStringProp2.CtPgYTxb.png)
