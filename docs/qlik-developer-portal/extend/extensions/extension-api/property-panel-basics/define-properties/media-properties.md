---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/media-properties/
last_updated: 2026-06-02T18:15:45+01:00
---

# Media properties

> **Note:** This feature is considered experimental and may be subject to change or be removed in future releases.

The media definition property template can be used to add a custom property of
media type. When defining a media property, the following fields can be used:

Definition properties

| Field       | Description                                                                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`      | This field is mandatory for media. Can be either `string`, `integer`, `number`, `array`, or `boolean`.Should always be defined as `string` for media items.> **Note:** The media effect is achieved by setting the `component` field to `"media"`; see below. |
| `label`     | Used for defining the label of the item.                                                                                                                                                                                                                      |
| `component` | Used for defining how the property is visualized in the property panel.Used to override the default component that comes with the type setting.This field is mandatory for a link property and should always be `"media"`.                                    |
| `ref`       | Name or ID used to reference a property.                                                                                                                                                                                                                      |
| `layoutRef` | Name or Id used to reference the layout.> **Note:** Adding media from the In app media library is not supported.                                                                                                                                              |

## Example

### Defining a custom media property

Defining a custom property of media type can look like below.

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
              MyMedia: {
                label:"My media",
                component: "media",
                ref: "myMedia",
                layoutRef: "myMedia",
                type: "string"
              }
            }
        }
      }
    },
    paint: ($element, layout) => {
      //add your rendering code here
      $element.css("background-size","cover");
      $element.css("background","url("+layout.myMedia+") no-repeat left top fixed");
      $element.html( "props-media "+layout.myMedia );
    }
  };

} );
```

This is what it looks like in the property panel

![Custom media selection object
in extension](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomMediaProp.K1g0x0Oi.png)

This is what it may look like after selecting to display an image

![Custom media selection object
in extension, displaying selected media](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomMediaPropCircles.B_ujreUo.png)

And this is what the visualization itself may look like after selecting to
display an image

![Custom media selection object
in sheet, displaying properties of the selected media](https://qlik.dev/_astro/ex_ExtensionPropertiesCustomMediaEditModeCircles.QEm-OzmA.png)
