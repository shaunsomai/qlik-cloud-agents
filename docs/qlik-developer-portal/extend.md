---
source: https://qlik.dev/extend/
last_updated: 2026-06-02T18:15:45+01:00
---

# Extending Qlik

Two types of add-on let you customize what Qlik Cloud Analytics looks like and how it works for
your users.

**Visualization extensions** are custom visualization objects built with standard web technologies.
You add them to a sheet in the same way as any native chart. Each extension receives data from the
Qlik Associative Engine, responds to selections made anywhere in the app, and can read the active
theme. Typical uses include custom chart types, third-party library integrations, and specialized
data presentations that the native objects do not cover.

**Themes** are JSON-based configurations that control the visual appearance of an app: colours,
typography, spacing, and the look of native charts. A theme applies at the app level. Extensions
can read the active theme through the Theme API, so they adapt automatically when a user or
administrator switches theme.

Both types of add-on are uploaded and managed through the Qlik Cloud Management Console and are
available to all apps on the tenant once deployed.

## Visualization extensions

Read the development guidelines before writing any code. They explain the rendering boundary,
which APIs are supported, what to avoid, and how to choose the right framework.

- [Extension development guidelines](extensions/extension-guidelines) - Supported APIs, anti-patterns, packaging requirements, and how to choose between nebula.js and the Extension API.
- [Visualization extensions overview](extensions/) - Understand the extension model and navigate to nebula.js or the Extension API.

### Build with nebula.js

nebula.js is the recommended framework for all new visualization extensions on Qlik Cloud.

- [Build your first extension](extensions/nebula-js/quickstart/first-extension) - Create a native visualization for Qlik Cloud using nebula.js.
- [Set up your nebula.js environment](extensions/nebula-js/set-up-nebula-environment/) - Install the nebula.js CLI and configure your development environment.
- [Deploy a visualization extension](extensions/nebula-js/deploy-extension/nebula-sense) - Package a custom visualization for use in Qlik Cloud Analytics.

### Legacy extension frameworks

If you have an existing solution built with the Extension API or picasso.js, take
a look at the technology overviews and tutorials. Consider
[migrating to nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula/) if you are
starting a significant update.

- [Extension API](extensions/extension-api/) - Explore the legacy Extension API, including data handling, property panels, and Picasso.js.
- [Get started with the Extension API](extensions/extension-api/create-with-extension-api/extension-get-started) - Learn the basics of building visualization extensions with the legacy Extension API.
- [Create visualizations with Picasso.js](extensions/picasso-js/get-started/) - Use the picasso.js charting library to build data visualizations inside extensions.

## Themes

Customize the appearance of your charts and Qlik Cloud Analytics applications.

- [Styling Qlik Cloud Analytics](create-custom-themes/) - Learn how themes make your analytics applications match your design language.
- [Making custom themes](create-custom-themes/custom-themes-getting-started) - Learn how to build themes you can add to Qlik Cloud.
- [Deploy a custom theme](https://qlik.dev/manage/platform-operations/add-custom-themes-and-extensions) - Upload a custom theme to Qlik Cloud so your end users can select it in their apps.
