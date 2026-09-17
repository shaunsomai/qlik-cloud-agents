---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-load-resources/
last_updated: 2026-06-02T18:15:45+01:00
---

# Load resources

You can use different types of resources in your visualization extensions, for example:

- Style sheets / CSS files
- JavaScript libraries
- Images
- Fonts
- Items from the content library

Qlik Sense loads resources asynchronously using RequireJS.

## Loading resources asynchronously using RequireJS

Qlik Sense uses RequireJS to take care of the asynchronous loading of resources.

```javascript
define( [ /* dependencies */ ],
    ( /* returned dependencies as arguments */ ) => {
        ...
    } );
```

> **Warning:** `jQuery` and `underscore` are being deprecated as built-in Extension API dependencies. Do not
> rely on Qlik to provide them via `require()`. Bundle these libraries directly in your extension
> instead. For more information, see [Extension development guidelines](https://qlik.dev/extend/extensions/extension-guidelines/).

jQuery is currently pre-configured as an internal dependency of Qlik Sense, so there is
no need to explicitly load it in existing extensions. By defining the dependency in the
first parameter of the `define` function, you ensure jQuery is loaded and that
the return value of this library will be passed as the first parameter in the
function (the second argument of `define`).

Loading the predefined dependency of jQuery looks like the following:

```javascript
define( [ "jquery" ],
    ( $ ) => {
        'use strict';
        return {

            paint: ( $element, layout ) => {
                // We can use jQuery here
                console.log($('head'));
            }
        };
    } );
```

## Style sheets / CSS files

There are several ways of loading style sheets into your visualization extension:

- Loading and adding the content of a CSS file to the document header
- Adding a link to a style sheet to the document header
- Using the RequireJS CSS plugin

> **Note:** Make sure to prevent conflicts between existing styles or style definitions from other visualization extensions when
> you are creating style sheets.
> For more information, see [Style your visualizations](https://qlik.dev/extend/extensions/extension-api/build-extension/working-with-styling/).

> **Tip:** It is good programming practice to keep your styling in a separate CSS file.
> Separating the content from the design makes it easier to maintain your visualizations.
> Qlik Sense sets the CSS class `qv-object-[extension name]` on your visualizations and your CSS rules should be
> prefixed with that.

### Loading and adding the content of a CSS file to the document header

You can use RequireJS and the `text!` prefix in the `define` statement to inject
the content into the header of the current document.

Qlik Sense includes the RequireJS plugin for loading text resources, which can
be used to load a specific CSS file. Assuming you have the following file structure:

![UI extensions get started file
structure](https://qlik.dev/_astro/ui-extension-get-started-12.IGO7kOs4.png)

When prefixing a path with `text!`, the text plugin loads a file and passes its
content to a variable.

```javascript
define( [ 
        'jquery',
        'text!./css/myStyle.css' 
    ], ( $, cssContent ) => {

        // cssContent now contains the content of myStyle.css

        // Inject the CSS declarations into the header of the current document
        $( '<style>' ).html(cssContent).appendTo( 'head' );

    } );
```

- `$("<style>")` creates a new object.
- The content of the `cssContent` variable is then assigned to the inner content
  of the `style` object.
- The style object, now including the CSS content, is added to
  the `<head>` section of the current document.

### Adding a link to a style sheet to the document header

You can add a link to the style sheet and append it to the head of the document.

```javascript
define( [ 
        "jquery"
    ], ( $ ) => {

        $('<link rel="stylesheet" type="text/css" href="/extensions/my-extension/css/myStyle.css">').appendTo("head");

    } );
```

### Using the RequireJS CSS plugin

You can use the CSS loader plugin of RequireJS to load your style sheets.

```javascript
define( [ 
        "jquery",
        "css!./css/myStyle.css" 
    ], ( $ ) => {

        // Nothing more is needed

    } );
```

## JavaScript libraries

You can load local or external JavaScript files.

### Loading local JavaScript files

Use RequireJS to add the local JavaScript file as a dependency:

```javascript
define([
        './lib/js/extensionUtils'
],
( extensionUtils ) => {
    'use strict';

    return {
        paint: ( $element, layout ) => {

            extensionUtils.doSomething();

        }
    };
});
```

### Loading external JavaScript files

If you want to load resources from a Content Delivery Network (CDN), see this example:

```javascript
define([
        '//code.highcharts.com/highcharts.js'
],
( highCharts ) => {
    'use strict';

    return {
        paint: ( $element, layout ) => {

            // do something with highCharts

        }
    };
});
```

> **Tip:** Loading JavaScript files from a CDN is a good approach if you use the same library in several visualization
> extensions, since the browser does not need to load the resource again.
> It's also a good approach if you're certain that users of your visualization extension have Internet access.

> **Note:** Qlik Sense does not support exporting or printing of visualization extensions that use external resources.

## Learn more

- [RequireJS CSS loader plugin](https://github.com/guybedford/require-css)
- [Style your visualizations](https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-load-resources/working-with-styling)
