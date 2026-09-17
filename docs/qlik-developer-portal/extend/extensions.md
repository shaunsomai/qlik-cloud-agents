---
source: https://qlik.dev/extend/extensions/
last_updated: 2026-06-02T18:15:45+01:00
---

# Visualization extensions

A visualization extension is a custom visualization object that you build with standard web
technologies. When placed on a sheet, it behaves like any native Qlik chart: it receives data from
the Qlik Associative Engine via a hypercube, participates in the app's selection state, and responds
to active themes. The extension renders inside a bounded element allocated by the sheet; everything
outside that boundary belongs to Qlik and must not be modified.

> **Tip:** **New to extensions?** Follow the [Build your first extension](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension/)
> tutorial to have a working visualization running in Qlik Cloud in about 30 minutes.

## Choose your tools

Two frameworks manage the integration between your code and Qlik Cloud - lifecycle, data binding,
selections, and themes - and one rendering library works with either of them.

| Tool              | Role                | Use when                                                 |
| ----------------- | ------------------- | -------------------------------------------------------- |
| **nebula.js**     | Extension framework | Building a new extension on Qlik Cloud                   |
| **Extension API** | Extension framework | Maintaining an existing Extension API extension          |
| **picasso.js**    | Rendering library   | Building custom chart components inside either framework |

For new work, choose nebula.js as your framework. The Extension API remains supported but is no
longer the recommended path. If you are starting a significant update to an existing Extension API
extension, consider
[migrating to nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula/) as
part of that work.

picasso.js is not an alternative to these frameworks - it is a charting library you can use inside
either one. It provides a component model for assembling charts from axes, marks, and scales similar to
libraries like D3, but with simplified APIs tailored for data visualization. Its `picasso-plugin-q`
understands the Qlik hypercube format natively, so you do not need to transform data before rendering.
Use it when you need a custom chart type that goes beyond what your framework provides out of the box.

> **Note:** Before writing any code, read the [extension development guidelines](https://qlik.dev/extend/extensions/extension-guidelines/).
> They define which APIs are supported, which patterns to avoid, and why.

- [Extension development guidelines](extension-guidelines) - Supported APIs, anti-patterns, packaging requirements, and how to choose your framework.
- [Configure your extension package](qext-file-overview) - The QEXT file is the package manifest for your extension. Define its name, version, icon, and preview image.
- [nebula.js](https://qlik.dev/extend/extensions/nebula-js/) - The recommended framework for new visualization extensions on Qlik Cloud.
- [Extension API](https://qlik.dev/extend/extensions/extension-api/) - The legacy framework. Use for existing extensions or when migrating to nebula.js.
- [Picasso.js](https://qlik.dev/extend/extensions/picasso-js/get-started/) - A rendering library for custom chart components. Works inside both nebula.js and the Extension API.
