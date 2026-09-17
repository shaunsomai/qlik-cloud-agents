---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/hypercube/
last_updated: 2026-06-02T18:15:45+01:00
---

# HyperCube introduction

The `HyperCubeDef` is the fundamental structure which you configure before you
are provided with the result in the form of a `HyperCube`. Don't let the name
scare you, while it does contain a lot of properties and can be configured in
many ways, in its most basic form it resembles a simple table with rows and
columns.

## HyperCubeDef configuration

Not all properties are equally important, and there are a few key ones that you
need to keep in mind when configuring the `HyperCubeDef`.

### qMode

While you may not need to set `qMode` explicitly since it defaults to the
simplest mode `'S'`, it's important to know the impact it has on the data
structure.

`qMode: 'P'`, or *pivot mode*, gives you a structure suitable for presenting
pivot tables with groups in both vertical and horizontal directions, as well as
a group for all measures.

`qMode: 'T'`, or *tree mode*, gives you a structure that resembles a tree and is
suitable to use for rendering tree-like visualizations; treemap, circle packing,
sunburst, dendrogram, trellising etc.

`qMode: 'S'`, or *straight mode*, is the simplest of them all and gives you a
data structure that looks like a simple table with rows and columns. For the
sake of simplicity in explaining the rest of the hypercube it can be assumed
that this one is used.

### qDimensions and qMeasures

`qDimensions` and `qMeasures` are the columns of your "table," there is no
explicit limit on the number of these you can add, but there is often a
limitation on the number of dimensions and measure a certain chart can
handle, and you need to keep the number of these in mind when you specify
`qInitialDataFetch`.

### qInitialDataFetch

Qlik's Associative Engine is a memory based solution, meaning the amount of the
data it can handle is based entirely on the memory resources it has access to.
A such, it can contain billions of data values and the number of rows in the
hypercube can therefore reach billions as well.

To avoid cases where that huge amounts of data is transferred to the front end
the hypercube by default doesn't include any rows at all. To control this you
can set the number of rows and columns you want initially with
`qInitialDataFetch`. This property allows you to set the *data pages* you want
to extract from the entire hypercube, so you can for example choose to get the
first 50 rows:

```js
qHyperCubeDef: {
  qInitialDataFetch: [{ qLeft: 0, qTop: 0, qHeight: 50, qWidth: 4 }];
}
```

If you think of the straight table as a grid from which you want to extract
some data, then `qLeft` and `qTop` are the upper left of the subset you want to
extract, while `qHeight` and `qWidth` are the number of rows and columns.

There is however a maximum limit of 10 000 cells that you are allowed to fetch
in one go, an amount larger than that causes an error. You therefore need to
keep track of the number of columns you may need to ensure the total doesn't
exceed 10 000. If you for example know that you never need more than 4 columns,
then you can set `qHeight` to `10000/4`:

```js
qInitialDataFetch: [{ qLeft: 0, qTop: 0, qHeight: 2500, qWidth: 4 }];
```

The initial data fetch only specifies the largest possible subsection of the
entire hypercube in the layout, if there are only 7 rows in the hypercube then
you doesn't get more than 7. You can also dynamically fetch more data later on.

## Consuming the HyperCube

The output, or *layout*, of the `HyperCubeDef` is a [HyperCube](https://qlik.dev/apis/json-rpc/qix/schemas/#hypercube).
In the layout, it's located in the same place as you defined it in your
properties, but without the `Def`, for example the input:

```js
{
  properties: {
    qHyperCubeDef: {},
    another: {
      one: {
        qHyperCubeDef: {}
      }
    }
  }
}
```

results in the output:

```js
{
  layout: {
    qHyperCube: {},
    another: {
      one: {
        qHyperCube: {}
      }
    }
  }
}
```

Next to the `qDimensionInfo` and `qMeasureInfo` properties which contain your
dimensions and measures, the most important part of the hypercube are the
*data pages*.

### Data pages

The data pages are where the actual data values of the hypercube are contained,
where exactly and what structure they have depends on the `qMode` value you set
earlier. For mode `'S'` that place is `qDataPages`, which in turn contains
`qArea` and `qMatrix`.

Assuming the hypercube contains one dimension, *Movie title*, and one measure,
*Average rating*, the content might look like this:

```js
qDataPages: [
  {
    qMatrix: [
      [
        // first row
        {
          qText: "2 Fast 2 Furious",
          qNum: "NaN",
          qElemNumber: 447,
          qState: "O",
        }, // NxCell
        { qText: "6.2", qNum: 6.2, qElemNumber: 0, qState: "L" },
      ],
      [
        // second
        { qText: "2 Guns", qNum: "NaN", qElemNumber: 681, qState: "O" },
        { qText: "6.6", qNum: 6.6, qElemNumber: 0, qState: "L" },
      ],
    ],
    qArea: { qTop: 0, qLeft: 0, qWidth: 2, qHeight: 2 },
  },
];
```

Besides the textual and numerical values, each [NxCell](https://qlik.dev/apis/json-rpc/qix/schemas/#nxcell)
contains a `qElemNumber` property known as the *rank*. The rank for a dimension
cell can be seen as a property that uniquely identifies the textual value of it
in its field, across the entire data model. You can leverage this property to
provide consistent behaviour throughout your application, you can for example
set persistent color of the dimension values in a field whenever and wherever
they're used:

```js
// color scheme
const colors = ["#26A0A7", "#79D69F", "#F9EC86", "#EC983D"];

const cellColor = colors[cell.qElemNumber % colors.length];
```

This property is also something you need to keep track of when you want to make
selections in your chart.

### Getting more data

Due to the limitation of the amount of data you can get in the initial layout,
there can be situations when you need to get the rest of the data if you want to
show more of it. You can do so by using the methods exposed on the *model* of
the Generic Object. Which method to use depends, again, on the `qMode` of the
hypercube, for the `'S'` mode it's [GetHyperCubeData](https://qlik.dev/apis/json-rpc/qix/genericobject/#gethypercubedata).
When paging data in straight mode, you should begin by looking at the
`qHyperCubeDef.qSize` property which contains information on the width and
height of the full hypercube. You can from that calculate the number of pages
you need to fetch:

```js
import { useModel, useLayout, useEffect } from '@nebula.js/stardust';

const NUM_CELLS_PER_PAGE = 10000;
const MAX_PAGES = 10;
// ...
component() {
  const model = useModel();
  const layout = useLayout();

  useEffect(() => {
    const Y = layout.qHyperCube.qSize.qcy;
    const X = layout.qHyperCube.qSize.qcx;

    const HEIGHT_PER_PAGE = Math.ceil(NUM_CELLS_PER_PAGE / X);
    const NUM_PAGES = Math.floor(MAX_PAGES, Math.ceil(Y / HEIGHT_PER_PAGE));

    const pagesToFetch = [];
    for (let i = 0; i < NUM_PAGES; i++) {
      pagesToFetch.push({ qLeft: 0, qTop: i * HEIGHT_PER_PAGE, qHeight: HEIGHT_PER_PAGE, qWidth: X });
    }

    Promise.all(pagesToFetch.map((page) => model.getHyperCubeData('/qHyperCubeDef', [page]))).then((pages) => {
      console.log(pages);
    });
  }, [layout]);

}
```

You should however be **careful** when dynamically fetching data like
this, keep in mind that the size of the cube can be in the millions, fetching
a data set that large could take time and create a poor user experience.
In the preceding example the number of pages is set to a maximum of 10 so that
no more than 100 000 values are fetched in total.

You can also leverage other techniques to avoid fetching all data at once.
*Virtual scrolling* in combination with throttling of each request can boost performance.
You should also consider using a reduced dataset if you don't need the exact values:

- [getHyperCubeBinnedData](https://qlik.dev/apis/json-rpc/qix/genericobject/#gethypercubebinneddata)
  binds data points into groups and is great for heatmaps and 2D density plots.
- [getHyperCubeContinuousData](https://qlik.dev/apis/json-rpc/qix/genericobject/#gethypercubecontinuousdata)
  reduces the number of points in a continuous dimension and is great for temporal data.
- [getHyperCubeReducedData](https://qlik.dev/apis/json-rpc/qix/genericobject/#gethypercubereduceddata)
  does some wavelet magic and is great for mini charts.
