---
source: https://qlik.dev/extend/extensions/picasso-js/get-started/installation/
last_updated: 2026-06-02T18:15:45+01:00
---

# Installation

`picasso.js` and the plugins `picasso-plugin-hammer`, `picasso-plugin-q` are
available on the public npm registry as npm packages and can be installed
through either npm or as a script import.

## Script import

The easiest way to load the module is from a CDN like `jsdelivr`:

```html
<script src="https://cdn.jsdelivr.net/npm/picasso.js" crossorigin></script>
```

When imported using the script tag, it adds the variable `picasso` to
the global namespace.

For production, it is recommended to use a specific version to avoid surprises
from newer or breaking versions of the APIs:

```html
<script src="https://cdn.jsdelivr.net/npm/picasso.js@1.0.0" crossorigin></script>
```

## Npm or yarn

If you are building your own web project using Webpack, Rollup, Parcel, or
similar you can install the package with npm:

```bash
npm install picasso.js
```

or yarn:

```bash
yarn add picasso.js
```

and then to use it:

```js
import picassojs from 'picasso.js';
```
