---
source: https://qlik.dev/toolkits/qlik-cli/qlik-cli-escaping/
last_updated: 2026-03-18T17:22:12Z
---

# Handle character escaping in qlik-cli

Proper character escaping is essential for working with qlik-cli, especially when passing JSON payloads or filter
expressions.

Escaping syntax depends primarily on your shell and, for PowerShell, on the PowerShell version.
This guide covers the `--filter` and `--body` options.

## Prerequisites

- qlik-cli installed and configured
- A context set up for authentication
- Familiarity with JSON and OData syntax

## Escape quotes in the `--filter` option

The `--filter` option uses OData syntax.

Example expression: `subject eq "user@example.com"`

All examples in the [Filter examples](#filter-examples) section produce this expression.

When filtering by `subject`, retrieve the `subject` value:

```bash
qlik user ls
```

Then, copy the `subject` value exactly as returned and escape it according to your shell.

The subject format varies depending on the identity type. Examples include:

- `user@example.com`
- `auth0|8d2626094d70ac63e5492d2eac494197adac5ec3755b044b79417c4e2ca43e76`
- `qlikbot\\fbf637de84ab48c1b8da767a9025a714`

### Filter examples

In PowerShell 7, use single quotes for the full filter expression:

```powershell
qlik user ls --filter 'subject eq "user@example.com"'
```

If you need to use a variable, use the format operator:

```powershell
$subject = "user@example.com"
qlik user ls --filter ('subject eq "{0}"' -f $subject)
```

In PowerShell 5, use doubled double quotes around the filter value:

```powershell
qlik user ls --filter 'subject eq ""user@example.com""'
```

If you need to use a variable, use the format operator:

```powershell
$subject = "user@example.com"
qlik user ls --filter ('subject eq ""{0}""' -f $subject)
```

> **Note:** You can also use `ConvertTo-Json` to build the filter argument when quoting becomes difficult:
>
> ```powershell
> $subject = "user@example.com"
> qlik user ls --filter $("subject eq `"$subject`"" | ConvertTo-Json)
> ```
>
> This can help in more complex variable-based scenarios, but the format operator example is usually easier to read.

In Bash, escape the inner double quotes with backslashes:

```bash
qlik user ls --filter "subject eq \"user@example.com\""
```

## Escape quotes in the `--body` option

When using the `--body` option with JSON payloads in commands like `qlik user patch` or `qlik raw patch`,
proper escaping rules depend on your shell.

> **Note:** The `qlik user patch` and `qlik raw patch` commands expect a user ID, for example `696el7cb6df8986cde32kia6`,
> not a `subject` value.
> To get the user ID, run `qlik user ls`.

### Body examples

In PowerShell 7, use valid JSON inside single quotes:

```powershell
$userId = "<userId>"

qlik user patch $userId --body '[{"op":"replace","path":"/email","value":"user@example.com"}]'
```

In PowerShell 5, single quotes and double-quote escaping do not work reliably for `--body` payloads.

Instead, use the `ConvertTo-Json` approach to generate and escape the JSON before passing it to `--body`:

```powershell
$userId = "<userId>"

$body = @(
  @{
    op    = "replace"
    path  = "/email"
    value = "user@example.com"
  }
)

$json = ConvertTo-Json -InputObject $body -Compress
$escapedJson = ConvertTo-Json -InputObject $json -Compress

qlik user patch $userId --body $escapedJson
```

The first `ConvertTo-Json` call creates the JSON Patch array.\
The second `ConvertTo-Json` call escapes that JSON so PowerShell 5 passes it correctly to `qlik-cli`.

In Bash, escape the inner JSON quotes with backslashes:

```bash
qlik user patch <userId> --body "[{\"op\":\"replace\",\"path\":\"/email\",\"value\":\"user@example.com\"}]"
```

For better readability with longer payloads, you can use line continuation with backslash:

```bash
qlik user patch <userId> \
  --body "[{\"op\":\"replace\",\"path\":\"/email\",\"value\":\"user@example.com\"}]"
```

You can use the same pattern with `qlik raw`, for example:

```bash
qlik raw patch v1/users/696el7cb6df8986cde32kia6 \
  --body "[{\"op\":\"replace\",\"path\":\"/name\",\"value\":\"Jane Doe\"}]"
```

## Avoid escaping issues

For scripts and more complex payloads, using a file is often easier than inline escaping.

```bash
qlik user patch <userId> --file patch.json
```

Example `patch.json` file:

```json
[
  {
    "op": "replace",
    "path": "/name",
    "value": "Jane Doe"
  }
]
```

This approach works reliably across shells.

## Verify your escaping with `--verbose`

If a command fails or you're unsure about your syntax, use the `--verbose` option to see the actual payload being sent
to the server.
This helps verify that your escaping is correct.

The output will show the formatted JSON payload and the server response, for example:

```text
PATCH https://<tenant>/api/v1/users/<userId>
...
PAYLOAD:
[
  {
    "op": "replace",
    "path": "/name",
    "value": "Jane Doe"
  }
]
...
Status: 204 No Content
Empty response body
```

> **Tip:** If the payload doesn't look correct, adjust your escaping and run the command again.
