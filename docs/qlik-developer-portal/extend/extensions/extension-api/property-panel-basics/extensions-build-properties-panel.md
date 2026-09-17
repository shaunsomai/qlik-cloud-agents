---
source: https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-build-properties-panel/
last_updated: 2026-06-02T18:15:45+01:00
---

# Build a properties panel

This section describes the basic principles behind defining and using properties
in visualization extensions.

Properties offers you a way of customizing the behavior of visualization
extensions in the same way as they would control native Qlik Sense
visualizations. A developer can use a programmatic interface to define
properties that are displayed in the properties panel exactly the same way as
they are in the native Qlik Sense visualizations.

## The properties panel

Properties are structured hierarchically, which is depicted in the following
properties panel accordion.

![Properties panel example, with Sections at the
top, Header at the top of the currently opened Section, and Items below the
Header](https://qlik.dev/_astro/ui-extension-get-started-08.BaaQpDq0.png)

- A: Sections
- B: Header
- C: Items

## Defining the properties panel

Properties are added by defining them in the definition property in the
JavaScript file. There are two ways of defining properties:

- [Reusing existing properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-reusing-properties/)
- [Adding custom properties](https://qlik.dev/extend/extensions/extension-api/property-panel-basics/extensions-add-custom-properties/)
