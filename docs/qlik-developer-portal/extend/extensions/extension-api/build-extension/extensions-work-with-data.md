---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/extensions-work-with-data/
last_updated: 2026-06-02T18:15:45+01:00
---

# Work with data

This topic describes how to bring data into your visualization extension.

## Creating the Hello-Data visualization extension

In this section, you will create the container, the QEXT file, and the main script
file.

### Create the container

Create a folder that will contain your assets and name it `Hello-Data`.

### Create the QEXT file

The next step is to create a QEXT file in the folder that you just created and
name it `Hello-Data.qext`.

It should contain the following information:

Example: Hello-Data.qext

```json
{
    "name" : "Hello Data",
    "description" : "Example on how to use data in visualization extensions",
    "icon" : "extension",
    "type" : "visualization",
    "version": "0.1.0",
    "preview" : "hellodata.png",
    "author": "Qlik"
}
```

### Create the main script file

Next, create the main script file named `Hello-Data.js`. Place this file in the
same folder as the QEXT file. Paste the following code into the script file and
save it.

Example: Hello-Data.js

```js
define( [],
  ( ) => {
    'use strict';
     return {
       definition: {},
       initialProperties: {},
       paint: function ( $element, layout ) {
         // Your code comes here

       }
     };
  } );
```

### Additional assets

The QEXT file defines that a image named `hellodata.png` is to be used as a
preview image. This file is included in the downloadable version of this example.

## Defining the properties panel

Reusing the built-in capability of defining dimensions and measures has already
been described.

[Reusing existing properties](https://qlik.dev/extend/extensions/extension-api/build-extension/property-panel-basics/extensions-reusing-properties)

Add the following code to the definition object of your visualization extension.

```js
definition: {
  type: "items",
  component: "accordion",
  items: {
    dimensions: {
      uses: "dimensions"
    },
    measures: {
      uses: "measures"
    },
    sorting: {
      uses: "sorting"
    },
    appearance: {
      uses: "settings"
    }
  }
},
```

The preceding code results in the following properties panel:

![Properties panel with custom fields](https://qlik.dev/_astro/ui-extension-hello-data-01.egv5GoBC.png)

When you add the visualization extension to a sheet, you are able to define the
dimensions and measures directly on the object without using the properties
panel. You can also drag and drop master dimensions, master measures, and fields
onto the visualization extension.

![Example of an extension in sheet view](https://qlik.dev/_astro/ui-extension-hello-data-02.4T_SYvyh.png)

## Testing the visualization extension with data

If you want to test your visualization extension, you can do so in an existing
Qlik Sense app or you can create a new app. If you create a new app, you also
need some data to create a sheet to put the visualization extension
onto. In this section, you will create a new app and load data from the test
script that comes with Qlik Sense.

### Generating the test script

Do the following:

1. Launch Qlik Cloud and create a new app. In this example, you will name
   the app `Hello-Data`.

2. Open the app and select to load data using the Data load editor.

3. In the Data load editor, place the cursor at the bottom of the script area
   and press Ctrl+00.

   The test script code is inserted into the script and it contains a few inline
   data fields.

4. Press the `Load data` button.

   The data is loaded into the app, which is automatically saved when loading is
   completed.

### Testing with even more data

If you want to test with more data, you can use a modified sample script:

```text
// Change the amount here to create more records
SET vAmountTransactions=10000;

Characters:
Load Chr(RecNo()+Ord('A')-1) as Alpha, RecNo() as Num autogenerate 26;

ASCII:
Load
 if(RecNo()>=65 and RecNo()<=90,RecNo()-64) as Num,
 Chr(RecNo()) as AsciiAlpha,
 RecNo() as AsciiNum
autogenerate 255
 Where (RecNo()>=32 and RecNo()<=126) or RecNo()>=160 ;

Transactions:
Load
 TransLineID,
 TransID,
 mod(TransID,26)+1 as Num,
 Pick(Ceil(3*Rand1),'A','B','C') as Dim1,
 Pick(Ceil(6*Rand1),'a','b','c','d','e','f') as Dim2,
 Pick(Ceil(3*Rand()),'X','Y','Z') as Dim3,
 Round($(#vAmountTransactions)*Rand()*Rand()*Rand1) as Expression1,
 Round(  10*Rand()*Rand()*Rand1) as Expression2,
 Round(Rand()*Rand1,0.00001) as Expression3;
Load
 Rand() as Rand1,
 IterNo() as TransLineID,
 RecNo() as TransID
Autogenerate $(#vAmountTransactions)
 While Rand()<=0.5 or IterNo()=1;
```

## Visualizing the data returned from the Qlik engine

Now it is time to start working with the data returned from the Qlik engine. It
is a good idea to visualize the data in a native Table, side by side with your
new visualization extension.

Do the following:

1. Create a new sheet.

2. Add your visualization extension (Hello-Data) to the sheet.

3. Add a Table to the sheet.

4. Add the same dimensions and measures to both your visualization extension and
   the table.

   Based on the test data you previously loaded, select the following data:

   Dimensions:

   - TransId
   - Dim1
   - Dim2

   Measures:

   - Sum(Expression1)
   - Sum(Expression2)

This results in a native Table looking something like this:

![Example of a table comparing dimensions and
measures](https://qlik.dev/_astro/ui-extension-hello-data-04.7af4__3z.png)

## Retrieving the data in your visualization extension

When dimensions and measures have been added to a visualization extension, a
hypercube is returned from the Qlik engine.

In this section,  you will use Chrome DevTools to output the hypercube to
DevTool's console. To do so, change the paint section in the main script file
as follows:

```js
paint: ( $element, layout )=> {
  console.log('Data returned: ', layout.qHyperCube);
}
```

The console output:

![Web dev tool console output, displaying
extension fields and information](https://qlik.dev/_astro/ui-extension-hello-data-05.Dpxedrfo.png)

You can see the structure of the hypercube in the console output. Expand the
following nodes to review:

- `qDimensionInfo`: dimensions used
- `qMeasureInfo`: measures used
- `qDataPages`: the result

## Creating an HTML table

After reviewing the underlying data structure, you can create a simple HTML
table to display the data. The HTML table should contain a header that includes
the labels for the dimensions and measures, and a body that contains the data.

### Skeleton

```js
paint: ( $element, layout ) => {
  const hc = layout.qHyperCube;
  console.log( 'Data returned: ', hc );

  $element.empty();
  const table = '<table border="1">';

table += '<thead>';
table += '<tr>';
for (var i = 0; i < hc.qDimensionInfo.length; i++) {
  table += '<th>' + hc.qDimensionInfo[i].qFallbackTitle + '</th>';
}
for (var i = 0; i < hc.qMeasureInfo.length; i++) {
  table += '<th>' + hc.qMeasureInfo[i].qFallbackTitle + '</th>';
}
table += '</tr>';
table += '</thead>';

  table += '<tbody>';
  table += '</tbody>';
  table += '</table>';
  $element.append( table );
}
```

### Table header

The table header should contain the labels for the dimensions and measures used
in the visualization extension. Start by adding the dimension labels. Iterate
through all existing dimensions using the `hc.DimensionInfo` array and then use
the `qFallbackTitle` property which holds the label of the dimension.

```js
table += '<thead>';
table += '<tr>';
for (var i = 0; i < hc.qDimensionInfo.length; i++) {
  table += '<th>' + hc.qDimensionInfo[i].qFallbackTitle + '</th>';
}
table += '</tr>';
table += '</thead>';
```

This results in the following:

![Example of an extension with table
Dimensions in header](https://qlik.dev/_astro/ui-extension-hello-data-06.BB9WLSGD.png)

Then you do the same for the measures:

```js
table += '<thead>';
table += '<tr>';
for (var i = 0; i < hc.qDimensionInfo.length; i++) {
  table += '<th>' + hc.qDimensionInfo[i].qFallbackTitle + '</th>';
}
for (var i = 0; i < hc.qMeasureInfo.length; i++) {
  table += '<th>' + hc.qMeasureInfo[i].qFallbackTitle + '</th>';
}
table += '</tr>';
table += '</thead>';
```

This results in the following:

![Example of an extension with table
Dimensions and Measures in header](https://qlik.dev/_astro/ui-extension-hello-data-07.CpNwLzpq.png)

### Changing the initial properties

By default, the Qlik associative engine returns no data. You change the
`qInitialDataFetch` property to overrule the default properties and fetch
10 columns and 100 rows instead. To make the change take effect, remove
your visualization extension from the sheet and then add it again.

Example: Updated initialProperties in Hello-Data.js

```js
initialProperties: {
  qHyperCubeDef: {
    qDimensions: [],
    qMeasures: [],
    qInitialDataFetch: [
      {
        qWidth: 10,
        qHeight: 100
      }
    ]
  }
},
```

After having updated the `initialProperties`, each row now has 5 cells.

![Console output displaying an array (column)
containing multiple objects (rows), each containing length:5](https://qlik.dev/_astro/ui-extension-hello-data-10.TWhpOU8r.png)

### Table data

If you look at the console output and expand the `qDataPages` node, you will see
that:

- `qDataPages` is an array
- The data is held with `qDataPages[0].qMatrix`
- `qDataPages[0].qMatrix` is an array of objects (the rows)
- The rows are holding an array of other objects (the cells)

![Example of console output displaying how
rows are stored as arrays, and cells are stored as objects](https://qlik.dev/_astro/ui-extension-hello-data-08.BB0JjsZP.png)

## Rendering table data

To render the rows and columns, you need to iterate over rows and then cells,
similar to the way you did when adding the headers.

```js
table += '<tbody>';

// iterate over all rows
for (var r = 0; r < hc.qDataPages[0].qMatrix.length; r++) {
  table += '<tr>';

  // iterate over all cells within a row
  for (var c = 0; c < hc.qDataPages[0].qMatrix[r].length; c++) {
    table += '<td>';
    table += hc.qDataPages[0].qMatrix[r][c].qText;
    table += '</td>';
  }
  table += '</tr>';
}
table += '</tbody>';
```

Result:

![Rendered table extension, displaying a
completed table with dimensions and measures from previous examples](https://qlik.dev/_astro/ui-extension-hello-data-11.IawuQrmE.png)

You have now finished the task of bringing data into your visualization
extension. Since the main objective of this example was to bring data into your
visualization extension, you may notice that there are a few issues with the
current implementation:

- The table is not scrollable.
- Only 100 rows are rendered (qHeight: 100) but the native table returns many
  more records.
- The current implementation does not support selections.
- The table is not styled.

## Best practices

When you work with data, the following best practices may be helpful:

- Prove the data returned from the Qlik engine by creating a native
  table using the same dimensions and measures.

- Use `console.log`wisely to understand the underlying data structure.

- Always add `initialProperties` to define how many rows and columns that are
  available in your JavaScript object.

- After changing `initialProperties`, remove your visualization extension from
  the sheet and then add it again.

## Source code

[Download the source code file (ZIP)](https://help.qlik.com/en-US/sense-developer/Subsystems/Extensions/Content/Sense_Extensions/Tutorials/03-Hello-Data.zip)
from Qlik Help.
