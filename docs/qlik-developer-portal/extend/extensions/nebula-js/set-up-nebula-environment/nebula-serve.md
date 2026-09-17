---
source: https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-serve/
last_updated: 2026-06-02T18:15:45+01:00
---

# nebula serve

Run a nebula visualization with a nebula web development server for local development and testing purposes.

## Usage

```bash
nebula serve
```

## Example

Connect to enigma on port `9077` to start the server

```bash
nebula serve --enigma.port 9077
```

Start the server without building the visualization

```bash
nebula serve --build false
```

Start the server and set a generic object type with `sn-table`

```bash
nebula serve --type sn-table
```

Start the server with a nebula configuration file in a new path

```bash
nebula serve --type combochart --config config/my-nebula-config.js
```

## Options

| Parameter                    | Description                                                      | Default            |
| ---------------------------- | ---------------------------------------------------------------- | ------------------ |
| --version boolean            | Show version number                                              |                    |
| --config, -c string          | Set the path to the config file                                  | "nebula.config.js" |
| --entry string               | Set the file entry point                                         |                    |
| --type string                | Set the generic object type                                      |                    |
| --build boolean              | Build the nebula visualization into the /dist dictionary         | true               |
| --host string                | Set the host to use                                              | "localhost"        |
| --port number                | Set the port number to listen for requests on                    |                    |
| --disableHostCheck boolean   | Bypasses host checking                                           | false              |
| --keyboardNavigation boolean | Turn on or off nebula to handle keyboard navigation              | false              |
| --resources string           | Set the path to a folder served as static files under /resources |                    |
| --scripts array              | Set an array of scripts to inject                                |                    |
| --stylesheets array          | Set an array of stylesheets to inject                            |                    |
| --enigma.host string         | Set the host to communicate with Qlik Associative Engine         | "localhost"        |
| --enigma.port number         | Set the port number to communicate with Qlik Associative Engine  | 9076               |
| --clientId string            | Set the tenant's clientId for OAuth connection                   |                    |
| --webIntegrationId string    | Set the tenant's webIntegrationId for enabling CORS              |                    |
| --fixturePath string         | Set the path to a folder for locating fixtures                   | "test/component"   |
| --mfe boolean                | Serve the SystemJS format bundle to use in micro frontend        | false              |
| -help, -h boolean            | Show help for the command                                        |                    |

## Details

### Using node.js API

Here is an example usage of @nebula.js/cli-serve in a Node.js script. This can be used for automated tests.

```js
const serve = require('@nebula.js/cli-serve');

serve({
  port: 3000,
  entry: path.resolve(__dirname, 'sn.js') // custom entrypoint
  enigma: {
    port: 9077
  }
}).then(s => {
  s.url; // serve url
  s.close(); // close the server
});
```

### Configuration file

The `nebula.config.js` file is a configuration file used in nebula.js

```js
module.exports = {
  serve: {
    types: [
      { name: "barchart", url: "https://unpkg.com/@nebula.js/sn-bar-chart" },
    ],
    themes: [
      {
        id: "sense",
        theme: {
          /* valid sense json theme */
        },
      },
    ],
    renderConfigs: [{ element: el, id: "abcdef" }],
    flags: { SOME_FEATURE: true },
    resources: "your-resources-path",
    snapshots: [
      {
        /* valid snapshots property */
      },
    ],
    webIntegrationId: "your_web_integration_id",
  },
};
```

#### Serve properties

The properties in the serve section of the configuration file are:

- types: An array of additional chart types to load into the serve instance. This is useful when used in conjunction
  with `useEmbed` and allows you to load additional visualizations from external sources.
- themes: An array of theme files to load. Themes are used to customize the appearance of the visualization,
  and you can specify multiple themes to be loaded.
- renderConfigs: Configuration for rendering visualizations, either creating or fetching existing objects,
  which can used for testing visualizations.
- flags: Additional flag settings for feature toggling.
  You can specify various feature flags and set their values to turn on or off certain features.
- resources: The path to the /resources folder, which is used for storing resources such as images, fonts,
  and other assets used in the visualization.
- snapshots: Snapshots property structure for use in automated test scenarios.
- webIntegrationId: The unique id for a web integration representing a list of allowlisted origins
  that can make requests to a specified tenant.
  It is used to turn on the CORS mechanism within Qlik Cloud.

##### Types

For more information, see the [list of Qlik Sense native chart types](https://qlik.dev/embed/visualizations-to-embed/chart-types).

##### Themes selection

Once the themes are correctly set in the configuration file,
they will be available for selection at the top-right corner of the running nebula hub.

![theme selection in current app](https://qlik.dev/_astro/theme-selection.D7qEpQkA.png)

### Engine WebSocket URL

When visiting the URL to the nebula web development server, make sure to point the engine WebSocket URL to your tenant,
which should be in the format `wss://tenant.us.qlikcloud.com`.

### ClientID

To obtain the `clientID` (OAuth2 client Id) for running visualizations against
the SaaS Edition of Qlik Sense, you can refer to
the [Create a SPA OAuth2 client tutorial](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa).
This tutorial will guide you on how to create a new OAuth2 client and obtain
the`clientID` for Single-Page Application (SPA).

The redirect URL should be in the format `http://localhost:8000/login/callback` where port 8000
is the default for `nebula serve`.

> **Note:** For Nebula 5.0.0, the redirect URL has changed to `http://localhost:8000/auth/login/callback`.

### Web Integration Id

To obtain the `webIntegrationId` (qlik-web-integration-id) for running visualizations against
the SaaS Edition of Qlik Sense, you can refer to
the [Build a simple mashup using nebula.js tutorial](https://qlik.dev/embed/nebula/quickstart/build-a-simple-mashup#set-up-a-qlik-sense-saas-account).
This tutorial will guide you on how to set up a Qlik Cloud tenant
and create your web integration to obtain the `webIntegrationId`.

> **Note:** The URL to the nebula web development server, such as `http://localhost:8000`, should be added to the allowlisted
> origins when you create your web integration.
