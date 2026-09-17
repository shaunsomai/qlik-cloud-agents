---
source: https://qlik.dev/toolkits/enigma-js/
last_updated: 2026-03-18T16:49:43Z
---

# enigma.js overview

enigma.js is a library that helps you communicate with the Qlik Associative Engine
in JavaScript environments.

Examples of use may be building your own browser-based analytics tools,
back-end services, or command-line scripts.

## Installation

```bash
npm install enigma.js
```

## Get started

The following commands should get you started in a Node.js environment.

> **Note:** You need an [API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key/)
> from your Qlik Cloud tenant to connect successfully.

```bash
npm install enigma.js ws
```

And then save the following snippet to a JavaScript file `connect.js`,
update with your information and execute it with Node.js.

```js
(async () => {
  const enigma = require("enigma.js");
  const schema = require("enigma.js/schemas/12.612.0");
  const WebSocket = require("ws");

  // replace with your information
  const appId = "<app-id>";
  const tenant = "<your-tenant.qlikcloud.com>";
  const apiKey = "<your-api-key>";

  const url = `wss://${tenant}/app/${appId}`;

  const session = enigma.create({
    schema,
    createSocket: () =>
      new WebSocket(url, {
        headers: { Authorization: `Bearer ${apiKey}` },
      }),
  });

  // bind traffic events to log what is sent and received on the socket:
  session.on("traffic:sent", (data) => console.log("sent:", data));
  session.on("traffic:received", (data) => console.log("received:", data));

  // open the socket and eventually receive the QIX global API, and then close
  // the session:
  try {
    const global = await session.open();
    console.log("You are connected!");
    await session.close();
    console.log("Session closed!");
  } catch (err) {
    console.log("Something went wrong :(", err);
  }
})();
```

```bash
node connect.js
```

## Node.js versus browser

enigma.js as a library can be used both in a Node.js environment, as well as in
a browser. This enables you to build projects that are portable, with similar behavior
on top of enigma.js. But this compatibility also introduces a few
differences in configuration that's explained more in detail under the [Configuration section](https://qlik.dev/apis/javascript/enigma-js/#definitions-configuration).

## Promises

Asynchronicity in the JavaScript world is commonly solved by using either
promises or callbacks.

enigma.js makes heavy use of promises because this technology gives you several
advantages compared to traditional callbacks:

- cleaner code for the end-user,
- error handling is easier to defer,
- compatible with emerging standards (async/await).

All generated API methods return a promise.

Read more:

- [Promises deep-dive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [`async`/`await` syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

## Authentication

enigma.js doesn't handle authentication due to the simple reason that different
products and deployments handle it differently. There are, however, a couple of
examples for the more common use cases which you can find on the link below.

Read more:

- [Authentication examples](https://github.com/qlik-oss/enigma.js/tree/master/examples/authentication)
- [Authentication options](https://qlik.dev/authenticate)

## Schemas, the QIX interface

enigma.js uses schemas to generate a programmatic interface against Qlik
Associative Engine. Outlined below describes what a schema consists of, and what
their purposes are.

An important note is that enigma.js normalizes the QIX method names into camelCasing,
while Qlik Associative Engine uses PascalCasing. `GetObject` in Qlik Associative
Engine would be `getObject` in enigma.js.

enigma.js allows you to invoke QIX methods by either using what's called 'position',
which is an array of parameters, or by name, using an object with key/value pairs.

Example of using the different parameters:

```js
doc.getObject("object-id");
doc.getObject({ qId: "object-id" });
```

Read more:

- [Request object](http://help.qlik.com/en-US/sense-developer/Subsystems/EngineAPI/Content/introducing-engine-API.htm)
  on Qlik Help
- [Parameter passing example](https://github.com/qlik-oss/enigma.js/tree/master/examples/basics/parameters#basics-parameter-passing)
  in the enigma.js repository

### QIX classes, or structs

QIX classes are [generic object](#generic-object-model) interfaces
describing the available QIX methods you may interact with for that type. Depending
on the schema version used, there may be a number of different classes available
(if you are curious, look at the specific schema file you are using for the available
classes and methods). In most cases, you create, retrieve, and remove these from the `Doc`
interface.

Read more:

- [Doc class](https://qlik.dev/apis/json-rpc/qix/doc#%23%2Fentries%2FDoc)
- [Field class](https://qlik.dev/apis/json-rpc/qix/field#%23%2Fentries%2FField)
- [GenericBookmark class](https://qlik.dev/apis/json-rpc/qix/genericbookmark#%23%2Fentries%2FGenericBookmark)
- [GenericObject class](https://qlik.dev/apis/json-rpc/qix/genericobject#%23%2Fentries%2FGenericObject)
- [GenericDimension class](https://qlik.dev/apis/json-rpc/qix/genericdimension#%23%2Fentries%2FGenericDimension)
- [GenericMeasure class](https://qlik.dev/apis/json-rpc/qix/genericmeasure#%23%2Fentries%2FGenericMeasure)
- [Global class](https://qlik.dev/apis/json-rpc/qix/global#%23%2Fentries%2FGlobal)

### QIX enums

The Qlik Associative Engine error codes have constants in the schema that you
can use to make your error handling code easier to read.

Read more:

- [Example of enums in 12.20.0](https://github.com/qlik-oss/enigma.js/blob/f45eb27de2f5d9af1ea99d6e1487cd62dda8fd73/schemas/12.20.0.json#L1188)

## Generic object model

This section gives you a brief overview on how the generic object model works. See
the links at the end of this section for more in-depth information.

The Qlik Associative Engine uses what' s called the generic object model within
an app (also sometimes called a document).

These generic objects all have unique identifiers, and can be interacted with
using the QIX interface schema methods.

Consider this:

An app, `your-app.qvf`, contains generic object properties, data, and load
scripts. To interact with that content, the standard approach is to use
the generic object model. For example, say you want to interact with a generic object
with id `my-object`:

```js
doc.getObject("my-object").then((api) => {
  // api is now an object with QIX interface methods for the GenericObject struct
});
```

When `getObject` is invoked, enigma.js sends a request to fetch a [*handle*](https://en.wikipedia.org/wiki/Handle_\(computing\))
for that object. Until that session is closed, Qlik Associative Engine notifies you
of changes on that handle every time it gets invalidated (either by changes related
to the data model referenced in it, or property changes).

Note that these changes are only triggered when the Qlik Associative Engine
changes the state from valid to invalid on that handle:

```js
// bind 'changed' event to get notified when the state is invalid':
api.on("changed", () => console.log("The generic object changed"));
// `getLayout` will set the generic object state to 'valid' in Qlik Associative Engine,
// evaluating any hypercubes, expressions, etc. inside it:
api.getLayout().then(() => {
  // 'getProperties' will give you the underlying properties describing
  // the generic object layout, including the hypercube/expression sources etc.:
  api.getProperties().then((props) => {
    // modify some properties to you liking:
    props.someValue = true;
    // 'setProperties' will modify the generic object state from 'valid' to
    // 'invalid' in Qlik Associative Engine, causing a 'changed' event in enigma.js:
    api.setProperties(props).then(() => {
      // the 'changed' event handler above should now have been invoked
    });
  });
});
```

Read more:

- [Generic objects](http://help.qlik.com/en-US/sense-developer/Subsystems/EngineAPI/Content/GenericObject/overview-generic-object.htm)
  on Qlik Help

## JSON-RPC protocol

The Qlik Associative Engine uses JSON-RPC over WebSockets for communication.
In short, it means that enigma.js gives you an API that's translated into a
JSON-RPC request object, and handles the JSON-RPC response sent back from the
engine, eventually sending it back to you in a predictable format. See the links
below for more details about the protocol.

Read more:

- [Qlik Engine API](http://help.qlik.com/en-US/sense-developer/Subsystems/EngineAPI/Content/introducing-engine-API.htm)
  on Qlik Help
- [JSON-RPC specification](http://www.jsonrpc.org/specification)
