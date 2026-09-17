---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/
last_updated: 2026-06-02T18:15:45+01:00
---

# Build an extension

Building a visualization extension with the Extension API involves several stages, from defining the
extension structure to adding interactivity and finishing touches.

## Steps overview

1. **Define the visualization structure** - every extension is made up of a backend *generic object*
   that holds the properties, and a frontend `paint()` method that renders the visual output.
   Start with [Visualization](https://qlik.dev/extend/extensions/extension-api/build-extension/visualization/) and
   [Generic object in visualization extensions](https://qlik.dev/extend/extensions/extension-api/build-extension/generic-object-viz-extension/).

2. **Configure data** - use `initialProperties` to specify the data your extension needs. A
   [HyperCube](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/) is the most common
   structure, mapping dimensions and measures to rows and columns.
   [qListObjectDef](https://qlik.dev/extend/extensions/extension-api/build-extension/qlistobjectdef/) is available
   for list-based extensions. See
   [Configuring data](https://qlik.dev/extend/extensions/extension-api/build-extension/configuring-data/) and
   [Consuming data](https://qlik.dev/extend/extensions/extension-api/build-extension/consuming-data/).

3. **Work with data** - access the data returned in the layout and render it. You can also
   [get additional data](https://qlik.dev/extend/extensions/extension-api/build-extension/get-additional-data/) by
   paging through large data sets.

4. **Handle selections** - allow users to interact with your visualization by
   [selecting data](https://qlik.dev/extend/extensions/extension-api/build-extension/selecting-data/). Review the
   available [selection models](https://qlik.dev/extend/extensions/extension-api/build-extension/selection-models/)
   to choose the right approach.

5. **Make the extension dynamic** - expose properties so users can configure the extension from the
   properties panel. See
   [Make your visualization extension dynamic](https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-make-dynamic/).

6. **Load external resources** - reference stylesheets, images, and other assets using the
   [resource loading](https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-load-resources/)
   approach.

7. **Apply styling and theming** - use
   [CSS styling](https://qlik.dev/extend/extensions/extension-api/build-extension/working-with-styling/) and
   integrate with the active Qlik Cloud
   [theme](https://qlik.dev/extend/extensions/extension-api/build-extension/theme-getting-started/) so your
   extension respects the app's appearance.

8. **Add finishing touches** - improve the authoring experience by adding a
   [preview image](https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-add-preview-image/).
   On Qlik Sense client-managed you can also
   [enable export](https://qlik.dev/extend/extensions/extension-api/build-extension/extension-enable-export/)
   to image, PDF, and PowerPoint. In Qlik Cloud, extensions support data export to XLSX if the
   chart includes a hypercube, but export to image, PDF, and PowerPoint is not supported.
