---
source: https://qlik.dev/toolkits/qlik-api/features/
last_updated: 2025-12-08T15:03:34Z
---

# Features

## Typed API calls

Each API comes with full TypeScript support to enhance the developer experience.
Use the types to understand how the API works by going
into the type definition. In most editors, like VS Code, you can use `CMD+click` (macOS)
or `CTRL+click` (Windows) on an api-call to see the type definition of parameters,
return structures, etc.

## Caching

Request responses are cached in the browser so requests can be fired away
without being concerned about causing unnecessary traffic. Ongoing requests are
also re-used if two equal requests go out at the same time. A request can be
forced by adding an option to the call `{ noCache: true }`. Clearing cache can
be automatically handled as shown in
[Automatic cache clearing and auto CSRF](#automatic-cache-clearing-and-auto-csrf).

```ts
import { getItems } from "@qlik/api/items";

try {
  await getItems();
  await getItems();
  await getItems();
  await getItems();
  // the 4 requests above will result in only one request over network

  // empty query object as 1st parameter, 2nd parameter is the ApiCallOptions
  await getItems({}, { noCache: true });
  // this request above will result in a network call because of the noCache option
} catch (e) {
  // something went wrong
}
```

### Automatic cache clearing and auto CSRF

Requests that need parameters are all using documented types inherited from the
spec files. Requests that require a valid csrf-token automatically fetch it
(once if needed) and add it to the outgoing requests headers. Requests that
change resources (for example POST/PUT) automatically clear the cache.

```ts
import { getSpaces, createSpace } from "@qlik/api/spaces";

try {
  let { data: spaceList } = await getSpaces({});
  // spaceList has 2 items
  const { data: space } = await createSpace({ name: "My space", description: "description", type: "shared" });
  // the call above automatically adds a csrf-token header. If no csrf-token has been fetched yet it will first fetch it.
  // space now has the Space type and your editor will show the types e.g:
  // space.id;
  // space.createdAt;

  { data: spaceList } = await getSpaces(); // cached response has automatically been cleared because of createSpace call above
  // spaceList has 3 items
} catch (e) {
  // something went wrong
}
```

### Manual cache clearing

The cache for an api can be cleared with the `clearCache` method. This clears
all cached responses for that specific api. It is recommended to use the
[automatic cache clearing](#automatic-cache-clearing-and-auto-csrf).

```ts
import { getSpaces, clearCache: clearSpaceCache } from "@qlik/api/spaces";

try {
  await getSpaces();
  clearSpaceCache(); // clears all cached responses for the space api.
  await getSpaces();
  // the 2 requests above will both go out on the network
} catch (e) {
  // something went wrong
}
```

> **Note:** `clearCache` only affects one API, all other api caches are unaffected.

## Paging

Many "list" APIs return links to the next and previous page in the list GET
response body. If the API follows the conventions and declares this in the
OpenAPI spec next and prev functions will be available in the API response type.
Note that the next and prev functions are only defined when there actually is a
next and prev page.

## Interceptors

You can add interceptors to allow custom functionality to happen before or after
an API call. They run globally and affect every request made by the library.
Interceptors use a middleware pattern where you receive the request, can modify
it, call `proceed()` to continue, and then modify the response before returning it.

> **Warning:** Interceptors affect every request globally and can introduce side effects such as pausing request handling
> which affects application runtime and logic, unintended data modifications, increased resource consumption,
> or cascading failures.
> Test thoroughly before deploying to production.

The interceptor format is:

```ts
const interceptor = async (request, proceed) => {
  // do things before the request
  const result = await proceed(request);
  // do things after the request
  return result;
};
```

### Example: Add a logging interceptor

```ts
import { addInterceptor } from "@qlik/api/interceptors";

addInterceptor(async (request, proceed) => {
  try {
    // log outgoing request: method, endpoint, variables, query params, and body
    console.log("-->", request.method, request.pathTemplate, request.pathVariables, request.query, request.body);
    const result = await proceed(request);
    // log incoming response data
    console.log("<--", result.data);
    return result;
  } catch (err) {
    // log errors (prefix <-* indicates error)
    console.log("<-*", err);
    throw err; // re-throw to preserve error handling in calling code
  }
});
```

### Example: Add a custom header to requests

```ts
import { addInterceptor, removeInterceptor } from "@qlik/api/interceptors";

const headerInterceptor = addInterceptor(async (request, proceed) => {
  // initialize request.options and headers object if they don't exist
  (request.options = request.options || {}).headers = request.options.headers || {};
  // add custom header to all requests
  request.options.headers["x-another-header"] = "foobarvalue";
  return proceed(request);
});

// remove the interceptor when the header is no longer needed (for example, on logout)
removeInterceptor(headerInterceptor);
```
