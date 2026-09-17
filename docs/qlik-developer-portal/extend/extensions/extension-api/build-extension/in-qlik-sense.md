---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/in-qlik-sense/
last_updated: 2026-06-02T18:15:45+01:00
---

# Load an extension into Qlik Sense

A visualization developed with nebula.js can be brought into Qlik Sense as
an extension. A property panel can be defined to allow adjustments of
settings for the visualization.

## Exposed from Qlik Sense

When a nebula.js extension is loaded in Qlik Sense it gets
a set of useful tools passed into the supernova function.

```js
export default function (galaxy) {
  return {
    ext,
    qae,
    component() {},
  };
}

/* Contents of galaxy */
galaxy: {
  anything: {
    sense: {
      navigation,
      theme,
    },
  },
  deviceType,
  translator,
}
```

The `ext` and `qae` has to be defined without access to the hooks from nebula.js
(the hooks are only available to use from within the `component` function).
For this purpose, the tools passed in with `galaxy` from Qlik Sense can come in handy.

### navigation

A module allowing navigation within Qlik Sense. It provides the following set
of functions for navigation between sheets and stories:

```js
getCurrentSheetId();
getCurrentStoryId();
getUrlForSheet(sheetId);
goToSheet(sheetId);
goToStory(storyId);
nextSheet();
prevSheet();
```

### theme

A module providing tools to work with the theme that is currently set in Qlik
Sense.

> **Note:** This module is similar to, but not the same as, the one from `useTheme`.
> For more information, see [Theme](https://qlik.dev/apis/javascript/nebulajs-stardust#%23%2Fdefinitions%2FTheme).

### deviceType

Active device type in Qlik Sense (automatically identified or manually enforced through settings).
Could be either `"desktop"` or `"tap"`.

> **Note:** This is similar to, but not the same as, the one from `useDeviceType`.

### translator

A translation tool for adding or retrieving translations.

> **Note:** This module is similar to, but not the same as, the one from `useTranslator`.
> For more information, see [Translator](https://qlik.dev/apis/javascript/nebulajs-stardust#%23%2Fdefinitions%2FTranslator).

## Property panel

The properties panel of your visualization extension is defined by a property
panel definition. The `definition` in the `ext` section is where the property
panel definition should reside.

```js
export default function (galaxy) {
  return {
    ext: {
      definition: {
        /* Property panel definition goes here */
        // The theme, translator and deviceType passed in through galaxy can be used in here.
      },
    },
    qae: {},
    component() {},
  };
}
```

Here is an example of a simple property panel:

```js
// Some components
const item1 = {
    ref: 'props.section1.item1',
    label: 'Item 1',
    type: 'string',
    expression: 'optional'
};

//...

// Supernova definition
export default function (galaxy) {
  return {
    ext: {
      definition: {
        type: 'items',
        component: 'accordion',
        items: {
          component: 'expandable-items',
          label: galaxy.anything.translator.get("labels.mysection"),
          items: {
            header1: {
              type: 'items',
              label: 'Header 1',
              items: {
                item1,
                item2,
              },
            },
          },
        },
      },
    },
    // ...
  };
```

Here is how it appears in Qlik Sense:

![Qlik Sense property panel](https://qlik.dev/_astro/sense-property-panel.tz2ZncXS.png)

For more information on how to create a property panel definition,
see [Build a properties panel](https://qlik.dev/extend/extensions/extension-api/build-extension/property-panel-basics/extensions-build-properties-panel).
