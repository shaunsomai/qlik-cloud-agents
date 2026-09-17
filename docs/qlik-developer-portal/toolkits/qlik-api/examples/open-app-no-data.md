---
source: https://qlik.dev/toolkits/qlik-api/examples/open-app-no-data/
last_updated: 2026-01-19T14:21:00Z
---

# Open an app without data

Large apps take longer to open in the Qlik Associative Engine.
If you only need to read or write metadata, opening the app without data is faster.

> **Use a distinct identity for sessions without data:** Always specify an identity for sessions opened without data to reduce the risk of collisions with active sessions the
> user might already have in the app with data.
> If you attempt to access an app in both modes using the same identity, you will receive an error.

Here's how to open an app without data:

```ts
import { apps, auth, qix } from "@qlik/api";

const hostConfig = {
  host: "your-tenant.region.qlikcloud.com",
  authType: "apikey",
  apiKey: "<api-key>",
};

auth.setDefaultHostConfig(hostConfig);

async function main() {
  try {
    const appId = "<app-id>"; // <- replace this with an appid

    const session = qix.openAppSession({ appId, withoutData: true, identity: "withoutdata" });
    const app = await session.getDoc();
    const appLayout = await app.getLayout();
    console.log(appLayout);
  } catch (e) {
    console.error(e);
  } finally {
    session.close();
  }
}

await main();
```
