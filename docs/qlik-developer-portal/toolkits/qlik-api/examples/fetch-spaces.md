---
source: https://qlik.dev/toolkits/qlik-api/examples/fetch-spaces/
last_updated: 2026-01-19T14:21:00Z
---

# Fetch spaces in a tenant

## Node.js using an API Key

This examples shows how to fetch the space list from a tenant.

```typescript
import { auth, spaces } from "@qlik/api";

const x = {
  host: "your-tenant.region.qlikcloud.com",
  authType: "apikey",
  apiKey: "<api-key>",
};

auth.setDefaultHostConfig(x);

async function main() {
  const { data: mySpaces } = await spaces.getSpaces({});
  console.log(mySpaces.data); // the data response (list of spaces)
}

await main();
```

Run the code with

```shell
node fetch-spaces.mjs
```

## Node.js using OAuth2

Create a file `fetch-spaces.mjs` and add the following:

```typescript
import { auth, spaces } from "@qlik/api";

const hostConfig = {
  host: "your-tenant.region.qlikcloud.com",
  authType: "oauth2",
  clientId: "<client-id>",
  clientSecret: "<client-secret>",
};

auth.setDefaultHostConfig(hostConfig);

async function main() {
  const { data: mySpaces } = await spaces.getSpaces({});
  console.log(mySpaces.data); // the data response (list of spaces)
}

await main();
```

Run the code with

```shell
node fetch-spaces.mjs
```

## Browser using cookies

When using a browser you can load the library files from a CDN provider. It is
also possible to use `npm` and a bundler to get the code into your application. In
the HTML below, an API call fetches the spaces from a tenant and
adds the names of the spaces as div elements in the dom.

```html
<!doctype html>
<html lang="en">
  <head>
    <title>Fetching spaces with @qlik/api</title>
  </head>
  <body>
    <div id="space-container" class="container">
      <div>Spaces:</div>
      <!-- Spaces will be added here -->
    </div>
    <script type="module">
      import { auth, spaces } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.mjs";

      auth.setDefaultHostConfig({
        host: "your-tenant.region.qlikcloud.com",
        authType: "cookie",
        webIntegrationId: "<web-integration-id>",
      });

      const { data: mySpaces } = await spaces.getSpaces();
      const spaceContainer = document.getElementById("space-container");
      for (const space of mySpaces.data) {
        const div = document.createElement("div");
        div.innerText = space.name;
        spaceContainer.appendChild(div);
      }
    </script>
  </body>
</html>
```

## Browser using OAuth2

Use the preceding example but change the host configuration to
use [OAuth2](https://qlik.dev/toolkits/qlik-api/authentication#oauth2).
