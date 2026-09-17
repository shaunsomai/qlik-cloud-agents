---
source: https://qlik.dev/extend/extensions/qext-file-overview/
last_updated: 2026-06-02T18:15:45+01:00
---

# Configure your extension package

The QEXT file is a JSON manifest that identifies your visualization extension to
Qlik Cloud Analytics. It works like an npm `package.json` - it declares the name,
version, type, and display metadata that Qlik uses to register the extension in
the assets panel.

When the extension is deployed to a Qlik Cloud Analytics tenant, it appears in
the **Charts** section of the assets panel under the name, icon, and preview image
you define here.

> **Tip:** Validate your QEXT file with a JSON validator such as [JSONLint](http://jsonlint.com/) before packaging. A malformed JSON file prevents the extension from loading.

Every extension package requires at least one QEXT file and one JavaScript entry point file.

> **Note:**
>
> - The `.qext` file extension must be in lower case: `my-extension.qext`, not `my-extension.QEXT`.
> - The QEXT filename, JavaScript entry point filename, and folder name must all match exactly, including case. For example: a folder named `com-example-myviz` must contain `com-example-myviz.qext` and `com-example-myviz.js`.
> - The package name must be unique on the tenant. Use a reverse-domain prefix to avoid collisions, for example `com-example-myviz`.

## Properties

### name

Required. The display name of the extension, shown in the assets panel and in the preview.

### type

Required. Set to `visualization` for visualization extensions.

### description

Optional. A short description displayed in the extension preview.

### icon

Optional. The icon shown for the extension in the assets panel. Defaults to `extension`.

| Value                  | Icon                   |
| ---------------------- | ---------------------- |
| `"bar-chart-vertical"` | Bar chart              |
| `"extension"`          | Puzzle piece (default) |
| `"filterpane"`         | Filter pane            |
| `"gauge-chart"`        | Gauge chart            |
| `"line-chart"`         | Line chart             |
| `"list"`               | Field/list             |
| `"map"`                | Map                    |
| `"pie-chart"`          | Pie chart              |
| `"scatter-chart"`      | Scatter chart          |
| `"table"`              | Table                  |
| `"text-image"`         | Text and image         |
| `"treemap"`            | Treemap                |

### preview

Optional. The filename of a custom PNG preview image. If not set, the `icon` definition is used instead.

```text
"preview": "my-extension-preview.png"
```

> **Note:** Save preview images in PNG format.

### version

Optional. The version of your extension. Use [semantic versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`)
to communicate compatibility and changes clearly, for example `"1.0.0"`.

### author

Optional. The author or organization responsible for the extension.

## Example

```json
{
  "name": "My Visualization",
  "description": "A custom visualization for Qlik Cloud Analytics.",
  "preview": "my-visualization-preview.png",
  "type": "visualization",
  "version": "1.0.0",
  "author": "Example Corp"
}
```

![Extension preview in the assets panel](https://qlik.dev/_astro/ex_gen_ExtensionQextInfoLibrary-HelloWorld.BpL3P3vy.png)
