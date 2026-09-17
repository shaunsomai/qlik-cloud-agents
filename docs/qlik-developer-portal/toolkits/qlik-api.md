---
source: https://qlik.dev/toolkits/qlik-api/
last_updated: 2026-01-19T14:21:00Z
---

# Qlik-api overview

This package provides a JavaScript API for interacting with Qlik Sense REST APIs
including the Qlik Associative Engine from a single package that can be used in
both Node.js and browser contexts.

## Get Started

For NodeJS applications or in the case of building a web app with a bundler use:

```sh
npm install --save @qlik/api
```

If code will run directly in a browser it is recommended to load the code directly from a CDN.

```html
<script type="module">
  import qlikApi from "https://cdn.jsdelivr.net/npm/@qlik/api/index.mjs";
  ...
</script>
```

## Module structure

`@qlik/api` is a collection of JavaScript modules which each exposes an API
built to make the integration process for JavaScript solutions as easy as
possible. The library is built for both browser and NodeJS usage and will
seamlessly integrate with `@qlik/embed` libraries.

The modules can be imported in a few different ways. Either directly through a
sub module

```ts
import subModule, { namedExport, type NamedType } from "@qlik/api/sub-module";
```

Or through the main module. If types from a sub module is needed they can only
be imported directly from the sub module itself. They can't be imported from the
main module.

```ts
import { subModuleA, subModuleB } from "@qlik/api";
import type { SubModuleAType } from "@qlik/api/sub-module-a";
import type { SubModuleBType } from "@qlik/api/sub-module-b";
```

`@qlik/api` also has a default export with each sub module as properties.

```ts
import qlikApi from "@qlik/api";

qlikApi.subModuleA;
qlikApi.subModuleB;
```

The modules that can be imported from `@qlik/api` are the rest entities, the
`qix` sub module and an `auth` module. All described below.

## REST API

`@qlik/api` library is generated from OpenAPI specifications released from
those Qlik Cloud services that exposes a restful API. The code generation tool
runs using the specs building TypeScript for all API calls specified in the
specs. One module per API is generated.

Learn more in the [REST](https://qlik.dev/toolkits/qlik-api/rest/) section.

## QIX API

One of the most important services available is Qlik's Analytics Engine Service
which is also known as the Qlik Associative Engine. `@qlik/api` offers a fully
typed API for connecting to and consuming Qlik Sense Applications including
"Qlik Sense mixins" which previously only was used internally by in-house
Qlik developers.

Learn more in the [QIX](https://qlik.dev/toolkits/qlik-api/qix/) section.

## Authentication

`@qlik/api` comes with several authentication options to make the integration
experience as easy as possible for external users.

Learn more in
the [authentication](https://qlik.dev/toolkits/qlik-api/authentication/) section.

## Features

`@qlik/api` comes with some handy features to make the development experience
as good as possible.

Learn more in
the [features](https://qlik.dev/toolkits/qlik-api/features/) section.

## Examples

Check out the [examples](https://qlik.dev/toolkits/qlik-api/examples) section.
