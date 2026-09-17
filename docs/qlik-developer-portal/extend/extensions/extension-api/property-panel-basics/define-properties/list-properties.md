---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/list-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Array properties

> **Note:** This feature is considered experimental and may be subject to change or be removed in future releases.

The array definition property template can be used to add a custom property of
array type. When defining a list property, the following fields can be used:

Definition properties

| Field          | Description                                                                            |
| -------------- | -------------------------------------------------------------------------------------- |
| type           | This field is mandatory for array types and should always be defined as array.         |
| label          | Used for defining the label that is displayed in the property panel.                   |
| component      | This field should not be used for array types.                                         |
| ref            | Name or ID used to reference a property.                                               |
| itemTitleRef   | Used for defining the title of the section items.                                      |
| allowAdd       | Boolean.`true` adds a button for adding new items.                                     |
| allowRemove    | Boolean.`true` adds a Delete button.                                                   |
| addTranslation | Used for defining a label of the button used to add new items.                         |
| allowMove      | Boolean.`true` enables the ability to move the accordion item in the properties panel. |

> **Note:** Hypercubes and List objects cannot be added inside array property templates.
> You must initiate listItems in initialProperties.

## Example: Defining a custom array property

Defining a custom property of array type can look like below.

> **Note:** Customization of properties always starts with `items`.

```js
define( [
],
( ) => {

  return {
    initialProperties: {
      listItems: []
    },
    definition : {
      type : "items",
      component : "accordion",
      items: {
        settings: {
          uses: "settings",
          items: {
            MyList: {
               "array",
              ref: "listItems",
              label: "List Items",
              itemTitleRef: "label",
              allowAdd: true,
              allowRemove: true,
              addTranslation: "Add Item",
              items: {
                button: {
                  label:"Click me",
                  component: "button",
                  action: function(data){
                    alert("click!");
                  }
                },
                label: {
                   "string",
                  ref: "label",
                  label: "Label",
                  expression: "optional"
                },
                textarea: {
                  label:"My textarea",
                  component: "textarea",
                  maxlength: 100,//you shouldn't write too much
                  ref: "myTextarea"
                }
              }
            }
          }
        }
      }
    },
    paint: ($element) => {
      //add your rendering code here
      $element.html( "props-list" );
    }
  };
} );
```

This is what it looks like in the property panel
Custom array/list object in extension, with `Add Item` button:

![Custom array/list object in
extension, with Add Item button](data:image/png;base64,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)

This is what it looks like when an item has been added
Custom array/list object in extension, with `Add Item` button clicked and
fields/data entry available:

![Custom array/list object
in extension, with Add Item button clicked and fields/data entry available](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomListItemAdded2.Dg6jNgRl.png)
