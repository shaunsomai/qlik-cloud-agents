---
source: https://qlik.dev/toolkits/qlik-cli/qlik-cli-contexts/
last_updated: 2025-07-08T16:09:30Z
---

# Authenticate to Qlik using qlik-cli contexts

Connections to Qlik Cloud tenants or Qlik Sense Enterprise client-managed sites
is managed through the use of contexts. Each context specifies:

- The friendly name of the context (for example, Production Tenant)
- The hostname of the tenant (for example, [https://mytenant.eu.qlikcloud.com](https://mytenant.eu.qlikcloud.com))
- The credentials used to connect to the tenant
- Any user provided comments

## Introduction to contexts

By default the contexts are stored in a file in your `%HOME` folder,
which will differ depending on operating system.
On OSX it will for example be stored in `~/.qlik/contexts.yml` and on
MS Windows in `%userprofile%\.qlik\contexts.yml`.

> **Note:** If you want to override the default location of the context file,

you can specify the absolute path to the file in
the `$QLIK_CLI_USER_HOME_DIR` environment variable.

You can find more information regarding the available context commands in the [qlik-cli reference](https://qlik.dev/toolkits/qlik-cli/context/context).
Calling `qlik context init` will guide you through the configuration of the context,
and depending on authentication type the input needed will differ.
The input for some of the fields will be considered secrets,
and will not be displayed in the terminal or stored in the terminal buffer.

> **Note:** The init command also takes an optional context name as input.
> For example: `qlik context init my-context`. If provided this will be the name
> used for your context, otherwise a name based on your tenant URL will be used.

## Creating a new context for Qlik Cloud

Authentication to a Qlik Cloud tenant is done by providing the URL to the
tenant as well as an [API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key)
or [OAuth credentials](https://qlik.dev/authenticate/oauth).
To quickly get started, you can use the qlik-cli command `qlik context init` to
guide you through the process and store the details locally.

### Connecting to Qlik Cloud with OAuth

Using a context authenticated via OAuth will result in any calls being executed
under a bot user on the tenant. This is often preferable to using your personal
account as it provides separation between orchestration and your usage of the
tenant.

You will need to provide a *Client ID* and a *Client Secret* for a
machine-to-machine OAuth client on the tenant,
see [create an OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).

```text
Acquiring access to Qlik Cloud

Specify your tenant URL, usually in the form: https://<tenant>.<region>.qlikcloud.com
Where <tenant> is the name of the tenant and <region> is eu, us, ap, etc...
Enter tenant url: https://<tenant>.<region>.qlikcloud.com
Specify what type of authentication that should be used i.e API-Key (A) or OAuth (O). Default is API-Key (A)
A/O?: O

To complete this setup, you have to have a Client ID and Client Secret for OAuth.
If you're unsure, you can ask your tenant-admin or go to https://qlik.dev/toolkits/qlik-cli/get-started-qlik-cli.

Client ID: <my-client-id>

Client Secret: <my-client-secret>
```

### Connecting to Qlik Cloud with API key

If you wish to run calls under your personal user account, you can create a
context using an API key on that account. To create an API key,
see [generate your first API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key).

```text
$ qlik context init
Acquiring access to Qlik Cloud

Specify your tenant URL, usually in the form: https://<tenant>.<region>.qlikcloud.com
Where <tenant> is the name of the tenant and <region> is eu, us, ap, etc...
Enter tenant url: https://<tenant>.<region>.qlikcloud.com
Specify what type of authentication that should be used i.e API-Key (A) or OAuth (O). Default is API-Key (A).
A/O?: A

To complete this setup you have to have the 'developer' role and have
API-keys enabled. If you're unsure, you can ask your tenant-admin.
To generate a new API-key, go to https://mytenant.eu.qlikcloud.com/settings/api-keys

API-key: <my-api-key>
```

## Creating a new context for client-managed

A client-managed context requires a virtual proxy configured with JWT on the
client-managed site. See [using qlik-cli with client-managed](https://qlik.dev/toolkits/qlik-cli/qlik-cli-qrs-get-started).
