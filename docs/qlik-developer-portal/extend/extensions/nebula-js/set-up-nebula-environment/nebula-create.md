---
source: https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-create/
last_updated: 2026-06-02T18:15:45+01:00
---

# nebula create

Create a new nebula visualization.

## Usage

```bash
nebula create <name>
```

## Example

Create a nebula visualization project and do not install any dependencies yet

```bash
nebula create sn-table --install false
```

Create a nebula visualization project called `sn-table` with the `npm` package manager
instead of yarn

```bash
nebula create sn-table --pkgm npm
```

Create a nebula visualization project without a
[picasso.js](https://qlik.dev/extend/extensions/picasso-js/get-started/) template.

```bash
nebula create sn-table --picasso none
```

## Options

| Parameter                                        | Description                   | Default |
| ------------------------------------------------ | ----------------------------- | ------- |
| --version                                        | Show version number           |         |
| --install                                        | Run package installation step | true    |
| --pkgm string ("npm"\|"yarn")                    | Set package manager           | "yarn"  |
| --picasso string ("none"\|"minimal"\|"barchart") | Set picasso template          |         |
| --author string                                  | Set package author            |         |
| -h, --help                                       | Show help for command         |         |

## Details

Running nebula create without --picasso prompts a selection of the available
options.

- none: without the picasso.js template
- minimal: a basic setup of picasso.js is ready
- barchart: a bar chart component created by picasso.js is ready

To learn how to build a basic nebula visualization,
see the [Build a HelloWorld extension using nebula.js tutorial](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension/).
