---
source: https://qlik.dev/toolkits/qlik-cli/get-started-qlik-cli/
last_updated: 2025-07-08T16:09:30Z
---

# Get started with qlik-cli examples

If you've already [installed qlik-cli](https://qlik.dev/toolkits/qlik-cli/install-qlik-cli) and [configured a context](https://qlik.dev/toolkits/qlik-cli/qlik-cli-contexts),
you can try it out with one of the following common use cases.

## List and switch between contexts

If you have multiple users or tenants, you can list and switch between them
through the contexts.

Listing the configured contexts

```bash
qlik context ls
```

Setting the context that should be used.

```bash
qlik context use <context-name>
```

Only one context can be configured as the current context.

> **Note:** The context to be used for a single command can also be overriden using the `--context` flag.

## Renaming and updating a context

If you want to rename an existing context

```bash
qlik context rename <old-context-name> <new-context-name>
```

It is also possible to update secrets in the context using the `qlik context update` command.
For example if you need to update the API-key of a context.

```bash
qlik context update <context-name> --api-key <my-api-key>
```

## Import a local app

Import a locally stored app to Qlik Cloud.

```bash
qlik app import -f the_app.qvf
```

More information about the app resource can be found in `qlik app --help`.

## Search for an app by name

Search for an app by name in Qlik Cloud.

```text
qlik item ls --resourceType app --name "app name"
```

More information about the app resource can be found in `qlik item --help`.

## Create a managed space and assign users

First you create the space and copy the returned ID.

```bash
qlik space create --name "Demo Space" --type managed --quiet
```

Then you assign a user with consumer, contributor, and publisher access by
supplying the ID returned by the first call.

```bash
qlik space assignment create --spaceId=<ID> --type user --roles consumer,contributor,publisher --assigneeId=<userid> -q
```

More information about the app resource can be found in `qlik space --help`.

## List failed reloads

To list your reloads for an app you enter:

```bash
qlik reload ls --appId=<appId>
```

Since this list can be large, you may wish to employ
some type of sorting or selection tool. [jq](https://stedolan.github.io/jq/) is
one such tool and can be used to filter out all `failed` reloads from the list.

```bash
qlik reload ls --appId=<appId> | jq '.[] | select(.status == "FAILED")'
```

More information about the app resource can be found in `qlik reload --help`.

## Analyze an app

With `qlik app meta`, you get an overview of the app with information about its
fields, tables, and associations.

```bash
qlik app meta --app <appid/app_name>
```

You can drill down even further and evaluate dimensions or measures.

```bash
qlik app eval --app <appid/app_name> 'Avg(Revenue)' by 'Country'
```

More information about the app resource can be found in `qlik app eval --help`.

## Limit the output to only return the `id`

Most commands return the full API response as json. If you are only
interested in the created or requested resource id, you can add the quiet flag
`--quiet` to suppress all but the ID output.
