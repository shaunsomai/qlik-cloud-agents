---
source: https://qlik.dev/extend/extensions/extension-guidelines/
last_updated: 2026-06-02T18:15:45+01:00
---

# Extension development guidelines

Visualization extensions run directly inside the Qlik Cloud host page, in a DOM (Document Object Model)
element allocated for the extension.
This makes it possible to build rich custom visualizations, but it also means your code must stay within clearly
defined boundaries.

Your responsibility is to modify only the code inside the allocated element. Everything outside it belongs to Qlik and
is off-limits. If you respect this boundary, your extension should remain compatible with future platform updates.
If you cross it, you risk silent failures and support issues for your users.

This page explains which APIs are supported, which must not be used, and why.

## Choose your development approach

If you are building a visualization extension:

| Scenario                                       | Recommended approach                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New visualization extension on Qlik Cloud      | `nebula.js`                                                                                                                                              |
| Migrating an existing Extensions API extension | `nebula.js`. See [Migrate a visualization extension to nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula/) |

### nebula.js (recommended)

nebula.js is the recommended framework for all new visualization extensions.\
You can use it with React, Vue, Svelte, or any modern front-end framework.\
It eliminates RequireJS and jQuery as mandatory dependencies, and integrates with\
modern front-end tooling through a local development server (`nebula serve`).

nebula.js exposes a set of hooks from `@nebula.js/stardust` such as `useElement`, `useLayout`, and
`useEffect`, that provide controlled, lifecycle-aware access to the extension's rendering element,
data, and selection state.

### Extensions API (legacy)

The Extensions API uses RequireJS and passes a jQuery-wrapped `$element` to the `paint()` method. It is still
supported but is no longer the recommended path for new extensions.

It carries jQuery as a mandatory dependency. Modern frameworks such as React and Vue expect exclusive
ownership of the DOM; jQuery's imperative mutations will conflict with their rendering model, increasing bundle
size and risking unpredictable behaviour. The migration path to nebula.js is documented at
[Migrate a visualization extension to nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula/).

> **Note:** Qlik is deprecating `underscore` and `jQuery` as libraries that extensions can access via
> `require()`. Extensions that currently depend on these must bundle the libraries themselves rather
> than relying on Qlik to provide them.

## Use only supported APIs

The following APIs are officially documented and tested by Qlik, and are permitted in extensions.
Restrict your code to these interfaces.

### nebula.js stardust hooks

Every extension starts with these:

- `useElement()`: access the `HTMLElement` allocated to the extension. Render only within this element.
- `useLayout()` / `useStaleLayout()`: access the [generic object](https://qlik.dev/extend/extension-api/build-extension/generic-object-viz-extension)
  layout and hypercube data.

Then add hooks based on what your extension needs to do:

- `useModel()`: interact with the generic object via the Qlik Associative Engine API.
- `useEffect()`: run side effects in response to layout or selection changes.
- `useRect()`: respond to size changes of the rendering element.
- `useTheme()`: resolve colors and font sizes from the active Qlik theme.

For complete details, see the [nebula.js stardust API reference](https://qlik.dev/apis/javascript/nebula-js/).

### Qlik Associative Engine API

Use enigma.js or `@qlik/api` to communicate with the Qlik Associative Engine. For more information,
see the [enigma.js overview](https://qlik.dev/toolkits/enigma-js/).

Key methods relevant to extensions:

- `qHyperCubeDef`: define dimensions, measures, and data fetch parameters.
  For more information, see the [hypercube introduction](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/).
- `getHyperCubeData()`: page through data beyond the initial fetch.
- `createSessionObject()` / `destroySessionObject()`: manage session-scoped generic objects.
  When the extension unmounts (when the user navigates away or closes the app), you must call destroySessionObject() to
  close the WebSocket subscription."
- `selectHyperCubeValues()` and equivalent selection methods: make associative selections.

## Anti-patterns: What not to do and why

The following patterns appear in extension code found in Qlik Community and in partner extensions.
Each one is brittle in ways that are not immediately obvious and generates support incidents when
Qlik ships a platform update.

### Anti-pattern 1: Manipulating host DOM outside the extension element

**What it looks like**

Using `document.querySelector()`, `$(document)`, or similar to find and modify elements in the
Qlik Sense application shell, for example hiding toolbar items, repositioning sheet elements, or
overriding application chrome.

**Why you must not do this**

The DOM structure of the Qlik Sense host application is internal and is not documented or versioned
as a public API. Qlik makes structural changes to the host page with every major release. When those
changes ship, extensions that depend on specific element IDs, class names, or DOM hierarchy break
without warning. The breakage is difficult to diagnose because the extension code itself has not
changed; only the surrounding page structure has. Qlik does not test extensions against internal DOM
structures.

A real-world example: third-party extensions that overlay their own navigation bar on top of Qlik's
topbar assume a fixed height for the host topbar. When Qlik changes that height, even by a few pixels
for entirely internal reasons, the overlay misaligns. The extension must then be patched for every
such change, which Qlik cannot co-ordinate or give advance notice of.

```js
// ❌ BAD: queries host application DOM
document.querySelector('.qv-toolbar').style.display = 'none';
$('.qv-panel-sheet').css('padding', '0');

// ✅ GOOD: operates only within the allocated element
const { useElement } = require('@nebula.js/stardust');

component() {
  const element = useElement();
  element.style.padding = '0'; // safe: this is your element
}
```

### Anti-pattern 2: Injecting global CSS that affects the host application

**What it looks like**

Adding a `<style>` tag to `document.head`, using `!important` overrides against Qlik class names
like `.qv-inner-object` or `.qv-object`, or loading a CSS framework such as Bootstrap without
namespacing it.

**Why you must not do this**

Global CSS affects the entire host page, not just your extension. CSS class names in the host
application are internal. Qlik has shipped releases in which theme and layout class names changed,
breaking extensions and custom themes that depended on them. Injecting `!important` overrides makes
the order of CSS application unpredictable across the page. A CSS framework loaded without
namespacing overrides Qlik's global styles, causing host UI elements to disappear.

```js
// ❌ BAD: injects a global style that affects the host page
const style = document.createElement('style');
style.innerHTML = `.qv-inner-object { padding: 0 !important; }`;
document.head.appendChild(style);

// ❌ BAD: loads Bootstrap globally, overrides host application styles
require('bootstrap/dist/css/bootstrap.css');

// ✅ GOOD: scope all styles to a class unique to your extension
const style = document.createElement('style');
style.innerHTML = `.my-ext-container { font-family: Arial; }`;
element.appendChild(style); // scoped to your element, not document.head

// ✅ GOOD: use the Qlik Theme API for colors and typography
const { useTheme } = require('@nebula.js/stardust');
const theme = useTheme();
const color = theme.getStyle('', '', 'color');
```

> **Tip:** Use the nebula.js Theme API (`useTheme()`) to read colors, font sizes, and spacing from the
> active Qlik theme rather than hardcoding values. This ensures your extension adapts correctly to
> both the default theme and any custom themes deployed on the tenant, including dark mode.

### Anti-pattern 3: Accessing internal or undocumented Qlik JavaScript modules

**What it looks like**

Using RequireJS `require()` paths that reference Qlik's internal module system, for example
`qvangular`, `qlik-stable`, internal AngularJS services, or the `autogenerated/qix/engine-api`
module. Also includes using `window.qlik` or any undocumented property set on the global scope by
the host application.

**Why you must not do this**

Internal JavaScript module paths are not public APIs. They do not appear in any official API
documentation. The modules `util` and `autogenerated/qix/engine-api` are unsupported and may be
renamed, removed, or replaced without notice in any platform update. Extensions relying on internal
modules have required emergency code changes after platform updates.

Use only the APIs listed in the preceding [Use only supported APIs](#use-only-supported-apis) section.

```js
// ❌ BAD: accesses Qlik's internal module system
require(['qvangular', 'qlik'], function(qvangular, qlik) { /* ... */ });
require(['autogenerated/qix/engine-api'], function(engineApi) { /* ... */ });

// ✅ GOOD: access the model via the nebula.js hook
import { useModel } from '@nebula.js/stardust';
const model = useModel(); // official, lifecycle-managed access
```

> **Warning:** Some functionality available through internal APIs, such as reading master dimension color segments
> via `layout.qHyperCube.qDimensionInfo[0].coloring.colorMapRef`, does not have an official public
> equivalent. Code that uses undocumented structures like this has no compatibility guarantee and may
> break at any Qlik Cloud release without prior notice.

### Anti-pattern 4: Fetching excessive hypercube data in a single request

**What it looks like**

Setting a large `qInitialDataFetch`, for example `qHeight: 10000, qWidth: 20`, in an attempt to load
all data at once, or rendering all returned rows to the DOM simultaneously.

**Why you must not do this**

The Qlik Engine enforces a hard limit of 10,000 cells per data page request
(`qWidth × qHeight ≤ 10,000`). Exceeding this causes an error. Beyond the limit, requesting large
pages and rendering all rows to the DOM at once can cause `GetLayout()` timeouts on large production
datasets and freeze the browser. The [hypercube documentation](https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/)
notes that datasets can reach millions of rows and that developers must take care when dynamically
fetching data.

```js
// ❌ BAD: 20 × 10,000 = 200,000 cells; exceeds the limit and errors
qInitialDataFetch: [{ qTop: 0, qLeft: 0, qWidth: 20, qHeight: 10000 }]

// ✅ GOOD: fetch a reasonable initial page
qInitialDataFetch: [{ qTop: 0, qLeft: 0, qWidth: 5, qHeight: 500 }]
// 5 × 500 = 2,500 cells, within the limit

// ✅ GOOD: page for additional data on demand
const layout = await model.getLayout();
const totalRows = layout.qHyperCube.qSize.qcy;
const pageSize = 1000;

for (let i = 0; i < Math.ceil(totalRows / pageSize); i++) {
  const pages = await model.getHyperCubeData('/qHyperCubeDef', [{
    qTop: i * pageSize,
    qLeft: 0,
    qWidth: 5,
    qHeight: pageSize,
  }]);
  // render incrementally
}
```

> **Warning:** Always call `destroySessionObject()` when the extension unmounts. A session object that is never
> destroyed keeps a WebSocket subscription open and uses more memory, degrading performance for
> users in the app.

### Anti-pattern 5: Opening a new app connection from within an extension

**What it looks like**

Calling `enigma.create()` or opening a new WebSocket session to the Qlik Engine from within the
extension, rather than using the model provided by `useModel()`.

**Why you must not do this**

When enigma.js opens the current app again from within the Sense client, it conflicts with the
existing client session and can break the host application. enigma.js is used internally by the
Qlik Sense client, and opening the same app a second time causes unpredictable behavior. Access
the model via `useModel()` in nebula.js instead.

```js
// ❌ BAD: opens a second session to the same app, conflicts with the host client
import enigma from 'enigma.js';
const session = enigma.create({ schema, url: `wss://<TENANT>/app/<APP_ID>` });
const app = await session.open();

// ✅ GOOD: use the model provided by the framework
import { useModel } from '@nebula.js/stardust';
const model = useModel(); // the existing session-managed model
```

## Packaging guidelines

Follow these conventions when preparing an extension ZIP for upload to Qlik Cloud.

- **Minify all code files** before packaging. Unminified source produces larger uploads and slower
  initial loads.

- **Include only runtime files.** Do not include source maps, `.qvf` or `.qvd` data files, or
  executables. These inflate package size and may fail upload validation.

- **Match filenames exactly.** For Qlik to locate and load your extension, the QEXT filename, JavaScript
  entry point, and folder name must match. A mismatch causes silent failures during import.\
  Example:
  ```text
  my-extension/
    my-extension.qext  ← QEXT file
    my-extension.js    ← Entry point (specified in QEXT)
  ```

- **Declare all external origins in the tenant CSP.** If your extension loads resources from
  external URLs such as fonts, CDN-hosted libraries, or external APIs, those origins must be added to the
  tenant's Content Security Policy allowlist before deployment. Requests to unlisted origins are
  blocked in the browser with no error shown in the Qlik UI. For more information, see
  [Manage extensions in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-extensions.htm).

## Testing and compatibility

- **Test against the current Qlik Cloud release.** Qlik Cloud is updated continuously. Extensions
  that rely on undocumented interfaces are likely to break without notice between releases.
- **Use `nebula serve` for local development.** The nebula.js development server isolates and tests
  rendering without requiring a full Qlik Sense deployment, making iteration faster.
- **Test against all deployment targets you support.** A behavior that works correctly on the
  current Qlik Cloud release may not behave the same way on Qlik Sense Client-Managed. If you
  support both, test against both.
