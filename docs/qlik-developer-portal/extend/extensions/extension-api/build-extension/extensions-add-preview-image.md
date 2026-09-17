---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-add-preview-image/
last_updated: 2026-06-02T18:15:45+01:00
---

# Add a custom preview image

This section describes how to add a custom preview image to your visualization
extension. The preview image is displayed in the preview window which is
accessed by selecting the visualization extension from the library.

Do the following:

1. Create a new image and save it as a PNG file. It should be saved in the same
   folder as your other extension files.

   > **Note:** The recommended size for a custom preview image is 140 x 140 pixels.

2. Update the QEXT file by adding the preview property as shown below. This
   example uses the Qlik Sense logo as an image.

   ```json
   {
   "name" : "Extension Tutorial - Hello World",
   "description" : "Extension Tutorial, Simple Hello World.",
   "icon" : "extension",
   "preview" : "qlik-sense-logo.png",
   "type" : "visualization",
   "version": "0.1",
   "author": "Your Name"
   }
   ```

You have now added a custom preview image.
