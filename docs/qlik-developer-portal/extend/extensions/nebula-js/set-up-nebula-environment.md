---
source: https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/
last_updated: 2026-06-02T18:15:45+01:00
---

# Overview - Set up your environment

`nebula.js` is a collection of JavaScript libraries, visualizations, and CLIs that helps developers
build and integrate visualizations on top of Qlik's Associative Engine. All packages are published
under the `@nebula.js` scope on npm. The primary package, `@nebula.js/stardust`, provides the APIs
for embedding visualizations in mashups and for building custom chart extensions.

This section covers setting up a nebula.js development environment:

- [Installation](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/installation/) -
  Load `@nebula.js/stardust` via a CDN script tag or install it with npm or yarn. Also covers
  installing `@nebula.js/cli` and using development builds during local development.
- [nebula create](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-create/) -
  Scaffold a new visualization project using `nebula create <name>`. Covers options for package
  manager, picasso.js template, and skipping dependency installation.
- [nebula serve](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-serve/) -
  Run a local development server with hot reload against a Qlik Associative Engine or Qlik Cloud
  tenant. Covers all server options and the `nebula.config.js` configuration file.
- [nebula CLI](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-cli/) -
  Full CLI reference for `nebula create`, `nebula build`, `nebula serve`, and `nebula sense`.
  Includes how to install globally, use via `npx`, and test a modified CLI locally.
