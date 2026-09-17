---
source: https://qlik.dev/extend/create-custom-themes/
last_updated: 2026-03-25T12:14:39+01:00
---

# Custom theme overview

Qlik Sense comes with four default themes (Sense Classic, Sense Focus,
Sense Breeze, and Qlik Horizon) and in addition to these you can create custom
themes based on your company standards.

You do not need previous experience developing custom themes,
but you should have at least a basic understanding of JSON and JavaScript.

With custom themes you can precisely style an app by changing the colors, adding
images and backgrounds as well as specifying the font sizes and font colors on
a global or granular basis throughout your app. You can also define color
palettes to be used and customize the specifications for margins, padding, and spacing.

A custom theme is a collection of files stored in a folder. It must contain a
definition (QEXT) file, a main JSON file, and optionally any other assets you
might need to support the custom theme, such as CSS files, custom font files
and images.

> **Warning:** Document Object Model (DOM) selectors in custom CSS are not a supported pattern. While they can be
> helpful for customizing the look and feel of applications, the DOM is subject
> to change at any time. To provide your feedback, raise tickets on the [Qlik Ideation portal](https://community.qlik.com/t5/Ideation/ct-p/qlik-product-insight)
> when you need custom CSS customization. This helps prioritize supported
> customization options to add to the platform.

The custom styles are defined in the following way:

- In the JSON file you define the style for the individual visualization types,
  for example bar charts and line charts.

When you have created a custom theme, zip the JSON file with any additional resources
and upload it to Qlik Cloud as an extension.

> **Note:** Fonts from a custom theme are not supported when embedding Qlik objects cross-domain unless you use
> `<qlik-embed iframe="true">`. Using the `iframe="true"` mode may impact performance.
