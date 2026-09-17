---
source: https://qlik.dev/toolkits/qlik-cli/install-qlik-cli/
last_updated: 2025-07-08T16:09:30Z
---

# Get started

qlik-cli is available for Mac, Linux and Windows, via package manager or for manual
install.

## Install qlik-cli

From a command-line, use a package manager or download and extract the archive file for your operating system to install qlik-cli.

### Install with a package manager

To install qlik-cli with [chocolatey](https://chocolatey.org), run:

```bash
choco install qlik-cli
```

To upgrade:

```bash
choco upgrade qlik-cli
```

And you're up to date.

**Choco upgrade failure troubleshooting**

If you see an error like:

```powershell
Error retrieving packages from source 'https://www.nuget.org/api/v2':
The combination of parameters provided to this OData endpoint is no longer supported.
Please refer to the following URL for more information about this deprecation: https://aka.ms/nuget/odata-deprecation
```

Then first run:

```powershell
choco source list
```

Then remove the one matching nuget.org:

```powershell
choco source rm --name=nuget.org
```

Another way to fix a failing upgrade is to uninstall and reinstall.

```powershell
choco uninstall qlik-cli
choco install qlik-cli
```

To install qlik-cli with [homebrew](https://brew.sh), you need to first tap
our [qlik-oss/taps](https://github.com/qlik-oss/homebrew-taps) if you haven't already:

```bash
brew tap qlik-oss/taps
```

After the tap has been tapped, you can install the tool with:

```bash
brew install qlik-cli
```

> **Note:** This will work for Mac or Linux (where you can use `linuxbrew`) and Windows Subsystem Linux (WSL).

### Install manually

If you prefer to manually install qlik-cli on Windows:

1. Download the latest `qlik-Windows-x86_64.zip` from [GitHub](https://github.com/qlik-oss/qlik-cli/releases).
2. Unzip the `qlik-Windows-x86_64.zip` file.
3. Move the `qlik.exe` binary to a location where you can execute it.
4. Add the path to the `qlik.exe` file to your `Path` environment variable.

If you prefer to manually install qlik-cli on macOS:

1. Download the latest `qlik-Darwin-x86_64.tar.gz` from [GitHub](https://github.com/qlik-oss/qlik-cli/releases).
2. Unzip the file: `tar -xvf qlik-Darwin-x86_64.tar.gz`.
3. Move the `qlik` binary to a location where you can execute it.

If you prefer to manually install qlik-cli on Linux:

1. Download the latest `qlik-Linux-x86_64.tar.gz` from [GitHub](https://github.com/qlik-oss/qlik-cli/releases).
2. Unzip the file: `tar -xvf qlik-Linux-x86_64.tar.gz`.
3. Move the `qlik` binary to a location where you can execute it.
4. Add the path to the `qlik` binary to your execution path.

## Enable completion feature

To make it easier to write commands, consider
enabling [completion](https://qlik.dev/toolkits/qlik-cli/completion/completion) which generates auto completion scripts for bash or zsh.

## Third-party dependencies

The tool uses [third-party dependencies](https://github.com/qlik-oss/qlik-cli/blob/master/third-party-dependencies.md).
