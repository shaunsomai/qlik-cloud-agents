---
source: https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula/
last_updated: 2026-09-01T13:23:42Z
---

# Migrate an existing visualization extension to nebula.js framework

This tutorial walks you through migrating a Qlik Sense visualization extension from the AngularJS-based
Extension API to nebula.js, the framework-agnostic visualization SDK.

The example extension is a simple D3.js bar chart. The tutorial uses this small example to make one point
clear: the surrounding scaffolding changes between the two frameworks, but the rendering code itself
stays the same. You move the same D3.js function from one framework to the other without rewriting it.

## What you'll learn

By the end of this tutorial, you'll have:

- Compared the complete source code of an Extension API-based bar chart with its nebula.js equivalent
- Scaffolded a nebula.js extension project using the CLI
- Ported the hypercube definition and property panel configuration to nebula.js
- Reused the existing D3.js rendering function unchanged in the migrated extension

## Prerequisites

Before you start, ensure you have access to the following:

- [Node.js](https://nodejs.org/en/download) (version 24 or newer)
- A terminal
- A modern web browser (for example, Google Chrome)
- A text editor or IDE (for example, Visual Studio Code)

## The extension you're migrating

The following extension renders one dimension and one measure as a horizontal D3.js bar chart. It's built
with the Extension API: a single JavaScript file, loaded with RequireJS, that defines the property panel
and renders the chart in a `paint()` method.

<details open>
  <summary>Extension API source: `bar-chart.js`</summary>

  ```js
  define(['jquery', 'd3'], function ($, d3) {
    function drawBarChart(element, layout) {
      const rows = layout.qHyperCube.qDataPages[0].qMatrix;
      const data = rows.map((row) => ({ label: row[0].qText, value: row[1].qNum }));

      const width = 400;
      const barHeight = 24;

      const x = d3.scaleLinear()
        .domain([0, d3.max(data, (d) => d.value)])
        .range([0, width]);

      d3.select(element).selectAll('*').remove();

      const svg = d3.select(element)
        .append('svg')
        .attr('width', width)
        .attr('height', barHeight * data.length);

      const row = svg.selectAll('g')
        .data(data)
        .enter()
        .append('g')
        .attr('transform', (d, i) => `translate(0, ${i * barHeight})`);

      row.append('rect')
        .attr('width', (d) => x(d.value))
        .attr('height', barHeight - 2)
        .attr('fill', 'steelblue');

      row.append('text')
        .attr('x', 6)
        .attr('y', barHeight / 2)
        .attr('dy', '0.35em')
        .attr('fill', 'white')
        .text((d) => d.label);
    }

    return {
      initialProperties: {
        qHyperCubeDef: {
          qDimensions: [],
          qMeasures: [],
          qInitialDataFetch: [{ qWidth: 2, qHeight: 100 }],
        },
      },
      definition: {
        type: 'items',
        component: 'accordion',
        items: {
          dimensions: { uses: 'dimensions', min: 1, max: 1 },
          measures: { uses: 'measures', min: 1, max: 1 },
          sorting: { uses: 'sorting' },
          settings: { uses: 'settings' },
        },
      },
      paint($element, layout) {
        drawBarChart($element[0], layout);
      },
    };
  });
  ```
</details>

Note the three things that a nebula.js migration needs to account for:

- `initialProperties` defines the default hypercube.
- `definition` configures the property panel.
- `paint($element, layout)` renders the chart into a jQuery-wrapped DOM element every time the layout changes.

The `drawBarChart()` function itself doesn't depend on the Extension API: it only needs a DOM element and
a `layout` object. That's the function you'll carry over to nebula.js unchanged.

## Create a project

Run the following command to create a new nebula.js extension project called `bar-chart`:

```bash
npx @nebula.js/cli create bar-chart --picasso none --pkgm npm
```

The `--picasso none` option tells the command to not create a picasso visualization template. Other
options are `minimal` and `barchart`. The `--pkgm npm` option makes the command use npm; without it, the
CLI uses yarn if it's installed locally, and falls back to npm otherwise.

The command scaffolds a project with the following files:

![Files generated after running the create command](https://qlik.dev/_astro/files.CDjdfxou.png)

## Start the development server

Run the following commands to start the development server:

```bash
cd bar-chart
npm run start
```

The command starts a local development server and opens `http://localhost:8000` in your browser.

![Connection dialog to the Qlik Associative Engine](https://qlik.dev/_astro/connect.DC6bNUzy.png)

Connect to your Qlik Cloud tenant using the WebSocket protocol, then select an app to test the
visualization against in the developer UI.

## Configure the data structure

nebula.js splits the properties and property panel definition that used to live in `initialProperties` and
`definition` across three files: `src/object-properties.js`, `src/ext.js`, and `src/data.js`.

Replace the content of `src/object-properties.js` with the following, matching the `initialProperties`
from the Extension API version:

```js
const properties = {
  qHyperCubeDef: {
    qInitialDataFetch: [{ qWidth: 2, qHeight: 100 }],
  },
};

export default properties;
```

Replace the content of `src/ext.js` with the following:

```js
export default function ext(/* galaxy */) {
  return {
    definition: {
      type: 'items',
      component: 'accordion',
      items: {
        data: { uses: 'data' },
        sorting: { uses: 'sorting' },
        settings: { uses: 'settings' },
      },
    },
    support: {
      snapshot: false,
      export: true,
      sharing: false,
      exportData: true,
      viewData: true,
    },
  };
}
```

Note the one meaningful difference from the Extension API version: nebula.js replaces the separate
`dimensions: { uses: 'dimensions' }` and `measures: { uses: 'measures' }` accordion items with a single
`data: { uses: 'data' }` item. The dimension and measure pickers it renders, and their min/max limits, are
now driven by the target you define in `src/data.js` instead.

> **Note:** `galaxy` contains environment-specific inputs. For more information, see [Load an extension into Qlik
> Sense](https://qlik.dev/extend/extensions/extension-api/build-extension/in-qlik-sense).

Add `/qHyperCubeDef` as a data target in `src/data.js`:

```js
export default {
  targets: [
    {
      path: '/qHyperCubeDef',
      dimensions: { min: 1, max: 1 },
      measures: { min: 1, max: 1 },
    },
  ],
};
```

## Reuse the rendering function unchanged

Add D3.js as a dependency:

```bash
npm install d3 --save
```

Create `src/viz.js` and paste in the exact same `drawBarChart()` function from the Extension API version,
without any changes:

```js
import * as d3 from 'd3';

export default function drawBarChart(element, layout) {
  const rows = layout.qHyperCube.qDataPages[0].qMatrix;
  const data = rows.map((row) => ({ label: row[0].qText, value: row[1].qNum }));

  const width = 400;
  const barHeight = 24;

  const x = d3.scaleLinear()
    .domain([0, d3.max(data, (d) => d.value)])
    .range([0, width]);

  d3.select(element).selectAll('*').remove();

  const svg = d3.select(element)
    .append('svg')
    .attr('width', width)
    .attr('height', barHeight * data.length);

  const row = svg.selectAll('g')
    .data(data)
    .enter()
    .append('g')
    .attr('transform', (d, i) => `translate(0, ${i * barHeight})`);

  row.append('rect')
    .attr('width', (d) => x(d.value))
    .attr('height', barHeight - 2)
    .attr('fill', 'steelblue');

  row.append('text')
    .attr('x', 6)
    .attr('y', barHeight / 2)
    .attr('dy', '0.35em')
    .attr('fill', 'white')
    .text((d) => d.label);
}
```

This confirms the point of the tutorial: the D3.js code that draws the chart didn't change. Only the
function signature moved from `paint($element, layout)` to a plain exported function that takes a DOM
element and a layout.

## Wire up the rendering logic

Replace the content of `src/index.js` with the following:

```js
import { useElement, useLayout, useEffect } from '@nebula.js/stardust';
import properties from './object-properties';
import data from './data';
import ext from './ext';
import drawBarChart from './viz';

export default function supernova(galaxy) {
  return {
    qae: {
      properties,
      data,
    },
    ext: ext(galaxy),
    component() {
      const element = useElement();
      const layout = useLayout();

      useEffect(() => {
        if (layout.qSelectionInfo.qInSelections) {
          return;
        }
        drawBarChart(element, layout);
      }, [element, layout]);
    },
  };
}
```

Compare this to the Extension API version:

- `useElement()` replaces the jQuery-wrapped `$element` parameter passed to `paint()`.
- `useLayout()` replaces the `layout` parameter passed to `paint()`.
- `useEffect()` re-runs `drawBarChart()` whenever `element` or `layout` change, replacing the automatic
  call nebula.js's runtime makes to `paint()`.

## Test the extension locally

1. Run the following command to start the development server:

```bash
npm run start
```

2. Add one dimension and one measure using the property panel on the right.

3. Verify that the chart renders as a horizontal bar chart, matching the Extension API version.

## Build and upload the extension

With the extension working locally, build and package it for deployment to your Qlik Cloud tenant.

1. Generate a bundle into the `/dist` folder:

```bash
npm run build
```

2. Generate the required Qlik Sense metadata files:

```bash
npm run sense
```

This command creates a `/bar-chart-ext` folder containing the `.qext` manifest and bundled JavaScript.

3. Zip the `/bar-chart-ext` folder and upload it to your Qlik Cloud tenant. For more information, see
   [Uploading and managing visualization extensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-extensions.htm)
   on Qlik Help.

> **Note:** To upload an extension to your Qlik Cloud tenant, you must have one of the following roles:
>
> - `Tenant Admin` role
> - `Analytics Admin` role
> - Custom role with the **Manage extensions** (`admin.extensions`) permission set to **Allowed** assigned

## Summary

You've migrated a D3.js visualization extension from the Extension API to nebula.js. The key takeaway:

- **Scaffolding differs.** Properties, property panel configuration, and rendering now live in separate
  files (`object-properties.js`, `ext.js`, `data.js`, `index.js`) instead of one Extension API file.
- **Rendering doesn't.** The `drawBarChart()` function moved into its own module without a single line
  changed. Any D3.js (or other library) rendering code you already have carries over the same way.
- **Hooks replace the `paint()` lifecycle.** `useElement()` and `useLayout()` replace the `$element` and
  `layout` parameters, and `useEffect()` replaces the automatic call to `paint()`.

## Next steps

Now that you've migrated a small extension to nebula.js, you can continue by exploring these resources:

- [Build a table visualization extension using nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension)
- [Why you should stop using Qlik's Capability API](https://community.qlik.com/t5/Qlik-Design-Blog/Why-you-should-stop-using-Qlik-s-Capability-API/ba-p/1797582)
- [Building an advanced visualization extension using nebula.js and third-party libraries such as D3.js](https://community.qlik.com/t5/Qlik-Design-Blog/Building-an-advanced-Visualization-extension-using-Qlik-s-Nebula/ba-p/1798745)
- [Dealing with variables in a mashup using nebula.js and enigma.js](https://community.qlik.com/t5/Qlik-Design-Blog/Dealing-with-variables-in-a-Mashup-using-Nebula-js-amp-Enigma-js/ba-p/1801289)
