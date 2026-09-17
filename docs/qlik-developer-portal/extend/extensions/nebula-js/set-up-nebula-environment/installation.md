---
source: https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/installation/
last_updated: 2026-06-02T18:15:45+01:00
---

# Installation

All `nebula.js` modules are available on the public npm registry as npm packages
and can be installed through either npm or as a script import.

`@nebula.js/stardust` is the primarily used module and it's required
when integrating `nebula.js` on the web.

## Script import

The easiest way to load the module is from a CDN like
`jsdelivr`:

```html
<script src="https://cdn.jsdelivr.net/npm/@nebula.js/stardust" crossorigin></script>
```

When imported using the script tag, it adds the variable `stardust` to the
global namespace.

For production, it's recommended to use a specific version of the module to
avoid surprises from newer or breaking versions of the APIs:

```html
<script src="https://cdn.jsdelivr.net/npm/@nebula.js/stardust@4.11.0" crossorigin></script>
```

## Npm or yarn

If you are building your own web project using Webpack, Rollup, Parcel, or
similar, you can install the package with npm:

```bash
npm install @nebula.js/stardust
```

or yarn:

```bash
yarn add @nebula.js/stardust
```

Notes:

`nebula.js` documentation use the package manager `npm`, `yarn` can be used interchangeable. You can compare `npm` and `yarn`
commands in [the yarn documentation](https://classic.yarnpkg.com/en/docs/migrating-from-npm#toc-cli-commands-comparison).

and then import `{ embed }` wherever you intend to embed a visualization:

```js
import { embed } from '@nebula.js/stardust';
```

## CLI

`nebula.js` provides a CLI to get you started with a project and
provides a development server to help you during the
development phase.

```bash
npm install @nebula.js/cli
```

If you would like to learn more about running `nebula.js` through the command
line, take a look
at [the nebula.js CLI Options page](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-cli/).

## Development builds

Some modules are available as a development build which provide more errors and
warnings for potential misuse of the APIs.
You should only use these during the development phase of your project, never
in production.

```html
<script src="https://cdn.jsdelivr.net/npm/@nebula.js/stardust@4.11.0/dist/stardust.dev.js" crossorigin></script>
```
