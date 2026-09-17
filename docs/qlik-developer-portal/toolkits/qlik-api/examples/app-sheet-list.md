---
source: https://qlik.dev/toolkits/qlik-api/examples/app-sheet-list/
last_updated: 2026-01-19T14:21:00Z
---

# Obtain a list of sheets from an analytics app

For this example, you need the ID of a Qlik Sense app that you have access to.
To get the ID of an app, click the "More actions" button on the app
from the Qlik Cloud Hub and click **details**. There, the app ID is visible.
Another option is to open the app and look at the URL. The app ID is located as
`/sense/<app-id>/` in the URL.

## Node.js using an API Key

```ts
import { auth, qix } from "@qlik/api";

const hostConfig = {
  authType: "apikey",
  host: "your-tenant.region.qlikcloud.com",
  apiKey: "<api-key>",
};

// to use "Oauth2" auth module switch hostConfig to oauth2 and set clientId
// and clientSecret instead of apiKey.

const appId = "<app-id>";

auth.setDefaultHostConfig(hostConfig);

async function main() {
  const session = qix.openAppSession({ appId });
  const app = await session.getDoc();

  const sheetList = await app.getSheetList();
  console.log(sheetList);
  session.close();
}

main();
```

The `app.getSheetList()` method is a "sense mixin", which is an extension of the
official QIX API used for Qlik Sense apps.
`@qlik/api` includes all "sense mixins", allowing you to interact with Qlik Sense
apps the same way in-house Qlik developers do.

## Browser using cookies

When using a browser you can load the library files from a CDN provider. It is
also possible to use npm and a bundler to get the code into your app. In
the HTML below, make an API call to fetch the sheet list from a Qlik
Sense app and add the sheet titles as `<div>` elements to the DOM.

```html
<!doctype html>
<html lang="en">
  <head>
    <title>Fetching sheet list from an app with @qlik/api</title>
  </head>
  <body>
    <div id="sheet-container" class="container">
      <div>Sheets:</div>
      <!-- Sheets will be added here -->
    </div>
    <script type="module">
      import { auth, qix } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js";
      auth.setDefaultHostConfig({
        host: "your-tenant.region.qlikcloud.com",
        authType: "cookie",
        webIntegrationId: "<web-integration-id>",
      });
      const appId = "<app-id>";
      const session = qix.openAppSession({ appId });
      const app = await session.getDoc();
      const sheetList = await app.getSheetList();
      const sheetContainer = document.getElementById("sheet-container");
      for (const sheet of sheetList) {
        const div = document.createElement("div");
        div.innerText = sheet.qMeta.title;
        sheetContainer.appendChild(div);
      }
      session.close(); // closing the app
    </script>
  </body>
</html>
```
