---
source: https://qlik.dev/apis/javascript/enigma-js/
last_updated: 2026-01-19T15:48:02Z
---

# enigma.js

`Version: 2.7.3` | _stable_

JavaScript library for consuming Qlik backend services, commonly used with nebula.js. Consider using the qlik-embed toolkit for an easier embedding experience, whilst building on the same core technologies.

## Table of Contents

### Entries

- [Enigma.create](#enigmacreateconfig-function)
- [errorCodes](#errorcodes-object)
- [SenseUtilities.buildUrl](#senseutilitiesbuildurlurlconfig-function)

### Definitions

- [API](#api-interface)
- [Configuration](#configuration-interface)
- [EnigmaError](#enigmaerror-class)
- [Interceptor](#interceptor-interface)
- [InterceptorRequest](#interceptorrequest-class)
- [InterceptorResponse](#interceptorresponse-class)
- [Mixin](#mixin-interface)
- [SenseConfiguration](#senseconfiguration-object)
- [Session](#session-class)

## Entries

### Enigma.create(config) `function`

Function used to create a QIX session.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | [Configuration](#configuration-interface) | Yes | - | The configuration object for the QIX session. |

#### Returns

[Session](#session-class) - Returns a new QIX session.

<details>
<summary>Examples</summary>

_Example minimal session creation_

```javascript
const enigma = require('enigma.js');
const schema = require('enigma.js/schemas/12.20.0.json');
const WebSocket = require('ws');
const config = {
  schema,
  url: 'ws://localhost:9076/app/engineData',
  createSocket: url => new WebSocket(url),
};
const session = enigma.create(config);
```

</details>

---

### errorCodes `object`

This is a list of error codes that can be thrown from enigma.js API calls.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `NOT_CONNECTED` | number | Yes | -1 | You're trying to send data on a socket that's not connected. |
| `OBJECT_NOT_FOUND` | number | Yes | -2 | The object you're trying to fetch does not exist. |
| `EXPECTED_ARRAY_OF_PATCHES` | number | Yes | -3 | Unexpected RPC response, expected array of patches. |
| `PATCH_HAS_NO_PARENT` | number | Yes | -4 | Not an object that can be patched. |
| `ENTRY_ALREADY_DEFINED` | number | Yes | -5 | This entry is already defined with another key. |
| `NO_CONFIG_SUPPLIED` | number | Yes | -6 | You need to supply a configuration. |
| `PROMISE_REQUIRED` | number | Yes | -7 | There's no promise object available (polyfill required?). |
| `SCHEMA_STRUCT_TYPE_NOT_FOUND` | number | Yes | -8 | The schema struct type you requested does not exist. |
| `SCHEMA_MIXIN_CANT_OVERRIDE_FUNCTION` | number | Yes | -9 | Can't override this function. |
| `SCHEMA_MIXIN_EXTEND_NOT_ALLOWED` | number | Yes | -10 | Extend is not allowed for this mixin. |
| `SESSION_SUSPENDED` | number | Yes | -11 | Session suspended - no interaction allowed. |
| `SESSION_NOT_ATTACHED` | number | Yes | -12 | onlyIfAttached supplied, but you got SESSION_CREATED. |

<details>
<summary>Examples</summary>

_Handling an enigma.js error_

```javascript
const { NOT_CONNECTED } = require('enigma.js/error-codes');
try {
  const layout = await model.getLayout();
} catch (err) {
  if (err.code === NOT_CONNECTED) {
    console.log('Tried to communicate on a session that is closed');
  }
}
```

</details>

---

### SenseUtilities.buildUrl(urlConfig) `function`

Function used to build a URL.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `urlConfig` | [SenseConfiguration](#senseconfiguration-object) | Yes | - | The URL configuration object. |

#### Returns

`string` - Returns the websocket URL.

<details>
<summary>Examples</summary>

_Example of building and using a Qlik Sense-compatible WebSocket URL_

```javascript
const enigma = require('enigma.js');
const schema = require('enigma.js/schemas/12.20.0.json');
const SenseUtilities = require('enigma.js/sense-utilities');
const url = SenseUtilities.buildUrl({ host: 'my-sense-host', appId: 'some-app' });
const session = enigma.create({ schema, url });
```

</details>

---

## Definitions

### API `interface`

The API for generated APIs depends on the QIX Engine schema you pass into your Configuration, and
on what QIX struct the API has.

All API calls made using the generated APIs will return promises that are either resolved or
rejected depending on how the QIX Engine responds.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Contains the unique identifier for this API. |
| `type` | string | Yes | - | Contains the schema class name for this API. |
| `genericType` | string | Yes | - | Corresponds to the qInfo.qType property on the generic object's properties object. |
| `session` | [Session](#session-class) | Yes | - | Contains a reference to the session that this API belongs to. |
| `handle` | number | Yes | - | Contains the handle QIX Engine assigned to the API. Used interally in enigma.js for caches and JSON-RPC requests. |

<details>
<summary>Examples</summary>

_Example using `global` and `generic object` struct APIs_

```javascript
global.openDoc('my-document.qvf').then((doc) => {
  doc.createObject({ qInfo: { qType: 'my-object' } }).then(api => { });
  doc.getObject('object-id').then(api => { });
  doc.getBookmark('bookmark-id').then(api => { });
});
```

</details>

---

#### changed() `event`

Handles changes on the API. The changed event is triggered whenever enigma.js or QIX Engine has
identified potential changes on the underlying properties or hypercubes and you should re-fetch
your data.

<details>
<summary>Examples</summary>

_Bind the `changed` event_

```javascript
api.on('changed', () => {
  api.getLayout().then(layout => { });
});
```

</details>

---

#### closed() `event`

Handles closed API. The closed event is triggered whenever QIX Engine considers an API closed.
It usually means that it no longer exists in the QIX Engine document or session.

<details>
<summary>Examples</summary>

_Bind the `closed` event_

```javascript
api.on('closed', () => {
  console.log(api.id, 'was closed');
});
```

</details>

---

#### traffic() `event`

Handles JSON-RPC requests/responses for this API. Generally used in debugging purposes.
`traffic:*` will handle all websocket messages, `traffic:sent` will handle outgoing messages
and `traffic:received` will handle incoming messages.

<details>
<summary>Examples</summary>

_Bind the traffic events_

```javascript
// bind both in- and outbound traffic to console.log:
api.on('traffic:*', console.log);
// bind outbound traffic to console.log:
api.on('traffic:sent', console.log);
// bind inbound traffic to console.log:
api.on('traffic:received', console.log);
```

</details>

---

### Configuration `interface`

The enigma.js configuration object.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema` | Object | Yes | - | Object containing the specification for the API to generate. Corresponds to a specific version of the QIX Engine API. |
| `url` | string | Yes | - | String containing a proper websocket URL to QIX Engine. |
| `createSocket` | function | No | - | A function to use when instantiating the WebSocket, mandatory for Node.js. |
| `Promise` | Object | No | - | ES6-compatible Promise library. |
| `suspendOnClose` | boolean | No | false | Set to true if the session should be suspended instead of closed when the websocket is closed. |
| `mixins` | [Mixin](#mixin-interface)[] | No | "[]" | Mixins to extend/augment the QIX Engine API. Mixins are applied in the array order. |
| `requestInterceptors` | Array | No | "[]" | Interceptors for augmenting requests before they are sent to QIX Engine. Interceptors are applied in the array order. |
| `responseInterceptors` | Array | No | "[]" | Interceptors for augmenting responses before they are passed into mixins and end-users. Interceptors are applied in the array order. |
| `protocol` | object | No | "{}" | An object containing additional JSON-RPC request parameters. |

<details>
<summary>Properties of `protocol`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `delta` | boolean | No | true | Set to false to disable the use of the bandwidth-reducing delta protocol. |

</details>

<details>
<summary>Examples</summary>

_Example defining a configuration object_

```javascript
const enigma = require('enigma.js');
const WebSocket = require('ws');
const bluebird = require('bluebird');
const schema = require('enigma.js/schemas/12.20.0.json');

const config = {
 schema,
 url: 'ws://localhost:4848/app/engineData',
 createSocket: url => new WebSocket(url),
 Promise: bluebird,
 suspendOnClose: true,
 mixins: [{ types: ['Global'], init: () => console.log('Mixin ran') }],
 protocol: { delta: false },
};

enigma.create(config).open().then((global) => {
  // global === QIX global interface
  process.exit(0);
});
```

</details>

---

### EnigmaError() `class`

extends `Error`

Error containing a custom error code.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `code` | number | Yes | - | The error code as defined by `errorCodes`. |
| `enigmaError` | boolean | Yes | true |  |

---

### Interceptor `interface`

Interceptor is a concept similar to mixins, but runs on a lower level. The interceptor concept
can augment either the requests (i.e. before sent to QIX Engine), or the responses (i.e. after
QIX Engine has sent a response). The interceptor promises run in parallel to the regular
promises used in enigma.js, which means that it can be really useful when you want to normalize
behaviors in your application.

---

### InterceptorRequest() `class`

implements [Interceptor](#interceptor-interface)

<details>
<summary>Examples</summary>

_Implement a request interceptor_

```javascript
const enigma = require('enigma.js');
const WebSocket = require('ws');
const schema = require('enigma.js/schemas/12.20.0.json');

const session = enigma.create({
  schema,
  url: 'ws://localhost:9076/app/engineData',
  createSocket: (url) => new WebSocket(url),
  requestInterceptors: [{
    onFulfilled: function logRequest(sessionReference, request) {
      console.log('Request being sent', request);
      return request;
    }
  },
});
```

</details>

---

#### onFulfilled(session, request) `function`

This method is invoked when a request is about to be sent to QIX Engine.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `session` | [Session](#session-class) | Yes | - | The session executing the interceptor. |
| `request` | Object | Yes | - | The JSON-RPC request that will be sent. |

---

### InterceptorResponse() `class`

implements [Interceptor](#interceptor-interface)

<details>
<summary>Examples</summary>

_Implement a request interceptor_

```javascript
const enigma = require('enigma.js');
const WebSocket = require('ws');
const schema = require('enigma.js/schemas/12.20.0.json');

const session = enigma.create({
  schema,
  url: 'ws://localhost:9076/app/engineData',
  createSocket: (url) => new WebSocket(url),
  responseInterceptors: [{
    onRejected: function logError(sessionReference, request, error) {
      console.log('Error returned from QIX engine', error, 'Originating request:', request);
      // throw error so it's continued to be rejected:
      throw error;
    }
  },
});
```

</details>

---

#### onFulfilled(session, request, result) `function`

This method is invoked when a promise has been successfully resolved;
use this to modify the result or reject the promise chain before it is sent
to mixins.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `session` | [Session](#session-class) | Yes | - | The session executing the interceptor. |
| `request` | Object | Yes | - | The JSON-RPC request resulting in this response. |
| `result` | Object | Yes | - | Whatever the previous interceptor is resolved with. |

---

#### onRejected(session, request, error) `function`

This method is invoked when a previous interceptor has rejected the
promise; use this to handle, for example, errors before they are sent into mixins.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `session` | [Session](#session-class) | Yes | - | The session executing the interceptor. You may use .retry() to retry sending it to QIX Engine. |
| `request` | Object | Yes | - | The JSON-RPC request resulting in this error. |
| `error` | Object | Yes | - | Whatever the previous interceptor is rejected with. |

---

### Mixin `interface`

The mixin concept allows you to add or override QIX Engine API functionality. A mixin is
basically a JavaScript object describing which types it modifies, and a list of functions
for extending and overriding the API for those types.

QIX Engine types like, for example, GenericObject, Doc, GenericBookmark, are supported but
also custom GenericObject types such as barchart, story and myCustomType. An API will get
both their generic type as well as custom type mixins applied.

Mixins that are bound to several different types can find the current API type in the
`genericType` or `type` members. `this.type` would, for instance, return `GenericObject` and
`this.genericType` would return `barchart`.

See the Mixins examples on how to use it. Below is an outline of what the mixin API consists of.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `types` | string \| string[] | Yes | - | String or array of strings containing the API-types that will be mixed in. |
| `extend` | Object | No | - | Object literal containing the methods that will be extended on the specified API. |
| `override` | Object | No | - | Object literal containing the methods to override existing methods. |
| `init` | function | No | - | Init function that, if defined, will run when an API is instantiated. It runs with Promise and API object as parameters. |

---

### SenseConfiguration `object`

This object describes the configuration that is sent into `buildUrl(config)`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appId` | string | No | - | The app ID. If omitted, only the global object is returned.                            Otherwise both global and app object are returned. |
| `noData` | boolean | No | false | Whether to open the app without data. |
| `secure` | boolean | No | true | Set to false if an unsecure WebSocket should be used. |
| `host` | string | No | - | Host address. |
| `port` | number | No | - | Port to connect to. |
| `prefix` | string | No | "/" | The absolute base path to use when connecting.                             Used for proxy prefixes. |
| `subpath` | string | No | "" | The subpath. |
| `route` | string | No | "" | Used to instruct Proxy to route to the correct receiver. |
| `identity` | string | No | "" | Identity to use. |
| `urlParams` | Object | No | "{}" | Used to add parameters to the WebSocket URL. |
| `ttl` | number | No | - | A value in seconds that QIX Engine should keep the session                             alive after socket disconnect (only works if QIX Engine supports it). |

---

### Session() `class`

The QIX Engine session object.

---

#### close(code?, reason?) `function`

emits [closed](#closed-event)

Closes the websocket and cleans up internal caches. Also triggers the closed event
on all generated APIs. Note that you have to manually invoke this when you want to
close a session and config.suspendOnClose is true.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `code` | number | No | 1000 | The reason code for closing the connection. |
| `reason` | string | No | "" | The human readable string describing why the connection is closed. |

##### Returns

`Promise<Object>` - Eventually resolved when the websocket has been closed.

<details>
<summary>Examples</summary>

_Closing a session_

```javascript
session.close().then(() => {
  console.log('Session was closed');
});
```

</details>

---

#### open() `function`

emits [opened](#opened-event)

Establishes the websocket against the configured URL and returns the Global instance.

##### Returns

`Promise<Object>` - Eventually resolved if the connection was successful.

<details>
<summary>Examples</summary>

_Opening a sesssion_

```javascript
session.open().then(() => {
  console.log('Session was opened');
});
```

</details>

---

#### resume(onlyIfAttached) `function`

emits [resumed](#resumed-event)

Resumes a previously suspended enigma.js session by recreating the websocket and,
if possible, reopen the document as well as refreshing the internal cashes. If successful,
changed events will be triggered on all generated APIs, and on the ones it was unable to
restore, the closed event will be triggered.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `onlyIfAttached` | boolean | Yes | - | If true, resume only if the session was reattached properly. |

##### Returns

`Promise<Object>` - Eventually resolved when the websocket (and potentially the
previously opened document, and generated APIs) has been restored; it is rejected when it fails
any of those steps, or when onlyIfAttached is true and a new session was created.

<details>
<summary>Examples</summary>

_Resuming a session_

```javascript
session.resume(true).then(() => {
  console.log('Session was resumed by re-attaching');
});
```

</details>

---

#### send(request) `function`

Function used to send data on the RPC socket.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request` | Object | Yes | - | The request to be sent. (data and some meta info) |

##### Returns

`Object` - Returns a promise instance.

---

#### suspend(code?, reason?) `function`

emits [suspended](#suspendedevt-event)

Suspends the enigma.js session by closing the websocket and rejecting all method calls
until it is has resumed again.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `code` | number | No | 4000 | The reason code for suspending the connection. |
| `reason` | string | No | "" | The human readable string describing why the connection is suspended. |

##### Returns

`Promise<Object>` - Eventually resolved when the websocket has been closed.

<details>
<summary>Examples</summary>

_Suspending a session_

```javascript
session.suspend().then(() => {
  console.log('Session was suspended');
});
```

</details>

---

#### closed() `event`

Handles closed state. This event is triggered when the underlying websocket is closed and
config.suspendOnClose is false.

<details>
<summary>Examples</summary>

_Handling session closed_

```javascript
session.on('closed', () => {
  console.log('Session was closed, clean up!');
});
```

</details>

---

#### notification() `event`

Handles all JSON-RPC notification events, 'notification:* or handles a specific JSON-RPC
notification event, 'notification:OnConnected'. These events depend on the product from which
you use QIX Engine.

<details>
<summary>Examples</summary>

_Bind the notification events_

```javascript
// bind all notifications to console.log:
session.on('notification:*', console.log);
// bind a specific notification to console.log:
session.on('notification:OnConnected', console.log);
```

</details>

---

#### opened() `event`

Handles opened state. This event is triggered whenever the websocket is connected and
ready for communication.

<details>
<summary>Examples</summary>

_Bind the session opened event_

```javascript
session.on('opened', () => {
  console.log('Session was opened');
});
```

</details>

---

#### resumed() `event`

Handles resumed state. This event is triggered when the session was properly resumed. It is
useful in scenarios where, for example, you can close blocking modal dialogs and allow the
user to interact with your application again.

<details>
<summary>Examples</summary>

_Handling session resumed_

```javascript
session.on('resumed', () => {
  console.log('Session was resumed, we can close that "reconnecting" dialog now');
});
```

</details>

---

#### suspended(evt) `event`

Handles suspended state. This event is triggered in two cases (listed below). It is useful
in scenarios where, for example, you want to block interaction with your application until
you resume again. Or, if config.suspendOnClose is true and there was a network disconnect
(socket closed) or if you ran session.suspend().

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `evt` | object | Yes | - | Event object. |

<details>
<summary>Examples</summary>

_Handling session suspended_

```javascript
session.on('suspended', () => {
  console.log('Session was suspended, retrying...');
  session.resume();
});
```

</details>

---

#### traffic() `event`

Handles websocket messages. Generally used for debugging purposes. `traffic:*` will handle all
websocket messages, `traffic:sent` will handle outgoing messages, and `traffic:received` will
handle incoming messages.

<details>
<summary>Examples</summary>

_Bind the traffic events_

```javascript
// bind both in- and outbound traffic to console.log:
session.on('traffic:*', console.log);
// bind outbound traffic to console.log:
session.on('traffic:sent', console.log);
// bind inbound traffic to console.log:
session.on('traffic:received', console.log);
```

</details>

---
