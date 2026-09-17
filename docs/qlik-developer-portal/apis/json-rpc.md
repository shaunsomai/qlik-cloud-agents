---
source: https://qlik.dev/apis/json-rpc/
last_updated: 2026-03-18T16:49:43Z
---

# JSON-RPC API (QIX API)

## Overview

The QIX API is the primary API used for working directly with Qlik Sense apps and the Qlik Associative Engine.

The QIX API offers the following features:

- WebSocket-based communication: this API uses the WebSocket protocol for interacting with the Qlik Associative Engine.
- Enhanced JSON-RPC protocol: the QIX API implements a superset of the
  [JSON-RPC protocol](https://www.jsonrpc.org/specification), with Qlik-specific enhancements for interacting with Qlik
  objects and methods.
- Stateful sessions: this API maintains session state, enabling session sharing.
- Handle-based object references: the QIX API uses handles to reference and interact with objects within the
  Qlik Associative Engine.

> You can use [Automations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm),
> [`@qlik/api`](https://qlik.dev/toolkits/qlik-api/), [`qlik-cli`](https://qlik.dev/toolkits/qlik-cli/), or the [Platform SDK](toolkits/platform-sdk/)
> to work with the QIX API without managing a WebSocket client directly.

## WebSockets

When you want to use the API, any WebSocket client implementation that follows
the [RFC specification](https://tools.ietf.org/html/rfc6455) should be supported.
The URL format is:

```http
wss://your-tenant.us.qlikcloud.com/app/<APP_ID>
```

Browser example:

```js
const websocket = new WebSocket(
  "wss://your-tenant.us.qlikcloud.com/app/123e4567-e89b-12d3-a456-426655440000"
);
```

### Headers

In a non-browser environment, most WebSocket client implementations support adding headers.

Use the header `Authorization: Bearer <token>` with an [API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key) for
authentication.

### Session sharing

When using the QIX API, you build up a state in what's called a session. A session is based on
a tenant, a user, an identity, and the app.

When opening a new WebSocket, you either get a new unique session, or get attached to an existing session. When sharing
a session, the state (like selections) is shared between all WebSocket connections.

The conditions for sharing a session are the following:

- The WebSocket URL needs to be identical (tenant URL and app ID).
- The user needs to be the same:
  - In a *browser* environment, the same user needs to be signed in.
  - In a *non-browser* environment, an API key from the same user and tenant
    needs to be used.

## JSON-RPC communication

The QIX API uses the [JSON-RPC protocol](https://www.jsonrpc.org/specification) for communication.
All requests sent from the client should contain the following properties:

```json
{
  // Protocol descriptor:
  "jsonrpc": "2.0",
  // Session-unique numeric ID, referred to in the response
  // to connect the request and response:
  "id": 6,
  // The handle for the object to interact with:
  "handle": 2,
  // The object type of the handle above decides
  // which API methods you may invoke:
  "method": "ApiMethodName",
  // Parameters for the invoked API method:
  "params": {}
}
```

### Example request

In this example request, an app is opened using [OpenDoc](https://qlik.dev/apis/json-rpc/qix/global/#opendoc).
If successful, the response contains a reference to the app handle, which can be used to do further requests towards the
[Doc](https://qlik.dev/apis/json-rpc/qix/doc) (app) API, and so forth.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "handle": -1,
  "method": "OpenDoc",
  "params": {
    "qDocName": "<APP_ID>"
  }
}
```

Note that there is only *one* static handle in the QIX API: `-1`.
This handle refers to the [Global](https://qlik.dev/apis/json-rpc/qix/global) API.

### Example response

If that app exists, the response would look similar to this:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "qReturn": {
      "qType": "Doc",
      "qHandle": 1,
      "qGenericId": "<APP_ID>"
    }
  },
  "change": [1]
}
```

> **Notes:**
>
> - `qHandle` contains the handle that might be used to make additional
>   requests to invoke API methods towards the app.
> - The `change` property is also included in the response.
>   This array can be sent by the Qlik Associative Engine
>   in any responses and contains all open handles in your session
>   that may have been invalidated. You should refetch the data to ensure
>   your application in a valid state.

## Session apps

Session apps are non-persisted Qlik Sense apps created on-the-fly in server
memory by the Qlik Associative Engine. You must define a load script and
trigger a data reload before any data model is accessible for each user
session. Similarly, if you create a session app from an existing app, you
must trigger a reload after retrieving objects from the template app.

Session apps are generated for an active Qlik Associative Engine session. When the session
ends, for example, when the user logs out, the session app is terminated, and all related resources
are released from server memory.

The WebSocket URL for creating a session app has the following format:

```http
wss://my-tenant.us.qlikcloud.com/app/SessionApp_{appId}
```

You must append a unique app ID to `SessionApp_` in the path. The app ID can
be a code-generated random number.

To create a session app from an app, you must add the template app ID as a
query parameter to the URL:

```http
wss://my-tenant.us.qlikcloud.com/app/SessionApp_{appId}?from={templateAppId}
```

## Error handling

When an error occurs, the API closes the WebSocket connection with a 4-digit error code and an optional
message.
To monitor these errors, use the following code:

```javascript
ws.on("close", (code, message) => {
  console.log(code);
  console.log(String(message));
});
```

Example response:

```json
4204
{"code":"QEP-104","traceId":"491a33e544de8dda40a9fc9b0cb53216"}
```

The following list includes common error codes and their causes:

- 4202 - the WebSocket request appears to be malformed.
- 4203 - the request could not be fulfilled because of a permissions
  issue.
- 4204 - the request failed because something could not be found. This
  may be because the app ID in the URL is incorrect or the app has been
  deleted.
- 4205 - the request could not be fulfilled because the system is busy,
  consider sending the request again later.
- 4230 - the request could not be fulfilled because there are too many
  open apps in your organization.
- 4240 - the request could not be fulfilled because there are no available
  engines.

## API reference documentation
