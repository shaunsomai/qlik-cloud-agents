---
source: https://qlik.dev/manage/platform-operations/private-content-bots/
last_updated: 2025-12-08T15:03:34Z
---

# Managing personal and private content

## Introduction

When an end user leaves your company, what happens to the analysis they create
and curate? When you need to extract and promote a sheet from a Sense app in a
managed space to a base-level asset, how do you do that?

In this tutorial, you are going to learn how to configure an OAuth
machine-to-machine client to access resources located in personal spaces.
You will also learn how to access private content like sheets in a Qlik
Sense analytics app to copy/paste it into another app and publish it.

## Prerequisites

To complete this tutorial you need:

- A Qlik Cloud enterprise tenant.
- Access to create an OAuth machine-to-machine client in the management console.
- Knowledge of JavaScript.

For the rest of this tutorial, the OAuth machine-to-machine client is called
the *private content bot*.

## Configuration

### Create an OAuth client

Access the management console in your Qlik Cloud tenant
and [create a machine-to-machine
OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).

When you create the OAuth client:

- Select the `admin.apps` scope.
- Select the `admin_classic` scope.
- Check the machine-to-machine grant type checkbox.

Save the OAuth client per the instructions in the OAuth client tutorial. Record
the `client_id` and `client_secret` for later use.

You have created the private content bot.

### Create a host configuration in qlik-api

The `qlik-api` is a TypeScript-typed library for accessing Qlik Cloud REST APIs
and the Qlik Analytics Engine. The library works as an ES module only, so you
may have to configure your `package.json` to support `type: 'module'`.

The `hostConfig` variable is where you input the information to connect to your
Qlik Cloud tenant. Adding the `scope` property is optional as machine-to-machine
tokens automatically scopes to their configuration in the management console.

Set `qlik-api` to use the `hostConfig`  by issuing the
`auth.setDefaultHostConfig()` command with the `hostConfig` variable as a
parameter.

```javascript
import { auth, spaces } from "@qlik/api";

const hostConfig = {
  host: "<your-tenant>.<region>.qlikcloud.com",
  authType: "oauth2",
  clientId: "<client-id>",
  clientSecret: "<client-secret>",
  scope: "user_default admin.apps admin_classic",
};

auth.setDefaultHostConfig(hostConfig);
```

You can begin issuing requests as the private content bot using qlik-api.

## Use the private content bot with qlik-api

### List analytics apps in personal spaces

In this example, the private content bot uses `qlik-api` to list analytics
apps in personal spaces and obtain each app owner's name.

```javascript
import { auth, users, items } from "@qlik/api";

(async () => {
  auth.setDefaultHostConfig(hostConfig);

  //get apps in personal spaces
  const { data: itemResponse } = await items.getItems({
    resourceType: "app",
    spaceType: "personal",
    limit: 100,
  });
  
  const itemList = itemResponse.data;
  
  //use a promise to return a new array of apps containing the app owner's name
  let appList = await Promise.all(
    itemList.map(async (item) => {
      return {
        id: item.id,
        resourceId: item.resourceId,
        name: item.name,
        ownerId: item.ownerId,
        ownerName: await getUserName(item.ownerId),
      };
    }),
  );
  console.log(appList);
  process.exit();
})();

//helper function that returns a name for the supplied userId
async function getUserName(userId) {
  const user = await users.getUser(userId);
  return user.data.name;
}
```

### List a user's private sheets

```javascript
import { auth, qix} from "@qlik/api";

const appId = "ff345764-ee83-4488-8637-e93ddb7ccc47";

(async () => {
  auth.setDefaultHostConfig({
    authType: "oauth2",
    host: "<your-tenant>.<region>.qlikcloud.com",
    clientId: "<client-id>",
    clientSecret: "<client-secret>",
    scope: "user_default admin.apps admin_classic",
  });

  const app = await qix.openAppSession(appId).getDoc();
  const sheets = await app.getSheetList();
  for(let sheet of sheets) {
    console.log(sheet.qMeta.title, sheet.qMeta.privileges, `Current publish status is:${sheet.qMeta.published}`);
  }
  process.exit();
})();
```

### Publish a private sheet

```javascript
import { auth, qix } from "@qlik/api";

const appId = "ff345764-ee83-4488-8637-e93ddb7ccc47";
const sheetId = "fa5fc527-3717-4a90-88f0-c6e4638c60b0";

(async () => {
  auth.setDefaultHostConfig(hostConfig);

  const app = await qix.openAppSession(appId).getDoc();
  const sheet = await app.getObject(sheetId);
  
  try {
    await sheet.publish();
    await app.doSave();
    console.log("Published");
  } catch (error) {
    console.log(error);
  }

  process.exit();
})();
```

### Duplicate a sheet in an app and change its owner

```javascript
import { auth, users, items, qix, apps } from "@qlik/api";

const appId = "ff345764-ee83-4488-8637-e93ddb7ccc47";
const sheetId = "fa5fc527-3717-4a90-88f0-c6e4638c60b0";

(async () => {
  auth.setDefaultHostConfig(hostConfig);

  const app = await qix.openAppSession(appId).getDoc();
  const sheet = await app.getObject(sheetId);
  const sheetPropsTree = await sheet.getFullPropertyTree();

  //duplicate the sheet by creating a new object;
  //if you are inserting into a new app, you do not need to
  //change the object ID.
  sheetPropsTree.qProperty.qInfo.qId = "randoString21";

  //create the new sheet by supplying the QProperty attribute.
  const newSheet = await app.createObject(sheetPropsTree.qProperty);
  
  //get the properties so you can confirm the object ID
  const newSheetProps = await newSheet.getProperties();
  console.log(newSheetProps);
  
  //save the app to persist changes
  await app.doSave();

  //run apps.updateAppObjectOwner to change the owner of the sheet
  try {
    const co = await apps.updateAppObjectOwner(appId,newSheetProps.qInfo.qId,{"ownerId": "64fb23dd7a7b40079f26346c"});
    await app.doSave();
    console.log(co);

  } catch (error) {
    console.log(error);
  }

  //sheet will show up in private. This example was performed
  //on an app in a managed space.

  process.exit();

})();
```

## Conclusion

These are just a few of the different management actions you can take with the
new private content bot.
