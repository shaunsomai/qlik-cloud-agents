---
source: https://qlik.dev/toolkits/qlik-api/examples/get-current-selections/
last_updated: 2026-01-19T14:21:00Z
---

# getCurrentSelections with qlik-api

`getCurrentSelections` is another popular helper function in the Capability
API. What this function does is evaluate the current selection state of
an analytics application and return all the dimensions and dimension values
the user has picked in their analysis.

The `getCurrentSelections` method is helpful because it gives developers a
way to update their custom analytics pages (aka mashups) to reflect the
choices users are making in an embedded context.

Here's a code snippet of how to obtain the current selections using
`qlik-api`.

```html
<script type="module">
  import { auth, qix } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js";

  // Replace with your host configuration
  auth.setDefaultHostConfig({
    ...
  });

  // Set the appId, open a session, and get the doc.
  const appId = "6b410f36-cb58-4bce-8e6f-a37220bfd437";
  const app = await qix.openAppSession(appId).getDoc();

  // Call the getCurrentSelectionObject function.
  let currSel = await app.getCurrentSelectionObject();

  // Call a getLayout on the currSel object.
  let currSelLayout = await currSel.getLayout();
  console.log(currSelLayout);

  // Listen on the changed event to get the layout and console it again.
  currSel.on("changed", async () => {
    currSelLayout = await currSel.getLayout();
    console.log(currSelLayout);
  });

  // Now every time the user makes a selection in your mashup
  // the console will log out the current selection state of the app.

</script>
```
