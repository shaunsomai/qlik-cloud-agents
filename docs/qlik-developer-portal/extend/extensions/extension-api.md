---
source: https://qlik.dev/extend/extensions/extension-api/
last_updated: 2026-06-02T18:15:45+01:00
---

# Extension API

> **Note:** The Extension API is the legacy framework for building visualization extensions. For new
> extensions, use [nebula.js](https://qlik.dev/extend/extensions/nebula-js/) instead. See the
> [extension development guidelines](https://qlik.dev/extend/extensions/extension-guidelines/)
> for guidance on choosing the right approach.

The Extension API uses RequireJS and passes a jQuery-wrapped `$element` to the `paint()` method.
It is still supported for existing extensions. The migration path to nebula.js is documented in
[Migrate a visualization extension to nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula).

> **Warning:** In Qlik Cloud, visualization extensions support data export to XLSX if the chart's data model
> includes a hypercube. Export to image, PDF, and PowerPoint is not supported for extensions in
> Qlik Cloud — those formats are only available on Qlik Sense client-managed.

- [Get started](create-with-extension-api/extension-get-started) - Learn the basics of building visualization extensions with the Extension API.
- [Build an extension](build-extension/) - Explore data handling, hypercubes, selections, and styling in extensions.
- [Property panels](property-panel-basics/) - Add properties to visualization extensions so end users can configure them.
- [Picasso.js](https://qlik.dev/extend/extensions/picasso-js/get-started/) - Use the Picasso.js charting library to build data visualizations inside extensions.
