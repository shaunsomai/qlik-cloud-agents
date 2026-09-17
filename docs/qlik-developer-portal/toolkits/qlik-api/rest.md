---
source: https://qlik.dev/toolkits/qlik-api/rest/
last_updated: 2025-07-08T16:09:30Z
---

# REST

Each rest entity is exposed as its own JavaScript module. It contains all API
calls and types exposed by the entity service. They can be imported from
`@qlik/api` as a sub module of the package like `/spaces` in the example below.
These modules both have named exports and a default export. Types are always
named exports.

```ts
import spaces, { type Spaces } from "@qlik/api/spaces";
await { data: mySpaces } = await spaces.getSpaces();

// mySpaces now has the type Spaces
```

Each module can also be imported directly from `@qlik/api`.

```ts
import { spaces, users } from "@qlik/api";
```

These modules are the default exports from each respective sub module. The types
from the sub modules are not exposed here since they would introduce name
conflicts. The types need to be imported from the respective sub modules.

For more information on these entities and their APIs, see
[Overview of Qlik APIs](https://qlik.dev/apis).

## HTTP Calls

HTTP calls uses the native fetch API. Each HTTP call with a response status
in the 200 range will resolve to an object with structure
`{ status, headers, data }`. If the status is in the >=300 range, an error will be
thrown.

```ts
import { getSpaces } from "@qlik/api/spaces";

try {
  const { status, headers, data: spaces } = await getSpaces();
  // status < 300
  if (spaces.data) {
    // the spaces list is returned as "data"
    // There are spaces
  }
} catch (e) {
  // status >= 300
  // something went wrong
}
```

## Error handling

Every HTTP response that has a status over 300 is considered to be an error and
the promise is rejected. To handle this in TypeScript, you can do the following:

```ts
import { deleteExtension, type DeleteExtensionHttpError } from "@qlik/qmfe/extensions";

try {
  const { status } = await deleteExtension("<extension-id>");
  ...
} catch (e as DeleteExtensionHttpError) {
    if (e.status === 404) {
        // DeleteEndpoint404HttpError
        e.data // < -- body of error
    }
}
```

## Caching

Every GET request is cached so that subsequent calls to the same API will
resolve immediately from the cache. For more information on caching, see
[Features](https://qlik.dev/toolkits/qlik-api/features).
