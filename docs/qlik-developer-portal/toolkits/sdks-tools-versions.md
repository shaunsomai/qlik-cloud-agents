---
source: https://qlik.dev/toolkits/sdks-tools-versions/
last_updated: 2026-06-02T18:15:45+01:00
---

# SDKs and tools versioning

This section describes the versioning and lifecycle policy for Qlik Software Development Kits (SDKs), libraries, and
tools.

Qlik provides updates that may include support for new or updated Qlik APIs, new features, enhancements,
bug fixes, security patches, or documentation updates.
Updates may also address changes with dependencies, language runtimes, and operating systems.

Users are strongly encouraged to stay up-to-date with SDKs, libraries, and tools releases to stay current with the
latest features, security updates, and underlying dependencies.
Continued use of an unsupported SDK version is not recommended and is done at the user's discretion.

## Versioning

The Qlik SDK, library, and tooling release versions are based on the semantic versioning standard, in the form of X.Y.Z
where X represents the major version, Y is the minor, and Z is the patch.

An increase in the major version indicates that this SDK, library, or tool has undergone significant,
substantive changes to support new idioms and patterns in the language, and contains breaking changes
that are backwards incompatible with the latest version. Applications need to be updated to work
with the latest SDK, library, or tool version. It is important to update major versions with care,
following the upgrade guidelines provided by Qlik.

## Latest SDKs and tools versions

| SDK, library, or tool                                                    | Latest version                                                                                    | Latest release date                                                                                          | Release status |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------- |
| [qlik-api](https://qlik.dev/toolkits/qlik-api/)                          | ![qlik-api-version](https://img.shields.io/npm/v/@qlik/api.svg)                                   | ![qlik-api-release-date](https://img.shields.io/github/release-date/qlik-oss/qlik-api-ts)                    | Stable         |
| [qlik-embed-web-components](https://qlik.dev/embed/qlik-embed/)          | ![qlik-embed-web-components-version](https://img.shields.io/npm/v/@qlik/embed-web-components.svg) | ![qlik-embed-web-components-release-date](https://img.shields.io/npm/last-update/@qlik/embed-web-components) | Stable         |
| [qlik-embed-react](https://qlik.dev/embed/qlik-embed/)                   | ![qlik-embed-react-version](https://img.shields.io/npm/v/@qlik/embed-react.svg)                   | ![qlik-embed-react-release-date](https://img.shields.io/npm/last-update/@qlik/embed-react)                   | Stable         |
| [qlik-embed-svelte](https://qlik.dev/embed/qlik-embed/)                  | ![qlik-embed-svelte-version](https://img.shields.io/npm/v/@qlik/embed-svelte.svg)                 | ![qlik-embed-svelte-release-date](https://img.shields.io/npm/last-update/@qlik/embed-svelte)                 | Experimental   |
| [enigma-go](https://qlik.dev/toolkits/enigma-go/)                        | ![enigma-go-version](https://img.shields.io/github/v/release/qlik-oss/enigma-go.svg)              | ![enigma-go-release-date](https://img.shields.io/github/release-date/qlik-oss/enigma-go)                     | Stable         |
| [enigma.js](https://qlik.dev/toolkits/enigma-js/)                        | ![enigma-js-version](https://img.shields.io/npm/v/enigma.js.svg)                                  | ![enigma-js-release-date](https://img.shields.io/github/release-date/qlik-oss/enigma.js)                     | Stable         |
| [nebula.js](https://qlik.dev/embed/nebula/)                              | ![nebula-js-version](https://img.shields.io/npm/v/@nebula.js/stardust.svg)                        | ![nebula-js-release-date](https://img.shields.io/npm/last-update/@nebula.js/stardust)                        | Stable         |
| [picasso.js](https://qlik.dev/extend/extensions/picasso-js/get-started/) | ![picasso-js-version](https://img.shields.io/npm/v/picasso.js.svg)                                | ![picasso-js-release-date](https://img.shields.io/npm/last-update/picasso.js)                                | Stable         |
| [Qlik Sense .Net](https://qlik.dev/toolkits/net-sdk/)                    | ![net-sdk-version](https://img.shields.io/nuget/v/QlikSense.NetSDK)                               | ![net-sdk-reelease-date](https://img.shields.io/badge/release_date-november_2024-green)                      | Stable         |
| [Platform SDK](https://qlik.dev/toolkits/platform-sdk/)                  | ![qlik-sdk-version](https://img.shields.io/pypi/v/qlik-sdk.svg)                                   | ![qlik-sdk-release-date](https://img.shields.io/badge/release_date-september_2023-red)                       | Experimental   |
| [qlik-cli](https://qlik.dev/toolkits/qlik-cli/)                          | ![qlik-cli-version](https://img.shields.io/github/v/release/qlik-oss/qlik-cli.svg)                | ![qlik-cli-release-date](https://img.shields.io/github/release-date/qlik-oss/qlik-cli)                       | Stable         |

## Discontinued SDKs and tools

| SDK, library, or tool | Latest version                                                           | Deprecated                                                                         | End of life                                                                           |
| --------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| qlik/sdk              | ![qlik-sdk-version](https://img.shields.io/badge/release-v0.28.0-orange) | [May 25, 2024](https://qlik.dev/changelog/88-typescript-platform-sdk-deprecation/) | [March 27, 2025](https://qlik.dev/changelog/129-typescript-platform-sdk-end-of-life/) |
