---
source: https://qlik.dev/extend/create-custom-themes/custom-themes-fontfamily-examples/
last_updated: 2025-11-21T14:05:39Z
---

# Create themes with custom fonts

These examples show how to set the font for text and labels in all built-in
charts using the custom theme JSON properties. By setting these JSON properties,
you can:

- Use both custom fonts and standard fonts.
- Set the font for the top level of the theme.
- Set the font for all lower levels of the theme.

> **Note:** Fonts from a custom theme are not supported when embedding Qlik objects cross-domain unless you use
> `<qlik-embed iframe="true">`. Using the `iframe="true"` mode may impact performance.

## Defining the font

You can specify the font of your choice for text and labels by defining the
`fontFamily` property in the main JSON file for the theme.

```json
"object": {
    "title": {
        "main": {
            "fontSize": "28px",
            "fontFamily": "Arial"
        }
    }
}
```

## Adding custom fonts using CSS

Custom fonts can be added to visualizations with the help of CSS. In this
example, you'll create a CSS file named `my_theme.css` to define the custom fonts.

> **Note:** Bundling font files with the theme extension is not supported in Qlik Cloud mashups.

```json
@font-face {
    font-family: "Alegreya Black";
    src: url("Alegreya-Black.ttf") format("truetype");
    font-weight: bold;
    font-style: normal;
}

@font-face {
    font-family: "YatraOne";
    src: url("YatraOne-Regular.ttf") format("truetype");
    font-weight: normal;
    font-style: normal;
}
```

Here is an example of the main JSON file that references the CSS file.

```json
{
    "_inherit": true,
    "customStyles": [
        {
            "cssRef": "my_theme.css",
            "classRef": "theme-style"
        }
    ],
    "fontFamily": "YatraOne",
    "object": {
        "title": {
            "main": {
                "fontSize": "28px",
                "fontFamily": "Alegreya Black"
            }
        }
    }
}
```

The contents of the theme folder for this example would look something like this:

- Alegreya-Black.ttf
- my\_theme.css
- my\_theme.json
- my\_theme.qext
- YatraOne-Regular.ttf
