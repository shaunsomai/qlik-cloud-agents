---
source: https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-sense/
last_updated: 2026-06-02T18:15:45+01:00
---

# Nebula sense

Generate a nebula visualization to be used as an extension in Qlik Sense.

## Usage

```bash
nebula sense
```

## Example

Generate a visualization with an extension definition

```bash
nebula sense --ext def.js
```

Generate a visualization with a meta info

```bash
nebula sense --meta meta.json
```

Generate a visualization no need of minifying and uglifying code

```bash
nebula sense --minify false
```

Generate a visualization setting destination directory as sn-table-ext

```bash
nebula sense --output sn-table-ext
```

Generate a visualization with generating source maps - `.js.map` files

```bash
nebula sense --sourcemap
```

Generate a legacy extension to run in Qlik Sense before 2020

```bash
nebula sense --legacy
```

## Options

| Parameter       | Description                    | Default       |
| --------------- | ------------------------------ | ------------- |
| --version       | Show version number            |               |
| --ext string    | Set extension definition       |               |
| --meta string   | Set extension meta information |               |
| --output string | Set Destination directory      | "\<name>-ext" |
| --minify        | Minify and uglify code         | true          |
| --sourcemap     | Generate sourcemaps            | false         |
| --legacy        | Generate legacy extension      | false         |
| -h, --help      | Show help for command          |               |

## Details

### Meta information

You can improve meta info about the extension, such as extension name, extension
icon, and description by providing a `.json` formatted file and supply that filename
as an argument to the `nebula sense` command with `--meta` option.

Create a file called meta.json and add the following code demonstrating an example
to set the extension meta information:

```json
{
  "name": "My tasty banana extension",
  "icon": "barchart",
  "description": "Nebula test table wrapped in a Qlik Sense extension"
}
```

Run the command:

```bash
nebula sense --meta meta.json
```

The meta data is ended up in the `QEXT` file, which is detailed next section.

Copy the updated `your-chart-ext` directory to your `Extension` directory,
overwriting the old version. Then the meta data of the extension has been changed.

The rest of the required information is populated automatically based on the content
in `package.json`.

### Metadata file

Running nebula sense generates an extension metadata file (`QEXT` - short for Qlik Extension) for you, which is
required for loading the visualization into sense as it is used by Qlik Sense to identify the visualization extension.

The `QEXT` file can also be manually created by yourself.

Create a file called `your-extension-name.qext` and add the following code as an
example:

```json
{
  "name": "your-extension-name",
  "version": "0.1.0",
  "description": "",
  "author": {
    "name": "",
    "email": ""
  },
  "icon": "extension",
  "type": "visualization",
  "supernova": true
}
```

The `"supernova": true` attribute should not be added when building with the
\--legacy option below.

When creating your `QEXT` file, making sure that:

- The file is a valid JSON file
- The filename extension of the `QEXT` file (`.qext`) is in lower case letters.
- Each visualization contains at least one `QEXT` file and one JavaScript file.
- The JavaScript file and the `QEXT` file have the same name, including matching case.
- The name is unique in the Qlik Sense so prefixing of the name should be considered.

For more information about the meaning of properties in the `QEXT` file, see
[Configure your extension package](https://qlik.dev/extend/extensions/qext-file-overview)

### Extension definition

You can set property panel definition and feature support by creating a separate
file for the extension definition and providing its filename as an argument to `--ext`.

Create a file called def.js and add the following code demonstrating an example
to set the extension definition:

```js
export default {
  definition: {
    // Property panel definition
  },
  support: {
    export: true,
    exportData: true,
    snapshot: true,
    viewData: true,
  },
  importProperties: null,
  exportProperties: null,
};
```

Run the command:

```bash
nebula sense --ext def.js
```

> **Note:** Using the `--ext` option overwrites any ext definition already presented on the chart.
> Its main purpose is to support legacy option below.

### Output

Generate all required files into the specified `--output` folder called sn-table-ext:

```bash
nebula sense --output sn-table-ext
```

You upload that folder as an extension. For more information, see [Uploading and managing visualization extensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-extensions.htm)
on Qlik Help.
