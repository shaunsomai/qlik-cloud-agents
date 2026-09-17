---
source: https://qlik.dev/toolkits/qlik-api/examples/create-cube/
last_updated: 2026-01-19T14:21:00Z
---

# createCube function for qlik-api

One of the more popular helper functions in the Capability API
is the `createCube` method. This method allows you to create a
hypercube (table of data) using defined parameters, passing the
resulting data to the page to be used or presented outside of Qlik
visualizations. It accepted two parameters,
a hypercube definition, and a function to call every time the
layout of the hypercube changes, also known as a callback function.

## The createCube function

You can emulate and support your own `createCube` function in `qlik-api`.
Here's a prototype for `createCube` and an example in practice.

```javascript
// createCube accepts a hypercube definition and a function definition
// to be called each time the `changed` event fires on the hypercube
// object.
async function createCube(hyperCubeDef, callback) {
  // Gets the qix doc reference to the app from being added to doc prototype
  const app = this;

  // okFunc checks for existence of a supplied callback function.
  // invokes callback function or empty function.
  const okFunc = await callback
    ? async function(data) {
      await callback(data, app);
    }
    : function() { };

  // Create a session object from the supplied hypercube definition.
  const theData = await app.createSessionObject(hyperCubeDef);
  let dataLayout;

  // When the object changes, get the layout of the updated object
  // and invoke the supplied callback function.
  theData.on("changed", async () => {
    dataLayout = await theData.getLayout();
    await okFunc(dataLayout);
    return theData;
  });

  return theData;
}

// Export the function so it can be added to the doc prototype.
export { createCube };
```

## Example hypercube definition

<details>
  <summary>Hypercube definition</summary>

  ```javascript
    const cubeDef = {
      qInfo: {
          qId: 'sessionChart',
          qType: 'qHyperCubeDef'
      },
    qHyperCubeDef: {
        qDimensions: [
          {
              qLibraryId: 'FFQHMq',
          },
          {
            qLibraryId: 'KFmTudV',
          }
        ],
        qMeasures: [
          {
            qDef: { qDef: "=SUM(Sales)", qLabel: "Total Sales" },
          },
        ],
        qInitialDataFetch: [
          {
            qLeft: 0,
            qTop: 0,
            qHeight: 100,
            qWidth: 3,
          },
        ],
      },
    };
  ```

</details>

## Using createCube with qlik-api

```javascript
import { auth, qix } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js";
import { createCube } from "./createCube.js";

// Replace with your host configuration
auth.setDefaultHostConfig({...});

// Set the appId, open a session, and get the doc.
const appId = "6b410f36-cb58-4bce-8e6f-a37220bfd437";
const app = await qix.openAppSession(appId).getDoc();

// Add the createCube function to the doc reference.
// app.createCube is like adding a prototype method.
app.createCube = createCube;
const myCube = await app.createCube(cubeDef, function(cubeData) {
  // console out the first page of the hypercube.
  console.log(cubeData.qHyperCube.qDataPages[0].qMatrix);
});

// You can always get the layout of the hypercube you created
// by calling a getLayout() function on it. This is because
// createCube returns the session object created in the method.

let dataLayout = await myCube.getLayout();
```

## Using createCube with qlik-embed

```html
<script type="module">
  import { createCube } from "./createCube.js";
  const embeddedViz = document.getElementById("visualization");
  const refApi = embeddedViz.getRefApi;
  const app = refApi.getDoc();

  app.createCube = createCube;

  const myCube = await app.createCube(cubeDef, function(cubeData) {
    // console out the first page of the hypercube.
    console.log(cubeData.qHyperCube.qDataPages[0].qMatrix);
  });

  // You can always get the layout of the hypercube you created
  // by calling a getLayout() function on it. This is because
  // createCube returns the session object created in the method.

  let dataLayout = await myCube.getLayout();
</script>
```

## Next steps

One of the main use cases for using the `createCube` function
is to create a table using plain `html` and have it update
automatically.

Here's some example code using the `createCube` function to
create and update an `html` table dynamically.

```javascript
import { auth, qix } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js";
import { createCube } from "./createCube.js";
    
// Set up your host configuration.
auth.setDefaultHostConfig({
  ...
});

// Supply the app Id with the data you want to connect to.
const appId = "<app-id>";
const app = await qix.openAppSession(appId).getDoc();

// Add your hypercube definition.
const cubeDef = { //Add your hypercube definition here };

// Add createCube to the app reference.
app.createCube = createCube;

// Create the hypercube session object by supplying the hypercube
// definition and the callback function. The callback function
// will update the hypercube layout on change events and call
// the paintChart function to refresh the html table.
const myCube = await app.createCube(cubeDef, function(cubeData) {
  paintChart(cubeData.qHyperCube.qDataPages[0].qMatrix, table, tBody);
});

// In this example, calling a getLayout request one time
// to get the columns and build the base table structure.
// You have flexibility to make this better so go for it!
let dataLayout = await myCube.getLayout();

// The html used in the example has a <div/> element
// named chart-data. The table will be appended to this
// element.
let container = document.getElementById("chart-data");
let table = document.createElement("table");

// This section builds out the table headers by getting
// the columns from the dataLayout variable. Depending
// on your hypercube, you will need to adjust the code.
let cols = [dataLayout.qHyperCube.qDimensionInfo[0].title,
  dataLayout.qHyperCube.qDimensionInfo[1].title,
  dataLayout.qHyperCube.qMeasureInfo[0].title];
let thead = document.createElement("thead");
let tr = document.createElement("tr");
cols.forEach((item) => {
  let th = document.createElement("th");
  th.textContent = item;
  tr.appendChild(th);
});
thead.appendChild(tr);
table.appendChild(thead);
let tBody = document.createElement("tbody");
table.appendChild(tBody);
container.appendChild(table);

// After the table is set up, call the paintChart function
// to populate the data the first time the page renders.
paintChart(dataLayout.qHyperCube.qDataPages[0].qMatrix, table, tBody);

// The paintChart function loops through the hypercube data
// and updates the rows of the table body to reflect the current
// hypercube layout.

function paintChart(theCube, table, tBody) {
  let newTBody = document.createElement("tbody");
  theCube.forEach((item) => {
    let tr = document.createElement("tr");
    let vals = Object.values(item);
    vals.forEach((elem) => {
      let td = document.createElement("td");
      td.textContent = elem.qText;
      tr.appendChild(td);
    });
    newTBody.appendChild(tr);
  });
  if (tBody != null) {
    table.replaceChild(newTBody, table.tBodies[0]);
  } else {
    table.appendChild(newTBody);
  }
}
```
