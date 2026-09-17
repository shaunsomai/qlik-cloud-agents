---
source: https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-cli/
last_updated: 2026-06-02T18:15:45+01:00
---

# nebula CLI

The nebula command-line tool (CLI) is the main entry point for getting up and
running with a nebula visualization, for using features including running
a development server and building out your visualization for extension and mashup.

## How to run nebula CLI

The nebula CLI is available via `npm` and can be installed globally by running the following:

```bash
npm install @nebula.js/cli -g
```

When you do not want to install nebula CLI globally, you can still use it, for example creating a new nebula
visualization by run the following:

```bash
npx @nebula.js/cli create sn-table
```

### Usage

All the following usage is available in the tool by running `nebula --help`.

```bash
nebula <command> [options]

Commands:
  nebula create <name>    Create a visualization
  / create mashup <name>  / Create a mashup
  nebula build          Build visualization
  nebula serve          Start a development server
  nebula sense          Build a nebula visualization as a Qlik Sense extension

Options:
  --version   Show version number                                      [boolean]
  -h, --help  Show help                                                [boolean]
```

## How to use nebula CLI in your visualization

You can use the package.json script variant of these commands, which are exposed
for you with [`nebula create`](https://qlik.dev/libraries-and-tools/nebulajs/nebula-create).
When you want to make the `nebula serve`, `nebula build`, and `nebula sense`
commands available in your visualization by yourself, run the following command.

```bash
npm install @nebula.js/cli @nebula.js/cli-build @nebula.js/cli-sense @nebula.js/cli-serve
```

Open up your package.json, those dependencies are added.

```json
{
  "devDependencies": {
    "@nebula.js/cli": "1.7.0",
    "@nebula.js/cli-build": "1.6.0",
    "@nebula.js/cli-sense": "1.7.0",
    "@nebula.js/cli-serve": "1.7.0"
  }
}
```

and add a script like so:

```json
"scripts": {
    "build": "nebula build",
    "start": "nebula serve",
    "sense": "nebula sense"
  },
```

You can also run nebula CLI commands with Node.js. Create a JavaScript file called build.js
and add the following:

```js
const build = require('@nebula.js/cli-build');
const sense = require('@nebula.js/cli-sense');

await build({
  config: '../nebula.config.js',
  sourcemap: false,
  core: 'core',
  mode: 'production',
  watch: false,
});
await sense({ output: 'sn-table-ext', sourcemap: true });
```

and run the following command:

```bash
node build.js
```

## How to test your modified nebula CLI locally and globally

Requirements:

- Node.js
- yarn

Clone the repository:

```bash
git clone https://github.com/qlik-oss/nebula.js
```

From the root directory, run the following command to install all the necessary
dependencies of nebula CLI:

```bash
yarn
```

You can modify code in commands directory and do the following to test modified
nebula CLI locally and globally:

### Test nebula CLI locally

Run nebula CLI locally to see help info using node.js:

```bash
cd commands/cli
node lib/index.js -h
```

### Test nebula CLI globally

From the commands/cli directory, run the following command to create a global
symlink to the binary:

```bash
yarn link
```

Run nebula CLI globally to see help info to verify whether it works:

```bash
nebula -h
```

Tips:

If 'There's already a package called "@nebula.js/cli" registered.' or 'command
not found: nebula' is displayed.

Run the following command to remove the symlinked nebula and run 'yarn link' again:

```bash
yarn unlink
```
