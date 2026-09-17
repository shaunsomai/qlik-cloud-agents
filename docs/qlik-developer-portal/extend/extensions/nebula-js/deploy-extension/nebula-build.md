---
source: https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-build/
last_updated: 2026-06-02T18:15:45+01:00
---

# Nebula build

Build a nebula visualization bundle

## Usage

```bash
nebula build
```

## Example

Specify a different configuration file

```bash
nebula build --config config/my-nebula-config.js
```

Activate file watching for changes in the source files in the `/src` directory,
and automatically rebuild the bundle when changes are detected, with the default bundle format set to UMD

```bash
nebula build --watch
```

Build the bundle without generating source maps (`.js.map` files)

```bash
nebula build --sourcemap false
```

In the development mode, the output files are not minified

```bash
nebula build --mode development
```

Disable the SystemJS module format bundle generation

```bash
nebula build --systemjs false
```

Enable core build generation, with the default output target for compiling ES modules set to `./core`

```bash
nebula build --core
```

Enable TypeScript parsing and bundling

```bash
nebula build --typescript
```

## Options

| Parameter                                                    | Description                                                  | Default            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------ |
| --version boolean                                            | Show version number                                          |                    |
| --config, -c string                                          | Set the path to a config file                                | "nebula.config.js" |
| --watch, -w boolean\|string (true\|false\|"umd"\|"systemjs") | Rebuild bundle when its source files change on disk          | false              |
| --sourcemap, -m boolean                                      | Generate source maps                                         | true               |
| --mode string ("production"\|"development")                  | Set the mode                                                 |                    |
| --systemjs boolean                                           | Transpile a SystemJS module format bundle for release        | true               |
| --core string                                                | Set a core build target for compiling ES Modules for release | "core"             |
| --typescript boolean                                         | Enable TypeScript parsing and bundling                       | false              |
| -h, --help                                                   | Show help for the command                                    |                    |

## Details

### Module bundler

Nebula build uses [rollup.js](https://rollupjs.org/guide/en/), a module bundler, to
compile the Nebula visualization code into a bundle that can be seamlessly integrated as a Qlik Sense extension.

Nebula build supports three formats, UMD (Universal Module Definition),
ESM (ECMAScript modules), and SystemJS module.
The UMD code is used by [nebula sense](https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-sense) to generate
Qlik Sense compatible files for use as an Extension.

> **Note:** In your root package.json file, ensure that the `main` field is set to the correct path, such as 'your-dir/your-file.js'.
> As `nebula build` references it to determine the output location of the UMD code.
>
> Additionally, the `peerDependencies` are treated by nebula build as external dependencies
> that are not bundled with your local JavaScript , thereby reducing the size of the bundle.

### Configuration file

Nebula build CLI automatically recognizes the 'nebula.config.js' file in your root directory as the configuration file,
you can set the path and filename of your preference with `nebula build --config your-path/your-name.js` command.

In the configuration file, the following build properties can be set:

- replacementStrings
- watch
- sourcemap
- mode
- systemjs
- core
- typescript

`replacementStrings` is set to replace strings in files during bundling
and the rest has the same meaning and purpose as the options preceding.

An example of setting the nebula build configuration in a config file is as follows:

```js
const path = require("path");
const targetPkg = require(path.resolve(process.cwd(), "package.json"));
const replacementStrings = {
  "process.env.PACKAGE_VERSION": JSON.stringify(targetPkg.version),
};
const mode =
  process.env.NODE_ENV === "production" ? "production" : "development";
const sourcemap = mode !== "production";

module.exports = {
  build: {
    replacementStrings,
    watch: true,
    sourcemap,
    mode,
    systemjs: false,
    core: "core",
    typescript: true,
  },
};
```

### Watch

You can specify different watching modes using the `--watch` option, with values `true`, `false`, `"umd"`, or `"systemjs"`:

```bash
nebula build # Disable watching
nebula build --watch # Watch for changes and rebuild in UMD format
nebula build --watch umd # Watch for changes and rebuild in UMD format
nebula build --watch systemjs # Watch for changes and rebuild in SystemJS format
```

### Source map

A source map is a file that maps from the bundled source file to the original
source files, allowing the browser to reconstruct and present the original source
code in the debugger. Thus, if there is an error in a file in the `/dist` directory,
the source map can tell you the original source file location.

Source maps are primarily useful for debugging and should be removed in production.

### Mode

Environment settings can be specified using the `--mode` parameter.

Production mode minifies all compiled modules, while development
mode keeps them unminified.
Minified output is the default, unless `watch` mode is enabled.

### SystemJS build

The generation of the SystemJS module format bundle is automatically enabled by default.

To specify the output file for the SystemJS module format bundle, you should
add a `systemjs` field in the `package.json` file:

```json
"systemjs": "dist/hello.systemjs.js"
```

### Core build

You can build an ESM bundle by adding the `--core` parameter.
The default output target for compiling ES modules is set to `./core` directory.

```bash
nebula build --core
```

Before running the preceding command,
you should first add a package.json file in the `/core` directory
and then specify the output file in a `module` field in that `package.json` file:

```json
"module": "core/esm/index.js",
```

After running the preceding command, the ESM bundle (`index.js`) is exported into the `/core/esm` directory.

To specify another directory, move the `package.json` file
into that directory and change the string in the `module` field accordingly:

```json
"module": "minimal/target/index.js",
```

and run the following command:

```bash
nebula build --core minimal/target
```

The `index.js` file is exported into the `/minimal/target` directory.

> Note: your added `package.json` file can have a different list of `peerDependencies`
> compared to the root `package.json` file, changing which dependencies are included in the ESM bundle.

### Typescript

With the `--typescript` option, you can enable TypeScript parsing and bundling for your code.

```bash
nebula build --typescript
```

To configure TypeScript according to your preferences, you should add a `tsconfig.json` file.
