---
source: https://qlik.dev/extend/extensions/extension-api/create-with-extension-api/create-extension-on-the-fly/
last_updated: 2026-06-02T18:15:45+01:00
---

# Create extensions on the fly

The `registerExtension` method allows you to register a visualization extension
in a mashup without installing it on the Qlik Sense server. After it has been
registered, it is free to use within the mashup just as if it was installed on
the server. This means that you can distribute mashups, including the extensions
being used, as one package.

## General workflow

This is the general workflow for creating extensions on the fly in mashups.

1. Configure requireJS.

2. Include the Qlik Sense CSS files.

3. Create a new extension or copy an existing extension into your mashup folder.
   You can also create a new extension inline.

4. Load the extension and register it using the `registerExtension` function.
   If the extension is created in separate folder, it must be loaded with reguireJS.

## Hello world on the fly

This example creates and registers a basic hello world extension in a mashup.

```js
//define the helloworld extension
const helloworld = {
  paint: ($element)=> {
    $element.html( "Hello world!!" );
  }
}
//register the extension
qlik.registerExtension( 'helloworld', helloworld );
```

### Complete code example: Hello world on the fly

<details>
  <summary>Visualization API</summary>

  ```javascript
  const config = {
    host: '<TENANT_URL>', //for example, 'abc.us.example.com'
    prefix: '/',
    port: 443,
    isSecure: true,
    webIntegrationId: '<WEB_INTEGRATION_ID>'
  };

   require.config({
    baseUrl: `https://${config.host}/resources`,
    webIntegrationId: config.webIntegrationId
  });

  //define the helloworld extension
  const helloworld = {
    paint: ($element)=> {
      $element.html( "Hello world!!" );
    }
  }

  require(["js/qlik"], (qlik) => {
    qlik.on('error', (error) => console.error(error));
    //register the extension
    qlik.registerExtension( 'helloworld', helloworld );

    const app = qlik.openApp('<APP_ID>', config);
    //create and show an object using the extension
    app.visualization.create( 'helloworld', ["Case Owner Group"] ).then(
     ( helloworld )=> {
       helloworld.show( "QV00" );
     });
  });
  ```
</details>

## Learn more

- [registerExtension method](https://qlik.dev/apis/javascript/capability/#entries-js/qlik-entries-registerextension)
