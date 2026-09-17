---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/link-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Link properties

The link definition property template can be used to add a custom property of
link type. When defining a link property, the following fields can be used:

Definition properties

| Field       | Description                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`      | This field is optional for links. Can be either `string`, `integer`, `number`, `array`, or `boolean`.> **Note:** The link effect is achieved by defining the component field to `link`,; see below.                      |
| `component` | Used for defining how the property is visualized in the property panel. Used to override the default component that comes with the type setting.This field is mandatory for a link property and should always be `link`. |
| `label`     | Used for defining the label that is displayed on the link.                                                                                                                                                               |
| `url`       | Used for defining the web address used in the link.> **Note:** Links are always opened in your default web browser when clicked.                                                                                         |

## Example

### Defining a custom button

Defining a custom property of link type can look like below.

Example:

> **Note:** Customization of properties always starts with `items`.

```js
define( [
],
  ( ) => {
    return {
      definition : {
        type : "items",
        component : "accordion",
        items: {
          settings: {
            uses: "settings",
            items: {
              MyLink: {
                label:"My Link",
                component: "link",
                url:"http://www.qlik.com/"
              }
            }
          }
        }
      },
      paint: ($element) => {
        //add your rendering code here
        $element.html( "props-link" );
      }
    };
  } );
```

This is what it looks like in the property panel

![Custom hyperlink object in
extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomLinkProp.DJmRbmKk.png)
