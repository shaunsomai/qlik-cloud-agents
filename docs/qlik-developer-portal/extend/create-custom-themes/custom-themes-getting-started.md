---
source: https://qlik.dev/extend/create-custom-themes/custom-themes-getting-started/
last_updated: 2026-06-02T18:15:45+01:00
---

# Get started building custom themes

In this example, you will create a basic theme extension where you'll modify
the font size and the primary colors.

## Creating the container

Create a folder that will contain your assets and name it `my-custom-theme`.

## Creating the definition file

The definition file defines how custom themes are loaded in Qlik Sense.

The QEXT file extension must be in lower case letters, as in `my-custom-theme.qext`.

> **Note:** Make sure your QEXT file is a valid JSON file.

JSON validator: [http://jsonlint.com](http://jsonlint.com/)

The following properties are mandatory for a valid custom theme definition file:

Definition file properties

| Property | Description                                                 |
| -------- | ----------------------------------------------------------- |
| name     | The name of the custom theme.                               |
| type     | Extension type. Should always be `theme` for custom themes. |

> **Tip:** Add additional properties to the QEXT file to provide helpful information about the custom component.

Example:

Create a QEXT file in the folder you just created and name it `my-custom-theme.qext`.

It should contain the following information:

```json
{
    "name": "Custom theme",
    "description": "My first custom theme",
    "type": "theme",
    "version": "1.0.0",
    "author": "Qlik"
}
```

## Creating the main JSON file

In the JSON file, you define the style for the individual visualization types.
Create a main JSON file and place it in the same folder as the QEXT file.
Name it theme.json, paste the following code into the JSON file, and then save it.

```json
{
  "_inherit": true,
  "_variables" : {
    "@greenColor" : "#61a729",
    "@text": "#4c4c4c"
  },
  "color": "@text",
  "fontSize": "12px",
  "object" : {
    "title": {
      "main": {
        "fontSize" : "16px"
      }
    }
  },
  "dataColors": {
    "primaryColor": "@greenColor"
  }
}
```

For more information on creating the JSON file and its properties, see [Custom theme JSON properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/define-properties/themes-properties).

## Prefixing custom themes

Custom themes are deployed to a shared tenant alongside themes from other developers
and vendors. Themes are identified by their folder name and the `name` property in the
QEXT file. If two themes share the same name, one will overwrite or conflict with the
other on the same tenant.

To avoid this, prefix all your names with a unique identifier - typically your company
or product name:

```text
my-custom-theme/          ← could clash with another developer's theme
acmecorp-custom-theme/    ← unique to your organisation
```

Apply the same prefix to the `name` field in the QEXT file:

```json
{
    "name": "AcmeCorp Custom Theme",
    "type": "theme"
}
```

This is the same convention as CSS class prefixes and scoped npm packages - a simple
way to carve out your own namespace in a shared environment.
