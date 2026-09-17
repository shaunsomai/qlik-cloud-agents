---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/working-with-styling/
last_updated: 2026-06-02T18:15:45+01:00
---

# Style your visualizations

Create visualizations for Qlik Sense using one of the following basic types of
Cascading Style Sheets (CSS):

- Inline: code is written into the tag and is only having an effect to the tag in
  which they are applied to.
- External: code is created in a separate document and are attached to the visualization.

> **Warning:** Do not append styles to `document.head`. Loading CSS into the host page's `head` element affects
> the entire Qlik Sense application, not just your extension, and will override Qlik's own styles.
> For more information, see [Extension development guidelines](https://qlik.dev/extend/extensions/extension-guidelines/).

> **Tip:** Keep your styling in a separate CSS file to separate content from presentation.
> Qlik Sense adds the CSS class `qv-object-[extension-name]` to your visualizations.
> Prefix your CSS rules with this class to scope your styles to your extension only.

Example: Prefix CSS rules

```javascript
.qv-object-com-qliktech-horizlist .qv-object-content {
    overflow: auto;
}
.qv-object-com-qliktech-horizlist ul {
    list-style: none;
}
.qv-object-com-qliktech-horizlist li.data {
    display: inline-block;
    margin: 3px;
    padding: 4px;
    border-top: 1px solid #ddd;
    border-left: 1px solid #ddd;
    border-bottom: 1px solid #111;
    border-right: 1px solid #111;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

## Loading style sheets

There are several ways of loading style sheets into your visualization extension:

- Loading and adding the content of a CSS file to the document header
- Adding a link to a style sheet to the document header
- Using the RequireJS CSS plugin

> **Note:** Make sure to prevent conflicts between existing styles or style definitions from other visualization extensions when
> you are creating style sheets.

### Loading and adding the content of a CSS file to the document header

You can use RequireJS and the `text!` prefix in the `define` statement to inject
the content into the header of the current document.

Qlik Sense includes the RequireJS plugin for loading text resources, which can
be used to load a specific CSS file. Assuming you have the following file structure:

![CSS file structure](https://qlik.dev/_astro/ui-extension-get-started-12.IGO7kOs4.png)

When prefixing a path with `text!`, the text plugin loads a file and passes its
content to a variable.

```javascript
define( [
        'jquery',
        'text!./css/myStyle.css'
    ], function ( $, cssContent ) {

        // cssContent now contains the content of myStyle.css

        // Inject the CSS declarations into the header of the current document
        $( '<style>' ).html(cssContent).appendTo( 'head' );

    } );
```

- `$("<style>")` creates a new object.
- The content of the `cssContent` variable is then assigned to the inner content
  of the `style` object.
- The style object, now including the CSS content, is added to the `<head>`
  section of the current document.

### Adding a link to a style sheet to the document header

You can add a link to the style sheet and append it to the head of the document.

```javascript
define( [
        "jquery"
    ], function ( $ ) {

        $('<link rel="stylesheet" type="text/css" href="/extensions/my-extension/css/myStyle.css">').appendTo("head");

    } );
```

### Using the RequireJS CSS plugin

You can use the CSS loader plugin of RequireJS to load your style sheets.

```javascript
define( [
        "jquery",
        "css!./css/myStyle.css"
    ], function ( $ ) {

        // Nothing more is needed

    } );
```

> **Note:** Using the RequireJS CSS plugin is supported as of Qlik Sense 2.0.

## Reusing CSS files for multiple visualizations

You can reuse your CSS file if you are creating multiple visualizations that
should have the same styling applied. Then store the CSS in a separate folder
and link to it from the visualizations for which it should apply.

## Short hand styling

To improve performance and make the CSS file load faster, it is good
programming practice to code your style sheet using short hand.

Example: Styling short hand

Instead of this:

```javascript
#potato {
    margin-left: 3px;
    margin-right: 4px;
    margin-top: 5px;
}
```

You should do this:

```javascript
#potato {
    margin: 5px 4px 0px 3px; // top, right, bottom and left values respectively.
}
```

## Examples

The below CSS examples are included in the Simple table code example,
included in your Qlik Sense installation.

Example: Loading CSS content and adding it to the HTML page

```javascript
define(["jquery", "text!./simpletable.css"],
function($, cssContent) {
    'use strict';
    $("<style>").html(cssContent).appendTo("head");
```

Example: simpletable.css

```javascript
.qv-object-com-qliktech-simpletable div.qv-object-content-container {
    overflow: auto;
}
.qv-object-com-qliktech-simpletable td,
.qv-object-com-qliktech-simpletable th {
    border-top: 0px solid #fff;
    border-bottom: 1px solid #ddd;
    border-right: 1px solid #ddd;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: middle;
    cursor: default;
    font-size: 12px;
}
.qv-object-com-qliktech-simpletable td.numeric {
    text-align: right;
}
.qv-object-com-qliktech-simpletable button {
    width: 100%;
}
```
