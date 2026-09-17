---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/extension-enable-export/
last_updated: 2026-06-02T18:15:45+01:00
---

# Enable export of your visualization extension

> **Warning:** In Qlik Cloud, visualization extensions support data export to XLSX if the chart includes a
> hypercube, but export to image, PDF, and PowerPoint is not supported. The image and report export
> functionality described on this page applies to Qlik Sense client-managed only.

By allowing users to export your visualization extensions, users can generate
insights and share them with people outside the boundaries of a Qlik Sense
system. For instance you can cooperate with customers and suppliers and take
decisions based on selected data.

To be able to export your visualization extensions, the export feature
must be enabled in the code of the visualization extension. The following export
functions can be enabled:

- Export to image
- Export to PDF
- Export story to PowerPoint
- Export story to PDF
- Export data

The following limitations apply:

- Qlik Sense does not support exporting or printing of visualization extensions
  that use external resources.

- Qlik Sense does not support exporting or printing of visualization extensions
  that use internal and undocumented JavaScript modules or APIs.

- When exporting as an image, the maximum size that can be exported is 2,000 by
  2,000 pixels. If the export would result in a larger image, the user must
  reduce the size under `Custom` in the `Export as an image dialog` in the app.

## Export to image, PDF, and PowerPoint

The export property is used to turn on or turn off the ability to export the
visualization extension as an image and as a PDF. It also allows the
visualization extension to be included in an export from data storytelling
(to PowerPoint or PDF). When `export` is set to `true`, the `Export as an image`
and the `Export to PDF` context menu options will be available for the visualization
extension. This also allows visualization extensions to be part of stories
exported to PowerPoint or PDF on the `Export story to PowerPoint` and
`Export story to PDF` context menu options.

Example: Export as an image

This example creates a deferred promise that is resolved when the image is
loaded. This ensures that the extension has finished rendering before the
`paint` method exits.

```javascript
define(['qlik'], function (qlik) {
    return {
        support: {
            export: true
        },
        paint: function ($element, layout) {
            const dfd = qlik.Promise.defer();
            const image = document.createElement('img');
            image.src = 'https://shorturl.at/iyHO0';
            image.onload = dfd.resolve;
            $element.append(image);
            return dfd;
        }
    };
});
```

Example: `export` property defined as a function

In this example, the `export` property is used as a function and does not allow
export to image when no data is available in the visualization extension.

```javascript
        definition : properties,
        support : {
            export: function( layout ) {
                return layout.qHyperCube.qDataPages[0].qMatrix.length;
            }
        },
        paint : function($element, layout) {
```

As well as this, you must set up the "finished rendering" notification in the
paint method.

## Export data

The `exportData` property is used to turn on or turn off the ability to export
data from the visualization extension and save it in an XLSX file. When set
to `true`, the `Export data` context menu option is enabled for the
visualization extension.

As well as this, you must set up the "finished rendering" notification in the
paint method.

> **Note:** The default value of the `exportData` property is `true`, which means that the option to export to data is enabled
> even if the property is not defined in the code.

Example: Basic example of `exportData` property

```javascript
        definition : properties,
        support : {
            exportData: true
        },
        paint : function($element, layout) {
```

Example: exportData as a function

In this example, the exportData property is used as a function and does not
allow export of data when no data is available in the visualization extension.

```javascript
        definition : properties,
        support : {
            exportData: function( layout ) {
                return layout.qHyperCube.qDataPages[0].qMatrix.length;
            }
        },
        paint : function($element, layout) {
```

## Set up "finished rendering" notification

To complete the enabling of export you must inform the printing service, in the
paint method, that the extension has finished rendering.

```javascript

    // ...,
    paint : function() {
        return qlik.Promise.resolve();
    }
    // ...
```

## Learn more

- [Extension API: export and exportData properties](https://qlik.dev/apis/javascript/extension/#definitions-extension)
