---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/
last_updated: 2026-06-02T18:15:45+01:00
---

# Properties panel basics

The properties panel of your visualization extension is defined by a property
panel definition. The properties panel definition can be either added as a
separate JavaScript file or included in the main JavaScript file.

## The properties panel in Qlik Cloud

The properties panel is available on the right-hand side when you are editing a
visualization or a sheet. If it is hidden, turn on `Advanced options`.

Depending on the visualization you have created, you have different settings
options. Typically, you can do the following:

- Edit titles.
- Change the way the visualization appears on the sheets.
- Add dimensions and measures and specify how they are displayed.
- Set the sorting order and sorting criteria.

## Property templates

The properties panel has support for different templates that are rendered in
different ways. There are two main types of property templates:

- Hierarchical templates
- Plain templates

### Hierarchical property templates

The hierarchical property templates renders a UI structure.

### Plain property templates

The plain property templates are connected to an actual property value that is
persisted. Based on the plain property templates, you can create custom
properties of the following types:

- String
- Integer
- Number
- Check box
- Drop down
- Radio button
- Switch
- Slider
- Range-slider

## Reusable and custom properties

You can reuse property panel definitions that come built in with Qlik Cloud.
They include the following:

- Dimensions
- Measures
- Sorting
- Add-ons
- Appearance

In addition to the reusable properties, you can define your own properties for
your visualization. Qlik Cloud automatically adds them to the property panel
and takes care of persistence.

## Properties workflow

1. Create extension with properties panel, and make it available in Qlik Cloud.

2. Update value of property in the properties panel.

3. Properties are set and returned from the Engine as a blob.

4. New layout is applied and the extension re-renders/updates.

![Illustration of properties workflow](https://qlik.dev/_astro/dr_gen_ExtensionPropertiesFlow.BU96cUTP.png)

## Learn more

- [Reusing existing properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-reusing-properties/)
- [Adding custom properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-add-custom-properties/)
